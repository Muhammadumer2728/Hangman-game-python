import random


#Dictionaries 
countries = ["england","chile","brazil","guinea","paraguay","maldives","canada","vietnam","palestine","mexico","ethiopia","thailand","tanzania","argentina","belgium","belarus","colombia","finland","jamaica","lebanon","libya"]
car = ["toyota ", "honda", "ford", "chevrolet", "rollsroyce", "mercedes", "tesla", "volkswagen", "nissan", "suzuki", "hyundai", "mclaren", "audi", "porsche", "ford", "lamborghini", "mazda", "lexus", "cadillac", "ferrari","bently"]
animal = ["lion","koala","tiger","panda","snake","owl","shark","turtle","wolf","parrot","frog","bear","seal","bat","swan","dolphin","horse","chimp","zebra","mouse"]
cities = ["tokyo", "bali", "london", "paris", "beijing", "sydney", "mumbai", "riyadh", "istanbul", "cairo", "islamabad", "karachi", "lahore", "faisalabad", "rawalpindi", "multan", "peshawar", "quetta", "sialkot", "abbottabad"]   


#The Hangman graphic
hangman = ('''
     +----+
     |    |
          |    
          |
          |
          |    
===========    
''')
hangman1 = ('''
     +----+
     |    |
     0    |
          |
          |
          |
===========    
''')
hangman2 = ('''
     +----+
     |    |
     0    |
     |    |
     |    |
          |
===========    
''')
hangman3 = ('''
     +----+
     |    |
     0    |
    /|\   |
     |    |
          |
===========
''')
hangman4 = ('''
     +----+
     |    |
     0    |
    /|\   |
     |    |
    / \   |
===========
''')
while True:
    difficulty = input ("Enter Difficulty\nEasy(press E)/hard(press H) :") . lower() #User chooses Difficulty of the game
    #initializing variables
    display = []
    wrong_letter = []
    tries = 1
    x = 0
    
    
    #code for choosing difficulty
    if difficulty == 'h':
        category = [car , countries]
    elif difficulty == 'e':
        category = [animal , cities]
    else:
        print ('Invalid input try again')
        continue
    
    
    #code for choosing the category randomly acc to difficulty and printing relative hint
    choose_category = random.randint (0 , 1)
    if choose_category == 0 and difficulty == 'e':
        print ('Hint *\nIts an animal')
    elif choose_category == 1 and difficulty == 'e':
        print ('Hint *\nIts a city',)
    if choose_category == 0 and difficulty == 'h':
        print ('Hint *\nIts an car')
    elif choose_category == 1 and difficulty == 'h':
        print ('Hint * \nIts a country',)
        
        
        #randomly choosing the word from before choosen category
    elements = random.randint (0 , 20)
    word = (category [choose_category]) [elements]
    print (hangman)
    
    
    #code for printing blanks acc to length of word
    for word_len in range (len(word)):
        display += '_'
    print(display)
    
    
    #code for taking input and checking ,if right placing it on right blank or if guessed before printing already guessed using a while a loop 
    while tries <= 5:
        guess_letter = input ("Guess a letter :") . lower()
        for position in range (len(word)):
            letter = word [position]
            if letter == guess_letter:
                if guess_letter in display [position]:
                    print('Already guessed \nThis letter is at blank', position + 1)
                else:
                    display [position] = guess_letter
                    print('Right Guess at blank :', position + 1)
        print (display)
        
        
        #if guessed wrong print wrong letter and incrementing the tries or already guessed and adding it into wrong letter dictionary 
        if guess_letter not in word: 
            if guess_letter in wrong_letter:
                print( " Already guessed this wrong letter " )
            else:
                wrong_letter +='_'
                wrong_letter [x] = guess_letter
                x += 1
                print('Wrong letter')
                
                
                #setting tries limit 
                tries += 1
                if tries == 2:
                    print(hangman1)
                if tries == 3:
                    print(hangman2)
                if tries == 4:
                    print(hangman3)
                if tries == 5:
                    print(hangman4)
                    
        
        #code when blanks are filled \ guessed the word
        if '_' not in display:
            print('YOU WIN \nThe word was indeed', word)
            break
        
        #code when all 4 tries are used
        if tries == 5:
            print('YOU LOSE')
            print('The letter was', word)
            break
        
        
    #code for playing again or quitting    
    y = str(input('Want to play again \"press any key and enter\" if not \"press q\" :')) . lower() 
    if y == 'q':
        print('Good byee!')
        break
    else:
        continue