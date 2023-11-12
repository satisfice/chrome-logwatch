# chrome-logwatch

This is a python script that monitors the Chrome debug log and plays audio when certain things appear in it.

# installation

Assuming you have Python installed:

`pip install -r requirements.txt`

Then edit chrome-logwatch-config.json to monitor the sites you want and to match the patterns you want.

The site list and match strings are interpreted as regexes.

The "say" string is what the voice will say through your speakers.
