#！/usr/bin/env python
#  -*- coding:utf-8 -*-
#  author:dabai time:2019/8/9


from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import logging
import time
start = time.time()

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


# model = Word2Vec(PathLineSentences(), sg=0, size=100, window=5, min_count=5, workers=6)
# input_dir = "./data/"
outp1 = 'model/2nd/all.model'
outp2 = 'model/2nd/word2vec_format'

model = Word2Vec.load('./model/1st/zhiwiki_news.word2vec')

sentences_file = './data/sentences-cut.txt'
model.train(LineSentence(sentences_file), total_examples=model.corpus_count,epochs=model.epochs)
vector_path = './model/2nd/all.word2vec'

model.save(vector_path)
model.save(outp1)
model.wv.save_word2vec_format(outp2, binary=False)

end = time.time()
print((end - start)/60, "min")
