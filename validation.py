"""Simple input validation helpers."""


def valid_menu_choice(choice, first, last):
    return choice.isdigit() and first <= int(choice) <= last


def same_output(prediction, answer):
    return prediction.strip() == answer.strip()
