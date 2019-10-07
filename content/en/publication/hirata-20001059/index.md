---
title: "A switching algorithm for design of optimal increasing binary filters over large windows"
date: 2000-01-01
publishDate: 2019-10-07T17:53:56.210177Z
authors: ["Nina S. T. Hirata", "Edward R. Dougherty", "Junior Barrera"]
publication_types: ["2"]
abstract: "All known approaches for the design of increasing translation-invariant binary window filters involve combinatoric searches. This paper proposes a new switching algorithm having the advantage that the search is over a smaller set than other algorithms. Beginning with an estimate from image realizations of the optimal generic (nonincreasing) window function, the algorithm switches (exchanges) a set of observation vectors (templates) between the optimal function's kernel and the kernel's complement. There are many such “switching sets” that provide a kernel defining an increasing filter. The optimal increasing filter is the one corresponding to the switching set that produces the minimal increase in error over the optimal generic filter. The core of the search problem is the inversion set of the optimal filter. The inversion set is composed of all vectors in the kernel lying beneath a nonkernel vector in the lattice of observation vectors and all nonkernel vectors lying above a kernel vector. The new algorithm, which is based on an error-related greedy property, recursively eliminates the inversion set until the optimal increasing filter is obtained. For purposes of computational efficiency, the actual implementation may be based on a relaxation of the original construction, so that the result may be based on a relaxation of the original construction, so that the result may be suboptimal. For the various models tested, the relaxed algorithm has proven to be optimal or very close to optimal. Besides its good estimation precision, the new algorithm has three noteworthy properties: first, it is applicable to relatively large windows; second, it operates directly on the input data via estimates of the determining conditional probabilities; and third, the degree of relaxation serves as an input parameter to the algorithm, so that computation time can be bounded for large windows and the algorithm can run to full optimality for small windows."
featured: false
publication: "*Pattern Recognition*"
tags: ["Increasing filter", "Optimal filter", "Nonlinear filter", "Boolean lattice", "Switching algorithm", "Greedy algorithm"]
url_pdf: "http://www.sciencedirect.com/science/article/pii/S003132039900165X"
doi: "https://doi.org/10.1016/S0031-3203(99)00165-X"
---

