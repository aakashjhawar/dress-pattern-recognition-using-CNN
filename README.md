Task: To build an image recognition model which is capable of identifying the pattern on a dress image.


`create_dataset.py`


Create 17 folder with the name of categories. Two folders named dataset_category and dataset_category_test for train and test dataset. 
Downloads the images using response.get and save it into their respective categories.

`model.ipynb `


Jupyter notebook file for main model. I have also saved the model and model weights.

`image_similarity.ipynb`


Jupyter notebook file to predict the given image categories and display similar images related to the same.

HTML files of both the Jupyter notebook are also included.


---

Another possible method to solve the above problem.

1. Get the image using response.get
2. Convert the 3D image into 2D and save it in the csv file next to the AWS S3 bucket URL.
3. Provide the 2D image matrix as input to the NN.  
I have included the screenshot of csv file.


---
