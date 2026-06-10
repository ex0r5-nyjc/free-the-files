# Objective

This assignment is practice to be comfortable **processing CSV data and building data structures**.

----------

# CSV Histogram: Building a Data Structure from CSV Data

## Task: Extract data from CSV and Create Histogram

A histogram is a graphical display of data using bars of different heights. In this assignment, you will be building a data structure that makes it easier to visualise a histogram (but you will not be printing one).

The file `basicpythonnotessurvey.csv` contains CSV data from a survey about which entries in a set of notes should be kept.

Write a function `process_survey_data(csv_file_path: str) -> dict` that:
- takes in a file path to a CSV file
- reads the CSV data and processes it
- returns a dictionary with the total number of votes for each entry, organized by category

**Example output**

The returned dictionary should look like:

```python
{
    'functions': {
        'help()': 7,
        'dir()': 7,
        # ... more entries
    },
    'strings': {
        '.count()': 9,
        '.find()': 9,
        # ... more entries
    },
    'lists': {
        'L.append(object)': 10,
        'L.clear()': 7,
        # ... more entries
    }
}
```

<details>
<summary><b>Algorithm</b></summary>
<p>To process the CSV data and create the histogram, follow these steps:</p>
<ol>
  <li>Read the CSV file and parse the headers to understand the data structure.</li>
  <li>Extract the relevant columns containing the survey data.</li>
  <li>Parse each entry to separate the categories (functions, strings, lists) from individual items.</li>
  <li>Count the occurrences of each item across all survey responses.</li>
  <li>Organize the results by category in a nested dictionary structure.</li>
</ol>
</details>

<details>
<summary><b>Tips</b></summary>
<p>Consider using Python's built-in `csv` module to read the CSV file.</p>
<p>Each cell contains multiple entries separated by semicolons. You'll need to split these entries.</p>
<p>Think about how to handle the data structure - a dictionary of dictionaries would work well.</p>
</details>

<details>
<summary><b>Challenge</b></summary>
<p>- Sort the entries by number of votes (descending order) within each category.</p>
<p>- Produce a visual bar chart for each entry, with a symbol (e.g. `#`) representing each vote.</p>
<p>- Write a function to export the histogram data to a text file in a formatted way.</p>
</details>

----------

# Submission

Before submitting your code, run the automated tests on your functions. In the shell, type `python test_main.py` and press enter to see the results of the testing.
