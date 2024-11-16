# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define d = Character("Donna")
define a = Character("Allie")
define k = Character("Mackenzie")
define l = Character("Lindsey")
define dm = Character("Donna’s Mom")

image school = "images/school.png"
image library = "images/library.png"
image darkness = "images/darkness.png"
define SlowD = Dissolve(3.0)
define weijiangfriendshippoints=0
#define quyang = Character("quyang")
#define weijiang = Character("weijiang")
# The game starts here.

#default tb_design = "normal"
while True: 
    image textbox:
        "gui/textbox_[tb_design].png"

label start:
    $ tb_design = "normal"
    scene restaurant
    with dissolve
    play music "audio/school2.mp3"
    "A Certain Fast Food Restaurant just north to the Canaryville High School is quite an interesting place. Of course it is—anything connected to the prestigious Canaryville High School has to be interesting."
    "And now, our remarkable story is about to begin…"

    show wj
    with dissolve
    l "No matter when I come by, this place is always packed. Hi, a Combo A, please!"
    "Food in hand, Lindsey starts to look for a seat."
    "She notices a quiet girl in the corner in the same red-and-white school uniform, working on her laptop."
    scene cg01
    l "Hi there! Would you mind if I sit here?"
    "With a nod from the girl, Wei Jiang pulls out a chair and sits beside her. She takes a sip of her drink and then, always the chatty type, strikes up a conversation."
    scene restaurant
    show wj at left
    show qy at right
    l "Your laptop looks really nice! What are you working on?"
    "The girl turns her laptop toward Wei Jiang. It’s a screen that looks familiar—it’s the MMORPG she’s been playing: UO14."
    l "Wow, I play this game, too! Do you need a teammate? I'm on the cat server—maybe we could play together sometime!"
    l "Oh, sorry… I just got so excited seeing someone else playing that I forgot to introduce myself! I'm Lindsey from 9th Grade. Nice to meet you! What's your name?"
    d "Donna. I’m in 9th grade too. Same server as well."
    "Donna speaks in a calm, steady tone, almost devoid of emotion. But something else catches Lindsey's eye: a few thick notebooks are spread out beside Donna's laptop, their open pages densely packed with formulas and diagrams."
    "These must be advanced—no, honor-level materials!"
    "{i}So even top students play games like this?{/i} Lindsey wonders. But she quickly snaps back to reality."
    l "Really? We are on the same server? What a coincidence! Donna, wanna add friends and play together? My ID is Tsuchi."
    "Lindsey’s face lights up with a smile."
    "Donna gapes at her, looking like her mind has drifted somewhere beyond this universe. She only snaps back to the present when Lindsey waves a hand in front of her."
    d "Friend request sent. My ID is Yurina."
    "Her tone remains as flat and emotionless as before."
    l "Let’s follow each other on Onstagram too! What’s your username?"
    hide wj 
    with dissolve
    hide qy
    with dissolve
    "After exchanging contact info, the two leave the restaurant in their own directions."
    scene room2
    with dissolve
    show wj
    "In the evening, Lindsey returns home and logs into the game. The familiar screen lights up, and just as she’s about to start, a familiar ID pops up in her friend list—Yurina is online."
    l "Wow, Donna is already online! Looks like I'll have some company today!"
    jump onetwo

label onetwo:
    $ tb_design = "quyang"
    scene room1
    with dissolve
    play music "audio/bgm1ok.mp3"
    "Note: this section is played from the perspective of Donna."
    show mrsqu
    dm "And now you’re playing games?"
    dm "You got into the honors program—you should be working extra hard so you can keep up with the other kids."
    dm "Your studies are more important than those good-for-nothing games. Don't you understand?"
    dm "You also need to preview material and email your teacher with questions and—"
    d "I just wanted to relax a bit… I made a new friend today."
    "Donna’s mother, already halfway out the door, retorts with a sarcastic jab."
    dm "A friend? With {i}your{/i} attitude, I can never imagine {i}you{/i} making any friends."
    "She pauses briefly, her tone turning even sharper."
    dm "It’s not a boy, is it? I knew it! I know what you kids are up to these days, especially with these games!"
    "Donna keeps her head down, keeps her head down and stays quiet. Her fingers tighten around the edge of her shirt."
    dm "I'm warning you, Donna. High school is for studying, not for getting caught up in nonsense! No dating. Understand?"
    d "…It’s a girl."
    "Donna’s face stays expressionless."
    hide mrsqu
    with dissolve
    "Her mother leaves the bedroom, still grumbling to herself. As her footsteps get farther down the hall, Donna walks over to the door, shuts it, and locks it."
    "She slips on her headphones, drowning out the noise of her mother's continued ranting in the kitchen."
    scene game1
    with dissolve
    show qy_game at left
    with dissolve
    "As soon as Donna logs into the game, a friend invite pops up on her screen—it’s from Tsuchi. She hesitates for a moment before clicking “Accept.”"
    show wj_game at right
    with dissolve
    "Donna spots a red-haired catgirl by the large teleport crystal in Ocean City."
    "Suddenly, Lindsey’s loud voice comes through her headphones, cheerful and excited."
    l "Hey hey! You’re finally online!"
    d "We're on voice chat... Why are you shouting like I'm super far away?"
    l "Ah, come on! It’s more fun this way!"
    "On the screen, Donna’s quiet, black-haired elf stands in contrasts to Lindsey’s lively, red-haired catgirl."
    d "So, what do you want to do? Dungeon run?"
    l "Nah, that’s too boring. Let’s take some photos together! Come on!"
    d "Photos?"
    l "Yeah! You know, exploring scenic spots, posing with our characters, taking screenshots—don’t you know?"
    d "I’m solo…no one ever mentioned it to me."
    l "Well, now you’ve got me! Playing together is way more fun. I love figuring out all the cool photo spots!"
    d "…Alright."
    "They guide their characters to scenic spots in the game."
    #scene gamemountain
    "On mountain peaks, they capture the setting sun’s glow, their characters standing side by side in warm twilight."
    #scene gamecoast
    "By the ocean, the catgirl jumps in a playful victory pose while the elf stands with a soft smile."
    #scene gamegrassland
    "Finally, they sit together on a grassy hill, gazing at a starry sky. "
    "A shooting star streaks across, carving a path through the darkness."
    "Some say shooting stars carry wishes, each streak in the sky marking a new hope. Lindsey's eye's sparkle, fully believing the star will bring her something special."
    "But Donna watches in silence. A shooting star is just another part of the night sky. Perhaps, she just doesn't believe in miracles anymore."
    "Against the backdrop of the night, every sound seems especially clear."
    "Lindsey’s lively voice carries through Donna’s headphones."
    l "Hey, do you play any other games? Maybe we can team up more often."
    d "This is the only one I play… I read online that it's a good place to make friends, so I downloaded it. But I never really made any friends… You’re actually the first."
    "Lindsey hesitates, unsure of how to respond. Sympathy doesn’t seem appropriate."
    "So, she clumsily changes the topic."
    l "Oh, so you actually want to make friends? I bet there are plenty of people at school who like games. Have you tried talking to them?"
    d "Some of the guys are too loud… I don’t really want to deal with them."
    "{i}A bit of a picky princess, huh?{/i} Lindsey thinks to herself."
    l "Why not try joining some clubs?"
    l "You might meet people with similar interests that way."
    d "Clubs? Are there any for gaming?"
    l "There should be! Tomorrow’s the Club Fair. You down to come with?"
    d "Down to…what?"
    l "I mean…do you want to walk around with me?"
    "Behind the screen, Donna nodded, then realized her friend couldn’t see it."
    "She quickly typed a reply. In the chat window’s corner, Yurina sent a simple, “Sure.”"

    





label test:
    $ tb_design = "normal"
    #模拟移动，先用SALIGIA的素材代替
    show school:
        xalign 0.5
        yalign 0.5
        zoom 2.0

    "move forward."
    # These display lines of dialogue.

    show school:
        zoom 2.0
        xalign 0.5
        yalign 0.5
        linear .5 zoom 2.2 ypos -100
        linear .5 zoom 2.4 ypos 300
        linear .5 zoom 2.6 ypos -200
        linear .5 zoom 2.8 ypos 400
        linear .5 zoom 3.0 ypos -300
        linear .5 zoom 3.2 ypos 500
    show darkness with SlowD
    "stop."

    scene library with dissolve

    e "TEST"

    quyang "test"

    weijiang "test"

    "test"



    jump scene1

label scene1:
    scene school1
    show wei_jiang at left
    with dissolve
    show qu_yang at right
    with dissolve
    $ tb_design = "quyang"
    
    "Qu Yang walks to the school\'s central park (1st time)"
    "What will Qu Yang do?"
    menu:
        "What will you do"
        "Chat with Wei Jiang at the teaching building":
            $ weijiangfriendshippoints +=1
            jump scene2
        "Head to the lab to find Wang Ze and Ling Fan":
            jump scene2

label scene2:
    scene school2
    show wei_jiang at left
    with dissolve
    show qu_yang at right
    with dissolve
    $ tb_design = "weijiang"
    
    "Qu Yang walks to the school\'s central park (2nd time)"
    "What will Qu Yang do?"
    menu:
        "What will you do"
        "Chat with Wei Jiang at the teaching building":
            $ weijiangfriendshippoints +=1
            jump scene3
        "Head to the lab to find Wang Ze and Ling Fan":
            jump scene3

label scene3:
    scene school3
    show wei_jiang at left
    with dissolve
    show qu_yang at right
    with dissolve
    "Qu Yang walks to the school\'s central park (3rd time)"
    "What will Qu Yang do?"
    menu:
        "What will you do"
        "Chat with Wei Jiang at the teaching building":
            $ weijiangfriendshippoints +=1
            if weijiangfriendshippoints >=2:
                jump ending1
            else:
                jump ending2
        "Head to the lab to find Wang Ze and Ling Fan":
            jump ending2

label ending1:
    scene school
    "Ending 1 reached! This is the lesbian route."

    return

label ending2:
    scene school
    "Ending 2 reached! This is the conquest route."

    return