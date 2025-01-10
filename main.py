import verbs.main as verbs
import user.main as user
from handlers.Errors import InvalidVerbFormError, QuizGameError, BankAccountError
def main():
    try:
        user.main()
        verbs.start()
    except InvalidVerbFormError as e:
        print(f"Error in verb data: {e}")
    except QuizGameError as e:
        print(f"Game error: {e}")
    except BankAccountError as e:
        print(f"Bank account error: {e}")
    except Exception as e:
        print(f"Error creating user: {e}")
    finally:
            print("\nThanks for playing!")
if __name__ == "__main__":
    main()