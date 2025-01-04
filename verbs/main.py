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
def get_past_way():
    return input("What's the past way of the verb?")
def verify_past_way(verb, past):
    return past == verb["past"]
def get_past_participle_way():
    return input("What's the past participle of the verb?")
def verify_past_participle_way(verb, past_participle):
    return past_participle == verb["past_participle"]
def get_present_way():
    return input("What's the present way of the verb?")
def verify_present_way(verb, present):
    return present == verb["present"]
def correct():
    print("Correct")
def incorrect():
    print("Incorrect")
def ask_past_and_past_participle(verb):
    if verify_past_way(verb, get_past_way()):
        correct()
    else:
        incorrect()
    if verify_past_participle_way(verb, get_past_participle_way()):
        correct()
    else:
        incorrect()
def ask_present_and_past_participle(verb):
    if verify_present_way(verb, get_present_way()):
        correct()
    else:
        incorrect()
    if verify_past_participle_way(verb, get_past_participle_way()):
        correct()
    else:
        incorrect()
def ask_present_and_past_simple(verb):
    if verify_present_way(verb, get_present_way()):
        correct()
    else:
        incorrect()
    if verify_past_way(verb, get_past_way()):
        correct()
    else:
        incorrect()
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