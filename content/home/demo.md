+++
# A Demo section created with the Blank widget.
# Any elements can be added in the body: https://sourcethemes.com/academic/docs/writing-markdown-latex/
# Add more sections by duplicating this file and customizing to your requirements.

widget = "blank"  # See https://sourcethemes.com/academic/docs/page-builder/
headless = true  # This file represents a page section.
active = true  # Activate this widget? true/false
weight = 20  # Order that this section will appear.

title = "About"

[design]
  # Choose how many columns the section has. Valid values: 1 or 2.
  columns = "1"

[design.background]
  # Apply a background color, gradient, or image.
  #   Uncomment (by removing `#`) an option to apply it.
  #   Choose a light or dark text color by setting `text_color_light`.
  #   Any HTML color name or Hex value is valid.

  # Background color.
  # color = "navy"
  
  # Background gradient.
  # gradient_start = "DeepSkyBlue"
  # gradient_end = "SkyBlue"
  
  # Background image.
  #image = "headers/background_imageu.jpg"  # Name of image in `static/img/`.
  #image_darken = 0.2  # Darken the image? Range 0-1 where 0 is transparent and 1 is opaque.

  # Text color (true=light or false=dark).
  text_color_light = false

[design.spacing]
  # Customize the section spacing. Order is top, right, bottom, left.
  padding = ["20px", "0", "20px", "0"]

[advanced]
 # Custom CSS. 
 css_style = ""
 
 # CSS class.
 css_class = ""
+++

A central goal in the field of Computer Vision is image understanding. In general, appearance cues are used to detect components of interest and then spatial and hierarchical relations among these components are used to "describe" the image content at the semantic level of interest. Current deep models have reached a stage of evolution in which they are able to learn and transfer low level features from one domain to another. However, structural information of images such as spatial and hierarchical relations between constituent components are still explicitly modeled using case specific details. This makes models harder to be understood, useful only for few specific applications, and implications on training data preparation effort is still unclear. The aim of this project is the development of a structure-aware-semantics-unaware deep model, with abilities to learn and encode structural information regardless of the semantic level of image components. This should impact model understandability (as structural information would be more explicitly encoded) and training data requirements (as transfer learning would be possible). Theoretical studies, development of visualization strategies and new deep models, and experimentation with respect to diverse computer vision tasks are planned. (AU)
