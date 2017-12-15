# -*- coding: utf-8 -*-
"""
Created on Sun May  7 14:09:53 2017

@author: zzpp220
"""
from tempfile import mkdtemp
import shutil
from functools import partial

import numpy as np
from scipy import sparse
from scipy.cluster import hierarchy

from sklearn.utils.testing import assert_true
from sklearn.utils.testing import assert_raises
from sklearn.utils.testing import assert_equal
from sklearn.utils.testing import assert_almost_equal
from sklearn.utils.testing import assert_array_almost_equal
from sklearn.utils.testing import assert_raise_message
from sklearn.utils.testing import ignore_warnings

from sklearn.cluster import ward_tree
from sklearn.cluster import AgglomerativeClustering, FeatureAgglomeration
from sklearn.cluster.hierarchical import (_hc_cut, _TREE_BUILDERS,
                                          linkage_tree)
from sklearn.feature_extraction.image import grid_to_graph
from sklearn.metrics.pairwise import PAIRED_DISTANCES, cosine_distances,\
    manhattan_distances, pairwise_distances
from sklearn.metrics.cluster import normalized_mutual_info_score
from sklearn.neighbors.graph import kneighbors_graph
from sklearn.cluster._hierarchical import average_merge, max_merge
from sklearn.utils.fast_dict import IntFloatDict
from sklearn.utils.testing import assert_array_equal
from sklearn.utils.testing import assert_warns

def test_agglomerative_clustering():
    # Check that we obtain the correct number of clusters with
    # agglomerative clustering.
    rng = np.random.RandomState(0)
    mask = np.ones([10, 10], dtype=np.bool)
    n_samples = 100
    X = rng.randn(n_samples, 50)
    connectivity = grid_to_graph(*mask.shape)
    for linkage in ("ward", "complete", "average"):
        clustering = AgglomerativeClustering(n_clusters=10,
                                             connectivity=connectivity,
                                             linkage=linkage)
        clustering.fit(X)
        # test caching
        try:
            tempdir = mkdtemp()
            clustering = AgglomerativeClustering(
                n_clusters=10, connectivity=connectivity,
                memory=tempdir,
                linkage=linkage)
            clustering.fit(X)
            labels = clustering.labels_
            assert_true(np.size(np.unique(labels)) == 10)
        finally:
            shutil.rmtree(tempdir)
        # Turn caching off now
        clustering = AgglomerativeClustering(
            n_clusters=10, connectivity=connectivity, linkage=linkage)
        # Check that we obtain the same solution with early-stopping of the
        # tree building
        clustering.compute_full_tree = False
        clustering.fit(X)
        assert_almost_equal(normalized_mutual_info_score(clustering.labels_,
                                                         labels), 1)
        clustering.connectivity = None
        clustering.fit(X)
        assert_true(np.size(np.unique(clustering.labels_)) == 10)
        # Check that we raise a TypeError on dense matrices
        clustering = AgglomerativeClustering(
            n_clusters=10,
            connectivity=sparse.lil_matrix(
                connectivity.toarray()[:10, :10]),
            linkage=linkage)
        assert_raises(ValueError, clustering.fit, X)

    # Test that using ward with another metric than euclidean raises an
    # exception
    clustering = AgglomerativeClustering(
        n_clusters=10,
        connectivity=connectivity.toarray(),
        affinity="manhattan",
        linkage="ward")
    assert_raises(ValueError, clustering.fit, X)

    # Test using another metric than euclidean works with linkage complete
    for affinity in PAIRED_DISTANCES.keys():
        # Compare our (structured) implementation to scipy
        clustering = AgglomerativeClustering(
            n_clusters=10,
            connectivity=np.ones((n_samples, n_samples)),
            affinity=affinity,
            linkage="complete")
        clustering.fit(X)
        clustering2 = AgglomerativeClustering(
            n_clusters=10,
            connectivity=None,
            affinity=affinity,
            linkage="complete")
        clustering2.fit(X)
        assert_almost_equal(normalized_mutual_info_score(clustering2.labels_,
                                                         clustering.labels_),
                            1)

    # Test that using a distance matrix (affinity = 'precomputed') has same
    # results (with connectivity constraints)
    clustering = AgglomerativeClustering(n_clusters=10,
                                         connectivity=connectivity,
                                         linkage="complete")
    clustering.fit(X)
    X_dist = pairwise_distances(X)
    clustering2 = AgglomerativeClustering(n_clusters=10,
                                          connectivity=connectivity,
                                          affinity='precomputed',
                                          linkage="complete")
    clustering2.fit(X_dist)
    assert_array_equal(clustering.labels_, clustering2.labels_)
import time

if __name__=="__main__":
    #test_spectral_clustering()
    #test_agglomerative_clustering()
    ref=np.array([[i]*120 for i in range(1,22)])
    ref=np.concatenate([i for i in ref])
    map_file=np.loadtxt('/media/zzpp220/Data/Linux_Documents/Mobile/SpectralClustering/spectral cluster/spectral/map-MFCC_file_load_order.txt')
    map_file=map_file.astype(int)
     #X_total=np.loadtxt('/media/zzpp220/Data/Linux_Documents/Mobile/DATA/TRAIN/Mobile_Timit/result/kmeans-iv/iv-2520-800/iv_200_256_800tot_cat.txt')
    X_total=np.loadtxt('/media/zzpp220/Data/Linux_Documents/Mobile/DATA/sparse/2016-08-29--13-256/shiyan/feature/bpSparseTestFeature_560-13-2520.txt',delimiter=',')
    X=X_total#X=X_total[map_file==1]##做匹配简直不嫩再方便；
    mask = np.ones([10, 10], dtype=np.bool)
    connectivity = grid_to_graph(*mask.shape)
    agc=AgglomerativeClustering(n_clusters=21,affinity="precomputed",linkage="complete")
    #agc.fit(X)
    
    #eigen_solver : {None, ‘arpack’, ‘lobpcg’, or ‘amg’}
    t_=time.time()
    D = pairwise_distances(X)  # Distance matrix
    S = np.max(D) - D  # Similarity matrix
    #S = sparse.coo_matrix(S)
    t0=time.time()
    sys_pre=agc.fit(S)  #/S  
    #sys_rbf=sp.fit(X)
    t1=time.time()
    sys=agc.labels_
#    sys=dict()
#    sys["sys_rbf"]=
    print "cal affinity sparse-fea spectural-clu: "+str(t0-t_)+"s"
    print "total time sparse-fea spectural-clu: "+str(t1-t0)+"s"
