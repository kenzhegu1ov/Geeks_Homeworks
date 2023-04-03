import random
from random import choice, randint
from enum import Enum


class SuperAbility(Enum):
    CRITICAL_DAMAGE = 1
    HEAL = 2
    BOOST = 3
    SAVE_DAMAGE_AND_REVERT = 4


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        hero = random.choice(heroes)
        self.__defence = hero.super_ability

    def hit(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                hero.health -= self.damage

    def __str__(self):
        return f'BOSS ' + super().__str__() + f' defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, super_ability):
        super().__init__(name, health, damage)
        self.__super_ability = super_ability

    @property
    def super_ability(self):
        return self.__super_ability

    def hit(self, boss):
        if self.health > 0 and boss.health > 0:
            boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        coeff = random.randint(2, 5)
        boss.health -= self.damage * coeff
        print(f'Warrior hits critically {self.damage * coeff}')


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.BOOST)

    def apply_super_power(self, boss, heroes):
        pass


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, SuperAbility.HEAL)
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and hero != self:
                hero.health += self.__heal_points


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)
        self.__saved_damage = 0

    @property
    def saved_damage(self):
        return self.__saved_damage

    @saved_damage.setter
    def saved_damage(self, value):
        self.__saved_damage = value

    def apply_super_power(self, boss, heroes):
        pass


class Golem(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)


    def apply_super_ability(self, boss, heroes):
        for hero in heroes:
            hero.health += boss.damage/5
            Golem.health -= boss.damage/5


class TrickyBastard(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)


    def apply_super_ability(self, boss, heroes):
        from random import randint
        if 4 < randint(1,5):
            boss.damage = 0
            TrickyBastard.damage = 0


class Deku(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.CRITICAL_DAMAGE)


    def apply_super_ability(self, boss, heroes):
        if 2 < randint(1, 2):
            if 2 < randint(1, 2):
                Deku.damage *= 1.2
            if 2 < randint(1, 2):
                Deku.damage *= 1.5
            if 2 < randint(1, 2):
                Deku.damage *= 2


class AntMan(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)


    def apply_super_ability(self, boss, heroes):
        if round_number == 2 or 4 or 6 or 8 or 10 or 12 or 14 or 16 or 18 or 20:
            if 3 < randint(1, 5):
                AntMan.damage *= 2
                AntMan.health *= 2
            if 3 > randint(1, 5):
                AntMan.damage /= 2
                AntMan.health /= 2


class Spitfire(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.CRITICAL_DAMAGE)


    def apply_super_ability(self, boss, heroes):
        for hero in heroes:
            if hero.health >= 0:
                boss.damage -= 80



class Witcher(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.HEAL)


    def apply_super_ability(self, boss, heroes):
        for hero in heroes:
            if hero.health == 0:
                hero.health += self.health
                self.health = 0
                print(f'Witcher gave {self.health} to {hero}')
round_number = 0


def print_statistics(boss, heroes):
    print('ROUND ' + str(round_number) + ' ----------------')
    print(boss)
    for hero in heroes:
        print(hero)


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
    return all_heroes_dead


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.hit(heroes)
    for hero in heroes:
        if boss.defence != hero.super_ability and hero.health > 0:
            if hero.super_ability != SuperAbility.CRITICAL_DAMAGE:
                hero.hit(boss)
            hero.apply_super_power(boss, heroes)
    print_statistics(boss, heroes)


def start_game():
    boss = Boss('Pudge', 800, 50)
    warrior = Warrior('Ahiles', 280, 10)
    doc = Medic('Invoker', 250, 5, 15)
    magic = Magic('Lolita', 290, 15)
    berserk = Berserk('Thor', 270, 10)
    assistant = Medic('Rafael', 300, 5, 5)
    golem = Golem('Iron', 600, 5)
    tricky = TrickyBastard('Mars', 250, 15)
    deku = Deku('Midoriya', 250, 15)
    ant = AntMan('Hank', 270, 20)
    spit = Spitfire('Speedy', 260, 10)
    heroes_list = [warrior, doc, magic, berserk, assistant, golem, tricky, deku, ant, spit,]

    print_statistics(boss, heroes_list)
    while not is_game_finished(boss, heroes_list):
        play_round(boss, heroes_list)


start_game()
