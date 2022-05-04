class WebServerResponse:
    def __init__(self):
        self.responseCode = 200
        self.responseBody = ""
        self.responseType = "text/html"
        
    def setResponseCode(self, code):
        self.responseCode = code
        
    def setResponseBody(self, responseBody):
        self.responseBody = responseBody
        
    def setResposneType(self, responseType):
        self.responseType = responseType