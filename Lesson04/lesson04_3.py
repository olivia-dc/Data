import gensim
import pandas as pd
def my_function():
    """查看训练结果"""
    model = gensim.models.Word2Vec.load('./model/zhiwiki_news.word2vec')
    print(model.similarity('专家','工程师'))
    print(model.similarity('专家', '教授'))
    print(model.similarity('专家', '博士'))
    print(model.similarity('专家', '科研人员'))
    print(model.similarity('勇敢', '行动'))
    print(model.similarity('勇敢', '表达'))
    result = pd.Series(model.most_similar(u'学习'))
    print(result)
    result1 = pd.Series(model.most_similar(u'儿童教育'))
    print(result1)
    print(model.wv['学习'])
if __name__ == '__main__':
    my_function()