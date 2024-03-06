# final-project-scrapers

This repository contains team scraper's code, presentation materials, 
and final project report for MACS 30122 Group Project that examines how research
funding influences awarded authors' research quantity and quality.

The following table outlines the table of contents for the main README file:
| Section          | Description                                   |
|------------------|-----------------------------------------------|
| [Team Members](#team-members-and-division-of-labor) | Information about the contributors to this project |
| [Project Description](#project-description) | Research questions, data analysis strategies, and result summary of this project |
| [Github Repo Navigation](#github-repo-navigation) | Top-level directory layout of this repoistory |
| [Links to Large Files](#links-to-large-files-ignored-by-the-repo) |  Information about where to view and download large, "ignored" files |
| [Running the Code](#running-the-code) | Information about how to run the code to reproduce the results |
| [Usage of AI](#usage-of-ai-to-complete-the-project) | Information about where AI tools was used in this project |
| [Links to Presentation and Final Report](#usage-of-ai-to-complete-the-project) | Presentation-related materials of this project |
| [Acknowledgement](#acknowledgement-👏👏) | Acknowledgement from team scraper  |

## Team Members and Division of Labor
- Guankun Li (guankun@uchicago.edu): data scraping 🔗
- Jiazheng Li (jiazheng123@uchicago.edu): data visualization 📊
- Tianyue Cong (tianyuec@uchicago.edu): data scraping 🔗
- Weiwu Yan (weiwuyan@uchicago.edu): data analysis 🧮 

## Project Description
This project examines the role of the National Science Foundation (NSF) 
funding in shaping the academic output of scholars within the realms of 
Behavioral and Cognitive Sciences. It boasts social science significance as it
explores the allocation and effectiveness of research funding, one of the most 
crucial public resources in scientific development, in enhancing research output 
and advancing knowledge in areas critical to societal progress and human well-being.

The three **main objectives of this project** are:
1. Assess NSF funding's effect on research output's quantity and quality, using metrics such as publication counts and citation impact.
2. Utilize k-means clustering on vectorized paper abstracts to categorize research subfields within the Behavioral and Cognitive Sciences.
3. Determine the differential impact of NSF funding across these subfields through clustering and heterogeneity analysis. 

This project relied on three **data sources**: 
1) *NSF awards* under the division of behavioral and cognitive science from 2011 to 2020 (https://www.nsf.gov/awardsearch/download.jsp) to collect awarded authors personal information, including name, email, institution, 
and the corresponding award’s year, amount (<ins>4959</ins> entries in total);
2) *Awarded author's Google Scholar page* (linked from NSF awards; [example](https://scholar.google.com/citations?user=kV4N4zoAAAAJ&hl=en)) to collect his/her academic interests, h-index, and yearly citation counts three years before 
and after the award (<ins>3230</ins> entries in total);
3) *Google Scholar page for publication* (linked from author's Google Scholar page; [example](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=kV4N4zoAAAAJ&citation_for_view=kV4N4zoAAAAJ:E10ZYwHxBI8C)) 3 years before and after NSF awards for each author from their Google Scholar page to collect publication-related information,
including coauthors, journal of publication, paper tile and abstract (<ins>207,370</ins> entries in total).

After data scraping, our teams performed four **data cleaning/wrangling** steps. First, when scraping author and publication information, we chose to focus on the division of behavioral and cognitive science within the directory for social, behavioral, and economic science. This not only enhance the efficiency of our research by focusing on a specific segment within a vast dataset but also zoom in on a more defined ”cluster” of related disciplines. Second, our team performed sufficient number of checks of NA values both during and after web-scraping processes. For most NA values, our team removed them on the fly. The only exception was authors’ yearly citation count, where we filled these NA values with zero. Third, our team merged funding, author, and publication information together and formated the string and numerical formats in the merged dataframe. Fourth, our team performed text tokenization and normalization for paper abstract for later clustering analysis.

Our **key findings** include:
- For *descriptive statistics*, we found an upward trend in NSF funding over the years, indicating increasing financial support for research. The scatter plot results suggest a positive correlation between NSF funding and both the quantity and quality of publications. 
- For *regression analysis*, baseline regression shows that NSF funding significantly increases the quantity of publications but has a negative impact on their quality. However, after controlling for time-fixed effects, funding positively affects publication quantity without significantly affecting quality, suggesting that NSF funding boosts the volume of academic research output in the Behavioral and Cognitive Sciences without detrimentally impacting the quality of research.
- For *clustering analysis*, after manually coded the eight clusters of study, we found significant variance in financial support within the Behavioral and Cognitive Sciences division, with Linguistics receiving the most funding while Human Biology, Archaeology, and Environmental Studies receiving the least. 
- For *regression analysis grouped by clustered subfields*, our team found that funding consistently has a positive effect on the number of publications across all subfields. The effect of funding is particularly strong in Cognitive Neuroscience, Human Biology, and Environmental Studies, indicating that these subfields may benefit more from increased funding in terms of publication output.


## Github Repo Navigation
The following is the **top-level directory layout** of this repo:

    .
    ├── author_clustering/            # Cluster authors based on tf-idf vectors of paper abstract
    ├── data_processing/              # Scrape, clean, and merge data (i.e., funding, author, and publication information)
    ├── database/                     # Store both raw and processed funding, author, and publication information
    ├── descriptive_visualization/    # Visualize descriptive results
    ├── nsf_data/                     # NSF funding information from 2011 to 2020 (ignored by the repo)
    ├── regression/                   # Build and fit linear regression models
    ├── slides/                       # slides for presentation and an updated version
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

## Links to Large Files "Ignored" by the Repo
This is the link to the Google Drive where we store large files: https://drive.google.com/drive/u/0/folders/0AH5r0n8gE6Z2Uk9PVA?ths=true.

To integrate them into the whole workflow, please place them in the requried position as outlined in gitignore file:

    # zipped NSF funding data (REMEMBER to unzip the zipped file)
    nsf_data

    # csv files of concatenated publication data and tokenized text for content analysis 
    database/publication_info.csv
    database/content_analysis.csv
    database/preprocessed_content_analysis.csv

## Running the Code

### Configure the environment

It is recommended to create a virtual environment to run the code of this project 
to avoid potential conflicts:

- Create the virtual environment:
    ```
    python3.11 -m venv myenv # replace "myenv" with the name for the virtual environment you want
    ```
- Activate the virtual environment:
    - Windows:
        ```
        myenv\Scripts\activate # replace "myenv" with the name for the virtual environment you want
        ```
    - MAC:
        ```
        source myenv/bin/activate # replace "myenv" with the name for the virtual environment you want
        ```
- Deactivate the base conda environment [suppose conda environment is the "(base)"]
    ```
    conda deactivate
    ```

Either using base environment (make sure that the Python version is no earlier than 3.11) or creating a virtual environment, the next step is to install the packages required for this project, type the following command in the terminal:
```
pip install --upgrade pip
pip install -r requirements.txt
```


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


## Usage of AI to Complete the Project
The scraper team relied on AI chatbot (specifically, ChatGPT) to solve encountered difficulties (bugs) in some parts of this project. Below is a table summarizing the areas where ChatGPT provided assistance:

| Aspect                      | Description                                                                                  |
|-----------------------------|----------------------------------------------------------------------------------------------|
| Dynamic web-scraping using Selenium  | Consulted on methods for locating elements                                          |
| Command-Line Arguments      | Consulted on specifying the command-line arguments for scraping helper functions             |
| Git Version Control         | Consulted on ways to reset commands and resolve diverging branches for git version control   |


## Links to Presentation and Final Report
Below are the materials related to our team's presentation as well as the final report:

|  materials               | Link                                                                                           |
|------------------------------|------------------------------------------------------------------------------------------------|
| In-Class Presentation Slide  | [View Slide](https://docs.google.com/presentation/d/16sgquYXFNGgwBLi8cZyFA8T0bTW2om5T/edit#slide=id.g2bd8c1f1ef0_1_7) |
| Updated Presentation Slide   | [View Slide](https://docs.google.com/presentation/d/1np87bklhwDuJ54SQmsRJux7S2diFRMsh/edit?usp=drive_link&ouid=117423846760378080439&rtpof=true&sd=true)  |
| Video Presentation           | [Watch Video](#)                                                                               |
| Final Report   | [View Pdf](https://drive.google.com/file/d/1HSWhWwPfE3M057aHXiM4ExJ7d3eOVD2_/view?usp=sharing)                                                                                |


## Acknowledgement 👏👏
Our team would like to express our gratitude for instrcutor Sabrina Nardin and teaching assistants for their constructive feedback throughout the whole project.

