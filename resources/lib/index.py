#
#    AFL Video XBMC Plugin
#    Copyright (C) 2012 Andy Botting
#
#    AFL Video is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    AFL Video is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with AFL Video.  If not, see <http://www.gnu.org/licenses/>.
#

# main imports
import sys, os, re, urllib2, urllib
import config
import utils

try:
	import xbmc, xbmcgui, xbmcplugin, xbmcaddon
except ImportError:
	pass 

def make_list():

	try:
		items = []

		__addon__ = xbmcaddon.Addon()
		favourite_team =  __addon__.getSetting('TEAM')

        # Disabled until moved to new API
		#if favourite_team > 0:
		#	for team in config.TEAMS:
		#		if favourite_team == team['id']:
		#			items.append({'name': team['name'], 'channel': team['channel']})

		categories = config.CATEGORIES

		# enumerate through the list of categories and add the item to the media list
		for i in items:
			url = "%s?channel=%s" % (sys.argv[0], i['channel'])
			listitem = xbmcgui.ListItem(i['name'])

			# add the item to the media list
			ok = xbmcplugin.addDirectoryItem(
						handle=int(sys.argv[1]), 
						url=url, 
						listitem=listitem, 
						isFolder=True, 
					)

		for category in categories:
			url = "%s?category=%s" % (sys.argv[0], category)
			listitem = xbmcgui.ListItem(category)

			# add the item to the media list
			ok = xbmcplugin.addDirectoryItem(
						handle=int(sys.argv[1]), 
						url=url, 
						listitem=listitem, 
						isFolder=True, 
						totalItems=len(config.CATEGORIES)
					)

		xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=ok)
	except:
		utils.handle_error('Unable build video category list')
