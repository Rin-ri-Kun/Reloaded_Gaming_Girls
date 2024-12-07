# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define d = Character("Donna", who_color="#CC33FF")#区洋
define a = Character("Allie", who_color="#FF0066")#凌凡
define k = Character("Mackenzie", who_color="#7AAFFF")#汪泽
define l = Character("Lindsey", who_color="#ffc72f")#魏江
define dg = Character("Yurina", who_color="#CC33FF")
define ag = Character("Allyknight", who_color="#FF0066")
define kg = Character("Trailblazer", who_color="#7AAFFF")
define lg = Character("Tsuchi", who_color="#ffc72f")
define dm = Character("Donna’s Mom")
define ca = Character("Classmate A")
define cb = Character("Classmate B")
define x = Character("???")

define interludechoice1 = 0
define interludechoice2 = 0

define SlowD = Dissolve(3.0)
define weijiangfriendshippoints=0
define add1 = False
define add2 = False
define add3 = False
# The game starts here.

#default tb_design = "normal"
#while True: 
image textbox:
    "gui/textbox_[tb_design].png"

image lindsey_neutral:
    "images/Lindsey_neutral.PNG"
    zoom 0.4
image donna_neutral:
    "images/donna_neutral.PNG"
    zoom 0.4
image mackenzie_neutral:
    "images/mackenzie_neutral.PNG"
    zoom 0.4
image allie_neutral:
    "images/allie_neutral.PNG"
    zoom 0.4
image lindsey_angry:
    "images/lindsey_angry.PNG"
    zoom 0.4
image donna_angry:
    "images/donna_angry.PNG"
    zoom 0.4
image mackenzie_angry:
    "images/mackenzie_angry.PNG"
    zoom 0.4
image allie_angry:
    "images/allie_angry.PNG"
    zoom 0.4
image lindsey_afraid:
    "images/lindsey_afraid.PNG"
    zoom 0.4
image donna_afraid:
    "images/donna_afraid.PNG"
    zoom 0.4
image mackenzie_afraid:
    "images/mackenzie_afraid.PNG"
    zoom 0.4
image allie_afraid:
    "images/allie_afraid.PNG"
    zoom 0.4
image lindsey_sad:
    "images/lindsey_sad.PNG"
    zoom 0.4
image donna_sad:
    "images/donna_sad.PNG"
    zoom 0.4
image mackenzie_sad:
    "images/mackenzie_sad.PNG"
    zoom 0.4
image allie_sad:
    "images/allie_sad.PNG"
    zoom 0.4
image lindsey_happy:
    "images/lindsey_happy.PNG"
    zoom 0.4
image donna_happy:
    "images/donna_happy.PNG"
    zoom 0.4
image mackenzie_happy:
    "images/mackenzie_happy.PNG"
    zoom 0.4
image allie_happy:
    "images/allie_happy.PNG"
    zoom 0.4
image mrsqu:
    "images/mrsqu.PNG"
    zoom 0.27
label splashscreen:
    $ tb_design = "none"
    show unitedbackground
    with dissolve
    pause 1
    hide unitedbackground
    with dissolve
    return
label start:
    $ tb_design = "normal"
    stop music
    scene bridge
    "Welcome to Unique Gaming Girls - Reloaded Edition!\nUse your mouse to click through the story and make choices when needed."
    "Note: This game is set in a fictional school setting, combining elements from different countries."
    "Please enjoy. (This time, we promise it’s actually enjoyable!)"
    jump oneone

label oneone:
    $ tb_design = "normal"
    scene restaurant
    with dissolve
    play music "audio/school2.mp3"
    "A Certain Fast Food Restaurant just north to the Canaryville High School is quite an interesting place. Of course it is—anything connected to the prestigious Canaryville High School has to be interesting."
    "And now, our remarkable story is about to begin…"

    show lindsey_neutral
    with dissolve
    l "No matter when I come by, this place is always packed. "
    #hide lindsey_neutral
    show lindsey_neutral:#跳跃动画
        linear 0.1 yalign 0.8
        linear 0.1 yalign 1.0
    l "Hi, a Combo A, please!"
    hide lindsey_neutral
    show lindsey_happy
    "Food in hand, Lindsey starts to look for a seat."
    scene cg01
    "She notices a quiet girl in the corner in the same red-and-white school uniform, working on her laptop."
    l "Hi there! Would you mind if I sit here?"
    "With a nod from the girl, Lindsey pulls out a chair and sits beside her. She takes a sip of her drink and then, always the chatty type, strikes up a conversation."
    scene restaurant
    show lindsey_neutral at left
    show donna_neutral at right
    l "Your laptop looks really nice! What are you working on?"
    "The girl turns her laptop toward Lindsey. It’s a screen that looks familiar—it’s the MMORPG she’s been playing: UO14."
    hide lindsey_neutral
    show lindsey_happy at left
    l "Wow, I play this game, too! Do you need a teammate? I’m on the cat server—maybe we could play together sometime!"
    hide lindsey_happy
    show lindsey_sad at left
    l "Oh, sorry… I just got so excited seeing someone else playing that I forgot to introduce myself! I’m Lindsey from 9th Grade. Nice to meet you! What’s your name?"
    d "Donna. I’m in 9th grade too. Same server as well."
    hide lindsey_sad
    show lindsey_neutral at left
    "Donna speaks in a calm, steady tone, almost devoid of emotion. But something else catches Lindsey’s eye: a few thick notebooks are spread out beside Donna’s laptop, their open pages densely packed with formulas and diagrams."
    "These must be advanced—no, honor-level materials!"
    "{i}So even top students play games like this?{/i} Lindsey wonders. But she quickly snaps back to reality."
    l "Really? We are on the same server? What a coincidence! Donna, wanna add friends and play together? My ID is Tsuchi."
    "Lindsey’s face lights up with a smile."
    "Donna gapes at her, looking like her mind has drifted somewhere beyond this universe. She only snaps back to the present when Lindsey waves a hand in front of her."
    d "Friend request sent. My ID is Yurina."
    "Her tone remains as flat and emotionless as before."
    l "Let’s follow each other on Onstagram too! What’s your username?"
    hide lindsey_neutral 
    with dissolve
    hide donna_neutral
    with dissolve
    "After exchanging contact info, the two leave the restaurant in their own directions."
    scene room2
    with dissolve
    show lindsey_happy
    "In the evening, Lindsey returns home and logs into the game. The familiar screen lights up, and just as she’s about to start, a familiar ID pops up in her friend list—Yurina is online."
    show lindsey_happy:#跳跃动画
        linear 0.1 yalign 0.8
        linear 0.1 yalign 1.0
    l "Wow, Donna is already online! Looks like I’ll have some company today!"
    scene darkness with dissolve
    "Meanwhile……"
    jump onetwo

label onetwo:
    $ tb_design = "quyang"
    scene room1
    with dissolve
    play music "<loop 4.58>audio/bgm1ok.mp3"
    "Note: sections with this textbox are played from the perspective of Donna."
    show mrsqu
    dm "And now you’re playing games?"
    dm "You got into the honors program—you should be working extra hard so you can keep up with the other kids."
    dm "Your studies are more important than those good-for-nothing games. Don’t you understand?"
    dm "You also need to preview material and email your teacher with questions and—"
    d "I just wanted to relax a bit… I made a new friend today."
    "Donna’s mother, already halfway out the door, retorts with a sarcastic jab."
    dm "A friend? With {i}your{/i} attitude, I can never imagine {i}you{/i} making any friends."
    "She pauses briefly, her tone turning even sharper."
    dm "It’s not a boy, is it? I knew it! I know what you kids are up to these days, especially with these games!"
    "Donna keeps her head down, keeps her head down and stays quiet. Her fingers tighten around the edge of her shirt."
    dm "I’m warning you, Donna. High school is for studying, not for getting caught up in nonsense! No dating. Understand?"
    d "…It’s a girl."
    "Donna’s face stays expressionless."
    hide mrsqu with moveoutleft
    "Her mother leaves the bedroom, still grumbling to herself. As her footsteps get farther down the hall, Donna walks over to the door, shuts it, and locks it."
    "She slips on her headphones, drowning out the noise of her mother’s continued ranting in the kitchen."
    scene game1
    with dissolve
    show qy_game at left
    with dissolve
    play music "audio/justice.mp3"
    "As soon as Donna logs into the game, a friend invite pops up on her screen—it’s from Tsuchi. She hesitates for a moment before clicking “Accept.”"
    show wj_game at right
    with dissolve
    "Donna spots a red-haired catgirl by the large teleport crystal in Ocean City."
    "Suddenly, Lindsey’s loud voice comes through her headphones, cheerful and excited."
    lg "Hey hey! You’re finally online!"
    dg "We’re on voice chat… Why are you shouting like I’m super far away?"
    lg "Ah, come on! It’s more fun this way!"
    "On the screen, Donna’s quiet, black-haired elf stands in contrasts to Lindsey’s lively, red-haired catgirl."
    dg "So, what do you want to do? Dungeon run?"
    lg "Nah, that’s too boring. Let’s take some photos together! Come on!"
    dg "Photos?"
    lg "Yeah! You know, exploring scenic spots, posing with our characters, taking screenshots—don’t you know?"
    dg "I’m solo…no one ever mentioned it to me."
    lg "Well, now you’ve got me! Playing together is way more fun. I love figuring out all the cool photo spots!"
    dg "…Alright."
    "They guide their characters to scenic spots in the game."
    scene gamemountain
    with dissolve
    show qy_game at left
    with moveinleft
    show wj_game at right
    with moveinleft
    "On mountain peaks, they capture the setting sun’s glow, their characters standing side by side in warm twilight."
    hide qy_game with moveoutright
    hide wj_game with moveoutright
    scene gamecoast
    with dissolve
    show qy_game at left
    with moveinleft
    show wj_game at right
    with moveinleft
    "By the ocean, the catgirl jumps in a playful victory pose while the elf stands with a soft smile."
    hide qy_game with moveoutright
    hide wj_game with moveoutright
    scene gamegrassland
    with dissolve
    show qy_game at left
    with moveinleft
    show wj_game at right
    with moveinleft
    "Finally, they sit together on a grassy hill, gazing at a starry sky. "
    scene gamegrassland
    show qy_game at left
    show wj_game at right
    show frame
    with fade
    "A shooting star streaks across, carving a path through the darkness."
    scene gamegrassland
    show qy_game at left
    show wj_game at right
    "Some say shooting stars carry wishes, each streak in the sky marking a new hope. Lindsey’s eye’s sparkle, fully believing the star will bring her something special."
    "But Donna watches in silence. A shooting star is just another part of the night sky. Perhaps, she just doesn’t believe in miracles anymore."
    "Against the backdrop of the night, every sound seems especially clear."
    "Lindsey’s lively voice carries through Donna’s headphones."
    lg "Hey, do you play any other games? Maybe we can team up more often."
    dg "This is the only one I play… I read online that it’s a good place to make friends, so I downloaded it. But I never really made any friends… You’re actually the first."
    "Lindsey hesitates, unsure of how to respond. Sympathy doesn’t seem appropriate."
    "So, she clumsily changes the topic."
    lg "Oh, so you actually want to make friends? I bet there are plenty of people at school who like games. Have you tried talking to them?"
    dg "Some of the guys are too loud… I don’t really want to deal with them."
    "{i}A bit of a picky princess, huh?{/i} Lindsey thinks to herself."
    lg "Why not try joining some clubs?"
    lg "You might meet people with similar interests that way."
    dg "Clubs? Are there any for gaming?"
    lg "There should be! Tomorrow’s the Club Fair. You down to come with?"
    dg "Down to…what?"
    lg "I mean…do you want to walk around with me?"
    "Behind the screen, Donna nodded, then realized her friend couldn’t see it."
    "She quickly typed a reply. In the chat window’s corner, Yurina sent a simple, “Sure.”"
    scene darkness with dissolve
    "The next day……"
    jump onethree

label onethree:
    $ tb_design = "normal"
    play music "audio/school2.mp3"
    scene garden 
    with dissolve
    "It’s 12:25, and the Central Garden is packed with students at the Club Fair."
    "The loud and bustling crowd has clearly exceeded the Garden’s capacity."
    "Donna walks out onto campus, fresh out of class, and hears someone calling her name from a distance."
    show lindsey_happy at left
    with dissolve
    show lindsey_happy:#跳跃动画
        linear 0.1 yalign 0.8
        linear 0.1 yalign 1.0
    l "Hey—hey—Donna! Over here!"
    show donna_sad:
        zoom 0.8
        yalign 1.0
        xalign 1.0
    "Donna’s face flushes with a hint of embarrassment. "
    show donna_sad:
        linear 1 xalign 0.3 zoom 1
    "She quickly walks over and gently tugs on Lindsey’s sleeve."
    d "Everyone’s looking at you…"
    hide lindsey_happy
    show lindsey_neutral at left
    l "Hehe…\nSo, we’re looking for the game club, right? Let’s get started!"
    "Donna instinctively stays close behind Lindsey."
    l "Hmm…Debate Club…Modern Music Club…Cultural Exchange Club…Oh, Anime Club! That looks interesting!"
    hide donna_sad
    show donna_neutral:
        xalign 0.3
        yalign 1.0
    show donna_neutral:
        linear 0.5 xalign 0.25
        linear 0.5 xalign 0.3
    "Lindsey feels another tug on her sleeve."
    d "I thought we were looking for a gaming club…"
    l "Oh—right, sorry, sorry! Got a little carried away there."
    l "Alright, let’s see…where’s the gaming club…?"
    d "Too loud…"
    hide lindsey_neutral
    show lindsey_neutral at left
    show allie_neutral at right
    x "Are you two looking for a gaming club? How about checking out the Game Design Club?"
    "Donna turns toward the calling voice—Donna turns toward the calling voice. To her right, a girl sat alone at a small table, empty other than a small stack of flyers and a SUSA gaming laptop with a Triscord QR code."
    "The lackluster scene stood out within the business of the Garden square."
    "The girl picked up a flier and waved it casually toward the two girls."
    l "Game Design Club? Sounds cool! Can you tell us more?"
    hide allie_neutral
    show allie_sad at right
    pause 0.5
    hide allie_sad
    show allie_neutral at right
    "Donna noticed a flicker of a curious expression on the older girl’s face."
    hide allie_neutral
    show allie_happy at right
    x "Sure! I’m Allie, 10th grade, and the club’s vice president. Our president, Kenzie—isn’t here today, so I’m handling recruitment."
    a "As the name suggests, we focus on creating games. Everyone in the club is a game enthusiast, and we treat it as a kind of ’interactive media’…"
    hide lindsey_neutral
    show lindsey_angry at left
    l "Hold up!"
    l "How many members are there in the club? What roles do people have? And what could Donna and I do if we joined?"
    hide allie_happy
    show allie_sad at right
    pause 0.5
    hide allie_sad
    show allie_neutral at right
    "Allie’s curious expression flashed again, though she managed to keep herself cool."
    $ renpy.music.set_pause(True, channel="music")
    show allie_neutral:
        linear 0.5 yalign 1.3
    a "Actually, if both of you join, we’d have four members, which would meet the minimum requirement for the club to exist."
    l "…"
    d "…"
    $ renpy.music.set_pause(False, channel="music")
    hide lindsey_angry
    show lindsey_afraid at left
    hide donna_neutral
    show donna_afraid:
        xalign 0.3
        yalign 1.0
    l "So…you’re a ghost club?"
    hide allie_neutral
    show allie_sad at right
    a "Don’t put it that way. The president, Mackenzie, and I are really dedicated to making this club work. I’ll handle music, she’s responsible for programming. We just need someone for art and writing…"
    hide donna_afraid
    show donna_neutral:
        xalign 0.3
        yalign 1.0
    hide lindsey_afraid
    show lindsey_neutral at left
    "Donna, who had been silent until now, suddenly spoke up."
    d "Um…I can write a bit."
    l "I could handle art—oh, wait!"
    hide lindsey_neutral
    show lindsey_angry at left
    "Lindsey slaps her forehead and seems to contemplate for a bit. Unexpectedly, she grabs Donna’s hand and pulls her aside. Donna, surprised by the sudden physical contact, stumbles into confusion."
    hide allie_sad
    show allie_angry at right
    l "This club seems odd. Only two members—it’s clearly just a placeholder club! Let’s find a bigger game club instead. We don’t wanna get caught up in anything weird!"
    a "…No offense, but I can hear that."
    hide lindsey_angry
    show lindsey_afraid at left
    "Lindsey, frozen up, blinks innocently at Allie before realizing how badly she just screwed herself over. She tries to walk away with Donna in tow. Donna can’t get over how warm Lindsey’s hand is."
    "Allie sighs and calls after them."
    a "Wait! You’re not wrong, but the other game club? They just grind ranked matches non-stop. You two don’t seem like the competitive type, do you?"
    hide lindsey_afraid
    show lindsey_neutral at left
    l "Ah, yeah, I usually play MMORPGs…"
    "Donna nods."
    hide allie_angry
    show allie_neutral at right
    a "Oh, like UO14? Ken-ken and I play that too!"
    l "No way! Which server?"
    a "We’re on the Cat server…"
    hide donna_neutral
    show donna_happy:
        xalign 0.3
        yalign 1.0
    "Donna’s heart skips, and a flash of excitement leaks from her usually stolid face. Lindsey lets out a surprised gasp."
    "Allie gives a dumbfounded stare, clearly taken aback by their reactions."
    a "I’m guessing you two are on that server, too…"
    scene darkness with dissolve
    "Later in the night……"
    jump onefour

label onefour:
    $ tb_design = "normal"
    play music "audio/justice.mp3"
    scene game1
    with dissolve
    show qy_game at left
    with dissolve
    "That evening, Donna, away from her mother’s sight, log into UO14 again."
    "The voice channel has four people—clearly, Lindsey had invited the newcomers. The team gathers by the Grand Crystal in Ocean City."
    show wj_game at right
    with dissolve
    show lf_game
    with dissolve
    "Allie appears as “Allyknight” in the game."
    hide lf_game
    show wz_game
    with dissolve
    "As for the club president, Mackenzie, who hadn’t been at the fair earlier, her ID carries a hint of dramatic flair."
    hide qy_game
    hide wz_game
    show wz_game at left
    lg "Wow, an elegant white-haired dragon girl named “Trailblazer”… Bold choice, senpai!"
    "Mackenzie’s gentle voice flows through their headsets."
    kg "Actually, Allie picked that ID for me, actually. I really like it."
    hide wj_game
    show lf_game at right
    ag "See? It suits you, you weirdo."
    kg "By the way! I designed Allie’s character."
    kg "Look at her—pink hair with blue highlights, just like her in real life—she’s my sweetheart, gotta mark my territory!"
    "Mackenzie’s tone suddenly takes on a playful edge, leaving it unclear whether she was referring to Allyknight or Allie herself…"
    hide wz_game
    show qy_game at left
    "Breaking the awkward atmosphere, Donna quietly interjects." 
    dg "So… Are we taking photos again tonight?"
    hide lf_game
    show wj_game at right
    lg "Nah, we’ve got enough people for a change! Let’s try a multiplayer dungeon run!"
    "Tsuchi, Lindsey’s red-haired catgirl, darts toward the dungeon entrance, with the pink-haired knight following close behind."
    hide wj_game
    show lf_game at right
    ag "Hey, wait! We need to talk about the club!"
    ag "Last time, you all disappeared before agreeing to join!"
    #scene new CG
    "As the dungeon load, monsters appeared on the screen, and the intense battle begin."
    "The monsters launch an AoE attack right off the bat, rapidly draining the team’s health."
    lg "Oh no! Someone heal me—I’m about to die!"
    ag "Hold on! My skills are still on cooldown—just hang in there!"
    kg "Allie, don’t die on me—I still need you to write my music!"
    "Suddenly, everyone’s health is fully restored. A quiet voice come through the headset."
    dg "…Healed."
    lg "Wow, Donna! That was amazing! You saved us!"
    "With that clutch move, Lindsey and the other players manage to strike the boss again, the boss finally fall."
    "With the intense battle over, the group relax, casually fighting small monsters as their conversation drift."
    scene game1
    play music "audio/school2.mp3"
    with dissolve
    show wj_game
    lg "Hey, we actually worked pretty well as a team!"
    hide wj_game
    show lf_game
    ag "See? If we’re this in-sync in the game, it’s only natural for you to join the club!"
    ag "With you both, we can finally get our game off the ground!"
    hide lf_game
    show wj_game
    lg "Hmm…well, working with you guys does sound kind of fun."
    lg "Even if it’s a “ghost club,” it doesn’t really matter."
    lg "Oh, and Donna wanted to find friends with similar interests, right?"
    hide wj_game
    show qy_game
    dg "…Yes, I could consider it."
    hide qy_game
    show lf_game
    ag "Ah, don’t “consider” it!"
    ag "Both of you are perfect—you with writing, Lindsey with art. Together, we’d make an amazing team. "
    ag "Come on, I know you would make the right decision."
    ag "You don’t want to leave our club hanging as a “ghost club”, right…"
    ag "This club is gonna be wonderful, I promise!"
    hide lf_game
    show wz_game at right
    show lf_game at left
    kg "I’ve already sent the club application forms to your emails!"
    "Mackenzie’s voice remains gentle as ever. Sensing Allie’s nervousness, she softly adds:"
    kg "It’s okay, Allie. Don’t worry, sweetie."
    "Allie, unseen by the other players, let out a deep sigh of relief."
    ag "Thanks for the reminder, Ken-ken! We will certainly need the club application forms for you!"
    hide lf_game
    hide wz_game
    show wj_game at left
    show qy_game at right
    "Lindsey and Donna give each other a look, and they seemingly finalize a decision."
    lg "Alright, alright—we’re in."
    dg "Yes."
    lg "So, since this is a game design club, what kind of game are we making?"
    show lf_game
    ag "…Originally, we planned to make a rhythm game."
    "Allie’s voice wavers slightly, as though still touched by Mackenzie’s reassurance. After a pause, her usual confident, teasing tone returns."
    ag "But Mackenzie’s programming skills aren’t the best…Rhythm games are a bit complex for us, so we switched to a narrative-driven game."
    lg "Narrative-driven? Like a galgame?"
    hide qy_game
    show wz_game at right
    kg "Isn’t that the kind of game otakus like?"
    ag "Highbrow folks call it a “visual novel” or “text adventure game”."
    kg "Basically, that’s it. When Allie and I were having our little“two-person world” in the clubroom, we thought it over~"
    lg "You two…really get along well, huh."
    "Lindsey’s comment makes the voice channel fall silent."
    "An unspoken tension linger in the air, and no one rushes to break it."
    hide wj_game
    show qy_game at left
    "After a few seconds, Donna speaks calmly, bringing the conversation back on track."
    dg "So… Do you have a theme for the game yet?"
    kg "Hmm…oh! How about a school setting?\nTragic, angsty stories of youth are always popular~"
    lg "Ooh, sounds intense!"
    ag "Hey, don’t listen to her rambling."
    ag "The game still has to pass the teacher’s review, anything weird is going to get us sent back to the drawing board!"
    "It is clear that, while Allie is poking fun at Mackenzie’s idea, she isn’t exactly a fan of the “reviewing teacher” herself."
    ag "Still, a school setting could work."
    kg "We did consider writing a more serious, traditional storyline."
    ag "But creating something meaningful and deep is challenging."
    ag "We’re still just high school students… We don’t have that much literary experience."
    kg "Yeah, I agree with Allie."
    kg "Building a new fictional world is too time-consuming."
    kg "Our story should probably stay closer to real life."
    hide qy_game
    show wj_game at left
    lg "Hey, that’s easy then!"
    lg "We can base it on our own experiences—it’ll feel more real and interesting that way!"
    kg "But my life isn’t all sunshine and rainbows."
    kg "Most of the time, it’s just me sitting in class—pretty boring."
    kg "Oh! Allie’s life should be a bit more eventful. How about letting her adapt her own experiences?"
    ag "Me? My writing skills are seriously lacking."
    ag "Besides, I’m already handling the music…"
    ag "Kenken, you’re such a terrible boss, trying to make me work double!"
    "The pink-haired knight drops her focus on the minor enemies and charges at the white-haired dragon girl, sword raised."
    "Even though players attacking each other doesn’t actually reduce health, Mackenzie’s exaggerated cries fill the voice channel."
    kg "Ah! Stop, stop, that really hurts! Allie, how can you be so ruthless?!"
    "The playful bickering between Mackenzie and Allie fill the background, mixed with Lindsey’s attempts to mediate."
    lg "Hey, quit fighting! Actually, Donna could take on the writing—she’d be great at it!"
    hide wz_game
    show qy_game at right
    dg "Oh… yes, I could."
    hide qy_game
    with dissolve
    hide lf_game
    with dissolve
    hide wj_game
    with dissolve
    "Donna didn’t pay much attention to the rest of their brainstorming."
    "Her thoughts keep circling back to something Lindsey had said:"
    "“Basing it on our own experiences…”"
    jump twoone

label twoone:
    $ tb_design = "quyang"
    scene cg_sleep
    with fade
    play music "audio/something2.mp3"
    "Donna’s sleeping posture is somewhat strange. She isn’t short for girls in this age, but when sleeping, she always unconsciously curls up into a ball."
    "She stares blankly into space, thinking about what Lindsey said earlier."
    d "Adapting my own experiences… What have I even experienced?"
    "Donna silently turns over, curling herself into an even smaller ball, trying to find some sense of security this way."
    d "Such a boring life, everyone would hate it if I told them about it. Ah, it’s already past midnight, I need to sleep quickly…"
    "Finally shaking off her scattered and chaotic thoughts, Donna lies in bed counting sheep, trying to drift off to sleep."
    d "Three hundred and twenty, three hundred nineteen… mmm…"
    "The hour hand moved across half the clock face before Donna finally began to feel drowsy."
    "Only soft breathing remains in the room. However, those earlier memories and thoughts haven’t disappeared, instead gradually weaving into her dreamscape, taking her back to those deeply buried memories."
    scene classroomdream
    with fade
    ca "Hey, that’s Donna over there, right!"
    cb "Must be her, always wearing that sour expression, who knows who she’s trying to impress."
    ca "I heard her family is pretty well-off, so why does she always have that “keep away” expression? No wonder the other girls exclude her."
    cb "Forget about her, she’s a bad omen. Let’s hurry home and play UO14. My sister told me the game has really strong “social features”, and she made lots of friends through it."
    ca "Whoa, look at that crazy girl’s computer! She’s playing UO14 too?"
    cb "Pff, probably just trying to find friends. Someone like her, with no friends in real life, no way she’ll make any online either!"
    "The two bullies left, laughing loudly."
    scene restaurantdream
    with dissolve
    "The dream shifts to a crowded fast food restaurant."
    show lindsey_happy
    with dissolve
    l "…Hi, I’m Lindsey from 9th grade…"
    scene gardendream
    with dissolve
    "At the Central Garden…"
    show lindsey_happy
    with dissolve
    l "Hey— hey— Donna! Over here."
    scene game1dream
    with dissolve
    "Inside UO14…"
    show wz_game at left
    with dissolve
    show wj_game
    with dissolve
    show lf_game at right
    with dissolve
    l "Let’s take a photo! Come on!"
    k "We’re counting on you for the script, Donnie!"
    a "Do your best!"
    scene room1
    with fade
    "Donna is awakened by an alarm clock. She opens her eyes, staring at the ceiling, slightly dazed. Realizing there’s a faint smile on her lips, she gently presses them together, hiding the smile away."
    "So, does this mean she finally made friends? She had downloaded that online game without thinking twice. Through it she met two senior students—and that girl who loves to smile."
    d "Club activities, huh…"
    "Although she has become skilled at hiding her emotions behind a calm expression, she realized —she might be looking forward to it: to the club, to the future, and to that girl."
    "Thinking about this, Donna changed into her school uniform and set off for school. There goes a new day."
    jump twotwo

label twotwo:
    $ tb_design = "quyang"
    scene classroom
    with dissolve
    play music "audio/school2.mp3"
    "In the blink of an eye, the day’s classes are about to end. At two in the afternoon, Donna prepares to head for Study Hall. She had just found a secluded corner to sit down, when she saw the blonde girl appearing at the study room door. "
    show lindsey_neutral at right
    show lindsey_neutral:
        linear 1 xalign 0.5
    l "Excuse me, is Donna here?"
    "Donna looks up, meeting Lindsey’s bright eyes directly. At this moment, Donna…"
    menu:
        "What would Donna do?"
        "Quickly hides, using her laptop to cover her face.":
            "Donna quickly hides behind her computer screen. She feels nervous and awkward, seemingly not expecting Lindsey to come looking for her in the study hall."
            "So, she bites her lip, trying hard not to make a sound."
            "Getting no answer, Lindsey stands at the door looking around. Soon, she spots Donna sitting in the last row, hiding behind her laptop screen."
        "Timidly responds to Lindsey. ":
            if add1 == False:
                $ add1 = True
                $ weijiangfriendshippoints+=1
            "Donna peeks out from behind her computer screen. Nervously, she trembles as she waves her hand, gesturing to Lindsey to come over. Then, in a tiny voice, she answers:"
            d "…I’m here. Don’t call so loudly, there are so many people…"
    l "Ah, Donnie, so that’s where you are! Good afternoon!"
    "Donna watches Lindsey walking towards her from afar. Her mind starts racing… When did she get a “new name”? Only when Lindsey comes over and waves in front of her does she snap back to reality, stammering."
    d "…Don…Donnie?"
    show lindsey_neutral:
        linear 0.5 yalign 1.1
        linear 0.5 yalign 1.05
    l "It’s a cute nickname, right? Always calling you Donna feels too formal. You can call me Linnie, that’s what my friends call me!"
    d "Ah, okay…Linnie."
    "Donna looks away, tilting her head slightly to hide her embarrassment. She’s still not used to such intimate nicknames."
    d "…Did you need something?"
    l "Not really. Just that we haven’t seen each other in person for several days, and I missed you."
    d "But… How did you know I was in this class?"
    hide lindsey_neutral
    show lindsey_happy 
    "Lindsey playfully winks at her."
    l "Because I have magic— Just kidding, I guessed! Since you’re a “Star Student” with straight As! I had a feeling you’d take study hall to complete homework."
    l "This is called— a pop inspection! Let me see if you’re secretly studying behind my back—"
    "The fluffy blonde head suddenly leans in next to Donna, eyes fixed unblinkingly on her computer. —On the screen is a new blank document."
    d "Ah, I’m not studying… I was trying to write our game script, but I can’t think of any ideas."
    l "Oh? Is that so? Where are you stuck? Maybe like we discussed last time, try writing about your own experiences. If you really can’t think of anything from your own experience, how about writing about teenage themes? Like a romantic comedy? Have you ever…"
    hide lindsey_happy
    show lindsey_sad
    stop music
    "Lindsey’s voice suddenly cuts off. "
    d "{i}I know Lindsey must have realized this topic might not be “suitable”!{/i}"
    d "{i}After all, I don’t have many friends, and have never experienced the so-called “romantic comedy”.{/i}"
    d "{i}Lindsey probably knows this would be difficult for me…{/i} "
    d "{i}Well, my tragic experiences had determined from the start that I wouldn’t be a good screenwriter…{/i}"
    hide lindsey_sad
    show lindsey_neutral
    play music "audio/school2.mp3"
    "Lindsey’s clear voice pulls Donna out of the abyss of negative emotions."
    "Ah, sorry, I shouldn’t have suddenly asked about such private matters! Then… perhaps, could you show us what you’ve written before? We could brainstorm together—"
    d "……"
    "Donna unconsciously clenches her fists, her nails digging deep into her palms. Lindsey’s words clearly reminded her of those works that her mother had torn to pieces. Along with those pieces… went her dream of becoming a novelist."
    d "…Most of them might be hard to find now, but I’ll look for them when I get home."
    hide lindsey_neutral
    show lindsey_afraid
    "Donna looks up after speaking. She sees Lindsey’s rosy cheeks gradually turning pale, seemingly feeling guilty about saying the wrong thing."
    l "Ah, okay… then, I should head back to class? The next period is-is about to start… "
    hide lindsey_afraid
    with dissolve
    "Donna watches Lindsey awkwardly disappearing from view and quietly sighed. There isn’t even a next period… school’s about to end. While thinking about those things, her expression must have been bad, she wonders if it scared her…"
    jump twothree

label twothree:
    $ tb_design = "quyang"
    play music "audio/inspired.mp3"
    scene room1memory
    with fade
    "Some years ago…"
    show mrsqu
    dm "What kind of nonsense are you writing? You read so many books, and all you read are such nonsense? Can’t you write something more wholesome and uplifting?"
    d "But, I’m writing about a tragedy… Writing it this way better highlights the emotional tension…"
    dm "You’re just a child, what do you know about tragedy? You’ve always had enough to eat and wear at home, what could you possibly be unhappy about?"
    "Young Donna just sat there on the bed, listening and watching. In her ears rang that woman’s seemingly endless mockery, while before her eyes, the drafts she had poured her heart into were mercilessly torn to shreds."
    scene cg_ep2_3
    "Donna’s fingers lightly tap on the desk— While writing the script just now, she had drifted into memories of those past fragments."
    "Actually, writing stories was what she was best at and what she loved most. Whenever the characters in her writing experienced misfortune, her heart would tremble, as if she could feel their pain."
    "However, her mother’s cold mockery always drew her into a whirlpool of self-doubt."
    scene cg_ep3_3
    "Suddenly, in Donna’s mind appear those lively, energetic girls from the club. Her lips curve slightly upward— "
    "But quickly, this hint of a smile disappears. She lowers her head, her fingers lightly tracing across the desk, still carrying some unease. Perhaps, Lindsey and the others wouldn’t hate her stories…"
    scene cg_ep2_3
    d "…Let me try one more time."
    "And so, the girl picks up her pen and begins outlining her story on blank paper. This is bound to be another sleepless night."
    jump twofour

label twofour:
    $ tb_design = "normal"
    scene bridge
    with dissolve
    play music "<loop 4.58>audio/bgm1ok.mp3"
    "The following day…"
    show lindsey_neutral at left
    with dissolve
    show mackenzie_neutral at right
    with dissolve
    l "Wow, this is my first time meeting senpai Mackenzie in person."
    hide mackenzie_neutral
    show mackenzie_happy at right
    show mackenzie_happy:
        linear 1.2 xalign 0.5 yalign 1.0
    k "No need to be so formal, you can just call me Kenzie like Lili does!"
    l "Okay Kenzie, no problem Kenzie!"
    hide lindsey_neutral
    show lindsey_happy at left
    "Lindsey stamps her foot with a “pa” sound, brings her fingers together in a salute to her temple, and playfully sticks out her tongue. Though her movements are proper, they’re so playful that they are not serious or stiff, instead making it kind of funny."
    k "Wow, that gesture is so cute! Come on, Lili, you do one too~"
    
    show allie_angry at right with dissolve:
        xzoom -1
    show allie_angry at right:
        xzoom -1
        rotate_pad False
        linear 0.2 rotate -45 yalign 1.1
        linear 0.2 rotate 0 yalign 1.0
    "{nw}{p=0.3}"
    hide mackenzie_happy
    show mackenzie_sad:
        xalign 0.5 yalign 1.0
    "Allie directly chops Mackenzie on the head. Mackenzie dramatically clutches her head, pretending to be hurt and complaining."
    k "Ouch! Lili, why do you hurt me both in-game and out—!"
    a "Stop fooling around, didn’t we have something important to discuss today? Donna, how’s your script coming along?"
    hide allie_angry
    show donna_neutral at right
    hide mackenzie_sad
    show mackenzie_neutral
    d "Ah, I was just going to talk about that…"
    l "Wow, is Donnie’s masterpiece finished already! Such high efficiency!"
    d "Yes. But I need everyone’s help with feedback for iterations…"
    "Donna’s voice is very faint, she has no confidence in her own writing at all."
    l "Oh come on, don’t be modest, I’m sure you wrote something amazing! Can we take a look at your story?"
    "​​Lindsey gently patted Donna on the shoulder, but she instinctively moved aside.\nAfter hesitating for a moment, she took out her laptop."
    scene cg_downfly
    with dissolve
    stop music fadeout 1.0
    "Donna’s story is heavy.\nThe title of the story is “Flying Downward”, and it tells the story of…\nA person who took their own life."
    "The story is short, narrating the thoughts of a high school girl as she jumps from a great height, reflecting on her life—\na life that, unfortunately, didn’t contain much happiness."
    "The writing is filled with a stream-of-consciousness flow of questions and accusations.\nThe girl is puzzled by the injustices of society and the frustrations of her life."
    "She doesn’t understand where her father, who frequently stayed out all night, went.\nNor does she understand why her mother always unleashed anger on her, as if she were the source of all the family’s misfortunes."
    "Even more, she doesn’t understand why her quiet personality was seen as a weakness, making her a target for bullying and mockery from her classmates."
    "Eventually, even her peers stopped bothering her—she became someone ignored by everyone."
    "In this solitude and despair, the protagonist develops an unusual thought:\nShe compares the act of falling from a building to “flying downward”.\nIt is described as a state of freedom, without any constraints."
    "In her brief life, this is the first and only time she feels such pure “beauty”."
    "However, the enjoyment of “flying” has an end."
    "The girl’s final thought is:\n“My death will probably look ugly. I hope I won’t trouble the cleaners or disturb the passersby too much…”"
    scene bridge
    show lindsey_sad:
        xalign 0.0
        yalign 1.0
    show donna_neutral:
        xalign 0.33
        yalign 1.0
    show mackenzie_sad:
        xalign 0.67
        yalign 1.0
    show allie_sad:
        xalign 1.0
        yalign 1.0
    "Donna’s story ends abruptly here."
    play music "audio/something2.mp3"
    a "Uh…I don’t really know what to say…"
    show allie_sad:
        linear 0.5 xalign 0.9
        linear 0.5 xalign 1.0
    "Allie looked over at Mackenzie, as if seeking help."
    hide mackenzie_sad
    show mackenzie_afraid:
        xalign 0.67
        yalign 1.0
    k "Don’t look at me; I’m terrible at literature."
    hide allie_sad
    show allie_angry:
        xalign 1.0
        yalign 1.0
    show allie_angry:
        linear 0.5 xalign 0.9
        linear 0.5 xalign 1.0
    "Allie shot Mackenzie a glare, then turned back to Donna and sighed softly."
    hide donna_neutral
    show donna_afraid:
        xalign 0.33
        yalign 1.0
    d "I understand… This piece of writing is just too… overly sentimental, right? I’ll rewrite it."
    "Disappointment wasn’t visible on Donna’s face. She simply pressed her lips together and quickly regained her composure."
    a "Ah, you misunderstood. That’s not what I meant…"
    stop music
    hide lindsey_sad
    show lindsey_angry:
        xalign 0.0
        yalign 1.0
    show lindsey_angry:
        linear 0.5 xalign 0.05 yalign 1.0
        linear 0.5 xalign 0.05 yalign 1.05
        linear 0.5 xalign 0.0 yalign 1.05
        linear 0.5 xalign 0.00 yalign 1.0
    l "What are you saying!"
    play music "audio/inspired.mp3"
    scene cg_ep2_4
    with dissolve
    "Lindsey slams her hand on the table, her voice growing louder, immediately drawing the attention of the three girls in the activity room. Her eyes are slightly red, clearly not calm inside."
    l "But you wrote so well…"
    "Lindsey’s voice carries a hint of choking up, but she firmly continues."
    scene cg_wj_angry
    l "The emotions you put into the story are so strong, and your writing is excellent— It really moved me deeply! Ah, sorry, I might be a bit too excited…"
    "I can’t describe my feelings clearly, but Donnie, you really wrote it well! Don’t doubt yourself! You can be more confident!"
    scene bridge
    show lindsey_neutral:
        xalign 0.0
        yalign 1.0
    show donna_sad:
        xalign 0.33
        yalign 1.0
    show mackenzie_neutral:
        xalign 0.67
        yalign 1.0
    show allie_neutral:
        xalign 1.0
        yalign 1.0
    "Allie now also catches up with Lindsey’s train of thought."
    a "Yes, yes, I think you handled the conflict between the beautiful fantasy and the cruel reality really well. "
    a "The approach to tragedy is also quite unique. From the perspective of “appreciating and understanding tragedy”, it suddenly becomes easy to understand and empathize with that falling girl."
    k "Though I’m not as professional as Lili, and can’t offer very good advice, I also think this script is amazing! Donna, don’t be too hard on yourself."
    hide donna_sad
    show donna_afraid:
        xalign 0.33
        yalign 1.0
    "The expression on Donna’s face suddenly freezes, then turns to surprise and confusion. She tightly presses her lips together."
    d "Is… is that so? Then what else do I need to do…"
    "Donna’s usually calm voice ripples like disturbed water, showing slight rises and falls in tone."
    a "Just keep refining this script, it’s really good! Let’s make our game based on this story. Ken-ken, what do you think?"
    k "Mm, I agree! Let our game creation journey begin from here!"
    jump interlude1

label interlude1:
    $ tb_design = "quyang"
    scene classroom
    with dissolve
    play music "audio/something2.mp3"
    "A few days later…"
    "Monday, 4 PM, the school bell rings.\nUnlike her hurrying classmates, Donna packs her bag slowly.\nShe’s clearly lost in thought."
    d "{i}During the last meeting, the club president mentioned we need to do club activities once a week… {/i}"
    d "{i}Who should I go with today?{/i}"
    d "{i}Hmm… Lindsey mentioned she’d be drawing on the bench in the central garden after school. Going to find her would probably be lively and energetic… {/i}"
    d "{i}But if I go find Mackenzie and Allie, they should be in the computer room preparing for club projects, that might be more relaxed and casual… {/i}"
    d "{i}Which should I choose?{/i}"
    menu:
        "What will Donna choose?"
        "Go to the central garden to find Lindsey":
            $ interludechoice1 = 1
            if add2 == False:
                $ add2 = True
                $ weijiangfriendshippoints += 1
            scene garden
            with dissolve
            play music "<loop 4.58>audio/bgm1ok.mp3"
            "Donna decides to go to the central garden to find Lindsey.\nFrom afar, she sees Lindsey sitting on the garden bench."
            show lindsey_neutral:
                xalign 1.0
                yalign 1.0
            with dissolve
            "She’s holding a pen, contemplating her drawing composition."
            show lindsey_neutral:
                linear 0.5 xalign 1.0 yalign 0.8
                linear 0.5 xalign 1.0 yalign 1.0
            "Seemingly hearing footsteps, Lindsey looks up."
            hide lindsey_neutral
            show lindsey_happy:
                xalign 1.0
                yalign 1.0
                linear 1.0 xalign 0.5 yalign 1.0
            "Upon seeing Donna, she immediately breaks into a radiant smile."
            l "Donnie! What brings you here?\nI was just wondering if I’d see you today, and here you are!"
            "Donna looks up to see excitement sparkling in Lindsey’s bright eyes."
            "She waves at Donna, her smile brimming with undisguised joy."
            "Despite knowing each other for a while now, Lindsey’s unrestrained enthusiasm still catches her off guard."
            "Donna awkwardly lowers her head, Feeling her cheeks grow slightly warm."
            d "I… I just thought this place was closer, that’s all."
            l "That’s perfect then~ We can go to club activities together."
            show lindsey_happy:
                linear 0.5 xalign 0.5 yalign 0.8
                linear 0.5 xalign 0.5 yalign 1.0
            l "Oh right, I brought my instant camera!"
            l "We can take some interesting campus photos along the way, and make them into small posters to hang in the activity room, what do you think?"
            d "…Okay."
            hide lindsey_happy
            show lindsey_neutral
            "Donna feels Lindsey grab her hand, giving it a gentle pull."
            "She finds herself unconsciously following Lindsey’s lead."
            "She sees Lindsey suddenly stop in an open space, her blonde hair seemingly glowing in the sunlight."
            "Lindsey turns around, tilting her head as she looks at her."
            l "How about here? The scenery is nice, let’s take a photo!"
            l "Come on—say cheese~"
            scene garden
            show lindsey_happy at left
            show donna_happy at right
            show frame
            with fade
            "Lindsey took a photo with you together!"
            scene garden
            with dissolve
            show lindsey_neutral
            "Her voice is light and cheerful, carrying a sincerity impossible to refuse."
            "Donna unconsciously breaks into a slight smile."
            l "Donnie, you look really pretty when you smile!"
            l "You should smile more often, don’t always be so reserved."
            d "Okay… I’ll try."
            scene bridge
            with dissolve
            "They make their way to the club activity room, taking photos along the path, and sync up on the game development progress with their two senior members."
            show mackenzie_neutral at left
            show allie_neutral at right
            show lindsey_neutral
            with dissolve
            "Under their influence, Donna gradually relaxes."
            "She begins to enjoy these casual interactions. The ordinary campus life gains a splash of color."
            scene room1
            with dissolve
            "After the fun club activities, Donna returns home with a hint of satisfaction to continue refining her script."
            "A fulfilling week passes by."
            jump interlude2
        "Go to the computer room to meet Mackenzie and Allie":
            $ interludechoice1 = 2
            scene bridge
            with dissolve
            play music "<loop 4.58>audio/bgm1ok.mp3"
            "Donna decides to go to the computer room to find Mackenzie and Allie."
            show mackenzie_neutral at left
            show allie_neutral at right
            "As she pushes open the door, warm light spills in, she sees Mackenzie sitting at the computer typing code, while Allie is wearing headphones, focusing on adjusting a piece of music."
            show allie_neutral:
                linear 0.5 xalign 1.0 yalign 0.8
                linear 0.5 xalign 1.0 yalign 1.0
            hide allie_neutral
            show allie_happy at right
            "Allie seems to sense someone entering, she looks up, removes her headphones, and gives Donna a bright smile."
            a "Donna, you’re here?"
            a "We’re prototyping music for a new scene today, do you want to listen too?"
            "Allie gently waves her hand, gesturing Donna to come closer, then presses the play button."
            "Fresh melodies flow through the computer room, weaving together with keyboard clicks to create a wonderful atmosphere."
            hide mackenzie_neutral
            show mackenzie_happy at left
            k "Lili, this music transitions so well with the scene!"
            k "You always create such amazing things! I love it."
            hide allie_happy
            show allie_neutral at right
            show allie_neutral:
                linear 0.5 yalign 1.3
            a "Stop praising me, you’re making me shy… "
            show allie_neutral at right
            "Though Allie says this, Donna notices her slightly upturned lips and that barely concealed look of pride."
            "Mackenzie pauses her work, turns to look at Allie, her tone as gentle as ever."
            k "That’s because Lili really does excellent work. \nYou deserve all the praise."
            k "Hmm… if I had to make a suggestion, maybe adding more sense of depth to that background music would make it even better? "
            k "I think your style is wonderful, especially those sustained notes in the last few seconds which are perfect."
            a "Okay, I’ll try adjusting it… stop staring at me, it makes me nervous!"
            show allie_neutral:
                linear 0.5 xalign 0.9 yalign 1.0
                linear 0.5 xalign 1.0 yalign 1.0
            show mackenzie_happy:
                linear 0.5 xalign 0.0 yalign 0.9
                linear 0.5 xalign 0.0 yalign 1.0
            "As Allie speaks, she lightly pushes Mackenzie’s shoulder, Mackenzie laughs and shrugs, still not taking her eyes away."
            "Their natural bond and feeling of ease stirs something in Donna’s heart."
            a "Oh right, Donna, how’s your script coming along?"
            d "…Still iterating, but everyone’s suggestions have given me more ideas."
            k "That’s good, don’t feel pressured. Our club atmosphere is meant to be casual, Donna, just do your best."
            hide mackenzie_happy
            show mackenzie_neutral at left
            "The computer room’s light falls over the three of them, time slips away amid keyboard clicks and musical melodies."
            hide allie_neutral
            show allie_neutral
            show lindsey_neutral at right
            with dissolve
            "Shortly after, Lindsey arrives late with her newly drawn CG art and joins the club discussion."
            scene room1
            with dissolve
            "The peaceful club activities come to an end."
            "Donna returns home to continue working on her unfinished script.\nA busy week passes by."
            jump interlude2

label interlude2:
    $ tb_design = "quyang"
    scene classroom
    with dissolve
    play music "audio/something2.mp3"
    "One week later…"
    "It’s the weekly club activity day again… \nWho should I go with today?"
    menu:
        "What will Donna choose?"
        "Go to the central garden to find Lindsey":
            $ interludechoice2 = 1
            if add3 == False:
                $ add3 = True
                $ weijiangfriendshippoints += 1
            scene garden
            with dissolve
            play music "<loop 4.58>audio/bgm1ok.mp3"  
            if interludechoice1 == 1:
                "Donna comes to the central garden again."
                "She’s wondering if Lindsey would be drawing on the bench again."
            else: 
                "Donna comes to the central garden this time."
            show lindsey_happy with dissolve:
                xalign 1.0 yalign 1.0
                linear 0.2 xalign 0.75 yalign 0.3
                linear 0.2 xalign 0.5 yalign 1.0
            "However, before she reaches the garden entrance, a figure suddenly jumps out from behind the bushes."
            l "Donnie! Surprise!"
            l "I’ve been waiting for you for so long!"
            "Donna is startled by Lindsey’s sudden appearance, involuntarily taking a step back."
            "She stares at the proudly grinning Lindsey before her, feeling both helpless and somewhat amused."
            d "You… Why did you suddenly pop out?"
            "Lindsey playfully sticks out her tongue."
            if interludechoice1 == 1:
                l "Hehe, I noticed you were coming later than last time, so I wanted to surprise you!"
            l "Come on, let’s go to club activities~"
            scene bridge 
            with dissolve
            show mackenzie_neutral at left
            show allie_neutral
            show lindsey_neutral at right
            "When they arrive at the club room, Mackenzie and Allie are already engaged in discussing new parts of their game’s narrative."
            "Donna is pulled by Lindsey to join their lively discussion."
            "Her new script receives praise from everyone."
            "She discovers that she’s gradually becoming part of this small group, and begins to enjoy Lindsey’s encouragement and companionship more."
            scene room1
            with dissolve
            "After the club activities, Donna begins preparing the next section for her script, taking the senior students’ new suggestions into account."
            "Such days seem to become the new normalcy."
            "However, unknown to Donna, the attentive Lindsey, seems to be brewing a plan… "
            jump threeone  
        "Go to the computer room to meet Mackenzie and Allie":
            $ interludechoice2 = 2
            scene bridge
            with dissolve
            play music "<loop 4.58>audio/bgm1ok.mp3"
            if interludechoice1 == 2:
                "Donna comes to the computer room again."
                "Today, as always, the room is filled with familiar keyboard clicks and musical melodies."
            else:
                "Donna comes to the computer room this time."
            show mackenzie_neutral at left 
            show allie_neutral at right
            "As Donna opens the door, she sees Allie hunched over the desk, humming a tune while jotting down inspiration, while Mackenzie gently places a warm milk tea in front of Allie."
            show mackenzie_neutral:
                linear 2 xalign 0.8 yalign 1.0
                linear 2 xalign 0.0 yalign 1.0
            k "Lili, don’t tire yourself out, take a break and have something to drink."
            a "Thanks, Kenken. You’re always so thoughtful!"
            hide allie_neutral
            show allie_happy:
                xalign 1.0 yalign 1.0
                linear 0.5 xalign 1.0 yalign 0.8
                linear 0.5 xalign 1.0 yalign 1.0
            "Allie looks up, showing a tired but satisfied smile."
            "Mackenzie’s eyes hold a hint of doting affection."
            "Donna quietly sits down, opens her document, with the sound of their soft conversations in her ears, that harmony brings her unexpected peace."
            hide allie_happy
            show allie_neutral
            show lindsey_neutral at right
            with dissolve 
            "Some time later, a cup of milk tea appears on Donna’s desk too."
            "It’s from Lindsey, who was sketching in the central garden."
            "Everyone discusses together the allocation of the game project’s remaining tasks."
            hide mackenzie_neutral
            hide allie_neutral
            hide lindsey_neutral
            "The game design project progresses steadily.\nSuch days seem to become the new normalcy."
            jump threeone

label threeone:
    $ tb_design = "weijiang"
    scene bridge
    with fade
    play music "audio/something2.mp3"
    "Note: sections with this textbox are played from the perspective of Lindsey."
    "A week later… "
    show mackenzie_neutral at left
    with dissolve
    show allie_neutral at right
    with dissolve
    "The atmosphere in the clubroom is as light-hearted as always, but Lindsey is hunched over at the desk, looking completely distracted."
    k "Hey, Lindsey, why have you been zoning out all day?"
    k "Did CG art wear you out to the point of memory loss?"
    k "Or is it because Donna isn’t here today because of her exam, and you miss her?"
    l "Ah, no, it’s not about game art…"
    l "But I really have been thinking about Donna."
    hide allie_neutral
    show allie_sad at right
    a "It’s because of her script, right?"
    k "Hmm? Lili, you feel the same way?\nI thought about that too."
    k "If the content she wrote is based on real experiences, she must have been under a lot of pressure in her life."
    l "I just feel like… maybe Donna has gone through something really terrible……"
    l "She doesn’t talk much, and her expression is always so cold…"
    l "I always get the sense that she’s keeping her distance from everyone. Could she be going through something difficult?"
    l "But keeping things locked inside, like that, will only make it worse over time, right?"
    hide mackenzie_neutral
    show mackenzie_sad at left
    k "Yeah, wasn’t Lili like that before?"
    k "She used to keep everything to herself, and I could never figure out what she was thinking!"
    hide allie_sad
    show allie_angry at right
    a "Hey, Kenken, stop saying weird stuff…"
    l "Allie, you were like that before too?"
    k "Of course! She used to be really awkward."
    k "She’d bottle everything up and never tell anyone."
    k "It wasn’t until she started talking to the school counselor that she slowly learned to accept other people’s concern. Right, Lili?"
    hide allie_angry
    show allie_sad at right
    a "…Yeah, but that was a long time ago."
    a "I think if there’s someone you can talk to, it really does make things a lot easier."
    k "Lindsey, why don’t you try asking Donna why she wrote this script?"
    k "Sometimes, just having someone willing to listen can make her feel a bit better."
    l "Hmm… I’ll give it a try."
    scene room2
    with fade
    "Later that night, Lindsey sits on the edge of her bed, reflecting on what the seniors had said."
    l "They’re right… Donna probably really needs someone to talk to, but… how do I even bring this up?"
    "She opens her computer, hesitates for a moment, and searches for the psychological counseling services offered by the school."
    "She browses through the information, but each page she clicks makes her hesitation grow deeper."
    l "What if Donna thinks I’m meddling… "
    "Lindsey holds her phone, opens Donna’s chat window, but can’t bring herself to send a message."
    "She sighs and falls back onto her bed."
    l "How do I even say it… "
    jump threetwo

label threetwo:
    $ tb_design = "weijiang"
    scene bridge
    with fade
    play music "audio/something2.mp3"
    "Another day at the club activity room…"
    show donna_neutral
    l "Ah, both of the senpais aren’t here today."
    d "Then I’ll keep working on my script.\nLinnie, do you want to try drawing some concept art?"
    "Lindsey, somewhat absent-minded, stares at the brush in her hand, but her mind is consumed with another question."
    l "Ah… ah, no problem—"
    l "But before that, Donna, I want to ask you…\nWhy did you write such a heavy story?"
    hide donna_neutral
    show donna_afraid
    "Although it feels a bit too direct to ask, once the question left her mouth, Lindsey couldn’t take it back."
    d "Didn’t the seniors suggest basing it on real experiences?\nSo I tried writing about my own story."
    d "—but I did add some artistic adjustments, I haven’t actually jumped off a building yet."
    l "Then… What about the other parts?"
    d "If it’s about my family, those parts are mostly real."
    d "My father really has been messing around with women other than my mother, and my mother… thinks I’m the burden of her failed marriage."
    "Donna speaks in a calm tone, as if she is recounting a story that had nothing to do with her, as if these events had never hurt her."
    l "And school… your classmates… "
    d "My middle school classmates did bully me every day.\nBut they didn’t like me because I didn’t resist."
    d "So after bullying me a few times, they stopped bothering me."
    "Lindsey listens, her heart filled with guilt and pain.\nShe bites her lip, trying hard to suppress her emotions."
    l "Donna… I’m really sorry, I can’t believe I’m hearing this… "
    d "It’s okay, it’s all in the past now, and I’ve gotten used to it."
    l "How can someone get used to something like that?"
    "Lindsey mutters softly to herself. \nDonna doesn’t catch all of it and looks at her, confused."
    hide donna_afraid
    show donna_angry
    d "Did you say something?"
    stop music
    l "How could you possibly get used to something like that!?"
    play music "audio/inspired.mp3"
    scene cg_wj_angry
    "Lindsey suddenly stands up, and the sunset outside shines through her eyes, sparkling like jewels."
    "She slams her hand down on the desk, unable to hold back her emotions anymore."
    scene cg_ep3_2_01
    "Donna stares at Lindsey, slightly stunned, as if her sudden outburst has caught her off guard."
    "But she quickly recovers, her face showing confusion."
    d "Lindsey, why are you crying? Are you okay? Do you need a tissue?"
    l "Why are you comforting me? It should be me comforting you…"
    l "—you’re the one who’s been hurt… why aren’t you upset?\n—How can you speak so calmly about all of this?"
    scene cg_ep3_2_02
    "Donna pauses for a moment before handing her a tissue.\nShe then spoke in that calm voice again."
    d "I don’t think there’s anything to be upset about.\nThese things are just things that happened to me."
    l "But… but you can’t just bottle it all up!"
    l "I think maybe you should talk to a counselor… "
    scene bridge
    show donna_angry
    "Lindsey tentatively suggests this, but she doesn’t expect her words to land like a sharp thorn, deeply embedding itself in Donna’s heart."
    d "A counselor…?"
    show donna_angry:
        linear 0.5 xalign 0.5 yalign 0.8
        linear 0.5 xalign 0.5 yalign 1.0
    d "Lindsey… Do you think I’m “sick” like my mother does?"
    l "No! That’s not what I meant!"
    l "I just think… if there’s someone who can listen to you, it might make things a little easier… "
    d "Does it really help?\nTalking to someone doesn’t make all these things disappear."
    "Donna’s tone is calm, but there is a distance in her words that left Lindsey unsure of how to respond."
    l "That’s not what I meant… I just want… I just want you to be okay… "
    d "I’m fine, really.\nLindsey, you don’t have to make my problems your responsibility."
    d "Sometimes, your concern… makes me feel a little burdened."
    "The air is thick with heavy silence.\nLindsey lowers her head, unable to say a word."
    "She feels as though an invisible but thick wall has formed between her and her friend across the table."
    hide donna_angry
    show donna_sad
    d "It’s getting late, we should head home."
    hide donna_sad
    with dissolve
    "Lindsey looks up, watching Donna’s retreating figure, her hand reaches out, but she doesn’t call out to her."
    "The distance between them seems to grow just a little more."
    jump threethree

label threethree:
    $ tb_design = "quyang"
    scene cg_sleep
    with fade
    play music "audio/something2.mp3"
    "Late into the night, the young girl on the bed still hasn’t fallen asleep."
    d "Of course I couldn’t get used to it… "
    "Donna had lied. She simply didn’t want to show her vulnerable side to her friends. Besides causing them unnecessary sadness, it wouldn’t serve any purpose. So in her bedroom, the only place where she was allowed to cry, Donna weeps silently."
    "She curls up alone, trying her best not to make any noise. After all, she might disturb the neighbors."
    stop music fadeout 2.0
    play music "audio/inspired.mp3"
    "It’s not that Donna hasn’t tried to fight against reality, but she was so powerless in the face of fate. She couldn’t mend her broken family, nor could she change the way her classmates ostracized her."
    "But at least she got into a decent high school. She hoped her life might take a turn for the better here."
    scene cg_ep3_3
    "Suddenly, the image of that blonde girl appeared in her mind."
    d "Linnie…"
    "Actually, she really appreciated Lindsey’s concern, but was afraid of causing her trouble."
    d "Linnie… I’m sorry… "
    scene cg_sleep
    "Donna apologizes softly as tears silently roll down her cheeks. Remembering Lindsey’s disappointed expression from that afternoon makes her heart ache as if pricked by a needle."
    "Since starting high school, Lindsey made her feel the warmth of friendship for the first time. But this also made her afraid - afraid she would destroy everything."
    d "If only things could stay like this forever…"
    "She knows these words were just wishful thinking. For her, happiness is like a mirage that could vanish at any moment. She is someone destined not to deserve happiness."
    d "But… Everyone is still by my side."
    "At least for now, just for this moment… Perhaps she has the right to smile as well?"
    jump threefour

label threefour:
    $ tb_design = "weijiang"
    scene room2
    with fade
    play music "audio/school2.mp3"
    "It is late at night, but Lindsey can’t sleep. She tosses and turns, her mind filled with Donna’s cold expression from that afternoon. Looking through her phone contacts, Lindsey hesitates before finally dialing Allie’s number."
    scene cg_ep3_4
    a "Hello, Lindsey? It’s so late, is something wrong?"
    l "Senpai… I’m sorry for disturbing you at this hour. But… I really don’t know who else to talk to about this."
    a "Don’t worry, take your time."
    "Lindsey takes a deep breath and recounts her conversation with Donna from that afternoon. Her voice is filled with regret as she finishes."
    l "When I mentioned the therapist, Donnie… She seemed very angry, and said my concern felt like a burden to her… Senpai, did I do something wrong?"
    "Her question is met with a long silence. After a while, Allie mumbles."
    a "So she’s been through something like that too… "
    "Before she could finish, Lindsey’s voice cut in. She seems anxious and hasn’t noticed the detail in Allie’s words."
    l "Senpai… I’m sure Donnie isn’t as indifferent to these things as she pretends to be… She must be feeling hurt! She’s just putting on a brave face because she doesn’t want to burden me with her negative emotions… "
    k "Lindsey, calm down!"
    l "Eh? Senpai Mackenzie, you’re there too?"
    k "Yes, I’ve been listening. Don’t blame yourself too much. Your concern was right, but maybe you were too hasty."
    k "Sometimes, when a friend is struggling, they don’t need you to solve their problems. They just need to know you’ll be there supporting them, waiting until they’re ready to take that step themselves."
    a "Yes, Lindsey, take it slow. She needs time, and she needs to feel your patience."
    l "Time… and companionship… "
    scene room2
    with dissolve
    "After hanging up, Lindsey lies in bed, a new understanding forming in her mind."
    l "Donnie, I understand now… I shouldn’t have gotten so emotional and made you feel like my concern was a burden. I need to convey my feelings to you more clearly."
    jump threefourpointfive

label threefourpointfive:
    $ tb_design = "normal"
    scene bridge
    with fade
    stop music fadeout 1.0
    show lindsey_neutral at left
    with dissolve
    show donna_neutral at right
    with dissolve
    "A few days later, after club activities ended, Lindsey gathers her courage and called out to Donna, who was packing her bag in the empty activity room."
    l "Donnie… wait a moment, I have something to tell you."
    d "What is it?"
    play music "audio/something2.mp3"
    hide lindsey_neutral
    show lindsey_sad at left
    l "About that day, I’m sorry… I didn’t mean to make you feel like my concern was a burden, I just… I was just too hasty. I didn’t consider your feelings."
    "Lindsey lowers her head, fingers tightly clasped, her voice filled with deep regret and self-reproach."
    hide donna_neutral
    show donna_sad at right
    d "…Linnie, you don’t need to apologize."
    l "No, I must apologize. I just want you to know, whether you want to talk about it or not, I’ll be here with you. You don’t have to bear everything alone, really… "
    hide donna_sad
    show donna_afraid at right
    "Hearing these words, Donna’s hand tightens on her bag strap. Lindsey’s voice is soft, but it stirs complex emotions in her heart."
    d "{i}Why does she go to such lengths… She’s always so unconditionally kind to me… Do I really deserve to be treated this way?{/i}"
    "She remembers their argument in the activity room and her cold words that day. She doesn’t want to drag Lindsey down, but those suppressed emotions have been bottled up for too long, and she ended up hurting her friend."
    "If she accepts her apology now, would she continue to be a burden?"
    jump thechoice

label thechoice:
    $ tb_design = "quyang"
    stop music
    play sound "audio/heartbeat.wav"
    scene bridge
    with fade
    show lindsey_neutral
    with dissolve
    menu:
        "Will you accept Lindsey’s apology?"
        "Reject":
            stop sound
            stop music
            "Silence falls over the activity room. Donna lowers her eyes, shoulders her bag, and speaks with a hint of distance in her voice."
            hide lindsey_neutral
            show lindsey_sad
            d "Thank you, but… I really don’t need this. Linnie, you’re too kind, but I’m not worth it."
            "With that, she turns and leaves, leaving a crestfallen Lindsey standing frozen in place. \nThe distance between them would never close again."
            jump badending
        "Accept":
            if weijiangfriendshippoints >= 2:
                stop sound
                jump threefive
            else:
                stop sound
                "After a moment of silence, Donna finally nods."
                d "…Thank you, Linnie. I’ll try to accept your kindness."
                "Her tone is still somewhat distant, but there is a hint of softening. Their relationship has eased somewhat, but perhaps it is not enough to make much difference."
                jump badending

label threefive:
    $ tb_design = "normal"
    scene bridge
    with dissolve
    show lindsey_sad at left
    show donna_sad at right
    play music "audio/inspired.mp3"
    "Donna’s gaze trembles slightly. She puts down her bag and speaks softly."
    d "I should be the one apologizing… I’m sorry, Linnie. I shouldn’t have treated you that way. Actually, I really appreciate your concern, it’s just… I was afraid of being a burden to you."
    "Lindsey is stunned for a moment, then breaks into her characteristic cheerful smile."
    l "Donnie, how could you think like that! You’ll never be a burden to me, you’re my best partner! Whenever you need me, I’ll always be here for you!"
    l "As long as you need me, I’ll always be here for you!"
    show donna_sad:
        linear 0.5 xalign 1.0 yalign 1.1
        linear 0.5 xalign 1.0 yalign 1.0
    "As Donna listens to these words, a flicker of faltering passes through her eyes."
    d "I… It’s not that I don’t want to trust you.\nBut I’m afraid… I’m afraid……"
    "Her voice gets lower and lower, as if she’s afraid that her weakness will be seen through."
    hide lindsey_sad
    show lindsey_neutral:
        xalign 0.0 yalign 1.0
        linear 1.5 xalign 0.4 yalign 1.2
    "Lindsey, however, steps forward and bends down, trying to meet her eyes."
    l "Donnie, why are you afraid?\nYou can tell me if you want to.\nI’m listening, always."
    d "I’m afraid… that I’ll let you down.\nI’ll make you feel sorry for me.\nYou’re so nice, and everyone in the club… "
    d "But I always make everyone worried… \nI’m the one who should have to bear these things. I’m used to it.\nI don’t want them to affect your emotions anymore."
    show donna_sad:
        linear 0.5 xalign 1.0 yalign 1.2
    "Her voice gradually chokes up, eventually reaching a point where she can’t keep speaking anymore."
    hide lindsey_neutral
    show lindsey_sad:
        xalign 0.4 yalign 1.2
    "Lindsey looks at her, feeling a deep ache in her heart."
    l "Donnie, How could that be? \nWhat I say next may be a bit presumptuous.\nIf anything makes you uncomfortable, please tell me—it’s okay."
    l "You might think the unpleasant things you’ve experienced were meant to happen to you.\nBut I believe—"
    l "Donnie, you’re a wonderful girl. You shouldn’t have gone through all that."
    d "But in reality, these things did happen. I’m used to it… \nMy misfortune—if it even counts as that… "
    d "I don’t think it matters much.\nIt’s just something I objectively experienced."
    l "Donnie, do you know?\nYou are worthy of being loved."
    "Donna freezes. It takes a few seconds for her to raise her head again.\nAfter a few seconds, she slowly looks up, her voice less composed."
    show donna_sad:
        linear 1.5 xalign 0.6 yalign 1.2
    d "Of course, I know. You don’t need to tell me that… "
    l "Donnie, you…you can try crying in front of me."
    l "I’ll always be here for you."
    scene cg_ep3_05_qy
    with dissolve
    d "……Wouldn’t this just trouble you?"
    "Donna’s eyes were already turning red from her sadness. Because of this, she didn’t notice the glimmer of tears in Lindsey’s eyes."
    l "Why say that? We’re friends, aren’t we? I’ll help you."
    "Two tears roll down Donna’s cheeks, as if emotions buried for a long time had finally found an outlet. She hastily reaches up to wipe them away, but the tears won’t dry. Panicking, the girl stands up."
    d "Sorry for not behaving myself. Could you leave me alone for a while?"
    scene cg_embrace
    with fade
    "She stands up, trying to escape, to hide her vulnerability. But just as she was about to turn away, she felt a pair of warm hands gently wrap around her."
    stop music fadeout 1.0
    l "It’s okay to cry right here. I’ll protect you."
    play music "audio/HE.mp3"
    "The two embrace tightly. Lindsey can’t see Donna’s face, but she can feel the girl’s head slightly leaning on her shoulder, gradually sinking lower, becoming heavier."
    "As the sobbing grows louder, the heart that has always pretended to be strong finally lays down its defenses."
    d "Why are you saying such silly things… What do you understand?"
    l "I’m sorry. Maybe I don’t understand you enough yet.\nPerhaps I was being presumptuous, thinking I could help you escape from this pain."
    l "—But I’ll do my best to help you. Trust me, okay?"
    l "I’m willing to face these difficulties with you and take small steps at a time to change things."
    l "Donnie, no matter what happens, I’ll always be there to support you.\nYou’ll never have to face things alone anymore."
    "The sound of one person’s crying gradually turns into a duet. At that moment, the weight of emotions fill the room, binding two hearts that had once been separated by heavy barriers tightly together."
    jump goodending

label badending:
    $ tb_design = "normal"
    scene bridge
    with fade
    play music "audio/BE.mp3"
    "One month later."
    "The club room feels emptier these days. Though people still gather here, something essential seems missing."
    show allie_sad at left
    with dissolve
    show lindsey_sad
    with dissolve
    show mackenzie_sad at right
    with dissolve
    a "Has anyone heard from Donna lately? She hasn’t been to club activities in weeks… "
    "Lindsey stares at her unfinished character illustrations, her usual energy noticeably dampened."
    scene cg_goodend
    with dissolve
    l "She… she still comes to school. I see her sometimes in the hallway, but… "
    scene cg_badendalt
    with fade
    k "But?"
    l "She always turns away when she sees me. Like she’s trying to avoid everyone… "
    "The room falls into uncomfortable silence. On the computer screen, Donna’s last script remains open - a story about a girl who chose solitude over the pain of connection."
    a "Maybe we should try talking to her again?"
    l "I’ve tried… She just says she’s busy with the honors classes. That she needs to focus on her studies… "
    k "(sighing softly) Sometimes people aren’t ready to be helped, no matter how much we want to reach out."
    scene classroom
    with dissolve
    show donna_afraid:
        xalign 1.0 yalign 1.0
        linear 3.0 xalign 3.0 yalign 1.0
    "{nw}{p=0.25}"
    hide donna_afraid
    with dissolve
    show lindsey_sad at left
    "Lindsey spots a familiar figure at the end of the hallway - Donna, walking alone as always. \nBefore she can call out, Donna notices her and quickly turns down another corridor."
    show lindsey_sad:
        linear 0.5 xalign 0.3 yalign 1.0
        linear 0.25 xalign 0.2 yalign 1.0
    "Lindsey takes a step forward, then stops. Her hand, half-raised in greeting, slowly falls to her side."
    scene game1
    with dissolve
    show wj_game at left
    with dissolve
    show wz_game
    with dissolve
    show lf_game at right
    with dissolve
    "That evening, three characters gather by the crystal - a red-haired catgirl, a pink-haired knight, and a white-haired dragon girl. The fourth character, a black-haired elf, hasn’t logged in for weeks."
    "The friend list shows “Yurina - Last Online: 32 days ago”"
    lg "I guess this is what she wanted… to go back to being alone."
    ag "The game design club will still continue. We can… find another writer."
    kg "Yeah… we’ll keep going."
    "But everyone knows it won’t be the same. Their small circle had briefly drawn in someone who had always been alone. For a moment, it seemed like they might help her change."
    "Instead, she chose the familiar comfort of isolation over the risk of being hurt again."
    scene classroom
    with fade
    "One week later."
    show lindsey_sad
    with dissolve
    "During lunch break, Lindsey notices Donna’s desk is empty. A classmate mentions she transferred to another class - one focused on advanced studies."
    "Lindsey pulls out her phone, opening their chat history. Their last conversation remains unchanged - Donna’s final message simply reads: “Sorry, I need to focus on my studies. Please don’t worry about me.”"
    "Lindsey begins typing: “I miss you. We all miss you. Please come back…”"
    "But after staring at the words for a long moment, she deletes them without sending."
    stop music fadeout 4.0
    "Some distances, once created, become too wide to cross."
    scene unitedbackground
    with fade
    "The end."
    return

label goodending:
    $ tb_design = "normal"
    scene classroom
    with dissolve
    "Ever since that day in the club’s lab where she confessed her feelings to Lindsey, Donna gradually begins to open her heart."
    show lindsey_neutral at left
    with dissolve
    show donna_neutral at right
    with dissolve
    "With Lindsey’s support, she courageously reports the bullying incidents in her class to the teachers."
    "The bullies are given serious punishments and apologize to Donna."
    "Though the past can’t be changed, in that moment, Donna feels a long-lost sense of relief, and the darkness of years of repression finally dissipates."
    scene room1
    with dissolve
    "Encouraged by Lindsey, Donna also tries to reconcile with her mother. With the help of counseling and mental health therapies, she gradually adjusts her mindset and takes the first steps towards peace."
    show mrsqu at left
    with dissolve
    show donna_happy at right
    with dissolve
    "During an ordinary dinner, Donna’s mother quietly places a piece of Donna’s favorite meal on Donna’s plate and softly says: “Mommy shouldn’t have been so harsh. Mommy just wanted you to reach happiness.”"
    "At that moment, Donna’s eyes are filled with tears. She realizes that while challenges would still lie ahead, she is no longer alone."
    scene cg_goodend
    with fade
    "The successful release of their game brings joy to the entire club."
    "Donna’s script resonates with many players, Lindsey’s art is vivid and colorful, Allie’s music and Mackenzie’s programming makes the work complete and captivating."
    "The team cheers and celebrates this hard-earned victory, brimming with anticipation for their next project. Looking at the smiles on everyone’s faces, Donna feels a warm current in her heart."
    "For the first time, she experiences such a genuine sense of belonging—a group of supportive and hardworking partners who would always stand by her. "
    "As everyone discusses their plans for the next project, Donna feels she is truly ready for both the challenges and the fun to come."
    "This story, like an Easter egg in a game, becomes one of the most unforgettable treasures of her life."
    scene unitedbackground
    with fade
    "Here marks the end of the story of Unique Gaming Girls - Reloaded Edition.\nIf this story touched your heart at any moment, then that is its truest influence."
    "Producer: Juehe\nCreative Director: KoliQed\nStory: Yan Chen (Rain), Kevin Chen"
    "Art: Amy Ding, Gabrielle Dela Cueva, Yaxuan Teng, Wendy Zeng, Akihi\nMusic & Sound: KoliQed, FallingStars, Ashlyn Dai, ProfBrian\nProgramming: KoliQed, Juehe"
    "UI and Background Edits: Juehe\nQuality Assurance: Allen Yang\nTranslation and Miscellanous: Jannie Wang, Kevin Chen, CJ Cortes, Juehe"
    "Special Thanks to: \nThe original Unique Gaming Girls developing team\nAll support from RDFZ Game Design, Show’s Chance and Dimensional Lab\nPlaytesters at USC Games"
    "And YOU playing our game!"
    

    return
    

    



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
    
    "Qu Yang walks to the school\’s central park (1st time)"
    "What will Qu Yang do?"
    menu:
        "What will you do"
        "Chat with Lindsey at the teaching building":
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
    
    "Qu Yang walks to the school\’s central park (2nd time)"
    "What will Qu Yang do?"
    menu:
        "What will you do"
        "Chat with Lindsey at the teaching building":
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
    "Qu Yang walks to the school\’s central park (3rd time)"
    "What will Qu Yang do?"
    menu:
        "What will you do"
        "Chat with Lindsey at the teaching building":
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