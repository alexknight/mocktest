import unittest
import mock
from main import func

class FuncTestCase(unittest.TestCase):
	@mock.patch('main.urlopen')
	def test_func(self,mock_open11):
		mock_open11.return_value='127.0.0.1'
		result=func()
		mock_open11.assert_called_with('http://ifconfig.me/ip')
		self.assertEqual(result,'127.0.0.1')

if __name__=='__main__':
	unittest.main()