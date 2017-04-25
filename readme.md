## Spotify Local Api Server

This server gives the possibility to control the local spotify client via REST calls. 

Using Flask you run a local server which listens for commands and relays them to the local http server that is run behind every spotify client.

The extra flask server is necessary as the spotify server can only be accessed from the device that is running the client.

Usable only with python2 for the moment!

### Installation:
1)Download the master branch, install [flask](http://flask.pocoo.org/docs/0.12/installation/)

2)
	cd path/to/spotify-local-http-api-master
	sudo pip2 install .  
	#make sure that you are installing and using the script with python2
	
3) Run the flask server:
	python spotloc
	
The script uses the flask dev http server. It's not meant for production as it can only serve 1 request/time, but for the needs of our little interface, is more that enough. There is no need to install and  configure extra server and wsgi.
	


###Usage
	
http://ip.of.the.client.machine:PORT/COMMAND

**PORT:** You can set it in the __main__.py script, defaults to 5000.

**COMMAND:**

* /play/*spotify uri*  
*  /pause
*  /unpause
*  /status (returns json data(playing:True/False,track-name,track-uri
