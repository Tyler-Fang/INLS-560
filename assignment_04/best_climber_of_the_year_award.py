# Assignment 4

# Constants for Best Climber of the Year Award
MIN_TIMES_WINNING_COMPETITION = 5
MIN_YEARS_CLIMBING = 3

years_climbing = int(input('Enter your years of climbing experience: '))
years_winning_competitions_award = int(input('Enter how many competitions you have won in rock climbing: '))

if years_climbing >= MIN_YEARS_CLIMBING and years_winning_competitions_award >= MIN_TIMES_WINNING_COMPETITION:
    print('Congratulations! Your are eligible for the Best Climber of the Year Award.')
else:
# Multi-line with f-string
    print(f'''
Sorry, you do not meet the requirements for the Best Climber of the Year Award.end
          
You need at least:
- {MIN_YEARS_CLIMBING} years of climbing experience
- {MIN_TIMES_WINNING_COMPETITION} competitions you have won rock climbing
''')