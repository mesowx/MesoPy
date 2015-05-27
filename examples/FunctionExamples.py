# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 20:31:51 2015

@author: joshclark
"""

from MesoPy import MesoPy as Meso
import pprint 

# I import Pretty Print to make the returned dictionary look, well, pretty.
pp = pprint.PrettyPrinter(indent=2)

# Here we retrieve only the stations in Larimer County, Colorado
stations = Meso.station_list(state='CO', county='Larimer')
pp.pprint(stations)

# Calling variable_list() returns all possible sensor variables at stations
variables = Meso.variable_list()
pp.pprint(variables)

# This returns a climatology for Denver from Apr 26 OOz to Apr 27 OOz
climate = Meso.climatology_obs(stid='kden', startclim='04260000', endclim='04270000', units='precip|in')
pp.pprint(climate)

# Fetches the latest obs for Fort Collins airport within 30 min of Apr 26 18z
latest = Meso.latest_obs(stid='kfnl', attime='201504261800', within='30')
pp.pprint(latest)

# Returns a time series from Fort Collins airport from Apr 26 18z to Apr 26 23z
time = Meso.timeseries_obs(stid='kfnl', start='201504261800', end='201504262300')
pp.pprint(time)

# Small example from README
precip = Meso.precipitation_obs(stid='kfnl', start='201504261800', end='201504271200', units='precip|in')
station = precip['STATION'][0]['STID']
totalPrecip = precip['STATION'][0]['OBSERVATIONS']['total_precip_value_1']
print('The total accumulated precipitation at ' + station + ' was ' + str(totalPrecip) + '"')
