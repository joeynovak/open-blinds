import ujson
import os

class Blinds:
    blindsInstance = 0
    
    def __init__(self, stepper, rotations_to_fully_operate):
        self.stepper = stepper
        self.rotations_to_fully_operate = rotations_to_fully_operate
        self.isOpen = False
        self.currentPosition = 0        
        self.loadSettings()
        Blinds.blindsInstance = self
        
    def setOpenPosition(self):
        self.settings['openPosition'] = self.currentPosition
    
    def setClosedPosition(self):
        self.settings['closedPosition'] = self.currentPosition
    
    def open(self):
        self.goto(self.settings['openPosition'])
        
    def close(self):
        self.goto(self.settings['closedPosition'])

    def openABit(self):
        self.rotate(90)
        
        
    def closeABit(self):
        self.rotate(-90)
        
    def loadSettings(self):
        try:
            with open('blindSettings.json', 'r') as fp:
                self.settings = ujson.load(fp)
        except:
            self.settings = {"openPosition": 0, "currentPosition": 90, "closedPosition": 100}
            
        self.currentPosition = self.settings['currentPosition']
    
    def saveSettings(self):
        self.settings['currentPosition'] = self.currentPosition
        try:
            os.remove('blindSettings.json')
        except:
            pass
            
        with open('blindSettings.json', 'w') as fp:
            ujson.dump(self.settings, fp)        
    
    def goto(self, position):
        change = position - self.currentPosition
        self.rotate(change)
        
    def rotate(self, degrees):
        self.currentPosition += degrees
        self.stepper.step(degrees)
        self.saveSettings()
        