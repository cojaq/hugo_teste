---
##############
#Core metadata
##############

#the title of your page
title: 

#one-sentence summary of the content on your page. The summary can be shown on the homepage and can also benefit your search engine ranking.
summary: 

#the RFC 3339 date that the page was published. A future date will schedule the page to be published in the future. If you use the hugo new ... commands described on this page, the date will be filled automatically when you create a page. Also see lastmod and publishDate.
date: 

#display the authors of the page and link to their user profiles if they exist. To link to a user profile, create a user based on the admin template and reference their username (the name of a user in your authors folder) in the authors field, e.g. authors: ["admin"].
authors: 

#tagging your content helps users to discover similar content on your site. Tags can improve search relevancy and are displayed after the page content and also in the Tag Cloud widget. E.g. tags: ["Electronics", "Diodes"].
tags: 

#################
#Popular metadata
#################

#an optional subtitle that will be displayed under the title
subtitle: 

#by setting featured: true, a page can be displayed in the Featured widget. This is useful for sticky, announcement blog posts or selected publications etc.
featured: 

#categorizing your content helps users to discover similar content on your site. Categories can improve search relevancy and display at the top of a page alongside a page’s metadata. E.g. categories: ["Art"].
categories: 

#the RFC 3339 date that the page was last modified. If using Git, enable enableGitInfo in config.toml to have the page modification date automatically updated, rather than manually specifying lastmod.
lastmod: 

#the RFC 3339 date that the page was published. You only need to specify this option if you wish to set date in the future but publish the page now, as is the case for publishing a journal article that is to appear in a journal etc.
publishDate: 

#by setting draft: true, only you will see your page when you preview your site locally on your computer
draft: 

##############
#Page features
##############

reading_time: false  # Show estimated reading time?
share: false  # Show social sharing links?
profile: false  # Show author profile?
commentable: false  # Allow visitors to comment? Supported by the Page, Post, and Docs content types.
editable: false  # Allow visitors to edit the page? Supported by the Page, Post, and Docs content types.

########### Example below #############################

title: "Template publication"
authors:
- admin
date: "2019-04-07T00:00:00Z"
doi: ""

draft: true

# Schedule page publish date (NOT publication's date).
publishDate: "2017-01-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["3"]

# Publication name and optional abbreviated publication name.
publication: ""
publication_short: ""

abstract: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum. Sed ac faucibus dolor, scelerisque sollicitudin nisi. Cras purus urna, suscipit quis sapien eu, pulvinar tempor diam. Quisque risus orci, mollis id ante sit amet, gravida egestas nisl. Sed ac tempus magna. Proin in dui enim. Donec condimentum, sem id dapibus fringilla, tellus enim condimentum arcu, nec volutpat est felis vel metus. Vestibulum sit amet erat at nulla eleifend gravida.

# Summary. An optional shortened abstract.
summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

#choose one, or more
#categories: 
# - Image Transformation
# - Object Detection
# - Astronomical Images
# - Document Images
# - Projection Learning

tags:
- Source Themes
featured: false

links:
- name: Custom Link
  url: http://example.org

#url_code and url_dataset are used to show content in (data + code) section
url_code: ""
url_dataset: ""

url_pdf: http://arxiv.org/pdf/1512.04133v1
url_poster: '#'
url_project: ''
url_slides: ''
url_source: '#'
url_video: '#'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: Imagem de [**Alexas_Fotos**](https://pixabay.com/pt/users/Alexas_Fotos-686414/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=3094035) por [**Pixabay**](https://pixabay.com/pt/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=3094035)
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects:
- internal-project

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: example
---

{{% alert note %}}
Click the *Slides* button above to demo Academic's Markdown slides feature.
{{% /alert %}}

Supplementary notes can be added here, including [code and math](https://sourcethemes.com/academic/docs/writing-markdown-latex/).
