class Player:
    def __init__(self, name):
       self.name = name
       self.kills = 0
    
    def add_kill(self):
        self.kills += 1
    
    def remove_kill(self):
         self.kills -= 1