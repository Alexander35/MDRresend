from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time
import configparser
from log import logger_setup

class MDRResend_bot:
	def __init__(self, config):
		self.uri = config['URI']['URI']
		self.user = config['MDR']['USER']
		self.password = config['MDR']['PASSWORD']
		binary = FirefoxBinary(r'c:\Program Files\Mozilla Firefox\firefox.exe')
		self.driver = webdriver.Firefox(firefox_binary=binary)
		self.logger = logger_setup(__name__)

	def resend_one(self, id):
		try:
			self.driver.get(
				'http://'
				+self.user+':'
				+self.password+'@'
				+self.uri
				+'?id='+id
				)
			self.logger.info('id : {} begin'.format(id))
			time.sleep(1)
			button = self.driver.find_element_by_id('btnResend')
			button.click()
			alert = self.driver.switch_to_alert()
			alert.accept()
			self.logger.info('id : {} end'.format(id))
		except Exception as exc:
			self.logger.error(
				'An error occured when performing id : {} {}'
				.format(id, exc)
				)