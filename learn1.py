strings = ('This is a great day to code and changes should take place as such')
print(strings)
print('''How's your day been so far?''')
user_answer = False
while user_answer == False:
    user_day = input()
    if user_day.lower() == 'good':
        print("That's great!")
        user_answer = True
    elif user_day.lower() == 'bad':
        print("That's okay. The day will be alright!")
        user_answer = True
    else:
        print("Sorry I didn't catch that. Can you please try again?")
print("Do take care of yourself and drink much water!")