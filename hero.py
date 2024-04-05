class SuperHero:

    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def display_name(self):
        print("Hero's name:", self.name)

    def double_health_points(self):
        self.health_points *= 2

    def __str__(self):
        return f"Nickname: {self.nickname}, Superpower: {self.superpower}, Health Points: {self.health_points}"

    def __len__(self):
        return len(self.catchphrase)

hero = SuperHero(name='Bruce Wayne', nickname='Batman', superpower='Rich', health_points=100, catchphrase='I am Batman')

hero.display_name()
hero.double_health_points()
print(hero)
print("Length of catchphrase:", len(hero))
