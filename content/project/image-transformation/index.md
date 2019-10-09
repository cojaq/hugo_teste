---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Image Transformation"
summary: "Smart transformations"
authors: []
tags: 
 - High risk transform
 - Image Analysis
 - Image process
categories: 
 - Image Analysis
 - Image Process
date: 2019-09-08T13:09:50-03:00

# Optional external URL for project (replaces project detail page).
external_link: ""

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: "smart"
  preview_only: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""
---

_Image transformation_ is a common task in many image analysis and understanding projects. For instance, one may find Morphological Operators to be particularly well suited to process a specific family of images. However, finding the right parameters and composition of these operators may not a simple task. In other situations, one may have no clue about how to start.

In such scenarios, the task of transforming input images into desired output images can be formulated as a machine learning problem.

Previous reference works:

 * TRIOSLib: a Python library with functions that help learning locally defined image transformations
 * The tutorial paper Image Operator Learning and Applications, by Igor S. Montagner, N. S. T. Hirata and R. Hirata

Ongoing works:

 * employing fully convolutional and other modern image-to-image networks 
