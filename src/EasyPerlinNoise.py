from turtle import delay
import matplotlib.pyplot as plt
import sys
sys.path.append('/home/benmowery/perlin_noise-1.11')
from perlin_noise import PerlinNoise
import logging
import csv
#Package importing
"""
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
"""




class Noise:
    global ShouldExport
    def __init__(self, xpix, ypix, zpix=1, octaves=3, fname=None): #initializes package arguments
        self.xpix = xpix    #number of values in x direction
        self.ypix = ypix    #number of values in y direction
        self.zpix = zpix    #number of values in z direction (optional)
        self.octaves = octaves  #base value for octaves (see InitalizeNoiseValues for how this is used), (if not supplied, base value will be 3)
        self.fname = fname
        LogFileName = 'PerlinNoiseLog.log' #initializes log file
        #CsvFileName = fname
        if (self.fname is None):    #Decides if noise should be exported based on if a file name is given
            ShouldExport = False
        else:
            ShouldExport = True
            self.fname = fname  #name of file that noise will be exported to (optional), if no value is supplied, the values will not be saved to a file)

    def InitializeNoiseValues(octaveVal):
        noise1_Octaves = octaveVal
        noise2_Octaves = octaveVal * 2
        noise3_Octaves = noise2_Octaves * 2
        noise4_Octaves = noise3_Octaves * 2
        noise1 = PerlinNoise(octaves=noise1_Octaves)
        noise2 = PerlinNoise(octaves=noise2_Octaves)
        noise3 = PerlinNoise(octaves=noise3_Octaves)
        noise4 = PerlinNoise(octaves=noise4_Octaves)

    def EasyNoiseGen(self):
        pic = list
        noise_val = PerlinNoise()
        pic = [[[noise_val([i/self.xpix, j/self.ypix, k/self.zpix]) for j in range(self.xpix)] for i in range(self.ypix)] for k in range(self.zpix)]
        


