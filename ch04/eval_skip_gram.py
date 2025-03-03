# coding: utf-8
import sys
sys.path.append('..')
from common.util import most_similar, analogy
import pickle


# pkl_file = 'cbow_params.pkl'
pkl_file = 'skip_gram_params.pkl'

with open(pkl_file, 'rb') as f:
    params = pickle.load(f)
    word_vecs = params['word_vecs']
    word_to_id = params['word_to_id']
    id_to_word = params['id_to_word']

# most similar task
# skip gram的结果没有问题
querys = ['you', 'year', 'car', 'toyota']
for query in querys:
    most_similar(query, word_to_id, id_to_word, word_vecs, top=5)

# # analogy task
# # skip gram的analogy有问题，可能是方法的问题。不能够直接把analogy的方法拿过来用
# print('-'*50)
# analogy('king', 'man', 'queen',  word_to_id, id_to_word, word_vecs)
# analogy('take', 'took', 'go',  word_to_id, id_to_word, word_vecs)
# analogy('car', 'cars', 'child',  word_to_id, id_to_word, word_vecs)
# analogy('good', 'better', 'bad',  word_to_id, id_to_word, word_vecs)
