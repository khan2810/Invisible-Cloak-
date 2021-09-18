# Invisible-Cloak
* Here we will try to implement an invisibility cloak using python which will work with cloaks of some basic colors like blue, green, red, white, yellow etc.
---
* If you have ever seen the movie harry potter, you would have definitely thought about that invisible cloak. it was not that magical, python is the solution for that.
* It can be made using an image processing technique called Color detection and segmentation.
* We can use it using a single-color cloth. The cloth should not contain any other color visible and the cloth color should be unique relative to the background.
* The key idea behind this, is to replacing the current frame corresponding to the cloth color with initially captured background frame means wherever that particular color is present in current frame, we will replace those places(pixels) with previously stored background.
## Libraries used