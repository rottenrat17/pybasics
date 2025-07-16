#stage 7
import random

class Character:
    def __init__(self,name, health, power):
        self._name = name
        self._health = health
        self._power = power
        self._alive = True


    def attack(self,other):
        pass

    def take_damage(self,amount):
        self._health -= amount
        if self._health <= 0:
            self._health = 0
            self._alive = False
            print(f"{self._name} has been defeated! ")

    def get_status(self):
        return f"Name: {self._name}, Health: {self._health}, Power: {self._power}"

    def is_alive(self):
        return self._alive


class Warrior(Character):
    def attack(self, other):
        print(f"{self._name} SLASHES {other._name} with a sword! ")
        other.take_damage(self._power)

class Wizard(Character):
    def attack(self,other):
        damage = int(self._power * 1.5)
        print(f"{self._name} casts FIREBALL on {other._name} ! ")
        other.take_damage(damage)

class Archer(Character):
    def attack(self,other):
        damage = int(self._power + 5)
        print(f"{self._name} shoots ARROWS at {other._name} ! ")
        other.take_damage(damage)

class Arena:
    def __init__(self,fighter1,fighter2):
        self._f1 = fighter1
        self._f2 = fighter2

    def fight(self):
        print("\n The Battle Begins!!\n")
        while self._f1.is_alive() and self._f2.is_alive():
            attacker = random.choice([self._f1, self._f2])
            defender = self._f1 if attacker == self._f2 else self._f2

            attacker.attack(defender)

            print(self._f1.get_status())
            print(self._f2.get_status())
            print("-" * 30)

        winner = self._f1 if self._f1.is_alive() else self._f2
        print(f"The winner is {winner._name}")


def main():
    while True:
        Ravi = Warrior("Ravii the Warrior", 100, 20)
        Harry = Wizard("Harry the Wizard", 75, 40)
        Maya = Archer("MAYA No maya", 80, 35)

        print("Choose your fighters: ")
        print("1. Ravi (Warrior)")
        print("2. Harry (Wizard)")
        print("3. Maya (Archer)")

        fighters = [Ravi, Harry, Maya]

        try:
            choice1 = int(input("Pick fighter 1 (1-3): "))
            choice2 = int(input("Pick fighter 2 (1-3): "))

            if choice1 == choice2:
                print("You cant choose the same fighter!")
                return

            f1 = fighters[choice1 - 1]
            f2 = fighters[choice2 - 1]

            arena = Arena(f1,f2)
            arena.fight()

        except ValueError:
            print("Something went wrong!Choose inbetween 1-3")
            continue

        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != "y":
            print("Thank you for playing!")
            break


if __name__ == "__main__":
    main()