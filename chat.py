#%%

class User:
    def __init__(self, name):
        self.name = name
        
    def join_room(self, room):
        room.accept(self)
        
    def send_message(self, message, room):
        room.broadcast(message)
    
    def receive_notification(self, message):
        print(self.name + " received: " + message)

class Room:   
    def __init__(self, name):
        self.name = name
        self.users = []
        
    def accept(self, user):
        self.users.append(user)
        
    def broadcast(self, message):
        for user in self.users:
            user.receive_notification(message)

        
room = Room("potato")

pepe = User("pepe")
anthony = User("anthony")
pepe.join_room(room)
anthony.join_room(room)

pepe.send_message("hello dolly", room)

















