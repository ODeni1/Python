class Person:
    def __init__(self, name):
       self.name = name

    def talk(self):
        print(f'Hi, I am {self.name}')


class Girl(Person):
    def love_shopping(self):
        print('One thing about me is that I love shopping')


class Boy(Person):
    def love_sport(self):
        print('One thing about me is that i love to play tennis')


name1 = Boy('Caleb')
name1.talk()
name1.love_sport()

name2 = Girl('Ruth')
name2.talk()
name2.love_shopping()
