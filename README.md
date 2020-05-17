# Reddit Hate-Speech User Input Application

A Reddit Hate user-input web application to take user input regarding hate-posts on Reddit.

### Directory Structure

The directory `hatespeech` is a ***Django*** web application set-up for hosting on *Heroku* servers. The description of files and folders can be found below:

  1. [manage.py](https://github.com/radonys/Reddit-Flair-Detector/blob/master/manage.py) - The file used to start Django server.
  2. [requirements.txt](https://github.com/radonys/Reddit-Flair-Detector/blob/master/requirements.txt) - Containing all Python dependencies of the project.
  3. [nltk.txt](https://github.com/radonys/Reddit-Flair-Detector/blob/master/nltk.txt) - Containing all NLTK library needed dependencies.
  4. [Procfile](https://github.com/radonys/Reddit-Flair-Detector/blob/master/Procfile) - Needed to setup Heroku.
  5. [hatespeech](https://github.com/radonys/Reddit-Flair-Detector/tree/master/website) - Folder containing the master settings of Django application.
  6. [templates](https://github.com/radonys/Reddit-Flair-Detector/tree/master/templates/flair_detector) - Folder containing HTML/CSS files.
  7. [user_input](https://github.com/radonys/Reddit-Flair-Detector/tree/master/flair_detector) - Folder containing the main application which loads the Machine Learning model.
  8. [Models](https://github.com/radonys/Reddit-Flair-Detector/tree/master/Models) - Folder containing the saved model.
  10. [Jupyter Notebooks](https://github.com/radonys/Reddit-Flair-Detector/tree/master/Jupyter%20Notebooks) - Folder containing Jupyter Notebooks to collect Reddit India data and train Machine Learning models. Notebooks can be opened in [Colaboratory](https://colab.research.google.com/) by Google.
  
### Codebase

The entire code has been developed using Python programming language, utilizing it's powerful text processing and machine learning modules. The application has been developed using Django web framework and hosted on Heroku web server.

### Project Execution

  1. Open the `Terminal`.
  2. Clone the repository by entering `git clone https://github.com/radonys/Reddit-Flair-Detector.git`.
  3. Ensure that `Python3` and `pip` is installed on the system.
  4. Create a `virtualenv` by executing the following command: `virtualenv -p python3 env`.
  5. Activate the `env` virtual environment by executing the follwing command: `source env/bin/activate`.
  6. Enter the cloned repository directory and execute `pip install -r requirements.txt`.
  7. Enter `python` shell and `import nltk`. Execute `nltk.download('stopwords')` and exit the shell.
  8. Enter the `hatespeech` directory.
  8. Now, execute the following command: `python manage.py runserver` and it will point to the `localhost` with the port.
  9. Hit the `IP Address` on a web browser and use the application.
  
### Dependencies

The following dependencies can be found in [requirements.txt](https://github.com/radonys/Reddit-Flair-Detector/blob/master/requirements.txt):

  1. [praw](https://praw.readthedocs.io/en/latest/)
  2. [scikit-learn](https://scikit-learn.org/)
  3. [nltk](https://www.nltk.org/)
  4. [Django](https://www.djangoproject.com/)
  5. [bs4](https://pypi.org/project/bs4/)
  6. [pandas](https://pandas.pydata.org/)
  7. [numpy](http://www.numpy.org/)
  
### Approach

The data has been taken from [A Benchmark Dataset for Learning to Intervene in Online Hate Speech](https://github.com/jing-qian/A-Benchmark-Dataset-for-Learning-to-Intervene-in-Online-Hate-Speech) to build a ML model. I used Logistic Regression, Random Forest and Linear SVM model and found Random Forest to be best performing model (see results below).

The idea is to collect hate-speech data from the user by just entering the URL of the Reddit post. In the background, we populate the data in our database (not implemented) and also check the hate-speech classification using our developed model.

In this way, we are able to provide user and ML-model based classifications to the social-media platform (the model provides hate-speech classifcation for title, body and top-level comments of the Reddit Post).
    
### Results Hate-Speech Classification

| Machine Learning Algorithm | Test Accuracy     |
| -------------              |:-----------------:|
| Linear SVM                 | 0.82      |
| Logistic Regression        | 0.83  |
| Random Forest              | **0.91**      |

### References

1. [How to scrape data from Reddit](http://www.storybench.org/how-to-scrape-reddit-with-python/)
2. [Multi-Class Text Classification Model Comparison and Selection](https://towardsdatascience.com/multi-class-text-classification-model-comparison-and-selection-5eb066197568)
