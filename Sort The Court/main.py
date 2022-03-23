import random

people = 100
happiness = 100
gold = 100

characher = str(input("Choose king or queen by typing king or queen: "))

if characher == "king":
    print("Royal Advisor: My lord ,I'll help you rule your kingdom,but you have to make tough choices. Just say yes or no, understand? ")
    y_n = str(input())
    if y_n == "no":
        print("Very funny. Just give people theire answers, okay?")
    else:   
        print("Good! You've already got the hang of it.")
    input("Press Enter to continue...")
    print("Our city's still very small right now, but it certeainly has the potential to grow.")
    input("Press Enter to continue...")
    print("Perhaps one day we will have a bustling metropolis an you'll be invited to join the Council of Crowns!")
    input("Press Enter to continue...")
    print("Fow now all you need to concern yourself with is keeping the citizens happy and gowing our population.")
    input("Press Enter to continue...")
    print("Do your best, sir!")
    input("Press Enter to continue...")
else:
    print("Royal Advisor: My lady ,I'll help you rule your kingdom,but you have to make tough choices. Just say yes or no, understand? ")
    y_n = str(input())
    if y_n == "no":
        print("Very funny. Just give people theire answers, okay?")
    else:   
        print("Good! You've already got the hang of it.")
    input("Press Enter to continue...")
    print("Our city's still very small right now, but it certeainly has the potential to grow.")
    input("Press Enter to continue...")
    print("Perhaps one day we will have a bustling metropolis an you'll be invited to join the Council of Crowns!")
    input("Press Enter to continue...")
    print("Fow now all you need to concern yourself with is keeping the citizens happy and gowing our population.")
    input("Press Enter to continue...")
    print("Do your best, madam!")
    input("Press Enter to continue...")

while True:
    if happiness < 100:
        print("People are sad. The city is shrinking.")
    else:
        print("People are happy the city is growing.")
    print('You have ' ,people, ' people , ' ,happiness, ' happiness , ' ,gold, ' gold.')
    x = str(input("Want the next person to come in? "))
    characher_pick = random.randrange(1,32)

    if characher_pick == 1: 
        random_line = random.randrange(1,6)
        if random_line == 1:
            y_n =  str(input("The guards confiscated some gold that I, uh... found... Can I have it back?"))
            if y_n == "yes":
                gold = gold - 25
            else: 
                gold = gold + 25
        
        if random_line == 2:
            y_n =  str(input("Want me to steal from the rich and give to... you? Not just from the rich, I'll steal from whoever, basically."))
            if y_n == "yes":
                happiness = happiness - 5
                gold = gold + 50
            else:
                print("Ok")
        
        if random_line == 3:
            y_n =  str(input("The new high class housing district looks...intresting. Bet there's lots of cool stuff to...find...there. Can I have the key to the uptown district gate?"))
            if y_n == "yes":
                happiness = happiness + 3
            else:
                print("Ok")
        
        if random_line == 4:
            y_n = str(input("Hey, you helped me out before. I brought you something, just don't ask where it came from. Will you accept my gift?"))
            if y_n == "yes":
                gold = gold + 25
            else:
                print("Ok")
        
        if random_line == 5:
            y_n = str(input("We’re pals, right? Think you could find a home for my friend? He’s… between places right now, you could say…"))
            if y_n == "yes":
                people = people + 1
            else:
                happiness = happiness - 1
        
    if characher_pick == 2:
        y_n = str(input("(It's just...stareing at me...Does it want someting?)"))
        if y_n == "yes":
            gold = gold + 100
        else:
            print("Ok")
    
    if characher_pick == 3:
        random_line = random.randrange(1,4)
        if random_line ==  1:
            y_n =  str(input("Hello friend. Care to gaze into my magical vampire crystal?"))
            if y_n == "yes":
                random_choice = random.randrange(1,4)
                if random_choice == 1:
                    happiness = happiness + 5
                elif random_choice == 2:
                    people = people - 15
                    happiness = happiness -15
                else:
                    gold = gold + 50
            else:
                print("Ok")
        
        if random_line == 2:
            y_n =  str(input("I'm the Duke of Spook! Do you want a spooky nickname?"))
            if y_n == "yes":
                happiness = happiness + 1
                print("Hmm... You can be... The Creep King/Queen?")
            else:
                happiness = happiness - 1

        if random_line == 3:
            y_n = str(input("You feelin' spooky today?"))
            if y_n == "yes":
                people = people - 1
            else:
                print("Not even a little spook? Little baby bat?")
        
    if characher_pick == 4:
        random_choice = random.randrange(1,3)
        y_n = str(input("Hey bud, care to flip a coin with me? Heads, I give you buncha gold. Tails, I take a bunch of yer people's souls."))
        if y_n == "yes":
            if random_choice == 1:
                people = people - 15
                happiness = happiness - 10
            else: 
                gold = gold + 200
        else: 
            print("Ok")
        
    if characher_pick == 5:
        y_n =  str(input("Bok bok! (It's Running wild! Should we try to capture it?"))
        if y_n == "yes":
            people = people - 1
        else:   
            print("Ok")
    
    if characher_pick == 6:
        random_line =  random.randrange(1,7)
        if random_line == 1:
            y_n = str(input("Eeeh, Hello sweetie. Can I borrow a coin for the newspaper?"))
            if y_n == "yes":
                gold = gold - 1
                happiness = happiness + 1
            else: 
                happiness = happiness - 1
        if random_line == 2:
            y_n = str(input("Ooh dear, I read quite the troubling tale in the paper today... Think everything will be alright?"))
            if y_n == "yes":
                happiness = happiness + 1
                gold = gold - 1
            else:
                happiness = happiness - 1
        if random_line == 3:
            y_n = str(input("I read the nicest story in the paper today. Isn't it a lovely day?"))
            if y_n == "yes":
                happiness = happiness + 1
            else:
                happiness = happiness - 1
        if random_line == 4:
            y_n = str(input("Eeeeeh, I was considering opening up a soup shop? Think it's a good idea? I'd need some gold..."))
            if y_n == "yes":
                people = people + 10
                happiness = happiness + 5
                gold = gold - 50
            else:
                print("Ok")
        if random_line == 5:
            y_n = str(input("The soup shop's been doing well. I came to offer you some of our earnings."))
            if y_n == "yes":
                gold = gold + 15
            else:
                happiness = happiness + 2
        if random_line == 6:
            y_n = str(input("Eeeh...Can you tell those scientists to keep it down?"))
            if y_n == "yes":
                happiness = happiness + 2
            else:
                happiness = happiness - 2
    if characher_pick == 7:
        random_line = random.randrange(1,6)
        if random_line == 1:
            y_n = str(input("My lord! I've come across a chest of gold in my adventures! Will you please accept this gift?"))
            if y_n == "yes":
                gold = gold + 300
            else:
                print("Ok")
        if random_line == 2:
            y_n = str(input("My lord! I wish to embark upon a treacherous quest!"))
            if y_n == "yes":
                print("For the kingdom! I shall return to you!")
            else:
                print("Ok")
        if random_line == 3:
            print("I have returned from my quest! A great bounty of treasure is ours, my lord!")
        if random_line == 4:
            y_n = str(input("My lord, I have returned. I am ashamed to inform you that I return with nothing. Shall I show myself to the dungeons?"))
            if y_n == "yes":
                people = people - 1
            else:
                happiness = happiness + 1
        if random_line == 5: 
            y_n = str(input("I saw a beautiful silver gauntlet in the blacksmith's today. May I have funds to purchase it?"))
            if y_n == "yes":
                happiness = happiness + 3
                gold = gold - 50
            else:
                happiness = happiness - 1
    
    if characher_pick == 8:
        random_line = random.randrange(1,6)
        if random_line == 1:
            y_n = str(input("Name's Molder. If you want to know the truth about... everything... you're gonna want to hire me."))
            if y_n == "yes":
                gold = gold - 10
            else:
                print("Ok")
        if random_line == 2:
            y_n = str(input("I... couldn't uncover anything. I was being followed. Too risky. Did you see anyone follow me out of the castle?"))
            if y_n == "yes":
                print("Ok")
            else:
                print("Ok")
        if random_line == 3:
            y_n = str(input("You ready for the truth? Aliens have already landed, and they're in our city. You think we're safe?"))
            if y_n == "yes":
                people = people + 7
                happiness = happiness + 1
            else:
                people = people + 7
        if random_line == 4:
            y_n = str(input("I'm back. I discovered an alien conspiracy to cover up large amounts of gold. Do you believe in aliens?"))
            if y_n == "yes":
                gold = gold + 50
            else:
                gold = gold + 50
    
    if characher_pick == 9:
        random_line = random.randrange(1,11)
        if random_line == 1:
            y_n = str(input("We've captured some foes on the battle field. Shall we bring them home and put them to work?"))
            if y_n == "yes":
                people = people + 8
                gold = gold + 20
            else:
                print("Ok")
        if random_line == 2:
            y_n = str(input("Shall we ransom the captured foes off for a bit of gold?"))
            if y_n == "yes":
                golg = gold + 100
            else:
                print("Ok")
        if random_line == 3:
            y_n = str(input("Might I put them in the dungeons then?"))
            if y_n == "yes":
                print("Ok")
            else:
                people = people + 5
        if random_line == 4:
            y_n = str(input("One of our prisoners has escaped! May I have some gold to offer a reward for her recapture?"))
            if y_n == "yes":
                gold = gold - 50
                happiness = happiness + 3
            else:
                people = people - 1
        if random_line == 5:
            y_n = str(input("The escaped prisoner has been recaptured thanks to the bounty you offered."))
            if y_n == "yes":
                print("Ok")
            else: 
                print("Ok")
        if random_line == 6:
            y_n = str(input("A nearby town has asked us to form an alliance with them. Should we use them to beef up our ranks?"))
            if y_n == "yes":
                people = people + 15
            else: 
                print("Ok")
        if random_line == 7:
            y_n = str(input("The town we made an alliance with is in trouble! Should we send soldiers to assist them?"))
            if y_n == "yes":
                people = people - 10
            else:
                happiness = happiness - 5
        if random_line == 8:
            y_n = str(input("Our allies have denounced us for refusing to aid them in battle. We'll lose a bit of confidance from our citizens due to this."))
            if y_n == "yes":
                print("Ok")
            else:
                print("Ok")
        if random_line == 9:
            y_n = str(input("The tribes from South we gave weapons to, have taken arms against us. Might I request additional funds so that we are able to adequately combat them?"))
            if y_n == "yes":
                gold = gold + 100
            else:
                happiness = happiness - 1
        if random_line == 10:
            y_n = str(input("The tribes from the South we gave weapons to, have taken arms against us. Their combat strength, however, is limited. I believe we can vanquish them with minimal additions to our arsenal. Might I request a modest sum of gold with which to organize a resistance?"))
            if y_n == "yes":
                print("Ok")
            else: 
                print("Ok")
        
    if characher_pick == 10:
        y_n = str(input("Ook ook ook!(He's got a shiny coin!"))
        if y_n == "yes":
            gold = gold + 5
        else:
            print("Ok")
    
    if characher_pick == 11:
        y_n = str(input("I wish to construct a tavern, but I'll need some gold from you to make it happen. I'm talking a considerable amout of gold, here. Like...a coiple hundred, at least. What do you think?"))
        if y_n == "yes":
            gold = gold - 200
            happiness = happiness + 3
        else:
            print("Ok")
            happiness = happiness - 3
    
    if characher_pick == 12:
        random_line = random.randrange(1,31)
        if random_line == 1:
            y_n = str(input("Builders wish to construct more houses in the town. They request gold, with which they could build much faster!"))
            if y_n == "yes":
                gold = gold - 100
                people = people + 7
            else:
                people = people + 3
        if random_line == 2:
            y_n = str(input("Some very strange creatures wish to move into the houses we built. Should we allow it?"))
            if y_n == "yes":
                people = people + 4
                happiness = happiness + 4
            else:
                happiness = happiness - 2
        if random_line == 3:
            y_n = str(input("Some families have moved into the new houses we built. Should we send them a welcome basket?"))
            if y_n == "yes":
                people = people + 6
                happiness = happiness + 3
                gold = gold - 20
            else:
                print("Ok")
        if random_line == 4:
            y_n = str(input("Villagers are complaining about garbage in the streets. Shall we hire workers to clean it up?"))
            if y_n == "yes":
                gold = gold - 50
                happiness = happiness + 2
            else:
                happiness = happiness - 1
        if random_line == 5:
            y_n = str(input("My lord, a man wishes to settle a dispute. He says he is way cool, but his friend says he is not. Do you think he is cool?"))
            if y_n == "yes":
                happiness = happiness + 1
            else:
                print("Ok")
        if random_line == 6:
            y_n = str(input("There's a very stinky kid running around the streets. Should we force her to have a bath?"))
            if y_n == "yes":
                happiness = happiness - 1
            else:
                happiness = happiness + 1
        if random_line == 7:
            y_n = str(input("Citizens say a monkey has been running around flinging... stuff... at them. Should we put out a bounty on it?"))
            if y_n == "yes":
                happiness = happiness + 1
                gold = gold - 30
            else:
                happiness = happiness - 2
        if random_line == 8:
            y_n = str(input("Fires have been breaking our frequently on Cabbage Street. Shall we install a well to make water more accessible there?"))
            if y_n == "yes":
                happiness = happiness + 5
                gold = gold - 150
            else:
                happiness = happiness - 3
                people = people - 3
        if random_line == 9:
            y_n = str(input("The prison is in need of repairs. Might there be room in the budget to devote a few hundred gold to it?"))
            if y_n == "yes":
                gold = gold - 250
            else:
                happiness = happiness - 10
        if random_line == 10:
            y_n = str(input("There's a petition going around to open our borders to the neighbouring town. What do you say?"))
            if y_n == "yes":
                people = people + 30
                happiness = happiness + 10
                gold = gold +50
            else:
                print("Ok")
        if random_line == 11:
            y_n = str(input("Since we opened our borders, travellers from all around are joining our city. Doesn't that just warm your heart?"))
            if y_n == "yes":
                gold = gold + 5
                people = people + 4
                happiness = happiness + 2
            else:
                print("Ok")
        if random_line == 12:
            y_n = str(input("The people have started a petition to ban pineapples in the city. Should we do it?"))
            if y_n == "yes":
                happiness = happiness + 3
                gold = gold - 10
            else:
                happiness = happiness - 2
        if random_line == 13:
            y_n = str(input("An angry pineapple trader has denounced your rule! Shall we have her arrested?"))
            if y_n == "yes":
                people = people - 1
            else:
                happiness = happiness - 5
        if random_line == 14:
            y_n = str(input("Without any gold, we're a bit stuck. We could sell off some of our goods, but that might make people sad. Should we do it?"))
            if y_n == "yes":
                gold = gold + 250
                happiness = happiness -15
            else:
                print("Ok")
        if random_line == 15:
            y_n = str(input("The guild of pineapple traders offers you a gift, (sir/madam)! Will you accept it?"))
            if y_n == "yes":
                gold = gold + 100
            else:
                print("Ok")
        if random_line == 16:
            y_n = str(input("Some villagers are threatening to leave unless we pay them a sum of gold. Should we listen to their demands?"))
            if y_n == "yes":
                gold = gold - 50
            else:
                people = people - 6
        if random_line == 17:
            y_n = str(input("Some refugees have arrived in town. Should we welcome them?"))
            if y_n == "yes":
                people = people + 15
                happiness = happiness + 3
            else:
                happiness = happiness - 2
        if random_line == 18:
            y_n = str(input("A petition to bring the circus to town is circulating. Could attract tourists, are you interested?"))
            if y_n == "yes":
                people = people + 10
                happiness = happiness + 10
                gold = gold + 100
            else:
                happiness = happiness - 5
        if random_line == 19:
            y_n = str(input("The owners of the tavern are making piles of gold, and wish to share some with you!"))
            if y_n == "yes":
                gold = gold + 100
            else:
                happiness = happiness + 3
        if random_line == 20:
            y_n = str(input("There's been a brawl at the tavern. Should we arrest those responsible for starting it?"))
            if y_n == "yes":
                happiness = happiness + 1
            else:
                happiness = happiness - 1
        if random_line == 21:
            y_n = str(input("Our granary stock has been infected. It'll cost us to replace it, but if we don't people could get sick. Should we do it?"))
            if y_n == "yes":
                happiness = happiness + 1
                gold = gold - 70
            else:
                people = people - 3
                happiness = happiness - 1
        if random_line == 22:
            y_n = str(input("The extra food we've been able to store in our granaries has attracted more settlers. Shall we let them in?"))
            if y_n == "yes":
                people = people + 5
                happiness = happiness + 1
            else: 
                happiness = happiness - 1
        if random_line == 23:
            y_n = str(input("The town wants to exile a notorious criminal. His crimes include theft, arson, and forgery. What do you say, shall we exile him?"))
            if y_n == "yes":
                gold = gold - 50 
                happiness = happiness + 3
            else:
                happiness = happiness - 3
        if random_line == 24:
            y_n = str(input("The treasury is empty, my lord. We could raise taxes a bit further, but the people won't like it much. Should we try?"))
            if y_n == "yes":
                gold = gold + 200
                people = people - 4
                happiness = happiness - 10
            else:
                print("Ok")
        if random_line == 25:
            y_n = str(input("I noticed that this wizard is bothering you. Should we banish the"))
            if y_n == "yes":
                people = people - 1
            else: 
                print("Ok")
        if random_line == 26:
            y_n = str(input("Since we opened our borders, trade from our caravans has increased dramatically. Do you wish to tax the merchants?"))
            if y_n == "yes":
                gold = gold + 100
                happiness = happiness - 2
            else:
                happiness = happiness - 6
        if random_line == 27:
            y_n = str(input("Shall we devote more gold to the hiring of tour guides?"))
            if y_n == "yes":
                gold = gold - 70
                happiness = happiness + 3
            else:
                print("Ok")
        if random_line == 28:
            y_n = str(input("Our road network is expanding and is in need of maintenance. Is there room in the budget?"))
            if y_n == "yes":
                gold = gold - 100
            else:
                happiness = happiness - 5
        if random_line == 29:
            y_n = str(input("I've collected some incomes from the circus. Would you like me to tax them?"))
            if y_n == "yes":
                gold = gold + 100
                happiness = happiness - 3
            else: 
                happiness = happiness + 5
        if random_line == 30:
            y_n = str(input("We've apprehended a girl trying to climb over the castle gates. We have fined her for her actions."))
            if y_n == "yes":
                input("Press Enter to continue...")
            else:
                input("Press Enter to continue...")
            
    if characher_pick == 13:
        random_line = random.randrange(1,4)
        if random_line == 1:
            random_choice = random.randrange(1,4)
            y_n = str(input("I was just passing through and thought you might like some magic. Anything could happen! Care to give it a try?"))
            if y_n == "yes":
                if random_choice == 1:
                    gold = gold + 100
                    people = people + 20
                    happiness = happiness + 5
                if random_choice == 2:
                    gold = gold + 200
                if random_choice == 3:
                    people = people - 10
                    happiness = happiness - 15
            else:
                print("Ok")
        if random_line == 2:
            y_n = str(input("Have you seen my magical cat, Pancake?"))
            if y_n == "yes":
                happiness = happiness + 2
            else:
                happiness = happiness - 2
        if random_line == 3:
            y_n = str(input("Ohoho! I heard you need some help breaking a curse. I could lend my assistance, for a small fee..."))
            if y_n == "yes":
                gold = gold - 40
                happiness = happiness +3
            else:
                happiness = happiness - 3
        
    if characher_pick == 14:
        random_line = random.randrange(1,10)
        if random_line == 1:
            y_n = str(input("Do you find me humerus?"))
            if y_n == "yes":
                happiness = happiness + 2
            else:
                print("Ok")
        if random_line == 2:
            y_n = str(input("You've got a skeleton of your own, you know. Don't you find it weird that you can't see it?"))
            if y_n == "yes":
                print("Ok")
            else:
                print("Ok")
        if random_line == 3:
            y_n = str(input("Some of the villagers mentioned they saw an alien walking around. You know anything about this?"))
            if y_n == "yes":
                print("Ok")
            else:
                gold = gold + 20
        if random_line == 4:
            y_n = str(input("Any mysteries afoot? I can do some snooping for a small fee if you're interested..."))
            if y_n == "yes":
                gold = gold - 10
            else:
                print("Ok")
        if random_line == 5:
            y_n = str(input("Reporting in! I figured out a mysterious new way to make gold. Want to know how?"))
            if y_n == "yes":
                gold = gold + 50
            else:
                gold = gold + 25
        if random_line == 6:
            y_n = str(input("Reporting in! I discovered an underground crime ring in the city's eastern ward...Could I have a bit of extra gold to bring in the guard and make some additional arrests?"))
            if y_n == "yes":
                happiness = happiness + 3
                gold = gold - 40
            else:
                print("Ok")
        if random_line == 7:
            y_n = str(input("Reporting in! I found a way to summon people from another dimension. Want me to summon some folks?"))
            if y_n == "yes":
                people = people + 20
            else:
                print("Ok")
        if random_line == 8:
            y_n = str(input("Reporting in! I solved the mystery about who stole Mrs. Pumpkin's baking pan. Want me to turn him in?"))
            if y_n == "yes":
                people = people - 1
                happiness = happiness + 3
            else:
                happiness = happiness - 1
        if random_line == 9:
            y_n = str(input("Reporting in! I managed to catch the necromancer behind a recent string of possessions."))
            if y_n == "yes":
                print("Ok")
            else:
                print("Ok")
    
    if characher_pick == 15:
        y_n = str(input("You haven't been talking to Skelly, have you?"))
        if y_n == "yes":
            print("Ok")
        else:
            print("Ok")
    
    if characher_pick == 16:
        random_line = random.randrange(1,5)
        if random_line == 1:
            y_n = str(input("Ohooooo! Might I have some gold for new juggling balls"))
            if y_n == "yes":
                happiness = happiness + 5
                gold = gold - 10
            else:
                happiness = happiness - 5
        if random_line == 2:
            y_n = str(input("Oooooooo! I wish to put on a shoooooooow! May I have the funds ot do soooo?"))
            if y_n == "yes":
                gold = gold - 50
            else:
                happiness = happiness - 2
        if random_line == 3:
            y_n = str(input("My shooooooow seems to have goooone over well! I wish to expand my proooooduction! Funds I shall need! Foooour hundred goooooold or soooooooo!"))
            if y_n == "yes":
                gold = gold - 400
            else:
                happiness = happiness - 3
        if random_line == 4:
            y_n = str(input("I dooo believe I have perfected my shoooooow! Gooold, it does require, but happiness it shall bring! Ohohoho! Seven hundred gooold, my loooord, and I can put on my shooow once mooooore!"))
            if y_n == "yes":
                gold = gold - 700
            else:
                happiness = happiness - 1
        
    if characher_pick == 17:
        random_line = random.randrange(1,8)
        if random_line == 1:
            y_n == str(input("I've got a friend from witch school looking to move to town. Could I get a couple gold to help her move in?"))
            if y_n == "yes":
                people = people - 1
                happiness = happiness + 3
                gold = gold - 3
            else:
                people = people + 1
                happiness = happiness - 4
        if random_line == 2:
            y_n = str(input("My friend from witch school wanted to thank you for your help, so we made you some magical cookies!"))
            if y_n == "yes":
                input("Press Enter to continue...")
            else:
                input("Press Enter to continue...")
        if random_line == 3:
            y_n = str(input("My broom's all worn out, and it's my birthday...Think you could buy me a new broom for a present? Sure would be nice of you!"))
            if y_n == "yes":
                happiness = happiness + 3
                gold = gold - 50
            else:
                happiness = happiness - 3
        if random_line == 4:
            y_n = str(input("The spirits are appeased right now, but perhaps we should grant them an offering of gold. What do you say? Two hundred gold would make a decent offering."))
            if y_n == "yes":
                gold = gold - 200
            else:
                print("Ok")
        if random_line == 5:
            y_n = str(input("There's a buncha goblins in the lower quarter. I'll slay 'em for a few gold coins if you want."))
            if y_n == "yes":
                happiness = happiness + 4
                gold = gold - 10
            else:
                happiness = happiness - 4
        if random_line == 6:
            y_n = str(input("Looking for coins? I could cast some dark magic to summon some gold, but it might cost a soul or two..."))
            if y_n == "yes":
                people = people - 2
                gold = gold + 200
            else:
                print("Ok")
        if random_line == 7:
            y_n = str(input("Break Chester's curse."))
            if y_n == "yes":
                happiness = happiness + 1
                gold = gold - 40
            else:
                print("Ok")

    if characher_pick == 18:
        random_line = random.randrange(1,7)
        if random_line == 1:
            y_n = str(input("Ahem. Might I get a cup of tea for you, my liege?"))
            if y_n == "yes":
                gold = gold - 3
                happiness = happiness + 3
            else:
                print("Ok")
        if random_line == 2:
            y_n = str(input("You've been drinking quite a bit of tea, sir. Might I upgrade you to... the good stuff?"))
            if y_n == "yes":
                happiness = happiness + 3
            else:
                print("Ok")
        if random_line == 3:
            y_n = str(input("Another cup of tea, my liege? I've got more of that good stuff you like..."))
            if y_n == "yes":
                happiness = happiness + 3
                gold = gold - 10
            else:
                print("Ok")
        if random_line == 4:
            y_n = str(input("There's a party I'd like to go to this evening, my liege/lady. Might I have the rest of the day off?"))
            if y_n == "yes":
                happiness = happiness + 3
            else:
                happiness = happiness - 3
        if random_line == 5:
            y_n = str(input("My liege, there is a man in the foyer asking to join your guard. He's got an eyepatch, looks a little shifty. What do you think, should we take a chance on this stranger?"))
            if y_n == "yes":
                people = people + 1
            else:
                happiness = happiness - 1
        if random_line == 6:
            y_n = str(input("That man you hired earlier has gone missing, sire. Shall we send a search party?"))
            if y_n == "yes":
                people = people - 1
                gold = gold - 5
            else:
                people = people - 1
            
    if characher_pick == 19:
        y_n = str(input("Booo! Give me your gold or I'll eat your townspeople!"))
        if y_n == "yes":
            gold = gold - 400
        else:
            people = people - 30

    if characher_pick == 20:
        random_line = random.randrange(1,3)
        if random_line == 1:
            y_n = str(input("Good day sir/madam. Do you require any haunting services? For a small price, I'll scare some people for you."))
            if y_n == "yes":
                gold = gold - 5
                people = people - 1
            else:
                print("Ok")
        if random_line == 2:
            y_n = str(input("Hmph. You call this a castle?"))
            if y_n == "yes":
                happiness = happiness + 1
            else:
                happiness = happiness - 1

    if characher_pick == 21:
        y_n = str(input("I would like some money please."))
        if y_n == "yes":
            gold = gold - 100
            happiness = happiness + 3
        else:
            happiness = happiness - 3

    if characher_pick == 22:
        random_line = random.randrange(1,8)
        if random_line == 1:
            y_n = str(input("Aha, that cog you have there... I wish to purchase it! Why? I have my reasons, good King! Might I offer a sum of, say, one thousand gold coins?"))
            if y_n == "yes":
                gold = gold + 1000
            else:
                print("Ok")
        if random_line == 2:
            y_n = str(input("I've got a business proposition for you and your tiny little town. Are you interested?"))
            if y_n == "yes":
                print("Ok")
            else:
                print("Ok")
        if random_line == 3:
            y_n = str(input("A caravan of mine wishes to camp in your city for the next few days. Might that be arranged?"))
            if y_n == "yes":
                people = people + 10
            else:
                print("Ok")
        if random_line == 4:
            y_n = str(input("An Offer For You Friend. I would like to purchase luxury goods from you for a fair price."))
            if y_n == "yes":
                gold = gold + 300
                happiness = happiness - 15
            else:
                print("Ok")
        if random_line == 5:
            y_n = str(input("An Offer For You Friend. I would like to sell you luxury goods for a fair price."))
            if y_n == "yes":
                gold = gold - 200
                happiness = happiness + 25
            else:
                print("Ok")
        if random_line == 6:
            y_n = str(input("Would you like to open a trade deal between our cities?..."))
            if y_n == "yes":
                gold = gold + 100
                people = people + 10
            else:
                print("Ok")
        if random_line == 7: 
            y_n = str(input("A caravan of mine wishes to camp in your city for the next few days. Might that be arranged?")) 
            if y_n == "yes":
                people = people + 10
            else:
                print("Ok")

    if characher_pick == 23: 
        y_n = str(input("My boat's too tiny to catch many fish. Can I have some gold to upgrade it? I'll pay you back, I swear..."))
        if y_n == "yes":
            gold = gold - 100
            happiness = happiness + 3
        else:
            happiness = happiness - 3

    if characher_pick == 24:
        y_n = str(input("Mom says I need to ask your permission to go on an adventure. So can I? Please? Please?"))
        if y_n == "yes":
            happiness = happiness + 2
        else:
            happiness = happiness - 2

    if characher_pick == 13:
        y_n = str(input("Bum bum badum dum dum! Booooosh! Yeah!! You like my rythm,bruh?"))
        if y_n == "yes":
            happiness = happiness + 3
        else:
            happiness = happiness - 3
    
    if characher_pick == 25:
        random_line = random.randrange(1,8)
        if random_line == 1:
            y_n = str(input("I'm a blacksmith and I'd like to set up a shop here. I can pay my own way, I just need your permission. What do you say?"))
            if y_n == "yes":
                people = people + 3
                happiness = happiness + 2
            else:
                print("Ok")
        if random_line == 2:
            y_n = str(input("Would you like to purchase any swords for your guards? A well protected city is a happy city!"))
            if y_n == "yes":
                happiness = happiness + 10
                gold = gold - 20
            else:
                print("Ok")
        if random_line == 3:
            y_n = str(input("My sales have brought in record profits, and I'd like to give you something as thanks. Will you accept my gift?"))
            if y_n == "yes":
                gold = gold + 40
            else:
                print("Ok")
        if random_line == 4:
            y_n = str(input("Sir, I heard about the dragon attack you were made to endure. I've come up with an idea to strike back. I'll need to track down the finest metals, but they're quite costly. Might I have a few hundred gold to begin my search?"))
            if y_n == "yes":
                gold = gold - 300
            else:
                print("Ok")
        if random_line == 5:
            y_n = str(input("Sir, about the Dragonblade... Yes, that's what I'm calling the sword now. I've purchased some top quality metals, but I'll need workers to help me do the crafting. Can you spare a few men?"))
            if y_n == "yes":
                people = people - 5
            else:
                print("Ok")
        if random_line == 6:
            y_n = str(input("It's finally done! I've finished crafting the Dragonblade! All we need now is somebody to wield it."))
            input("Press Enter to continue...")
        if random_line == 7:
            y_n = str(input("Sir, a people from the South have been asking for weapons. Do I have your permission to supply them? I'll need some extra gold to help fill the order."))
            if y_n == "yes":
                gold = gold - 100
            else:
                happiness = happiness + 1

    if characher_pick == 26:
        y_n = str(input("Meeow. (Looks like he wants somebody to pat his belly..."))
        if y_n == "yes":
            happiness = happiness + 1
        else:
            happiness = happiness - 1

    if characher_pick == 27:
        random_line = random.randrange(1,7)
        if random_line == 1:
            y_n = str(input("Bonjour! My name is Madame Abeille, and I've come to join your court. Will you have me?"))
            if y_n == "yes":
                people = people + 1
            else:
                happiness = happiness - 1
        if random_line == 2:
            y_n = str(input("Bonjour. I have returned to give you a chance to reconsider. Might I join your court?"))
            if y_n == "yes":
                people = people + 1
            else:
                happiness = happiness - 1
        if random_line == 3:
            y_n = str(input("Bonjour! I've just finished moving in, but i would like to request an assistant of my own. May I have but 1 person?"))
            if y_n == "yes":
                people = people - 1
            else:
                print("Ok")
        if random_line == 4:
            y_n = str(input("My assistant and I have found a way to make some extra gold by trading sweets. Are you interested?"))
            if y_n == "yes":
                gold = gold + 150
            else:
                print("Ok")
        if random_line == 5:
            y_n = str(input("Bonjour! Proceeds from the candy trade have been rolling in steadily. Do you wish to collect your taxes?"))
            if y_n == "yes":
                gold = gold + 35
            else:
                print("Ok")
        if random_line == 6:
            y_n = str(input("I accidentally stayed up all night eating candies... Can I have some gold to go to the doctor?"))
            if y_n == "yes":
                gold = gold - 10
            else:
                happiness = happiness - 5

    if characher_pick == 28:
        random_line = random.randrange(1,6)
        if random_line == 1:
            y_n = str(input("Hey uhhhhh, it's sliiiiiime day... Got a preeeesent for meeeee?"))
            if y_n == "yes":
                gold = gold - 5
                happiness = happiness + 2
            else:
                happiness = happiness - 1
        if random_line == 2:
            y_n = str(input("Hey uhhhh, somebody came by and cleeeeeaned up my hooooome. You gonna pay me baaaack for that?"))
            if y_n == "yes":
                gold = gold - 10
            else:
                happiness = happiness - 5
        if random_line == 3:
            y_n = str(input("Hey uhhhh, you think you could tell people to stoooop callin' me 'slimeball'? It's hurtin' my feeeeelings..."))
            if y_n == "yes":
                happiness = happiness - 3
            else:
                happiness = happiness - 3
        if random_line == 4:
            y_n = str(input("Hey uhhhh, I think there's something going oooooon in the seeeeeeeewers...I've been hearing some weird soooooooounds... I could go investigate if you waaaaant..."))
            if y_n == "yes":
                gold = gold - 50
            else:
                print("Ok")
        if random_line == 5:
            y_n = str(input("I found some monsters in the seeeeewers... I cleaned them up with my gooooooooop...Nooooooothing to wooooorry about anymoooooore..."))
            if y_n == "yes":
                happiness = happiness + 1
            else:
                happiness = happiness - 5
    
    if characher_pick == 29:
        random_line = random.randrange(1,7)
        if random_line == 1:
            y_n = str(input("Plants are interesting, don't you think? I would like to open a garden, may I have some workers to help me?"))
            if y_n == "yes":
                people = people - 3
            else:
                happiness = happiness - 1
        if random_line == 2:
            y_n = str(input("We've completed work on the garden. Are you pleased?"))
            if y_n == "yes":
                people = people + 3
                happiness = happiness + 5
            else:
                print("Ok")
        if random_line == 3:
            y_n = str(input("Some nasty bugs have made a home out of our garden! Can we have some gold to hire an exterminator?"))
            if y_n == "yes":
                happiness = happiness + 3
                gold = gold - 25
            else:
                happiness = happiness - 6
        if random_line == 4:
            y_n = str(input("Would you like to buy some flowers from our garden? They're a special low price for you, sir/madam!"))
            if y_n == "yes":
                happiness = happiness + 7
                gold = gold - 5
            else:
                people = people + 3
        if random_line == 5:
            y_n = str(input("Some plant people have sprouted in the gardens. Are we allowed to make them official citizens?"))
            if y_n == "yes":
                people = people + 5
            else:
                happiness = happiness - 2
        if random_line == 6:
            y_n = str(input("The plant People citizens have taken root and grown into a lovely field of flowers. Can you hear them rejoicing?"))
            if y_n == "yes":
                happiness = happiness + 15
            else:
                happiness = happiness + 10

    if characher_pick == 30:
        y_n = str(input("Mew. (This cat seems slightly magical. Not sure what it wants, tough..."))
        if y_n == "yes":
            happiness = happiness + 1
        else:
            happiness = happiness - 1

    if characher_pick == 31:
        random_line = random.randrange(1,5)
        if random_line == 1:
            y_n = str(input("Allo, Ma,am Are you looking for experienced barbers in your court?"))
            if y_n == "yes":
                people = people + 1
            else:
                print("Ok")
        if random_line == 2:
            y_n = str(input("Demands for my services are through the roof! May I have your permission to raise my prices?"))
            if y_n == "yes":
                happiness = happiness + 3
                gold = gold + 50
            else:
                happiness = happiness - 1
        if random_line == 3:
            y_n = str(input("It is nice to see you, sir. Do you like my new haircut?"))
            if y_n == "yes":
                happiness = happiness + 7
            else:
                print("Ok")
        if random_line == 4:
            y_n = str(input("Citizens from far and wide come to visit my barbershop! Would you like a fresh cut, sir? Free of charge!"))
            if y_n == "yes":
                happiness = happiness + 3
            else:
                happiness = happiness + 3

    if x == "no":
        break
    