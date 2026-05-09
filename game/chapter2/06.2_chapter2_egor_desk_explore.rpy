
label chapter2_egor_desk_explore:

    scene it_corner
    'Егор вышел за кофе. Я остаюсь в комнате один. Взгляд падает на его стол.'

    # Инициализация переменных осмотра
    if not hasattr(store, 'egor_keyboard_examined'):
        $ egor_keyboard_examined = False
        $ egor_photo_examined = False
        $ egor_notebook_examined = False
        $ egor_drawer_examined = False
        $ egor_explore_mode = "first"

    menu:
        'Осмотреться на столе' if not (egor_keyboard_examined and egor_photo_examined and egor_notebook_examined and egor_drawer_examined):
            $ egor_explore_mode = "return"
            call egor_explore_menu
            jump chapter2_egor_desk_explore
        
        'Ничего не трогать' if egor_explore_mode == "first":
            'Отхожу от стола. Не моё.'
            'Егор возвращается, ставит передо мной кофе.'
            egor 'Что смотришь?'
            main_bro 'Да так. Просто ждал.'
            jump chapter2_continue
        
        'Перестать смотреть' if egor_explore_mode == "return":
            'Хватит. Отхожу.'
            'Егор возвращается.'
            egor 'Ну что, готов обсуждать?'
            main_bro 'Да.'
            jump chapter2_continue


label egor_explore_menu:

    menu:
        'Клавиатуры (разные, в разной степени сборки)' if not egor_keyboard_examined:
            call egor_examine_keyboards
            jump egor_explore_menu
        
        'Фотографии на мониторе' if not egor_photo_examined:
            call egor_examine_photo
            jump egor_explore_menu
        
        'Блокнот с записями' if not egor_notebook_examined:
            call egor_examine_notebook
            jump egor_explore_menu
        
        'Ящик стола (закрыт? приоткрыт?)' if not egor_drawer_examined:
            call egor_examine_drawer
            jump egor_explore_menu
        
        'Вернуться и сесть на место':
            return


# ==================== ОСМОТР КЛАВИАТУР ====================

label egor_examine_keyboards:
    $ egor_keyboard_examined = True
    'На столе — три клавиатуры в разной степени готовности.'
    
    'Первая — прозрачная, с подсветкой. Внутри переключатели с голубыми каплями.'
    'Вторая — разобранная, плата лежит отдельно, кнопки — в коробке.'
    'Третья — маленькая, без цифрового блока, с тёмно-серыми кнопками.'
    
    'Я провожу пальцем по кнопкам первой. Клацают приятно. Наверное, дорогие.'
    
    menu:
        'Нажать на пробел':
            'Пробел проваливается с глухим, тяжёлым звуком. Хорошо. Надёжно.'
            $ egor_trust += 0
        
        'Не трогать, просто посмотреть':
            'Лучше не трогать. Егор заметит, если что-то сдвинуто.'
            $ egor_trust += 0
    
    return


# ==================== ОСМОТР ФОТОГРАФИЙ ====================

label egor_examine_photo:
    $ egor_photo_examined = True
    'На рамке монитора — старая Polaroid. Группа студентов. Егор в центре.'
    
    'Я присматриваюсь. Рядом с ним — Варя. Она смеётся. Егор тоже.'
    
    'Сейчас они даже не здороваются. Странно, как всё ломается.'
    
    if varya_trust >= 2:
        'Вспоминаю Варю. Она говорила о нём с такой болью... А он просто хранит фото.'
        $ secret_egor_varya_photo_unlocked = True
        main_bro 'Он всё-таки помнит. Иначе зачем хранить?'
    
    menu:
        'Поставить фотографию на место':
            'Аккуратно ставлю обратно. Пусть стоит.'
        
        'Сфотографировать на телефон (тайком)':
            if varya_trust >= 2:
                'Щёлкаю. Теперь смогу показать Варе? Или не стоит?'
                'Потом решу.'
                $ secret_egor_varya_photo_copied = True
            else:
                'Телефон сел. Не судьба.'
    
    return


# ==================== ОСМОТР БЛОКНОТА ====================

label egor_examine_notebook:
    $ egor_notebook_examined = True
    'Потрёпанный блокнот в клетку. Лежит рядом с клавиатурой, заляпанный кофе.'
    
    'Я открываю. Схемы, формулы, какие-то расчёты. Егор явно проектирует что-то сложное.'
    
    'На одной странице — заметка. «Варя, позвони». Перечёркнуто. Ниже — другая: «Забыть. Не получается».'
    
    main_bro '...'
    
    menu:
        'Прочитать ещё':
            'Дальше — схемы. И больше ни слова о ней.'
            'Но я уже знаю. Он помнит. Просто не хочет показывать.'
            $ egor_trust += 1
        
        'Закрыть блокнот':
            'Закрываю. Неловко копаться в чужом.'
            'Варя не простила бы, если бы узнала. И Егор тоже.'
    
    return


# ==================== ОСМОТР ЯЩИКА ====================

label egor_examine_drawer:
    $ egor_drawer_examined = True
    'Ящик стола приоткрыт. Ручка болтается.'
    
    'Я выдвигаю. Внутри — провода, старые переходники, моток скотча.'
    
    'И... старый ключ. На брелоке — номер этажа и надпись «хозблок».'
    
    main_bro 'Зачем ему ключ от подсобки?'
    
    menu:
        'Взять ключ (секретный предмет)':
            $ secret_key_office = True
            'Я забираю ключ. Вдруг пригодится.'
            'Если спросит — скажу, что нашёл на полу.'
            $ egor_trust += 0
        
        'Оставить на месте':
            'Не моё. Кладу обратно.'
            $ egor_trust += 1
    
    return