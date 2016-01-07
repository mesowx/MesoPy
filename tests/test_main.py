from MesoPy import Meso, MesoPyError
from nose.tools import *

m = Meso(token='demotoken')

# Basic Function Tests
def testvars():
    var_list = m.variables()
    ok_(var_list)


def testmetadata():
    stations = m.metadata(bbox=[-120,40,-119,41])
    ok_(stations)


def testtimeseries():
    timeseries = m.timeseries(stid='kfnl', start='201504261800', end='201504262300')
    ok_(timeseries)


def testclimatology():
    climatology = m.climatology(stid='kden', startclim='04260000', endclim='04270000', units='precip|in')
    ok_(climatology)


def testprecip():
    precip = m.precip(stid='kfnl', start='201504261800', end='201504271200', units='precip|in')
    ok_(precip)


# Miscellaneous Tests

def testlateststrlist():
    latest = m.latest(stid=['kfnl','kden','ksdf'], within='30')
    eq_(len(latest['STATION']), 1)


# Error Handling
@raises(MesoPyError)
def testbadurlstring():
    latest = m.latest(stid='')
    print(latest)


@raises(MesoPyError)
def testauth():
    badtoken = Meso(token='3030')
    badtoken.latest(stid=['kfnl', 'kden', 'ksdf'], within='30')


@raises(MesoPyError)
def testgeoparms():
    m.precip(start='201504261800', end='201504271200', units='precip|in')