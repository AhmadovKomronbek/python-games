import random
import arts

# Funksiyalar
# FLag
bayroq = False
# Salomlashish
print(arts.salomlashish_img)
print("O'yin shartiga ko'ra siz tosh qaychi qog'ozni tanlaymiz va compyuter bilan raqobatlashasiz, \nSizda va kompyuterda 3 tadan yurak bo'ladi. \nAgar siz tanlagan jism compyuter tanlagan jismdan kuchliroq bo'lsa compyuerning jonidan 1 ayiriladi. \n Agar uning teskarisi bo'lsa sizdan bitta yurak ayiriladi. \nKimning yuragi soni 0 ga teng bo'lsa uning dushmani yutadi.")
def tosh_qaychi_qogoz_imgs():
    print(f"Tosh {arts.tosh}\nQaychi {arts.qaychi}\nQog'oz{arts.qogoz}")
tosh_qaychi_qogoz_imgs()

Boshlaymizmi = input("Boshlaymizmi (Ha yoki Ho'q) :").lower()
if Boshlaymizmi == "ha":
    compyuter_yuradi_sonni = 3
    foydalamuvchi_yuragi_sonni = 3
    compyuterning_jismlar_arrayi = [arts.tosh,arts.qogoz,arts.qaychi]

#     Foydalanuvchidan malumot olish
    while not bayroq:
        tosh_qaychi_qogoz_imgs()
        foydalanchi_tanlagan_jim = input("Qaysi birini tanlaysiz :").lower()
        if foydalanchi_tanlagan_jim == "tosh" or foydalanchi_tanlagan_jim == "qaychi" or foydalanchi_tanlagan_jim == "qogoz":
            #         Random
            compyuter_tanlagan_jism = random.choice(compyuterning_jismlar_arrayi)
            print(f"Kompyuter tanlagan jism {compyuter_tanlagan_jism}")

            # Tekshirish
            if foydalanchi_tanlagan_jim == "tosh" and compyuter_tanlagan_jism == arts.qaychi:
                if compyuter_yuradi_sonni > 0:
                    compyuter_yuradi_sonni = compyuter_yuradi_sonni - 1
                    if compyuter_yuradi_sonni == 0:
                        arts.YouWin()
                        bayroq = True
                    else:
                        print(f"Sening yuraging sonni {foydalamuvchi_yuragi_sonni}")
                        print(f"Copyuterning yuragining sonni {compyuter_yuradi_sonni}")

            elif foydalanchi_tanlagan_jim == "qaychi" and compyuter_tanlagan_jism == arts.qogoz:
                if compyuter_yuradi_sonni > 0:
                    compyuter_yuradi_sonni = compyuter_yuradi_sonni - 1
                    if compyuter_yuradi_sonni == 0:
                        arts.YouWin()
                        bayroq = True
                    else:
                        print(f"Sening yuraging sonni {foydalamuvchi_yuragi_sonni}")
                        print(f"Copyuterning yuragining sonni {compyuter_yuradi_sonni}")

            elif foydalanchi_tanlagan_jim == "qogoz" and compyuter_tanlagan_jism == arts.tosh:
                if compyuter_yuradi_sonni > 0:
                    compyuter_yuradi_sonni = compyuter_yuradi_sonni - 1
                    if compyuter_yuradi_sonni == 0:
                        arts.YouWin()
                        bayroq = True
                    else:
                        print(f"Sening yuraging sonni {foydalamuvchi_yuragi_sonni}")
                        print(f"Copyuterning yuragining sonni {compyuter_yuradi_sonni}")
            elif foydalanchi_tanlagan_jim == "tosh" and compyuter_tanlagan_jism ==arts.tosh:
                print("teng")
            elif foydalanchi_tanlagan_jim == "qaychi" and compyuter_tanlagan_jism ==arts.qaychi:
                print("teng")
            elif foydalanchi_tanlagan_jim == "qogoz" and compyuter_tanlagan_jism ==arts.qogoz:
                print("teng")
            else:
                if foydalamuvchi_yuragi_sonni > 0:
                    foydalamuvchi_yuragi_sonni = foydalamuvchi_yuragi_sonni - 1
                    if compyuter_yuradi_sonni == 0:
                        arts.YouWin()
                        bayroq = True
                    else:
                        print(f"Sening yuraging sonni {foydalamuvchi_yuragi_sonni}")
                        print(f"Copyuterning yuragining sonni {compyuter_yuradi_sonni}")
                elif foydalamuvchi_yuragi_sonni == 0:
                    bayroq = True
                    arts.ComputerWins()



else:
    print("Ha ,mayli uxla")