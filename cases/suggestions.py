# -*- coding: utf-8 -*-

from base import *

class Suggestions(HPTestCase):
	
	@unittest.expectedFailure  # to test with test photo, suggestions should be allowed on the map
	@url('dialog:/%d/tab:write-story/suggest:title/' % ID_MAP_ITEM)
	def test_title_suggestion(self):
		# TODO
		title_option = self.e('#suggestion_field option:nth-of-type(2)')
		self.assertTrue(title_option.is_selected())
		self.assertEqual('Title', title_option.text)
		
		self.e('#suggestion_title input').send_keys('Bulgarian theater')
		
		self.e('.apply').click()
		
		alert = self.browser.switch_to_alert()
		alert.accept()
		
		self.e('.write_story').send_keys('I think this is the right title')
		self.e('.apply').click()
		
		sleep(4)
		
		self.assertTrue(self.e('#info-dialog'), WebElement)
		
		title_suggestion = ('.stories_list .suggestion.title')
		self.assertEqual(self.e('#photo-side .photo-title').text, title_suggestion.e('.ba_from .value').text)  # to compare if the title is equal to photo title
		
		self.assertEqual('Bulgarian theater'				, title_suggestion.e('.ba_to .value').text)
		self.assertEqual('I think this is the right title'	, title_suggestion.e('.story_cnt').text)
		
		self.assertTrue(self.e('.suggestion-accept'), WebElement)
		self.assertTrue(self.e('.icon.delete'), WebElement)
		
		self.e('.icon.delete').click()
		alert = self.browser.switch_to_alert()
		alert.accept()
		
		self.assertFalse(title_suggestion, WebElement)
		
		# TODO refactor this when suggestions are on the map
		pass
	
	@unittest.expectedFailure
	@url('dialog/%d/tab:write-story/suggest:date/' % ID_MAP_ITEM)
	def test_specific_date_suggestion(self):
		
		sp_date_option = self.e('#suggestion_field option:nth-of-type(3)')
		self.assertTrue(sp_date_option.is_selected())
		self.assertEqual('Date', sp_date_option.text)
		
		self.e('#day option:nth-of-type(4)').click()
		self.e('#month option:nth-of-type(10)').click()
		self.e('#year option:nth-of-type(4)').click()
		
		# TODO check if it is correct
		self.assertEqual('disabled', self.e('#year_from').get_attribute('class'))
		self.assertEqual('disabled', self.e('#year_to').get_attribute('class'))
		
		self.e('.apply').click()
		
		alert = self.browser.switch_to_alert()
		alert.accept()
		
		self.e('.write_story').send_keys('I think this is the right specific date')
		self.e('.apply').click()
		# TODO
		
		sp_date_suggestion = ('.stories_list .suggestion.date')
		self.assertEqual(self.e('#photo-side .photo-date').text		, sp_date_suggestion.e('.ba_from .value').text)  # to compare if the title is equal to photo title
		self.assertEqual('3 September 2012'							, sp_date_suggestion.e('.ba_to .value').text)
		self.assertEqual('I think this is the right specific date'	, sp_date_suggestion.e('.story_cnt').text)
		
		self.assertTrue(self.e('.suggestion-accept'), WebElement)
		self.assertTrue(self.e('.icon.delete'), WebElement)
		
		self.e('.icon.delete').click()
		alert = self.browser.switch_to_alert()
		alert.accept()
		
		self.assertFalse(sp_date_suggestion, WebElement)
		
		# TODO refactor this when suggestions are on the map
		pass
	
	@url('/%d' % ID_MAP_ITEM)
	def test_timeframe_date_suggestion(self):
		# TODO
		# open link /tab:write-story/suggest:date/
		# check if date option is selected
		# select timefime
		# check if the specific options have class disabled
		# click publish
		# accept the allert
		# enter a description
		# check the suggestion in comments
		# delete the suggestion
		
		# TODO refactor this when suggestions are on the map
		pass
	
	@url('/%d' % ID_MAP_ITEM)
	def test_tags_suggestion(self):
		# TODO
		# open link /tab:write-story/suggest:keywords/
		# check if tags option is selected
		# clear all tags and type some new ones
		# click "publish"
		# agree the alert
		# enter a description
		# click publish
		# assert the comment section in the dialog
		# delete the suggestion
		
		# TODO refactor this when suggestions are on the map
		pass
	
	@url('/%d' % ID_MAP_ITEM)
	def test_location_suggestion(self):
		# TODO
		# open link /tab:suggestion-location/suggest:location/
		# assert map
		# assert current address
		# assert GO, cancel and save
		# send keys to new address, e.g. bulevard "Knyaginya Maria Luiza" 9-11, 1000 Sofia, Bulgaria
		# click GO
		# click Save
		# assert the new address in the location suggestion section
		# click publish
		# accept the allert
		# enter a description
		# check the suggestion section
		# delete the suggestion
		
		# TODO refactor this when suggestions are on the map
		pass
	
	@url('/%d' % ID_MAP_ITEM)
	def test_streetview_suggestion(self):
		# TODO
		# open link /tab:suggestion-location/suggest:streetview/
		# drag and drop the image with SV
		# click Record position
		# assert SV suggestion
		# click publish
		# accept the allert
		# enter a description
		# check the suggestion section
		# delete the suggestion
		
		# TODO refactor this when suggestions are on the map
		pass
	
