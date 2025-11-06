#Transtextual, Ver 1

#imported utilities
import textwrap
import string
import sys
import array
import random

#Actual game scenes

def upstairs_hall(): #to do
    pass

def upstairs_hell(): #to do
    pass

def your_room(): #Scene 1
    print("You are sitting in the large armchair in your room. Which is located diagonally across from the door out into the {hall}.")
    action = input("> ").lower().strip()
    if action == "look room":
        print("Your room is a boxy space roughly 14' by 16', from the armchair you can see the whole room with a little craning of your neck. The rooms")
        print("walls are covered in {prints} hanging in frames, two walls are painted a dark rusty orange, and your {bed} is shoved into the corner where") 
        print("they meet. There are string lights lining the upper edge of the walls around the space. The floor is covered in laundry, and other mess. The") 
        print("surfaces of your room are covered in knick knacks, and books. Most notable are the bookshelf near the armchair, the tower {shelf} near the")
        print("door, your bedside table, and the {dresser}. Also in the room is your relatively clean {desk} and the {closet} which you recently removed the")
        print("doors from in order to use its space more effectively.")
        pause()
        your_room()
    elif action == "go to hall":
        print("You move through your room carefully stepping over laundry baskets, and various unacknowledged miscellany, open the door and step out into the hall.")
        if abv[0] == range(0,2):
            upstairs_hall()
            cursce.pop(0)
            cursce.insert(0, upstairs_hall)
        elif abv[0] == 3:
            upstairs_hall()
            cursce.pop(0)
            cursce.insert(0, upstairs_hell)
    elif action == "look hall":
        print("Your door is open, you can see out into the hallway, currently the space is poorly lit but you know it well from living here for over ten years.")
        your_room()
    #elif action == "look prints":
    elif action == "look bed":
        print("The full bed is pressed against the corner, it looks relatively bare, dressed in only a fitted sheet, and an uncovered comforter ")
   # elif action == "look tower shelf" or "look shelf":
    elif action == "inv":
        inv_manage()
   # elif action == "look dresser":
   # elif action == "look desk":
    #elif action == "look closet":

def start_game(): #Opening Description
    print("You are 21, you are living in a mid-sized midwestern town, same one you've always lived in actually. It's November, your university will be")
    print("starting back up again tomorrow after a short break, you don't have any friends in town, but you've decided that you can't just let life pass you by.")
    print("To this end you've planned to leave your phone at home today, you don't expect anyone will notice, it's not like there's anyone who might text. You know that you're")
    print("not exactly comfortable with silence, so you've loaded up an old mp3 player with music. Today is suppposed ot be cold, but hopefully not so cold you'll")
    print("find yourself completely isolated")
    hand.pop(0)
    add_item('jacket',1)
    add_item('mp3_player',1)
    pause()
    cursce.pop(0) 
    cursce.insert(0, your_room)
    your_room()

def drunk_crash():
    print("you done fucked up...")

#how the fuck do you build a dialogue system???

def talking2companions():
    while True: #creates a loop
        incidental(comp[0],loc) #incidental(companion,location) is a defined secondary function under each scene
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

def discuss_relationship():
    if comp[0] == 'the_statue':
        relationshipwstatue(statue_grth.count(1))
    elif comp[0] == 'the_drink':
        relationshipwdrink(drink_grth.count(1))
    elif comp[0] == 'the_girl':
        relationshipwgirl(girl_grth.count(1))
    elif comp[0] == 'the_fetish':
        relationshipwfetish(fetish_grth.count(1))
    elif comp[0] == 'the_writer':
        relationshipwwriter(writer_grth.count(1))

def discuss_current():
    if comp[0] == 'no_one':
        print("You're alone, who are you even trying to talk to?")
        exit()
    elif comp[0] == 'the_statue':
        currentwstatue(loc)
    elif comp[0] == 'the_drink':
        currentwdrink(loc)
    elif comp[0] == 'the_girl':
        currentwgirl(loc)
    elif comp[0] == 'the_fetish':
        currentwfetish(loc)
    elif comp[0] == 'the_writer':
        currentwwriter(loc)

def discuss_whatever():
    ShootintheShit = random.randint(1,)
    if comp[0] == 'the_statue':
        whateverwstatue(ShootintheShit)
    elif comp[0] == 'the_drink':
        whateverwdrink(ShootintheShit)
    elif comp[0] == 'the_girl':
        whateverwgirl(ShootintheShit)
    elif comp[0] == 'the_fetish':
        whateverwfetish(ShootintheShit)
    elif comp[0] == 'the_writer':
        whateverwwriter(ShootintheShit)


#Shootin the Shit w/Companions
voyeurism = 1
def whateverwstatue(voyeurism):
    print("You can't help but find your attention locked to Danielle, you're trying not to stare, but you've always had difficultly looking away from people.")
    print("She doesn't seem to notice, or maybe she does, and just doesn't really mind. You've been unable to tell the difference before. Should you ask her")
    print("about watching people?")
    answer = input("> ").lower().strip()
    if answer == "yes":
        #this bit is formatted intentionally, in order to create a novel like shape output
        print('"Why do you keep looking at me like that?" Danielle asks you, passively chewing on the cuff of her jacket.')
        print('"')
    elif answer == "no":
        print("You guess that might be weird, maybe you'll ask later.")
        pass
    else:
        print("You need to come to a decision, {yes} you ask, or {no} you don't?")

#Discussing Relationship w/Companions

#Talking about current scene w/Companions

#Initial Menus and Such

def start_screen(): #Start screena
    print("Welcome to Transtextual")
    print("       by Eryn")
    print("Do you want to Start, or do you need Help?")
    choice = input("> ").lower().strip()
    if choice == "start":
        start_game() 
    elif choice == "help":
        help_screen() 
    else:
        print("I'm sorry, I don't understand")
        print()
        start_screen() 

def help_screen(): #Player info
    print("               This is Transtextual, if you want to know about why I made it input 'info'!")
    print("Transtextual is a relatively simple text adventure, the way navigation works will be this, if you want to go to a")
    print("location mentioned in a description simply write 'go to [location]' if you want to pick up an item, write 'take [item]")
    print("if you want to use something in the environment write 'use [object], and if you are talking to someone 'ask [subject]'")
    print("or whatever contextually makes sense as a reply will work, assuming of course I thought of it. I will {highlight} objects")
    print("you can interact with, and if someone asks you a question I'll tell you what your options are. At anytime in the game you")
    print("can use the inputs 'inventory', 'save', and 'load' to do what it sounds like the command does. Occasionally the text will stop")
    print("coming, if this happens, the program is waiting for any input, simply hit enter to continue.")
    print("Do you understand?")
    choice = input("> ").lower().strip()
    if choice == "yes":
        start_screen() 
    elif choice == "no":
        print("Refer to the readme file for more detailed instructions.")
        print()
        start_screen() 
    elif choice == "info":
        print("I wrote Transtextual in October of 2025, because of a Tumblr post about 'programmer art' and 'artist programming'")
        print("for some reason I found the idea of trying to create a game as someone with no experience very exciting, I'm sure")
        print("that's true for a lot of first time developers. Crucially though I decided I wasn't going to actually learn how to")
        print("code, instead I was going to bodge it together as poorly as possible, initially I wanted to create this in BASIC")
        print("turns out that there aren't a whole lot of guides on how to use an outdated language like that, so Transtextual is")
        print("written in Python. If you want to know about how I wrote the game, 'ask code' or if you want to know about the") 
        print("narrative 'ask narrative' on the help screen! You can input whatever to get back there.")
        pause()
    elif choice == "ask code":
        print("Due to my desire not to actually learn how to program, specifically because I think it would be funny I have had to")
        print("make do with many bodge solutions, for instance here every distinct line, is an unique print command, if there is a")
        print("better way to do this, well it's not one I know. Additionally the source code of the game is structured so that")
        print("anytime a scene is being described to you, I actually had to create and reference it earlier in the code, essentially")
        print("that means that anytime you open Transtextual the game reads and remembers every single possible scene, before it even")
        print("introduces itself! Isn't that neat! If you want more examples of my bad design hit enter, or to escape type 'home'")
        choice = input("> ").lower().strip() #this bit allows an empty input to continue onwards, or the input of 'home' to escape
        if choice == "":
             print()
             code_issues()
        elif choice == "home":
            print ()
            start_screen()
    elif choice == "ask narrative":
        print("") #explain once you've actually come up with one
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
    print("of writing, I don't actually know will work once the game gets more complex, natuarally that is part of the appeal of this project to me it's just a lot")
    print("of work to redo if I royally screwed it up.")
    pause()
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

def car():
    while True:
        alc_check()
        destination = input("Where do you want to go?").lower().strip()
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

def approach_car():
    while True:
        car_parked(car_loc) #describes the car's parked location

home = 'home'
def car_parked(home):
    print("Your car is parked in the driveway,") #etc.

cemetary = 'cemetary'    
def car_parked(cemetary):
    print("")

downtown = 'downtown'
def car_parked(downtown):
    print("")

boyd = 'boyd park'
def car_parked(boyd):
    print("")

simon = 'mt simon'
def car_parked(mt):
    print("")

high = 'hi bridge'
def car_parked(high):
    print("")

mall = 'mall'
def car_parked(mall):
    print("")

water = 'water st'
def car_parked(water):
    print("")

campus = 'low campus'
def car_parked(campus):
    print("")

carson = 'carson'
def car_parked(carson):
    print("")

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
    if loc == start_game:
        print("You put on the dark blue pleated skirt and twirl around in your room, it feels nice, you feel")
        print("happy, but you know you can't bear to wear it outside")
        add_item('skirt', 1)
        inv_manage()
    elif loc == drunk_start:
        print("You put on the expensive tailored skirt you bought because you were hoping it would make you")
        print("feel less self conscious, that didn't work but with the wine in you, there is a nice sense of")
        print("confidence in you, you think you'll wear it out today for the first time.")
        pause()
        print("You are wearing your skirt.")
        drunk_start()
    else:
        print("You look longingly at the soft cotton skirt, you don't think you deserve to wear it out.")
        add_item('skirt', 1)
        inv_manage()

def jacket(): #First Time Jacket Interaction
    print("Your trusty jacket, you've been wearing it since highschool and it shows. Mustard darning lines its edges in a desperate effort to hold off entropy")
    print("it feels deeply comfortable on you, you appreciate how it effectively hides your figure, and its many {pockets}. It was your greatest asset during")
    print("that shoplifting phase you went through in highschool. The jacket is, as much as you love it, kind of a piece of shit, some fast fashion bullshit that")
    print("you didn't buy, but found in a closet. You'll never be able to replace it exactly. Especially now that its once vaguely green, vaguely brown canvas")
    print("outershell has faded and sunbleached into a nigh unreplicable hue.")
    choice = input("> ").lower().strip()
    if choice == "use pockets":
        print("You rummage through the many pockets of your jacket searching for anything you might have left in it over summer. Across its 9 pockets you find a folded")
        print("note, your pocket scissors, a pen, a pocket sized notebook, $7, a large coin, and a usb stick")
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
        inv_manage()
    elif choice == 'back':
        inv_manage()
    elif choice == 'remove jacket':
        print("You're not going to do that, she would never do that. Look, I'm not going to let /you/ hurt her, I mean she's going to hurt through this experience, but I")
        print("refuse to let you take away her support maliciously, if you keep trying, I will be back and we're going to have a long conversation, do you understand me?")
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
    print("Your trusty jacket, you've been wearing it since highschool and it shows. Mustard darning lines its edges in a desperate effort to hold off entropy")
    print("it feels deeply comfortable on you, and you appreciate how it effectively hides your figure, and its many pockets. It was your greatest asset during")
    print("that shoplifting phase you went through in highschool. The jacket is, as much as you love it, kind of a piece of shit, some fast fashion bullshit that")
    print("you didn't buy, but found in a closet. You'll never be able to replace it exactly. Especially now that its once, vaguely green, vaguely brown canvas")
    print("outershell has faded and sunbleached into an nigh unreplicable hue.")
    pause()
    inv_manage()

def mp3player(): #mp3 player which ideally comes with a referable list to pull from of songs
    print("An old mp3 player, you've had it since you were very young, it's not exactly a modern piece of technology, but you have good memories attached to")
    print("it. It's red, about 1 by 3 inches in size. Apparently produced by a company called COBY, but you don't know anything else about them. You set it to")
    print("shuffle today.")
    T = random.randint(1,50)
    print("The mp3 player is currently playing:"); print(mp3[T])
    pause()
    inv_manage()

def foldednote():
    print("An old note you keep in your jacket, a gift from the longest friendship you still have, and best you've ever had,")
    print("its content is a consistent source of comfort, occasionally a source of pain, but deeply important to you. She was")
    print("there when you started asking questions, and provided the greatest support as you began to understand yourself. It")
    print("wouldn't be an exageration to say that she is the person you love most in this world, and while you have no way to")
    print("prove it, you know there is a time where she would have said the same of you. Since then she moved to Alaska. You")
    print("can't help but feel a little betrayed by her, because she left you alone in this town, like that.")
    pause()
    inv_manage()

def pocketscissors():
    print("A pair of fold away scissors, in your experience people often find it weird that you always have scissors on you,")
    print("but that usually comes roughly 30 seconds before they realize that they need a cutting instrument.")
    pause()
    inv_manage()

def pen():
    print("A fairly standard capped pen, specifically a Pilot Precise V5, writes well on paper and skin.")
    pause()
    inv_manage()

def money():
    print("Money, cash, it can be used to purchase goods and services, you could get coffee, or access to some kind of private space. You don't") 
    print("usually have a lot of money, given that you've been unemployed for almost a full year, but it should be okay, today isn't really about") 
    print("shopping.")
    pause()
    inv_manage()

def largecoin():
    print("A fairy coin, technically on loan from a friend who got it at a rennaisance faire, she was showing it to you and as she")
    print("was talking, you found yourself fidgeting with it, spinning it through your fingers. At the time she said you could have")
    print("it, but you are unwilling to assume that means to keep it long term.")
    pause()
    inv_manage()

def usbstick():
    print("A USB stick, capacity: 16 GB, you use it for printing homework, or keeping backups of important things, right now if you recall it") 
    print("should be empty, but without access to a computer it is all but useless.")
    pause()
    inv_manage()

def notebook():
    print("A small notebook, you can use it to record how your day has been going!")
    menu = input("Save / Load").lower().strip()
    if menu == "save":
        save_game()
    elif menu == "load":
        load_game()
    
def oraclecards():
    print("You deftly pull out the deck of cards and pull the rubber band from binding the stack together onto your wrist, you quickly shuffle")
    print("while focusing on the strange day you're going through. Performing the requisite twisting to ensure a true shuffle for the oracle cards.")
    print("Though you aren't following any kind of specific spread, you figure that the first card should refer to yourself, the second to someone")
    print("important for your day, and the third to the current state of yourself and the world.")
    print("You go to draw the first card...")
    pause()
    if grth.count(1) in range(0,14): #upside down
        print("You pull a card with 'III - THE EMPRESS' emboldened across what would be the bottom if it were not upside down, the bulk of the card is")
        print("dedicated to an illustration of a woman sitting on a pink draped bed. Legs lifted so as to show the bottom of her bare thighs, she is")
        print("dressed in a thin white grecian dress, through which you can see the soft outlines of her body. A pair of blue snakes twist up her forearms")
        print("and in her right hand she holds a mirror. Her rich brown hair is done in braids, and upside down like this her expression seems to be an")
        print("almost mocking smile, like she knows something you haven't quite figured out yet.")
        pause()
        print("With the card upside down your eye is instinctively drawn to where her legs cross at the ankle, obscuring her groin. All in all from this")
        print("angle something about the illustration feels unbalanced and odd, like she might slip off the card and dissapear forever.")
        pause()
        print("You know that the upside down Empress often represents hardships, scarecity, bareness and neediness, this does very little to bring you")
        print("comfort.")
        pause()
    elif grth.count(1) in range(15,200):
        print("You pull a card with 'III - THE EMPRESS' emboldened across the bottom, the bulk of the card is dedicated to an illustration of a woman")
        print("sitting on a pink draped bed. Legs lifted so as to show the bottom of her bare thighs, she is dressed in a thin white grecian dress,")
        print("through which you can see the soft outlines of her body. A pair of blue snakes twist up her forearms and in her right hand she holds a")
        print("mirror. Her rich brown hair is done in braids, and rightside up you see her expression as more comfortably assured. Like she's looking")
        print("at something going the way she figures it should be.")
        pause()
        print("With the card rightside up she feels sturdy and confident, secure in her position, and comfortable no less. Your eye is naturally drawn")
        print("to her face where oddly you notice some features you share with her, that not quite bulbous nose you're used to seeing in the mirror,") 
        print("similarly thin eyes which you used to blame on others having difficulty reading you, but now seem so expressive on the empress.")
        print("You realize she sort of looks like how you wish you looked.")
        pause()
        print("You know that the rightside up Empress often represents nurturing, abundance, the feminine divine, and sovreignty over the natural order.") 
        print("That feels good, if those are the traits you've earned today, then maybe life will start to get a little easier going forward.")
        pause()
    else:
        print("You pull a rules card from the deck, it explains that your current growth as an individual stored as a number of appended '1' digits")
        print("in an array has managed to fall outside the range of 0 to 200, something which should not be physically possible within the mechanics")
        print("of the game.")
        pause()
    print("You go to draw the second card...")
    if comp[0] == 'no_one':
        D = random.randint(1,6)
        if D == 6:
            print("You manage to fumble and pull 5 cards. Do you want to {look} at all of them or just {move on}?")
            choice = input('> ').lower().strip()
            if choice == 'look' or 'look at cards' or 'look at all of them' or 'yes':
                print("The five cards end up face down in your hand, it's hard to say if you should flip them horizontally or vertically, you decide to flip")
                print("them without any respect to orinetation, afterall it was a mistake to pull this many at all, what the cards mean won't be all that")
                print("useful anyways.")
                pause()
                print("The first of the five you flip to look at is labeled at the bottom as '● ace of cups ●' much of the card is dedicated to an image of a")
                print("hand sticking out of the placid surface of water, holding a chalice, in which there is a large complex wave.")
                pause()
                print("The next you flip has a red border all around the image, in the border are a few blocks of text, going clockwise from the top left corner")
                print("the text reads 'CHALICES COPAS 9 COPPE COUPES BEKERS KELCHE' within the red border there is an illustration of two figures on a bench,")
                print("a man and a woman. The man has a sheet wrapped around, his lower half. While the woman is dressed only in thin semi-transparent light grey")
                print("underwear. They sit seemingly entranced by each other, hands entangled together.")
                pause()
                print("The next card you flip has a black border, in the top left is a downward pointing triangle in which is the numeral '2', in the top left")
                print("you see a block of text which reads 'WATER WASSER EAU AGUA' in the bottom left is the text 'ACQUA' and in the bottom right is printed")
                print("'♀ ♋︎' within the black border is an illustration of two figures, a man and a woman wading through waste deep water. The man has his arms")
                print("wrapped around the woman's neck almost like he's choking her, this reading is corroborated by the woman's poise and face, she's reaching")
                print("out, with an expression of desperation. She's wearing a thin brown blouse, from which her breasts are valiantly attempting to escape, a")
                print("mirror of their keepers desperation.")
                pause()
                print("You flip the third card of the bundle, it has a maroon border, at the top and bottom, on a an illustration of a brass plate there is the")
                print("numeral '6'. The illustartion consists of a pair of figures. A man and a woman, the man is almost entirely obscured as the woman sits on")
                print("his lap. Her dark red dress is riding up her legs exposing her thighs, on her left thigh lays the mans hand. The dress is entirely loosed")
                print("from the top, her breasts are exposed, wrapped by her arms with which she clings to herself. Behind the pair of figures leaning against")
                print("the wall behind them there are six wooden staffs.")
                pause()
                print("The final of the five cards you flip is nearly taken up entirely by its illustration, barring two small symbols at the bottom, the numeral")
                print("'3', and a pictograph of a sword. The illustration is of a woman with dark brown hair, she is dressed in armor and a cloak. She sits facing")
                print("away from the viewer, her legs folded beneath her. She sits in a puddle of blood, its source obvious as the woman appears to be drawing a")
                print("a sword out of her bleeding chest, on the wall behind her two more swords hang.")
                pause()
            elif choice == 'move on' or 'no':
                pass
        elif D == 5: #the girl
            print("You pull a card with a black border, in the top left is a downward pointing triangle in which is the numeral '2', in the top left")
            print("you see a block of text which reads 'WATER WASSER EAU AGUA' in the bottom left is the text 'ACQUA' and in the bottom right is printed")
            print("'♀ ♋︎' within the black border is an illustration of two figures, a man and a woman wading through waste deep water. The man has his arms")
            print("wrapped around the woman's neck almost like he's choking her, this reading is corroborated by the woman's poise and face, she's reaching")
            print("out, with an expression of desperation. She's wearing a thin brown blouse, from which her breasts are valiantly attempting to escape, a")
            print("mirror of their keepers desperation.")
        elif D == 4: #the statue
            print("You pull a card which is labeled at the bottom as '● ace of cups ●' much of the card is dedicated to an image of a hand sticking out of")
            print("the placid surface of water, holding a chalice, in which there is a large complex wave.")
        elif D == 3: #the drink
            print("You pull a card which is nearly taken up entirely by its illustration, barring two small symbols at the bottom, the numeral '3', and a")
            print("pictograph of a sword. The illustration is of a woman with dark brown hair, she is dressed in armor and a cloak. She sits facing away")
            print("from the viewer, her legs folded beneath her. She sits in a puddle of blood, its source obvious as the woman appears to be drawing a")
            print("sword out of her bleeding chest, on the wall behind her two more swords hang.")
        elif D == 2: #the writer
            print("You pull a card which has a red border all around the image, in the border are a few blocks of text, going clockwise from the top left corner")
            print("the text reads 'CHALICES COPAS 9 COPPE COUPES BEKERS KELCHE' within the red border there is an illustration of two figures on a bench, a man")
            print("and a woman. The man has a sheet wrapped around, his lower half. While the woman is dressed only in thin semi-transparent light grey underwear.")
            print("They sit seemingly entranced by each other, hands entangled together.")
        elif D == 1: #the fetish
            print("You pull a card which has a maroon border, at the top and bottom, on a an illustration of a brass plate there is the numeral '6'. The illustartion")
            print("consists of a pair of figures. A man and a woman, the man is almost entirely obscured as the woman sits on his lap. Her dark red dress is riding up") 
            print("her legs exposing her thighs, on her left thigh lays the mans hand. The dress is entirely loosed from the top, her breasts are exposed, wrapped by")
            print("her arms with which she clings to herself. Behind the pair of figures leaning against the wall behind them there are six wooden staffs.")
    elif comp[0] == 'the_girl': #The Hierophant
        if girl_grth.count(1) in range(0,14): #upside down
            print("You pull a card with a black border, it's upside down, the border has several blocks of text, if it were right side up, starting in the top left the text reads")
            print("'V  THE PRIEST DER PRIESTER LE PRETRE EL SACERDOTE ♉︎ IL SACERDOTE' within the border there is an illustration of a woman crouching against a pillar with her")
            print("knees splayed, she is nude from the waist down. She wears a low cut, black spotted, blouse. A cardinals hat obscurs her crotch, he is looking towards her. Her")
            print("her arms are tucked behind her back presumably supporting her from behind. Her pitch black hair billows and pleasure seems to erupt across her face.")
            pause()
            print("With the card upside down, the cardinals poise seems to be one of pause and appreciation towards the woman's provocation. The inverted view casts the rounded")
            print("top of the cardinals hat as a phallus approaching the woman's vagina, the angle creates a look of tension, as though her legs are going to burst with the difficulty")
            print("of her task.")
            pause()
            print("The deck this card is from, varies slightly from convention, but you know the card should correspond roughly to 'The Hierophant' which when inverted, you recall")
            print("represents arrogance, elitism, hypocrisy, and charlatanism. It brings you little joy to think of Sophie in this way, surely if she noticed she would have something")
            print("to say about the provocative imagery on the card. You aren't in the mood to be judged right now, so you slip the card under your Empress before Sophie catches on.")
            pause()
        elif girl_grth.count(1) in range(15,200): #upright
            print("You pull a card with a black border, the border has several blocks of text within it, starting in the top left and moving clockwise the text reads")
            print("'V  THE PRIEST DER PRIESTER LE PRETRE EL SACERDOTE ♉︎ IL SACERDOTE' within the border there is an illustration of a woman crouching against a pillar with her")
            print("knees splayed, she is nude from the waist down. She wears a low cut, black spotted, blouse. A cardinals hat obscurs her crotch, he is looking towards her. Her")
            print("pitch black hair billows, and her arms are tucked behind her back presumably supporting her from behind.")
            pause()
            print("With the card upside down, the cardinals pose reads as shock at the womans provacativity. Where once her expression seemed to read as pleasure it now looks to you")
            print("more like exertion. Perhaps she is not engaged in a sexual act, but one of desperation.")
            pause()
            print("The deck this card is from, varies slightly from convention, but you know the card should correspond roughly to 'The Hierophant' which when upright, you recall")
            print("representing wisdom, authority, knowledge, doctrine, and advice.") #connect to Sophie's development
            pause()
        else:
            print("You pull a rules card from the deck, it explains that the development of your relationship with Sophie stored as a number of appended")
            print("'1' digits in an array has managed to fall outside the range of 0 to 200, something which should not be physically possible within the")
            print("mechanics of the game.")
            pause()
    elif comp[0] == 'the_statue': #The Lovers
        if statue_grth.count(1) in range(0,14): #upright
            print("You pull a pleasant light cream card from the deck.") #to do
        elif statue_grth.count(1) in range(15,200): #upside down
            print('You pull') #to do
        else:
            print("You pull a rules card from the deck, it explains that the development of your relationship with Danielle stored as a number of appended")
            print("'1' digits in an array has managed to fall outside the range of 0 to 200, something which should not be physically possible within the")
            print("mechanics of the game.")
            pause()
    elif comp[0] == 'the_drink': #The Hermit
        if drink_grth.count(1) in range(0,14): #upside down
            print("You pull") #to do
        elif drink_grth.count(1) in range(15,200): #upright
            print("You pull") #to do
        else:
            print("You pull a rules card from the deck, it explains that the development of your relationship with [REDACTED] stored as a number of appended")
            print("'1' digits in an array has managed to fall outside the range of 0 to 200, something which should not be physically possible within the")
            print("mechanics of the game.")
            pause()    
    elif comp[0] == 'the_writer': #the Hanged Man
        if writer_grth.count(1) in range(0,14): #upside down
            print("You pull") #to do
        elif writer_grth.count(1) in range(15,200): #upright
            print("You pull") #to do
        else:
            print("You pull a rules card from the deck, it explains that the development of your relationship with Maddy stored as a number of appended")
            print("'1' digits in an array has managed to fall outside the range of 0 to 200, something which should not be physically possible within the")
            print("mechanics of the game.")
            pause()
    elif comp[0] == 'the_fetish': #the Devil
        if fetish_grth.count(1) in range(0,14): #upside down
            print("You pull") #to do
        elif fetish_grth.count(1) in range(15,200): #upright
            print("You pull") #to do
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
        print("You pull out a...") #to do
        inv_manage()
    elif choice == "no":
        inv_manage()
#Here is being worked on


#All of this stuff is for Inv Management, mostly it's done.

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

#These Two are untested things off the internet

def save_game(): #Save Function (Untested)
    with open("savefile.txt", "w") as f:
        f.write(",".join(inventory))

def load_game(): #Load Function (Untested)
    global inventory
    with open("savefile.txt", "r") as f:
        inventory = f.read().split(",")

cursce = [start_game]
loc = cursce[0]
car_loc = car_parked[0]
car_spot = ['home']
alc = []
abv = []
ang = []
# mp3 list is 50 long
mp3 = ['bedroom community by glass beach','Crumbs by Belaganas','Cecily Smith (Bonus Track) by Will Connolly','420-666-6969 by Peter France, Glam Cowgirl','Trace by Micah Marcos','I Was An Island by John-Allison Weiss','Girls Who Play Guitar by Maximo Park','Viva La Resistance by Hypernova','Lovecraft in Brooklyn by The Mountain Goats','City Never Sleeps by Tourism','i haunt ur dreams by hey, nothing','Brave as a Noun by AJJ','International Space Station by Sea Power','From Dusk to Dawn by Fever Dolls','Aphrodite, Your Electric Sexiness by Human Zoo','Brass Band by Jukebox The Ghost',"The Painter by I'm From Barcelona",'Gennifer Flowers by Fever Dolls','Love Me For Me by Sig Figs Collective','Underground by Cody Fry','Homecoming Serf by Sidney Gish','Presumably Dead Arm (617 Sessions) by Sidney Gish','Nickel by flipturn','Adeline by Fever Dolls','Talia by King Princess','a Castle of Rats by The Narcissist Cookbook','Grand Romantic Life by Mom Rock','Candlelight by Cinders','conversation by Coastal Club','Rule #3-Paperwork by Fish in a Birdcage','Rule #34 by Fish in a Birdcage','I Am the Answer by Overtown','Nail Salon by Cinders','From the Sea to the Land Beyond by Sea Power','Untouched by The Veronicas','Life Out of Phase by The Narcissist Cookbook','Sleep Walking by Cinders','Infatuation by Dudes and Their Guys','Dust and Stars(Zacks Thumb Reprise) by Blue Foster','Photos from When We Were Young by Nana Grizol','cold weather by glass beach','Moscow by Autoheart','Clean Slated State by The Altogether','Davy Crochet by The Backseat Lovers','Out of Vogue by Fever Dolls','Loaded by Primal Scream','Lets Dance to Joy Division by The Wombats','Worth It by Dudes and Their Guys','The Good Ship You by The Narcissist Cookbook','Mountain Sound by Of Monsters and Men','Rivers and Roads by The Head And The Heart','Peach Scone by Hobo Johnson','Get Used to It by Ricky Montgomery','Im Free by The Soup Dragons','yoshis island by glass beach','Last Snowstorm of the Year by Hippo Campus','This is Love by Air Traffic Controller']
comp = ['no_one']
inventory = {}
known_loc ={'water street','carson park','downtown','mall'}
hand = ['mp3 player'] #now we have an object that we can check against anytime the player opts to 'use'

#Companion development, card flips 
girl_grth = []
statue_grth = []
drink_grth = []
writer_grth = []
fetish_grth = []

#Win condition if grth = 15? then flip card
grth = []

start_screen() #has to be the very end. All "def scene():" must occur in the code before they are reffered to