## Film Script Analysis
The files consist of:
- [Project Proposal](https://github.com/luisecastro/dataInc/blob/master/project_proposal.pdf): Project proposal that contains a detailed step by step explanation of the process (old file).
- [Presentation](https://github.com/luisecastro/dataInc/blob/master/script_analysis.pdf) Presentation of the project, proposed steps.
- [00_webscrapping](https://github.com/luisecastro/film_script_analysis/blob/master/00_webscrapping.ipynb): Scrapping pages and parsing html to text.
- [01_imdb](https://github.com/luisecastro/film_script_analysis/blob/master/01_imdb.ipynb): Querying omdb API to retrive film meta data.
- [02_nlp](https://github.com/luisecastro/film_script_analysis/blob/master/02_nlp.ipynb): Use of NLTK library for tokenization, lemmation and text statistics.
- [03_watson](https://github.com/luisecastro/film_script_analysis/blob/master/03_watson.ipynb): Watson API interface to perform personality insights on the scripts.
- [04_cleaning](https://github.com/luisecastro/film_script_analysis/blob/master/04_cleaning.ipynb): Remove NA's, corrupted data, clean and order dataset.
- [05_preprocessing](https://github.com/luisecastro/film_script_analysis/blob/master/05_preprocessing.ipynb): Scale data to have mean=0 and std = 1, used for learning models.
- [06_visualization](https://github.com/luisecastro/film_script_analysis/blob/master/06_visualization.ipynb): Visualize relationships among the features of the datasets and clusterings.
- [07_classification](https://github.com/luisecastro/film_script_analysis/blob/master/07_classification.ipynb): Perform classification of script Genre using predictor features.
- [08_regression](https://github.com/luisecastro/film_script_analysis/blob/master/08_regression.ipynb): Peform regression of script imdbRating using predictor features.
- [09_recomendation](https://github.com/luisecastro/film_script_analysis/blob/master/09_recommendation.ipynb): Recommend scripts based on their content and their rating.
- [10_summarization](https://github.com/luisecastro/film_script_analysis/blob/master/10_summarization.ipynb): Return script summary based on sentence words' frequencies.
- [11_word2vec](https://github.com/luisecastro/film_script_analysis/blob/master/11_word2vec.ipynb): Create word embedings, word vectors using the whole script corpora, check word relationships.