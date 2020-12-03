import subprocess
import random

def custommac():
	interfacec = input("interface > ")
	cusmac = input("new MAC > ")

	print("[+] Changing MAC address for " + interfacec + " to " + cusmac)

	subprocess.call(["ifconfig", interfacec, "down"])
	subprocess.call(["ifconfig", interfacec, "hw", "ether", cusmac])
	subprocess.call(["ifconfig", interfacec, "up"])
pass

def randommac():
	symbols1 = ["a", "b", "c", "d", "e", "f"]
	symbols2 = ["a", "b", "c", "d", "e", "f"]
	symbols3 = ["a", "b", "c", "d", "e", "f"]
	symbols4 = ["a", "b", "c", "d", "e", "f"]
	symbols5 = ["a", "b", "c", "d", "e", "f"]
	symbols6 = ["a", "b", "c", "d", "e", "f"]
	symbols7 = ["a", "b", "c", "d", "e", "f"]
	symbols8 = ["a", "b", "c", "d", "e", "f"]
	symbols9 = ["a", "b", "c", "d", "e", "f"]
	symbols10 = ["a", "b", "c", "d", "e", "f"]
	symbols11 = ["a", "b", "c", "d", "e", "f"]
	symbols12 = ["a", "b", "c", "d", "e", "f"]

	evennum1 = ["0", "2", "4", "6", "8"]
	evennum2 = ["0", "2", "4", "6", "8"]

	spl = ":"


	var1 = random.randint(0, 1)
	var2 = random.randint(0, 1)
	var3 = random.randint(0, 1)
	var4 = random.randint(0, 1)
	var5 = random.randint(0, 1)
	var6 = random.randint(0, 1)
	var7 = random.randint(0, 1)
	var8 = random.randint(0, 1)
	var9 = random.randint(0, 1)
	var10 = random.randint(0, 1)
	var11 = random.randint(0, 1)
	var12 = random.randint(0, 1)

	if var1 == 0:
		s1 = str(random.choice(evennum1))
	else:
		s1 = str(random.choice(evennum1))

	if var2 == 0:
		s2 = str(random.choice(evennum2))
	else:
		s2 = str(random.choice(evennum2))

	if var3 == 0:
		s3 = str(random.randint(0, 9))
	else:
		s3 = str(random.choice(symbols3))

	if var4 == 0:
		s4 = str(random.randint(0, 9))
	else:
		s4 = str(random.choice(symbols4))

	if var5 == 0:
		s5 = str(random.randint(0, 9))
	else:
		s5 = str(random.choice(symbols5))

	if var6 == 0:
		s6 = str(random.randint(0, 9))
	else:
		s6 = str(random.choice(symbols6))

	if var7 == 0:
		s7 = str(random.randint(0, 9))
	else:
		s7 = str(random.choice(symbols7))

	if var8 == 0:
		s8 = str(random.randint(0, 9))
	else:
		s8 = str(random.choice(symbols8))

	if var9 == 0:
		s9 = str(random.randint(0, 9))
	else:
		s9 = str(random.choice(symbols9))

	if var10 == 0:
		s10 = str(random.randint(0, 9))
	else:
		s10 = str(random.choice(symbols10))

	if var11 == 0:
		s11 = str(random.randint(0, 9))
	else:
		s11 = str(random.choice(symbols11))

	if var12 == 0:
		s12 = str(random.randint(0, 9))
	else:
		s12 = str(random.choice(symbols12))
	
	gen_mac = s1+s2+spl+s3+s4+spl+s5+s6+spl+s7+s8+spl+s9+s10+spl+s11+s12

	interface = input("interface > ")

	print("[+] Changing MAC address for " + interface + " to " + gen_mac)

	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["ifconfig", interface, "hw", "ether", gen_mac])
	subprocess.call(["ifconfig", interface, "up"])
pass

print("~"*17 + "MAC Changer v1.1" + "~"*17)
print("1) Random MAC")
print("~" * 50)

menu_option = input( " > " )
if menu_option == 1 or "1)" or "1) Random MAC":
	randommac()
else:
	print("~"*17 + "MAC Changer v1.1" + "~"*17)
	print("1) Random MAC")
	print("~" * 50)

	menu_option = input( " > " )
