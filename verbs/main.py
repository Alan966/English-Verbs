import random
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from handlers.Errors import InvalidVerbFormError, QuizGameError

@dataclass
class Verb:
    present: str
    past: str
    past_participle: str
class VerbQuizGame:
    def __init__(self, verbs: List[Dict[str, str]]):
        self.verbs = [Verb(**verb) for verb in verbs]
        self.current_score = 0
        self.max_attempts = 3

    def get_random_verb(self, verb: Verb) -> Tuple[str, int]:
        """Returns a random verb form and its corresponding index."""
        try:
            random_number = random.randint(0, 2)
            verb_forms = {
                0: verb.present,
                1: verb.past,
                2: verb.past_participle
            }
            return verb_forms[random_number], random_number
        except KeyError as e:
            raise InvalidVerbFormError(f"Invalid verb form index: {e}")

    def get_user_input(self, prompt: str, attempts: int = 3) -> Optional[str]:
        """Get user input with retry logic and validation."""
        while attempts > 0:
            try:
                user_input = input(prompt).strip().lower()
                if not user_input:
                    print("Input cannot be empty. Please try again.")
                    attempts -= 1
                    continue
                if any(char.isdigit() for char in user_input):
                    print("Input cannot contain numbers. Please try again.")
                    attempts -= 1
                    continue
                return user_input
            except EOFError:
                print("\nInput terminated. Please try again.")
            except KeyboardInterrupt:
                print("\nGame interrupted by user.")
                return None
        return None

    def verify_answer(self, expected: str, actual: str) -> bool:
        """Verify if the provided answer matches the expected one."""
        return expected.lower() == actual.lower()

    def handle_answer(self, is_correct: bool) -> bool:
        """Handle the result of an answer and return whether to continue."""
        if is_correct:
            print("✓ Correct!")
            self.current_score += 1
            return True
        print("✗ Incorrect!")
        return False

    def ask_verb_forms(self, verb: Verb, form_index: int) -> bool:
        """Ask for different verb forms based on the given form."""
        prompts = {
            0: [
                ("past", lambda v: v.past),
                ("past participle", lambda v: v.past_participle)
            ],
            1: [
                ("present", lambda v: v.present),
                ("past participle", lambda v: v.past_participle)
            ],
            2: [
                ("present", lambda v: v.present),
                ("past", lambda v: v.past)
            ]
        }

        try:
            for form_name, form_getter in prompts[form_index]:
                prompt = f"What's the {form_name} form of the verb? "
                answer = self.get_user_input(prompt, self.max_attempts)
                if answer is None:
                    raise QuizGameError("Maximum attempts reached or game interrupted")
                if not self.handle_answer(
                    self.verify_answer(form_getter(verb), answer)
                ):
                    return False
            return True
        except KeyError:
            raise InvalidVerbFormError(f"Invalid form index: {form_index}")

    def shortRandomVerb(self):
        length = len(self.verbs)
        random_verbs = []
        for _ in range(0, length):
            random_verbs.append(random.choice(self.verbs))
        return random_verbs
    def run(self):
        """Run the quiz game."""
        print("\n=== Welcome to the Verb Quiz Game! ===\n")
        for verb in self.shortRandomVerb():
                verb_form, form_index = self.get_random_verb(verb)
                print(f"\nRandom verb form: {verb_form}")
                if not self.ask_verb_forms(verb, form_index):
                    print(f"\nGame Over! Final score: {self.current_score}")
                    return

        print(f"\nCongratulations! You completed the quiz! Score: {self.current_score}")
def start():
    verbs = [
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
    game = VerbQuizGame(verbs)
    game.run()

if __name__ == "__main__":
    start()