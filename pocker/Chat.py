class Chat:
    
    
    
    listMsg = []
    
    def __init__(self):
        pass           
    
    colorList = [('red', '\033[0;31m'), 
                 ('green', '\033[0;32m'),
                 ('yellow', '\033[0;33m'),
                 ('blue', '\033[0;34m'),
                 ('purple', '\033[0;35m'),
                 ('cyan', '\033[0;36m')]
    
    def getColorTag(self, getColorName):
        tag = ''
        for (colorName, colorTag) in self.colorList:
            if colorName == getColorName:
                tag = colorTag
        return tag
    
    def addMessage(self, user, message, color):
        '\033[0m'
        self.listMsg.append((self.getColorTag(color) + user + '\033[0m',message))
                