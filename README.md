# Dress Pattern Recognition using CNN

Task: To build an image recognition model which is capable of identifying the pattern on a dress image.

Predicts The dress pattern and suggests similar pattern dress images. Useful in e-commerce websites to suggest customer similar dresses based on their preferences.

Total number of dress pattern available in dataset are 17: 

'animal', 'cartoon', 'chevron', 'floral', 'geometry', 'houndstooth', 'ikat', 'letter_numb', 'OTHER', 'plain', 'polka dot', 'scales', 'skull', 'squares', 'stars', 'stripes', 'tribal'


## Project description

`create_dataset.py`


Create folder for each category. Two folders named dataset_category and dataset_category_test for train and test dataset. 
Images are downloaded from AWS s3 bucket and saved into their respective category folders.



`model.ipynb `

Train a CNN for the given 17 classes. The training accuracy is 96.32% and validation accuracy is 95.03%.
After training the model, save the model and its weight.


`image_similarity.ipynb`

Predict the category of given image and suggest similar images.


## Results
Model prediction for stripes dress image.

![Prediction](https://github.com/aakashjhawar/dress-pattern-recognition-using-CNN/blob/master/prediction.png)

---

Another possible method to solve the above problem.

1. Get the image using response.get
2. Convert the 3D image into 2D and save it in the csv file next to the AWS S3 bucket URL.
3. Provide the 2D image matrix as input to the NN.  
I have included the screenshot of csv file.


---
