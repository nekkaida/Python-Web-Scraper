# **Simple Web Scraper with Data Storage**

## **Overview**

This project is a Python-based web scraper designed to extract structured data from a Wikipedia page. The scraper targets multiple sections of the page, such as the infobox, references, external links, and the introduction paragraph. The extracted data can be used for various purposes, such as research, analysis, or simply gathering information in an organized format.

## **Features**

- **Data Extraction from Multiple Sections**: 
  - **Infobox**: Extracts key information such as capital, population, area, etc.
  - **Introduction Paragraph**: Extracts the first paragraph of the Wikipedia page.
  - **References**: Gathers the list of references cited on the page.
  - **External Links**: Extracts links to external websites from the "External links" section.

- **Enhanced Logging**: The scraper is equipped with a logging system that records all operations and errors to a log file (`scraper.log`), making it easier to debug and trace the execution flow.

- **Error Handling**: Robust error handling is implemented to manage network issues, HTTP errors, and parsing issues.

## **Requirements**

- **Python 3.x**
- **Libraries**:
  - `requests`
  - `beautifulsoup4`
  - `logging`

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

   To run the scraper, simply execute the `scraper.py` script. By default, it scrapes data from the Wikipedia page for Japan.

   ```bash
   python scraper.py
   ```

2. **Extracted Data**:

   After running the scraper, the extracted data from the Wikipedia page will be displayed in the console. The data includes information from the infobox, the introductory paragraph, references, and external links.

3. **Log File**:

   All activities, including successful operations and any errors encountered during scraping, are logged in the `scraper.log` file. This file can be reviewed to diagnose issues or track the scraper's operations.

## **Code Structure**

- **`scraper.py`**: The main script that contains the logic for fetching the page, parsing the HTML content, and displaying the extracted data.
- **`scraper.log`**: A log file that records the operations and errors encountered by the scraper.

## **Functions**

- **`fetch_page_content(url)`**:
  - Fetches the HTML content of the specified URL.
  - Handles HTTP errors and logs all operations.

- **`parse_infobox(soup)`**:
  - Extracts key information from the infobox on the page.
  - Returns a dictionary of the extracted data.

- **`parse_introduction(soup)`**:
  - Extracts the first paragraph of the page (typically the introduction).
  - Returns the paragraph as a string.

- **`parse_references(soup)`**:
  - Extracts the list of references cited on the page.
  - Returns a list of reference texts.

- **`parse_external_links(soup)`**:
  - Extracts external links from the "External links" section.
  - Returns a list of URLs.

- **`display_data(data)`**:
  - Displays the extracted data in a readable format in the console.

## **Customization**

- **Target URL**:
  - The scraper is currently set to target the Wikipedia page for Japan. You can change the `url` variable in the `__main__` block to target a different Wikipedia page or another website.

- **Sections to Extract**:
  - The scraper is modular, allowing you to easily add or remove sections that you want to extract. Simply add or remove the corresponding function calls in the `data` dictionary in the `__main__` block.

## **Contributing**

If you would like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request. Contributions are welcome!
