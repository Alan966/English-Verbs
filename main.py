import verbs.main as verbs
import user.main as user
def main():
    print("We'll start this game")
    #Ask the user their age
    name = get_name()
    age = get_age()
    bank_account = get_bank_account()
    favorite_artis = get_favorite_artist()
    try:
        user = user.User(name, age, bank_account, favorite_artis)
    except Exception as e:
        print(f"Error creating user: {e}")
        return
    if user.could_play_game():
        verbs.start()
    else:
        print("You don't have enough money to play this game")

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
if __name__ == "__main__":
    main()