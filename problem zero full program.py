def main():
    print('welcome to problem set 0!'.upper())
    while True:
        again = input('would you like to test another part? (y/n) ').lower()
        if again == 'y':
            choice()
        elif again == 'n':
            print('goodbye!')
            break
        else:
            print('invalid input!'.upper())

    
def choice():
    guide = ('choose:\n for indoor voice type 1\n for playback speed type 2\n for making faces type 3\n for einstein type 4\n for tip calculator type 5')
    print (guide)
    userChoice = (input('what pert of problem set 0 would you like to test? '))
    if userChoice == '1':
        print('==testing indor voice=='.upper())
        user_input()
    elif userChoice == '2':
        print('==testing playback speed=='.upper())
        playback()
    elif userChoice == '3':
        print('==testing making faces=='.upper())
        faces()
    elif userChoice == '4':
        print('==testing einstein=='.upper())
        einstein()
    elif userChoice == '5':
        print('==testing tip calculator=='.upper())
        tip_calculator()
    else:
        print('invalid input!'.upper())
                
        
    


#indoor.py   
def user_input():
    userInput=  input('type something: ').strip().upper()
       
    print(userInput)

#playback.py 
def playback():
    playback_speed = input('type something: ').strip()
    play = playback_speed.replace(' ', '...')
    print(play)
    


#faces.py    
def faces():
    user_input = input('enter a face: ').strip()

    if ':)' in  user_input :
        face = user_input.replace(':)','🙂')
        print(face)
    elif '(:' in user_input:
        face = user_input.replace('(:','🙁')
        print(face)
    else:
        print('invalid input')
    

#einstein.py  
def einstein():
    #e=mc**2
    c =  300000000
    c2 = c**2
    m = int(input('enter the value of m: '))
    E = m*c2
    print (E)
    

#tip calculator
def tip_calculator():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
       return float(d.replace('$',''))


def percent_to_float(p):
    # TODO
         return float(p.replace('%',''))/100
main()


