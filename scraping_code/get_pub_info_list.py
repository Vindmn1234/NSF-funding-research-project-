import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

# Read the 'author_url_2019.csv' file
df = pd.read_csv('author_url_2019.csv')

# Create an empty DataFrame to store all authors' publication information
all_publications = pd.DataFrame()

# Configure Selenium WebDriver
options = webdriver.ChromeOptions()
# Set browser options
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--headless=new')
# Here, ensure that chromedriver.exe is in system PATH
# Check by `where chromedriver`` (for Windows) or `which chromedriver` (for MAC)
# If not, move it to the system PATH to avoid running webdriver.ChromeService()
# driver = webdriver.Chrome(options=options)

for index, row in df.iterrows():
    # Configure webdriver (again) every time after quitted for each iteration
    driver = webdriver.Chrome(options=options)

    url = row['url']

    # Visit the author's homepage
    driver.get(url)
    time.sleep(2)

    # Click the "Show more" button until all papers are loaded
    while True:
        try:
            show_more_button = driver.find_element(By.ID, "gsc_bpf_more")
            if show_more_button.is_displayed() and show_more_button.is_enabled():
                show_more_button.click()
                time.sleep(2)
            else:
                break
        except (NoSuchElementException, ElementClickInterceptedException):
            break

    # Extract information about the papers
    publications = []
    rows = driver.find_elements(By.CSS_SELECTOR, "tr.gsc_a_tr")
    for row in rows:
        title = row.find_element(By.CSS_SELECTOR, "a.gsc_a_at").text
        authors_and_journal = row.find_elements(By.CSS_SELECTOR, "div.gs_gray")[0].text
        year = row.find_element(By.CSS_SELECTOR, "span.gsc_a_hc").text
        cited_by = row.find_element(By.CSS_SELECTOR, "a.gsc_a_ac").text
        paper_url = row.find_element(By.CSS_SELECTOR, "a.gsc_a_at").get_attribute("href")

        publications.append({
            "Title": title,
            "Authors and Journal": authors_and_journal,
            "Year": year,
            "Cited by": cited_by,
            "Paper URL": paper_url
        })

    # Convert the author's publication information into a DataFrame
    author_publications_df = pd.DataFrame(publications)

    # Add the author's publication information to the overall DataFrame
    all_publications = pd.concat([all_publications, author_publications_df], ignore_index=True)
    all_publications.to_csv('all_author_publications.csv', index=False, encoding='utf-8-sig')
    driver.quit()

# Save all authors' publication information as a CSV file
all_publications.to_csv('all_author_publications.csv', index=False, encoding='utf-8-sig')
