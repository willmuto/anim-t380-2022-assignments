import sys
import random
import maya.cmds as cmds

def createRandomCubes(numOfCubes, randomSize=True):
   """Create random cubes in the scene.
 
   Args:
       numOfCubes (int): Specify the number of cubes to make.
       randomSize (int): Also make them random sizes between
           zero and one. Cubes are all (1,1,1) otherwise.
 
   Returns:
       bool: True if successful, False if not.
   """
 
   i = 0
   while (i < numOfCubes - 1):
       if randomSize:
           cube_size = [
               random.random(),
               random.random(),
               random.random()
           ]
 
       else:
           cube_size = (1, 1, 1)
 
       cubePosition = [
           random.random() * 100,
           random.random() * 100,
           random.random() * 100,
       ]
 
   cube = cmds.polyCube()
 
   # TODO: check to make sure cubes don't overlap?
   cmds.move(
       cubePosition[0],
       cubePosition[1],
       cubePosition[2],
       cube
   )
 
   cmds.scale(
       cube_size[0],
       cube_size[1],
       cube_size[2],
       cube
   )
 
   return True
