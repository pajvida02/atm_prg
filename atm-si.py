
gret = 'welcome to sbi bank \n '
print(gret.title())
_opt1 = ["0- banking","1-transfer"] #banking
for i in _opt1:
	print(i,"\n")
_in = int(input("entre the value"))
if _opt1[_in] == '0- banking':
	print("select the following option")
	_opt2 = ['withdraw','pin change','mini statment',]
	for i in _opt2:
		print(i, "\n")
	#print(_opt2, "\n")
	_a = int(input())
	if _opt2[_a] == _opt2[0]:     ##withdraw
		print("entre the amount")
		opt2a = int(input("amout"))
		print(opt2a,"ok")
		#print("entre the pin")
		#pin = int(input("please the value"))
		for i in range(3):
			print("entre the pin")
			pin = str(input("please the value"))
			if pin == str(1234):
				print("congo","have nice")
				break
			elif pin == str(''):
				print("please the entre the pin")
			else:
				print("please try again")
	elif _opt2[_a] == _opt2[1]: #pin change
		print("please entre your pin")
		for i in range(3):
			a = str(input("entre your pin \n"))
			if a == str(1234):
				print("please type new pin")
				_b = int(input("entre the new pin"))
				print('ur pin update')
				break
			elif a == "":
				print("sorry please type")
			else:
				print("please re-type your pin")
		print("end")
# 	elif _opt2[a] == 'mini statement':
#		print("your balance is 2500")
elif _opt1[_in] == '1-transfer':
	print("transfer money")
	print("entre your pin")
	a = str(input("entre the a/c no"))
	b = str(input("entre the money"))
	print(a, "\n",b)
	pin = str(input(""))
	if pin == 1234:
		print('done success')
	else:
		print("wrong pin")
	print('exit')
