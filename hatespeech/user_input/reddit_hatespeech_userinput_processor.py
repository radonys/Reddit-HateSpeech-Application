# -*- coding: utf-8 -*-
"""Reddit-HateSpeech-UserInput-Processor.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LP2KEUAiEt6P2sU3vba0-bpBQUzsXl2F

# Reddit Hate-Speech User Input Collection

## Libraries

### Install
"""

#!pip install praw

"""### Import"""

import sklearn
import pickle
import praw
import re
from bs4 import BeautifulSoup
import nltk
import numpy as np
nltk.download('stopwords')
from nltk.corpus import stopwords
from django.conf import settings

"""## Variable Declaration"""

reddit = praw.Reddit(client_id='#', client_secret='#', user_agent='#', username='#', password='#')

REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
STOPWORDS = set(stopwords.words('english'))

"""## Utility Functions"""

def clean_text(text):
   
    text = BeautifulSoup(text, "lxml").text
    text = text.lower()
    text = REPLACE_BY_SPACE_RE.sub(' ', text)
    text = BAD_SYMBOLS_RE.sub('', text)
    text = ' '.join(word for word in text.split() if word not in STOPWORDS)
    
    return text

def comment_hate_check(comments, loaded_model):

  hate = np.zeros(len(comments))

  for idx in range(0, len(comments)):

    comment = clean_text(comments[idx])
    hate[idx] = loaded_model.predict([comment])

  return hate

"""## Input URL Processing"""

def url_process(url,loaded_model = settings.MODEL_FILE):

  submission = reddit.submission(url=url)

  data = {}

  data['title'] = submission.title
  data['url'] = submission.url
  data['id'] = submission.id
  data['comm_num'] = submission.num_comments
  data['created'] = submission.created
  data['body'] = submission.selftext

  submission.comments.replace_more(limit=None)
  comments = []

  counter = 0

  for top_level_comment in submission.comments:
    
    comments.append(top_level_comment.body)
    counter += 1

    if counter == 5:
      break

  data['hate_user_input'] = 1

  data["comment"] = comments

  data['title'] = clean_text(data['title'])
  data['body'] = clean_text(data['body'])

  data['hate_body'] = loaded_model.predict([data['body']])
  data['hate_title'] = loaded_model.predict([data['title']])
  data['hate_comment_onehot'] = comment_hate_check(comments, loaded_model)

  ## Function sends data to the database

  return 'Input Received'