# GENSIM TRAINING:
# Gensim ver:3.5.0

# 1
# provide sentences in form of lists, in current example three sentences provided.
sentences_ls = [['I','like','deep learning'],['I', 'like','NLP'],['I','enjoy','flying']]


#2 
# Set parameters
num_features = 128     # Word vector dimensionality. (default=100)
min_word_count = 1     # ignore words that are less than count of min_word_count in corpus. (default=5)
num_workers = 8        # Number of threads to run in parallel
context = 10           # Context window size
downsampling = 1e-3    # Downsample setting for frequent words
iter_ = 1000
sg = 1  # if 1 skip-gram technique is used, else CBoW. (default=0)


# 2.1
# Print parameters
print('\nModel parameters')
print('%-20s' % '   Word vector size',':',num_features)
print('%-20s' % '   min word count',':',min_word_count)
print('%-20s' % '   Window size',':',context)
print('%-20s' % '   Iterations',':',iter_)
print('%-20s' % '   Techinque used',':',('Skip-gram' if sg == 1 else 'CBoW'))   
print('\nTraining Word2Vec model ...\n')



# 3 
# Start training Word2Vec model
model = word2vec.Word2Vec(sentences_ls, sg = 1, workers = num_workers, size = num_features, iter = iter_, min_count = min_word_count, window = context, sample = downsampling, seed = 1)


## If Word2Vec model training finished and no more updates, only querying
model.init_sims(replace=True)


# 4
# Save model
model_name = 'word2vect_vec'+str(num_features)+'_win'+str(context)
model.save(model_name)


# 4.1
# Loading model
model_file_path = ''
model = word2vec.Word2Vec.load(model_file_path)

# 4.2
# iterating whole vocab of the model.
for word in model.wv.vocab:

# or get vocab as a list
words_vocab_ls = model.wv.vocab.keys()

# 4.3
# get vocab with word frequencies
words_freq = {}
for w in model.wv.vocab:
    words_freq[w] = model.wv.vocab[w].count



# GENSIM FUNCTIONS

# Args: word that exists  trained word2vec model.
# returns top N closest words from trained word2vec model.
model.most_similar(word, topn=10)

# figure out difference from model.most_similar
model.similar_by_word(word)

# Args:
# word_vec_1, word_vec_2: 2 word vectors from trained word2vec model.
# returns: cosine similarity of word vectors.
model.similarity(word_vec_1, word_vec_2)


# CUSTOM FUNCTIONS

## Vector distances:
# Args:
# word_vec_1, word_vec_2: 2 word vectors from trained word2vec model.

# wroks the same as gensim's native function
# model.similarity(word_vec_1, word_vec_2)
def get_cosine_similarity(word_vec_1, word_vec_2):
    cosine_similarity = np.dot(word_vec_1, word_vec_2)/ \
                        (np.linalg.norm(word_vec_1)* np.linalg.norm(word_vec_2))
    return cosine_similarity

def get_euclidian_distance(word_vec_1, word_vec_2):
    distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(word_vec_1, word_vec_2)]))
    return distance

# works way faster than get_cosine_similarity
def get_euclidian_distance_2(word_vec_1, word_vec_2):

    return np.linalg.norm(word_vec_1 - word_vec_2)


# CUSTOM FUNCTIONS USING TSNE.

# Args:
# model: trained word2vec model
# word: word that exists in trained word2vec model vocab.
# word2vec_size: vector length of words in trained word2vec model.

# Output:
# Shows 2D sctterplot in new window
def display_closest_words_tsne_scatterplot_2D(model, word, word2vec_size):

    arr = np.empty((0, word2vec_size), dtype='f')
    word_labels = [word]

    # get close words
    close_words = model.similar_by_word(word)

    # add the vector for each of the closest words to the array
    arr = np.append(arr, np.array([model[word]]), axis=0)
    for wrd_score in close_words:
        wrd_vector = model[wrd_score[0]]
        word_labels.append(wrd_score[0])
        arr = np.append(arr, np.array([wrd_vector]), axis=0)
        
    # find tsne coords for 2 dimensions
    tsne = TSNE(n_components=2, random_state=0)
    np.set_printoptions(suppress=True)
    Y = tsne.fit_transform(arr)

    x_coords = Y[:, 0]
    y_coords = Y[:, 1]
    # display scatter plot
    plt.scatter(x_coords, y_coords)

    for label, x, y in zip(word_labels, x_coords, y_coords):
        plt.annotate(label, xy=(x, y), xytext=(0, 0), textcoords='offset points')
    plt.xlim(x_coords.min()+0.00005, x_coords.max()+0.00005)
    plt.ylim(y_coords.min()+0.00005, y_coords.max()+0.00005)
    plt.show()

def display_closest_words_tsne_scatterplot_1D(model, word, word2vec_size):

    arr = np.empty((0, word2vec_size), dtype='f')
    word_labels = [word]

    # get close words
    close_words = model.similar_by_word(word)

    # add the vector for each of the closest words to the array
    arr = np.append(arr, np.array([model[word]]), axis=0)
    for wrd_score in close_words:
        wrd_vector = model[wrd_score[0]]
        word_labels.append(wrd_score[0])
        arr = np.append(arr, np.array([wrd_vector]), axis=0)
        
    # find tsne coords for 2 dimensions
    tsne = TSNE(n_components=1, random_state=0)
    np.set_printoptions(suppress=True)
    Y = tsne.fit_transform(arr)
    print('tsne shape:', Y.shape)
    print('tsne type:', type(Y.ravel().tolist()))

    for i,l in zip(Y.ravel().tolist(),word_labels):
        print('Y:',i,l)

    x_coords = Y[:, 0]
    #y_coords = Y[:, 1]
    # display scatter plot
    #plt.scatter(x_coords, y_coords)
    #plt.plot(Y.ravel(),np.ones(np.shape(Y.ravel())),'*',markersize=10)

    # val = 0. # this is the value where you want the data to appear on the y-axis.
    # ar = np.arange(10) # just as an example array
    # plt.plot(Y.ravel(), np.zeros_like(Y.ravel()) + val, 'x')

    #plt.plot(Y.ravel().tolist(), len(Y.ravel().tolist()) * [1], "x")
    # plt.plot(Y)
    #plt.show()


    x_coords = Y.ravel()
    y_coords = np.zeros_like(Y.ravel())
    #y_coords = np.asarray([x*1 for x in range(1,12,100)])

    lim = 0.00005
    lim = 1000
    for label, x, y in zip(word_labels, x_coords, y_coords):
        plt.annotate(label, xy=(x, y), xytext=(0, 0), textcoords='offset points')
    plt.xlim(x_coords.min()+lim, x_coords.max()+lim)
    plt.ylim(y_coords.min()+lim, y_coords.max()+lim)
    plt.show()


# Args:
# model: trained word2vec model
# word: words list that exist in trained word2vec model vocab.
# word2vec_size: vector length of words in trained word2vec model.

# Output:
# Each function provides 2D or 3D sctterplot in new window respectively
def display_selected_words_tsne_scatterplot_2D(model, words_ls, word2vec_size):

    arr = np.empty((0, word2vec_size), dtype='f')
    word_labels = []

    # get close words
    #close_words = model.similar_by_word(word)

    # add the vector for each of the closest words to the array
    #arr = np.append(arr, np.array([model[word]]), axis=0)
    for wrd in words_ls:
        wrd_vector = model[wrd]
        word_labels.append(wrd)
        arr = np.append(arr, np.array([wrd_vector]), axis=0)
        
    # find tsne coords for 2 dimensions
    tsne = TSNE(n_components=2, random_state=0)
    np.set_printoptions(suppress=True)
    Y = tsne.fit_transform(arr)

    x_coords = Y[:, 0]
    y_coords = Y[:, 1]
    # display scatter plot
    plt.scatter(x_coords, y_coords)

    for label, x, y in zip(word_labels, x_coords, y_coords):
        plt.annotate(label, xy=(x, y), xytext=(0, 0), textcoords='offset points')
    plt.xlim(x_coords.min()+0.00005, x_coords.max()+0.00005)
    plt.ylim(y_coords.min()+0.00005, y_coords.max()+0.00005)
    plt.show()

def display_selected_words_tsne_scatterplot_3D(model, words_ls, word2vec_size):

	arr = np.empty((0, word2vec_size), dtype='f')
	word_labels = []

    # get close words
    #close_words = model.similar_by_word(word)

    # add the vector for each of the closest words to the array
    #arr = np.append(arr, np.array([model[word]]), axis=0)
	for wrd in words_ls:
		wrd_vector = model[wrd]
		word_labels.append(wrd)
		arr = np.append(arr, np.array([wrd_vector]), axis=0)
        
    # find tsne coords for 2 dimensions
	tsne = TSNE(n_components=3, random_state=0)
	np.set_printoptions(suppress=True)
	Y = tsne.fit_transform(arr)

	x_coords = Y[:, 0]
	y_coords = Y[:, 1]
	z_coords = Y[:, 2]

	# display scatter plot
	fig=plt.figure()
	ax = fig.gca(projection='3d')
	#cset = ax.contour(x_coords, y_coords, z_coords) #, 16, extend3d=True)

	for x,y,z,word in zip(x_coords, y_coords, z_coords, words_ls):
		#ax.plot(x,y,z, 'gray')  # draws line
		ax.scatter(x,y,z, c='blue', edgecolors='none', s=50)  # draws dots
		ax.text(x,y,z, word, size=10, zorder=1, color='k') # puts annotations over dots

	ax.set_xlabel('x')
	ax.set_ylabel('y')
	ax.set_zlabel('z')
	plt.show()





