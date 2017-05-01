## Spotify Local Api Server

This server gives the possibility to control the local spotify client via REST calls. 

Using Flask you run a local server which listens for commands and relays them to the local http server that is run behind every spotify client.

The extra flask server is necessary as the spotify server can only be accessed from the device that is running the client.

Usable only with python 2 for the moment!

### VERSIONS

There are currently two versions of the server.

1. **Spotloc:** The server is simply a python library and you can run it by simply typing
`$python spotloc`. Great for UNIX systems since you can automate it via a simple *cron-job* or by integrating in another python script.

2. **Winspotserver** The server is wrapped in a windows service. Once installed, it will run silently at every startup and the server will be always on.