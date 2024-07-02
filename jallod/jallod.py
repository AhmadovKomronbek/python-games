
import random
import jallod_art
import jallod_words


chosen_word = random.choice(jallod_words.word_list)
print(chosen_word)

end_of_game = False
lives = 6
print(jallod_art.logo)

latersArray = list(chosen_word)
changeLatter1 = list(chosen_word)
changeLatter1Text = ""

for i in range(0,len(changeLatter1)):
    changeLatter1[i]="_"
for i in range(0,len(changeLatter1)):
    changeLatter1Text += changeLatter1[i]
print(changeLatter1Text)


while not end_of_game:
    guess = input("Guess a letter: ").lower()


    # TODO-4: - Agar foydalanuvchi allaqachon taxmin qilgan harfni kiritgan bo'lsa, xatni chop eting va ularga xabar bering.


    # taxmin qilingan so'zni tekshiring

    #Foydalanuvchi noto'g'ri ekanligini tekshiring.
    if guess not in chosen_word:
    #     TODO-5: - Agar harf tanlangan_so'zda bo'lmasa, xatni chop eting va ularga bu so'zda yo'qligini bildiring.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(jallod_art.stages[lives])
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(jallod_art.stages[0])

    # Ro'yxatdagi barcha elementlarni qo'shing va uni Stringga aylantiring.
    else:
        for i in range(0,len(chosen_word)):
            if list(chosen_word)[i] == guess:
                changeLatter1[i] = guess
                print(changeLatter1)
                print(jallod_art.stages[lives])
                if changeLatter1 == list(chosen_word):
                    print("you win")



    # Foydalanuvchi barcha harflarni topganini tekshiring.

    # TODO-2: -Bosqichlarni jallod_art.py dan import qiling va bu xatolikni bartaraf qiling.
