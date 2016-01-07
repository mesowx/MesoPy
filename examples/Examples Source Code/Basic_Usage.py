"""
@author: joshclark

This script just demonstrates some example usage for the workshop

"""
from MesoPy import Meso
import pprint

# I import Pretty Print to make the returned dictionary look, well, pretty.
pp = pprint.PrettyPrinter(indent=2)

# Instance a Meso object by passing in YOUR api_token
m = Meso(token='YOUR TOKEN')
# Fetches the latest obs for Boulder airport within 30 min of now
latest = m.latest(stid='kbdu', within='30', units='ENGLISH')
pp.pprint(latest)

# Let's format a pretty sentence that tells us the Boulder wx
x = latest['STATION'][0]
st_name = x['NAME']
temp = str(x['OBSERVATIONS']['air_temp_value_1']['value']) + u'\N{DEGREE SIGN}' + 'F'
wind = str(x['OBSERVATIONS']['wind_speed_value_1']['value']) + ' mph'

result = 'The current weather at ' + st_name + ' is ' + temp + ' with a sustained wind of ' + wind
print(result)

# I import Pretty Print to make the returned dictionary look, well, pretty.
pp = pprint.PrettyPrinter(indent=2)

# Instance a Meso object by passing in YOUR api_token
m = Meso(token='YOUR TOKEN') # this token for testing only

# Here we retrieve only the stations in Larimer County, Colorado
stations = m.metadata(state='CO', county='Larimer')

# Calling variables() returns all possible sensor variables at stations
variables = m.variables()

# This returns a climatology for Denver from Apr 26 OOz to Apr 27 OOz
climate = m.climatology(stid='kden', startclim='04260000', endclim='04270000', units='precip|in')

# Fetches the latest obs for Fort Collins airport within 30 min of Apr 26 18z
attime = m.attime(stid='kfnl', attime='201504261800', within='30')

# Or just get the latest observation within the last 15 minutes
latest = m.latest(stid='kfnl', within='15')

# Returns a time series from Fort Collins airport from Apr 26 18z to Apr 26 23z
time = m.timeseries(stid='kfnl', start='201504261800', end='201504262300')

# Returns the precip obs from Fort Collins airport from Apr 26 18z to Apr 27 12z
precip = m.precip(stid='kfnl', start='201504261800', end='201504271200', units='precip|in')

# Learn more about all of the networks in MesoWest with the networks() func
networks = m.networks()

# Or explore the categories MesoWest networks belong to
nettypes = m.networktypes()

# You can obtain time series statistics for any station
stats = m.time_stats(stid='mtmet', start='201403240000', end='201403280000', type='all')

# Or get climatology stats for a station (remember to change the date!)
clim_stats = m.climate_stats(stid='mtmet', startclim='03240000', endclim='03280000', type='all')

# Lastly, see the latency of the API by using the latency() function
latency = m.latency(stid='mtmet', start='201403240000', end='201403280000')