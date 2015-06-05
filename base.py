import unittest

from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement


from conf import *

def web_element_exists(self, selector):
	try:
		self.e(selector)
		return True
	except NoSuchElementException:
		return False

WebElement.e	= WebElement.find_element_by_css_selector
WebElement.es	= WebElement.find_elements_by_css_selector
WebElement.css	= WebElement.value_of_css_property
WebElement.exists = web_element_exists
WebElement.parent_node = lambda self: self.find_element_by_xpath('./parent::node()')



def url(url):
	def wrapper(fn):
		def wrapped(*args, **kwargs):
			args[0].go(url)
			
			sleep(1)
			
			fn(*args, **kwargs)
		return wrapped
	return wrapper


def logged_in(fn):
	def wrapped(*args, **kwargs):
		args[0].login_cookie_set()
		fn(*args, **kwargs)
		args[0].login_cookie_del()
	return wrapped


# class Browser(webdriver.Firefox):
class Browser(webdriver.Chrome):
	def go(self, url):
		self.get(('' if url.startswith('http') else URL_BASE) + url)
		self.pageload_wait()
		sleep(2)
	
	def es(self, selector):
		return self.find_elements_by_css_selector(selector)
	
	exists = web_element_exists
	
	def e(self, selector):
		return self.find_element_by_css_selector(selector)
	
	def e_wait(self, selector, timeout = 30):
		try:
			w = WebDriverWait(self, timeout)
			return w.until(lambda driver: driver.e(selector))
		except:
			raise NoSuchElementException('The element could not be found')
	
	def pageload_wait(self, timeout = 30):
		sleep(1)
		# TODO Fix this to work with something else than dummy sleep
		# self.e_wait('body')
		# try:
		# 	w = WebDriverWait(self, timeout)
		# 	return w.until(lambda driver: driver.execute_script("return document.readyState;") == "complete")
		# except:
		# 	raise Exception('Page could not load')
	
	def hover(self, elem):
		ActionChains(self).move_to_element(elem).perform()
		sleep(.5)
	
	def double_click(self, elem):
		ActionChains(self).double_click(elem).perform()
		sleep(.5)  # TODO is this necessary
	
	def click_xy(self, elem, x, y):
		ActionChains(self).move_to_element_with_offset(elem, x, y).click().perform()
		sleep(.5)  # TODO is this necessary



class TestCase(unittest.TestCase):
	@classmethod
	def browser_start(cls, browser):
		cls.browser = browser
		cls.browser.maximize_window()
		
		cls.go				= cls.browser.go
		cls.refresh			= cls.browser.refresh
		cls.es				= cls.browser.es
		cls.e				= cls.browser.e
		cls.e_wait			= cls.browser.e_wait
		# cls.pageload_wait	= cls.browser.pageload_wait
		cls.hover			= cls.browser.hover
		cls.double_click	= cls.browser.double_click
	
	@classmethod
	def browser_close(cls):
		cls.browser.close()
	
	def assertTitle(self, title):
		self.assertIn(title, self.browser.title)


LOGIN_COOKIES = []

def run(*tests):
	import cases
	
	suite = unittest.TestSuite()
	
	if tests:
		for i in tests:
			i = i.split('.')
			
			test_case = getattr(cases, i[0])
			if len(i) > 1:
				suite.addTest(test_case(i[1]))
			else:
				suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_case))
	else:
		suite.addTests(unittest.TestLoader().loadTestsFromModule(cases))
	
	# TestCase.browser_start(Browser())
	TestCase.browser_start(Browser(PATH_CRHOME_DRIVER))
	# HPTestCase.login()
	
	unittest.TextTestRunner(verbosity = 1).run(suite)
	TestCase.browser_close()


class HPTestCase(TestCase):
	@classmethod
	def login(cls):
		cls.go('/user/')
		
		login = cls.e('#site-content #login-google')
		login.click()
		sleep(3)
		
		cls.e('#Email').send_keys('gabriela.ananieva@historypin.org')
		cls.e('#Passwd').send_keys('tristania1010')
		cls.e('#signIn').click()
		sleep(3)
		
		try:
			cls.e('#submit_approve_access').click()
			sleep(3)
		except:
			pass
		
		LOGIN_COOKIES.append(cls.browser.get_cookie('hpsid'))
		
		cls.login_cookie_del()
		
		cls.browser.execute_script('window.stop();')
		sleep(1)
	
	@classmethod
	def login_cookie_set(cls):
		if not LOGIN_COOKIES:
			HPTestCase.login()
		
		for i in LOGIN_COOKIES:
			if i: cls.browser.add_cookie(i)
	
	@classmethod
	def login_cookie_del(cls):
		for i in LOGIN_COOKIES:
			if i: cls.browser.delete_cookie(i['name'])
	
	# def logout(self):
	# 	self.go(URL_BASE + '/user/logout/')
	# 	self.pageload_wait()


