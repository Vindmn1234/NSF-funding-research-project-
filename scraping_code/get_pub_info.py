from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException

def extract_info_from_html(publication_url, driver):
    driver.get(publication_url)
    time.sleep(3)  # Wait for the page to load

    # Initialize variables to store extracted information
    authors = ""
    publication_date = ""
    journal = ""
    abstract = ""
    citation_list = []
    year_citations = {}

    # Extract authors
    try:
        authors_element = driver.find_element(By.XPATH, "//div[@class='gs_scl'][div='Authors']/div[@class='gsc_oci_value']")
        authors = authors_element.text
    except:
        authors = "authors not found"

    # Extract publication date
    try:
        publication_date_element = driver.find_element(By.XPATH, "//div[@class='gs_scl'][div='Publication date']/div[@class='gsc_oci_value']")
        publication_date = publication_date_element.text
    except:
        publication_date = "date not found"

    # Extract journal
    try:
        journal_element = driver.find_element(By.XPATH, "//div[@class='gs_scl'][div='Journal']/div[@class='gsc_oci_value']")
        journal = journal_element.text
    except:
        journal = "journal not found"

    # Extract abstract
    try:
        abstract_element = driver.find_element(By.CSS_SELECTOR, "div.gsh_csp")
        abstract = abstract_element.text
    except:
        try:
            abstract_element = driver.find_element(By.CSS_SELECTOR, "div.gsh_small")
            abstract = abstract_element.text

        except:
            abstract = "Abstract not found"

    # Extract citations and years
    try:
        year_elements = driver.find_elements(By.CSS_SELECTOR, "div#gsc_oci_graph_bars span.gsc_oci_g_t")
        citation_elements = driver.find_elements(By.CSS_SELECTOR, "div#gsc_oci_graph_bars a.gsc_oci_g_a span.gsc_oci_g_al")
        for year, citation in zip(year_elements, citation_elements):
            citation_count = driver.execute_script("return arguments[0].textContent", citation)
            year_citations[year.text] = citation_count
    except:
        pass

    return {
        "Authors": authors,
        "Publication Date": publication_date,
        "Journal": journal,
        "Abstract": abstract,
        "Citations": year_citations
    }

# Configure Selenium WebDriver
options = webdriver.ChromeOptions()
# Set browser options
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--headless=new')
cService = webdriver.ChromeService(
    executable_path=r"D:\learning materials\Chicago\MACS 30122\final\chromedriver.exe")

driver = webdriver.Chrome(service=cService, options=options)

# Read CSV file
input_csv_file = "author_publications_with_infotest.csv"
output_csv_file = "author_publications_with_infotest.csv"

df = pd.read_csv(input_csv_file)

# Create new columns to store extracted information
df["Authors"] = ""
df["Publication Date"] = ""
df["Journal"] = ""
df["Abstract"] = ""
df["Citations"] = ""
import chardet
# Iterate through each row, execute the scraping function, and update the DataFrame
for index, row in df.iterrows():

    publication_url = row["Paper URL"]
    try:
        info = extract_info_from_html(publication_url, driver)
        print(info)
        df.at[index, "Authors"] = info["Authors"]
        df.at[index, "Publication Date"] = info["Publication Date"]
        df.at[index, "Journal"] = info["Journal"]
        df.at[index, "Abstract"] = info["Abstract"]
        df.at[index, "Citations"] = str(info["Citations"])
    except:
        pass

    time.sleep(2)
    # Save data every 50 rows
    if (index + 1) % 50 == 0:
        df.to_csv(output_csv_file, index=False, encoding='utf-8-sig')
        print(f"Saved data for {index + 1} rows.")

    # Close and restart WebDriver
    if (index + 1) % 50 == 0:
        driver.quit()
        print("Driver closed. Sleeping for 20 seconds...")
        time.sleep(20)
        # Restart WebDriver
        driver = webdriver.Chrome(service=cService, options=options)

# Save remaining data
df.to_csv(output_csv_file, index=False, encoding='utf-8-sig')

# Close WebDriver
driver.quit()
