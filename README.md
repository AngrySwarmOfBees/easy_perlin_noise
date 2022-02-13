# easy_perlin_noise
This is a package used to streamline the use of the perlin_noise package (https://github.com/salaxieb/perlin_noise), while adding more functionality, like exporting generated noise to files for later use.

This package streamlines the use of the package perlin_noise by allowing to create perlin noise with a single package function

required packages: 

  - perlin_noise (https://github.com/salaxieb/perlin_noise)
  - matplotlib (https://matplotlib.org/)
  - logging (python built in package)
  - sys (python built in package)

# Usage
To import the package, use `from EasyPerlinNoise import Noise`

To generate noise use: 
```
[Chosen Variable Name] = Noise([xpix], [ypix], [zpix], [octaves], [fname])
[Chosen Variable Name].EasyNoiseGen()
```
This will generate the requested Perlin Noise, to access the perlin noise, use the variable name you chose


Arguments:
  - xpix : width of array
  - ypix : height of array
  - zpix : depth of array (optional)
  - octaves : base octave, all octaves are double the previous octave, if the octave provided is 2, the 2nd octave level will be 4, and the 3rd octave will be 8...
  - fname : name of csv file that values should be exported to (optional) 


**further documentation at a later date**
