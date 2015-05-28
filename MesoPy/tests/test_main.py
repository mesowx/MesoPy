from MesoPy import MesoPy as meso
from nose.tools import eq_, ok_


# Basic Function Tests
def testvarlistfunc():
    var_list = meso.variable_list()
    ok_(var_list)


def teststationsfunc():
    stations = meso.station_list(state='CO', county='Larimer')
    ok_('KFNL' == stations['STATION'][1]['STID'])


def testtimeseriesfunc():
    timeseries = meso.timeseries_obs(stid='kfnl', start='201504261800', end='201504262300')
    ok_(timeseries)


def testclimatologyfunc():
    climatology = meso.climatology_obs(stid='kden', startclim='04260000', endclim='04270000', units='precip|in')
    ok_(climatology)


def testprecipfunc():
    precip = meso.precipitation_obs(stid='kfnl', start='201504261800', end='201504271200', units='precip|in')
    ok_(precip)


# Miscellaneous Tests
def testvarexists():
    var_list = meso.variable_list()
    ok_('relative_humidity' in var_list['VARIABLES'])


def testlateststrlist():
    latest = meso.latest_obs(stid=['kfnl', 'kden', 'ksdf'])
    # assert len(latest['STATION'])==3
    eq_(len(latest['STATION']), 3)
