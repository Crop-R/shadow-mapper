from setuptools import setup, Extension
import numpy

shadowmap = Extension('c_shadowmap',
                      include_dirs=[numpy.get_include()],
                      sources=['shadowmap.c'])

setup(name='shadow-mapper',
      version='0.2',
      description='Where\'s the sun?',
      url='https://github.com/Crop-R/shadow-mapper',
      author=u'Per Liedman/ Tom de Ruijter/ Erik-Jan Blanksma',
      author_email='erikjan@dacom.nl',
      ext_modules=[shadowmap])
