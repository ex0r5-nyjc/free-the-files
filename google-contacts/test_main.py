import unittest
import csv
import os
import tempfile
from typing import List, Dict

from main import (
    read_google_contacts,
    add_contacts_to_groups,
    write_google_contacts,
    search_contacts_by_name,
    search_contacts_by_group
)


class TestGoogleContacts(unittest.TestCase):

    def setUp(self):
        """Create a sample CSV file for testing"""
        self.sample_csv = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv')
        self.sample_csv_path = self.sample_csv.name

        # Write sample Google Contacts CSV data
        fieldnames = ['Name', 'Email', 'Phone', 'Group Membership']
        writer = csv.DictWriter(self.sample_csv, fieldnames=fieldnames)
        writer.writeheader()

        writer.writerow({
            'Name': 'John Doe',
            'Email': 'john@example.com',
            'Phone': '123-456-7890',
            'Group Membership': 'Friends ::: Co-workers'
        })
        writer.writerow({
            'Name': 'Jane Smith',
            'Email': 'jane@example.com',
            'Phone': '234-567-8901',
            'Group Membership': 'Family'
        })
        writer.writerow({
            'Name': 'Bob Johnson',
            'Email': 'bob@example.com',
            'Phone': '345-678-9012',
            'Group Membership': ''
        })

        self.sample_csv.close()

    def tearDown(self):
        """Clean up test files"""
        if os.path.exists(self.sample_csv_path):
            os.remove(self.sample_csv_path)

    def test_read_google_contacts_returns_list(self):
        """Test that reading Google Contacts returns a list"""
        contacts = read_google_contacts(self.sample_csv_path)
        self.assertIsInstance(contacts, list)

    def test_read_google_contacts_structure(self):
        """Test that contacts have the expected dictionary structure"""
        contacts = read_google_contacts(self.sample_csv_path)

        if len(contacts) > 0:
            first_contact = contacts[0]
            self.assertIsInstance(first_contact, dict)

            # Should have expected fields
            expected_fields = ['Name', 'Email', 'Phone', 'Group Membership']
            for field in expected_fields:
                self.assertIn(field, first_contact)

    def test_read_google_contacts_count(self):
        """Test that all contacts are read"""
        contacts = read_google_contacts(self.sample_csv_path)
        self.assertEqual(len(contacts), 3)

    def test_add_contacts_to_groups_returns_list(self):
        """Test that adding to groups returns a list"""
        contacts = read_google_contacts(self.sample_csv_path)
        group_assignments = {
            'john@example.com': 'New Group',
            'jane@example.com': 'Family'
        }

        result = add_contacts_to_groups(contacts, group_assignments)
        self.assertIsInstance(result, list)

    def test_add_contacts_to_groups_modifies_group_membership(self):
        """Test that group memberships are actually modified"""
        contacts = read_google_contacts(self.sample_csv_path)
        group_assignments = {
            'bob@example.com': 'New Group'
        }

        result = add_contacts_to_groups(contacts, group_assignments)

        # Find Bob's contact and check if group was added
        bob_contact = next((c for c in result if c.get('Email') == 'bob@example.com'), None)
        self.assertIsNotNone(bob_contact)
        self.assertIn('New Group', bob_contact.get('Group Membership', ''))

    def test_write_google_contacts_creates_file(self):
        """Test that writing contacts creates a valid CSV file"""
        contacts = read_google_contacts(self.sample_csv_path)
        output_file = tempfile.NamedTemporaryFile(delete=False, suffix='.csv')
        output_path = output_file.name
        output_file.close()

        try:
            write_google_contacts(contacts, output_path)
            self.assertTrue(os.path.exists(output_path))

            # Verify it's valid CSV
            with open(output_path, 'r') as f:
                reader = csv.DictReader(f)
                rows = list(reader)
                self.assertEqual(len(rows), 3)
        finally:
            if os.path.exists(output_path):
                os.remove(output_path)

    def test_search_contacts_by_name(self):
        """Test searching contacts by name"""
        contacts = read_google_contacts(self.sample_csv_path)

        results = search_contacts_by_name(contacts, 'John')
        self.assertIsInstance(results, list)
        self.assertGreater(len(results), 0)

        # Should find John Doe
        john_found = any('John' in c.get('Name', '') for c in results)
        self.assertTrue(john_found)

    def test_search_contacts_by_group(self):
        """Test searching contacts by group"""
        contacts = read_google_contacts(self.sample_csv_path)

        results = search_contacts_by_group(contacts, 'Family')
        self.assertIsInstance(results, list)

        # Should find Jane Smith (in Family group)
        jane_found = any('Jane' in c.get('Name', '') for c in results)
        self.assertTrue(jane_found)

    def test_roundtrip_consistency(self):
        """Test that read -> write -> read produces consistent results"""
        # Read original contacts
        original_contacts = read_google_contacts(self.sample_csv_path)

        # Write to temp file
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.csv')
        temp_path = temp_file.name
        temp_file.close()

        try:
            write_google_contacts(original_contacts, temp_path)
            reread_contacts = read_google_contacts(temp_path)

            # Should have same number of contacts
            self.assertEqual(len(original_contacts), len(reread_contacts))
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

    def test_read_google_contacts_structure_valid(self):
        """Test that result structure is always valid"""
        contacts = read_google_contacts(self.sample_csv_path)

        # Result is always a list
        assert isinstance(contacts, list)

        # All items are dictionaries
        for contact in contacts:
            assert isinstance(contact, dict)

            # Each contact has Name and Email fields
            assert 'Name' in contact or 'Email' in contact

    def test_add_contacts_preserves_count(self):
        """Test that adding groups doesn't change contact count"""
        contacts = read_google_contacts(self.sample_csv_path)
        original_count = len(contacts)

        group_assignments = {'john@example.com': 'Test Group'}
        result = add_contacts_to_groups(contacts, group_assignments)

        # Number of contacts should remain the same
        assert len(result) == original_count


if __name__ == '__main__':
    unittest.main()
