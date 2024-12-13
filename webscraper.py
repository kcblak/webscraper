import requests
from bs4 import BeautifulSoup
import pandas as pd
import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog
from retrying import retry

# Retry settings
@retry(stop_max_attempt_number=5, wait_fixed=2000)
def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Will raise an HTTPError for bad responses
        return BeautifulSoup(response.text, 'html.parser')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
        raise

# Function to extract data from the webpage
def extract_data(soup):
    data = []
    table = soup.find('table')  # Find the first table
    if not table:
        messagebox.showerror("Error", "No table found on the page.")
        return data, []

    headers = [th.text.strip() for th in table.find_all('th')]  # Extract headers
    for row in table.find_all('tr')[1:]:  # Skip the header row
        cells = row.find_all('td')
        data.append({headers[i]: cells[i].text.strip() for i in range(len(cells))})

    return data, headers

# Function to run the scraping process
def run_scraper():
    url = simpledialog.askstring("Input", "Enter the URL of the webpage to scrape:")
    if not url:
        return
    
    try:
        soup = fetch_page(url)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch page after multiple attempts: {e}")
        return

    if not soup:
        return

    data, headers = extract_data(soup)
    if not data:
        return

    # Let user select columns to omit
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    columns_to_omit = simpledialog.askstring("Input", f"Enter columns to omit (comma-separated):\nAvailable columns: {', '.join(headers)}")
    
    if columns_to_omit:
        columns_to_omit = [col.strip() for col in columns_to_omit.split(',')]
        data = [{k: v for k, v in row.items() if k not in columns_to_omit} for row in data]
        headers = [header for header in headers if header not in columns_to_omit]

    # Convert to DataFrame and save to Excel
    df = pd.DataFrame(data, columns=headers)
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
    
    if file_path:
        df.to_excel(file_path, index=False)
        messagebox.showinfo("Success", f"Data has been scraped and saved to {file_path}")

# Main function to set up the UI
def main():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    run_scraper()

if __name__ == "__main__":
    main()
