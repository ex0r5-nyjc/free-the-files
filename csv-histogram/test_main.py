import unittest
import os
from typing import Dict

from main import process_survey_data, write_histogram_to_file, create_visual_bar_chart


class TestCSVAistogram(unittest.TestCase):

    def test_process_survey_data_file_exists(self):
        """Test that the function can process the actual survey data file"""
        result = process_survey_data("basicpythonnotessurvey.csv")
        self.assertIsInstance(result, dict, "Result should be a dictionary")

    def test_process_survey_data_structure(self):
        """Test that the returned data has the expected structure"""
        result = process_survey_data("basicpythonnotessurvey.csv")

        # Should have at least the main categories
        expected_categories = ['functions', 'strings', 'lists']
        for category in expected_categories:
            self.assertIn(category, result, f"Should contain {category} category")
            self.assertIsInstance(result[category], dict, f"{category} should be a dictionary")

    def test_process_survey_data_counts(self):
        """Test that vote counts are positive integers"""
        result = process_survey_data("basicpythonnotessurvey.csv")

        for category, items in result.items():
            for item, count in items.items():
                self.assertIsInstance(count, int, f"Count for {category}.{item} should be an integer")
                self.assertGreater(count, 0, f"Count for {category}.{item} should be positive")
                self.assertLessEqual(count, 15, f"Count for {category}.{item} seems too high (max 15 responses)")

    def test_process_survey_data_specific_entries(self):
        """Test specific known entries from the survey data"""
        result = process_survey_data("basicpythonnotessurvey.csv")

        # These are based on the actual data in the CSV file
        # Test a few specific entries that should exist
        self.assertIn('functions', result)
        self.assertIn('strings', result)
        self.assertIn('lists', result)

    def test_process_survey_data_completeness(self):
        """Test that all data is processed (no empty categories)"""
        result = process_survey_data("basicpythonnotessurvey.csv")

        total_entries = sum(len(items) for items in result.values())
        self.assertGreater(total_entries, 0, "Should have at least some entries")
        self.assertGreater(total_entries, 10, "Should have many entries across all categories")

    def test_process_survey_data_result_structure(self):
        """Test that result structure is always valid"""
        result = process_survey_data("basicpythonnotessurvey.csv")

        # Result is always a dict
        assert isinstance(result, dict)

        # All values are dicts
        for category in result.values():
            assert isinstance(category, dict)

            # All counts are positive integers
            for item, count in category.items():
                assert isinstance(count, int)
                assert count > 0

    def test_write_histogram_to_file(self):
        """Test that histogram data can be written to file"""
        histogram_data = process_survey_data("basicpythonnotessurvey.csv")
        output_file = "test_output.txt"

        try:
            write_histogram_to_file(histogram_data, output_file)

            # Check file was created and has content
            with open(output_file, 'r') as f:
                content = f.read()
                self.assertGreater(len(content), 0, "Output file should have content")
                self.assertIn('functions', content.lower(), "Output should contain functions category")
        finally:
            # Clean up test file
            if os.path.exists(output_file):
                os.remove(output_file)

    def test_create_visual_bar_chart(self):
        """Test that visual bar chart can be created"""
        histogram_data = process_survey_data("basicpythonnotessurvey.csv")
        chart = create_visual_bar_chart(histogram_data)

        self.assertIsInstance(chart, str, "Chart should be a string")
        self.assertGreater(len(chart), 0, "Chart should have content")
        self.assertIn('#', chart, "Chart should contain the bar symbol")

    def test_create_visual_bar_chart_custom_symbol(self):
        """Test that visual bar chart can be created with custom symbol"""
        histogram_data = process_survey_data("basicpythonnotessurvey.csv")
        chart = create_visual_bar_chart(histogram_data, symbol='*')

        self.assertIn('*', chart, "Chart should contain the custom symbol")


if __name__ == '__main__':
    unittest.main()
