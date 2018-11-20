
## the band has a name too
#%%
class Member:

    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument
        
    def play(self):
        if self.instrument == "guitar":
            print("PIIIAAUUU PIAAUUU")
        elif self.instrument == "bass":
            print("DONG DONG")
        elif self.instrument == "drums":
            print("dum tsss dum tss")
        else:
            print("LA LA AL AL LA")
            
class RockBand:
    
    members = []
    
    def __init__(self, name):
        self.name = name
        
    def add_member(self, member):    
        self.members.append(member)
        
    def add_members_list(self, members_list):
        self.members += members_list

    def rehearse(self):        
        for member in self.members:
            member.play()
        
        
        
beatles = RockBand("Beatles")
members = [Member("Ringo", "drums")
    ,Member("Paul", "bass")
    ,Member("John", "sings")
    ,Member("George", "guitar")]
        
beatles.add_members_list(members)
        
        
        
        