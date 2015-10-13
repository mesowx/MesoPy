# ==================================================================================================================== #
# MesoPy                                                                                                               #
# Version: 1.1.2                                                                                                       #
# Copyright (c) 2015 Joshua Clark <joclark@ucar.edu>                                                                   #
#                                                                                                                      #
# LICENSE:                                                                                                             #
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated         #
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation the  #
# rights to use,copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to       #
# permit persons to whom the Software is furnished to do so, subject to the following conditions:                      #
#                                                                                                                      #
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the #
# Software.                                                                                                            #
#                                                                                                                      #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE #
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS   #
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,WHETHER IN AN ACTION OF CONTRACT, TORT OR   #
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.     #
#                                                                                                                      #
# ==================================================================================================================== #

try:
    # noinspection PyUnresolvedReferences
    from requests import get, exceptions

except ImportError:
    raise Exception("MesoPy requires the 'requests' library to work")

# ==================================================================================================================== #
# MesoPyError class                                                                                                    #
# Type: Exception                                                                                                      #
# Description: This class is simply the means for error handling when an exception is raised.                          #
# ==================================================================================================================== #


class MesoPyError(Exception):
    def __init__(self, error_message):
        self.error_message = error_message

    def __str__(self):
        r""" This just returns one of the error messages listed in the checkresponse() method"""
        return repr(self.error_message)


# ==================================================================================================================== #
# Meso class                                                                                                           #
# Type: Main                                                                                                           #
# Description: This class defines an instance of MesoPy and takes in the user's token                                  #
# ==================================================================================================================== #


class Meso(object):
    def __init__(self, api_token):
        r""" Instantiates an instance of MesoPy.

        Arguments:
        ----------
        api_token: string, mandatory
            Your API token that authenticates you for requests against MesoWest.

        Returns:
            None.

        Raises:
            None.
        """

        self.base_url = 'http://api.mesowest.net/v2/'
        self.api_token = api_token
        self.geo_criteria = ['stid', 'state', 'country', 'county', 'radius', 'bbox', 'cwa', 'nwsfirezone', 'gacc',
                             'subgacc']

    # ================================================================================================================ #
    # Functions:                                                                                                       #
    # ================================================================================================================ #

    @staticmethod
    def _checkresponse(response):
        r""" Returns the data requested by the other methods assuming the response from the API is ok. If not, provides
        error handling for all possible API errors. HTTP errors are handled in the get_response() method.

        Arguments:
        ----------
            None.

        Returns:
            The response from the API as a dictionary if the API code is 2.

        Raises:
            MesoPyError: Gives different response messages depending on returned code from API. If the response is 2,
            resultsError is displayed. For a response of 200, an authError message is shown. A ruleError is displayed
            if the code is 400, a formatError for -1, and catchError for any other invalid response.
        """

        results_error = 'No results were found matching your query'
        auth_error = 'The token or API key is not valid, please contact Josh Clark at jclark754@gmail.com to resolve ' \
                     'this'
        rule_error = 'This request violates a rule of the API. Please check the guidelines for formatting a data ' \
                     'request and try again'
        catch_error = 'Something went wrong. Check all your calls and try again'

        if response['SUMMARY']['RESPONSE_CODE'] == 1:
            return response
        elif response['SUMMARY']['RESPONSE_CODE'] == 2:
            raise MesoPyError(results_error)
        elif response['SUMMARY']['RESPONSE_CODE'] == 200:
            raise MesoPyError(auth_error)
        elif response['SUMMARY']['RESPONSE_CODE'] == 400:
            raise MesoPyError(rule_error)
        elif response['SUMMARY']['RESPONSE_CODE'] == -1:
            format_error = response['SUMMARY']['RESPONSE_MESSAGE']
            raise MesoPyError(format_error)
        else:
            raise MesoPyError(catch_error)

    def _get_response(self, endpoint, request_dict):
        """ Returns a dictionary of data requested by each function.

        Arguments:
        ----------
        endpoint: string, mandatory
            Set in all other methods, this is the API endpoint specific to each method.
        request_dict: string, mandatory
            A dictionary of parameters that are formatted into the API call.

        Returns:
            response: A dictionary that has been dumped from JSON.

        Raises:
            MesoPyError: Overrides the exceptions given in the requests library to give more custom error messages.
            Connection_error occurs if no internet connection exists. Timeout_error occurs if the request takes too
            long and redirect_error is shown if the url is formatted incorrectly.
        """
        connection_error = 'Could not connect to the API. Please check your connection'
        timeout_error = 'Connection Timeout, please retry later'
        redirect_error = 'Bad URL, check the formatting of your request and try again'

        try:
            resp = get(self.base_url + endpoint, params=request_dict)
            return self._checkresponse(resp.json())
        except exceptions.ConnectionError:
            raise MesoPyError(connection_error)
        except exceptions.Timeout:
            raise MesoPyError(timeout_error)
        except exceptions.TooManyRedirects:
            raise MesoPyError(redirect_error)
        except exceptions.RequestException as e:
            raise e

    def _check_geo_param(self, arg_list):
        r""" Checks each function call to make sure that the user has provided at least one of the following geographic
        parameters: 'stid', 'state', 'country', 'county', 'radius', 'bbox', 'cwa', 'nwsfirezone', 'gacc', or 'subgacc'.

        Arguments:
        ==========
        arg_list: list, mandatory
            A list of kwargs from other functions.

        Returns:
            None.

        Raises:
            MesoPyError if no geographic search criteria is provided.
        """

        geo_func = lambda a, b: any(i in b for i in a)
        check = geo_func(self.geo_criteria, arg_list)
        if check is False:
            raise MesoPyError('No stations or geographic search criteria specified. Please provide one of the '
                              'following: stid, state, county, country, radius, bbox, cwa, nwsfirezone, gacc, subgacc')

    def latest_obs(self, **kwargs):
        r""" Returns a dictionary of latest observations at a user specified location for a specified time. Users must
        specify at least one geographic search parameter ('stid', 'state', 'country', 'county', 'radius', 'bbox', 'cwa',
        'nwsfirezone', 'gacc', or 'subgacc') to obtain observation data. Other parameters may also be included. See
        below for optional parameters. Also see the station_list() method for station IDs.

        Arguments:
        ----------
        attime: string, optional
            Date and time in form of YYYYMMDDhhmm for which returned obs are closest. All times are UTC. e.g.
            attime='201504261800'
        within: string, optional
            When used without 'attime', it can be left blank to return the latest ob or represent the number of minutes
            which would return the latest ob within that time period. When used with 'attime' it can be a single number
            representing a time period before attime or two comma separated numbers representing a period before and
            after the attime e.g. attime='201306011800', within='30' would return the ob closest to attime within a 30
            min period before or after attime.
        obtimezone: string, optional
            Set to either UTC or local. Sets timezone of obs. Default is UTC. e.g. obtimezone='local'.
        showemptystations: string, optional
            Set to '1' to show stations even if no obs exist that match the time period. Stations without obs are
            omitted by default.
        stid: string, optional
            Single or comma separated list of MesoWest station IDs. e.g. stid='kden,kslc,wbb'
        county: string, optional
            County/parish/borough (US/Canada only), full name e.g. county='Larimer'
        state: string, optional
            US state, 2-letter ID e.g. state='CO'.
        country: string, optional
            Single or comma separated list of abbreviated 2 or 3 character countries e.g. country='us,ca,mx'
        radius: list, optional
            Distance from a lat/lon pt as [lat,lon,radius (mi)]e.g. radius=[-120,40,20]
        bbox: list, optional
            Stations within a [lon/lat] box in the order [lonmin,latmin,lonmax,latmax] e.g. bbox=[-120,40,-119,41]
        cwa: string, optional
            NWS county warning area e.g. cwa='LOX' See http://www.nws.noaa.gov/organization.php for CWA list
        nwsfirezone: string, optional
            NWS Fire Zone e.g. nwsfirezone='LOX241'
        gacc: string, optional
            Name of Geographic Area Coordination Center e.g. gacc='EBCC' See http://gacc.nifc.gov/ for a list of GACCs.
        subgacc: string, optional
            Name of Sub GACC e.g. subgacc='EB07'
        vars: string, optional
            Single or comma separatd list of sensor variables. Will return all stations that match one of provided
            variables. Useful for filtering all stations that sense only certain vars. Do not request vars twice in
            the query. e.g. vars='wind_speed,pressure' Use the variables method to see a list of sensor vars.
        status: string, optional
            A value of either active or inactive returns stations currently set as active or inactive in the archive.
            Omitting this param returns all stations. e.g. status='active'
        units: string, optional
            String or set of strings and pipes separated by commas. Default is metric units. Set units='ENGLISH' for
            FREEDOM UNITS ;) Valid  other combinations are as follows: temp|C, temp|F, temp|K; speed|mps, speed|mph,
            speed|kph, speed|kts; pres|pa, pres|mb; height|m, height|ft; precip|mm, precip|cm, precip|in; alti|pa,
            alti|inhg. e.g. units='temp|F,speed|kph,metric'
        groupby: string, optional
            Results can be grouped by key words: state, county, country, cwa, nwszone, mwsfirezone, gacc, subgacc
            e.g. groupby='state'

        Returns:
            Dictionary of the latest time observations through the get_response() method.

        Raises:
            None.
        """

        self._check_geo_param(kwargs)
        kwargs['token'] = self.api_token

        return self._get_response('stations/nearesttime', kwargs)

    def precipitation_obs(self, start, end, **kwargs):
        r""" Returns a dictionary of a time series of observations at a user specified location for a specified time.
        Users must specify at least one geographic search parameter ('stid', 'state', 'country', 'county', 'radius',
        'bbox', 'cwa', 'nwsfirezone', 'gacc', or 'subgacc') to obtain observation data. Other parameters may also be
        included. See below mandatory and optional parameters. Also see the station_list() method for station IDs.

        Arguments:
        ----------
        start: string, mandatory
            Start date in form of YYYYMMDDhhmm. MUST BE USED WITH THE END PARAMETER. Default time is UTC
            e.g., start='201306011800'
        end: string, mandatory
            End date in form of YYYYMMDDhhmm. MUST BE USED WITH THE START PARAMETER. Default time is UTC
            e.g., end='201306011800'
        obtimezone: string, optional
            Set to either UTC or local. Sets timezone of obs. Default is UTC. e.g. obtimezone='local'.
        showemptystations: string, optional
            Set to '1' to show stations even if no obs exist that match the time period. Stations without obs are
            omitted by default.
        stid: string, optional
            Single or comma separated list of MesoWest station IDs. e.g. stid='kden,kslc,wbb'
        county: string, optional
            County/parish/borough (US/Canada only), full name e.g. county='Larimer'
        state: string, optional
            US state, 2-letter ID e.g. state='CO'.
        country: string, optional
            Single or comma separated list of abbreviated 2 or 3 character countries e.g. country='us,ca,mx'
        radius: list, optional
            Distance from a lat/lon pt as [lat,lon,radius (mi)]e.g. radius=[-120,40,20]
        bbox: list, optional
            Stations within a [lon/lat] box in the order [lonmin,latmin,lonmax,latmax] e.g. bbox=[-120,40,-119,41]
        cwa: string, optional
            NWS county warning area e.g. cwa='LOX' See http://www.nws.noaa.gov/organization.php for CWA list
        nwsfirezone: string, optional
            NWS Fire Zone e.g. nwsfirezone='LOX241'
        gacc: string, optional
            Name of Geographic Area Coordination Center e.g. gacc='EBCC' See http://gacc.nifc.gov/ for a list of GACCs.
        subgacc: string, optional
            Name of Sub GACC e.g. subgacc='EB07'
        vars: string, optional
            Single or comma separatd list of sensor variables. Will return all stations that match one of provided
            variables. Useful for filtering all stations that sense only certain vars. Do not request vars twice in
            the query. e.g. vars='wind_speed,pressure' Use the variables method to see a list of sensor vars.
        status: string, optional
            A value of either active or inactive returns stations currently set as active or inactive in the archive.
            Omitting this param returns all stations. e.g. status='active'
        units: string, optional
            String or set of strings and pipes separated by commas. Default is metric units. Set units='ENGLISH' for
            FREEDOM UNITS ;) Valid  other combinations are as follows: temp|C, temp|F, temp|K; speed|mps, speed|mph,
            speed|kph, speed|kts; pres|pa, pres|mb; height|m, height|ft; precip|mm, precip|cm, precip|in; alti|pa,
            alti|inhg. e.g. units='temp|F,speed|kph,metric'
        groupby: string, optional
            Results can be grouped by key words: state, county, country, cwa, nwszone, mwsfirezone, gacc, subgacc
            e.g. groupby='state'

        Returns:
            Dictionary of precipitation observations through the get_response() method.

        Raises:
            None.
        """

        self._check_geo_param(kwargs)
        kwargs['start'] = start
        kwargs['end'] = end
        kwargs['token'] = self.api_token

        return self._get_response('stations/precipitation', kwargs)

    def timeseries_obs(self, start, end, **kwargs):
        r""" Returns a dictionary of time series of observations at a user specified location for a specified time.
        Users must specify at least one geographic search parameter ('stid', 'state', 'country', 'county', 'radius',
        'bbox', 'cwa', 'nwsfirezone', 'gacc', or 'subgacc') to obtain observation data. Other parameters may also be
        included. See below mandatory and optional parameters. Also see the station_list() method for station IDs.

        Arguments:
        ----------
        start: string, mandatory
            Start date in form of YYYYMMDDhhmm. MUST BE USED WITH THE END PARAMETER. Default time is UTC
            e.g., start='201306011800'
        end: string, mandatory
            End date in form of YYYYMMDDhhmm. MUST BE USED WITH THE START PARAMETER. Default time is UTC
            e.g., end='201306011800
        obtimezone: string, optional
            Set to either UTC or local. Sets timezone of obs. Default is UTC. e.g. obtimezone='local'.
        showemptystations: string, optional
            Set to '1' to show stations even if no obs exist that match the time period. Stations without obs are
            omitted by default.
        stid: string, optional
            Single or comma separated list of MesoWest station IDs. e.g. stid='kden,kslc,wbb'
        county: string, optional
            County/parish/borough (US/Canada only), full name e.g. county='Larimer'
        state: string, optional
            US state, 2-letter ID e.g. state='CO'.
        country: string, optional
            Single or comma separated list of abbreviated 2 or 3 character countries e.g. country='us,ca,mx'
        radius: list, optional
            Distance from a lat/lon pt as [lat,lon,radius (mi)]e.g. radius=[-120,40,20]
        bbox: list, optional
            Stations within a [lon/lat] box in the order [lonmin,latmin,lonmax,latmax] e.g. bbox=[-120,40,-119,41]
        cwa: string, optional
            NWS county warning area e.g. cwa='LOX' See http://www.nws.noaa.gov/organization.php for CWA list
        nwsfirezone: string, optional
            NWS Fire Zone e.g. nwsfirezone='LOX241'
        gacc: string, optional
            Name of Geographic Area Coordination Center e.g. gacc='EBCC' See http://gacc.nifc.gov/ for a list of GACCs.
        subgacc: string, optional
            Name of Sub GACC e.g. subgacc='EB07'
        vars: string, optional
            Single or comma separatd list of sensor variables. Will return all stations that match one of provided
            variables. Useful for filtering all stations that sense only certain vars. Do not request vars twice in
            the query. e.g. vars='wind_speed,pressure' Use the variables method to see a list of sensor vars.
        status: string, optional
            A value of either active or inactive returns stations currently set as active or inactive in the archive.
            Omitting this param returns all stations. e.g. status='active'
        units: string, optional
            String or set of strings and pipes separated by commas. Default is metric units. Set units='ENGLISH' for
            FREEDOM UNITS ;) Valid  other combinations are as follows: temp|C, temp|F, temp|K; speed|mps, speed|mph,
            speed|kph, speed|kts; pres|pa, pres|mb; height|m, height|ft; precip|mm, precip|cm, precip|in; alti|pa,
            alti|inhg. e.g. units='temp|F,speed|kph,metric'
        groupby: string, optional
            Results can be grouped by key words: state, county, country, cwa, nwszone, mwsfirezone, gacc, subgacc
            e.g. groupby='state'

        Returns:
            Dictionary of time series observations through the get_response() method.

        Raises:
            None.
        """

        self._check_geo_param(kwargs)
        kwargs['start'] = start
        kwargs['end'] = end
        kwargs['token'] = self.api_token

        return self._get_response('stations/timeseries', kwargs)

    def climatology_obs(self, startclim, endclim, **kwargs):
        r""" Returns a dictionary of a climatology of observations at a user specified location for a specified time.
        Users must specify at least one geographic search parameter ('stid', 'state', 'country', 'county', 'radius',
        'bbox', 'cwa', 'nwsfirezone', 'gacc', or 'subgacc') to obtain observation data. Other parameters may also be
        included. See below mandatory and optional parameters. Also see the station_list() method for station IDs.

        Arguments:
        ----------
        startclim: string, mandatory
            Start date in form of MMDDhhmm. MUST BE USED WITH THE ENDCLIM PARAMETER. Default time is UTC
            e.g. startclim='06011800' Do not specify a year
        endclim: string, mandatory
            End date in form of MMDDhhmm. MUST BE USED WITH THE STARTCLIM PARAMETER. Default time is UTC
            e.g. endclim='06011800' Do not specify a year
        obtimezone: string, optional
            Set to either UTC or local. Sets timezone of obs. Default is UTC. e.g. obtimezone='local'.
        showemptystations: string, optional
            Set to '1' to show stations even if no obs exist that match the time period. Stations without obs are
            omitted by default.
        stid: string, optional
            Single or comma separated list of MesoWest station IDs. e.g. stid='kden,kslc,wbb'
        county: string, optional
            County/parish/borough (US/Canada only), full name e.g. county='Larimer'
        state: string, optional
            US state, 2-letter ID e.g. state='CO'.
        country: string, optional
            Single or comma separated list of abbreviated 2 or 3 character countries e.g. country='us,ca,mx'
        radius: list, optional
            Distance from a lat/lon pt as [lat,lon,radius (mi)]e.g. radius=[-120,40,20]
        bbox: list, optional
            Stations within a [lon/lat] box in the order [lonmin,latmin,lonmax,latmax] e.g. bbox=[-120,40,-119,41]
        cwa: string, optional
            NWS county warning area e.g. cwa='LOX' See http://www.nws.noaa.gov/organization.php for CWA list
        nwsfirezone: string, optional
            NWS Fire Zone e.g. nwsfirezone='LOX241'
        gacc: string, optional
            Name of Geographic Area Coordination Center e.g. gacc='EBCC' See http://gacc.nifc.gov/ for a list of GACCs.
        subgacc: string, optional
            Name of Sub GACC e.g. subgacc='EB07'
        vars: string, optional
            Single or comma separatd list of sensor variables. Will return all stations that match one of provided
            variables. Useful for filtering all stations that sense only certain vars. Do not request vars twice in
            the query. e.g. vars='wind_speed,pressure' Use the variables method to see a list of sensor vars.
        status: string, optional
            A value of either active or inactive returns stations currently set as active or inactive in the archive.
            Omitting this param returns all stations. e.g. status='active'
        units: string, optional
            String or set of strings and pipes separated by commas. Default is metric units. Set units='ENGLISH' for
            FREEDOM UNITS ;) Valid  other combinations are as follows: temp|C, temp|F, temp|K; speed|mps, speed|mph,
            speed|kph, speed|kts; pres|pa, pres|mb; height|m, height|ft; precip|mm, precip|cm, precip|in; alti|pa,
            alti|inhg. e.g. units='temp|F,speed|kph,metric'
        groupby: string, optional
            Results can be grouped by key words: state, county, country, cwa, nwszone, mwsfirezone, gacc, subgacc
            e.g. groupby='state'

        Returns:
            Dictionary of climatology observations through the get_response() method.

        Raises:
            None.
        """

        self._check_geo_param(kwargs)
        kwargs['startclim'] = startclim
        kwargs['endclim'] = endclim
        kwargs['token'] = self.api_token

        return self._get_response('stations/climatology', kwargs)

    def station_list(self, **kwargs):
        """ Returns a dictionary of a list of stations (and metadata) that corresponds to user-specified parameters.

        Arguments:
        ---------
        state: string, optional
            US state, 2-letter ID e.g. state='CO'
        county: string, optional
            County/parish/borough (US/Canada only), full name e.g. county='Larimer'
        radius: list, optional
            Distance from a lat/lon pt as [lat,lon,radius (mi)] e.g. radius=[-120,40,20]
        bbox: string, optional
            Stations within a [lon/lat] box in the order [lonmin,latmin,lonmax,latmax] e.g. bbox=[-120,40,-119,41]
        cwa: string, optional
            NWS county warning area (string) e.g. cwa='LOX' See http://www.nws.noaa.gov/organization.php for CWA list
        nwsfirezone: string, optional
            NWS Fire Zone (string) e.g. nwsfirezone='LOX241'
        gacc: string, optional
            Name of Geographic Area Coordination Center e.g. gacc='EBCC' See http://gacc.nifc.gov/ for a list of
            GACC abbreviations
        subgacc: string, optional
            Name of Sub GACC e.g. subgacc='EB07'
        network: string, optional
            Single or comma separated list of network IDs. The ID may be found by using the /networks web service.
            e.g. network='1,2'

        Returns:
            Dictionary of stations through the get_response() method.

        Raises:
            None.
        """

        kwargs['token'] = self.api_token

        return self._get_response('stations/metadata', kwargs)

    def variable_list(self):
        """ Returns a dictionary of a list of variables that could be obtained from the 'vars' param in other functions.
        Some stations may not record all variables listed. Use the station_list() function to return metadata on each
        station.

        Arguments:
        ----------
        None

        Returns:
            Dictionary of variables through the get_response() method.

        Raises:
            None.
        """

        return self._get_response('variables', {'token': self.api_token})


