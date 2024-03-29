---
title: "A Machine Learning Approach for Graph-Based Page Segmentation"
date: 2018-10-01
publishDate: 2019-10-19T00:44:13.995351Z
authors: ["ana-maia", "frank-aguilar", "nina"]
publication_types: ["1"]
abstract: "We propose a new approach for segmenting a document image into its page components (e.g. text, graphics and tables). Our approach consists of two main steps. In the first step, a set of scores corresponding to the output of a convolutional neural network, one for each of the possible page component categories, is assigned to each connected component in the document. The labeled connected components define a fuzzy over-segmentation of the page. In the second step, spatially close connected components that are likely to belong to a same page component are grouped together. This is done by building an attributed region adjacency graph of the connected components and modeling the problem as an edge removal problem. Edges are then kept or removed based on a pre-trained classifier. The resulting groups, defined by the connected subgraphs, correspond to the detected page components. We evaluate our method on the ICDAR2009 dataset. Results show that our method effectively segments pages, being able to detect the nine types of page components. Furthermore, as our approach is based on simple machine learning models and graph-based techniques, it should be easily adapted to the segmentation of a variety of document types."
featured: false
publication: "*2018 31st SIBGRAPI Conference on Graphics, Patterns and Images (SIBGRAPI)*"
tags: ["convolutional neural nets","document image processing","graph theory","image segmentation","learning (artificial intelligence)","edge removal problem","close connected components","fuzzy over-segmentation","convolutional neural network","page components detection","document image","machine learning approach","graph-based page segmentation","Image segmentation","Layout","Image edge detection","Machine learning","Training","Page segmentation", "document image", "machine learning", "graph", "connected components classification", "convolutional neural network"]
doi: "10.1109/SIBGRAPI.2018.00061"
---

