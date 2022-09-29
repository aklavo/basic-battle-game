class Bender:
    def __init__(self,name,health,attack,speed,element):
        self.name = name
        self.health = health
        self.attack = attack
        self.speed = speed
        self.element = element

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    def get_speed(self):
        return self.speed

    def get_element(self):
        return self.element

    def __str__(self):
        return str(self.name)