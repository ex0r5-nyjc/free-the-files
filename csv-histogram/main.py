import csv
from typing import Dict

def process_survey_data(csv_file_path: str) -> Dict[str, Dict[str, int]]:
    """
    Process CSV survey data and create a histogram structure.

    Args:
        csv_file_path: Path to the CSV file containing survey data

    Returns:
        A dictionary organized by category, with each category containing
        a dictionary of items and their vote counts
    """
    # Write your code here
    fvotes = []
    svotes = []
    lvotes = []
    ftally = {}
    stally = {}
    ltally = {}
    with open(csv_file_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            fvotes.append(row["Python Functions"])
            svotes.append(row["Python String Methods"])
            lvotes.append(row["Python List Methods"])
    output = {"functions": {}, "strings": {}, "lists": {}}
    for i in range(3):
        tup = [(fvotes, ftally), (svotes, stally), (lvotes, ltally)][i]
        votes, tally = tup
        tally = {}
        for entry in votes:
            data = entry.split("; ")
            for candidate in data:
                if candidate in tally.keys():
                    tally[candidate] += 1
                else:
                    tally[candidate] = 1
        output[list(output.keys())[i]] = dictsort(tally)
    return output

def write_histogram_to_file(histogram_data: Dict[str, Dict[str, int]], output_file: str) -> None:
    """
    Write histogram data to a text file in a formatted way.

    Args:
        histogram_data: The dictionary returned by process_survey_data
        output_file: Path to the output file
    """
    # Write your code here
    with open(output_file, "w") as f:
        for category in histogram_data.keys():
            f.write(category.upper() + ":\n")
            votes = histogram_data[category]
            for entry in votes.keys():
                tally = str(votes[entry])
                f.write(entry + ": " + tally + "\n")
            f.write("\n")

def create_visual_bar_chart(histogram_data: Dict[str, Dict[str, int]], symbol: str = '#') -> str:
    """
    Create a visual bar chart representation of the histogram data.

    Args:
        histogram_data: The dictionary returned by process_survey_data
        symbol: The symbol to use for the bar chart (default: '#')

    Returns:
        A string containing the formatted bar chart
    """
    output = ""
    for category in histogram_data.keys():
        output += category.upper() + "\n"
        votes = histogram_data[category]
        padding = 0
        for entry in votes.keys():
            if len(entry) > padding:
                padding = len(entry)
        padding += 1
        for entry in votes.keys():
            output += entry + (padding - len(entry)) * " " + "| " + symbol * votes[entry] + " " + str(votes[entry]) + "\n"
        output += "\n"
    return output

def dictsort(d: Dict[str, int]) -> Dict:
    """
    Sorts a dictionary according to the integer value, in descending order.

    Arguments:
    d (dict): the dictionary

    Returns:
    (dict) the sorted dictionary
    """
    D = {}
    for i in range(len(d.keys())):
        max = -1
        entry = None
        for key in d.keys():
            value = d[key]
            if value > max:
                max = value
                entry = key
        del d[entry]
        D[entry] = max
    return D


if __name__ == "__main__":
    data = process_survey_data("basicpythonnotessurvey.csv")
    write_histogram_to_file(data, "histogram.csv")
    print(create_visual_bar_chart(data))