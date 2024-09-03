import requests
from bs4 import BeautifulSoup
import logging

# Configure logging
logging.basicConfig(filename='scraper.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Step 1: Fetch the Web Page Content with Enhanced Logging
def fetch_page_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful (status code 200)
        logging.info(f"Successfully fetched content from {url}")
        return response.text  # Return the HTML content as text
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")  # Handle specific HTTP errors
    except requests.exceptions.ConnectionError as conn_err:
        logging.error(f"Connection error occurred: {conn_err}")  # Handle connection errors
    except requests.exceptions.Timeout as timeout_err:
        logging.error(f"Timeout error occurred: {timeout_err}")  # Handle timeout errors
    except requests.exceptions.RequestException as req_err:
        logging.error(f"An error occurred: {req_err}")  # Handle other types of requests errors
    return None

# Step 2: Parse the HTML Content and Extract Data from the Infobox
def parse_infobox(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find the infobox table by class name
    infobox = soup.find('table', {'class': 'infobox'})
    
    if not infobox:
        logging.warning("No infobox found on the page.")
        return None
    
    # Dictionary to store the extracted data
    extracted_data = {}
    
    # Iterate over each row in the infobox
    for row in infobox.find_all('tr'):
        header = row.find('th')  # Header cell (e.g., "Capital")
        value = row.find('td')   # Data cell (e.g., "Tokyo")
        
        if header and value:
            # Extract and clean the text from the header and value
            header_text = header.get_text(strip=True)
            value_text = value.get_text(strip=True)
            
            # Store the extracted data in the dictionary
            extracted_data[header_text] = value_text
    
    logging.info("Successfully parsed the infobox data.")
    return extracted_data

# Step 3: Display the Extracted Data
def display_data(data):
    if data:
        logging.info("Displaying extracted information.")
        print("Extracted Information:")
        for key, value in data.items():
            print(f"{key}: {value}")
    else:
        logging.warning("No data extracted.")

# Main function to execute the web scraper
if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Japan"
    
    # Fetch the page content
    page_content = fetch_page_content(url)
    
    if page_content:
        # Parse the infobox and extract data
        infobox_data = parse_infobox(page_content)
        
        # Display the extracted data
        display_data(infobox_data)
