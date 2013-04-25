# -*- coding: utf-8 -*-

from base import *

class Community(HPTestCase):
	@unittest.skip("TODO")
	@url('/community/')
	def test_home(self):
		self.assertTitle('Historypin | Community Homepage')
		self.assertEqual(self.e('.info h1').text, 'Get Involved')
		self.assertEqual(self.e('.main-image img').get_attribute('src'), URL_BASE + '/resources/images/channels/channels_home_promo_image.jpg')
		self.assertEqual(self.e('.info p').text, 'Welcome to the Historypin community, made up of people, groups and organisations working together to unearth and pin as much history as possible from all over the world - from within archives, in attics, and saved up in wise old heads.')
		
		sel = '#schools_section a'
		self.assertEqual(self.e(sel).get_attribute('href'), URL_BASE + '/community/schools')
		self.assertEqual(self.e(sel).text, 'Schools')

		sel = '#localprojects_section a'
		self.assertEqual(self.e(sel).get_attribute('href'), URL_BASE + '/community/localprojects')
		self.assertEqual(self.e(sel).text, 'Local projects')

		sel = '#lams_section a'
		self.assertEqual(self.e(sel).get_attribute('href'), URL_BASE + '/community/lams')
		self.assertEqual(self.e(sel).text, 'Libraries, Archives\n and Museums')

		self.assertEqual(self.e('.grid h2:nth-child(1)').text, 'Latest News')

		self.assertEqual(self.e('h2:nth-of-type(2)').text, 'Challenges')
		# TODO fix HTML first

		# TODO
		# assert title done 
		# assert heading done
		# assert text done
		# assert image done
		# assert schools linka and text done
		# assert local projects link and text done
		# LAMs link and text done
		# latest news heading done
		# verify elements present LATER
		# challenges title done
		# sub-titles 
		# links
		# text
		# images
		# get involved title
		# sub-headings
		# images
		# link
		# text

	@url('/community/schools')
	def test_sidebar(self):
		sidebar = [
			['Community Homepage', URL_BASE + '/community', 'Lots of news, ideas, and info for Historypinners round the world'],
			['Schools Homepage', URL_BASE + '/community/schools', 'Want to run a Historypin session or event in your school?'],
			['Local Projects Homepage', URL_BASE + '/community/localprojects', 'Want to run a Historypin session or event with your group?'],
			['Libraries, Archives and Museums Homepage', URL_BASE + '/community/lams', 'Want to get your institution involved?'],
			['Libraries, Archives and Museums Involved', URL_BASE + '/community/lams-involved', 'Find out the institutions that are already sharing their history on Historypin.'],
			['How To Guides', URL_BASE + '/community/howtos', 'Downloadable pdfs and videos to explain how to do everything'],
			['Activities & Downloadables for schools', URL_BASE + '/community/schools-resources', 'Resources to make running sessions and events easier.'],
			['Activities & Downloadables for projects', URL_BASE + '/community/localprojects-resources', 'Resources to make running sessions and events easier.'],
			['Topics to Explore', URL_BASE + '/community/topics-to-explore', 'Some of the most interesting photos, Tours and Collections to explore in sessions.'],
			['School Case Studies', URL_BASE + '/community/schools-case-studies', 'Some examples of schools around the word using Historypin'],
			['Local Project Case Studies', URL_BASE + '/community/localprojects-case-studies', 'Some examples of local projects around the world using Historypin'],
			['Support Us', 'http://www.historypin.com/donate/', u'Donate to Friends of Historypin and you’ll be helping support Historypin Community and Education Programmes.\n\nRegistered Charity Number 1134546'],
			['Blog', 'http://blog.historypin.com/', 'Find out the latest community, site development, partnership and Challenges news'],
			['Contact', URL_BASE + '/contact-us', 'For more information contact Rebekkah Abraham, Historypin Content Manager on rebekkah.abraham@wearewhatwedo.org.'],
		]
		
		headings = self.es('.sidebar .inner h4')
		paragraphs = self.es('.sidebar .inner p')
		for n in (range(len(sidebar))):
			i = sidebar[n]
			self.assertEqual(headings[n].text, i[0])
			self.assertEqual(headings[n].e('a').get_attribute('href'), i[1])
			self.assertEqual(paragraphs[n].text, i[2])
			
		self.assertEqual(self.e('.sidebar .inner p:last-of-type a').get_attribute('href'), 'mailto:rebekkah.abraham@wearewhatwedo.org')
	
	@url('/community/schools')
	def test_home_schools(self):
		self.assertTitle('Historypin | Community | Schools')
		self.assertEqual(self.e('h1.title').text, 'Schools')
		self.assertEqual(self.e('.section img').get_attribute('src'), 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/schools_main.jpg')
		
		questions = [
			['Why use Historypin in schools?', '', ''],
			['How can I use it?', URL_BASE + '/community/howtos', 'Have a look at our How to Guides for more help'],
			['How are other schools using it?', URL_BASE + '/community/schools-case-studies', 'Have a look at our Case Studies for some ideas'],
			['What are the best things to look at in the classroom?', URL_BASE + '/community/topics-to-explore', 'Have a look at our Topics to Explore for some ideas'],
			['What activity ideas and resources do you have?', URL_BASE + '/community/schools-resources', 'See our Activities and Downloadables'],
		]
		
		headings = self.es('.section h3')
		paragraphs = self.es('.section p a')
		k = 0
		for n in (range(len(questions))):
			i = questions[n]
			self.assertEqual(headings[n].text, i[0])
			
			if i[1] and i[2]:
				self.assertEqual(paragraphs[k].get_attribute('href'), i[1])
				self.assertEqual(paragraphs[k].text, i[2])
				
				k += 1
		
	@url('/community/localprojects')
	def test_home_projects(self):
		self.assertTitle('Historypin | Community | Local Projects')
		self.assertEqual(self.e('h1.title').text, 'Local Projects')
		self.assertEqual(self.e('.section img').get_attribute('src'), 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/localprojects_main.jpg')
		
		questions = [
			['Why use Historypin in local projects?', '', ''],
			['How can I use it?', URL_BASE + '/community/howtos', 'Have a look at our How to Guides for more help'],
			['How are other local projects using it?', URL_BASE + '/community/localprojects-case-studies', 'Have a look at our Local Projects Case Studies for some ideas'],
			['What are the best things to look at?', URL_BASE + '/community/topics-to-explore', 'Have a look at our Topics to Explore for some ideas'],
			['What activity ideas and resources do you have?', URL_BASE + '/community/localprojects-resources', 'See our Activites and Downloadables for Local Projects'],
		]
		
		headings = self.es('.section h2')
		paragraphs = self.es('.section p a')
		k = 0
		for n in (range(len(questions))):
			i = questions[n]
			self.assertEqual(headings[n].text, i[0])
			
			if i[1] and i[2]:
				self.assertEqual(paragraphs[k].get_attribute('href'), i[1])
				self.assertEqual(paragraphs[k].text, i[2])
				
				k += 1

	@url('/community/lams')
	def test_home_lams(self):
		self.assertTitle('Historypin | Community | Libraries, Archives & Museums')
		self.assertEqual(self.e('.right h1').text, 'Libraries, Archives and Museums homepage')
		self.assertEqual(self.e('.right img').get_attribute('src'), 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/lams_main.jpg')
		
		# TODO
		# get started heading
		# link and text(Getting started guide)
		# institutions involved heading
		# - link and text
		# bulk upload link and text

	@url('/community/lams-involved')
	def test_lams_involved(self):
		self.assertTitle('Historypin | Community | Schools | Historypin in the Classroom')
		self.assertEqual(self.e('.right h1').text, 'Institutions involved')
		self.assertEqual(self.e('.right h2').text, 'What Institutions are saying about Historypin')
		
		# TODO
		# assert all images under the comments

	@unittest.skip("TODO")
	@url('/community/howtos')
	def test_how_tos(self):
		# TODO
		# assert title 
		# assert heading
		# assert all sub-headings
		#  - assert all links and text 
		pass
	
	@unittest.skip("TODO")
	@url('/community/localprojects-resources')
	def test_projects_resources(self):
		# TODO
		# assert title
		# assert heading
		# Downloadable Resources heading 
		# Activity Sheets/Tip Sheets/Posters, flyers and certificates headings
		# - assert all links 
		# - assert all texts
		# - assert all texts under the link
		pass
	
	@unittest.skip("TODO")
	@url('/community/localprojects-case-studies')
	def test_projects_studies(self):
		# TODO
		# assert title
		# assert heading
		# assert subheadings 
		# - assert links and links texts
		# - assert images
		pass

	@url('/community/localprojects-case-study-magicme')
	def test_projects_studies_magicme(self):
		self.assertTitle('Historypin | Community | Local Projects | Magic Me, Tower Hamlets, London, UK')
		self.assertEqual(self.e('h1.title').text, 'Magic Me, Tower Hamlets, London, UK')
		self.assertEqual(self.e('.section p:nth-of-type(1) img').get_attribute('src'), 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/4c_main.jpg')
		self.assertEqual(self.e('.section p:nth-of-type(9) img').get_attribute('src'), 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/4c_sec.jpg')
		self.assertEqual(self.e('.section p:nth-of-type(4) a').get_attribute('href'), URL_BASE + '/channels/view/6932562/name/magicme/')

	@url('/community/localprojects-case-study-reading')
	def test_projects_studies_reading(self):
		self.assertTitle('Historypin | Community | Local Projects | Reading, Berkshire, UK')
		self.assertEqual(self.e('h1.title').text, 'Reading, Berkshire, UK')
		self.assertEqual(self.e('.section p:nth-of-type(1) img').get_attribute('src'), 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/4a_main.jpg')
		self.assertEqual(self.e('.section p:nth-of-type(5) img').get_attribute('src'), 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/4a_sec.jpg')
		self.assertEqual(self.e('.section p:nth-of-type(8) a').get_attribute('href'), 'http://historypin.com/community-localprojects-reading/') #check this link
		self.assertEqual(self.e('h3:nth-of-type(1)').text, 'What people had to say about it')
		self.assertEqual(self.e('h3:nth-of-type(2)').text, 'What was the impact?')
		# TODO
		# another test case with this page/community-localprojects-reading/

	@url('/community/localprojects-case-study-sanfrancisco')
	def test_projects_studies_sanfrancisco(self):
		self.assertTitle('Historypin | Community | Local Projects | San Francisco, USA')
		self.assertEqual(self.e('h1.title').text, 'San Francisco, USA')
		self.assertEqual(self.e('.section p img').get_attribute('src'), 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/4d_main.jpg')
		self.assertEqual(self.e('.section p:nth-of-type(6) a').get_attribute('href'),'http://historypin.com/sfmta') #check this link
		self.assertEqual(self.e('.section p:nth-of-type(6) a').text, 'SFMTA collection on Historypin')

	@url('/community/localprojects-case-study-lighthouse')
	def test_projects_studies_lighthouse(self):
		self.assertTitle('Historypin | Community | Local Projects | Lighthouse, Brighton, UK')
		self.assertEqual(self.e('h1.title').text, 'Lighthouse, Brighton, UK')
		self.assertEqual(self.e('.section p img').get_attribute('src'), 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/4b_main.jpg')

	@unittest.skip("TODO")
	@url('/community/topics-to-explore')
	def test_topics_to_explore(self):
		# TODO
		# assert title
		# assert heading
		# assert Collection subheading ('s' should be added)
		# - all links
		# - all texts
		# - all all images
		# assert Tours subheading
		# - all links
		# - all texts
		# - all all images
		# assert Photos, Videos and Audio clips subheading
		# - all links
		# - all texts
		# - all all images
		pass

	@unittest.skip("TODO")
	@url('/community/schools-case-studies/')
	def test_schools_studies(self):
		# TODO
		# assert title
		# assert heading
		# assert text
		# assert all subheadings
		# assert all text
		# assert all hrefs
		# assert all images
		#check sidebar
		pass
		
	@url('/community/schools-eic/')
	def test_schools_studies_eic(self):
		self.assertTitle('Historypin | Community | Schools | English International College, Marbella, Spain')
		self.assertEqual(self.e('h1.title').text, 'English International College, Marbella, Spain')
		self.assertEqual(self.e('.section p img').get_attribute('src'), 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/6b_main.jpg')
		self.assertEqual(self.e('h2:nth-of-type(1)').text, 'Amy, Year 9')
		self.assertEqual(self.e('.section p:nth-of-type(10) img').get_attribute('src'), 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/6b_fav1.jpg')
		
	@url('/community/schools-billericay/')
	def test_schools_studies_bill(self):
		self.assertTitle('Historypin | Community | Schools | Billericay School, Essex, UK')
		self.assertEqual(self.e('h1.title').text, 'Billericay School, Essex, UK')
		self.assertEqual(self.e('.section p:nth-of-type(1) img').get_attribute('src'), 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/6d_main.jpg')
		self.assertEqual(self.e('.section p:nth-of-type(12) a').get_attribute('href'),'http://billericayschool.net/speakup/2011/06/pinning-down-history/')
		self.assertEqual(self.e('.section p:nth-of-type(12) a').text,'Read more about the project on their blog.')
		self.assertEqual(self.e('h3:nth-of-type(1)').text, 'Video made by Billericay School for the day')
		self.assertEqual(self.e('h3:nth-of-type(2)').text, 'Feature on Radio Essex about the Billericay Historypin project')
		self.assertEqual(self.e('.section p:nth-of-type(14) img').get_attribute('src'), 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/6d_sec.jpg')
	
	@unittest.skip("TODO")
	@url('/community/schools-cromer/')
	def test_schools_studies_cromer(self):
		# TODO
		# assert title
		# assert heading
		# assert image
		pass
		
	@unittest.skip("TODO")
	@url('/community/schools-nelson/')
	def test_schools_studies_nelson(self):
		# TODO
		# assert title
		# assert heading
		# assert images
		# assert photo link and text
		# assert channel link and text
		pass
		
	@unittest.skip("TODO")
	@url('/community/schools-newport/')
	def test_schools_studies_newport(self):
		# TODO
		# assert title
		# assert heading
		# assert images
		pass
		
	@unittest.skip("TODO")
	@url('/community/schools-resources/')
	def test_schools_resources(self):
		# TODO
		# assert title
		# assert heading
		# assert "Downloadable Resources" text
		# assert Activity Sheets/Tip Sheets/Posters, flyers and certificates
		# - assert all bullets links and text
		# - assert all texts under the bullets
		# assert Activities by subject
		# assert all h3s
		pass

