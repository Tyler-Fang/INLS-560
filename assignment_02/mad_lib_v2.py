#Mad lib example for functions

def madlib(ADJECTIVE_1, NOUN_1, VERB_1, ADJECTIVE_2, NOUN_2, VERB_2, 
           ADJECTIVE_3, NOUN_3, VERB_3):
    '''Mad lib function''' # Docstring must be indented.
    story = f'''
How to Snowboard: A Fun Guide Snowboarding is all about balance and control. 
First, make sure you have your {NOUN_1} strapped securely to your feet. It's 
important to stand up straight and keep your knees {ADJECTIVE_1} as you 
{VERB_1} forward. Once you're ready, start sliding down the hill and {VERB_2} 
through the snow. Make sure to keep your weight centered over the board. As you
gain speed, you'll want to steer by shifting your weight. If you lean too 
{ADJECTIVE_2} , you'll turn sharply, so be careful! To stop, simply lean back 
onto your {NOUN_2} and dig your edge into the snow. This will help you come to 
a smooth stop without {VERB_3}-ing out. Finally, enjoy the ride! Snowboarding 
can be a {ADJECTIVE_3} adventure, especially when you're flying down the 
slopes. Just don't forget to wear your {NOUN_3} for protection, and stay 
focused to avoid any nasty falls. Before you know it, you'll be shredding like
a pro!
'''
    return story

def get_user_input():
    """Prompt the user for input for the mad lib."""
    ADJECTIVE_1 = input("Enter an adjective: ")
    NOUN_1 = input("Enter a noun: " )
    VERB_1 = input("Enter a verb: ")
    ADJECTIVE_2 = input("Enter a second adjective: ")
    NOUN_2 = input("Enter a second noun: ")
    VERB_2 = input("Enter a second verb: ")
    ADJECTIVE_3 = input("Enter a third adjective: ")
    NOUN_3 = input("Enter a third noun: ")
    VERB_3 = input("Enter a third verb: ")

    return  ADJECTIVE_1, NOUN_1, VERB_1, ADJECTIVE_2, NOUN_2, VERB_2, ADJECTIVE_3, NOUN_3, VERB_3

# Get user input
user_inputs = get_user_input()

# Print the mablib story
print(madlib(*user_inputs))

