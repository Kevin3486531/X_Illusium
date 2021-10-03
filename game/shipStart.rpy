label shipIntro:

    if hallIntro == False or cabinIntro == False or labIntro == False:
        main "Where should I go?"
        menu:
            "Main hall" if hallIntro == False:
                $ hallIntro = True
                jump hall
            "Main hall" if hallIntro == True:
                main "I already went there."
                jump shipIntro
            "Control cabin" if cabinIntro == False:
                $ cabinIntro = True
                jump cabin
            "Control cabin" if cabinIntro == True:
                main "I already went there."
                jump shipIntro
            "Laboratory" if labIntro == False:
                $labIntro = True
                jump lab
            "Laboratory" if labIntro == True:
                main "I already went there."
                jump shipIntro

    "That seems to be all the important people at least."
    return

label hall:

    hide roomA with fade
    show shipIn with fade

    show lt
    lt "Welcome to our spaceship! I have been partnering with the captain for many years."
    lt "This spaceship is faster than the spaceship we have driven before.
        But don’t worry, our abilities are fully capable of handling it."

    "This is the lieutenant, Jack Fare. I've seen him a few times with the captain
    before and he seems to be a pretty reliable guy."
    hide lt

    show shipIn with fade

    show eng
    eng "You're curious about this spaceship?"
    eng "Why, it was designed by my team, headed by yours truly.
        It is the perfect transport for such a glorious mission."
    eng "As the head engineer, I know the design and functionality of the entire spacecraft.
        It is my pride and joy!"

    "This is the head engineer, Dr. Igarashi. I've seen him in the news before,
    but he seems a fair more egotistical than I remember."
    hide eng with moveoutleft

    "THUD"
    "Someone shoves me in the back."
    stranger "Oops, my mistake."
    show exp
    exp "Oh, it's you again. Better not get in my way this time."
    hide exp with moveoutright
    main "Hey, that was definitely your fault."
    "That was Sue, another exploration expert like me."
    "We had a mission in the past but ran into some trouble because of her not assessing the area
    for traps before making a move."

    "Anyway, that seemed to be everyone here."

    show shipIn with fade
    jump shipIntro

label cabin:

    hide roomA with fade
    show shipIn with fade

    show cpt
    cpt "I've never seen you before. You are one of the exploration experts, correct?"
    "This is Captain Bychkov. I saw him receiving the mission from the general personally
    yesterday, but I've never actually spoken with him before."
    main "Yes, my name is Eric He. Captain, what do you think of this mission?"
    cpt "This mission will be very difficult. We don't know what those aliens are planning.
        Our planet's future may be decided by this mission."
    cpt "No matter how many sacrifices we make, we must complete this mission.
         As the captain, I will take command and lead us to victory."
    cpt "Now, I must continue preparing for our meeting regarding our plans."
    cpt "I expect to see you there."
    hide cpt with moveoutleft

    "I'd like to hope that there will be no sacrifices."

    stranger "WUWUWUWUWUWUWUWUWUWUWU"
    "I turn towards the source of the sound and look down."
    show monkey
    "...What?"
    hide monkey with moveoutleft
    "Am I hallucinating? Why is there a monkey aboard this ship?"

    "I think I should head back, seemed like that was everyone here."

    show shipIn with fade
    jump shipIntro

label lab:

    hide roomA with fade
    show shipIn with fade

    show sci:
        xalign 0.7
    show ast:
        xalign 0.3
    sci "Yes, the dynamic theory of this spacecraft was researched by me.
        In the universe, our human civilization is simply like a small dust particle."
    sci "To have discovered an alien civilization in my lifetime, oh I just can't wait to
        see their technology! Aren't you excited, Cecelia?"
    ast "Yes, yes, I get it. You really want to see those aliens up close. It's too bad we are basically at war."

    "That's our researcher, Dr. Newinstein and who I assume is his assistant."

    hide sci with moveoutright
    ast "Hm, who are you?"
    main "Hello, my name is Eric-"
    ast "So you're not a researcher?"
    ast "Then why are you here? We can't risk you breaking any important equipment."
    ast "If you have no business then you should just leave."
    hide ast

    "Stunned by the sudden aggressiveness, I turned away."
    "It seemed like it was just those two here anyway."


    show shipIn with fade
    jump shipIntro
