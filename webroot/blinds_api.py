import Blinds

class blinds_api:
    def __init__(self, response):
        self.response = response;
        
    def openABit(self):
        self.response.setResponseBody("Opening")
        Blinds.Blinds.blindsInstance.openABit()
        
    def closeABit(self):
        self.response.setResponseBody("Closing")
        Blinds.Blinds.blindsInstance.closeABit()
        
    def open(self):
        self.response.setResponseBody("Opening")
        Blinds.Blinds.blindsInstance.open()
        
    def close(self):
        self.response.setResponseBody("Closing")
        Blinds.Blinds.blindsInstance.close()
        
    def setOpenPosition(self):
        self.response.setResponseBody("Closing")
        Blinds.Blinds.blindsInstance.setOpenPosition()
        
    def setClosedPosition(self):
        self.response.setResponseBody("Closing")
        Blinds.Blinds.blindsInstance.setClosedPosition()