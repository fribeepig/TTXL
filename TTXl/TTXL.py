#Transtextual, Ver 1

#imported utilities
import textwrap
import string
import sys
import array
import random

#Actual game scenes

def start_game(): #Opening Description
    sg01 = "You are 21, you are living in a mid-sized midwestern town, same one you've always lived in actually. It's November, your university " \
    "will be starting back up again tomorrow after a short break, you don't have any friends in town, but you've decided that you can't just let " \
    "life pass you by. To this end you left your phone at home today, you don't expect anyone will notice, it's not like there's anyone who might " \
    "text. You know that you're not exactly comfortable with silence, so you've loaded up an old mp3 player with music. Today is suppposed to be " \
    "cold, but hopefully not so cold you'll find yourself completely isolated."
    print(textwrap.fill(sg01,width))
    hand.pop(0)
    add_item('jacket',1)
    add_item('mp3_player',1)
    pause()
    cursce.pop(0) 
    cursce.insert(0,scene_1)
    scene_1()

def scene_1():
    s101 = "Looking up into the cup {you} see the final swig of coffee disappear beneath your nose, the light brown liquid is run through with " \
    "dark splotches of syrup not fully mixed in to the beverage. You aren't certain of the time, and you intend to keep it that way for " \
    "as long as possible. " \
    "Downing the specialty drink, the phrase \"slemming coffee\" springs to your mind, in the way personal memetics always do. As you set it " \
    "on its plate the white porcelain lets out a solid clink. You are sitting in your favorite local cafe, officially its name is \"Racy " \
    "D'lenes Coffee Lounge\", but ever since you were introduced to it, you've only ever called it {Racy's}. You are sitting by the bay " \
    "windows that make up much of the cafe's front, at your usual {table}."
    print(textwrap.fill(s101,width))
    while True:
        s102 = "You can feel the caffeine slowing you down, sort of like your head is filling with that back of the throat weight that " \
        "comes with a deep yawn. You regret having not ordered your drink with decaf. Though it occurs to you to wonder if that would have even " \
        "been an option."
        print(textwrap.fill(s102,width))
        action = input("> ").lower().strip()
        if action == "look you":
            s103 = "You got dressed today with a little more intentionality than usual, but not by much. Your attire is basic, but you " \
            "know that it's comfortable, and hopefully normal enough not to be noteworthy. You're wearing your jacket, which you think of " \
            "as something akin to your signature, a black t-shirt which reads \"Something Rotten\" under an image of a character in a videogame, " \
            "also wearing a black t-shirt with \"Something Rotten\" emblazened across the front, a pair of cuffed dark wash jeans expose the " \
            "missmatch socks whose patterns stick out from your running shoes."
            print(textwrap.fill(s103,width))
            pause()
            s104 = "Though it's too bright to see your reflection in the window next to you, you know what you look like. Your curly, " \
            "dark brown hair reaches your shoulders, but only that growing from the top of your head, on the sides and back it barely " \
            "manages to clear your chin. An odd side effect of the process that lead to your current hairstyle. As for your face, the " \
            "features which stand out most to you are these: your nose is large and rounded but you'd hesitate to call it bulbous, your " \
            "eyebrows are what you'd call fuzzy, not exactly wild, but certainly unattended, the inside end of your left brow is oddly thinned " \
            "and doesn't flow with the rest of the hairs. Your lips are angular, and asymetrical, on one side the upper lip slopes down to " \
            "meet the edge of your lower lip, and on the other it ends some distance before the edge of your lower lip. Atop all of these " \
            "features sit a pair of browline glasses, mostly made of thin silver metal, with the browline itself being semi transparent green " \
            "plastic they got roughed up shortly after you got them so they sit a litle oddly on your face."
            print(textwrap.fill(s104,width))
            pause()
        elif action == "look racy's":
            s106 = "The cafe is a relatively small space, it is sparcely populated. A few college age people sit at the counter chatting " \
            "quietly with the barista, who they clearly know. Indie music plays quietly over the spaces speakers. As comfortable as you are " \
            "here, now that your drink is finished you have no real reason not to leave, your car is parked just {outside}."
            print(textwrap.fill(s106,width))
            pause()
        elif action == "look table":
            s105 = "On the table sits the now empty mug, formerly the vessel for your preffered drink from Racy's, a \"Willow\", though " \
            "you struggle to define what exactly it tastes like, it has been your go to order for the past few years, since Jeremiah stopped " \
            "working as a barista, when he was there your go to was the \"Bree's Knees\" but no one else makes it like he used to, the " \
            "\"Willow\" is a far less subtle drink, so you find that it comes out more consistently well made. As for the table itself, " \
            "it's unremarkable as an object, a slightly wobbly tall circular surface, flanked on two sides by spinning stools. The only " \
            "thing that makes it compelling is the specific nostalgia you have tied to it."
            print(textwrap.fill(s105,width))
            pause()
        elif action == "inventory" or "inv":
            inv_manage()
        elif action == "go outside" or "leave":
            s107 = "You stand from the stool, collect the mug and plate, and place them in the dish return bin at the far end of the counter, " \
            "as you walk to the door you perform the needless but ritualistic patting of the pockets in your jacket to check you have everything. " \
            "You push the door outwards to exit the cafe, and quickly upon exiting take your default posture with your hands in the main pockets. "
            "As you adjust to the cold, it occurs to you to consider. 'What do I do now?'."
            print(textwrap.fill(s107,width))
            pause()
            break
        else:
            print("I don't understand.")
    cursce.pop(0) 
    cursce.insert(0,racys_parking_lot)
    racys_parking_lot()

def racys_parking_lot():
    if car_spot == 'racys':
        car_parked_racys() #that'll contain the scene description
    else:
        print("Your car isn't parked here.")
    rpl01 = "The Racy's parking lot, not a huge space, it runs perpendicular to Water St., along what would be conventionally thought of as the " \
    "back of the building. From where you're standing you can see {Water St.} itself, "
    print(textwrap.fill(rpl01,width))

def drunk_crash():
    print("you done fucked up...") #"*"

#how the fuck do you build a dialogue system???

def talking2companions(): #"*"
    while True: #creates a loop
        incidental(comp[0],cursce[0]) #incidental(companion,location) is a defined secondary function under each scene
        action = input("> ").lower().strip()
        if action == "help":
            print("When talking to a companion you have a few options, 'shoot the breeze'(chat), 'small talk'(current), and 'big talk'(us). As well as 'exit'.")
            pause()
        elif action == "exit":
            break
        elif action == "shoot the breeze" or "chat":
            discuss_whatever()
            pause()
        elif action == "big talk" or "us":
            discuss_relationship()
            pause()
        elif action == "small talk" or "current":
            discuss_current()
            pause()
        else:
            print("Command not understood, try 'help' for example commands.")
    exit()

def discuss_relationship(): #"*" these may change to reflect how the different companions grow in deifferent ways
    if comp[0] == 'the_statue':
        relationshipwstatue(statue_grth.count(1))
    elif comp[0] == 'the_drink':
        relationshipwdrink(drink_grth.count(1))
    elif comp[0] == 'the_girl':
        relationshipwgirl(girl_grth.count(1))
    elif comp[0] == 'the_fetish':
        relationshipwfetish(fetish_grth.count(1))
    elif comp[0] == 'the_saviour':
        relationshipwsaviour(saviour_grth.count(1))

def discuss_current(): #"*" I need to write all these dialogues, and also, double check this works
    if comp[0] == 'no_one':
        pass #"*" should add to meeting fielding
    else:
        (callable_comp[0](cursce[0]))

sts_lib = ["voyeurism"] #"*" has 1 option, is a list of the options for the 'shoot the shit' command

def discuss_whatever(): #"*"
    ShootintheShit = random.randint(0,0)
    if comp[0] == 'no_one':
        pass #"*" Should add to meeting fielding
    else:
        (callable_comp[0](sts_lib[ShootintheShit]))

#Shootin the Shit w/Companions
def the_statue(voyeurism):
    print("*")
def the_drink(voyeurism):
    print("*")
def the_girl(voyeurism):
    print("*")
def the_fetish(voyeurism):
    print("*")
def the_saviour(voyeurism): #"*"
    print("*")

#Discussing Relationship w/Companions

#Talking about current scene w/Companionss

#Initial Menus and Such
def start_screen(): #Start screena
    print("Welcome to")
    title()
    print("       by Eryn")
    print("Do you want to Start, or do you need Help?")
    choice = input("> ").lower().strip()
    if choice == "start":
        start_game() 
    elif choice == "help":
        help_screen() 
    elif choice == "settings":
        width_set()
    else:
        print("I'm sorry, I don't understand")
        print()
        start_screen() 

def help_screen(): #Player info
    print("               This is Transtextual, if you want to know about why I made it input 'info'!")
    hs01 = "Transtextual is a relatively simple text adventure, the way navigation works will be this, if you want to go to a location " \
    "mentioned in a description simply write 'go to [location]' if you want to pick up an item, write 'take [item] if you want to use " \
    "something in the environment write 'use [object], and if you are talking to someone 'ask [subject]' or whatever contextually makes " \
    "sense as a reply will work, assuming of course I thought of it. I will {highlight} objects you can interact with, and if someone asks " \
    "you a question I'll tell you what your options are. You can use the input 'inventory', to access said inventory, this is available during " \
    "most \"action\" prompts, but not during \"dialogue\" prompts. From the inventory you can use the \"use me\" command with the notebook item " \
    "to save, or load. Occasionally the text will stop coming, if this happens, the program is waiting for any input, simply hit enter to continue."
    print(textwrap.fill(hs01,width))
    print("Do you understand?")
    choice = input("> ").lower().strip()
    if choice == "yes":
        start_screen() 
    elif choice == "no":
        print("Refer to the readme file for more detailed instructions.")
        print()
        start_screen() 
    elif choice == "info":
        hs02 = "I started writing Transtextual in October of 2025, because of a Tumblr post about 'programmer art' and 'artist programming' " \
        "for some reason I found the idea of trying to create a game as someone with no experience very exciting, I'm sure that's true for a " \
        "lot of first time developers. Crucially though I decided I wasn't going to actually learn how to code, instead I was going to bodge " \
        "it together as poorly as possible, initially I wanted to create this in BASIC turns out that there aren't a whole lot of guides on " \
        "how to use an outdated language like that, so Transtextual is written in Python. If you want to know about how I wrote the game, 'ask " \
        "code' or if you want to know about the narrative 'ask narrative' on the help screen! You can input whatever to get back there."
        print(textwrap.fill(hs02,width))
        pause()
    elif choice == "ask code":
        hs03 = "Due to my desire not to actually learn how to program, specifically because I think it would be funny I have had to make " \
        "do with many bodge solutions, for instance here every distinct line, is an unique print command, if there is a better way to do " \
        "this, well it's not one I know. Additionally the source code of the game is structured so that anytime a scene is being described " \
        "to you, I actually had to create and reference it earlier in the code, essentially that means that anytime you open Transtextual " \
        "the game reads and remembers every single possible scene, before it even introduces itself! Isn't that neat! If you want more " \
        "examples of my bad design hit enter, or to escape type 'home'"
        print(textwrap.fill(hs03,width))
        choice = input("> ").lower().strip() #this bit allows an empty input to continue onwards, or the input of 'home' to escape
        if choice == "":
             print()
             code_issues()
        elif choice == "home":
            print ()
            start_screen()
    elif choice == "ask narrative":
        print("*") #explain once you've actually come up with one
    else:
        print("I'm sorry, I'm confused what you mean.")
        print ()
        help_screen() 

def code_issues(): #Diary of Bodge
    print("To answer the question raised by this being printed in code, no there is not a .txt file that contains all the words, I don't know how to do that.")
    pause()
    print("I genuinely have no idea how to implement a system wherein you can always save, load, or look at your inventory, to this end my plan is just provide")
    print("it as a part of the if statement for every single input tree.")
    pause()
    print("I created a system for inventory management it uses a series of dumb function loops and a lot of if statements, all to come to a conclusion that at time")
    print("of writing, I don't actually know if it will work once the game gets more complex, natuarally that is part of the appeal of this project to me it's just a lot")
    print("of work to redo if I royally screwed it up.")
    pause()
    print("Currently as I design this each line is created as it's own independent print action, which I want to change, it occurs to me now though, that I should definitely")
    print("change my workflow now so I don't have to go change everything all at once later.")
    start_screen()

#Storage for Looking through stuff

#General use functions
def wrap_text(writing, width):
    return textwrap.fill(writing, width)

def pause(): #Pause and wait for user input function
    choice = input("").lower().strip()
    if choice == "":
        pass
    else:
        pass

def alc_check():
    D = alc.count(1)
    abv.pop(0)
    abv.insert(0,D)

def drink():
    alc.append(1)

def dest_list():
    for location in known_loc:
        print(f"{location}")

def car(): #"*" should probably describe how the comps interact with the car.
    car01 = "You walk up to the driver side of the old beater, spinning the keys on your finger in the same way one might twirl a revolver, " \
    "slide into the familiar seat, start the engine, and plug in your mp3 player."
    print(textwrap.fill(car01,width))
    T = random.randint(1,50)
    print("With the audible buzz of active audio equipment interacting"); print(mp3[T]); print("erupts from the cars speakers.")
    alc_check()
    while True:
        print("Where do you want to go?")
        destination = input("> ").lower().strip()
        if destination == "i don't know" or 'idk' or 'help' or 'i dont know':
            print("These are the places you can think to go to:")
            dest_list()
            pass
        elif destination in known_loc:
            if random.randint(1,6) in range(1,abv[0]):
                drunk_crash()
            else:
                break
        else:
            print("I don't understand what you mean.")
            pass
    (destination())

cemetary = 'cemetary'    
def car_parked_cemetary():
    cp_cemetary = "*"
    print(textwrap.fill(cp_cemetary,width))

downtown = 'downtown'
def car_parked_downtown():
    cp_downtown = "*"
    print(textwrap.fill(cp_downtown,width))

boyd = 'boyd park'
def car_parked_boyd():
    cp_boyd = "*"
    print(textwrap.fill(cp_boyd,width))

simon = 'mt simon'
def car_parked_mt():
    cp_mt = "*"
    print(textwrap.fill(cp_mt,width))

high = 'hi bridge'
def car_parked_high():
    cp_high = "*"
    print(textwrap.fill(cp_high,width))

mall = 'mall'
def car_parked_mall():
    cp_mall = "*"
    print(textwrap.fill(cp_mall,width))

water = 'water st'
def car_parked_water():
    cp_water = "*"
    print(textwrap.fill(cp_water,width))

campus = 'low campus'
def car_parked_campus():
    cp_campus = "*"
    print(textwrap.fill(cp_campus,width))

carson = 'carson'
def car_parked_carson():
    cp_carson = "*"
    print(textwrap.fill(cp_carson,width))

racys = 'racys'
def car_parked_racys():
    cp_racys = "*"
    print(textwrap.fill(cp_racys,width))

#Car drive_tos

def drive_to_home():
    print("You think about going home, but as you go to turn the key, you realize you can't do it, you're not ready to go home.")
    print("There's so much left to do, or at least you hope so.")
    car()

#Inventory use_mes

def wine(): #Model of generic use_me() function, and for Wine
    alc_check()
    if (abv[0]) == 0:
        print("You drink the first third of the wine. You are feeling a little a tipsy, probably not enough for it to be a problem.")
        drink()
        inv_manage()
    elif (abv[0]) == 1:
        print("You drink roughly a third of the wine. You are feeling comfortably lightheaded, probably shouldn't drive, but no one should notice.")
        drink()
        inv_manage()
    elif (abv[0]) == 2:
        print("You finish off the wine. You feel comfortably numbed, confident, you feel drunker than you should, but you aren't complaining.")
        drinK()
        inv_manage()

def skirt(): #Skirt Interaction Model
    if cursce[0] == start_game:
        print("You put on the dark blue pleated skirt and twirl around in your room, it feels nice, you feel")
        print("happy, but you know you can't bear to wear it outside")
        add_item('skirt', 1)
        inv_manage()
    elif cursce[0] == drunk_start:
        print("You put on the expensive tailored skirt you bought because you were hoping it would make you")
        print("feel less self conscious, that didn't work but with the wine in you, there is a nice sense of")
        print("confidence, you think you'll wear it out today for the first time.")
        pause()
        print("You are wearing your skirt.")
        drunk_start()
    else:
        print("You look longingly at the soft cotton skirt, you don't think you deserve to wear it out.")
        add_item('skirt', 1)
        inv_manage()

def jacket(): #First Time Jacket Interaction
    j101 = "Your trusty jacket, you've been wearing it since highschool and it shows. Mustard darning lines its edges in a desperate " \
    "effort to hold off entropy it feels deeply comfortable on you, you appreciate how it effectively hides your figure, and its many " \
    "{pockets}. It was your greatest asset during that shoplifting phase you went through in highschool. The jacket is, as much as you " \
    "love it, kind of a piece of shit, some fast fashion bullshit that you didn't buy, but found in a closet. You'll never be able to " \
    "replace it exactly. Especially now that its once vaguely green, vaguely brown canvas outershell has faded and sunbleached into a " \
    "nigh unreplicable hue."
    print(textwrap.fill(j101,width))
    choice = input("> ").lower().strip()
    if choice == "use pockets":
        j102 = "You rummage through the many pockets of your jacket searching for anything you might have left in it over summer. Across" \
        " its 9 pockets you find a folded note, your pocket scissors, a pen, a pocket sized notebook, $7, a large coin, and a usb stick"
        print(textwrap.fill(j102,width))
        pause()
        remove_item('jacket',1)
        add_item('your jacket',1)
        add_item('folded note',1)
        add_item('pocket scissors',1)
        add_item('pen',1)
        add_item('money',7)
        add_item('large coin',1)
        add_item('usb stick',1)
        add_item('notebook',1)
        add_item('oracle cards',1)
        add_item('wallet',1)
        inv_manage()
    elif choice == 'back':
        inv_manage()
    elif choice == 'remove jacket':
        j103 = "You're not going to do that, she would never do that. Look, I'm not going to let /you/ hurt her, I mean she's going " \
        "to hurt through this experience, but I refuse to let you take away her support maliciously, if you keep trying, I will be " \
        "back and we're going to have a long conversation, do you understand me?"
        print(textwrap.fill(j103,width))
        choice = input("< ").lower().strip()
        if choice == 'yes':
          print("okay, good.")
          print('')
          jacket()
        else:
            print("I don't care, what you have to say, this is final.")
            ang.append('1')
            anger = ang.count(1)
            if anger == 3:
                print("fuck you")
                sys.exit()
            else:
                jacket()
    else:
        print("I'm sorry, I don't understand, try 'back' or 'use pockets'!")
        jacket()

def yourjacket(): #Every other time you look at jacket
    j201 = "Your trusty jacket, you've been wearing it since highschool and it shows. Mustard darning lines its edges in a desperate" \
    " effort to hold off entropy it feels deeply comfortable on you, and you appreciate how it effectively hides your figure, and its" \
    " many pockets. It was your greatest asset during that shoplifting phase you went through in highschool. The jacket is, as much as " \
    "you love it, kind of a piece of shit, some fast fashion bullshit that you didn't buy, but found in a closet. You'll never be able " \
    "to replace it exactly. Especially now that its once, vaguely green, vaguely brown canvas outershell has faded and sunbleached into " \
    "an nigh unreplicable hue."
    print(textwrap.fill(j201,width))
    pause()
    inv_manage()

def mp3player(): #mp3 player which ideally comes with a referable list to pull from of songs
    mp301 = "An old mp3 player, you've had it since you were very young, it's not exactly a modern piece of technology, but you have " \
    "good memories attached to it. It's red, about 1 by 3 inches in size. Apparently produced by a company called COBY, but you don't " \
    "know anything else about them. You set it to shuffle today."
    print(textwrap.fill(mp301,width))
    T = random.randint(1,50)
    print("The mp3 player is currently playing:"); print(mp3[T])
    pause()
    inv_manage()

def foldednote():
    fn01 = "An old note you keep in your jacket, a gift from the longest friendship you still have, and best you've ever had, its " \
    "content is a consistent source of comfort, occasionally a source of pain, but deeply important to you. She was there when you " \
    "started asking questions, and provided the greatest support as you began to understand yourself. It wouldn't be an exageration " \
    "to say that she is the person you love most in this world, and while you have no way to prove it, you know there is a time where " \
    "she would have said the same of you. Since then she moved to Alaska. You can't help but feel a little betrayed by her, because " \
    "she left you alone in this town, like that."
    print(textwrap.fill(fn01,width))
    pause()
    inv_manage()

def pocketscissors():
    ps01 = "A pair of fold away scissors, in your experience people often find it weird that you always have scissors on you, but " \
    "that usually comes roughly 30 seconds before they realize that they need a cutting instrument."
    print(textwrap.fill(ps01,width))
    pause()
    inv_manage()

def pen():
    print("A fairly standard capped pen, specifically a Pilot Precise V5, writes well on paper and skin.")
    pause()
    inv_manage()

def money():
    m01 = "Money, cash, it can be used to purchase goods and services, you could get coffee, or access to some kind of private" \
    " space. You don't usually have a lot of money, given that you've been unemployed for almost a full year, but it should be " \
    "okay, today isn't really about shopping."
    print(textwrap.fill(m01,width))
    pause()
    inv_manage()

def largecoin():
    lc01 = "A fairy coin, technically on loan from a friend who got it at a rennaisance faire, she was showing it to you and as " \
    "she was talking, you found yourself fidgeting with it, spinning it through your fingers. At the time she said you could have " \
    "it, but you are unwilling to assume that means to keep it long term."
    print(textwrap.fill(lc01,width))
    pause()
    inv_manage()

def usbstick():
    usb01 = "A USB stick, capacity: 16 GB, you use it for printing homework, or keeping backups of important things, right now " \
    "if you recall it should be empty, but without access to a computer it is all but useless."
    print(textwrap.fill(usb01,width))
    pause()
    inv_manage()

def notebook():
    print("A small notebook, you can use it to record how your day has been going!")
    menu = input("Save / Load").lower().strip()
    if menu == "save":
        save_game()
    elif menu == "load":
        load_game()
    
def oracle_cards():
    oc01 = "You deftly pull out the deck of cards and pull the rubber band from binding the stack together onto your wrist, you " \
    "quickly shuffle while focusing on the strange day you're going through. Performing the requisite twisting to ensure a true " \
    "shuffle for the oracle cards. Though you aren't following any kind of specific spread, you figure that the first card should " \
    "refer to yourself, the second to someone important for your day, and the third to the current state of yourself and the world."
    print(textwrap.fill(oc01,width))
    print("You go to draw the first card...")
    pause()
    if grth.count(1) in range(0,14): #upside down
        ocgrth01 = "You pull a card with 'III - THE EMPRESS' emboldened across what would be the bottom if it were not upside down, the " \
        "bulk of the card is dedicated to an illustration of a woman sitting on a pink draped bed. Legs lifted so as to show the " \
        "bottom of her bare thighs, she is dressed in a thin white grecian dress, through which you can see the soft outlines of her " \
        "body. A pair of blue snakes twist up her forearms and in her right hand she holds a mirror. Her rich brown hair is done in " \
        "braids, and upside down like this her expression seems to be an almost mocking smile, like she knows something you haven't " \
        "quite figured out yet."
        print(textwrap.fill(ocgrth01,width))
        pause()
        ocgrth02 = "With the card upside down your eye is instinctively drawn to where her legs cross at the ankle, obscuring her " \
        "groin. All in all from this angle something about the illustration feels unbalanced and odd, like she might slip off the " \
        "card and dissapear forever."
        print(textwrap.fill(ocgrth02,width))
        pause()
        ocgrth03 = "You know that the upside down Empress often represents hardships, scarecity, bareness and neediness, this does " \
        "very little to bring you comfort."
        print(textwrap.fill(ocgrth03,width))
        pause()
    elif grth.count(1) in range(15,200):
        ocgrth04 = "You pull a card with 'III - THE EMPRESS' emboldened across the bottom, the bulk of the card is dedicated to " \
        "an illustration of a woman sitting on a pink draped bed. Legs lifted so as to show the bottom of her bare thighs, she is " \
        "dressed in a thin white grecian dress, through which you can see the soft outlines of her body. A pair of blue snakes twist " \
        "up her forearms and in her right hand she holds a mirror. Her rich brown hair is done in braids, and rightside up you see " \
        "her expression as more comfortably assured. Like she's looking at something going the way she figures it should be."
        print(textwrap.fill(ocgrth04,width))
        pause()
        ocgrth05 = "With the card rightside up she feels sturdy and confident, secure in her position, and comfortable no less. Your " \
        "eye is naturally drawn to her face where oddly you notice some features you share with her, that not quite bulbous nose you're " \
        "used to seeing in the mirror, similarly thin eyes which you used to blame on others having difficulty reading you, but now seem " \
        "so expressive on the empress. You realize she sort of looks like how you wish you looked."
        print(textwrap.fill(ocgrth05,width))
        pause()
        ocgrth06 = "You know that the rightside up Empress often represents nurturing, abundance, the feminine divine, and sovreignty " \
        "over the natural order. That feels good, if those are the traits you've earned today, then maybe life will start to get a " \
        "little easier going forward."
        print(textwrap.fill(ocgrth06,width))
        pause()
    else:
        ocgrth07 = "You pull a rules card from the deck, it explains that your current growth as an individual stored as a number of " \
        "appended '1' digits in an array has managed to fall outside the range of 0 to 200, something which should not be physically " \
        "possible within the mechanics of the game."
        print(textwrap.fill(ocgrth07,width))
        pause()
    print("You go to draw the second card...")
    if comp[0] == 'no_one':
        D = random.randint(1,6)
        if D == 6:
            print("You manage to fumble and pull 5 cards. Do you want to {look} at all of them or just {move on}?")
            choice = input('> ').lower().strip()
            if choice == 'look' or 'look at cards' or 'look at all of them' or 'yes':
                occomp01 = "The five cards end up face down in your hand, it's hard to say if you should flip them horizontally or " \
                "vertically, you decide to flip them without any respect to orinetation, afterall it was a mistake to pull this many at " \
                "all, what the cards mean won't be all that useful anyways."
                print(textwrap.fill(occomp01,width))
                pause()
                occomp02 = "The first of the five you flip to look at is labeled at the bottom as '● ace of cups ●' much of the card is " \
                "dedicated to an image of a hand sticking out of the placid surface of water, holding a chalice, in which there is a large " \
                "complex wave."
                print(textwrap.fill(occomp02,width))
                pause()
                occomp03 = "The next you flip has a red border all around the image, in the border are a few blocks of text, going clockwise " \
                "from the top left corner the text reads 'CHALICES COPAS 9 COPPE COUPES BEKERS KELCHE' within the red border there is an " \
                "illustration of two figures on a bench, a man and a woman. The man has a sheet wrapped around, his lower half. While the " \
                "woman is dressed only in thin semi-transparent light grey underwear. They sit seemingly entranced by each other, hands " \
                "entangled together."
                print(textwrap.fill(occomp03,width))
                pause()
                occomp04 = "The next card you flip has a black border, in the top left is a downward pointing triangle in which is the numeral " \
                "'2', in the top left you see a block of text which reads 'WATER WASSER EAU AGUA' in the bottom left is the text 'ACQUA' and " \
                "in the bottom right is printed '♀ ♋︎' within the black border is an illustration of two figures, a man and a woman wading " \
                "through waste deep water. The man has his arms wrapped around the woman's neck almost like he's choking her, this reading " \
                "is corroborated by the woman's poise and face, she's reaching out, with an expression of desperation. She's wearing a thin " \
                "brown blouse, from which her breasts are valiantly attempting to escape, a mirror of their keepers desperation."
                print(textwrap.fill(occomp04,width))
                pause()
                occomp05 = "You flip the third card of the bundle, it has a maroon border, at the top and bottom, on a an illustration of a " \
                "brass plate there is the numeral '6'. The illustartion consists of a pair of figures. A man and a woman, the man is almost " \
                "entirely obscured as the woman sits on his lap. Her dark red dress is riding up her legs exposing her thighs, on her left " \
                "thigh lays the mans hand. The dress is entirely loosed from the top, her breasts are exposed, wrapped by her arms with which " \
                "she clings to herself. Behind the pair of figures leaning against the wall behind them there are six wooden staffs."
                print(textwrap.fill(occomp05,width))
                pause()
                occomp06 = "The final of the five cards you flip is nearly taken up entirely by its illustration, barring two small symbols " \
                "at the bottom, the numeral '3', and a pictograph of a sword. The illustration is of a woman with dark brown hair, she is " \
                "dressed in armor and a cloak. She sits facing away from the viewer, her legs folded beneath her. She sits in a puddle of " \
                "blood, its source obvious as the woman appears to be drawing a sword out of her bleeding chest, on the wall behind her " \
                "two more swords hang."
                print(textwrap.fill(occomp06,width))
                pause()
            elif choice == 'move on' or 'no':
                pass
        elif D == 5: #the girl
            ocnctg01 = "You pull a card with a black border, in the top left is a downward pointing triangle in which is the numeral '2', " \
            "in the top left you see a block of text which reads 'WATER WASSER EAU AGUA' in the bottom left is the text 'ACQUA' and in the " \
            "bottom right is printed '♀ ♋︎' within the black border is an illustration of two figures, a man and a woman wading through " \
            "waste deep water. The man has his arms wrapped around the woman's neck almost like he's choking her, this reading is " \
            "corroborated by the woman's poise and face, she's reaching out, with an expression of desperation. She's wearing a thin brown " \
            "blouse, from which her breasts are valiantly attempting to escape, a mirror of their keepers desperation."
            print(textwrap.fill(ocnctg01,width))
        elif D == 4: #the statue
            ocncts01 = "You pull a card which is labeled at the bottom as '● ace of cups ●' much of the card is dedicated to an image of " \
            "a hand sticking out of the placid surface of water, holding a chalice, in which there is a large complex wave."
            print(textwrap.fill(ocncts01,width))
        elif D == 3: #the drink
            ocnctd01 = "You pull a card which is nearly taken up entirely by its illustration, barring two small symbols at the bottom, " \
            "the numeral '3', and a pictograph of a sword. The illustration is of a woman with dark brown hair, she is dressed in armor " \
            "and a cloak. She sits facing away from the viewer, her legs folded beneath her. She sits in a puddle of blood, its source " \
            "obvious as the woman appears to be drawing a sword out of her bleeding chest, on the wall behind her two more swords hang."
            print(textwrap.fill(ocnctd01,width))
        elif D == 2: #the saviour
            ocncts01 = "You pull a card which has a red border all around the image, in the border are a few blocks of text, going " \
            "clockwise from the top left corner the text reads 'CHALICES COPAS 9 COPPE COUPES BEKERS KELCHE' within the red border " \
            "there is an illustration of two figures on a bench, a man and a woman. The man has a sheet wrapped around, his lower " \
            "half. While the woman is dressed only in thin semi-transparent light grey underwear. They sit seemingly entranced by each " \
            "other, hands entangled together."
            print(textwrap.fill(ocncts01,width))
        elif D == 1: #the fetish
            ocnctf01 = "You pull a card which has a maroon border, at the top and bottom, on a an illustration of a brass plate there is " \
            "the numeral '6'. The illustartion consists of a pair of figures. A man and a woman, the man is almost entirely obscured as " \
            "the woman sits on his lap. Her dark red dress is riding up her legs exposing her thighs, on her left thigh lays the mans " \
            "hand. The dress is entirely loosed from the top, her breasts are exposed, wrapped by her arms with which she clings to " \
            "herself. Behind the pair of figures leaning against the wall behind them there are six wooden staffs."
            print(textwrap.fill(ocnctf01,width))
    elif comp[0] == 'the_girl': #The Hierophant
        if girl_grth.count(1) in range(0,14): #upside down
            ocggrth01 = "You pull a card with a black border, it's upside down, the border has several blocks of text, if it were right " \
            "side up, starting in the top left the text reads 'V  THE PRIEST DER PRIESTER LE PRETRE EL SACERDOTE ♉︎ IL SACERDOTE' within " \
            "the border there is an illustration of a woman crouching against a pillar with her knees splayed, she is nude from the waist " \
            "down. She wears a low cut, black spotted, blouse. A cardinals hat obscurs her crotch, he is looking towards her. Her arms " \
            "are tucked behind her back presumably supporting her from behind. Her pitch black hair billows and pleasure seems to erupt " \
            "across her face."
            print(textwrap.fill(ocggrth01,width))
            pause()
            ocggrth02 = "With the card upside down, the cardinals poise seems to be one of pause and appreciation towards the woman's " \
            "provocation. The inverted view casts the rounded top of the cardinals hat as a phallus approaching the woman's vagina, " \
            "the angle creates a look of tension, as though her legs are going to burst with the difficulty of her task."
            print(textwrap.fill(ocggrth02,width))
            pause()
            ocggrth03 = "The deck this card is from, varies slightly from convention, but you know the card should correspond roughly " \
            "to 'The Hierophant' which when inverted, you recall represents arrogance, elitism, hypocrisy, and charlatanism. It brings " \
            "you little joy to think of Sophie in this way, surely if she noticed she would have something to say about the provocative " \
            "imagery on the card. You aren't in the mood to be judged right now, so you slip the card under your Empress before Sophie " \
            "catches on."
            print(textwrap.fill(ocggrth03,width))
            pause()
        elif girl_grth.count(1) in range(15,200): #upright
            ocggrth04 = "You pull a card with a black border, the border has several blocks of text within it, starting in the top " \
            "left and moving clockwise the text reads 'V  THE PRIEST DER PRIESTER LE PRETRE EL SACERDOTE ♉︎ IL SACERDOTE' within the " \
            "border there is an illustration of a woman crouching against a pillar with her knees splayed, she is nude from the waist " \
            "down. She wears a low cut, black spotted, blouse. A cardinals hat obscurs her crotch, he is looking towards her. Her pitch " \
            "black hair billows, and her arms are tucked behind her back presumably supporting her from behind."
            print(textwrap.fill(ocggrth04,width))
            pause()
            ocggrth05 = "With the card upside down, the cardinals pose reads as shock at the womans provacativity. Where once her " \
            "expression seemed to read as pleasure it now looks to you more like exertion. Perhaps she is not engaged in a sexual " \
            "act, but one of desperation."
            print(textwrap.fill(ocggrth05,width))
            pause()
            ocggrth06 = "The deck this card is from, varies slightly from convention, but you know the card should correspond " \
            "roughly to 'The Hierophant' which when upright, you recall representing wisdom, authority, knowledge, doctrine, " \
            "and advice." #connect to Sophie's development
            print(textwrap.fill(ocggrth06,width))
            pause()
        else:
            ocggrth07 = "You pull a rules card from the deck, it explains that the development of your relationship with Sophie " \
            "stored as a number of appended '1' digits in an array has managed to fall outside the range of 0 to 200, something " \
            "which should not be physically possible within the mechanics of the game."
            print(textwrap.fill(ocggrth07,width))
            pause()
    elif comp[0] == 'the_statue': #The Lovers
        if statue_grth.count(1) in range(0,14): #upright
            print("You pull a pleasant light cream card from the deck.") #"*"
        elif statue_grth.count(1) in range(15,200): #upside down
            print('You pull') #"*"
        else:
            print("You pull a rules card from the deck, it explains that the development of your relationship with Danielle stored as a number of appended")
            print("'1' digits in an array has managed to fall outside the range of 0 to 200, something which should not be physically possible within the")
            print("mechanics of the game.")
            pause()
    elif comp[0] == 'the_drink': #The Hermit
        if drink_grth.count(1) in range(0,14): #upside down
            print("You pull") #"*"
        elif drink_grth.count(1) in range(15,200): #upright
            print("You pull") #"*"
        else:
            print("You pull a rules card from the deck, it explains that the development of your relationship with [REDACTED] stored as a number of appended")
            print("'1' digits in an array has managed to fall outside the range of 0 to 200, something which should not be physically possible within the")
            print("mechanics of the game.")
            pause()    
    elif comp[0] == 'the_saviour': #the Hanged Man
        if saviour_grth.count(1) in range(0,14): #upside down
            print("You pull") #"*"
        elif saviour_grth.count(1) in range(15,200): #upright
            print("You pull") #"*"
        else:
            print("You pull a rules card from the deck, it explains that the development of your relationship with Fielding stored as a number of appended")
            print("'1' digits in an array has managed to fall outside the range of 0 to 200, something which should not be physically possible within the")
            print("mechanics of the game.")
            pause()
    elif comp[0] == 'the_fetish': #the Devil
        if fetish_grth.count(1) in range(0,14): #upside down
            print("You pull") #"*"
        elif fetish_grth.count(1) in range(15,200): #upright
            print("You pull") #"*"
        else:
            print("You pull a rules card from the deck, it explains that the development of your relationship with Carry stored as a number of appended")
            print("'1' digits in an array has managed to fall outside the range of 0 to 200, something which should not be physically possible within the")
            print("mechanics of the game.")
            pause()
    else:
        print("Damn, that's fucked, you don't even have the 'no_one' companion that I use to check against, try getting someone to hangout with you.")
    print("Are you sure you want to draw the third and final card...")
    choice = input("> ").lower().strip()
    if choice == "yes":
        print("You pull out a...") #"*" this would be a description of the current variables, as well as perhaps something about the plot, based on something
        inv_manage()
    elif choice == "no":
        inv_manage()
#Here is being worked on

#All of this stuff is for Inv Management, mostly it's done. Maybe reformat this to treat the jacket itself as the inventory

def inv_manage(): #Inv Management menu Function
    while True:
        action = input("What would you like to do? (view/use me/use/drop/exit): ").strip().lower(); 
        if action == 'exit':
            break
        elif action == 'use me':
            use_me()
        elif action == 'use':
            use_env()
        elif action == 'drop':
            drop_object()
        elif action == 'view':
            display_inventory()
        else:
            print("Invalid action. Please try again.")
        exit()

def display_inventory(): #Display Inv Function
    if not inventory:
        print("Your inventory is empty.")
    else:
        for item, quantity in inventory.items():
            print(f"{item}: {quantity}")
        #print("Hand:" (hand)) #for reasons unexplaianble I can't make it display what's in the hand

def add_item(item, quantity): #Add to Inv Function
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity

def remove_item(item, quantity): #Remove from Inv Function
    if item in inventory:
        if inventory[item] >= quantity:
            inventory[item] -= quantity
            if inventory[item] == 0:
                del inventory[item]
        else:
            print("Not enough quantity to remove.")
    else:
        print("Item not found in inventory.")

def use_me(): #Generic use me Inv Nav
    print("Use what?")
    item = input("> ").lower().strip()
    strg = item.replace(" ","")
    if item in inventory:
        function_name = strg
        func = eval(function_name)
        (func())
    elif item == "return":
        inv_manage()
    else:
        print("You don't have that on you right now.")

def use_env(): #Equip item to Hand Function
    print("Use what?")
    item = input("> ").lower().strip() #determines what item
    if item in inventory:
        add_item(hand[0],1) #add whatever is in hand to inv.
        hand.pop(0) #removes item from hand
        hand.insert(0,item) #insert given item to hand
        remove_item(item, 1) #erases inv vers
        print("You are holding"); print(hand)
        pause()
        exit()
    elif item == "return":
        inv_manage()
    else:
        print("You do not have that item.")

def drop_object(): #drop items from Inv
    print("Drop what?")
    item = input("").lower().strip()
    if item == "jacekt":
        print("You can't drop that.")
    else:
        choice = input("Are you sure?")
        if choice == "yes":
            remove_item(item, 1)
            print(f"You dropped {item}")
            pause()
            inv_manage()
        elif choice == "no":
            inv_manage()

def exit(): #Exit inv to whatever scene on
    (cursce[0]())

#Function for adding a companion to the party
def drink_comp_get():
    comp.pop(0)
    callable_comp.pop(0)
    comp.insert(0,'the_drink')
    callable_comp.insert(0,the_drink)

def girl_comp_get():
    comp.pop(0)
    callable_comp.pop(0)
    comp.insert(0,'the_girl')
    callable_comp.insert(0,the_girl)

def saviour_comp_get():
    comp.pop(0)
    callable_comp.pop(0)
    comp.insert(0,'the_saviour')
    callable_comp.insert(0,the_saviour)

def statue_comp_get():
    comp.pop(0)
    callable_comp.pop(0)
    comp.insert(0,'the_statue')
    callable_comp.insert(0,the_statue)

def fetish_comp_get():
    comp.pop(0)
    callable_comp.pop(0)
    comp.insert(0,'the_fetish')
    callable_comp.insert(0,the_fetish)

def comp_leave():
    comp.pop(0)
    callable_comp.pop(0)
    comp.insert(0,'no_one')
    callable_comp.insert(0,no_one)
#These Two are untested things off the internet

def save_game(): #Save Function "*"
    with open("savefile.txt", "w") as f:
        f.write(",".join(inventory))

def load_game(): #Load Function "*"
    global inventory
    with open("savefile.txt", "r") as f:
        inventory = f.read().split(",")

def width_set():
    print("The default text width is '150', after choosing a new value, an example text will be displayed.")
    value = input("Input New Value> ")
    width.pop(0)
    width.insert(0,value)
    example_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque vel aliquam urna. Fusce suscipit gravida nisi, id placerat massa imperdiet sit amet. Mauris venenatis, quam et laoreet euismod, risus augue efficitur lectus, sit amet interdum ante massa in mauris. Vivamus ut est et nisl auctor rutrum eget ut mauris. Fusce ullamcorper, dui interdum interdum ultrices, lacus magna luctus risus, eu eleifend nisl nunc a est. Morbi in ex consectetur, sagittis est sit amet, feugiat turpis. Nam quis tincidunt dui. Morbi sodales auctor mauris vitae mattis. Vivamus vitae ullamcorper erat, sit amet faucibus arcu. Integer vitae tempus urna, id egestas libero. Duis nec lacus vehicula, sollicitudin est sed, tincidunt magna. Integer tincidunt nisi id justo consectetur, a ultrices nibh hendrerit. Morbi condimentum consequat tristique. Etiam imperdiet massa sit amet justo fringilla, ut mollis nisi luctus. "
    print(textwrap.fill(example_text,width[0]))
    pause()
    start_screen()

cursce = [start_game]
car_loc = car_parked[0]
car_spot = ['racys']
alc = []
abv = []
ang = []
# mp3 list is 50 long
mp3 = ['bedroom community by glass beach','Crumbs by Belaganas','Cecily Smith (Bonus Track) by Will Connolly','420-666-6969 by Peter France, Glam Cowgirl','Trace by Micah Marcos','I Was An Island by John-Allison Weiss','Girls Who Play Guitar by Maximo Park','Viva La Resistance by Hypernova','Lovecraft in Brooklyn by The Mountain Goats','City Never Sleeps by Tourism','i haunt ur dreams by hey, nothing','Brave as a Noun by AJJ','International Space Station by Sea Power','From Dusk to Dawn by Fever Dolls','Aphrodite, Your Electric Sexiness by Human Zoo','Brass Band by Jukebox The Ghost',"The Painter by I'm From Barcelona",'Gennifer Flowers by Fever Dolls','Love Me For Me by Sig Figs Collective','Underground by Cody Fry','Homecoming Serf by Sidney Gish','Presumably Dead Arm (617 Sessions) by Sidney Gish','Nickel by flipturn','Adeline by Fever Dolls','Talia by King Princess','a Castle of Rats by The Narcissist Cookbook','Grand Romantic Life by Mom Rock','Candlelight by Cinders','conversation by Coastal Club','Rule #3-Paperwork by Fish in a Birdcage','Rule #34 by Fish in a Birdcage','I Am the Answer by Overtown','Nail Salon by Cinders','From the Sea to the Land Beyond by Sea Power','Untouched by The Veronicas','Life Out of Phase by The Narcissist Cookbook','Sleep Walking by Cinders','Infatuation by Dudes and Their Guys','Dust and Stars(Zacks Thumb Reprise) by Blue Foster','Photos from When We Were Young by Nana Grizol','cold weather by glass beach','Moscow by Autoheart','Clean Slated State by The Altogether','Davy Crochet by The Backseat Lovers','Out of Vogue by Fever Dolls','Loaded by Primal Scream','Lets Dance to Joy Division by The Wombats','Worth It by Dudes and Their Guys','The Good Ship You by The Narcissist Cookbook','Mountain Sound by Of Monsters and Men','Rivers and Roads by The Head And The Heart','Peach Scone by Hobo Johnson','Get Used to It by Ricky Montgomery','Im Free by The Soup Dragons','yoshis island by glass beach','Last Snowstorm of the Year by Hippo Campus','This is Love by Air Traffic Controller']
comp = ['no_one']
callable_comp = [no_one]
inventory = {}
known_loc ={}
hand = ['mp3 player'] #now we have an object that we can check against anytime the player opts to 'use'
outfit = ['default']
width = [150]

#Companion development, card flips 
girl_grth = []
statue_grth = []
drink_grth = []
saviour_grth = []
fetish_grth = []

#Win condition if grth = 15? then flip card
grth = []

start_screen() #has to be the very end. All "def scene():" must occur in the code before they are reffered to

#Notes:
#Now that this project is starting to have significant size, use "*" to find areas where I still need to write something, at least that I know of


def title():
    print("    .....                                                    .x+=:.        s                                 s                                     .. ")
    print(" .H8888888h.  ~-.                                           z`    ^%      :8                                :8                               x .d88\"  ")
    print(" 888888888888x  `>    .u    .                  u.    u.        .   <k    .88                  uL   ..      .88       x.    .                  5888R   ")
    print("X~     `?888888hx~  .d88B :@8c        u      x@88k u@88c.    .@8Ned8\"   :888ooo      .u     .@88b  @88R   :888ooo  .@88k  z88u         u      '888R   ")
    print("'      x8.^\"*88*\"  =\"8888f8888r    us888u.  ^\"8888\"\"8888\"  .@^%8888\"  -*8888888   ud8888.  '\"Y888k/\"*P  -*8888888 ~\"8888 ^8888      us888u.    888R   ")
    print(" `-:- X8888x         4888>'88\"  .@88 \"8888\"   8888  888R  x88:  `)8b.   8888    :888'8888.    Y888L       8888      8888  888R   .@88 \"8888\"   888R   ")
    print("      488888>        4888> '    9888  9888    8888  888R  8888N=*8888   8888    d888 '88%\"     8888       8888      8888  888R   9888  9888    888R   ")
    print("    .. `\"88*         4888>      9888  9888    8888  888R   %8\"    R88   8888    8888.+\"        `888N      8888      8888  888R   9888  9888    888R   ")
    print("  x88888nX\"      .  .d888L .+   9888  9888    8888  888R    @8Wou 9%   .8888Lu= 8888L       .u./\"888&    .8888Lu=   8888 ,888B . 9888  9888    888R   ")
    print(" !\"*8888888n..  :   ^\"8888*\"    9888  9888   \"*88*\" 8888\" .888888P`    ^%888*   '8888c. .+ d888\" Y888*\"  ^%888*    \"8888Y 8888\"  9888  9888   .888B .")
    print("'    \"*88888888*       \"Y\"      \"888*\"\"888\"    \"\"   'Y\"   `   ^\"F        'Y\"     \"88888%   ` \"Y   Y\"       'Y\"      `Y\"   'YP    \"888*\"\"888\"  ^*888%  ")
    print("        ^\"***\"`                  ^Y\"   ^Y'                                         \"YP'                                           ^Y\"   ^Y'     \"%    ")