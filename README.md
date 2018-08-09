# Doppelganger Project

## Overview

Inspired by the big doppelganger craze on social media a view years back, this project allows the user to upload their own personal image into my web app to find out their celebrity lookalike.

This project uses deep learning models to perform facial recognition on each image and measure facial features using OpenCV/dlib libraries.  This creates 128 different "measurements" of each image, and from there we can implement a classification algorithm like SVM to classify future images.  If you input an image that's not in the original dataset (like a picture of yourself), then the model will predict the closest celebrity match.

 

## How the web app works

{insert link/video here to show uploading image through web app and it's prediction}

Once in the web app (via Flask), you can upload an image which is saved to a local directory on your computer.  From the if you hit the "Predict your Doppelganger" button, the app will run the image through our pretrained classifier model which includes over 200k images of 1500 different celebrities ranging from Angelina Jolie to Abraham Lincoln.  This will return a celebrity name, along with an image of that celebrity.  

## Running on your own computer

{insert link to installation instructions/requirements file}


