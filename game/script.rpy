# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define main = Character("Eric")
define cpt = Character("Cpt. Bychkov")
define lt = Character("Lt. Fare")
define eng = Character("Dr. Igarashi")
define tech = Character("Adette")
define exp = Character("Sue")
define soldier = Character("Burkhart")
define sci = Character("Dr. Newinstein")
define ast = Character("Cecelia")
define robot = Character("Britz")
define monkey = Character("Caesar")

define stranger = Character("???")

define hallIntro = False
define cabinIntro = False
define labIntro = False

# The game starts here.

label start:

    show shipIn
    #play music "audio/sounds/Alien space ship sound.mp3"
    #play sound "audio/sounds/treasure founds.mp3"

    show robot with easeinright
    robot "Greetings, you may call me Britz, I am the robot in charge of your lives on the spaceship.
        If you have any questions, you may contact me, I am everywhere, even in the lavatory."
    hide robot with moveoutleft

    main "For now, I think I should go meet the team and see the people I'm working with."

    call shipIntro

label ship2:

    "end"

    return
