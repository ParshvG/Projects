class animal:
    def __init__(self, leg, tail, sound):
        self.leg = leg
        self.tail = tail
        self.sound = sound

    def speak(self):
        print("animal lanuage ", self.sound)

class humans:
    def __init__(self, age, gender, lanuage):
        self.age = age
        self.gender = gender
        self.lanuage = lanuage

    def speak(self):
        print("human lanuage ", self.lanuage)

value = animal("4", "1", "bow-bow")
value1 = humans("18", "male", "gujarati")
value.speak()
value1.speak()