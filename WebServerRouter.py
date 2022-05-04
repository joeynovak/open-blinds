import WebServerResponse

class WebServerRouter:
    def getResponse(self, request):
        response = WebServerResponse.WebServerResponse()
        path = request.getRequestedPath()
        
        if path == "/":
            f = open('webroot/index.html')
            response.setResponseBody(str(f.read(), 'utf8'))
            f.close()
        elif self.fileExists('webroot' + path):
            f = open('webroot' + path)
            response.setResponseBody(str(f.read(), 'utf8'))
            f.close()
        elif self.controllerExists(path):
            path = path.replace("-", "_")
            methodName = 'index'
            pathParts = path.split('/')            
            controllerName = pathParts[1]
            if len(pathParts) > 2:
                methodName = pathParts[2]
                
            try:
                webrootModule = __import__('webroot.' + controllerName)
                importedModule = getattr(webrootModule, controllerName)
                controllerClass = getattr(importedModule, controllerName)            
                controller = controllerClass(response)
                method = getattr(controller, methodName)
                result = method()                    
            except Exception as e:                
                response.setResponseBody(str(e))
                response.setResponseCode(500)
                raise e
        else:
            f = open('webroot/404.html')
            response.setResponseBody(str(f.read(), 'utf8'))
            response.setResponseCode(404)
            f.close()
        return response
    
    def fileExists(self, path):
        try:
            f = open(path)
            f.close()
            return True
        except:
            return False
        
    def controllerExists(self, path):
        path = path.replace("-", "_")
        pathParts = path.split('/')
        if len(pathParts) > 1:
            controller = pathParts[1]            
            if self.fileExists('webroot/' + controller + '.py'):
                return True                        
        return False
