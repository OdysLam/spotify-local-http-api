### Installation:

1. Download the master branch, install [flask](http://flask.pocoo.org/docs/0.12/installation/)
2. Install this library
	
	`~& cd path/to/spotify-local-http-api-master`
	
	`~& sudo pip2 install` 
	#make sure that you are installing for python2
	
3. Run the flask server:
	
	`~$ python spotloc`
	
The script uses the flask dev http server. It's not meant for production as it can only serve 1 request/time, but for the needs of our little interface, is more that enough. There is no need to install and  configure extra server and wsgi.
	


### Usage
	
`http://ip.of.the.client.machine:PORT/COMMAND`

**PORT:** You can set it in the __main__.py script, defaults to 5000.

**COMMAND:**

* /play/*spotify uri*  
*  /pause
*  /unpause
*  /status (returns json data(playing:True/False,track-name,track-uri
