import numpy as np, pandas as pd

import re
import spacy
from spacy.lang.en import English
from spacy.lang.en.stop_words import STOP_WORDS
from nltk.tokenize import word_tokenize
import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
import string
from string import ascii_lowercase

from tqdm import tqdm as tqdm_notebook
import itertools

from functools import reduce
from tensorflow import keras
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Dense, Input, LSTM, Embedding, Dropout, Activation
from keras.layers import Bidirectional, GlobalMaxPool1D
from keras.models import Model
from keras.models import Sequential
from keras.layers import Conv1D, MaxPooling1D
from keras.layers import BatchNormalization
from keras import initializers, regularizers, constraints, optimizers, layers

processed_train_data = [] 
with open("web/models_data/output.txt", "r") as txt_file:
    for line in txt_file:
        processed_train_data.append(line)

for i in range(0,len(processed_train_data)):
    processed_train_data[i] = processed_train_data[i].replace("\n", "")

tokenizer = Tokenizer(num_words=100000)
tokenizer.fit_on_texts(list(processed_train_data))
model = keras.models.load_model(filepath="web/models_data")

def toxicity_level(string):
    new_string = [string]
    new_string = tokenizer.texts_to_sequences(new_string)
    new_string = pad_sequences(new_string, maxlen=200, padding='post')
    prediction = model.predict(new_string)

    print("Toxicity level for '{}':".format(string))
    print('Toxic:               {:.0%}'.format(prediction[0][0]))
    print('Severse Toxic:       {:.0%}'.format(prediction[0][1]))
    print('Obscene:             {:.0%}'.format(prediction[0][2]))
    print('Threat:              {:.0%}'.format(prediction[0][3]))
    print('Insult:              {:.0%}'.format(prediction[0][4]))
    print('Identity Hate:       {:.0%}'.format(prediction[0][5]))
    print()

    if(prediction[0][0] < 0.3 and prediction[0][1] < 0.3 and prediction[0][2] < 0.3 and prediction[0][3] < 0.3 and prediction[0][4] < 0.3 and prediction[0][5] < 0.3):
        return 1
    else:
        return 0