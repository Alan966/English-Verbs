import verbs.main as verbs
import user.main as user
def main():
    try:
        user.main()
        verbs.start()
    except Exception as e:
        print(f"Error creating user: {e}")
        return
    else:
        print("You don't have enough money to play this game")

if __name__ == "__main__":
    main()