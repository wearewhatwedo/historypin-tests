# -*- coding: utf-8 -*-

from base import *

# TODO - refactor links for japan projects, when they are set live

JAPAN_LINK = 'http://www.v5-japan.historypin-hrd.appspot.com'
FUJINOMIYA_LINK = '%s/jp/project/47-fujinomiya-project' % JAPAN_LINK

class Project_Fujinomiya(HPTestCase):
	
	@url(FUJINOMIYA_LINK)
	def test_index(self):
		
		self.assertTitle('Fujinomiya project')
		blog_link = 'http://blog.historypin.jp'
		
		site_cnt = self.e('#site')
		nav_links = site_cnt.es('.primary a')
		
		self.assertEqual('%s/resources/images/project-japan/historypin-logo.png' % JAPAN_LINK, nav_links[0].e('img').get_attribute('src'))
		self.assertEqual('http://www.historypin.jp/jp', nav_links[0].get_attribute('href'))
		
		self.assertEqual('%s/' % FUJINOMIYA_LINK, nav_links[1].get_attribute('href'))
		self.assertEqual(u'ホーム', nav_links[1].text)
		
		self.assertEqual('%s/explore/#|map/' % FUJINOMIYA_LINK, nav_links[2].get_attribute('href'))
		self.assertEqual(u'探索', nav_links[2].text)
		
		self.assertEqual('%s/upload/' % FUJINOMIYA_LINK, nav_links[3].get_attribute('href'))
		self.assertEqual(u'投稿', nav_links[3].text)
		
		self.assertEqual('%s/' % blog_link		, nav_links[4].get_attribute('href'))
		self.assertEqual(u'ブログ', nav_links[4].text)
		
		self.assertEqual('%s/about/' % blog_link		, nav_links[5].get_attribute('href'))
		self.assertEqual(u'富士宮プロジェクトについて', nav_links[5].text)
		
		self.assertEqual('%s/faq/' % blog_link		, nav_links[6].get_attribute('href'))
		self.assertEqual(u'よくある質問', nav_links[6].text)
		
		user_links = site_cnt.es('.secondary a')
		
		self.assertEqual('%s/user/' % FUJINOMIYA_LINK, user_links[0].get_attribute('href'))
		self.assertEqual(u'アカウント作成', user_links[0].text)
		
		self.assertEqual('%s/user/' % FUJINOMIYA_LINK, user_links[1].get_attribute('href'))
		self.assertEqual(u'ログイン', user_links[1].text)
		
		self.assertEqual(u'富士宮プロジェクト', self.e('.sec-header h1').text)
		
		self.assertEqual('%s/jp/attach/project/47-fujinomiya-project/map/index/' % JAPAN_LINK, self.e('#embed-frame').get_attribute('src'))
		
		touts_items = [
			['/fujinomiya/about/'						, u'富士宮プロジェクトについて（外部サイト）'	, u'富士宮プロジェクトについて詳しく知る'	, 'tout1_image'],
			['/category/historypin-japan/fujinomiya/'	, u'富士宮プロジェクトブログ'				, u'富士宮プロジェクトの最新情報'		, 'tout2_image'],
		]
		
		h3s_links	= self.es('.w23 .inner h3 a')
		paragraphs	= self.es('.w23 .inner p')
		imgs_links	= self.es('.w23 .inner p + a')
		imgs		= self.es('.w23 .inner a img')
		
		for n in range(len(touts_items)):
			i = touts_items[n]
			self.assertEqual(blog_link + i[0], h3s_links[n].get_attribute('href'))
			self.assertEqual(blog_link + i[0], imgs_links[n].get_attribute('href'))
			self.assertEqual(i[1], h3s_links[n].text)
			self.assertEqual(i[2], paragraphs[n].text)
			self.assertEqual(JAPAN_LINK + '/projects/img/pid/47/dim/285x290/type/' + i[3] + '/crop/1/', imgs[n].get_attribute('src'))
		
		activity = self.e('#activity')
		self.assertIsInstance(activity.e('h1'), WebElement)
		self.assertEqual(u'総投稿数', activity.e('h6').text)
		
		item_feed = self.e('.activity li:nth-of-type(1)')
		self.assertIsInstance(item_feed.e('a')	, WebElement)
		self.assertIsInstance(item_feed.e('img'), WebElement)
		
		
		icon_tout1 = self.e('#icon-tout-0 a')
		
		# self.assertEqual('http://www.historypin.com/project/39-japan/', icon_tout1.get_attribute('href')) TODO Fix links for icon touts when live
		self.assertEqual(u'Historypin Japan に戻る'							, icon_tout1.text)
		self.assertIn('ss-icon'		, icon_tout1.e('span').get_attribute('class'))
		self.assertIn('ss-undo'		, icon_tout1.e('span').get_attribute('class'))
		
		icon_tout2 = self.e('#icon-tout-1 a')
		
		# self.assertEqual('http://www.historypin.com/'	, icon_tout2.get_attribute('href')) TODO fix link when live
		self.assertEqual(u'Historypin.com (グローバルサイト）へ移動)', icon_tout2.text)
		self.assertIn('ss-icon'		, icon_tout2.e('span').get_attribute('class'))
		self.assertIn('ss-search'	, icon_tout2.e('span').get_attribute('class'))
		
		supported = self.e('.footer .supported_by span')
		self.assertEqual('%s/fujinomiya/about/' % blog_link, supported.e('a').get_attribute('href'))
		self.assertEqual(u'富士宮プロジェクト実行委員会', supported.e('a').text)
		
		self.assertIsInstance(self.e('.addthis_toolbox'), WebElement)
		self.assertEqual(u'シェア:', self.e('.addthis_toolbox h3').text)
		
		self.assertEqual(u'使用写真はhalsan2000さんとtajima.tomocomさんがシェアしたものです。', self.e('.photos-by span').text)
		
		footer = self.e('.footer-links')
		footer_links = footer.es('a')
		
		footer_items = [
			['%s/terms-and-conditions/'	% blog_link, 'Terms and conditions'],
			['%s/privacy-policy/'		% blog_link, 'Privacy policy'],
			['%s/cookies/'				% blog_link, 'Cookies'],
			['http://wearewhatwedo.org/'			, u'© We Are What We Do'],
		]
		
		for n in range(len(footer_items)):
			i = footer_items[n]
			self.assertEqual(i[0], footer_links[n].get_attribute('href'))
			self.assertEqual(i[1], footer_links[n].text)
	
