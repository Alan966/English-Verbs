from dataclasses import dataclass
from handlers.Errors import BankAccountError
@dataclass
class IUser:
    name: str
    age: int
    bank_account: float
    favorite_artist: str
class User (IUser):
    def __init__(self, name: str, age:int, bank_account: float, favorite_artist: str):
        self.name = name
        self.age = age
        self.bank_account = bank_account
        self.favorite_artist = favorite_artist
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def is_old_enough(self):
        return self.age >= 18
    def get_bank_account(self):
        return self.bank_account
    def get_favorite_artist(self):
        return self.favorite_artist
    def verify_favorite_artist(self):
            if(self.favorite_artist.startswith("DRAKE")):
                self.favorite_artist = "DRAKE"
            elif(self.favorite_artist.startswith("PARTYNEXTDOOR")):
                self.favorite_artist = "PARTYNEXTDOOR"
            elif(self.favorite_artist.startswith("TYLOR THE CREATOR")):
                self.favorite_artist = "TYLOR THE CREATOR"
            else:
                self.favorite_artist = None
    def get_discount_by_artist(self):
        match self.favorite_artist:
            case "DRAKE":
                return 0.25
            case "PARTYNEXTDOOR":
                return 0.1
            case "TYLOR THE CREATOR":
                return 0.05
            case _:
                raise Exception("Artist not found")
    def verify_bank_account(self):
        if(self.bank_account < 100):
            print(self.bank_account)
            print("You don't have enough money to play this game")
            raise BankAccountError("You balance is : " + str(self.bank_account))
        else:
            print("You have enough money to play this game")

    def could_play_game(self):
        self.verify_favorite_artist()
        if self.favorite_artist == None:
            return self.verify_bank_account()
        else:
             if(self.bank_account >= 100 * (1 - self.get_discount_by_artist())):
                 raise Exception("You don't have enough money to play this game")
def get_name():
    name = input("What's your name? ")
    return name.strip().title()
def get_age():
    age = input("What's your age? ")
    return int(age)
def get_bank_account():
    bank_account = input("How much money do you have in your bank account? ")
    return round(float(bank_account), 2)
def get_favorite_artist():
    favorite_artist = input("Who is your favorite Artist? ")
    return favorite_artist.strip().upper()

def main():
    print("We'll start this game")
    #Ask the user their age
    name = get_name()
    age = get_age()
    bank_account = get_bank_account()
    favorite_artis = get_favorite_artist()
    user = User(name, age, bank_account, favorite_artis)
    user.could_play_game()
