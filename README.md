# final-project-scrapers

This repository contains team scraper's code, presentation-related materials, 
and final report for UChicago MACS 30122 Group Project.

## Team Members:
- Guankun Li: guankun@uchicago.edu
- Jiazheng Li: jiazheng123@uchicago.edu
- Tianyue Cong: tianyuec@uchicago.edu
- Weiwu Yan: weiwuyan@uchicago.edu

## Project Description
This project examines the role of the National Science Foundation (NSF) 
funding in shaping the academic output of scholars within the realms of 
Behavioral and Cognitive Sciences. It boasts social science significance as it
explores the allocation and effectiveness of NSF funding in enhancing research 
output and advancing knowledge in areas critical to societal progress and human well-being.

The two **main objectives of this project** are:
1. Evaluate the impact of research funding on scholars' *research quantity* (operationalized as the number of articles published by a scholar in a given year) and *research quality* (measured by sum of citations of the top three most-cited articles published by the scholar in the same year and also the average Impact Factor of these journals where the top three most-cited articles are published);
2. Identify which subfields within Behavioral and Cognitive Sciences are most affected by NSF funding in terms of 

To answer the previous two research questions, this project relies on three **data sources**: 
1) *NSF awards* from 2011 to 2020 (under the division of behavioral and cognitive science) 
to collect awarded authors personal information, including name, email, institution, 
and the corresponding award’s year, amount (<ins>4959</ins> entries in total);
2) *Awarded author's Google Scholar page* (linked from NSF awards) to collect his/her 
academic interests, h-index, and yearly citation counts three years before 
and after the award (<ins>3230</ins> entries in total);
3) *Google Scholar page for publication* (linked from author's Google Scholar page) 3 years before and after NSF awards for 
each author from their Google Scholar page to collect publication-related information,
including coauthors, journal of publication, paper tile and abstract (<ins>207,370</ins> entries in total).

Data clearning and wrangling
Data analysis strategy

## Github Repo Navigation
The following is the **top-level directory layout** of this repo:

    .
    ├── author_clustering/            # Cluster authors based on tf-idf vectors of paper abstract
    ├── data_processing/              # Scrape, clean, and merge data (i.e., funding, author, and publication information)
    ├── database/                     # Store both raw and processed funding, author, and publication information
    ├── descriptive_visualization/    # Visualize descriptive results
    ├── nsf_data/                     # NSF funding information from 2011 to 2020 (ignored by the repo)
    ├── regression/                   # Build and fit linear regression models
    ├── .gitignore
    ├── LICENSE
    ├── README.md
    └── requirements.txt

For detailed layout under each directory, please refer to the specific README file under each directory:
- [README for `author_clustering` directory](author_clustering/README.md)
- [README for `data_processing` directory](data_processing/README.md)
- [README for `database` directory](database/README.md)
- [README for `descriptive_visualization` directory](descriptive_visualization/README.md)
- [README for `regression` directory](regression/README.md)

## Link to Large Files "Ignored" by the Repo
This is the link to the Google Drive where we store large files: https://drive.google.com/drive/u/0/folders/0AH5r0n8gE6Z2Uk9PVA?ths=true.

To integrate them into the whole workflow, please place them in the requried position as outlined in gitignore file:

    # zipped NSF funding data (REMEMBER to unzip the zipped file)
    nsf_data

    # csv files of concatenated publication data and tokenized text for content analysis 
    database/publication_info.csv
    database/content_analysis.csv
    database/preprocessed_content_analysis.csv
    regression/merged_publications_2011_2020.csv

## Running the Code

### Configure the environment

Either using base/conda environment or creating a virtual environment, 
make sure that the Python version is no older than 3.11.

To install the packages required for this project, type the following command in the terminal:
```
pip install --upgrade pip
pip install -r requirements.txt
```

Create virtual environment

### Setting up Chromedriver
To facilitate the smooth running of the code, it is important to ensure that 
`chromedriver.exe` is in system PATH (after installation). Type the following 
commands to check where `chromedriver.exe` is located:
- Windows:
```
where chromedriver
```
- MAC:
```
which chromedriver
```

If `chromedriver.exe` is not in system PATH, make sure to move it to the system PATH.


### Workflow
This section outlines the (recommended) sequential order by which the users can play around with the code:

0. In case you are interested in how the funding, author, and funding related 
csv files were generated in the first place, you can type the following command 
in the terminal (however, bear in mind that it will take extremely long time to 
finish scraping all information: more than 10,000 minutes):
```
# Remove current funding, author, and publication information
rm -r database/author_info database/publication_info
rm database/author_info.csv database/funding_info.csv

# Use command-line arguments to scrape data
python -m data_processing.scraping_helper_functions.get_all_NSF
for year in {2011..2020}; do python -m data_processing.scraping_helper_functions.get_author_info $year; done
for year in {2011..2020}; do python -m data_processing.scraping_helper_functions.get_pub_info $year; done
```

1. The first step is to clean and merge data (i.e., funding, author, and publication information). To do so, simply run [clean.ipynb](data_processing/clean.ipynb) and subsequently [merge.ipynb](data_processing/merge.ipynb) under `data_processing` directory.
2. The second step is to perform author clustering based on ti-idf vectors of paper abstract. To do so, simply run [cluster_by_author.ipynb](author_clustering/cluster_by_author.ipynb) under `author_clustering` directory.
3. The third step is to get descriptive visualization of the data. To do so, simply run [descriptive_visualization.ipynb](descriptive_visualization/descriptive_visualization.ipynb) under `descriptive_visualization` directory. 
4. The fourth step is to build and fit multiple linear regression models. To do so, simply run [prepare_data.ipynb](regression/prepare_data.ipynb) and subsequently [reg.ipynb](regression/reg.ipynb) under `regression` directory 

## Usage of AI to complete the project

dynamic scraping
command-line arguments for scraping helper functions 
debugging
git version control

## Division of Labor
- Guankun Li: Data Scraping
- Jiazhen Li: Data Visualization
- Tianyue Cong: Data Scraping
- Weiwu Yan: Data Analysis

## Links to Presentation
1. This is the link for our team's **in-class presentation slide**: 
https://docs.google.com/presentation/d/16sgquYXFNGgwBLi8cZyFA8T0bTW2om5T/edit#slide=id.g2bd8c1f1ef0_1_7
2. This is the link for our team's **updated presentation slide**: 
3. This is the link for our team's **video presentation**: 

## Data source


## Acknowledgement 👏👏
Our team would like to express our gratitude for instrcutor Sabrina Nardin and teaching assistants for their constructive feedback throughout the whole project.

