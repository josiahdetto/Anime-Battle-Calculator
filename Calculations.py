class Calculations:
    
    max_total = 8.3
    
    def __init__(self, state, data):
        self.data = data
        self.state = state

    def character_role_score(self):
        role = self.data[0]
        return role
    def character_trained_score(self):
        trained = self.data[1]
        return trained
    def enemy_role_score(self):
        role = self.data[2]
        return role
    def calc_lost_score(self):
        times_lost = self.data[4]
        if times_lost <= 3:
            return 2 ** times_lost
        else:
            return 4
    def calc_timeskip_score(self):
        battles_fought = self.data[6]
        if battles_fought == 0:
            return 5
        else:
            return 1
    
    def character_lost_score(self):
        lost = self.data[3]
        if lost == 0:
            return 0
        else:
            return self.calc_lost_score()

    def post_timeskip_score(self):
        timeskip = self.data[5]
        if timeskip == 0:
            return 0
        else:
            return self.calc_timeskip_score()

    def protect_friends_score(self):
        protect = self.data[7]
        return protect

    def calculate_pre_battle(self):
        char_role_weight = 0.5
        trained_weight = 0.3
        enemy_role_weight = 0.7 
        lost_weight = 0.2
        timeskip_weight = 0.5
        protect_weight = 0.3

        char_role_score = self.character_role_score()
        trained_score = self.character_trained_score()
        enemy_role_score = self.enemy_role_score()
        lost_score = self.character_lost_score()
        timeskip_score = self.post_timeskip_score()
        protect_score = self.protect_friends_score()
        
        total = ((char_role_weight * char_role_score) + (trained_weight *
                trained_score) + (enemy_role_weight * enemy_role_score) +
                (lost_weight * lost_score) + (protect_weight * protect_score))
        return total/Calculations.max_total
                
    def calculate_during_battle(self):
        pass
    
    def get_score(self):
        if self.state: 
            return self.calculate_during_battle()
        else:
            return self.calculate_pre_battle()

    def get_verdict(self):
        score = self.get_score()
        print(score)

        if round(score, 2) >= 0.5:
            return True
        else:
            return False
