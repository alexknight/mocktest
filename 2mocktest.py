from mock import Mock

class Foo(object):
# instance properties
	_fooValue = 123
	def callFoo(self):
		print "Foo:callFoo_"
	def doFoo(self, argValue):
		print "Foo:doFoo:input = ", argValue
mockFoo = Mock(spec = Foo, return_value = "narf")
print mockFoo
print mockFoo.call_args

mockFoo()
print mockFoo.call_args

mockFoo("troz")
print mockFoo.call_args

# mockFoo("zort")
# # print mockFoo.call_args
# mockFoo.callFoo()
# print mockFoo.call_args