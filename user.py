from _input import _bal , _pin
#import atm_def
#print("welcome\t "+ atm_def.name + "\t sbi grp")

def _bank(name):
    print("welcome\t "+ name + "\t sbi grp")
    bankinfo = ['balance', 'transfer',"pin change","mini statment"]
    for i in range(len(bankinfo)):
        print( str(i)+ "\t" + bankinfo[i])
    a = bankinfo[int(input("entre the "))]
    if a == bankinfo[0]:
        _b = _bal(name)
        print("check ur bal" + str(_b) )
        #print("bala")
    elif a == bankinfo[1]:
        print("please entre the a/c no" )
        print("please entre the pin")
        pin = input("entre the pin")
        b = _input._pin(pin)
        c = input("")
        if  _b == c :
            print("rohit your transfer money done")
        else:
            print("recheck ur pin")

_bank("code test")
