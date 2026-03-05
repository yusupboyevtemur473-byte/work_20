#1-misol
   # n = int(input("1-7 gacha son kiriting: "))
   # match n:
#        case 1: print("Dushanba")
     #   case 2: print("Seshanba")
    #    case 3: print("Chorshanba")
      #  case 4: print("Payshanba")
       # case 5: print("Juma")
        #case 6: print("Shanba")
        #case 7: print("Yakshanba")
        #case _: print("Xato son!")


#2-misol
   # k = int(input("Bahoni kiriting (1-5): "))
    #match k:
    #    case 1: print("Yomon")
    #    case 2: print("Qoniqarsiz")
     #   case 3: print("Qoniqarli")
      #  case 5: print("A'lo")
       # case _: print("Xato")


#3-misol
 #   oy = int(input("Oy raqamini kiriting (1-12): "))
  #  match oy:
   #     case 12 | 1 | 2: print("Qish")
    #    case 3 | 4 | 5: print("Bahor")
     #   case 6 | 7 | 8: print("Yoz")
      #  case 9 | 10 | 11: print("Kuz")
       # case _: print("Xato oy")


#4-misol
    #oy = int(input("Oy raqamini kiriting (1-12): "))
    #match oy:
     #   case 1 | 3 | 5 | 7 | 8 | 10 | 12:
      #      print("31 kun")
       # case 4 | 6 | 9 | 11:
        #    print("30 kun")
       # case 2:
    #       print("28 kun (kabisa emas)")
        #case _:
         #   print("Xato oy")


#5-misol
 #   A = float(input("A = "))
  #  B = float(input("B = "))
   # amal = int(input("Amal (1:+, 2:-, 3:/, 4:*): "))
#
 #   match amal:
  #      case 1:
   #         print("Natija:", A + B)
    #    case 2:
     #       print("Natija:", A - B)
      #  case 3:
       #     if B != 0:
        #        print("Natija:", A / B)
         #   else:
          #      print("0 ga bo'lish mumkin emas!")
        #case 4:
         #   print("Natija:", A * B)
        #case _:
          #  print("Xato amal!")


#6-misol
 #   birlik = int(input("Birlik (1-dm,2-km,3-m,4-mm,5-cm): "))
  #  uzunlik = float(input("Uzunlikni kiriting: "))
#
 #   match birlik:
  #      case 1:
   #         print("Metrlarda:", uzunlik * 0.1)
    #    case 2:
     #       print("Metrlarda:", uzunlik * 1000)
      #  case 3:
       #     print("Metrlarda:", uzunlik)
        #case 4:
        #    print("Metrlarda:", uzunlik * 0.001)
       # case 5:
        #    print("Metrlarda:", uzunlik * 0.01)
        #case _:
         #   print("Xato birlik!")


#7-misol
 #   birlik = int(input("Birlik (1-kg,2-mg,3-g,4-tonna,5-sentner): "))
 #ogirlik = float(input("Og'irlikni kiriting: "))

  #  match birlik:
   #     case 1:
    #        print("Kilogramda:", ogirlik)
     #   case 2:
      #      print("Kilogramda:", ogirlik / 1_000_000)
       # case 3:
        #    print("Kilogramda:", ogirlik / 1000)
       # case 4:
        #    print("Kilogramda:", ogirlik * 1000)
        #case 5:
         #   print("Kilogramda:", ogirlik * 100)
        #case _:
         #   print("Xato birlik!")
