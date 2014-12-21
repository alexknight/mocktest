class Order(object):
	_orderItem="None"
	_orderAmount=0
	_orderFilled=-1

	def __init__(self,argItem,argAmount):
		print "Order:__init__"

		if (isinstance(argItem,str)):
			if (len(argItem)>0):
				self._orderItem=argItem
		if (argAmount>0):
			self._orderAmount=argAmount

	def __repr__(self):
		locOrder={'item':self._orderItem,'amount':self._orderAmount}
		return repr(locOrder)

	def fill(self,argSrc):
		print "Order:fill_"

		try:
			if(argSrc is not None):
				if(argSrc.hasInventory(self._orderItem)):
					locCount=argSrc.getInventory(self._orderItem,self._orderAmount)
					self._orderFilled=locCount
				else:
					print "Inventory item not available"
			else:
				print "Warehouse not available"
		except TypeError:
			print "Invalid warehouse."

	def isFilled(self):
		print "Order:isFilled_"
		return (self._orderAmount==self._orderFilled)

class Warehouse(object):
	_houseName=None
	_houseList=None

	def warehouseName(self):
		return (self._houseName)
	def inventory(self):
		return (self._houseList)
	def setup(self,argName,argList):
		pass
	def hasInventory(self,argItem):
		pass
	def getInventory(self,argItem,argCount):
		pass
	def addInventory(self,argItem,argCount):
		pass

import unittest
from mock import Mock,call

class OrderTest(unittest.TestCase):
	fooSource=None

	def setUp(self):
		print "OrderTest:setUp_:begin"

		testName=self.id().split(".")
		testName=testName[2]
		print testName

		if (testName=="testA_newOrder"):
			print "OrderTest:setup_:testA_newOrder:RESERVED"
		elif(testName=="testB_nilInventory"):
			self.fooSource=Mock(spec=Warehouse,return_value=None)
		elif (testName=="testC_orderCheck"):
			self.fooSource=Mock(spec=Warehouse)
			self.fooSource.hasInventory.return_value=True
			self.fooSource.getInventory.return_value=0
		elif(testName=="testD_orderFilled"):
			self.fooSource=Mock(spec=Warehouse)
			self.fooSource.hasInventory.return_value=True
			self.fooSource.getInventory.return_value=5
		else:
			print "UNSUPPORTED TEST ROUTINE"

	def tearDown(self):
		print "OrderTest:tearDown_:begin"
		print ""

	def testA_newOrder(self):
		testOrder=Order("mushrooms",10)
























































