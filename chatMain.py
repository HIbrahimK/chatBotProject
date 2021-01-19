import warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=FutureWarning)
    from tensorflow.keras.models import load_model
import nltk
import tensorflow as tf
from snowballstemmer import TurkishStemmer
import numpy as np
import random
import json
#import requests
#import bs4

# nltk.download('punkt')

# Json dosyası olarak oluşturulan Covid-19 metin veri setini yükleme
with open(r"covidDataset.json", encoding="utf8") as file:
    data = json.load(file)

# Değişken tanımlamaları
stemmer = TurkishStemmer()
words = []
labels = []
docs_x = []
docs_y = []
tag = " "
global cevap
# Cümlelerin kelimelere ve etiketlere ayrılması
for intent in data["intents"]:
    for pattern in intent["patterns"]:
        wrds = nltk.word_tokenize(pattern)
        words.extend(wrds)
        docs_x.append(wrds)
        docs_y.append(intent["tag"])

    if intent["tag"] not in labels:
        labels.append(intent["tag"])

# Cümlelerin küçük harfe alınması ve ayrılması
words = [stemmer.stemWord(w.lower()) for w in words if w != "?"]
words = sorted(list(set(words)))

# Etiketlerin alfabetik sıralanması
labels = sorted(labels)

# Eğitilmiş ağırlık dosyasının yüklenmesi.
# Eğitilmiş ağırlık dosyasının yüklenmesi.

model = load_model('covid.h5')


# Buradaki fonksiyon bot ile konuşan kişinin cümlelerini 1 ve 0'lar ile ifade etmesine yarıyor.
def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]
    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stemWord(word.lower()) for word in s_words]
    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
    #print(np.array(bag))
    return np.array(bag)


# Sohbet fonksiyonu
def chat(message):

    results = model.predict(np.asanyarray([bag_of_words(message, words)]))[0]
    # print(results)
    results_index = np.argmax(results)
    # print("label sayısı",len(labels))
    tag = labels[results_index]
    # print("etiket",tag)
    # print("tahmin",results[results_index] )
    if results[results_index] > 0.85:
        for tg in data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']
        return [random.choice(responses), tag]
    else:
        return ["Tam olarak anlayamadım", "bulanamadı"]


def cevapla(mesaj):
    cevap = chat(mesaj)
    print("*****************", cevap)
    return cevap
