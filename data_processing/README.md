# `data_processing` Directory Structure
    .
    ├── scraping_helper_functions/     # A sub-directory containing helper functions for scraping
        ├── __init__.py           # Mark the directory as a Python package directory
        ├── get_all_NSF.py        # Convert xml files of NSF awards into a concatenated csv of information about NSF awarded projects
        ├── get_author_info.py    # Generate author's personal information linking from NSF awards
        ├── get_pub_info.py       # Generate author's publication-related information from the urls of their Google Scholar pages
        ├── webdriver_setup.py    # Initialize the selenium webdriver for dynamic web-scraping 
    ├── __init__.py     # Mark the directory as a Python package directory
    ├── clean.ipynb     # A Jupyter Notebook that cleans the scraped data
    ├── merge.ipynb     # A Jupyter Notebook that merges funding, author, and publication information
    ├── scrape.ipynb    # A Jupyter Notebook that scrapes funding, author, and publication information
    ├── README.md