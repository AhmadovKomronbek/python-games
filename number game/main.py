import random
import logo
import color

# function

def print_text(number_of_hearts):
    print(f"{color.GREEN}You have {number_of_hearts} hearts\n{color.END}")


def blog_code(number_of_hearts, RANDOM_NUMBER, logo, color, times):
    flag = True
    while flag:
        if number_of_hearts != 0:
            user_input = int(input(f"{color.GREEN}Please enter enter number (from 1 to 100) :{color.END}"))
            if user_input > RANDOM_NUMBER:
                print(f"{color.RED}High !!!{color.END}")
                print_text(number_of_hearts - 1)
                number_of_hearts -= 1

            elif user_input < RANDOM_NUMBER:
                print(f"{color.RED}Low !!!{color.END}")
                print_text(number_of_hearts - 1)
                number_of_hearts -= 1

            else:
                print(color.LIGHT_GREEN, logo.you_won, color.END)
                print(f"{color.CYAN}the number the computer picked was {RANDOM_NUMBER}{color.END}")
                print(f"{color.GREEN}you tried {(times - number_of_hearts) - 1} times\n{color.END}")
                break

        else:
            print(color.RED, logo.you_lose, color.RED)
            break

def main_code():
    print(logo.logo)
    print(f"""{color.YELLOW}
    Game mode       number of heart

    1 easy          10
    2 normal        8
    3 hard          5
    {color.END}
    """)

    game_mode = input(f"{color.GREEN}Please enter game mode (easy, normal , hard) :{color.END}").lower()

    RANDOM_NUMBER = random.randint(1, 100)

    number_of_hearts = 0
    times = 0

    if game_mode == "easy" or game_mode == "normal" or game_mode == "hard":
        if game_mode == "easy":
            number_of_hearts = times = 10
        elif game_mode == "normal":
            number_of_hearts = times = 8
        elif game_mode == "hard":
            number_of_hearts = times = 5

        blog_code(number_of_hearts, RANDOM_NUMBER, logo, color, times)

    else:
        print(f"{color.RED}Please choose one .\n{color.END}")
        main_code()
main_code()