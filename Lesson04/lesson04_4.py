import pandas as pd

pd.options.mode.chained_assignment = None
import numpy as np
import re
import nltk
from gensim.models import word2vec

from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from gensim.models.word2vec import LineSentence
# % matplotlib inline


def tsne_plot(model):
    "Creates and TSNE model and plots it,do not sucess"
    labels = []
    tokens = []

    for word in model.wv.vocab:
        tokens.append(model[word])
        labels.append(word)

    tsne_model = TSNE(perplexity=40, n_components=2, init='pca', n_iter=2500, random_state=23)
    new_values = tsne_model.fit_transform(tokens)

    x = []
    y = []
    for value in new_values:
        x.append(value[0])
        y.append(value[1])

    plt.figure(figsize=(16, 16))
    for i in range(len(x)):
        plt.scatter(x[i], y[i])
        plt.annotate(labels[i],
                     xy=(x[i], y[i]),
                     xytext=(5, 2),
                     textcoords='offset points',
                     ha='right',
                     va='bottom')
    plt.show()

if __name__ == '__main__':
    wiki_news = open(r'D:\NLP course\lesson04\reduce_zhiwiki.txt','r',encoding = 'utf-8')
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    model2 = word2vec.Word2Vec(LineSentence(wiki_news),sg=0, size=200, window=10, min_count=500, workers=6)
    print(model.wv['学习'])
    # tsne_plot(model2)