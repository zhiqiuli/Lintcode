Disjoint-set/Union-find Forest
 
Find(x): find the root/cluster-id of x
Union(x, y): merge two clusters
 
Check whether two elements are in the same set or not in O(1)*.
 
Find: O(a(n))* ~= O(1)
Union: O(a(n))* ~= O(1)
Space: O(n)
 
Without optimization: Find: O(n)
Two key optimizations:
Path compression: make tree flat
Union by rank: merge low rank tree to high rank one
 
*: amortized
 
 
Optimization 1: Path compression, happened during Find
 
Optimization 2: Union by rank, merge low rank tree into high rank on one.
If two sub-tree has the same rank, break tie arbitrarily and increase the merged tree’s rank by 1
Reduce path compression overhead.
