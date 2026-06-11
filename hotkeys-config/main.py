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
    # read the file
    lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
    
    output = {}
    current_category = "Unclassified"
    i = 0
    while i < len(lines):
        # remove \n
        lines[i] = lines[i].strip("\n")
        if lines[i] == "":
            del lines[i]
        else:
            # identify headers
            if lines[i][0] == "[":
                cat_name = lines[i][1:-1]
                output[cat_name] = {}
                current_category = cat_name
            else:
                # split up key and value
                key, value = lines[i].split(" = ")
                if "," in value:
                    value = value.split(",")
                output[current_category][key] = value
                
            i += 1
    
    return output


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
    # TODO: verify that keys within are not invalid
    if not validate_key_combination(key):
        raise InvalidKeyException("invalid hotkey combination")

    # verified -> put it in
    if category not in config:
        config[category] = {action:""}
    config[category][action] = key
    return config


def save_config_file(config: Dict[str, Dict[str, str]], file_path: str) -> None:
    """
    Save configuration to a file.

    Args:
        config: The configuration dictionary
        file_path: Path to save the configuration file
    """
    # Write your code here
    with open(file_path, "w") as f:
        for category in config.keys():
            f.write(f"\n[{category}]\n")
            for action in config[category].keys():
                if type(config[category][action]) == list:
                    key = ",".join(config[category][action])
                else:
                    key = config[category][action]
                f.write(f"{action} = {key}\n")
            f.write("\n")


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
    try:
        return config[category][action]
    except KeyError:
        return None


def validate_key_combination(key: str) -> bool:
    """
    Validate if a key combination is valid.

    Args:
        key: The key combination to validate

    Returns:
        True if valid, False otherwise
    """
    # Write your code here
    SPECIAL_KEYS = [
        "CAPSLOCK", "ENTER", "SPACE", "TAB", "RETURN", "ESC", "BS", "SHIFT",
        "SCROLLLOCK", "DEL", "INS", "HOME", "END", "PGUP", "PGDN", "UP", "DOWN", "LEFT", "RIGHT",
        "NUM_0", "NUM_1", "NUM_2", "NUM_3", "NUM_4", "NUM_5", "NUM_6", "NUM_7", "NUM_8", "NUM_9", "NUM_DOT",
        "NUM_INS", "NUM_END", "NUM_DOWN", "NUM_PGDN", "NUM_LEFT", "NUM_CLEAR", "NUM_RIGHT", "NUM_HOME", "NUM_UP", "NUM_PGUP", "NUM_DEL",
        "NUM_LOCK", "NUM_DIV", "NUM_MULT", "NUM_ADD", "NUM_SUB", "NUM_ENTER",
        "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12",
        "F13", "F14", "F15", "F16", "F17", "F18", "F19", "F20", "F21", "F22", "F23", "F24",
        "WIN", "CTRL", "COMMAND", "ALT", "OPTION", "SHIFT",
        "BROWSER_BACK", "BROWSER_FORWARD", "BROWSER_REFRESH", "BROWSER_STOP", "BROWSER_SEARCH", "BROWSER_FAVOURITES", "BROWSER_HOME",
        "VOLUME_MUTE", "VOLUME_DOWN", "VOLUME_UP", "MEDIA_NEXT", "MEDIA_PREV", "MEDIA_STOP", "MEDIA_PLAY_PAUSE",
        "LAUNCH_MAIL", "LAUNCH_MEDIA", "LAUNCh_APP1", "LAUNCH_APP2"
        "MENU", "PRT_SC", "CTRL_BREAK", "PAUSE", "BREAK", "HELP", "SLEEP"
    ]
    checklist = key.upper().split("+")
    checked = []
    for item in checklist:
        if not (item.isalnum() or item in SPECIAL_KEYS) or item in checked:
            return False
        checked.append(item)
    return True


def list_categories(config: Dict[str, Dict[str, str]]) -> list:
    """
    List all categories in the configuration.

    Args:
        config: The configuration dictionary

    Returns:
        A list of category names
    """
    # Write your code here
    return list(config.keys())


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
    return list(config[category].keys())

if __name__ == "__main__":
    data = parse_config_file("hotkeys.cfg")
    print(data)
    data = set_hotkey(data, "global", "abandon", "A") #/
    data = set_hotkey(data, "useless", "shutdown", "S") #/
    data = set_hotkey(data, "scenedit_maintoolbar", "russian_roulette", "R") #?
    data = set_hotkey(data, "scenedit_maintoolbar", "fastforward", "SHIFT+F") #X
    data = set_hotkey(data, "aidebug", "settings", "S+E+T+I+N+G") #/
    print(data)
    save_config_file(data, "completelyrubbishhotkeys.cfg")