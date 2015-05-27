from MesoPy import MesoPy as meso
from nose.tools import eq_

def testvarlist():
    var_list = meso.variable_list()
    print(var_list)
    assert var_list

def testvar():
    var_list = meso.variable_list()
    assert 'relative_humidity' in var_list['VARIABLES']

def teststations():
    stations = meso.station_list(state='CO', county='Larimer')
    print(stations)
    assert 'KFNL' == stations['STATION'][1]['STID']

def testlatest():
    latest = meso.latest_obs(stid='kfnl,kden,kbou')
    print(latest)
    assert latest

def testlateststrlist():
    latest = meso.latest_obs(stid= ['kfnl', 'kden', 'ksdf'])
    #assert len(latest['STATION'])==3
    eq_(len(latest['STATION']), 3)



