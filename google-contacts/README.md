# Objective

This assignment is practice to be comfortable **working with CSV data structures and managing contact groups**.

----------

# Google Contacts: Managing Contact Groups

## Task: Read and Manage Google Contacts Data

Ever needed to find a specific group of people from your Google contacts, or to modify a whole bunch of people at a go? Now you can!

Google Contacts allows you to export your contacts data as a CSV file. This assignment focuses on reading, parsing, and modifying this contact information programmatically.

### Part 1: Read Google Contacts CSV

Write a function `read_google_contacts(csv_file_path: str) -> list[dict]` that:
- takes in a file path to a Google Contacts CSV export file
- reads the CSV data and parses it into a list of dictionaries
- returns a list where each dictionary represents a contact with all available fields

**Note**: You will need to export your Google Contacts to get a sample CSV file. For this exercise, you can create a sample CSV file with the following columns:
- Name
- Email
- Phone
- Group Membership

### Part 2: Manage Contact Groups

Under the "Group Membership" column, contacts in multiple groups have their groups stored with a specific delimiter. 

Write a function `add_contacts_to_groups(contacts: list[dict], group_assignments: dict) -> list[dict]` that:
- takes in a list of contacts (from Part 1) and a dictionary of email-to-group assignments
- adds the specified contacts to appropriate groups
- returns the modified list of contacts

### Part 3: Write Back to CSV

Write a function `write_google_contacts(contacts: list[dict], output_file: str) -> None` that:
- takes in the modified list of contacts and an output file path
- writes the contacts back to a CSV file that can be imported into Google Contacts

<details>
<summary><b>Algorithm</b></summary>
<p>To read and manage Google Contacts data, follow these steps:</p>
<ol>
  <li>Use Python's csv module to read the Google Contacts CSV export.</li>
  <li>Parse each row into a dictionary using the header row as keys.</li>
  <li>Identify the Group Membership column and understand its delimiter format.</li>
  <li>For group management, parse existing groups and add new ones.</li>
  <li>Write the modified data back to CSV format for re-import.</li>
</ol>
</details>

<details>
<summary><b>Tips</b></summary>
<p>Google Contacts CSV files use specific column names. Examine the exported file structure first.</p>
<p>The Group Membership column typically uses " ::: " as a delimiter between group names.</p>
<p>When writing back to CSV, maintain the same column structure as the original export.</p>
</details>

<details>
<summary><b>Challenge</b></summary>
<p>- Implement contact search functionality to find contacts by name, email, or group membership.</p>
<p>- Create a function to merge duplicate contacts based on email address.</p>
<p>- Implement batch operations to add/remove multiple contacts from groups efficiently.</p>
</details>

----------

# Submission

Before submitting your code, run the automated tests on your functions. In the shell, type `python test_main.py` and press enter to see the results of the testing.
