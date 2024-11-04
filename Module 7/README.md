# Module 7 Notes: Metrics and Model Development 

## Metrics

Metrics should be `unbiased`, universal, and concise.
    1. A way to obtain similar responses
    2. A way to measure the performance
    3. A way to measure prediction

For our sample analysis we will use `KNN` K-nearest Neighbor
- `K` is an arbitrary pick
- Need a 'base case`
- Compare the neighbors
- Sort the results 

Dataset for this analysis: 
``` bash
icarus.cs.weber.edu:~hvalle/cs4580/data/movies.csv
```

### KNN-Euclidean Distance

Note: All code 

The Euclidean distance is the distance between points in `N-dimensional` space

Formula
$
d(p, q) = \sqrt{\sum_{i=1}^n (q_i - p_i)^2}
$

Where:
- $p = (p_1, p_2, \dots, p_n)$
- $p = (q_1, q_2, \dots, q_n)$

#### task:
Fidn the distance between these points:
- x = (0, 0)
- y = (4, 4)

Distance = 5.65685...

``` python
# see
def euclidean_distance()
```

### KNN with Jaccard Similarity Index
Compares members of two individual sets to determine which members are `shared` and which are `distinct`.
The index measures the similarity between the two sets.

$$
J(A, B) = \frac{|A \cap B|}{|A \cup B|}
$$

Ex: $A = {1, 2, 3, 4}$ and $B = {3, 4, 5, 6}$ = $\frac{2}{6}$ or $0.333$

``` python
# see
def jaccard_similarity_normal()
```