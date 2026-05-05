
# Игра начинается здесь:
label start:
    'Для начала выберите ваш пол'
    menu:
        'мужчина':
            $ pronoun = 1
        'женщина':
            $ pronoun = 0


    $ viname = renpy.input('Введите ваше имя')

    if not viname:
        if pronoun == 1:
            $ viname = 'Алексей'
        elif pronoun == 0:
            $ viname = 'Мария'

    call check_name

    if gosha_67 == True:
        jump sixseven
        return

    jump chapter1

 
   
