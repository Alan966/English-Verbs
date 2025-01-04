import random
verbs= [
    {
        "present": "be",
        "past": "was",
        "past_participle": "been"
    },
    {
        "present": "have",
        "past": "had",
        "past_participle": "had"
    }
]
def get_random_verb(verb):
    random_number = random.randint(0, 2)
    if random_number == 0:
        return [verb["present"], random_number]
    elif random_number == 1:
        return [verb["past"], random_number]
    else:
        return[ verb["past_participle"], random_number]
def ask_past_and_past_participle(verb):
    past = input("What's the past way of the verb?")
    if past == verb["past"]:
        print("Correct")
    else:
        print("Incorrect")
    past_participle = input("What's the past participle of the verb?")
    if past_participle == verb["past_participle"]:
        print("Correct")
    else:
        print("Incorrect")
def ask_present_and_past_participle(verb):
    present = input("What's the present way of the verb?")
    if present == verb["present"]:
        print("Correct")
    else:
        print("Incorrect")
    past_participle = input("What's the past participle of the verb?")
    if past_participle == verb["past_participle"]:
        print("Correct")
    else:
        print("Incorrect")
def ask_present_and_past_simple(verb):
    present = input("What's the present way of the verb?")
    if present == verb["present"]:
        print("Correct")
    else:
        print("Incorrect")
    past = input("What's the past way of the verb?")
    if past == verb["past"]:
        print("Correct")
    else:
        print("Incorrect")
def ask_default_forms(verb, random_number):
    match random_number:
        case 0:
            ask_past_and_past_participle(verb)
        case 1:
            ask_present_and_past_participle(verb)
        case 2:
            ask_present_and_past_simple(verb)
def main():
    print("We'll start this game")
    length = verbs.__len__()
    for i in range(length):
        verb = verbs[i]
        [verb_to_show, random_number] = get_random_verb(verb)
        print(f"Random verb: {verb_to_show}")
        ask_default_forms(verb, random_number)

if __name__ == "__main__":
    main()