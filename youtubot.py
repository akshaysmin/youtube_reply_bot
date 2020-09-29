from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from time import sleep
from datetime import datetime
from sys import argv
from functions import *

##########
video_link = 'https://www.youtube.com/watch?v=zspAWmeHpRo'
driver_path = r"D:\ProgramData\Python add-ons\geckodriver.exe"
start_comment = 0
max_wait_time = 10 #seconds
explicit_wait_time = 20 #seconds
max_comment_read = 10#0
max_comment_load_attempts = 500
scroll_wait_time = 10
cookies_signin = [{'name': 'YSC', 'value': 'dCVxBZQaLHw', 'path': '/', 'domain': '.youtube.com', 'secure': True, 'httpOnly': True, 'sameSite': 'None'}, {'name': 'VISITOR_INFO1_LIVE', 'value': 'btiBzXf3T2c', 'path': '/', 'domain': '.youtube.com', 'secure': True, 'httpOnly': True, 'expiry': 1616039017, 'sameSite': 'None'}, {'name': 'GPS', 'value': '1', 'path': '/', 'domain': '.youtube.com', 'secure': False, 'httpOnly': False, 'expiry': 1600488817, 'sameSite': 'None'}, {'name': 'SID', 'value': '1gcZCpjNUltPBMza1SZEkl-5yFXf79-_biuHH7t9sijH1jMUaV_VL56ssf10K3mxbm9cww.', 'path': '/', 'domain': '.youtube.com', 'secure': False, 'httpOnly': False, 'expiry': 1663559574, 'sameSite': 'None'}, {'name': '__Secure-3PSID', 'value': '1gcZCpjNUltPBMza1SZEkl-5yFXf79-_biuHH7t9sijH1jMUuMfZ60ryJL7oEc6SfmZ6jA.', 'path': '/', 'domain': '.youtube.com', 'secure': True, 'httpOnly': True, 'expiry': 1663559574, 'sameSite': 'None'}, {'name': 'HSID', 'value': 'A0MvVelgHIdQospxS', 'path': '/', 'domain': '.youtube.com', 'secure': False, 'httpOnly': True, 'expiry': 1663559574, 'sameSite': 'None'}, {'name': 'SSID', 'value': 'AwPP-_qanKYE7jJip', 'path': '/', 'domain': '.youtube.com', 'secure': True, 'httpOnly': True, 'expiry': 1663559574, 'sameSite': 'None'}, {'name': 'APISID', 'value': '2OLGG7IFKUJFdLxr/AtKl4vn_RImD3bp9X', 'path': '/', 'domain': '.youtube.com', 'secure': False, 'httpOnly': False, 'expiry': 1663559574, 'sameSite': 'None'}, {'name': 'SAPISID', 'value': 'CfIhABsK36cQKYfj/AfgTaFzOajhqLQa7V', 'path': '/', 'domain': '.youtube.com', 'secure': True, 'httpOnly': False, 'expiry': 1663559574, 'sameSite': 'None'}, {'name': '__Secure-3PAPISID', 'value': 'CfIhABsK36cQKYfj/AfgTaFzOajhqLQa7V', 'path': '/', 'domain': '.youtube.com', 'secure': True, 'httpOnly': False, 'expiry': 1663559574, 'sameSite': 'None'}, {'name': 'CONSENT', 'value': 'YES+IN.en+201912', 'path': '/', 'domain': '.youtube.com', 'secure': True, 'httpOnly': False, 'expiry': 2146723199, 'sameSite': 'None'}, {'name': 'LOGIN_INFO', 'value': 'AFmmF2swRgIhANmGoMox_faMDmrrCyBYJIgjyxy97jltDiJHwxvjWyQXAiEAwVnlGKIyzwZZ__z1MA7ptabPik47Z4_jj2KDf0fWqAY:QUQ3MjNmeXdleWdvcmhJVU5Sa3dwWV9yRG9fVU1La1VNa1NkTGtkOGhXSWJ2TEhBb240N1dMeVN2cEFiZkdVbW5TRUVmVUlUV3JreVR2VktaUHFPTWRIT0I2X3pvLUlGNjlQeEMxUVFzelBjVGxkcDVoRmptM0tyRlRUWEEtSGp2SkU2dzNrVDQ2Z3RfOVdfeDNWNWY1T05FVl9rN29hMDEtdWlwaUE0aERlN2d5dDhpMVdGY21qN3N1ZlhsS2t6akY5d25zam1rNVFZ', 'path': '/', 'domain': '.youtube.com', 'secure': True, 'httpOnly': True, 'expiry': 1663559575, 'sameSite': 'None'}, {'name': 'SIDCC', 'value': 'AJi4QfHXNO-ctuOBWiL_z9R5UkfGyWsTsO3fV-46u4fiAPYL-lmL4buEdSo2UPkkcDSTEFEd0Q', 'path': '/', 'domain': '.youtube.com', 'secure': False, 'httpOnly': False, 'expiry': 1632023598, 'sameSite': 'None'}, {'name': '__Secure-3PSIDCC', 'value': 'AJi4QfEnjCjeA8MREqQXHedFuTYEwgAyxIvP9YVcYmumsdMuro_FioqWj_Y98sqNRzputBfN', 'path': '/', 'domain': '.youtube.com', 'secure': True, 'httpOnly': True, 'expiry': 1632023598, 'sameSite': 'None'}]
#"https://www.youtube.com/c/LostPause/videos"
##########

options = Options()
#options.headless = True

driver = webdriver.Firefox(executable_path=driver_path,options=options)
driver.get('https://www.youtube.com')
temp = [driver.add_cookie(c) for c in cookies_signin]

###
if len(argv)==3:
	channel_link = argv[1]
	video_link = get_latest_video_url(driver,channel_link=channel_link) if 'videos' in channel_link else channel_link
	max_comment_read = int(argv[2])
elif len(argv)==4:
	channel_link = argv[1]
	video_link = get_latest_video_url(driver,channel_link=channel_link) if 'videos' in channel_link else channel_link
	max_comment_read = int(argv[2])
	start_comment = int(argv[3])
	print(f'start_comment = {start_comment}')
###

def do_stuff_to_comment(ci,block):
	comment = block.find_element_by_id('comment')
	cauth_name, ctext, cchannel = get_comment_info(comment)
	print(f'**********{ci}\nname   : {cauth_name}\nchannel : {cchannel}\ncomment :\n{ctext}')

	#toolbar = comment.find_element_by_id('toolbar')
	#like_button = toolbar.find_element_by_id('like-button')
	#like_count = toolbar.find_element_by_id('vote-count-middle').text
	#creator_heart = toolbar.find_element_by_id('creator-heart')
	
	reply_to(comment,wait_time = 1000,driver=driver)

	''' #this section works well, but is unneccessary for this purpose for now
	reply = block.find_element_by_id('replies')
	#more_replies_button = get_clickable(block,'more-replies',explicit_wait_time)
	more_replies_button = block.find_elements_by_id('more-replies')

	if len(more_replies_button)!=0 and more_replies_button[0].is_displayed():
		more_replies_button = more_replies_button[0]
		more_replies_button.click()
		#rcontents = reply.find_element_by_id('expander-contents')
	
		#reply.find_element_by_id('less-replies').click()
		#sleep(5)
	
		lreplies = reply.find_element_by_id('loaded-replies').find_elements_by_tag_name('ytd-comment-renderer')
		sec_wasted = 0
		while not lreplies:
			sleep(1)
			lreplies = reply.find_element_by_id('loaded-replies').find_elements_by_tag_name('ytd-comment-renderer')
			sec_wasted += 1
			if sec_wasted == max_wait_time:
				break	
		#WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath('//*[@class="statusList"]'))
		for ri,onereply in enumerate(lreplies):
			rauth_name, rtext, rchannel = get_comment_info(onereply)
			print(f'----------{ci+1}-{ri+1}\nname   : {rauth_name}\nchannel : {rchannel}\ncomment :\n{rtext}')
	'''

def do_stuff_to_comments(comments,index=0,start_comment=0):
	for ci,block in enumerate(comments):
		if index+ci>=start_comment:
			#print(f'index+ci>=start_comment={start_comment}', )
			do_stuff_to_comment(index+ci,block)
	return index + len(comments)

#input('Press Enter after you login and comment section is loaded')	
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def do_stuff_with_video_link(video_link,start_comment=0):
	print('target video : ',video_link)
	driver.get(video_link)

	csection = driver.find_elements_by_id('comments')
	while not csection:
		sleep(1)
		csection = driver.find_elements_by_id('comments')
	csection = csection[0]

	comments = []#csection.find_element_by_id('contents').find_elements_by_tag_name('ytd-comment-thread-renderer')
	comments_done =[]
	last_loop = False
	cindex = 0
	comment_load_attempts = 0

	while len(csection.find_elements_by_id('contents'))==0:
		driver.execute_script('arguments[0].scrollIntoView()',csection)

	while True:
		comments_now = csection.find_element_by_id('contents').find_elements_by_tag_name('ytd-comment-thread-renderer')

		if clen == len(comments_now):
			comment_load_attempts += 1	
		else:
			clen = len(comments_now)
	
		if clen>max_comment_read:
			comments_now = comments_now[0:max_comment_read]
			last_loop = True
			clen = max_comment_read
		elif comment_load_attempts > max_comment_load_attempts:
			last_loop = True
	
		comments = list(set(comments_now)-set(comments_done)) #| is for union, & is for intersection, - is for substract
	
		print('considering ',clen,'comments')
		cindex = do_stuff_to_comments(comments,index=cindex,start_comment = start_comment)
		comments_done += comments
	
		if last_loop: break
	
		if clen==0:
			driver.execute_script('arguments[0].scrollIntoView()',csection)
		else:
			last_comment = comments_now[-1]
			driver.execute_script('arguments[0].scrollIntoView()',last_comment)
		sleep(10)

today = '1'#datetime.today().strftime('%d')
def on_server(channel_link,today):
	while True:
		if today!=datetime.today().strftime('%d'):
			print('hwaaa.. back to work UwU')
			video_link = get_latest_video_url(driver,channel_link=channel_link)
			do_stuff_with_video_link(video_link)
			today = datetime.today().strftime('%d')
		else:
			print('I dont see anything new.. Im gonna sleep for an hour zzz')
			sleep(3600)#an hour

if __name__=='__main__':
	do_stuff_with_video_link(video_link,start_comment=start_comment)
