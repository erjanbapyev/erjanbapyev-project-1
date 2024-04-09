# class SuperHero:
#
#     people = 'people'
#
#     def __init__(self, name, nickname, superpower, health_points, catchphrase):
#         self.name = name
#         self.nickname = nickname
#         self.superpower = superpower
#         self.health_points = health_points
#         self.catchphrase = catchphrase
#
#     def display_name(self):
#         print("Hero's name:", self.name)
#
#     def double_health_points(self):
#         self.health_points *= 2
#
#     def __str__(self):
#         return f"Nickname: {self.nickname}, Superpower: {self.superpower}, Health Points: {self.health_points}"
#
#     def __len__(self):
#         return len(self.catchphrase)
#
# hero = SuperHero(name='Bruce Wayne', nickname='Batman', superpower='Rich', health_points=100, catchphrase='I am Batman')
#
# hero.display_name()
# hero.double_health_points()
# print(hero)
# print("Length of catchphrase:", len(hero))



class SuperHero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def increase_hp(self):
        self.hp = self.hp ** 2

    def fly(self):
        return False

    def true_phrase(self):
        return "True"


class AirHero(SuperHero):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp)
        self.damage = damage

    def increase_hp(self):
        super().increase_hp()
        self.fly = True

    def true_phrase(self):
        return super().true_phrase() + " in the air"


class EarthHero(SuperHero):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp)
        self.damage = damage

    def increase_hp(self):
        super().increase_hp()
        self.fly = True

    def true_phrase(self):
        return super().true_phrase() + " on the ground"


class Villain(EarthHero):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp, damage)
        self.people = "monster"

    def gen_x(self):
        pass

    def crit(self):
        return self.damage ** 2


air_hero = AirHero("Airman", 100, 10)
earth_hero = EarthHero("Earthman", 150, 20)
villain = Villain("Villain", 200, 30)

air_hero.increase_hp()
print(air_hero.hp)
print(air_hero.fly)
print(air_hero.true_phrase())

earth_hero.increase_hp()
print(earth_hero.hp)
print(earth_hero.fly)
print(earth_hero.true_phrase())

print(villain.people)
print(villain.crit())

