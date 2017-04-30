import win32service
import win32serviceutil  
import win32event  
import servicemanager 
import threading
from winspotserver import __main__ as winspotserver

class PySvc(win32serviceutil.ServiceFramework):
    # you can NET START/STOP the service by the following name
    _svc_name_ = "Spotify API"
    # this text shows up as the service name in the Service
    # Control Manager (SCM)
    _svc_display_name_ = "Spotify REST API "
    # this text shows up as the description in the SCM
    _svc_description_ = "control the local spotify client via REST calls"
    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        # create an event to listen for stop requests on
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
    # core logic of the service
    def SvcDoRun(self):
        stop_flag = None
        self.server_thread = threading.Thread(target=winspotserver.run_server)
        while stop_flag != win32event.WAIT_OBJECT_0:
            if not self.server_thread.is_alive():
                self.server_thread = threading.Thread(target=winspotserver.run_server)
                self.server_thread.daemon = True
                self.server_thread.start()
            self.server_thread.join(1)
            stop_flag = win32event.WaitForSingleObject(self.hWaitStop, 1000)
    def SvcStop(self): 
        # tell the SCM we're shutting down
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        # fire the stop event
        win32event.SetEvent(self.hWaitStop)
if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(PySvc)


    