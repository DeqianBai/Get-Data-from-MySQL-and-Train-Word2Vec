#！/usr/bin/env python
#  -*- coding:utf-8 -*-
#  author:dabai time:2019/8/9

from gensim.corpora import WikiCorpus
import jieba
from hanziconv import HanziConv


def extract_function():
    space = ' '
    i = 0
    l = []
    zhwiki_name = './data/zhwiki-20190720-pages-articles-multistream.xml.bz2'
    f = open('./data/reduce_zhiwiki.txt', 'w', encoding='utf-8')
    wiki = WikiCorpus(zhwiki_name, lemmatize=False, dictionary={})  # 从xml文件中读出训练语料
    for text in wiki.get_texts():
        for temp_sentence in text:
            temp_sentence = HanziConv.toSimplified(temp_sentence)  # 繁体中文转为简体中文
            seg_list = list(jieba.cut(temp_sentence))  # 分词
            for temp_term in seg_list:
                l.append(temp_term)
        f.write(space.join(l) + '\n')
        l = []
        i = i + 1

        if (i % 200 == 0):
            print('Saved ' + str(i) + ' articles')
    f.close()



if __name__ == '__main__':
    
    extract_function()