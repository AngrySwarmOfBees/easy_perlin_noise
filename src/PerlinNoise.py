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
def NewInitializeValues(octaveVal):
    noise1_Octaves = octaveVal
    noise2_Octaves = octaveVal * 2
    noise3_Octaves = noise2_Octaves * 2
    noise4_Octaves = noise3_Octaves * 2
    noise1 = PerlinNoise(octaves=noise1_Octaves)
    noise2 = PerlinNoise(octaves=noise2_Octaves)
    noise3 = PerlinNoise(octaves=noise3_Octaves)
    noise4 = PerlinNoise(octaves=noise4_Octaves)


global pic
#integrate argumetns used on running script, (resolution(x,y,z)...)
class EasyPerlinNoise:
    def __init__(self, xpix, ypix, octaves=3, zpix=1, fname="PerlinNoiseValues.csv", lname=pic):
        self.xpix() = xpix
        self.ypix() = ypix
        self.zpix() = zpix
        self.octaves() = octaves
        self.fname() = fname
        self.lname() = lname
        LogFileName = 'PerlinNoiseLog.log'
        CsvFileName = fname
    def EasyNoiseGen():
        global pic
        noise_val = PerlinNoise()
        pic = [[[noise_val([i/xpix, j/ypix, k/zpix]) for j in range(xpix)] for i in range(ypix)] for k in range(zpix)]
        #plt.imshow(pic, cmap='gray') #!!!THIS WILL PRODUCE NO ERRORS, REMOVED TO CREATE ACTIVE DISPLAY OF NOISE GENERATION
        #plt.savefig(NoisePictureName, format='png')
        for row in pic:
            for i in row:
                Writer.writerow(i)
        
logging.info("Now Exporting Data to: " + CsvFileName)
# !!!Saving data to file!!!

'''
try:
    for i, row in pic:
        #Writer.writerow([row[i] for row in pic])
        print(row)
except:
    logging.error("Could not export data to file")
    CsvFile.close()
else:
    logging.info("succesfully exported data to file: " + CsvFileName)
    print("succesfully exported data to file: " + CsvFileName)
    CsvFile.close()
'''

#xpix, ypix = 10, 10
'''
pic = []
for i in range(xpix):
    row = []
    for j in range(ypix):
        noise_val = noise1([i/xpix, j/ypix])
        noise_val += 0.5 * noise2([i/xpix, j/ypix])
        noise_val += 0.25 * noise3([i/xpix, j/ypix])
        noise_val += 0.125 * noise4([i/xpix, j/ypix])

        row.append(noise_val)
        print("Appended", noise_val, "to row")
    #print("Appended Values of row to var pic")

    #Add random cloud reduction function for reducing clouds in consecutive layers to generate clouds for weather simulation
    #!!!Experimental!!! ALL code errors will be found in the following code, all preceeding code is error free !!!EXPERIMENTAL!!!#
#Begin code for 3d perlin noise generation, which uses the previous layers as a base for the new layers

plt.imshow(pic, cmap='gray') #!!!THIS WILL PRODUCE NO ERRORS, REMOVED TO CREATE ACTIVE DISPLAY OF NOISE GENERATION
plt.savefig(NoisePictureName, format='png')
'''  


