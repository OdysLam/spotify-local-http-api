##Spotify  Local Api Server


This server gives the possibility to control the local spotify client via REST calls. Great when you can't control the device with spotify connect, as when using a script.

Using Flask you run a local server which listens for commands and then controls the spotify client via the local http server that is hidden behind every client.

The extra flask server is necessary as the spotify server can only be accessed from the devic that is running the client.

###Installation:
1)Download the master branch, install [flask](http://flask.pocoo.org/docs/0.12/installation/)

2)

	cd path/to/spotify-local-http-api-master
	sudo sudo pip2 install -e .
	
3) Deploy the flask server:

 Either using the built-in server (serves 1 request per time) as in [here](http://flask.pocoo.org/docs/0.12/patterns/packages/) .
Basically just cd in the directory of setup.py and run:
	
	export FLASK_APP=spot_server
	python2 -m flask run --host=0.0.0.0 
#make sure python2 is used
	

Or read [this](http://flask.pocoo.org/docs/0.12/deploying/#deployment) for deployment options with a proper server.



###Usage
	http://localhost:PORT/COMMAND
	
**PORT:** You can set it when running the server in which you use flask,
please read [here](http://flask.pocoo.org/docs/0.12/deploying/) for deployment options:

**COMMAND:**

* /play/*spotify uri*  
*  /pause
*  /unpause
*  /status (returns json data(playing:True/False,track-name,track-uri
