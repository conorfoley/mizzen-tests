#selenium test that sends garbage characters to mizzen-ui.herokuapp.com and takes a screenshot
#mss requires pyobjc-framework-Quartz and pyobjc-framework-LaunchServices

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import string
from take_screenshot_with_mss import takeScreenshot

numOfGarbageChars = 50 
timesToSubmit = 50
timeToSleep = 0.3 #don't set this below 0.3 or the we app doesn't register Keys.RETURN

def createGarbageText(numOfChars):
	'''creates a string of random garbage characters'''
	ultraGarbage = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(numOfChars))
	return ultraGarbage

class MizzenSearchUI(unittest.TestCase):
	'''class for testing mizzen-ui.herokuapp.com input form'''
	def setUp(self):
		
		self.driver = webdriver.Firefox()

	def test_search_in_mizzen_ui(self):

		driver = self.driver
		driver.get("http://mizzen-ui.herokuapp.com")
		inputForm = driver.find_element_by_tag_name("input")
		
		def submitForm(keysToSend, numberOfTimesToSend):
			for i in range(numberOfTimesToSend):
				inputForm.send_keys(keysToSend)
				time.sleep(timeToSleep)
				inputForm.send_keys(Keys.RETURN)
				time.sleep(timeToSleep)

		submitForm(createGarbageText(numOfGarbageChars), timesToSubmit)
	def tearDown(self):

		time.sleep(9.0) 
		takeScreenshot('mizzen-ui-ss-'+str(numOfGarbageChars)+'chars-'+str(timesToSubmit)+'times-sent.png')
		

		self.driver.close()

if __name__ == "__main__":
	unittest.main()
