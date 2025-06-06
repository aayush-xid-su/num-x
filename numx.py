import sys
import requests
import json
import time

def banner():
	print('''
 ⣴⠖⢶⡄⠀⢀⡶⠲⣦⢠⡶⠲⣦⠀⠀⣠⠖⠲⡄⣰⠖⢶⡄⠀⠀⠀⢠⡶⠲⣦⠀⠀⠀⠀⠀   ⢠⡶⠳⣄⠀⠀⢠⡴⠳⣦
⡟⠀⠀⠹⣆⢸⡇⠀⢹⢸⠃⠀⢹⠀⠀⣿⠀⠀⡇⠛⠀⠀⠙⢦⠀⣴⠏⠀⠀ ⢸⠀⠀⠀⠀⠀⠀   ⠘⢦⡀⠈⢷⣴⠏⠀⣠⠟
⡇⠀⢠⡄⠀⢿⡇⠀⢸⢸⠀⠀⣼⠀⠀⣿⠀⠀⡇⠀⠀⢰⣄⠀⠛⠁⢠⡆⠀ ⢸⠀⠀⠀⠀⠀⠀   ⠀⠀⢻⣦⠀⠀⢠⡾⠉⠀
⡇⠀⠈⡿⣦⠀⠁⠀⢸⠸⡆⠀⢹⣄⣀⡿⠀⢀⡇⣇⠀⠈⡟⣦⣀⣴⢾⡇⠀⢸ ⣴⠋⠉⠉⠉⢻⡆  ⣠⠟⠁⣠⣤⠀⠙⢦⡀
⣷⠀⢨⡇⠈⢷⣄⠀⣸⠀⠹⣦⣀⠈⠀⢀⣤⠏⠀⣿⡀⢠⡇⠀⠉⠁⢸⣇⠀⣸ ⠈⠓⠒⠒⠒⠋   ⢸⡅⢀⡴⠋⠘⢷⣄⢀⣻
⠈⠉⠉⠀⠀⠀⠉⠉⠁⠀⠀⠀⠉⠛⠛⠉⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀   ⠀   ⠙⠋⠀⠀⠀⠀  ⠙⠛⠁ 
	Author: Xidiotic
	Github: https://github.com/aayush-xid-su             
	''')

def main():
	banner()
	if len(sys.argv) == 2:
		number = sys.argv[1]
		output = requests.get(f'http://apilayer.net/api/validate?access_key={key}&number={number}&country_code=&format=1').text
		obj = json.loads(output)
		
		country_code = obj['country_code']
		country_name = obj['country_name']
		location = obj['location']
		carrier = obj['carrier']
		line_type = obj['line_type']

		print('[+] Phone number information gathering')
		print('--------------------------------------')
		time.sleep(0.2)

		if country_code == '':
			print(' - Getting Country\t\t[ FAILED ]')
		else:
			print(' - Getting Country\t\t[ OK ]')

		time.sleep(0.2)
		if country_name == '':
			print(' - Getting Country Name\t\t[ FAILED ]')
		else:
			print(' - Getting Country Name\t\t[ OK ]')

		time.sleep(0.2)
		if location == '':
			print(' - Getting Location\t\t[ FAILED ]')
		else:
			print(' - Getting Location\t\t[ OK ]')

		time.sleep(0.2)
		if carrier == '':
			print(' - Getting Carrier\t\t[ FAILED ]')
		else:
			print(' - Getting Carrier\t\t[ OK ]')

		time.sleep(0.2)
		if line_type == None:
			print(' - Getting Device\t\t[ FAILED ]')
		else:
			print(' - Getting Device\t\t[ OK ]')

		print('[+] Information Output')
		print('--------------------------------------')
		print(' - Phone number:', number)
		print(' - Country:', country_code)
		print(' - Country Name:', country_name)
		print(' - Location:', location)
		print(' - Carrier:', carrier)
		print(' - Device:', line_type)
	else:
		print('[?] Usage:')
		print('\tnumx.py <phone-number>')
		print('	python3 numx.py +13213707446 (Test Number)')

if __name__ == '__main__':
	config = open('config.json').read()
	data = json.loads(config)
	key = data['api_key']
	main()