# ----------------------главная-----------------------

label start:

    # ВВОД ИМЕНИ (без выбора пола)
    $ viname = renpy.input('Введите ваше имя, игра идет от мужского лица', 'Андрей')
    
    if not viname:
        $ viname = 'Андрей'
    
    call check_name
    
    # Если сработала пасхалка с Гошей
    if gosha_67 == True:
        jump sixseven
    
    # Старт пролога
    jump prologue