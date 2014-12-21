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

if __name__=='__main__':
	testOrder=Order("mushrooms",10)
	print repr(testOrder)
	self.assertEqual(testName,"mushrooms","Invalid item name")