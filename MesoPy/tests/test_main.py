from MesoPy import MesoPy as meso

def testvarlist():
    var_list = meso.variable_list()
    print(var_list)
    assert var_list

def testvar():
    var_list = meso.variable_list()
    assert 'relative_humidity' in var_list['VARIABLES']


