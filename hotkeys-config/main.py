import os
from typing import Dict, Optional


class InvalidKeyException(Exception):
    """Exception raised when an invalid key combination is provided"""
    pass


def parse_config_file(file_path: str) -> Dict[str, Dict[str, str]]:
    """
    Parse a configuration file into a nested dictionary structure.

    Args:
        file_path: Path to the configuration file

    Returns:
        A nested dictionary with categories as top-level keys and
        key-value pairs as inner dictionaries
    """
    # Write your code here
    pass


def set_hotkey(config: Dict[str, Dict[str, str]], category: str, action: str, key: str) -> Dict[str, Dict[str, str]]:
    """
    Set a hotkey in the configuration.

    Args:
        config: The configuration dictionary
        category: The category name
        action: The action name
        key: The key binding

    Returns:
        The modified configuration dictionary

    Raises:
        InvalidKeyException: If the key combination is invalid
    """
    # Write your code here
    pass


def save_config_file(config: Dict[str, Dict[str, str]], file_path: str) -> None:
    """
    Save configuration to a file.

    Args:
        config: The configuration dictionary
        file_path: Path to save the configuration file
    """
    # Write your code here
    pass


def get_hotkey(config: Dict[str, Dict[str, str]], category: str, action: str) -> Optional[str]:
    """
    Get a hotkey from the configuration.

    Args:
        config: The configuration dictionary
        category: The category name
        action: The action name

    Returns:
        The key binding, or None if not found
    """
    # Write your code here
    pass


def validate_key_combination(key: str) -> bool:
    """
    Validate if a key combination is valid.

    Args:
        key: The key combination to validate

    Returns:
        True if valid, False otherwise
    """
    # Write your code here
    pass


def list_categories(config: Dict[str, Dict[str, str]]) -> list:
    """
    List all categories in the configuration.

    Args:
        config: The configuration dictionary

    Returns:
        A list of category names
    """
    # Write your code here
    pass


def list_actions_in_category(config: Dict[str, Dict[str, str]], category: str) -> list:
    """
    List all actions in a specific category.

    Args:
        config: The configuration dictionary
        category: The category name

    Returns:
        A list of action names in the category
    """
    # Write your code here
    pass
