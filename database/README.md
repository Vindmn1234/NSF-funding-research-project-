# `database` Directory Structure
    .
    ├── author_clustering/                  # A sub-directory containing objects related to author clustering
        ├── cluster_by_author.csv           # A dataframe that contains author's clusters based on both ti-idf and word2vec
        ├── cluster_df.csv                  # A dataframe that contains author's normalized abstract and clusters based on both ti-idf
        ├── kmeans_tfidf.pkl                # Fitted k-means clustering object based on ti-idf vectors of paper abstract
        ├── tfidf_cluster_mapping.pkl       # Manually labelled cluster names from k-means clustering results
        ├── tfidf_matrix_2D.pkl             # PCA dimension-reduced representation of clustering results
    ├── author_info/                        # A sub-directory of author information for authors awarded between 2011 and 2020                              
    ├── publication_info/                   # A sub-directory containing publication information of authors awarded between 2011 and 2020
    ├── author_info.csv                     # Concatenated author information between 2011 and 2020
    ├── content_analysis.csv                # Merged dataframe of funding, author, and publication information (*ignored by this repo*)
    ├── funding_info.csv                    # NSF funding information 
    ├── preprocessed_content_analysis.csv   # A dataframe where paper abstract in `content_analysis.csv` is tokenized and normalized(*ignored by this repo*) 
    ├── publication_info.csv                # Concatenated publication information between 2011 and 2020
    ├── README.md
