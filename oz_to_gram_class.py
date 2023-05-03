class OzToGram:
    def __init__(self,type):
        if type == 1:
            self.constant = 31
        else:
            self.constant = 28
    def get_data(self,oz):
        return oz*self.constant
ozToGram = OzToGram(1)
ozToGram.constant = 50
print(ozToGram.get_data(1))