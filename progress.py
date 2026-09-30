"""Session progress for RUNPREDICT."""


def new_progress():
    return {"attempts": 0, "correct": 0}


def record_answer(progress, correct):
    progress["attempts"] = progress["attempts"] + 1
    if correct:
        progress["correct"] = progress["correct"] + 1


def show_result(progress):
    print("\n----- SESSION RESULT -----")
    print("Attempts:", progress["attempts"])
    print("Correct :", progress["correct"])
    if progress["attempts"] > 0:
        percentage = progress["correct"] * 100 / progress["attempts"]
        print("Score   :", str(round(percentage, 1)) + "%")
