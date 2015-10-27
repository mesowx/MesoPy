"""
@author: joshclark

This script just demonstrates some example usage for the workshop

"""
from MesoPy import Meso
import pprint

# I import Pretty Print to make the returned dictionary look, well, pretty.
pp = pprint.PrettyPrinter(indent=2)

# Instance a Meso object by passing in YOUR api_token
m = Meso(api_token='3428e1e281164762870915d2ae6781b4')
# Fetches the latest obs for Boulder airport within 30 min of now
latest = m.latest_obs(stid='kbdu', within='30', units='ENGLISH')
pp.pprint(latest)

# Let's format a pretty sentence that tells us the Boulder wx
x = latest['STATION'][0]
st_name = x['NAME']
temp = str(x['OBSERVATIONS']['air_temp_value_1']['value']) + u'\N{DEGREE SIGN}' + 'F'
wind = x['OBSERVATIONS']['wind_speed_value_1']['value'] + ' mph'

result = 'The current weather at ' + st_name + ' is ' + temp + ' with a sustained wind of ' + wind
print(result)

# I import Pretty Print to make the returned dictionary look, well, pretty.
pp = pprint.PrettyPrinter(indent=2)

# Instance a Meso object by passing in YOUR api_token
m = Meso(api_token='3428e1e281164762870915d2ae6781b4') # this token for testing only

# Here we retrieve only the stations in Larimer County, Colorado
stations = m.station_list(state='CO', county='Larimer')

# Calling variable_list() returns all possible sensor variables at stations
variables = m.variable_list()

# This returns a climatology for Denver from Apr 26 OOz to Apr 27 OOz
climate = m.climatology_obs(stid='kden', startclim='04260000', endclim='04270000', units='precip|in')

# Fetches the latest obs for Fort Collins airport within 30 min of Apr 26 18z
latest = m.latest_obs(stid='kfnl', attime='201504261800', within='30')

# Returns a time series from Fort Collins airport from Apr 26 18z to Apr 26 23z
time = m.timeseries_obs(stid='kfnl', start='201504261800', end='201504262300')

# Returns the precip obs from Fort Collins airport from Apr 26 18z to Apr 27 12z
precip = m.precipitation_obs(stid='kfnl', start='201504261800', end='201504271200', units='precip|in')

#pp.pprint(stations)