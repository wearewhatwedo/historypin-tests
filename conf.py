
PATH_CRHOME_DRIVER	= '/usr/lib64/chromium-browser/chromedriver'
GO_TIMEOUT = 1

# VERSION = 'v5-multilingual'
VERSION = 'v5-00-11'
# VERSION = 'http://www.historypin.com'
LINK_BASE = '%s.historypin-hrd.appspot.com' % (VERSION)
# LINK_BASE = 'historypin.com'

URL_BASE = 'http://www.%s' % LINK_BASE

IS_ON_SDK = not (LINK_BASE.endswith('.appspot.com') or LINK_BASE.endswith('.historypin.com'))

if VERSION == 'v5-00-11':
	ID_COLLECTION	= 3033
	ID_TOUR			= 1706
	
	ID_COLLECTION_VIEW	= 2967
	ID_TOUR_VIEW		= 1989
	
	ID_COLLECTION_IMAGES	= [160180, 149729]
	# SQL  National Theatre in Sofia, Bulgaria, - Bulgarian Army Theater [ids from SQL]
	
	ID_TOUR_IMAGES			= [160180, 149729]
	
	# SQL National Theatre in Sofia, Bulgaria, - Bulgarian Army Theater [ids from SQL]
	
	FAVOURITE_CHANNELS			= [26288, 14950, 33328]  # SQL
	FAVOURITE_CHANNELS_IMAGES	= [26288, 14950, 33328]  # SQL
	
	ID_USER			= 35019
	ID_USER_VIEW	= 33283
	
	ID_MAP_ITEM		= 149729  # SQl
	ID_EDIT_ITEM	= 160180  # SQl
	
	ID_PROJECTS			= [3, 5, 6, 8, 10, 15, 22, 26, 34, 39, 41, 44]
	ID_PROJECTS_IMAGES	= [3, 5, 6, 8, 10, 15, 22, 26, 34, 39, 41, 44]
	
	# TODO change the ids after migration
	CHANNELS_EXAMPLES = [2238022, 8721093, 2662022, 6487189, 1042029]
	
	# TODO change the ids after migration
	COLLECTION_EXAMPLES	= [3762008, 6600998, 7700038, 8798159, 8691041]
	TOUR_EXAMPLES		= [8279489, 6631649, 7764038, 8748071, 6605903]
	
else:
	ID_COLLECTION	= 26157007
	ID_TOUR			= 16502051
	
	ID_COLLECTION_VIEW	= 22782015  # when not logged in
	ID_TOUR_VIEW		= 22354015
	
	ID_COLLECTION_IMAGES	= [22363018, 26162010]
	# HP - 322003 - Morden College east elevation and chapel, 2090034- Pinner High St from Church, 22363018 - National Theatre in Sofia, Bulgaria, 26162010 - Bulgarian Army Theater [322003, 2090034, 22363018, 26162010]
	
	ID_TOUR_IMAGES			= [22363018, 26162010]
	
	# HP - 322003 - Morden College east elevation and chapel, 2090034- Pinner High St from Church, 22363018 - National Theatre in Sofia, Bulgaria, 26162010 - Bulgarian Army Theater [322003, 2090034, 22363018, 26162010]
	
	FAVOURITE_CHANNELS			= [7947312, 6994288, 10668143]
	FAVOURITE_CHANNELS_IMAGES	= [7947312, 6994288, 10668143]
	
	ID_USER			= 11675544
	ID_USER_VIEW	= 10649049
	
	ID_MAP_ITEM		= 22363018
	ID_EDIT_ITEM	= 26162010
	
	ID_PROJECTS			= [11461010, 11462012, 11483012, 11499008, 11886013, 13388066, 13839007, 15742010, 16690005, 23580013, 30128133]
	ID_PROJECTS_IMAGES	= [11461010, 11462012, 11483012, 11499008, 11886013, 13388066, 13839007, 15742010, 16690005, 23580013, 30128133]
	
	CHANNELS_EXAMPLES = [2238022, 8721093, 2662022, 6487189, 1042029]

	COLLECTION_EXAMPLES	= [3762008, 6600998, 7700038, 8798159, 8691041]
	TOUR_EXAMPLES		= [8279489, 6631649, 7764038, 8748071, 6605903]

URL_ATTACH = '%s/attach/uid%d' % (URL_BASE, ID_USER)
