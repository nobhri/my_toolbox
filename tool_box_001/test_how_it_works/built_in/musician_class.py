class musician_class_sub:
    def __init__(self, name, instrument,genre):
        self.name = name
        self.instrument = instrument
        self.genre = genre

    def learn_their_music(self):
        return f'It is not easy to play the {self.instrument} like {self.name}.'
Jimi_Hendrix = musician_class_sub(name = 'Jimi Hendrix',instrument = 'guitar', genre = 'rock')
Miles_Davis = musician_class_sub(name = 'Miles Davis', instrument = 'trumpet', genre = 'jazz')

if __name__ == '__main__':


    
    print(Jimi_Hendrix.name)
    print(Miles_Davis.instrument)
    print(Jimi_Hendrix.learn_their_music())