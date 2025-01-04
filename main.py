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
    discount_code = get_discountCode()
    if could_play_game(discount_code, bank_account) == False:
        print("You don't have enough money to play this game")
        return
    print("You can play this game")

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
def get_discountCode():
    discountCode = input("Do you have a first discount code? ")
    return discountCode
def verify_discountCode(discountCode):
    return discountCode == "DRAKE" or discountCode == "PARTYNEXTDOOR" or discountCode =="TYLOR,THECREATOR"
def verify_discountCodes_with_percentage(discountCode):
    match discountCode:
        case "DRAKE":
            return 0.25
        case "PARTYNEXTDOOR":
            return 0.1
        case "TYLOR,THECREATOR":
            return 0.05
        case _:
            return
def could_play_game(discount_code, bank_account):
    if verify_discountCode(discount_code) == False:
      return verify_bank_account(bank_account)
    else:
      discount = verify_discountCodes_with_percentage(discount_code) or 0
      return bank_account >= 100 * (1 - discount)

if __name__ == "__main__":
    main()