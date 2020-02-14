class Band():
    members = []

    def __init__(self, name):
        self.name = name

    @staticmethod
    def moment_of_fame():
        return "Lets do this"

    def __repr__(self):
        return self.name

    @classmethod
    def play_solos(cls):
        for member in cls.members:
            print(f'{member} has an amazing {member.instrument} solo')

    @classmethod
    def create_from_data(cls, data):
        for musician in data:
            if musician['instrument'] == 'Guitar':
                cls.members.append(
                    Guitarist(musician['name'], musician['instrument']))

            elif musician['instrument'] == 'Bass':
                cls.members.append(
                    Bassist(musician['name'], musician['instrument']))

            elif musician['instrument'] == 'Drums':
                cls.members.append(
                    Drummer(musician['name'], musician['instrument']))

            elif musician['instrument'] == 'Vocals':
                cls.members.append(
                    Singer(musician['name'], musician['instrument']))

    @classmethod
    def to_list(cls):
        return cls.members


class Musician(Band):
    musician_list = []

    def __init__(self, name):
        super().__init__(self)
        self.name = name
        self.__class__.musician_list.append(self)

    @classmethod
    def get_members(cls):
        return cls.musician_list


class Guitarist(Musician):
    def __init__(self, name):
        self.name = name
        self.instrument = 'guitar'
        super().__init__(name)

    def play_solo(self):
        return 'Guitar noises'

    def get_instrument(self):
        return 'guitar'


class Bassist(Musician):
    def __init__(self, name):
        self.name = name
        self.instrument = 'bass'
        super().__init__(name)

    def play_solo(self):
        return 'Musician noises'

    def get_instrument(self):
        return 'Bass'


class Drummer(Musician):
    def __init__(self, name):
        self.name = name
        self.instrument = 'drums'
        super().__init__(name)

    def play_solo(self):
        return 'drum noises'

    def get_instrument(self):
        return 'drums'


class Singer(Musician):
    def __init__(self, name):
        self.name = name
        self.instrument = 'Singer'
        super().__init__(name)

    def play_solo(self):
        return 'song noises'

    def get_instrument(self):
        return 'Vocals'


data = [
    {'name': 'Thom York',
     'instrument': 'Vocals'
     },
    {'name': 'Colin Greenwood',
        'instrument': 'Bass'
     },
    {'name': 'Philip Selway',
        'instrument': 'Drums'
     },
    {'name': 'Jonny Greenwood',
     'instrument': 'Guitar'
     }
]

    




