# Midterm

Students, working individually, will develop a tool (command line or graphical) to solve one of the problems below (or a similar pitch approved by the instructor). They will create test/placeholder data as needed. This project will be a tool written from scratch for proficiency in designing and executing a workflow, informed by the previous lectures. Projects should contain a complete README, and students should be prepared to present their project to the class. Graduate/PhD students should treat the extra credit feature as required.

## Problem 1

### Overview
The art supervisor is looking for a faster way to provide notes back to the team. Using drawover images (for example, out of photoshop), develop a tool which allows the user to:
* send paths to the images 
* as well as text notes about each image
* to a predefined group of artists’ emails in a config file
* Extra credit feature: Generate a CSV that can be imported as a spreadsheet which includes the image path, artist name, and notes from the supervisor

### Hints
It is ok to assume the images will all be in a single folder. Notes can also be in the folder either in a single text file or in a text file with the same name as the image. JSON or YAML are worth looking at for config file formats.

## Problem 2

### Overview
For prepping deliveries back to client, develop a tool which: 
* collects a sequence of frames and 
* renames them in a configurable way 
* with the option to zip into an archive 
* Extra credit feature: automatically generate a thumbnail and CSV including the filename and date to be included in the zip archive

### Hints
The sequence of frames should have a well-defined "internal" naming convention (similar to one discussed in the lecture). JSON or YAML are worth looking at as a config file to store the "client" naming convention, and using `format` strings for the client naming convention will make your life a lot easier here. To create the zip archive, you can use either the python module or subprocess to a another tool

## Problem 3

### Overview
The compositing supervisor is requesting a tool to help identify broken frames. Create a utility that: 
* collects a sequence of frames based on a naming convention
* identifies frames either vastly different in filesize or are completely black
* generates a report that lists potential frames to be reviewed (text, html, or email)
* Extra credit feature: combine thumbnails in a single grid image for quick reference

### Hints
Use a well-definied naming convention similar to one discussed in the lecture. To identify a frame that is completely black, a python approach that is worth looking at is `OpenImageIO`. You could do it with `ffmpeg`, but it would be trickier.

## Problem 4

### Overview
Layout has a list of camera specs from the shoot. Create a tool in maya that: 
* generates a camera 
* selected from a CSV list
* setting focal length and filmback size correctly 
* Extra credit feature: add a framing chart image plane and a test render

### Hints
This will probably be most useful as a simple GUI, so I would recommend making a `PySide` tool here, and the camera list populates some widgets. If you wanted to approach this in Maya standalone, think about how an artist would use the tool, and provide feedback to make it easier to see what cameras are available to choose from. The filmback size in Maya is under the `Camera Aperture` attributes (either in inches or millimeters) and refers to the physical size of the camera sensor.