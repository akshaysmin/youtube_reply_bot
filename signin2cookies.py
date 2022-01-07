from selenium import webdriver
from time import sleep
import sys
import json

#####
url = 'https://www.youtube.com'
file = 'cookies.dat'
driver_path = r"D:\ProgramData\Python add-ons\geckodriver.exe"

how_to_use = '''***** How to Use *****

signin2cookies.py
	--> this uses default driver_path "D:\ProgramData\Python add-ons\geckodriver.exe", goes to default url 'https://www.youtube.com', prompts to signin and saves cookies to default file 'cookies.dat' after you click ENTER
signin2cookies.py url file 
	--> this uses default driver_path "D:\ProgramData\Python add-ons\geckodriver.exe", goes to given url, prompts to signin and saves cookies to given file after you click ENTER
signin2cookies.py driver_path url file 
	--> this uses given driver_path, goes to given url, prompts to signin and saves cookies to given file after you click ENTER
extra options:
-firefox --> to use firefox
-chrome  --> to use chrome
'''
control_driver = webdriver.Firefox
#####

print(how_to_use)

if '-firefox' in sys.argv:
	control_driver = webdriver.Firefox
	driver_path = r"D:\ProgramData\Python add-ons\geckodriver.exe"
	sys.argv.remove('-firefox')
elif '-chrome' in sys.argv:
	control_driver = webdriver.Chrome
	driver_path = r"D:\ProgramData\Python add-ons\chromedriver.exe"
	sys.argv.remove('-chrome')

while '-firefox' in sys.argv:
	sys.argv.remove('-firefox')
while '-chrome' in sys.argv:
	sys.argv.remove('-chrome')

if len(sys.argv)==3:
	url = sys.argv[1]
	file = sys.argv[2]
elif len(sys.argv)==4:
	driver_path = sys.argv[1]
	url = sys.argv[2]
	file = sys.argv[3]
elif len(sys.argv)==1:
	pass
else:
	sys.exit()

print('On loading the site, signin and visit site again to get cookies')

driver = control_driver(executable_path=driver_path)

#driver.execute_script("alert('Signin to website to get cookies');")
	
input('After signin, click ENTER')

driver.get(url)
cookies = driver.get_cookies()

with open(file,'w') as f:
	json.dump(cookies,f)

print(f'Successfully saved cookies of the site "{url}" in the file "{file}"')
#driver.execute_script("url=arguments[0];file=arguments[1];alert('Successfully saved cookies of the site \"' + url + '\" in the file \"' + file+'\"');",url,file)
