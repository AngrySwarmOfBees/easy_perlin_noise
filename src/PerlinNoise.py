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
xpix = 10  #setup
ypix = 10  #setup
#TEMPORARY interface to communicate arguments with script
print("Note, higher pixel counts will result in exponentially higher processing times, 100x100 is reccomended")     #Temporary
print("For 3 dimensional perlin noise choose a depth of greater than 1, NOTE: higher layer count will increase processing times as the number of calculations needed will increase greatly")
print("For 2 dimensional perlin noise, choose a depth of 1")
def GetDesiredResolution(): #Temporary
    global xpix
    global ypix
    global zpix
    try:    #Temporary
        xpix = int(input("Enter desired width in pixels "))      #Temporary
        ypix = int(input("Enter desired height in pixels "))      #Temporary
        zpix = int(input("Enter desired depth in pixels "))      # Temporary
        if zpix == 0:
            logging.error("Error a depth of: 0 cannot be produced, as that would require 0 calculations")
            GetDesiredResolution()
    except ValueError:  #Temporary
        logging.error("Error: provided input is not an integer")    #Temporary
        print("Error: provided value is not an integer, an image resolution must be an integer")    #Temporary
        GetDesiredResolution()  #Temporary
    else:   #Temporary
        logging.info("Requested resolution value was of type: int, no errors")  #Temporary
        logging.info("Requested resolution is: ", xpix, "x", ypix, "total pixels is: ", xpix * ypix)
        logging.info("Requested depth is:", zpix, "layers")    #Temporary
        print("Requested image resolution results in total pixel count is: ", xpix * ypix)  #Temporary
'''
def InitializeValues():
    print("Note: Choosing octaves for perlin noise generation will be available at a later date")       #Temporary 
    #Initializing Logging and variables
    GetDesiredResolution()
    LogFileName = 'PerlinNoiseLog.log'
    NoisePictureName = 'Noise.png'
    CsvFileName = "PerlinNoiseValues.csv"
    noise1_Octaves = 3
    noise2_Octaves = 6
    noise3_Octaves = 12
    noise4_Octaves = 24
    logging.basicConfig(filename=LogFileName, level=logging.DEBUG)
    logging.info("Script will log to", LogFileName)
    logging.info("Upon completion of script, Perlin noise will be saved as", NoisePictureName)
    noise1 = PerlinNoise(octaves=noise1_Octaves)
    noise2 = PerlinNoise(octaves=noise2_Octaves)
    noise3 = PerlinNoise(octaves=noise3_Octaves)
    noise4 = PerlinNoise(octaves=noise4_Octaves)
    logging.info("Initialized perlin noise octave levels")
    logging.info("Perlin Noise octaves are set to:", noise1_Octaves, noise2_Octaves, noise3_Octaves, "and", noise4_Octaves)
    print("Perlin Noise octaves are set to:", noise1_Octaves, noise2_Octaves, noise3_Octaves, "and", noise4_Octaves)
    try:
        CsvFile = open(CsvFileName, "w", newline='')
        Writer = csv.writer(CsvFile)
    except:
        logging.error('Error: there was a problem creating the file to export the perlin noise values to, exiting program')
        exit()
    else:
        logging.info('File initalized succesfully, data will be exported to: ' + CsvFileName)
        print('File initalized succesfully, data will be exported to: ' + CsvFileName)
'''
def NewInitializeValues(octaveVal, fname, logname):
    LogFileName = logname
    CsvFileName = fname
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
    def EasyNoiseGen():
        
        global pic
        noise_val = PerlinNoise()
        pic = [[[noise_val([i/xpix, j/ypix, k/zpix]) for j in range(xpix)] for i in range(ypix)] for k in range(zpix)]
        #plt.imshow(pic, cmap='gray') #!!!THIS WILL PRODUCE NO ERRORS, REMOVED TO CREATE ACTIVE DISPLAY OF NOISE GENERATION
        #plt.savefig(NoisePictureName, format='png')
        
RunNoiseCalculation()
logging.info("Now Exporting Data to: " + CsvFileName)
# !!!Saving data to file!!!

for row in pic:
    for i in row:
        Writer.writerow(i)
        #print(row)
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


