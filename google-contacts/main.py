import csv
from typing import List, Dict


def read_google_contacts(csv_file_path: str) -> List[Dict]:
    """
    Read Google Contacts CSV export file and parse into list of dictionaries.

    Args:
        csv_file_path: Path to the Google Contacts CSV export file

    Returns:
        A list of dictionaries, where each dictionary represents a contact
    """
    # Write your code here
    data = []
    with open(csv_file_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data

def add_contacts_to_groups(contacts: List[Dict], group_assignments: Dict[str, str]) -> List[Dict]:
    """
    Add contacts to specified groups.

    Args:
        contacts: List of contact dictionaries
        group_assignments: Dictionary mapping email addresses to group names

    Returns:
        Modified list of contacts with group memberships updated
    """
    # Write your code here
    new_contacts = []
    for contact in contacts:
        email = contact["Email"]
        if email in group_assignments.keys():
            group = group_assignments[email]
            contact["Group Membership"] = group
        new_contacts.append(contact)
    return new_contacts

def write_google_contacts(contacts: List[Dict], output_file: str) -> None:
    """
    Write contacts back to CSV file for import into Google Contacts.

    Args:
        contacts: List of contact dictionaries
        output_file: Path to the output CSV file
    """
    # Write your code here
    with open(output_file, "w") as f:
        fieldnames = contacts[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)

def search_contacts_by_name(contacts: List[Dict], name: str) -> List[Dict]:
    """
    Search for contacts by name (case-insensitive partial match).

    Args:
        contacts: List of contact dictionaries
        name: Name or partial name to search for

    Returns:
        List of contacts matching the search criteria
    """
    # Write your code here
    output = []
    for contact in contacts:
        if name.upper() in contact["Name"].upper():
            output.append(contact)
    return output


def search_contacts_by_group(contacts: List[Dict], group: str) -> List[Dict]:
    """
    Search for contacts by group membership.

    Args:
        contacts: List of contact dictionaries
        group: Group name to search for

    Returns:
        List of contacts in the specified group
    """
    # Write your code here
    output = []
    for contact in contacts:
        if contact["Group Membership"] == group:
            output.append(contact)
    return output

if __name__ == "__main__":
    # setup
    data = []
    data1 = {}
    fieldnames = None
    with open("BrawlStars - Sheet 1.csv", "r") as f:
        reader = csv.DictReader(f)
        fieldnames = ["Name", "Phone", "Email", "Group Membership"]
        for row in reader:
            del row["Quote"]
            del row["Rarity"]
            data.append(row)
            data1[row["Email"]] = row["Group Membership"]
    
    with open("notmygooglecontacts.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            row["Group Membership"] = ""
            writer.writerow(row)
    
    # testing
    data = read_google_contacts("notmygooglecontacts.csv")
    data_final = add_contacts_to_groups(data, data1)
    write_google_contacts(data_final, "stillnotmygooglecontacts.csv")
