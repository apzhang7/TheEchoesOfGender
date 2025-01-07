# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#Isabella - polite but will react when not a man 
define i = Character("Innkeeper Isabella")

#Bruce - blunt bordering rude - only polite with transgender men and cis-men
define b = Character("Blacksmith Bruce")

#Alexis - normal overall but will try to recruit only cis-women
define a = Character("Alchemist Alexis")

#Maxwell - is kind and accepting but will give gendered compliments
define m = Character("Merchant Maxwell")

#Glo - will be kind and courteous regardless of gender
define g = Character("Gatekeeper Glo")

#You
define you = Character("You")


init:
    image bg citygate = Image("citygate.png")
    image bg citygateNight = Image("citygateNight.png")
    image bg street = Image("street.png")
    image bg streetNight = Image("streetNight.png")
    image bg inn = Image("inn.png")
    image bg innNight = Image("innNight.png")
    image bg blacksmith = Image("blacksmith.png")
    image bg blacksmithNight = Image("blacksmithNight.png")
    image bg alchemist = Image("alchemist.png")
    image bg alchemistNight = Image("alchemistNight.png")
    image bg merchant = Image("merchant.png")
    image bg merchantNight = Image("merchantNight.png")


    image isabella = Image("isabella.png")
    image isabella sad = Image("isabella sad.png")

    image bruce = Image("bruce.png")
    image bruce mad = Image("bruce mad.png")

    image alexis = Image("alexis.png")
    image alexis argue = Image("alexis argue.png")

    image maxwell = Image("maxwell.png")

    image glo = Image("glo.png")
 
    default easy = False
    default medium = False
    default hard = False
    default transman = False
    default transwoman = False
    default night = True
    default innDone = False
    default blacksmithDone = False
    default alchemistDone = False
    default merchantDone = False
    default complete = False
    default nightTime = True
    default bruceDeny = False
    default visits = 0



# The game starts here.

label start:

    #the intro

    scene bg citygateNight
    with fade

    $ renpy.music.play("audio/medieval.mp3", loop = True, relative_volume = 0.2)

    "On a mission from the adventurer's guild to slay a monster, you arrive at the gates of Osnia." 
    "It's a large sprawling city that dwarfs any town you've ever seen."

    "The journey here has been cruel, and most of your gear is lost or beyond repair." 
    "You're relieved to finally reach safety, but you can't continue like this."

    scene bg streetNight
    with fade
    "As you step into the bustling streets of Osnia, you realize you need to gather gear in this city before venturing into the wilderness." 
    "A mental checklist forms in your mind:"

    jump introExplanation

    label introExplanation:

        scene bg innNight
        with fade
        "First, find the Inn. A good night's rest is crucial and nothing else is open."

        scene bg blacksmithNight
        with fade
        "In the morning, visit the Blacksmith. Without proper armor and a weapon, you won't last long against any monsters."

        scene bg alchemistNight
        with fade
        "Next, the Alchemist's shop. Health potions and herbs could mean the difference between life and death in the wilderness."

        scene bg merchantNight
        with fade
        "Then, seek out the Merchant. Food provisions and other necessities are essential for the journey ahead."

        scene bg innNight
        with fade
        "After, go back to the Inn. Let the Innkeeper know you will be going."

        scene bg citygateNight
        with fade
        "Finally, return to the Gatekeeper. Only after you've gathered all you need will they allow you to continue your mission."

        scene bg streetNight
        with fade
        "A good warrior is one that prepares thoroughly after all." 

    menu:
        "So are you ready?"

        "Yes! Let's get started.":
            jump difficultyIntro

        "No. What do I do again?":
            jump introExplanation



    # selects gender identity (which determines difficulty)
    label difficultyIntro:
        "Unfortunately, in this fantasy world, your gender identity determines the dialogue required for your adventure."
        "Currently there are a total of 3 levels of difficulty in this game:"
        jump difficultyChoose


    label difficultyChoose:
        scene bg streetNight
        menu:
            "What will it be?"

            "Easy - Cisgender Man":
                menu:
                    "You choose Easy - Cisgender Man, are you sure?"
                    
                    "Yes!":
                        $ easy = True
                        jump nightMap
                    "No.":
                        jump difficultyChoose
                

            "Medium - Cisgender Woman":
                menu:
                    "You choose Medium - Cisgender Woman, are you sure?"
                    
                    "Yes!":
                        $ medium = True
                        jump nightMap
                    "No.":
                        jump difficultyChoose

            "Hard - Transgender":
                menu:
                    "You choose Hard - Transgender. Please know the dialogue only slightly differs. Which one?"
                    
                    "Transgender Man":
                        menu:
                            "You choose Hard - Transgender Man, are you sure?"
                    
                            "Yes!":
                                $ hard = True
                                $ transman = True
                                jump nightMap
                            "No.":
                                jump difficultyChoose

                    "Transgender Woman":
                        menu:
                            "You choose Hard - Transgender Woman, are you sure?"
                    
                            "Yes!":
                                $ hard = True
                                $ transwoman = True
                                jump nightMap
                            "No.":
                                jump difficultyChoose


    #the map menu for places to go
    label nightMap:
        scene bg streetNight
        $ nightTime = True
        menu:
            "Where to?"

            "The Inn.":
                "You head to the Inn to rest."
                jump innIsabella
            "The Blacksmith.":
                scene bg blacksmithNight
                if (blacksmithDone == False) and (bruceDeny):
                    jump blacksmithBruce
                else:
                    "They are closed. Go to the inn first and wait for morning."
                    jump nightMap
            "The Alchemist.":
                scene bg alchemistNight
                "They are closed. Go to the inn first and wait for morning."
                jump nightMap
            "The Merchant.":
                scene bg merchantNight
                "They are closed. Go to the inn first and wait for morning."
                jump nightMap
            "The Gate.":
                scene bg citygateNight
                "They are closed. Go to the inn first and wait for morning."
                jump nightMap

    #the map menu after first night is unlocked
    label map:
        scene bg street
        menu:
            "Where to?"

            "The Inn.":
                jump innIsabella
            "The Blacksmith.":
                jump blacksmithBruce
            "The Alchemist.":
                jump alchemistAlexis
            "The Merchant.":
                jump merchantMaxwell
            "The Gate.":
                jump gatekeeperGlo
            "Wait for night.":
                $ visits = visits + 4
                "You have waited for night to come, perhaps it is because you need something at night?"
                jump interactionDone


    #determines the map + night time
    label interactionDone:
        if visits > 3:
            $ nightTime = True
            jump nightMap
        else: 
            jump map

    
    #beginning of actual game with interactions after difficulty choices
    label innIsabella:
        if nightTime:
            scene bg innNight
            with fade
        else: 
            scene bg inn
            with fade

        if (innDone == False) and nightTime:
            show isabella

            i "Hello! Welcome to Osnia's Inn, I am Isabella the Innkeeper. What can I do for you?"
            you "I'd like a room for the next few nights, I plan on staying in the town for a guild quest."
            you "I am to kill the Crazed Boar outside the town."

            if easy:
                i "Of course! I can do that for you sir, this inn holds lots of adventurers like you!"

            elif medium:
                show isabella sad
                i "Oh! The Crazed Boar quest went to you?"
                you "What does that mean? The quest was assigned to me."
                i "It's cause you're a little lass like me! I was just surprised to see a female warrior."
                show isabella
                i "I bet you're really strong if the quest was assigned to you! Good luck to you then!"

            elif hard:
                i "Yes... Sorry should I refer to you as sir or miss?"
                menu: 
                    "What does it matter?":
                        show isabella sad
                        i "You're right, where are my manners I am sorry."
                    "It's fine, just refer to me however you like.":
                        if (transman):
                            i "Okay sir!"
                        else:
                            i "Yes ma'am!"
                        

            i "Here's the key for room 204, it's up those stairs and to the left."
            $ innDone = True
            hide isabella

        elif (innDone and blacksmithDone and alchemistDone and merchantDone) and (complete == False):
            show isabella
            $ complete = True
            i "Oh, welcome back! Are you done collecting all your gear?"
            you "Yes, I will head out now."
            if nightTime:
                i "That will not do! The gatekeeper won't even let you go this late."
                i "I will save room 204 for when you come back so don't worry."
                hide isabella

            else:
                i "Good luck with the Crazed Boar! I will save room 204 for when you come back."
            hide isabella
            "..."
            "You are all ready, head to the Gatekeeper!"
        else:
            "There is nothing you need here right now."

        if (nightTime):
            "..."
            "You have rested for the night!"
            $ nightTime = False
            $ visits = 0

        jump interactionDone




    label blacksmithBruce:
        if nightTime:
            scene bg blacksmithNight
            with fade
        else: 
            scene bg blacksmith
            with fade

        if (nightTime) and (bruceDeny):    
            show bruce mad
            b "Oh it's you. Took you long enough."
            b "This is the only time we will do any business. Got that?" 
            b "Now scram. Get out of my store."
            $ bruceDeny = False

        elif (blacksmithDone == False) and (bruceDeny == False):
            show bruce

            b "This is the blacksmith, what do you want?"

            if (nightTime == False):
                if (easy or (hard and transman)):
                    b "Oh, a warrior! The name's Bruce."
                    b "What can I forge for you, brother? I have swords and shields of all kinds!"
                elif medium:
                    show bruce mad
                    b "Oh a woman? You sure you in the right place? The dress shop is down the street. Don't waste my time."
                
                if hard:
                    show bruce mad
                    b "...wait what are you supposed to be? Look, I don't have time for this. State your business or leave."
                    $ bruceDeny = True

                you "I need armor and a weapon for my quest to slay the Crazed Boar."
                show bruce

                if easy:
                    b "Alright, I will see what we can do for you."
                elif medium:
                    b "Armor? For the little lady?"

                    menu:
                        "This little lady will let the guild know the next sentences you say so watch yourself.":
                            show bruce mad
                            b "Alright fine let's get you a weapon. But are you sure you can handle the weight?"
                        "I am not a little lady. But yes, armor and a sword.":
                            b "Haha, but are you sure you can handle the weight?"

                    you "..."
                    show bruce
                    b "I am just joking girlie. The name's Bruce." 
                    b "Hmm, how about this pink short sword?"
                    you "Give me the regular one."
                    b "You've got bad taste lassie."
                
                else:
                    show bruce mad
                    b "Come here at night. Leave now, if you wanna get a weapon at all later."
                    $ bruceDeny = True
                    $ visits = visits + 2
                    hide bruce
                    "..."
                    "You have obtained: nothing."
                    jump interactionDone


        if ((blacksmithDone == False) and ((easy) or (medium))):
            hide bruce
            "..."
            "You have obtained: SWORD and IRON ARMOR!"
            $ blacksmithDone = True
            $ visits = visits + 1
        elif ((blacksmithDone == False) and (hard and (bruceDeny == False))):
            hide bruce
            "..."
            "You have obtained: SWORD and LEATHER ARMOR!"
            $ blacksmithDone = True
            $ visits = visits + 1
        elif (bruceDeny and (nightTime == False)):
            "There is nothing you need here right now. Wait till night comes."
        else:
            "There is nothing you need here right now."
        
        jump interactionDone
        


    label alchemistAlexis:
        if nightTime:
            scene bg alchemistNight
            with fade
        else: 
            scene bg alchemist
            with fade

        if alchemistDone == False:
            show alexis

            a "Welcome to my shop of wonders! I am Alexis. How may I assist you today?"
            you "I need health potions and the usual herbs for a quest."
            a "Certainly! Always good to be prepared."

            if medium:
                a "You know, we're always looking for more women in alchemy. Have you ever considered a career change?"
                you "I'm here as a warrior. I was dispacted to slay the Crazed Boar."
                show alexis argue
                a "But alchemy would really suit you! You should give it a try."
                you "I have tried it, I am awful at it."
                a "That's only because you haven't met the right alchemy teacher!"
                you "..."
                show alexis
                a "Well, the offer stands if you change your mind!"
            elif (hard and transwoman):
                show alexis argue
                a "You know, we're always looking for more women in alchemy... nevermind."
                you "I'm here as a warrior, but what made you change your mind?"
                a "You're just not..."
                show alexis
                a "It's nothing. I just saw your potential as a warrior."
            
            a "Anything specific you're looking for?"
            you "I would like two health potions and one poison antidote please."
            a "Coming right up!"

            hide alexis
            "..."

            "You have obtained: POTIONS and POISON ANTIDOTE!"

            $ alchemistDone = True
            $ visits = visits + 1

        else:
            "There is nothing you need here right now."

        jump interactionDone


    label merchantMaxwell:
        scene bg merchant
        with fade

        if (merchantDone == False):
            show maxwell

            m "Hello there! I am Maxwell the Merchant. What can I get for you today?"
            you "I need food provisions and a new water satchel for my quest."

            if easy:
                m "Of course, sir!"
            elif medium:
                m "Certainly, miss! It's so brave of you to go on such a dangerous quest. Your husband must be so proud!"
                you "..."
            elif hard and transman:
                m "Absolutely! You're quite the handsome young man, aren't you?" 
                m "I bet the ladies love a brave warrior like yourself!"
            elif hard and not transman:
                m "Of course, sir! Oh, I'm so sorry, I meant ma'am! Or... um, what would you prefer?"
                you "Ma'am please."

            m "Okay! Let me put together a package for you."

            if hard and not transman:
                m "I am sorry about the mixup, I have put in some extra snacks as an apology."

            hide maxwell
            "..."

            "You have obtained: FOOD and WATER SATCHEL!"

            $ merchantDone = True
            $ visits = visits + 1

        else:
            "There is nothing you need here right now."

        jump interactionDone


    label gatekeeperGlo:
        scene bg citygate
        with fade
        show glo

        g "Halt. State your business."
        you "I'm here for my quest."
        g "I see. Have you prepared for your journey?"
        
        if complete:
            you "Yes, I've gathered supplies from the town."
            g "Your courage is admirable, regardless of who you are."
            g "May fortune favor you on your quest."
            g "The gate is now open. Be cautious and come back in one piece."
            hide glo

            "..."
            "You have obtained: EVERYTHING!"
            "And so, your adventure truly begins..."
            "THE END"
        else:
            you "No, I have not finished."
            g "On with it then, come back when you are finished."
            jump interactionDone


    return