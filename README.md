# **Simple Web Scraper with Data Storage**

## **Overview**

This project is a Python-based web scraper designed to extract structured data from a Wikipedia page. The scraper specifically targets the infobox on the page, which typically contains key information such as population, area, capital city, and more. The extracted data is then displayed in a readable format.

## **Features**

- **Infobox Data Extraction**: 
  - Extracts key information such as the capital, population, area, and more from the infobox of a Wikipedia page.
  
- **Enhanced Logging**: 
  - The scraper includes a logging system that records all operations and errors in a log file (`scraper.log`). This makes it easier to debug and trace the execution flow.

- **Error Handling**: 
  - Robust error handling is implemented to manage network issues, HTTP errors, and parsing issues.

## **Requirements**

- **Python 3.x**
- **Libraries**:
  - `requests`
  - `beautifulsoup4`
  - `logging` (part of Python's standard library)

## **Setup**

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/simple-web-scraper.git
   cd simple-web-scraper
   ```

2. **Set Up a Virtual Environment (Optional but Recommended)**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the Required Libraries**:

   ```bash
   pip install requests beautifulsoup4
   ```

## **Usage**

1. **Running the Scraper**:

   To run the scraper, execute the `scraper.py` script. By default, it scrapes data from the Wikipedia page for Japan.

   ```bash
   python scraper.py
   ```

2. **Extracted Data**:

   After running the scraper, the extracted data from the Wikipedia page will be displayed in the console. The data includes information such as the capital, population, area, and more from the infobox.

3. **Log File**:

   All activities, including successful operations and any errors encountered during scraping, are logged in the `scraper.log` file. This file can be reviewed to diagnose issues or track the scraper's operations.

## **Code Structure**

- **`scraper.py`**: The main script containing the logic for fetching the page content, parsing the HTML, and displaying the extracted data.
- **`scraper.log`**: A log file that records the operations and errors encountered by the scraper.

## **Functions**

- **`fetch_page_content(url)`**:
  - Fetches the HTML content of the specified URL.
  - Handles HTTP errors and logs all operations.

- **`parse_infobox(html_content)`**:
  - Extracts key information from the infobox on the page.
  - Returns a dictionary of the extracted data.

- **`display_data(data)`**:
  - Displays the extracted data in a readable format in the console.

## **Customization**

- **Target URL**:
  - The scraper is currently set to target the Wikipedia page for Japan. You can change the `url` variable in the `__main__` block to target a different Wikipedia page or another website.

## **Contributing**

If you would like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request. Contributions are welcome!
