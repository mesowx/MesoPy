# MesoPy

MesoPy is a small pure python wrapper around the MesoWest (http://mesowest.utah.edu/) API. It is useful for retrieving meteorological data at over 40,000 observation stations in the United States. This project was created with the researcher in mind and I would like feedback on how you are using MesoPy!

## Requirements
MesoPy requires [requests] ( `pip install requests`) because of it's voodoo powers in making API calls for us. 

## Installation
There are two easy ways to install MesoPy:
1. Run  `pip install mesopy` from a command line window
2. Download the source folder and place `MesoPy.py` into your working directory

## Example Usage
MesoPy contains seven functions that request different types of data from the API. Information on function usage can be obtained by typing `help(whatever_function)` into the interactive interpreter. Alternatively, you can retrieve this information from code by printing `whateverfunction.__doc__`. Alternatively, I have created a .doc [here] that describes the paramters associated with each function.

## Version
1.0.0 released on 28 April 2015

## License
MIT

## Support
MesoPy was designed to be as simple as possible and I hope you enjoy its usage. If you have any questions/comments, please direct them to [jclark754@gmail.com].

## Credits
MesoWest has come a long way and I feel that Dr. John Horel's [research group] at the University of Utah deserves considerable praise for their work in creating a one-stop shop for meteorological data. Additional facilities were also provided by the [Western Region] of the National Weather Service. 

[requests]:https://pypi.python.org/pypi/requests/
[jclark754@gmail.com]: mailto:jclark754@gmail.com
[here]: http://google.com
[research group]: http://meso1.chpc.utah.edu/mesowest_overview/
[Western Region]: http://www.wrh.noaa.gov/
