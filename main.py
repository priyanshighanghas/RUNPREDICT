"""RUNPREDICT - CSE1021 console practice project."""

from questions import get_question
from validation import valid_menu_choice, same_output
from progress import new_progress, record_answer, show_result


def show_title():
    print("\n========================================")
    print(" RUNPREDICT - CSE1021 PRACTICE")
    print("========================================")
    print("Read a small Python program and predict its output.")


def choose_topic():
    print("\n1. Data, expressions and statements")
    print("2. Control flow")
    print("3. Fundamental algorithms")
    print("4. Lists, tuples and dictionaries")
    print("5. Return to main menu")
    choice = input("Choose a topic: ")

    if not valid_menu_choice(choice, 1, 5):
        print("Please enter a number from 1 to 5.")
        return 0
    return int(choice)


def play_round(progress):
    level = choose_topic()

    if level == 0 or level == 5:
        return False

    code, answer, hint, topic = get_question(level)

    print("\nTopic:", topic)
    print("\nPredict the output:")
    print("----------------------------------------")
    print(code)
    print("----------------------------------------")

    prediction = input("Your prediction (or H for a hint): ")

    if prediction.strip().upper() == "H":
        print("Hint:", hint)
        prediction = input("Your prediction: ")

    correct = same_output(prediction, answer)
    record_answer(progress, correct)

    if correct:
        print("Correct. Good tracing.")
    else:
        print("Not quite. The actual output is:")
        print(answer)

    return True


def main():
    progress = new_progress()

    while True:
        show_title()
        print("\n1. Start practice")
        print("2. Show session result")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            play_round(progress)
            input("\nPress Enter to continue...")
        elif choice == "2":
            show_result(progress)
            input("\nPress Enter to continue...")
        elif choice == "3":
            show_result(progress)
            print("\nThank you for practising CSE1021.")
            break
        else:
            print("Please enter 1, 2 or 3.")


if __name__ == "__main__":
    main()
