# Plastic-Recyclability
## About
I created this project individually as the final project for CS175 Projects in Artificial Intelligence. The goal of this project is to classify images of plastics into recyclable or non-recyclable plastics. 
## Problem Statement
Many people assume all plastics are recyclable, but this is not necessarily true. Different recycling centers in different areas only process certain types of plastics, while other plastics are directed towards landfill. Misguided waste disposal is problematic because recycling centers process waste in large batches, and if the batch has a certain percentage of non-recyclables, the entire batch is moved over to landfill. Therefore, an improperly recycled item could cause correctly recycled waste to end up in landfill.
## Implementation
I tacked the problem of classifying plastic images with deep learning. To compare various models, I trained a plain convolutional network in `plain_train.ipynb`, and a residual network(https://arxiv.org/pdf/1512.03385.pdf) in `res_train.ipynb`. Training takes 20-30 minutes using Google colab GPUs. To understand the data used, look in the `data` subdirectory. Results are in image files in the `results` subdirectory.

