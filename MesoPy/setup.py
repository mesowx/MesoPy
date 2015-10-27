from distutils.core import setup
setup(
  name = 'MesoPy',
  py_modules = ['MesoPy'],
  version = '1.1.2',
  description = 'A pure python wrapper for the MesoWest API',
  author = 'Josh Clark',
  author_email = 'joclark@ucar.edu',
  url = 'https://github.com/jclark754/MesoPy',
  download_url = 'https://github.com/jclark754/MesoPy/tarball/1.1.2',
  keywords = ['weather API climate MesoWest meteorology'],
  classifiers = [], requires=['requests']
)
