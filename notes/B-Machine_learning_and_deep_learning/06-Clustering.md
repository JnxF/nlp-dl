# Clustering

Outline:
* Unsupervised learning.
* Without labels.
* Clustering similar things.
* K-means.

What is cluster analysis:
* A cluster is a collection of data objects.
* Cluster analysis is grouping similar data instances cacording to their features.

Examples:
* Marketing.
* Land use: similar areas of land.
* Insurance.
* City-planning.
* Earth-quake studies.
* Games.

What is good clustering:
* High intra-class similarity, low inter-class similarity.
* Using a metric: d(i, j).
* Separate "quality" function measures "goodness" of a cluster.

Requirements:
* Scalability
* Different types of attributes.
* Dynamic data
* High dimensionality
* Interpretability and usability
* Incorporation of user-specified constraints

Dissimilarity:
* Data matrix for dissimilarity (just half matrix).

Categories:
* Partitioning. k-means, mixture model, k-medoids.
* Hierarchical. Start from bottom-up or  viceversa.
* Density-based. DBSCAN, OPTICS. Arbitrary shapes.

Partitioning algorithms:
* Building _k_ clusters.
* The global optimal is impracticable.
* Heuristics: k-means, k-medoids, gaussian mixture.

Problems of k-means:
* Relies on distance-from-center. This means, clusters are defined as circles.
* Items are either in or out.
* Sensitive to outliers.

Evaluation of clustering:
* Assess cluster tendency (are there any clusters in the data?)
* Determine the number of clusters in a dataset (how many clusters are there)
* Measuring clustering quality.

Assess cluster tendency:
* Clustering makes no sense if there is no structure in the data.

The hopkins statistic:
* Sample n points and compute the distance to their nearest neighbor.
* Generate n points uniformly distributed in the space of D and compute their distance to their nearest neihbor in D.
* Compute the Hopkins test: H.
* A mesure of whether the data is uniformly distributed.

Determining the number of clusters in a dataset:
* Elbow method: increase the number of clusters, the sum of within-cluster variance of each cluster.
* Run clustering for different parameters.

Evaluating clustering:
* High intra-class similarity, low inter-class similarity.
* Methods: intrinsic methods (we do not have the groud truth data), extrinsic evaluation (we have the ground truth, we compare the clustering with the ground truth).

Silhouette coefficient.