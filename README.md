# Invisible-Cloak
* Here we will try to implement an invisibility cloak using python which will work with cloaks of some basic colors like blue, green, red, white, yellow etc.
---
* If you have ever seen the movie harry potter, you would have definitely thought about that invisible cloak. it was not that magical, python is the solution for that.
* It can be made using an image processing technique called [Color detection and segmentation](https://towardsdatascience.com/object-detection-via-color-based-image-segmentation-using-python-e9b7c72f0e11).
* We can use it using a single-color cloth. The cloth should not contain any other color visible and the cloth color should be unique relative to the background.
* The key idea behind this, is to replacing the current frame corresponding to the cloth color with initially captured background frame means wherever that particular color is present in current frame, we will replace those places(pixels) with previously stored background.
## Libraries used
* I have used the opencv, numpy and time libraries to implement this.
* [**_`openCV`_**](https://docs.opencv.org/master/d6/d00/tutorial_py_root.html)  a Python computer-vision library used for accessing the camera and manipulating frames and for color detection and segmentation techniques.
* [**_`numpy`_**](https://numpy.org/doc/)  This module is used for manipulting numbers and for operations related to HSV colour range.
* [**_`time`_**](https://docs.python.org/3/library/time.html)  This module is used for creating a time delay between capturing background frame and current frame.
## How to Use
* for using it, you just need a cloth of single colour like blue, white, red, yellow, green etc.
* To use a particular color cloth, you just need to uncomment the lower and upper bounds for [HSV colour space](https://stackoverflow.com/questions/36817133/identifying-the-range-of-a-color-in-hsv-using-opencv/51686953) value of that color.
* I have used blue color cloth, if you want to try with some other color you can just uncomment that color's HSV bounds and commenting every other color.
* Make sure that your background doesn't contain the color of the cloth you are going to use.
* Run the program and come in front of webcam after 1 or 2 seconds, because it has to store the initial background frame.
* And now you can use your cloak to become invisible in good lighting conditions.
* Be careful in case of black color cloak, because your hairs may be black and your surrounding may have black parts too.
* you can even use multiple color cloth, in that case you have to uncomment the HSV ranges of all the colors the cloth contains because we have to process the current frame for all those colors.
