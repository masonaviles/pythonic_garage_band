class Band:
    booked = False
    instances = []

    def __init__(self, name, members, **kwargs):
        # which is a string.
        self.name = name
        # which is a list of instances that inherit from Musician
        self.members = members
        self.instances.append(self)
        for key, value in kwargs.items():
            setattr(self, key, value)
    def __str__(self):
        return f"We are {self.name}."

    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())
        return tuple(solos)
    @classmethod
    def to_list(cls):
        return cls.instances
    

class Musician:
    def __init__(self, name, **kwargs):
        self.name = name
        for key, value in kwargs.items():
            setattr(self, key, value)
    def __repr__(self):
        return f'{self.__class__.__name__} instance. Name = {self.name}'
    def __str__(self):
        return f'My name is {self.name} and I play {self.get_instrument()}'


class Guitarist(Musician):
    playing_solo = False

    def __init__(self):
        self.guitarists = []
    def __iter__(self):
        yield from self.guitarists
    def add_guitarist(self, guitarist):
        self.guitarists.append(guitarist)
    
    def get_instrument(self):
        return 'guitar'
    def play_solo(self):
        self.playing_solo = True
        return 'face melting guitar solo'


class Bassist(Musician):
    playing_solo = False

    def __init__(self):
        self.bassists = []
    def __iter__(self):
        yield from self.bassists
    def add_bassist(self, bassist):
        self.bassists.append(bassist)

    def get_instrument(self):
        return 'bass'
    def play_solo(self):
        self.playing_solo = True
        return 'bom bom buh bom'


class Drummer(Musician):
    playing_solo = False

    def __init__(self):
        self.drummers = []
    def __iter__(self):
        yield from self.drummers
    def add_drummer(self, drummer):
        self.drummers.append(drummer)

    def get_instrument(self):
        return 'drums'
    def play_solo(self):
        self.playing_solo = True
        return 'rattle boom crash'