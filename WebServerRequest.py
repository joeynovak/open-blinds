import gc

class WebServerRequest:
    def __init__(self):
        self.method = "";
        self.url = "";
        self.path = "";
        self.queryString = "";
        self.haveFirstLine = False        
        
    def appendRequestData(self, data):
        if self.haveFirstLine != True:
            data = str(data, "utf8").split(" ")
            self.method = data[0]
            self.url = data[1]
            data = self.url.split('?')
            self.path = data[0]
            if len(data) > 1:
                self.queryString = data[1]
            self.haveFirstLine = True
            print(self.method)
            print(self.path)
        print(gc.mem_free())
        
    def getRequestedPath(self):
        return self.path    
    
    def endReached(self):
        #All we need is the first line right now, so that's all we get...
        return self.haveFirstLine