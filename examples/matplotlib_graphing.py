# matplotlib_graphing.py
# Joshua Clark, 2015
# This is a simple script for displaying data retrieved through the MesoPy package using basic matplotlib plots
# You may use this script as boilerplate for any of your own projects

from MesoPy import Meso
from matplotlib import pyplot as plt

m = Meso(api_token='3428e1e281164762870915d2ae6781b4')
# Retrieving the data for y-axis and plot
climatology = m.timeseries_obs(stid='kfnl', start='201505010600', end='201505020600', vars='air_temp',
                                  units='temp|F')
kfnl_obs = climatology['STATION'][0]['OBSERVATIONS']

climatology1 = m.timeseries_obs(stid='kgxy', start='201505010600', end='201505020600', vars='air_temp',
                                   units='temp|F')
kgxy_obs = climatology1['STATION'][0]['OBSERVATIONS']

climatology2 = m.timeseries_obs(stid='kden', start='201505010600', end='201505020600', vars='air_temp',
                                   units='temp|F')
kden_obs = climatology2['STATION'][0]['OBSERVATIONS']

# Creating a sequential list that matches the number of obs for the x-axis
# This is not really ideal though, as one would prefer time as the x-axis. I may get to it eventually, but I would
# appreciate a contribution here that allows the user to display time as the x-axis.

xAxis = []
i = 0
for obs in enumerate(kfnl_obs['air_temp_set_1']):
    i += 1
    xAxis.append(i)

xAxis1 = []
j = 0
for obs in enumerate(kgxy_obs['air_temp_set_1']):
    j += 1
    xAxis1.append(j)

xAxis2 = []
k = 0
for obs in enumerate(kden_obs['air_temp_set_1']):
    k += 1
    xAxis2.append(k)

# This is all matplotlib customization
fig = plt.figure()
fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=False, sharey=False)
fig.text(0.06, 0.5, 'Temperature in Fahrenheit', ha='center', va='center', rotation='vertical')
fig.text(0.5, 0.04, 'Observation Occurrence', ha='center', va='center')

ax1.plot(xAxis, kfnl_obs['air_temp_set_1'], marker='x', linestyle='-', color='b')
ax1.set_title('Air Temp Obs at Fort Collins for 1 May 15 6z to 2 May 15 6z')
ax2.plot(xAxis1, kgxy_obs['air_temp_set_1'], marker='o', linestyle='-', color='r')
ax2.set_title('Air Temp Obs at Greeley for 1 May 15 6z to 2 May 15 6z')
ax3.plot(xAxis2, kden_obs['air_temp_set_1'], marker='+', linestyle='-', color='c')
ax3.set_title('Air Temp Obs at Denver for 1 May 15 6z to 2 May 15 6z')

fig.subplots_adjust(hspace=0.6)
plt.show()


# You may find some of this code useful in creating your own data

# import pprint
# pp = pprint.PrettyPrinter(indent = 2)
# pp.pprint(climatology)

# Slice only the mm:dd from the date_time strings
# newList =[]
# for i in kfnl_obs['date_time']:
#     newList.append(i[11:-4])
# list1 = [s.replace(':', '') for s in newList]
# print(newList)

# Create a new list with obs in it
# list1 = [(i) for i in  kfnl_obs['air_temp_set_1']]
