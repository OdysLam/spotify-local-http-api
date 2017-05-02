## Installation:

The installation is simple enough. We need to install a couple of libraries and then configure the service.

1. Install flask by running `pip install flask` #make sure it's pip for python 2

2. Install the right version of [Python For Windows Extension](https://sourceforge.net/projects/pywin32/). These libraries are needed in order to write the windows service in python.

3. Install **winspoteserver**. Clone this repository, cd into the directory of setup.py and run 
`pip install .`

4. Install the windows service. In the directory of SpotSvc.py run `python SpotSvc.py install`. You are advised to inspect the code of the service. You shouldn't install services from untrusted sources *without* vetting the code.

5. Configure the service 'Spotify REST API` to run on startup. Visit [here](https://technet.microsoft.com/en-us/library/cc755249(v=ws.11).aspx) for more information.

6. Allow the same service to communicate through the firewall. Visit [here](https://technet.microsoft.com/en-us/library/cc719865(v=ws.10).aspx) for more information.

7. Reboot
