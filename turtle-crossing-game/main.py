# TODO: fayllarni import qilish
# TODO: scrennni sozlash
# TODO: obyektlarni yaratish
# TODO: while sikli yaratish
# TODO: o'yinni sekinlashtirish uchun time.sleep()dan foydalanish
# TODO: yangi block yaratish
# TODO: yaratilgan blocklarni haraklantirish
# TODO: agar player blockka urilsa o'yinni to'xtatish
# TODO: agar player qator oxiriga borsa keyingi bosqichga o'tish
# TODO: o'yin leveliga qarab tezlikni oshirish
# TODO: scoreboradni yangilash
# TODO: o'yin bosilsa to'xtasin
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle crossing game")

best_score = 0
number_car = 0
game_mode_name = ""

def play_game(score, number_c, game_mode_n):
    if screen.textinput("TURTLE GAME", "Do you want play (yes or no) :").lower() == "yes":
        game_mode = screen.textinput("TURTLE GAME", "Enter game mode(easy, normal, hard):").lower()
        if game_mode == "hard":
            number_c = 6
            game_mode_n = "hard"

        elif game_mode == "normal":
            number_c = 10
            game_mode_n = "normal"

        else:
            number_c = 15
            game_mode_n = "easy"
            

        scoreboard = ScoreBoard()
        player = Player()
        car_manager = CarManager()
        screen.tracer(0)

        screen.listen()
        screen.onkey(player.move_forward, "w")
        screen.onkey(player.move_back, "s")
        screen.onkey(player.move_left, "a")
        screen.onkey(player.move_right, "d")

        flag = True
        while flag:
            time.sleep(0.05)
            screen.update()

            car_manager.make_car(number_c)

            car_manager.move()

            for car in car_manager.all_cars:
                if car.distance(player) < 20:
                    flag = False
                    screen.clear()
                    player.go_to_start()
                    if score <= scoreboard.level - 1:
                        score = scoreboard.level - 1
                    scoreboard.game_over(score, game_mode_n)
                    time.sleep(3)
                    scoreboard.clear()
                    screen.clear()
                    player.go_to_start()
                    play_game(score, number_c, game_mode_n)

            if player.finish_line():
                scoreboard.update_scoreboard()
                car_manager.increase_speed()
                player.go_to_start()

play_game(best_score, number_car, game_mode_name)

screen.exitonclick()
