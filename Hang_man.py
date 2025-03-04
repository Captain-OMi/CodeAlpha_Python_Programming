from replit import clear
import random
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

stage = ['''
  (o_o)  
   <|    
   / \ 
Proficient
''','''
  (•_•)  
   <|>   
   / \ 
  Expert   
''','''
  (•‿•)  
   <|>   
   / \ 
  Elite   
''','''
  (⌐■_■)  
   <|>   
   / \ 
  Master   
''','''
  (😃)  
   \|/   
    |    
   / \ 
Excellent   
''','''
  😎  
  \|/    
   |    
  / \  
Supreme  
''','''
   👑
   😎  
   \|/   
    |    
   / \ 
Legendary   
''']

word_list = [
 'car',
 'biard', 
 'ship', 
 'glass', 
 'fabrick', 
 'supercar', 
 'legendary', 
 'psychology', 
 'mentality'
 ]

print(logo)
play = False
play_game = input("\nDo You play HangMan game?(Y/N):- ").upper()

while not play:
    clear()
    
    if play_game == 'Y' or play_game == 'N':
        while play_game == 'Y':
            chosen_word = random.choice(word_list)
            word_length = len(chosen_word)
            end_of_game = False
            lives = 6

            display = []
            for _ in range(word_length):
                display += "_"
            print(' '.join(display))

            while not end_of_game:
                guess = input("guess a letter\n= ").lower()
                print(chosen_word)
                clear()

                if guess in display:
                    print("Chosen latter is alrady in disply")
                elif guess not in chosen_word:
                        lives -= 1
                        print("You'r chosen wrong letter.")
                        if lives == 0:
                            print("You lost")
                            end_of_game = True
                else:
                    print(f'You chose letter "{guess}"')

                    if guess not in chosen_word:
                        lives -= 1
                        print("You'r chosen wrong letter.")
                        if lives == 0:
                            print("You lost")
                            end_of_game = True

                for position in range(word_length):
                    letter = chosen_word[position]
                    if letter == guess:
                        display[position] = letter
                print(' '.join(display))

                if "_" not in display:
                    end_of_game = True
                    print(stage[lives])
                    print("🎉 You Win! 🎉")
                
                print(f'\nLives = {lives}.')
                if lives == 0:
                    print("\n😞 Loser 😞")
        
            play_game = input("\nDo You play again HangMan game.(Y/N):- ").upper()
    if play_game == 'N':
        play = True
    else:
        clear()
        if play_game != 'N' or play_game != 'Y':
            play_game = input("\nYou chosen wrong later please try again.(Y/N):- ").upper()
            clear()