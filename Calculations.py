class Calculations:
    def __init__(self, state, data):
        self.data = data
        if state:
            pre_battle()
        else:
            during_battle()

    def character_role(self):
        self.data[0] = 
