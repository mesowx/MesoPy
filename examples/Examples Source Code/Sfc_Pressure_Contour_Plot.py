# -*- coding: utf-8 -*-
"""
Created on Fri May 29 09:54:26 2015

@author: joshclark

This script demonstrates using cartopy to view data obtained from MesoPy on a map
It uses some boilerplate from the cartopy example project for mapquest tiles

"""
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from MesoPy import Meso
import pprint


def main():

    pp = pprint.PrettyPrinter(indent=4)

    # Create instance of Meso object, pass in YOUR token
    m = Meso(api_token='3428e1e281164762870915d2ae6781b4')
    # Get all latest sea level pressure obs (in millibars) within 90 minutes of now in the lat/long box specified.
    latest = m.timeseries_obs(bbox=[[-111, 35, -99, 43]], within='90', vars='air_temp', units='temp|F')

    lat_list = [float(ob['LATITUDE']) for ob in latest['STATION']]
    lon_list = [float(ob['LONGITUDE']) for ob in latest['STATION']]
    temp_list = [float(ob['OBSERVATIONS']['air_temp_value_1']['value']) for ob in latest['STATION']]
    pp.pprint(latest)

    # Create a new figure
    fig = plt.figure(figsize=(15, 12))
    # Add the map and set the extent
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.set_extent([-99, -111, 35, 43])

    # Contour pressure at each lat/long
    plt.tricontourf(lon_list, lat_list, temp_list, 100, transform=ccrs.PlateCarree())
    plt.plot(lon_list, lat_list, linestyle ='none', marker='o', color='black', markersize=5, alpha=0.3,
             transform=ccrs.PlateCarree())
    plt.colorbar(fraction=0.032)


    # Retrieve the state boundaries using cFeature and add to plot
    states_provinces = cfeature.NaturalEarthFeature(
        category='cultural',
        name='admin_1_states_provinces_lines',
        scale='50m',
        facecolor='none')
    ax.add_feature(states_provinces, edgecolor='gray')



    # Make a title with the time value
    #plt.title('Temperature forecast ' + '(' + u'\u00b0' + 'F)' + ' for ' + str(time_val) + 'z', fontsize=20)
    # Plot markers for each lat/long to show grid points for 0.25 deg GFS
    # for lon, lat in latlon_list:
    #     plt.plot(lon, lat, marker='o', color='black', markersize=2,
    #              alpha=0.3, transform=ccrs.Geodetic())

    plt.show()


if __name__ == '__main__':
    main()