# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
image school = "images/school.png"
image library = "images/library.png"
image darkness = "images/darkness.png"
define SlowD = Dissolve(3.0)
define weijiangfriendshippoints=0
define quyang = Character("quyang")
define weijiang = Character("weijiang")
# The game starts here.

#default tb_design = "normal"
while True: 
    image textbox:
        "gui/textbox_[tb_design].png"

label start:
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