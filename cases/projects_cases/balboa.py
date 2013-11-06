# -*- coding: utf-8 -*-

from base import *

class Project_Balboa(HPTestCase):
	@url('/project/6-balboa')
	def test_index(self):
		
		self.assertTitle('Balboa Park | Home')
		
		logo_link = self.e('#logo-title a')
		
		self.assertEqual('http://balboapark.org/', logo_link.get_attribute('href'))
		self.assertEqual('%s/resources/images/webapps/balboa/logo.png' % URL_BASE, logo_link.e('img').get_attribute('src'))
		
		self.assertEqual('%s/attach/project/6-balboa/photos/index/' % URL_BASE, self.e('#embed-frame').get_attribute('src'))
		
		balboa_link = 'http://www.balboapark.org'
		
		footer_items = [
			['%s/info/' % balboa_link				, 'About'],
			['%s/faq' % URL_BASE					, 'FAQs'],
			['%s/terms-and-conditions' % URL_BASE	, 'Terms & Conditions'],
			['%s/contact/' % balboa_link			, 'Contact'],
		]
		
		footer = self.e('#supp')
		footer_links = footer.es('li a')
		
		for n in range(len(footer_items)):
			i = footer_items[n]
			self.assertEqual(i[0], footer_links[n].get_attribute('href'))
			self.assertEqual(i[1], footer_links[n].text)
		
	
	@url('/attach/project/6-balboa/map/')
	def test_map_tab(self):
		
		filter_bar = self.e('#filter-bar')
		
		self.assertEqual('Search tags', filter_bar.e('label').text)
		self.assertIsInstance(filter_bar.e('input')	, WebElement)
		self.assertIsInstance(self.e('#tags_search'), WebElement)
		
		date_slider_icons = self.es('#date-slider a')
		self.assertIn('ss-icon'		, date_slider_icons[0].e('span').get_attribute('class'))
		self.assertIn('ss-location'	, date_slider_icons[0].e('span').get_attribute('class'))
		
		self.assertIn('ss-icon'		, date_slider_icons[1].e('span').get_attribute('class'))
		self.assertIn('ss-location'	, date_slider_icons[1].e('span').get_attribute('class'))
		
		self.e('.hp-marker.hp-marker-cluster').click()
		sleep(3)
		
		cluster = self.e('#galleryInfoWindow_contents li:nth-of-type(1)')
		
		self.assertIsInstance(cluster.e('.hp-info-gallery-pin img'), WebElement)
		self.assertIsInstance(cluster.e('.info h6 a'), WebElement)
		self.assertIsInstance(cluster.e('.info p'), WebElement)
		
	
	@url('/attach/project/6-balboa/collections/all/')
	def test_collections_tab(self):
		pass
	
	@url('/attach/project/6-balboa/contribute/')
	def test_contribute_tab(self):
		pass
	
	