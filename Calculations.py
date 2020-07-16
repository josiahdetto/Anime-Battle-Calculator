class Calculations:
    def __init__(self, state, data):
        self.data = data
        self.state = state
        """if state:
            pre_battle()
        else:
            during_battle()"""

    def character_role_score(self):
        role = self.data[0]
        if role == 1:
            return 10
        else if role == 2:
            return 5
        else:
            return 1
    def character_trained_score(self):
        trained = self.data[1]
        if trained == 1:
            return 10
        else:
            return 0
    def enemy_role_score(self):
        role = self.data[2]
        if role == 1:
            return 10
        else if role == 2:
            return 5
        else:
            return 1
    def calc_lost_score(times_lost):
        if times_lost <= 3:
            return 2 ** times_lost
        else:
            return 4 
    
    def character_lost_score(self):
        lost = self.data[3]
        if type(lost) is bool:
            return 0
        else:
            return calc_lost_score(lost)

    def protect_friends_score(self):
        protect = self.data[4]
        if protect:
            return 10
        else:
            return 0

    def calculate_pre_battle(self):
        char_role_weight = 0.3
        trained_weight = 0.2
        enemy_role_weight = 0.5
        lost_weight = 0.25
        protect_weight = 0.35

        char_role_score = self.character_role_score()
        trained_score = self.character_trained_score()
        enemy_role_score = self.enemy_role_score()
        lost_score = self.character_lost_score()
        protect_score = self.protect_friends_score()
        
        return ((char_role_weight * char_role_score) + (trained_weight *
                trained_score) + (enemy_role_weight * enemy_role_score) +
                (lost_weight * lost_score) + (protect_weight * protect_score)) /
                1.6
                
    def calculate_during_battle(self):
        pass
    
    def get_score(self):
        if self.state:
            return self.calculate_during_battle()
        else:
            return self.calculate_pre_battle()

    def get_verdict():
        score = self.get_score()

        if score >= 0.8:
            return True
        else:
            pass
    
        
    
            
