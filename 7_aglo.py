#Implementation of Agglomerative#

import numpy as np
from scipy.cluster import hierarchy
from scipy.spatial import distance
import matplotlib.pyplot as plt

points = [(18, 0), (22, 0), (43, 0), (42, 0), (27, 0), (25, 0)]
names = ["p1", "p2", "p3", "p4", "p5", "p6"]

x = distance.pdist(points, 'euclidean')
 
# Plot the hierarchical clustering as a dendrogram.
temp = hierarchy.linkage(x, 'single')
plt.figure()
dn = hierarchy.dendrogram(temp, labels=names)
plt.title("Hierarchical Clustering : Aglomerative")
plt.show()
