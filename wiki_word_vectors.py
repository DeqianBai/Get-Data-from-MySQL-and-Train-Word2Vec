#！/usr/bin/env python
#  -*- coding:utf-8 -*-
#  author:dabai time:2019/8/9


from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import logging
import time
start = time.time()

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

outp1 = 'model/1st/zhiwiki_news.model'
outp2 = 'model/1st/word2vec_format'
wiki_news = open('./data/reduce_zhiwiki.txt', 'r', encoding='utf-8')
model = Word2Vec(LineSentence(wiki_news), sg=0, size=200, window=5, min_count=5, workers=6)

model.save('./model/1st/zhiwiki_news.word2vec')
model.save(outp1)
model.wv.save_word2vec_format(outp2, binary=False)

end = time.time()
print((end - start)/60, "min")
