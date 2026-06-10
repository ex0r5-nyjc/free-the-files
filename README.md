# File Format Practice Repository

This repository contains programming exercises focused on file format processing and data structure manipulation. Each exercise emphasizes practical file handling skills for different formats.

## Repository Structure

The exercises are organized by the type of file format being processed:

### CSV Data Processing
- **[CSV Histogram](csv-histogram/)**: Process CSV survey data and build histogram data structures
- **[Google Contacts](google-contacts/)**: Read, manage, and write Google Contacts CSV data

### Configuration Files
- **[Hotkeys Configuration](hotkeys-config/)**: Parse and modify game hotkey configuration files (.cfg format)

## How to Use This Repository

Each exercise directory contains:
- **README.md**: Detailed exercise description, examples, and challenges
- **main.py**: Starter code with function signatures and documentation
- **test_main.py**: Comprehensive test suite including property-based tests
- **Data files**: Sample data files for testing (when applicable)

## Running the Exercises

1. Navigate to an exercise directory:
   ```bash
   cd csv-histogram
   ```

2. Read the README.md to understand the exercise requirements

3. Implement the functions in main.py

4. Run the tests:
   ```bash
   python test_main.py
   ```

## Testing Philosophy

The test files use a combination of:
- **Unit tests**: Specific test cases for individual functions
- **Property-based tests**: Using Hypothesis library to test properties that should hold for all inputs
- **Integration tests**: Testing the complete functionality

To run property-based tests, install the Hypothesis library:
```bash
pip install hypothesis
```

## Learning Objectives

These exercises help develop skills in:
- **File I/O**: Reading and writing various file formats (CSV, config files)
- **Data Structures**: Building appropriate data structures for different problems
- **Data Processing**: Transforming and analyzing data from different sources
- **Testing**: Writing comprehensive tests including property-based testing
- **Documentation**: Understanding and implementing from specifications

## File Format Focus

### CSV Files
CSV (Comma-Separated Values) files are one of the most common data exchange formats. Understanding how to properly parse, process, and generate CSV data is essential for data processing tasks.

### Configuration Files
Configuration files (.cfg, .ini, etc.) are used to store application settings. Learning to parse and modify these files is important for system administration and application development.

## Contributing

This repository is part of the NYJC Computing 2026 curriculum. For questions or issues, please refer to the course materials.

## License

Educational use for NYJC Computing curriculum.
