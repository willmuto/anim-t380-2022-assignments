# Final

Students, working in pairs, will develop a tool (command line or graphical) to solve one of the problems below (or a similar pitch approved by the instructor). They will create test/placeholder data as needed. This project will be a tool written from scratch for proficiency in designing and executing a workflow, informed by the previous lectures. Projects should contain a complete README, and students should be prepared to present their project to the class. Graduate/PhD students should treat the extra credit feature as required.

## Problem 1

### Overview
The rigging team is tasked with generating prop rigs for a large number of assets. The number of props requires the task to be done procedurally. Within Maya:
* create a graphical interface which
* references a model when a button is pressed
* automatically builds a simple rig (at least a joint hierarchy) based on locator placement
* Extra credit feature: add a button to the UI to select a version of the model based on a naming convention

### Hints
To determine the order of the joint hierarchy, the locators will probably need specific names. To make this system more flexible, it may even be worth putting this hierarchy into a JSON config file.

## Problem 2

### Overview
Editorial needs a better way to update ShotGrid. Given a folder of media, generate a tool that: 
* updates cut information (first & last frame) in ShotGrid
* combines the media into a single file for review
* generates an email report with all the new cut information and path for the media for the prod team
* Extra credit feature: Auto-generate a nuke script that creates a thumbnail grid for production to reference

### Hints
ffmpeg is a pretty common approach for combining media via scripts. It'll probably be the most flexible way to read the first and last frame from the media as well.

## Problem 3

### Overview
The compositors are having trouble tracking the various versions of elements coming into the department. Write a tool which 
* allows the artists to select which elements and versions they want to bring into their comp based on file naming
* generates read nodes, as well as 
* creating a write node based on a configuration file. 
* Extra credit feature: Generate a text report of the versions being used in the comp (and the latest version on disk)

### Hints
The configuration file is probably best as JSON (or YAML if you prefer). Use the config file to store at least one setting (such as output file format).


## Problem 4

### Overview
Various media needs to be created for review on set once the animators finish a playbast. Create a tool that: 
* generates h264 compressed media in the background once the render is complete with the source file path added as metadata 
* updates a status in ShotGrid and 
* zips the file
* Extra credit feature: Add a burnin to the new media with the source file name

### Hints
It is fine to have this be a shelf button and not tie it in to a playblast post process. ffmpeg is going to be your friend here for the compressed media. For the burnin, it is possible to do in ffmpeg as well but Nuke may be an easier path forward.