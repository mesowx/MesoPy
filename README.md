# MesoPy

MesoPy is a small pure python wrapper around the MesoWest (http://mesowest.utah.edu/) API. It is useful for retrieving meteorological data at over 40,000 observation stations in the United States. This project was created with the researcher in mind and I would like feedback on how you are using MesoPy!

## Requirements
MesoPy requires [requests] ( `pip install requests`) because of it's voodoo powers in making API calls for us. Currently only Python 3 is supported but I hope to fix that by the end of summer 2015. 

## Installation
There are two easy ways to install MesoPy:

1. Run  `pip install mesopy` from a command line window
2. Download the source folder and place `MesoPy.py` into your working directory

## Usage
#### Retrieving data:
You can request different types of observations by simply making a function call and passing in a few parameters:

```
# Here we pass in stid, start, end, and units as string parameters (see docs for params)
precip = precipitation_obs(stid='kfnl', start='201504261800', end='201504271200',
units='precip|in')
```

This returns the following data in JSON format:

> { 'STATION': [ { 'ELEVATION': '5016',
>                         'ID': '192',
>                   'LATITUDE': '40.45',
>                  'LONGITUDE': '-105.01667',
>                    'MNET_ID': '1',
>                       'NAME': 'Fort Collins/Loveland, Fort Collins-Loveland '
>                               'Municipal Airport',
>               'OBSERVATIONS': { 'count_1': 6,
>                           'ob_end_time_1': '2015-04-27T00:55:00Z',
>                         'ob_start_time_1': '2015-04-26T18:55:00Z',
>                    'total_precip_value_1': 0.13,
>                              'vids case4': ['39', '51', '40', '52']},
>                      'STATE': 'CO',
>                     'STATUS': 'ACTIVE',
>                       'STID': 'KFNL',
>                   'TIMEZONE': 'US/Mountain'}],
>  'SUMMARY': { 'METADATA_RESPONSE_TIME': '898.586988449 ms',
>                    'NUMBER_OF_OBJECTS': 1,
>                        'RESPONSE_CODE': 1,
>                     'RESPONSE_MESSAGE': 'OK',
>                           'TOTAL_TIME': '2027.99797058 ms'}}

You can retrieve any of the dictionary keys/values listed above by merely doing the following:

```
# The JSON dictionary is stored in the precip variable. Let's print the total precip
# accumulation for Fort Collins Airport.
station = precip['STATION'][0]['STID']
totalPrecip =  precip['STATION'][0]['OBSERVATIONS']['total_precip_value_1'] 
print('The total accumulated precip at ' + station + ' was ' + str(totalPrecip) + ' in')
```
Which prints:

> The total accumulated precipitation at KFNL was 0.13 inches

#####You should note two things from the above example: 
1. Whenever the data you're requesting returns `['STATION']`, it is necessary to specify which station (index value) in the list you will subsequently be referring to. For example if you pass in `stid=kden,kslc`, the dictionary will return a list of the two stations' relevant info. So to get to information on KDEN, you would type `['STATION'][0]` because KDEN would be first in the list of stations. Remember that `{}` specifies a dictionary and `[]` denotes a list and `[0]` is the first position in a list. You could store `precip['STATION'][0]` as a variable to reduce clutter.  
2. You must cast `str()` on any `int` values (such as totalPrecip above) if you expect to concatenate a string like the example.

## Documentation
MesoPy contains six functions that request different types of data from the API. Information on function usage can be obtained by typing `help(whatever_function)` into the interactive interpreter. Alternatively, you can retrieve this information from code by printing `whateverfunction.__doc__`. I have created a text version [here] that describes the parameters associated with each function.

## Example Projects 
Possible projects include:

1. A GUI that displays current weather information at several stations using tkinter
2. Plotting timeseries/climatology data using matplotlib
3. Displaying precipitation data on a map using cartopy

I will try to add these example projects when I get a bit more time this summer. 
>>>>>>> origin/master

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
[here]: https://github.com/jclark754/MesoPy/blob/master/FunctionDoc.md
[research group]: http://meso1.chpc.utah.edu/mesowest_overview/
[Western Region]: http://www.wrh.noaa.gov/
