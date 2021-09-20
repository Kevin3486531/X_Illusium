# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Max = Character("Max")

# The game starts here.

label start:

    show ship

    "I remember the words clearly"
    "My mind returns to the present"

    hide ship

    show roomA

    show Max happy

    Max "Quit spacing out."
    Max "We have a crew meeting in about half an hour from now right?"
    Max "Let's get going."
    "To be continued"

    # This ends the game.

    return
