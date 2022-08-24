class Team:
    def __init__(self, name, arc):
        self.name = name
        self.arc = arc
        self.avg = 0
        self.opps = 0
        
    def set_avg(self, avg):
        self.avg = avg
        
    def set_opps(self, opps):
        self.opps = opps