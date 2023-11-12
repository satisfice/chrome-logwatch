# chrome-logwatch

This is a python script that monitors the Chrome debug log and plays audio when certain things appear in it.

# installation

1. Assuming you have Python installed:

`pip install -r requirements.txt`

2. Then edit chrome-logwatch-config.json to monitor the sites you want and to match the patterns you want.

The site list and match strings are interpreted as regexes.

The "say" string is what the voice will say through your speakers.

3. Edit the script to include the correct filename for the Chrome debug log. Note that you have to specify on the Chrome command-line that you want it to keep a log. Otherwise, there won't be one.
   
