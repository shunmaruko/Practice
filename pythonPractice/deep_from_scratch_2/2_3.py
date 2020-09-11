import numpy as np
"""
copus (text data arranged for natural language processing)
the code is for preprocessing corpus
"""
def preprocess(text):
    #split words and period,kannm
    words = text.lower().replace("."," .").split(' ')
    #initialize dictinoary
    word_to_id = {}
    id_to_word = {}

    for word in words:
        if word not in word_to_id:#id already exists, skip the word
            new_id = len(word_to_id)
            word_to_id[word] = new_id
            id_to_word[new_id] = word
    # make list of word id
    #corpus is id of word
    corpus = np.array([word_to_id[w] for w in words])# convert to np.ndarray
    return corpus, word_to_id, id_to_word
"""
Distributional hypothesis
Purpose : express word as vector
How : Judge from context
  Eg,"I drink beer"
     "We drink wine"
     "We guzzle beer"
  Apparently, "guzzle" have same meaning as "drink"
Question: how long the context is ? => window size
"""
#make Co-occurence matrix when window size is 1 
C = np.array([
    [0,1,0,0,0,0,0],
    [1,0,1,0,1,1,0],
    [0,1,0,1,0,0,0],
    [0,0,1,0,1,0,0],
    [0,1,0,1,0,0,0],
    [0,1,0,0,0,0,1],
    [0,0,0,0,0,1,0],
], dtype=np.int32)

def create_co_matrix(corpus,vocab_size,window_size=1):
    corpus_size = len(corpus)
    co_matrix = np.zeros((vocab_size,vocab_size), dtype=np.int32)
    for i in range(corpus_size):
        icorpus = corpus[i]
        for j in range(1,window_size):
            print(i,j)
            right_index = corpus[i+j]
            #1_index = i + j
            if right_index < corpus_size:
                co_matrix[icorpus][right_index] += 1
            left_index = corpus[i-j]
            #1_index = i - j
            if left_index >= 0:
                co_matrix[icorpus][left_index] += 1

    return co_matrix


if(__name__=="__main__"):
    #sample text
    text = 'You say goodbye and I say hello.'
    corpus, word_to_id, id_to_word =  preprocess(text)
    print(corpus)
    print(word_to_id)
    print(create_co_matrix(corpus,7))

