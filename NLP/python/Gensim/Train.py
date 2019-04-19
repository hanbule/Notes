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
