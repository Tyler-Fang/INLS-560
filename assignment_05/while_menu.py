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
        print("Great pick! Rock climbing is super cool. I've been doing this since I got to UNC, so it's been about 2 years now. I work at UNC Campus Recreation, so if you ever want to climb let me know!")
    elif menu_option == 'q' :
        print("See ya later, alligator")
