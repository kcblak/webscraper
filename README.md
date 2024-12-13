# Web Scraper

A Python script that scrapes data from a webpage, extracts table content, allows users to omit specific columns, and saves the result to an Excel file. The script utilizes `requests`, `BeautifulSoup`, `pandas`, `tkinter`, and `retrying` libraries.

## Features

- **Scrape Webpages**: Extract data from a table found on a webpage.
- **Column Omission**: Allows users to specify columns to omit during the data extraction process.
- **Excel Export**: Saves the scraped data to an Excel file (`.xlsx`).
- **Retry Mechanism**: Built-in retry logic to handle failed network requests.
- **User-Friendly Interface**: A simple GUI built with `tkinter` for interacting with the user.

## Installation

### Prerequisites

Ensure you have Python 3.x installed on your system. You can check this by running:

```bash
python --version
Install Dependencies
The script requires the following Python libraries:

requests: For making HTTP requests to fetch the webpage content.
beautifulsoup4: For parsing the HTML and extracting table data.
pandas: For handling and manipulating the data, and saving it to an Excel file.
openpyxl: For writing Excel files.
retrying: For automatic retries on network request failures.
tkinter: For building the graphical user interface (GUI).
To install the required dependencies, run the following command:

```bash
pip install requests beautifulsoup4 pandas openpyxl retrying
### Usage
Running the Script
Run the script:

After installing the dependencies, you can run the script using the following command:
```bash
python webscraper.py
Input URL:

The script will prompt you to input the URL of the webpage you want to scrape. For example:

vbnet
Copy code
Enter the URL of the webpage to scrape:
https://example.com/page-with-table
Column Omission:

After the script scrapes the table data, it will show the available columns and ask whether you want to omit any columns. For example:

```css
Enter columns to omit (comma-separated): Column1, Column2
If you do not want to omit any columns, just leave the input blank and press Enter.

Save the Data:

The script will then prompt you to choose a location and file name for saving the data as an Excel file:

```javascript
Save the data to: /path/to/your/folder/output.xlsx
Completion:

Once the data is saved, a success message will appear:

## css
Copy code
Data has been scraped and saved to /path/to/your/folder/output.xlsx
## Example
To use the script:

Run the script:

```bash
python webscraper.py
Provide the URL when prompted:

```vbnet
Enter the URL of the webpage to scrape:
https://example.com/page-with-table
Choose the columns to omit, if any:

css
Copy code
Enter columns to omit (comma-separated): Column1, Column3
Choose the location to save the resulting Excel file.

A success message confirms the data has been saved.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Troubleshooting
Common Issues
No Table Found: If the script cannot find any table on the provided webpage, it will show an error message: No table found on the page..

Ensure the page contains a properly structured HTML table.
Check the webpage structure for dynamically loaded content, which may not be captured by requests and BeautifulSoup.
Invalid URL: If you provide an invalid or unreachable URL, the script will display an error message and retry the request up to 5 times.

Ensure the URL is correct and accessible.
Missing Dependencies: If you receive an error about missing libraries, ensure that you've installed the required dependencies using the following command:

```bash
pip install requests beautifulsoup4 pandas openpyxl retrying

### Error Handling
The script uses the retrying library to retry failed requests up to 5 times with a 2-second wait between attempts. If the script is unable to fetch the page after the retries, it will show an error message indicating the failure.

## Contributing
We welcome contributions to this project! To contribute, follow these steps:

Fork the repository to your GitHub account.
Create a new branch for your feature or bug fix.
Make your changes and commit them.
Push your changes to your forked repository.
Open a pull request to merge your changes into the main repository.
Code Style
Follow PEP 8 guidelines for Python code.
Ensure that your changes are well-documented and that any new functionality is accompanied by appropriate tests.
Credits
This project uses the following open-source libraries:

requests: Used for making HTTP requests.
beautifulsoup4: Used for parsing HTML content.
pandas: Used for handling and saving data.
tkinter: Used for the graphical user interface.
retrying: Used for retrying failed network requests.
File Structure
plaintext
Copy code
webscraper.py  # Main script
README.md      # This documentation file
LICENSE        # License file (MIT)
Steps to Use:
Create the GitHub repository and upload the webscraper.py file.
Add the above README.md to your repository to provide documentation.
Follow the steps to create the repository and push your files as previously explained.

