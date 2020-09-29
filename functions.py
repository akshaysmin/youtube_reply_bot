from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_clickable(element,id,wait_time,method = 'id'):
	if method == 'id':
		return WebDriverWait(element, wait_time).until(EC.element_to_be_clickable((By.ID, id)))

def sing_a_song():
	print('********** are for comments\n---------- are for replies\n########## are my replies')

# Function to convert into UwU text 
def generateUwU(input_text):
    vowels = ['a','e','i','o','u']
    length = len(input_text) 
    output_text = '' 
      
    # check the cases for every individual character 
    for i in range(length): 
          
        # initialize the variables 
        current_char = input_text[i] 
        previous_char = '&# 092;&# 048;'
          
        # assign the value of previous_char 
        if i > 0: 
            previous_char = input_text[i - 1] 
          
        # change 'L' and 'R' to 'W' 
        if current_char == 'L' or current_char == 'R': 
            output_text += 'W'
        
        # change 'l' and 'r' to 'w' 
        elif current_char == 'l' or current_char == 'r': 
            output_text += 'w'
          
        # if the current character is 'o' or 'O' 
        # also check the previous charatcer 
        elif current_char.lower() in vowels: 
            if previous_char == 'N' or previous_char == 'n' or previous_char == 'M' or previous_char == 'm': 
                output_text += "yo"
            else: 
                output_text += current_char
 
	#replace th with ff
        elif current_char == 'H' or current_char == 'h':
        	if previous_char == 'T' or previous_char == 't':
        		output_text += "ff"
        	else: 
                	output_text += current_char 
          
        # if no case match, write it as it is 
        else: 
        	output_text += current_char 
  
    return output_text 

def get_comment_info(comment):
	cauth_name = comment.find_element_by_id('author-text').text
	ctext = comment.find_element_by_id('expander').text
	cchannel = comment.find_element_by_id('author-thumbnail').find_element_by_tag_name('a').get_attribute('href')
	return cauth_name, ctext,cchannel

def get_reply(cauth_name, ctext):
	#'lol'
	return 'UwU\n' + generateUwU(ctext)

def reply_to(comment,driver=None,wait_time = 10):
	cauth_name, ctext, cchannel = get_comment_info(comment)
	reply_text = get_reply(cauth_name, ctext)
	toolbar = comment.find_element_by_id('toolbar')
	#reply_button = toolbar.find_element_by_id('reply-button-end')
	reply_button = get_clickable(toolbar,'reply-button-end',wait_time)
	if driver is not None:			#it is recommended to input driver as argument
		driver.execute_script('arguments[0].scrollIntoView(false)',reply_button)
	reply_button.click()
	commentbox = comment.find_element_by_id('commentbox')
	commentbox.find_element_by_id('contenteditable-root').send_keys(reply_text)
	submit_button = commentbox.find_element_by_id('submit-button')
	submit_button.click()
	print(f'##########\nreplied to {cauth_name} by the text :\n{reply_text}')

def like_count(comment):
	toolbar = comment.find_element_by_id('toolbar')
	return toolbar.find_element_by_id('vote-count-middle').text

def get_latest_video_url(driver,channel_link="https://www.youtube.com/c/LostPause/videos"):
	#"https://www.youtube.com/user/LostPause"
	#"https://www.youtube.com/c/LostPause/videos"
	driver.get(channel_link)
	videos_list = driver.find_element_by_id("page-manager").find_element_by_tag_name("ytd-two-column-browse-results-renderer").find_element_by_id("contents").find_element_by_id("contents").find_elements_by_tag_name("ytd-grid-video-renderer")
	latest_video_url = videos_list[0].find_element_by_id("video-title").get_attribute('href')
	return latest_video_url

def youtube_signin(): # youtube must be loaded first #this function is under development and abandoned for cookies
	#signin
	email = 'nanoisnotarobotfightme@gmail.com'
	login_link = driver.find_element_by_id('masthead').find_element_by_id('container').find_element_by_id('end').find_element_by_tag_name('ytd-button-renderer').find_element_by_tag_name('a').get_attribute('href')
	driver.get(login_link)
	#email
	#driver.find_element_by_tag_name('form').find_element_by_tag_name('input').send_keys(email+'\n')
	driver.find_element_by_tag_name('form').find_element_by_id('Email').send_keys(email+'\n')
	time.sleep(5)
	#password
	password = 'nanimonai'
	driver.find_element_by_tag_name('form').find_element_by_id('password').click()
	driver.find_element_by_tag_name('form').find_element_by_id('password').find_element_by_tag_name('input').send_keys(password+'\n')
	time.sleep(5)