from base import *
import os, sys

class Add_Projects(HPTestCase):
	
	@unittest.skipIf(IS_LIVE, 'Do not run on live')
	@logged_in
	@url('/en/person/{0}/'.format(ID_USER))
	def test_add_premium_collection(self):
		self.e_wait('.create-collection-card')
		
		self.assertEqual('kris.test00', self.e('.profile-meta h2').text)
		self.e('.create-collection-card').click()
		self.e_wait('.ui-autocomplete-input')
		sleep(1)
		
		self.e('.ui-autocomplete-input').send_keys('KrisTestTwitter')						# add manager
		sleep(2)
		
		self.e('.ui-autocomplete li:nth-of-type(1)').click()								# collection manager drop menu
		self.e('.project-title').send_keys('Automated Collection')
		self.e('#short-description').send_keys('Automated Collection')
		self.e('#mce_0').send_keys('Automated Collection')									# long description
		self.e('#get-in-touch').send_keys('@automation awesome')
		self.e('#location-search').send_keys('greenland')
		sleep(1)
		
		self.e('#location-search').send_keys(Keys.ENTER)
		
		instance(self, '#map')																# left side map
		instance(self, '.hp-editor-map-cnt')												# location map
		self.e('.add-input').send_keys('http://vjs.zencdn.net/v/oceans.mp4')				# video landing screen
		self.e('[for="explore-view-gallery"]').click()
		self.e('[for="open-collection"] .switch').click()
		self.e('[for="custom-add-pin"] .switch').click()
		self.e('[name="add_pin_text"]').send_keys('Selenium field')							# add custom name
		self.e('[for="show-navigation-tags"] .switch').click()
		self.e('#s2id_autogen1').send_keys('3.14!@#$%^&*()_+?><|}{:;~,' , 'automated,')		# add tags
		self.e('#sort-select').click()														# default gallery sorting
		sleep(1)
		
		self.e('#sort-select :nth-of-type(2)').click()										# recently added gallery sorting
		displayed(self, '.map-overlay-col .button')											# send a request button
		displayed(self, '.map-overlay-preview')
		displayed(self, '#blog-feed')
		displayed(self, '.white-bg')														# cancel button
		self.e('#button_save').click()
		self.e_wait('.title')
		
		self.assertTitle('Historypin | Automated Collection')
		
		self.delete_collection()
		
	@logged_in
	@url('/en/person/{0}/'.format(ID_USER))
	def delete_collection(self):
		self.e_wait('.project-item .icon-trash')
		sleep(1)
		
		self.assertEqual('now', self.e('.activity li:first-of-type .time').text)
		self.assertEqual('kris.test00', self.e('.profile-meta h2').text)
		self.assertEqual('Automated Collection', self.e('.project-item h3').text)
		self.e(".project-item .icon-trash").click()											# delete project
		sleep(2)
		
		self.accept_alert()																	# submit popup window
		
		self.go('/en/person/{0}/'.format(ID_USER))
		self.e_wait('.project-item .icon-trash')
		
		self.assertEqual('Premium Automated Collection', self.e('.project-item h3').text)


