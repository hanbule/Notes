import numpy as np
from gensim.models import word2vec, Phrases
from sklearn.cluster import KMeans
from time import gmtime, strftime
import time

def get_elapsed_time(start_time):
    elapsed_time = time.time()-start_time
    str_ = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
    return str_

if __name__=="__main__":
    # 1
    # Load model
    model = word2vec.Word2Vec.load(<path>)
    
    # 2
    # Word vecs into matrix  (option 1)
    mtx = []
    for idx, w in enumerate(model.wv.vocab):
        w_vec = model.wv[w]
        mtx.append(w_vec)

        # if(idx > 5):
        # 	break
    mtx = np.array(mtx)
    
    # 3
    # Kmeans params
    rand_state = 1
    jobs = 8                        # threads num
    cl_cnt = len(model.wv.vocab)    # max number of clusters to check

    # 4
    # Cluster data into [1,cl_cnt] clusters and collect errors to make elbow plot
    for k in range (1, cl_cnt+1):
        start_ = time.time()

        kmeans = KMeans(n_clusters=k, random_state=rand_state, n_jobs = jobs)
        kmeans_model = kmeans.fit(mtx)
        labels = kmeans_model.labels_
        interia = kmeans_model.inertia_     # can calculate cost as 𝑆𝑆𝐸=∑𝐾𝑖=1∑𝑥∈𝑐𝑖𝑑𝑖𝑠𝑡(𝑥,𝑐𝑖)2

        print("Clusters cnt: %d  Cost: %d  time spent: %s" % (k, interia, get_elapsed_time(start_)))
