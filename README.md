# username_checker
Check usernames availability on various websites using Selenium and Python.

Example website provided is "https://anilist.co/".

# Requirements
1. https://github.com/mozilla/geckodriver/releases

2. Firefox installed.

# Setup
Put all files into one folder.

Put geckodriver into the same folder.

Insert wanted usernames into usernames.txt.

py run.py

# Optional changes
Change line 6's "firefox_binary" to your firefox installation location.

Change line 7's "timeout" to your wanted waiting time (in seconds) before going to the next user.

Change line 9's "base_url" to your wanted website.

Change line 10's "url_check" to the format of a registered user.

Change line 11's "url_free" to the free username redirect.
