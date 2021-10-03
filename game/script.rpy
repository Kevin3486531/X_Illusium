﻿# The script of the game goes in this file.

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

    show shipEx
    "It's currently year 3249."
    "Alien life has been discovered and although they have not attacked us yet, their technology far surpasses ours in terms of power."
    "They have introduced their planet as Ambrose."
    "Recent interception of their communications have been decrypted to give us the information of the coordinates of \"Planet X\"."
    "According to the information, this planet holds a large energy source from a past successful civilization."
    "If the ambrosians were to obtain this energy source, they will be a massive threat to Earth."
    "I am Eric, a professional in exploration and my mission, alongside a team of experts, is to secure this energy source from Planet X."
    hide shipEx

    show roomA
    play music "audio/music/xilussim3.mp3"
    #play sound "audio/sounds/treasure founds.mp3"

    show robot
    robot "Greetings, you may call me Britz, I am the robot in charge of your lives on the spaceship.
        If you have any questions, you may contact me, I am everywhere, even in the lavatory."
    hide robot with moveoutleft

    main "For now, I think I should go meet the team and see the people I'm working with."

    call shipIntro from _call_shipIntro

    ""

    "end"

    return
