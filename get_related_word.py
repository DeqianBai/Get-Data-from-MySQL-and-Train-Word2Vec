from collections import defaultdict
from gensim.models import Word2Vec
import os

def get_related_words(initial_words, model):
    """
    @initial_words are initial words we already know
    @model is the word2vec model
    """

    unseen = initial_words

    seen = defaultdict(int)

    max_size = 500  # could be greater

    while unseen and len(seen) < max_size:
        if len(seen) % 50 == 0:
            print('seen length : {}'.format(len(seen)))

        node = unseen.pop(0)

        new_expanding = [w for w, s in model.most_similar(node, topn=20)]

        unseen += new_expanding

        seen[node] += 1

        # optimal: 1. score function could be revised
        # optimal: 2. using dymanic programming to reduce computing time

    return seen

def get_words_said(initial_words,model_path):
    model = Word2Vec.load(model_path)
    related_words = get_related_words(initial_words, model)
    related_words = sorted(related_words.items(), key=lambda x: x[1], reverse=True)
    said = [i[0] for i in related_words if i[1] >= 1]
    return said


def save_said(initial_words, model_path):
    said = get_words_said(initial_words,model_path)
    string = '|'.join(said)
    try:
        with open("similar_said.txt", 'w') as f:
            f.write(string)
        return True
    except:
        return False


def load_said(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            string = f.readlines()
            string = string[0].split('|')
            return string



if __name__ == '__main__':

    initial_words = ['说','认为','表示']
    model_path = './model/2nd/all.word2vec'
    
    result = save_said(initial_words,model_path)
    if result:
        string = load_said("./similar_said.txt")
        print(string)



