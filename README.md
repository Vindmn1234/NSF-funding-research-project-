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
1) NSF awards from 2011 to 2020 (under the division of behavioral and cognitive science) 
to collect awarded authors personal information, including name, email, institution, 
and the corresponding award’s year, amount (<ins>4959</ins> entries in total);
2) Awarded author's Google Scholar page (linked from NSF awards) to collect his/her 
academic interests, h-index, and yearly citation counts three years before 
and after the award (<ins>3230</ins> entries in total);
3) Google Scholar page for publication 3 years before and after NSF awards for 
each author from their Google Scholar page to collect publication-related information,
including coauthors, journal of publication, paper tile and abstract (<ins>207370</ins> entries in total).

Data clearning and wrangling
Data analysis strategy

## Github Repo Navigation
The following is the **top-level directory layout** of this repo 
(for detailed layout under each directory, please refer to the specific README file under each directory):

    .
    ├── author_clustering/            # Cluster authors based on tf-idf vectors of paper abstract
    ├── data_processing/              # Scrape, clean, and merge data (i.e., funding, author, and publication information)
    ├── database/                     # Store both raw and processed funding, author, and publication information
    ├── descriptive_visualization/    # Visualize descriptive results
    ├── regression/                   # Build and fit linear regression models
    ├── .gitignore
    ├── LICENSE
    ├── README.md
    └── requirements.txt

## Link to Large Files "Ignored" in the Repo
This is the link to the Google Drive where we store large files: .

To integrate them into the whole workflow, please place them in the requried position as outlined in gitignore file:

    # unzipped NSF funding data
    NSF_data

    # csv files of concatenated publication data and tokenized text for content analysis 
    database/publication_info.csv
    database/content_analysis.csv
    database/preprocessed_content_analysis.csv

## Running the Code

### Configure the environment

### Workflow

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
