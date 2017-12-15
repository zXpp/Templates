from pprint import pprint
my_dict={
    "background": {
        "presistent": True,
        "scripts": ["js/background.js" ]
    },
    "browser_action": {
        "default_icon": "images/logo.png",
        "default_title": "Listen 1"
    },
    "description": "Listen 1 for all music",
    "icons": {
        "128": "images/logo.png",
        "16": "images/logo.png",
        "48": "images/logo.png"
    },
    "manifest_version": 2,
    "name": "Listen 1",
    "permissions": [ "notifications", "unlimitedStorage", "downloads", "storage", "contextMenus", "tabs", "*://music.163.com/*", "*://*.xiami.com/*", "*://*.qq.com/*", "webRequest", "webRequestBlocking"],
    "version": "1.0",
    "web_accessible_resources": [ "images/*" ]
}
pprint(my_dict) #perform well especially on dict type
print(my_dict)

"""
zzpp220@zzpp:~/Templates/tools$ python Goodpprint.py

use pprint:

{'background': {'presistent': True, 'scripts': ['js/background.js']},
 'browser_action': {'default_icon': 'images/logo.png',
                    'default_title': 'Listen 1'},
 'description': 'Listen 1 for all music',
 'icons': {'128': 'images/logo.png',
           '16': 'images/logo.png',
           '48': 'images/logo.png'},
 'manifest_version': 2,
 'name': 'Listen 1',
 'permissions': ['notifications',
                 'unlimitedStorage',
                 'downloads',
                 'storage',
                 'contextMenus',
                 'tabs',
                 '*://music.163.com/*',
                 '*://*.xiami.com/*',
                 '*://*.qq.com/*',
                 'webRequest',
                 'webRequestBlocking'],
 'version': '1.0',
 'web_accessible_resources': ['images/*']}

use print:

{'background': {'presistent': True, 'scripts': ['js/background.js']}, 'browser_action': {'default_icon': 'images/logo.png', 'default_title': 'Listen 1'}, 'description': 'Listen 1 for all music', 'icons': {'128': 'images/logo.png', '16': 'images/logo.png', '48': 'images/logo.png'}, 'manifest_version': 2, 'name': 'Listen 1', 'permissions': ['notifications', 'unlimitedStorage', 'downloads', 'storage', 'contextMenus', 'tabs', '*://music.163.com/*', '*://*.xiami.com/*', '*://*.qq.com/*', 'webRequest', 'webRequestBlocking'], 'version': '1.0', 'web_accessible_resources': ['images/*']}
zzpp220@zzpp:~/Templates/tools$ 




"""