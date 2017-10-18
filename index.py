# encoding: utf-8
from weibo import APIClient
import webbrowser

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

APP_KEY = '1165200782'
APP_SECRET = '5c57f343fb4c540e2a86ae1d28fbed2b'
CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
url = client.get_authorize_url()
webbrowser.open_new(url)

print 'input your code , and enter:'

code = raw_input()
r = client.request_access_token(code)
access_token = r.access_token
expires_in = r.expires_in
client.set_access_token(access_token, expires_in)

result = client.comments.show.get(id = 4160547165300149,count = 200,page = 1)

for st in result.comments:
	text = st.text