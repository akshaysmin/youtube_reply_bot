
csection = driver.find_element_by_id('comments')
comments = csection.find_element_by_id('contents').find_elements_by_tag_name('ytd-comment-thread-renderer')

for block in comments:
	comment = block.find_element_by_id('comment')
	cauth_name, ctext, cchannel = get_comment_info(comment)
	print(f'**********\nname   : {cauth_name}\nchannel : {cchannel}\ncomment :\n{ctext}')

	try:
		reply = block.find_element_by_id('replies')
		reply.find_element_by_id('more-replies').click()
		#reply.find_element_by_id('less-replies').click()
		time.sleep(5)
		lreplies = reply.find_element_by_id('loaded-replies')
#WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath('//*[@class="statusList"]'))
		
		onereply=lreplies[0]
		rauth_name, rtext, rchannel = get_comment_info(onereply)
		print(f'----------\nname   : {rauth_name}\nchannel : {rchannel}\ncomment :\n{rtext}')
	except Exception as e:
		print('some error')
		print(e.__doc__)