import random


def generate_colours():
    """This function will generate the hidden colours that need to be found"""
    COLOURS = ["RED","BLUE","YELLOW","WHITE","GREY","ORANGE","GREEN","PINK"]
    answer = []
    count = 4
    for row in range(count):
        choice = COLOURS[random.randint(0,len(COLOURS)-1)]
        if not choice in answer:
            answer.append(choice)
            COLOURS.remove(choice)

    return answer

def check_colours(guess,answers:list):
    count = 0
    if guess in answers:
        count = 1
        answers.remove
    else:
        count = 0
    return int(count)


def check_position(guesses:list, answers:list):
    count = 0
    for i in range(1,len(answers)+1):
        if guesses[i-1] == answers[i-1]:
            count += 1
    return int(count)



def start_mastermind():
    TURNS = 3
    COLOURS = ["RED","BLUE","YELLOW","WHITE","GREY","ORANGE","GREEN","PINK"]
    round_count = 0 
    correct_colours = 0
    correct_positions = 0 
    game_history = []

    answers = generate_colours()
    print(answers)
    # User input
    print("LETS PLAY MASTERMIND")
    print("Your colour choices:")
    print(COLOURS)
    while round_count < TURNS:
        guess_list = []
        print(f"MAKE YOUR PICKS FOR ROUND {round_count + 1}")
        g1 = input("colour 1: ").upper()
        guess_list.append(g1)
        correct_colours += check_colours(g1,answers)


        
        g2 = input("colour 2: ").upper()
        guess_list.append(g2)
        correct_colours += check_colours(g2,answers)


        g3 = input("colour 3: ").upper()
        guess_list.append(g3)
        correct_colours += check_colours(g3,answers)


        g4 = input("colour 4: ").upper()
        guess_list.append(g4)
        correct_colours += check_colours(g4,answers)

        correct_positions = check_position(guess_list,answers)
        game_history.append(guess_list)

        if correct_colours == 4 and correct_positions == 4:
            print("         -=-=--=-=-=-=-=-")
            print("      =-=-=-=--=-=-=-=-=-=-=")
            print("   -=-=-=-=-=--=-=-=-=-=-=-=-=-")
            print("-=-=-=-=-=-YOU WIN-=-=-=-=-=-=-=-=-")
            print("   -=-=-=-=-=--=-=-=-=-=-=-=-=-")
            print("      =-=-=-=--=-=-=-=-=-=-=")
            print("         -=-=--=-=-=-=-=-")

            print(answers)
            break
        elif round_count == TURNS:
            print("BETTER LUCK NEXT TIME")
            print(answers)
            break
        else: 
            round_count += 1

            

        # game naration
        print("---------------")
        print(f"ROUND {round_count}:")
        print(" ")
        print(f"Guess: {guess_list}")
        print(f"Correct colour guesses: {correct_colours}")
        print(f"Correct position guesses: {correct_positions}")
        print("GAME HISTORY:")
        print(f"{game_history}")
        print("---------------")

        correct_colours = 0
        correct_positions = 0 


if __name__ == "__main__":
    start_mastermind()
