from urllib import urlopen

def func():
	url_ip='http://ifconfig.me/ip'
	ip=None
	try:
		ip=urlopen(url_ip)
	except:
		pass
	return ip

if __name__=='__main__':
	print(func())