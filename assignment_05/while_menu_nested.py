# Assignment 5

# Prime the while statement
menu_option = ''
while menu_option != 'q':
    print("Select the sport to learn more about it.: \n"
          "a. Snowboarding \n"
          "b. Rock Climbing \n"
          "q. Quit \n")
    menu_option = input("Choose what sport you want to learn about and how it relates to me: ")
    if menu_option == 'a' :
        print("Great choice! Snowboarding is awesome. I've been doing it for about 3-4 years now and I haven't stopped since. I wish here in North Carolina that it's year round though.")
    elif menu_option == 'b' :
        answer = input ("Great pick! Do you think rock climbing is dangerous? enter (y or n):")
        if answer == 'y' :
            print("Nice way to use your noggin. Of course climbing is dangerous, but if you learn to do it safely, then nothing wrong will ever happen.")
        else:
            print("Use your brain. Of course climbing is dangerous. You're climbing a good distance above the ground dummy. That fall won't feel great.")
    elif menu_option == 'q' :
        print("See ya later, alligator")