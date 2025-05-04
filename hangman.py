# # 
import random

lives = 6
stage = [
    """
    +---+
        |
        |
        |
        ===
    """,
    """
    +---+
    O   |
        |
        |
        ===
    """,
    """
    +---+
    O   |
    |   |
        |
        ===
    """,
    """
    +---+
    O   |
    /|  |
        |
        ===
    """,
    """
    +---+
    O   |
    /|\\ |
        |
        ===
    """,
    """
    +---+
    O   |
    /|\\ |
    /   |
        ===
    """,
    """
    +---+
    O   |
    /|\\ |
    / \\ |
        ===
    """
]

word_list = ["machen", "schafen", "vorfugbaren"]
choosen_word = random.choice(word_list)
print(choosen_word)

placeholder = ""
word_length = len(choosen_word)
for position in range(word_length):
    placeholder += "_"

print(placeholder)

game_over = False
correct_letter = []

while not game_over:
    Guess = input("Guess a letter: ").lower()
    display = ""

    for letter in choosen_word:
        if letter == Guess:
            display += letter
            if Guess not in correct_letter:
                correct_letter.append(Guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"

    print(display)

    if Guess not in choosen_word:
        lives -= 1
        print(f"Falsch! Der Buchstabe '{Guess}' ist nicht im Wort.")
        print(f"Noch {lives} Versuche übrig.")
        print(stage[6 - lives])
        if lives == 0:
            game_over = True
            print("Du hast verloren! Das Wort war:", choosen_word)
    else:
        print("Richtig!")

    if "_" not in display:
        game_over = True
        print("Glückwunsch! Du hast gewonnen!")

print(display)
