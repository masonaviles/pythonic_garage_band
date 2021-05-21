class Band:
    def __init__(self, name, members):
        # which is a string.
        self.name = name
        # which is a list of instances that inherit from Musician
        self.members = members
    
    def __str__(self):
        return f"We are {self.name}."

class Musician:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"My name is {self.name}."

class Guitarist:
    def __init__(self):
        self.guitarists = []
    
    def __iter__(self):
        yield from self.guitarists
    
    def add_guitarist(self, guitarist):
        self.guitarists.append(guitarist)

class Bassist:
    def __init__(self):
        self.bassists = []
    
    def __iter__(self):
        yield from self.bassists
    
    def add_bassist(self, bassist):
        self.bassists.append(bassist)

class Drummer:
    def __init__(self):
        self.drummers = []
    
    def __iter__(self):
        yield from self.drummers
    
    def add_drummer(self, drummer):
        self.drummers.append(drummer)