# MesoPy Function Documentation
MesoPy contains six functions to retrieve data from the API. Please note, pass optional parameters into the function as string variables e.g. `MesoPy.latest_obs(state='CO', county='Larimer')` 
### Retrieve the Latest Observations:
    latest_obs(**kwargs):
        Description: Returns in JSON format latest observations at a user
                    specified location for a specified time. Other parameters
                    may also be included (see below). See the station_list 
                    method for station IDs.  
                    
         Optional Params:
           attime: Date and time in form of YYYYMMDDhhmm for which returned
                   obs are closest. All times are UTC.
                   e.g. attime=201504261800
           within: When used without 'attime', it can be left blank to return
                   the latest ob or represent the number of minutes which would
                   return the latest ob within that time period. When used with
                   'attime' it can be a single number representing a time 
                   period before attime or two comma separated numbers 
                   representing a period before and after the attime
                   e.g. attime=201306011800&within=30,30 would return the ob
                   closest to attime within a 30 minute period before or after 
                   attime.
           obtimezone: Set to either UTC or local. Sets timezone of obs. 
                       Default is UTC. e.g. obtimezone=local
           showemptystations: Set to '1' to show stations even if no obs exist 
                              that match the time period. Stations without obs 
                              are omitted by default.
           stid: Single or comma separated list of MesoWest station IDs. 
                 e.g. stid=kden,kslc,wbb
           state: US state, 2-letter ID e.g. state=CO
           country: Single or comma separated list of abbreviated 2 or 3 
                    character countries e.g. country=us,ca,mx
           county: County/parish/borough (US/Canada only), full name	
                   e.g. county=Larimer
           radius: Distance from a lat/lon pt as [lat,lon,radius (mi)]
                   e.g. radius=-120,40,20 
           bbox: Stations within a [lon/lat] box in the order 
                 [lonmin,latmin,lonmax,latmax] e.g. bbox=-120,40,-119,41
           cwa: NWS county warning area (string) e.g. cwa=LOX	
                See http://www.nws.noaa.gov/organization.php for CWA list 
           nwsfirezone: NWS Fire Zone (string) e.g. nwsfirezone=LOX241
           gacc: Name of Geographic Area Coordination Center 
                 e.g. gacc=EBCC See http://gacc.nifc.gov/ for a list of GACC 
                 abbreviations
           subgacc: Name of Sub GACC e.g. subgacc=EB07	
           vars: single or comma separatd list of sensor variables. Will return
                 all stations that match one of provided variables. Useful for 
                 filtering all stations that sense only certain vars. Do not 
                 request vars twice in the query. e.g. vars=wind_speed,pressure
                 Use the variables method to see a list of sensor vars
           status: A value of either active or inactive returns stations 
                   currently set as active or inactive in the archive. Omitting
                   this param returns all stations e.g. status=active
           units: string or set of strings and by pipes separated by commas. 
                  Default is metric units. Set units=ENGLISH for FREEDOM UNITS 
                  ;) Valid  other combinations are as follows: temp|C, temp|F, 
                  temp|K; speed|mps, speed|mph, speed|kph, speed|kts; pres|pa, 
                  pres|mb; height|m, height|ft; precip|mm, precip|cm, 
                  precip|in; alti|pa, alti|inhg. 
                  e.g. units=temp|F,speed|kph,metric
           groupby: Results can be grouped by key words: state, county,
                    country, cwa, nwszone, mwsfirezone, gacc, subgacc
                    e.g. groupby=state
### Retrieve Accumlated Precipitation Observations:
    precipitation_obs(**kwargs)
        Description: Returns in JSON format accumulated precipitation 
                     observations at a user specified location for a specified 
                     time. Other parameters may also be included (see above). 
                     See the station_list method for station IDs. 
                     
        Optional Params:
           start: Start date in form of YYYYMMDDhhmm. MUST BE USED WITH THE 
                  END PARAMETER. Default time is UTC
                  start=201306011800
           end: End date in form of YYYYMMDDhhmm. MUST BE USED WITH THE 
                START PARAMETER. Default time is UTC
                end=201306011800
           obtimezone: Set to either UTC or local. Sets timezone of obs. 
                       Default is UTC. e.g. obtimezone=local
           showemptystations: Set to '1' to show stations even if no obs exist 
                              that match the time period. Stations without obs 
                              are omitted by default.
           stid: Single or comma separated list of MesoWest station IDs. 
                 e.g. stid=kden,kslc,wbb
           state: US state, 2-letter ID e.g. state=CO
           country: Single or comma separated list of abbreviated 2 or 3 
                    character countries e.g. country=us,ca,mx
           county: County/parish/borough (US/Canada only), full name	
                   e.g. county=Larimer
           radius: Distance from a lat/lon pt as [lat,lon,radius (mi)]
                   e.g. radius=-120,40,20 
           bbox: Stations within a [lon/lat] box in the order 
                 [lonmin,latmin,lonmax,latmax] e.g. bbox=-120,40,-119,41
           cwa: NWS county warning area (string) e.g. cwa=LOX	
                See http://www.nws.noaa.gov/organization.php for CWA list 
           nwsfirezone: NWS Fire Zone (string) e.g. nwsfirezone=LOX241
           gacc: Name of Geographic Area Coordination Center 
                 e.g. gacc=EBCC See http://gacc.nifc.gov/ for a list of GACC 
                 abbreviations
           subgacc: Name of Sub GACC e.g. subgacc=EB07	
           vars: single or comma separatd list of sensor variables. Will return
                 all stations that match one of provided variables. Useful for 
                 filtering all stations that sense only certain vars. Do not 
                 request vars twice in the query. e.g. vars=wind_speed,pressure
                 Use the variables method to see a list of sensor vars
           status: A value of either active or inactive returns stations 
                   currently set as active or inactive in the archive. Omitting
                   this param returns all stations e.g. status=active
           units: string or set of strings and by pipes separated by commas. 
                  Default is metric units. Set units=ENGLISH for FREEDOM UNITS 
                  ;) Valid  other combinations are as follows: temp|C, temp|F, 
                  temp|K; speed|mps, speed|mph, speed|kph, speed|kts; pres|pa, 
                  pres|mb; height|m, height|ft; precip|mm, precip|cm, 
                  precip|in; alti|pa, alti|inhg. 
                  e.g. units=temp|F,speed|kph,metric
           groupby: Results can be grouped by key words: state, county,
                    country, cwa, nwszone, mwsfirezone, gacc, subgacc
                    e.g. groupby=state

### Retrieve Observations over a Time Period:
    timeseries_obs(**kwargs)

       Parameters: token: assigned within library
       
       Optional Params:
           start: Start date in form of YYYYMMDDhhmm. MUST BE USED WITH THE 
                  END PARAMETER. Default time is UTC
                  start=201306011800
           end: End date in form of YYYYMMDDhhmm. MUST BE USED WITH THE 
                START PARAMETER. Default time is UTC
                end=201306011800
           recent: In lieu of a start and end date/time, return a timeseries of
                   observations for the last n minutes. e.g. latest=60
           output: Changes the output to csv or JSON format if requesting a 
                   single station time series. Default is JSON unless requested
                   time series is longer than two years e.g. output=csv
           obtimezone: Set to either UTC or local. Sets timezone of obs. 
                       Default is UTC. e.g. obtimezone=local
           showemptystations: Set to '1' to show stations even if no obs exist 
                              that match the time period. Stations without obs 
                              are omitted by default.
           stid: Single or comma separated list of MesoWest station IDs. 
                 e.g. stid=kden,kslc,wbb
           state: US state, 2-letter ID e.g. state=CO
           country: Single or comma separated list of abbreviated 2 or 3 
                    character countries e.g. country=us,ca,mx
           county: County/parish/borough (US/Canada only), full name	
                   e.g. county=Larimer
           radius: Distance from a lat/lon pt as [lat,lon,radius (mi)]
                   e.g. radius=-120,40,20 
           bbox: Stations within a [lon/lat] box in the order 
                 [lonmin,latmin,lonmax,latmax] e.g. bbox=-120,40,-119,41
           cwa: NWS county warning area (string) e.g. cwa=LOX	
                See http://www.nws.noaa.gov/organization.php for CWA list 
           nwsfirezone: NWS Fire Zone (string) e.g. nwsfirezone=LOX241
           gacc: Name of Geographic Area Coordination Center 
                 e.g. gacc=EBCC See http://gacc.nifc.gov/ for a list of GACC 
                 abbreviations
           subgacc: Name of Sub GACC e.g. subgacc=EB07	
           vars: single or comma separatd list of sensor variables. Will return
                 all stations that match one of provided variables. Useful for 
                 filtering all stations that sense only certain vars. Do not 
                 request vars twice in the query. e.g. vars=wind_speed,pressure
                 Use the variables method to see a list of sensor vars
           status: A value of either active or inactive returns stations 
                   currently set as active or inactive in the archive. Omitting
                   this param returns all stations e.g. status=active
           units: string or set of strings and by pipes separated by commas. 
                  Default is metric units. Set units=ENGLISH for FREEDOM UNITS 
                  ;) Valid  other combinations are as follows: temp|C, temp|F, 
                  temp|K; speed|mps, speed|mph, speed|kph, speed|kts; pres|pa, 
                  pres|mb; height|m, height|ft; precip|mm, precip|cm, 
                  precip|in; alti|pa, alti|inhg. 
                  e.g. units=temp|F,speed|kph,metric
           groupby: Results can be grouped by key words: state, county,
                    country, cwa, nwszone, mwsfirezone, gacc, subgacc
                    e.g. groupby=state
        
### Retrieve a Climatology of Observations:
    climatology_obs(**kwargs)

        Description: Returns in JSON a time series of observations at a user 
                     specified location for a specified time. Other parameters 
                     may also be included (see above). See the station_list 
                     method for station IDs.           
        Optional Params:
           startclim: Start date in form of YYYYMMDDhhmm. MUST BE USED WITH THE 
                      ENDCLIM PARAMETER. Default time is UTC
                      startclim=201306011800
           endclim: End date in form of YYYYMMDDhhmm. MUST BE USED WITH THE 
                    STARTCLIM PARAMETER. Default time is UTC
                    endclim=201306011800
           recent: In lieu of a start and end date/time, return a timeseries of
                   observations for the last n minutes. e.g. latest=60
           output: Changes the output to csv or JSON format if requesting a 
                   single station time series. Default is JSON unless requested
                   time series is longer than two years e.g. output=csv
           obtimezone: Set to either UTC or local. Sets timezone of obs. 
                       Default is UTC. e.g. obtimezone=local
           showemptystations: Set to '1' to show stations even if no obs exist 
                              that match the time period. Stations without obs 
                              are omitted by default.
           stid: Single or comma separated list of MesoWest station IDs. 
                 e.g. stid=kden,kslc,wbb
           state: US state, 2-letter ID e.g. state=CO
           country: Single or comma separated list of abbreviated 2 or 3 
                    character countries e.g. country=us,ca,mx
           county: County/parish/borough (US/Canada only), full name	
                   e.g. county=Larimer
           radius: Distance from a lat/lon pt as [lat,lon,radius (mi)]
                   e.g. radius=-120,40,20 
           bbox: Stations within a [lon/lat] box in the order 
                 [lonmin,latmin,lonmax,latmax] e.g. bbox=-120,40,-119,41
           cwa: NWS county warning area (string) e.g. cwa=LOX	
                See http://www.nws.noaa.gov/organization.php for CWA list 
           nwsfirezone: NWS Fire Zone (string) e.g. nwsfirezone=LOX241
           gacc: Name of Geographic Area Coordination Center 
                 e.g. gacc=EBCC See http://gacc.nifc.gov/ for a list of GACC 
                 abbreviations
           subgacc: Name of Sub GACC e.g. subgacc=EB07	
           vars: single or comma separatd list of sensor variables. Will return
                 all stations that match one of provided variables. Useful for 
                 filtering all stations that sense only certain vars. Do not 
                 request vars twice in the query. e.g. vars=wind_speed,pressure
                 Use the variables method to see a list of sensor vars
           status: A value of either active or inactive returns stations 
                   currently set as active or inactive in the archive. Omitting
                   this param returns all stations e.g. status=active
           units: string or set of strings and by pipes separated by commas. 
                  Default is metric units. Set units=ENGLISH for FREEDOM UNITS 
                  ;) Valid  other combinations are as follows: temp|C, temp|F, 
                  temp|K; speed|mps, speed|mph, speed|kph, speed|kts; pres|pa, 
                  pres|mb; height|m, height|ft; precip|mm, precip|cm, 
                  precip|in; alti|pa, alti|inhg. 
                  e.g. units=temp|F,speed|kph,metric
           groupby: Results can be grouped by key words: state, county,
                    country, cwa, nwszone, mwsfirezone, gacc, subgacc
                    e.g. groupby=state
### Retrieve a List of Stations:
    station_list(**kwargs)
        Description: Returns in JSON format a list of stations (and metadata) 
                     that corresponds to user-specified parameters. 
        Parameters: The user may pass in any of the below parameters as strings 
                   state: US state, 2-letter ID e.g. state=CO
                   county: County/parish/borough (US/Canada only), full name	
                           e.g. county=Larimer
                   radius: Distance from a lat/lon pt as [lat,lon,radius (mi)]
                           e.g. radius=-120,40,20 
                   bbox: Stations within a [lon/lat] box in the order 
                         [lonmin,latmin,lonmax,latmax] e.g. bbox=-120,40,-119,41
	 	           cwa: NWS county warning area (string) e.g. cwa=LOX	
                        See http://www.nws.noaa.gov/organization.php for CWA 
                        list 
                   nwsfirezone: NWS Fire Zone (string) e.g. nwsfirezone=LOX241
                   gacc: Name of Geographic Area Coordination Center 
                         e.g. gacc=EBCC See http://gacc.nifc.gov/ for a list 
                         of GACC abbreviations
                   subgacc: Name of Sub GACC e.g. subgacc=EB07	
 
### Retrieve a List of Variables:
    variable_list()
     
       Description: Returns in JSON format a list of variables that could be
                    obtained from the 'vars' param in other methods. Some 
                    stations may not record all variables listed. Use the 
                    station_list method to return metadata on each station.
