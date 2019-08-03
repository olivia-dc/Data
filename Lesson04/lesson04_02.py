import logging
import sys

from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


def my_function():
    """单词词向量训练
    training on a 1024066165 raw words (789407877 effective words) took 724.0s, 1090418 effective words/s"""
    wiki_news = open('reduce_zhiwiki.txt', 'r', encoding='utf-8')
    model = Word2Vec(LineSentence(wiki_news), sg=0, size=200, window=5, min_count=5, workers=6)
    model.save('./model/zhiwiki_news.word2vec')


if __name__ == '__main__':
    my_function()