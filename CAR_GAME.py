# PROBLEM STATEMENT : User needs to type "help" to get started , then we need to display 3 options asking user to type start , stop or quit to strat the car , stop the car or quit the game

user_input= ''
is_started=False
is_stopped=False
while user_input.lower() != 'quit':
    user_input=input(">").lower()
    if user_input == 'start':
        if is_started :
            print("car already started")
        else :
            is_started=True
            print('car started')
    elif user_input == 'stop':
        if is_stopped :
            print("car already stopped")
        else :
            is_stopped=True
            print('car stopped')
    elif user_input == 'quit':
        quit()
    elif user_input=='help':
        print("start : To start the car \n stop : To stop the car \n quit : To quit the game")
    else :
        print("naku telvad")




