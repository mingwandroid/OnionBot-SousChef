![Header](https://user-images.githubusercontent.com/32883278/97621285-a4208a80-1a1a-11eb-8b7f-90141d867982.png)

# OnionBot | Python API

<p float="left">
    <img src="https://www.raspberrypi.org/wp-content/uploads/2011/10/Raspi-PGB001.png" height="100"/>
    <img src="https://www.nasuni.com/wp-content/uploads/2019/10/googleCloudPartner.png" height="100"/>
    <img src="https://miro.medium.com/max/400/0*xNxZokzztcgpPueM.png" height="100"/>
    <img src="https://user-images.githubusercontent.com/32883278/84203339-32fb2d80-aaa1-11ea-843e-f7f69da66e53.png" height="50"/>
</p>

*A collaborative computational cooking robot using computer vision built with Raspberry Pi*

Python logic and recipes for automatic cooking 

[See it in action on YouTube](https://youtu.be/poE4O6JZY0E) | 
[Read more about the project on DesignSpark](https://www.rs-online.com/designspark/student-innovation-onionbot-building-a-robot-sous-chef)


### About 

![Sauce](https://user-images.githubusercontent.com/32883278/97640295-5adf3380-1a38-11eb-9287-349cc64aed16.JPG)

The OnionBot sous chef can:

- Automatically proceed through a complete pasta with tomato sauce recipe
- Advance through instructions hands-free, using image classification
- Autonomously control pan temperature using PID feedback control
- Detect when the pasta is boiling-over and turn down the heat!
- Remind you if you haven’t stirred in a while, preventing your food from burning!

This simple recipe functionality only scratches the surface of what could be possible in the future with machine vision!

### Recipe example 

![flow](https://user-images.githubusercontent.com/32883278/97643676-4c951580-1a40-11eb-8298-1f67f483daaf.png)

An example of how the sous chef can use image classification to provide assitive functionality with a pasta boiling recipe. 


### System structure

![Screenshot 2020-06-09 at 21 40 54](https://user-images.githubusercontent.com/32883278/84198237-270c6d00-aa9b-11ea-9481-0a2cd971f2a7.png)

`API.py` API for showing recipe steps (messages) on screen and controlling recipe progress

`main.py` Read recipes from files and walk through steps, sending commands to the main `OnionBot-API`

`recipes/*` Store process, model and screen message information on a recipe-by-recipe basis

### Known issues 

- This code is a proof of concept only for using `OnionBot-API` for recipe automation - it is hacky and buggy 
- Special functionality is hard coded into the main file, would be much neater to plug addons in via config files
- Only 2 recipes tested so far


### TODO 

- Test more recipes!
- Refactor to make code actually safe for human viewing


### Interested in building a cooking automation robot?

Get in touch! 
