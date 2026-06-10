# Objective

This assignment is practice to be comfortable **parsing configuration files and managing key-value data structures**.

----------

# Hotkeys Configuration: Parsing .cfg Files

## Task: Parse Configuration File

Some games allow players to customize the hotkeys for various actions through a configuration file. A configuration follows a certain format:

```
[category]
key = value
```

The file `hotkeys.cfg` has its hotkey configuration organized by category, with each hotkey appearing in a particular category.

### Part 1: Parse Configuration File

Write a function `parse_config_file(file_path: str) -> dict` that:
- takes in a file path to a `.cfg` file
- reads and parses the configuration file
- returns a dictionary structure that enables looking up the hotkey for a particular action in a particular category

**Example output**

The returned dictionary should look like:

```python
{
    'movement': {
        'move_forward': 'W',
        'move_backward': 'S',
        'move_left': 'A',
        'move_right': 'D'
    },
    'combat': {
        'attack': 'SPACE',
        'block': 'SHIFT',
        'use_item': 'E'
    }
}
```

### Part 2: Modify and Save Configuration

Write a function `set_hotkey(config: dict, category: str, action: str, key: str) -> dict` that:
- takes in the configuration dictionary, category name, action name, and key binding
- modifies the configuration to set the specified hotkey
- returns the modified configuration

Write a function `save_config_file(config: dict, file_path: str) -> None` that:
- takes in the configuration dictionary and output file path
- saves the configuration back to a `.cfg` file

### Part 3: Query Configuration

Write a function `get_hotkey(config: dict, category: str, action: str) -> str` that:
- takes in the configuration dictionary, category name, and action name
- returns the key binding for that action

<details>
<summary><b>Algorithm</b></summary>
<p>To parse a configuration file, follow these steps:</p>
<ol>
  <li>Read the file line by line.</li>
  <li>Identify category headers (lines like `[category]`).</li>
  <li>For each category, parse key-value pairs (format: `key = value`).</li>
  <li>Build a nested dictionary structure with categories as top-level keys.</li>
  <li>Handle whitespace and comments appropriately.</li>
</ol>
</details>

<details>
<summary><b>Tips</b></summary>
<p>Configuration files often have comments (lines starting with `#` or `;`). You may want to skip these.</p>
<p>Be careful with whitespace around keys and values - strip them appropriately.</p>
<p>The nested dictionary structure makes it easy to look up values by category and action.</p>
</details>

<details>
<summary><b>Challenge</b></summary>
<p>- Implement validation when modifying the configuration such that an `InvalidKeyException` is raised if an invalid key combination is given.</p>
<p>- Implement your program as a class with methods to read in the configuration from a `.cfg` file, modify the configuration, and save it back to a `.cfg` file.</p>
<p>- Add support for value types other than strings (integers, booleans, lists).</p>
</details>

----------

# Submission

Before submitting your code, run the automated tests on your functions. In the shell, type `python test_main.py` and press enter to see the results of the testing.
