'''
Test Battery for our sample app
Created on 20151201
@author: marcelo, carlos@xt6.us
@changelog:
'''

import unittest

from cm2c.commons.gen.utils import get_tmp_fn
from cm2c.csvimport.sql3load import sql3load

#--
class Test(unittest.TestCase):
	def setUp(self):
		pass
	# end def

	def tearDown(self):
		pass
	# end def

	def testCase1(self):
		self.assertEqual(1+2,3)
		pass

# end class

## end class Test

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
