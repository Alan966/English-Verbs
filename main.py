import verbs.main as verbs
def main():
    print("We'll start this game")
    name = get_name()
    #Ask the user their age
    age = get_age()
    if verify_age(age) == False:
        print("You're too young to play this game")
        return
    print("You're old enough to play this game")
    bank_account = get_bank_account()
    favorite_artis = get_favorite_artist()
    if could_play_game(favorite_artis, bank_account) == False:
        print("You don't have enough money to play this game")
        return
    print("You can play this game")
    verbs.start()

def get_name():
    name = input("What's your name? ")
    return name.strip().title()
def get_age():
    age = input("What's your age? ")
    return int(age)
def verify_age(age):
    return age >= 18
def get_bank_account():
    bank_account = input("How much money do you have in your bank account? ")
    return round(float(bank_account), 2)
def verify_bank_account(bank_account):
    return bank_account >= 100
def get_favorite_artist():
    favorite_artist = input("Who is your favorite Artist? ")
    return favorite_artist.strip().upper()
def verify_favorite_artist(artist: str):
    if(artist.startswith("DRAKE")):
        return "DRAKE"
    elif(artist.startswith("PARTYNEXTDOOR")):
        return "PARTYNEXTDOOR"
    elif(artist.startswith("TYLOR THE CREATOR")):
        return "TYLOR THE CREATOR"
def verify_discountCodes_by_artist(artsit: str):
    match artsit:
        case "DRAKE":
            return 0.25
        case "PARTYNEXTDOOR":
            return 0.1
        case "TYLOR THE CREATOR":
            return 0.05
        case _:
            return
def could_play_game(discount_code, bank_account):
    formmated_artist = verify_favorite_artist(discount_code)
    if formmated_artist == None:
      return verify_bank_account(bank_account)
    else:
      discount = verify_discountCodes_by_artist(formmated_artist) or 0
      return bank_account >= 100 * (1 - discount)

if __name__ == "__main__":
    main()