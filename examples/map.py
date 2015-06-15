# -*- coding: utf-8 -*-
"""
Created on Fri May 29 09:54:26 2015

@author: joshclark

This script demonstrates using cartopy to view data obtained from MesoPy on a map
It uses some boilerplate from the cartopy example project for mapquest tiles

"""
import matplotlib.pyplot as plt
from matplotlib.transforms import offset_copy
import cartopy.crs as ccrs
import cartopy.io.img_tiles as cimgt
from MesoPy import Meso
# import pprint


def main():

    # This is just useful for formatting returned json
    # pp = pprint.PrettyPrinter(indent=2)

    # Create instance of Meso object, pass in YOUR token
    m = Meso(api_token='3428e1e281164762870915d2ae6781b4')

    # Use to lookup stations, could specify counties or whatever here
    # findstationids = m.station_list(state='CO')
    # print(findstationids)

    # Grab most recent temp (F) ob in last 90 min at each of the below stations
    stations = ['kgxy, kccu, kcos, kden, kgjt, kbdu, kpub, klhx, kspd, kdro, ksbs, keeo, kguc, klic, '
                'kstk, kals, ktad']
    latest = m.latest_obs(stid=stations, within='90', vars='air_temp', units='temp|F')
    print(latest)

    # create a list to store everything, iterate over the number of objs returned in latest and append
    # lat, long, temp, and stid for use later
    data = []
    for ob in latest['STATION']:
        data.append((float(ob['LATITUDE']), float(ob['LONGITUDE']),
                     float(ob['OBSERVATIONS']['air_temp_value_1']['value']), ob['STID']))

    # Create a MapQuest open aerial instance.
    map_quest_aerial = cimgt.MapQuestOpenAerial()
    # Create a GeoAxes in the tile's projection.
    ax = plt.axes(projection=map_quest_aerial.crs)
    # Limit the extent of the map to Colorado's borders
    ax.set_extent([-102.03, -109.03, 37, 41])
    # Add the MapQuest data at zoom level 8.
    ax.add_image(map_quest_aerial, 8)

    # Plot lat/long pts with below params
    for lat, lon, temp, stid in data:
        plt.plot(lon, lat, marker='o', color='y', markersize=1,
                 alpha=0.7, transform=ccrs.Geodetic())

    # Transforms for the text func we're about to call
    geodetic_transform = ccrs.Geodetic()._as_mpl_transform(ax)
    text_transform = offset_copy(geodetic_transform, units='dots', x=0, y=0)

    # Plot temp and station id for each of the markers
    for lat, lon, temp, stid in data:
        plt.text(lon, lat, stid + '\n' + str(round(temp, 1)) + u' \N{DEGREE SIGN}' + 'F',
                 verticalalignment='center', horizontalalignment='center',
                 transform=text_transform, fontsize=9,
                 bbox=dict(facecolor='wheat', alpha=0.5, boxstyle='round'))
    plt.title('Current Weather Around Colorado')
    plt.show()

if __name__ == '__main__':
    main()