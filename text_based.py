def start_game():
    print("مرحبا بك في لعبة الهروب من الغرفة")
    print("استيقظت ووجدت نفسك داخل غرفة مظلمة")
    print("أمامك باب وطاولة عليها مفتاح وغرض غريب")
    print("ماذا تفعلين؟")

    option = input("اكتبي رقم الخيار: ")

    if option == "1":
     take_key()

    elif option == "2":
     check()

    elif option == "3":
     open_door(False)

    else: 
     print("هذا الخيار غير موجود")
     start_game()

def take_key():
    print("اخذت المفتاح. ربما يفيدك لاحقاً")
    open_door(True)

def check():
    print("الغرض كان صندوقًا صغيرًا، لكن لا يمكنك فتحه الآن")
    start_game()

def open_door(key_found):
    if key_found:
        print("استخدمتِ المفتاح وخرجتِ من الغرفة! مبروك")
    else:
        print("الباب مغلق، وتحتاجين إلى مفتاح")
        start_game()

start_game()