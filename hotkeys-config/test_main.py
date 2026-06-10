import unittest
import os
import tempfile
from typing import Dict

from main import (
    parse_config_file,
    set_hotkey,
    save_config_file,
    get_hotkey,
    validate_key_combination,
    list_categories,
    list_actions_in_category,
    InvalidKeyException
)


class TestHotkeysConfig(unittest.TestCase):

    def setUp(self):
        """Create a sample config file for testing"""
        self.sample_config = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.cfg')
        self.sample_config_path = self.sample_config.name

        # Write sample config data
        self.sample_config.write('[movement]\n')
        self.sample_config.write('move_forward = W\n')
        self.sample_config.write('move_backward = S\n')
        self.sample_config.write('move_left = A\n')
        self.sample_config.write('move_right = D\n')
        self.sample_config.write('\n')
        self.sample_config.write('[combat]\n')
        self.sample_config.write('attack = SPACE\n')
        self.sample_config.write('block = SHIFT\n')
        self.sample_config.write('use_item = E\n')

        self.sample_config.close()

    def tearDown(self):
        """Clean up test files"""
        if os.path.exists(self.sample_config_path):
            os.remove(self.sample_config_path)

    def test_parse_config_file_returns_dict(self):
        """Test that parsing config returns a dictionary"""
        config = parse_config_file(self.sample_config_path)
        self.assertIsInstance(config, dict)

    def test_parse_config_file_structure(self):
        """Test that config has the expected nested structure"""
        config = parse_config_file(self.sample_config_path)

        # Should have expected categories
        self.assertIn('movement', config)
        self.assertIn('combat', config)

        # Categories should be dictionaries
        self.assertIsInstance(config['movement'], dict)
        self.assertIsInstance(config['combat'], dict)

    def test_parse_config_file_content(self):
        """Test that config content is parsed correctly"""
        config = parse_config_file(self.sample_config_path)

        self.assertEqual(config['movement']['move_forward'], 'W')
        self.assertEqual(config['movement']['move_backward'], 'S')
        self.assertEqual(config['combat']['attack'], 'SPACE')

    def test_set_hotkey_modifies_config(self):
        """Test that setting a hotkey modifies the configuration"""
        config = parse_config_file(self.sample_config_path)
        modified = set_hotkey(config, 'movement', 'move_forward', 'UP')

        self.assertEqual(modified['movement']['move_forward'], 'UP')

    def test_set_hotkey_creates_new_category(self):
        """Test that setting a hotkey creates a new category if needed"""
        config = parse_config_file(self.sample_config_path)
        modified = set_hotkey(config, 'new_category', 'new_action', 'Q')

        self.assertIn('new_category', modified)
        self.assertEqual(modified['new_category']['new_action'], 'Q')

    def test_get_hotkey_existing(self):
        """Test getting an existing hotkey"""
        config = parse_config_file(self.sample_config_path)
        key = get_hotkey(config, 'movement', 'move_forward')

        self.assertEqual(key, 'W')

    def test_get_hotkey_nonexistent(self):
        """Test getting a non-existent hotkey"""
        config = parse_config_file(self.sample_config_path)
        key = get_hotkey(config, 'movement', 'nonexistent_action')

        self.assertIsNone(key)

    def test_save_config_file_creates_file(self):
        """Test that saving config creates a valid file"""
        config = parse_config_file(self.sample_config_path)
        output_file = tempfile.NamedTemporaryFile(delete=False, suffix='.cfg')
        output_path = output_file.name
        output_file.close()

        try:
            save_config_file(config, output_path)
            self.assertTrue(os.path.exists(output_path))

            # Verify content
            with open(output_path, 'r') as f:
                content = f.read()
                self.assertIn('[movement]', content)
                self.assertIn('move_forward', content)

            # Verify it can be parsed back
            reread_config = parse_config_file(output_path)
            self.assertEqual(reread_config['movement']['move_forward'], 'W')

        finally:
            if os.path.exists(output_path):
                os.remove(output_path)

    def test_list_categories(self):
        """Test listing all categories"""
        config = parse_config_file(self.sample_config_path)
        categories = list_categories(config)

        self.assertIsInstance(categories, list)
        self.assertIn('movement', categories)
        self.assertIn('combat', categories)

    def test_list_actions_in_category(self):
        """Test listing actions in a category"""
        config = parse_config_file(self.sample_config_path)
        actions = list_actions_in_category(config, 'movement')

        self.assertIsInstance(actions, list)
        self.assertIn('move_forward', actions)
        self.assertIn('move_backward', actions)

    def test_roundtrip_consistency(self):
        """Test that parse -> save -> parse produces consistent results"""
        original_config = parse_config_file(self.sample_config_path)

        output_file = tempfile.NamedTemporaryFile(delete=False, suffix='.cfg')
        output_path = output_file.name
        output_file.close()

        try:
            save_config_file(original_config, output_path)
            reread_config = parse_config_file(output_path)

            # Should have same categories
            self.assertEqual(set(original_config.keys()), set(reread_config.keys()))

            # Should have same values
            for category in original_config:
                self.assertEqual(original_config[category], reread_config[category])

        finally:
            if os.path.exists(output_path):
                os.remove(output_path)

    def test_validate_key_combination_valid(self):
        """Test validation of valid key combinations"""
        # Test various valid key combinations
        valid_keys = ['W', 'A', 'S', 'D', 'SPACE', 'SHIFT', 'CTRL', 'ALT', 'F1', 'NUMPAD1']

        for key in valid_keys:
            result = validate_key_combination(key)
            self.assertTrue(result, f'Key {key} should be valid')

    def test_validate_key_combination_invalid(self):
        """Test validation of invalid key combinations"""
        # Test invalid key combinations
        invalid_keys = ['', '   ', 'INVALID_KEY_NAME_123456789']

        for key in invalid_keys:
            result = validate_key_combination(key)
            self.assertFalse(result, f'Key {key} should be invalid')

    def test_parse_config_structure_valid(self):
        """Test that parsed config always has valid structure"""
        config = parse_config_file(self.sample_config_path)

        # Result is always a dict
        assert isinstance(config, dict)

        # All values are dicts
        for category in config.values():
            assert isinstance(category, dict)

            # All keys and values are strings
            for key, value in category.items():
                assert isinstance(key, str)
                assert isinstance(value, str)

    def test_set_hotkey_preserves_structure(self):
        """Test that setting hotkeys preserves valid structure"""
        config = parse_config_file(self.sample_config_path)
        modified = set_hotkey(config, 'test_category', 'test_action', 'Q')

        # Result is still a dict
        assert isinstance(modified, dict)

        # All categories remain dicts
        for cat in modified.values():
            assert isinstance(cat, dict)

    def test_roundtrip_preserves_data(self):
        """Test that roundtrip preserves all data"""
        original = parse_config_file(self.sample_config_path)

        # Save and reread
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.cfg')
        temp_path = temp_file.name
        temp_file.close()

        try:
            save_config_file(original, temp_path)
            reread = parse_config_file(temp_path)

            # All data preserved
            assert original == reread

        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)


if __name__ == '__main__':
    unittest.main()
