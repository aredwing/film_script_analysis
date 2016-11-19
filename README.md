## Film Script Analysis Application
The files consist of:
- [Project Proposal](https://github.com/luisecastro/dataInc/blob/master/project_proposal.pdf): Contains a detailed step by step explanation of the process, the main document.
- [Presentation](https://github.com/luisecastro/dataInc/blob/master/script_analysis.pdf) Presentation of the project.
- [Data Collection / Preparation](https://github.com/luisecastro/dataInc/blob/master/data_pre.ipynb): Here is detailed the whole process of data acquisition and preparation.
 	- Webcrawling: Automatically fetch all url's of scripts and proceed to download the information from them.
    - NLP: Analyze raw script text to extract meaningful statistics from it.
    - Watson API: Submit the scripts to IBM's Watson to receive the personality insights from them.
    - IMDB API: Request using the name of the films corresponding to the scripts, valuable meta data like Year, Actors, Directors, Genre, etc.
    - Create a first iteration dataset.
- [Data Visualization](https://github.com/luisecastro/dataInc/blob/master/data_viz.ipynb): Getting to know the dataset just created, it is approached as follows: 
	- Description of general statistics like averages, quantiles, standar deviation.
	- Checks for missing data and outliers.
	- Preprocesses the numerical data to bring the features to the same ranges.
	- Early feature priorization with Random Forest feature importances.
	- Principal Component Analysis and Linear Discriminant Analysis.
	- Creation of the simmilarity matrix using Cosine Distance.
- [Recommendation / Summarization](https://github.com/luisecastro/dataInc/blob/master/rec_sum.ipynb):
	- Levenshtein Distance: For identifying and correcting mistakes in names and strings typed, returns the most similar string contained in the dataset (for film name search).
	- Recommender: Selects the top matches from a similarity matrix to recommend the most similar scripts.
	- Summarize: It filters and selects phrases in the text to return a summary of the script, it also displays relevant IMDB information, and recommended titles.
- [Classification / Regression](https://github.com/luisecastro/dataInc/blob/master/reg_class.ipynb): Using supervised learning for assigning a genre and/or a score to them: Rhis is done by runing various ML models like KNN, SVM, RF and NN. The algorithms are tuned to deliver the most accurate prediction and a feature selection processes to select the feature with greatest predicting power.

Additionaly there are 3 folders and 2 files:
- data: Contains csv and json files, dataset, preprocessed dataset, simmilarity matrix, and imdb metadata.
- images: Images used in the Jupyter notebooks.
- scrapped: The raw texts of the scripts.
- rs.py: Used for some plots.
- summarization.py: Function for the summarization of the text.
