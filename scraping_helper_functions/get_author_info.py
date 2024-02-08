from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def find_url(driver, full_name, email_domain):
    '''
    Finds awarded author's Google Scholar url (for further web scraping).

    Inputs:
        1) driver: selenium webdriver
        2) full_name: full name of the awared author
        3) email_domain: email domain name of the awared author

    Returns: awarded author's Google Scholar url
    '''

    # Starting point to search for author's Google Scholar url
    url = f"https://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors={full_name}"
    driver.get(url)
    time.sleep(7)

    authors = driver.find_elements(By.CSS_SELECTOR, "div.gs_ai.gs_scl.gs_ai_chpr")
    if len(authors) == 1:
        link_element = authors[0].find_element(By.CSS_SELECTOR, "a.gs_ai_pho")
        return link_element.get_attribute('href')
    else:
        for author in authors:
            author_email_text = author.find_element(By.CSS_SELECTOR, "div.gs_ai_eml").text
            if 'Verified email at ' in author_email_text:
                author_email_domain = author_email_text.split('Verified email at ')[1]
                # Make sure the email domain matches
                if email_domain == author_email_domain:
                    link_element = author.find_element(By.CSS_SELECTOR, "a.gs_ai_pho")
                    return link_element.get_attribute('href')

    return None


def find_citations(driver, url):
    '''
    Finds awarded author's citation-related indices.

    Inputs:
        1) driver: selenium webdriver
        2) url: awarded author's Google Scholar url

    Returns: a tuple of 1) awarded author's total number of citation 
        (as of the date when the info is scraped); 2) awarded author's h-index;
        3) awarded author's yearly citation number (from the year he/she 
        publishes the first paper to 2024)
    '''

    driver.set_window_size(800, 1000)
    driver.get(url)
    time.sleep(3)

    cited_by_tab = driver.find_element(By.ID, "gsc_prf_t-cit")
    cited_by_tab.click()
    time.sleep(3)

    # Extract total number of citation and h-index
    total_citations = driver.find_element(By.XPATH, '//*[@id="gsc_rsb_st"]/tbody/tr[1]/td[2]').text
    h_index = driver.find_element(By.XPATH, '//*[@id="gsc_rsb_st"]/tbody/tr[2]/td[2]').text

    # Extract yearly citation number
    year_citations = {}
    year_elements = driver.find_elements(By.CSS_SELECTOR, "div.gsc_md_hist_w .gsc_g_t")
    citation_elements = driver.find_elements(By.CSS_SELECTOR, "div.gsc_md_hist_w .gsc_g_a")

    for year, citation in zip(year_elements, citation_elements):
        citation_count = driver.execute_script("return arguments[0].textContent", citation)
        year_citations[year.text] = citation_count

    return total_citations, h_index, year_citations


def find_interests(driver, url):
    '''
    Finds awarded author's research interest(s) on the Google Scholar page.
    
    Inputs:
        1) driver: selenium webdriver
        2) url: awarded author's Google Scholar url

    Returns: a list of awarded author's research interests
    '''

    driver.get(url)
    time.sleep(3)

    interests = []

    try:
        interest = driver.find_elements(By.CSS_SELECTOR, "div#gsc_prf_int a.gsc_prf_inta")
        interests = [i.text for i in interest] if interest else None

    except Exception as e:
        print(f"Error occurred: {e}")

    return interests


def update_and_save_dataframe(df):
    # Configure Selenium WebDriver
    options = webdriver.ChromeOptions()
    # Set browser options
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--headless=new')
    # Here, ensure that chromedriver.exe is in system PATH
    # Check by `where chromedriver`` (for Windows) or `which chromedriver` (for MAC)
    # If not, move it to the system PATH to avoid running webdriver.ChromeService()
    driver = webdriver.Chrome(options=options)

    # Updates Google Scholar urls
    df = df.dropna(subset=['email'])
    # df['url'] = None

    # for index, row in df.iterrows():
    #     # driver = webdriver.Chrome(service=cService, options=options)
    #     full_name = row['first_name'] + '+' + row['last_name']
    #     full_name = full_name.strip()
    #     email_domain = row['email'].split('@')[-1]
    #
    #     url = row['url']  # get existing URL
    #     if pd.isna(url):  # if url NaN find_url
    #         url = find_url(driver, full_name, email_domain)
    #         df.loc[index, 'url'] = url
    #     print(url)
    #     time.sleep(1)
    #     # driver.quit()
    #     if index % 50 == 0:
    #         df.to_csv("author_url_blank.csv", index=False)  # save every 50 rows
    # driver.quit()

    df = df.dropna(subset=['url'])
    df['interests'] = None

    for index, row in df.iterrows():
        url = row['url']
        # Updates citations
        total_citations, h_index, year_citations = find_citations(driver, url)
        df.at[index, 'total_citations'] = total_citations
        df.at[index, 'h_index'] = h_index

        for year, citations in year_citations.items():
            col_name = f'citations_{year}'
            df.at[index, col_name] = citations

        # Updates interests
        interests = find_interests(driver, url)
        if interests:
            df.at[index, 'interests'] = [interest for interest in interests]

        print(interests)
        time.sleep(1)

        if index % 50 == 0:
            df.to_csv("author_info_2019.csv", index=False)  # save every 50 rows
    driver.quit()
    # save DataFrame
    df.to_csv('author_info_2019.csv', index=False)

