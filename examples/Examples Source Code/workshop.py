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