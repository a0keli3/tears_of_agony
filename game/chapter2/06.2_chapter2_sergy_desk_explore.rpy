
label chapter2_sergy_desk_explore:

    scene it_corner
    'Сергей вышел за кофе. Я остаюсь в комнате один. Взгляд падает на его стол.'

    # Инициализация переменных осмотра
    if not hasattr(store, 'sergy_keyboard_examined'):
        $ sergy_keyboard_examined = False
        $ sergy_photo_examined = False
        $ sergy_notebook_examined = False
        $ sergy_drawer_examined = False
        $ sergy_explore_mode = "first"

    menu:
        'Осмотреться на столе' if not (sergy_keyboard_examined and sergy_photo_examined and sergy_notebook_examined and sergy_drawer_examined):
            $ sergy_explore_mode = "return"
            call sergy_explore_menu
            jump chapter2_sergy_desk_explore
        
        'Ничего не трогать' if sergy_explore_mode == "first":
            'Отхожу от стола. Не моё.'
            'Сергей возвращается, ставит передо мной кофе.'
            sergy 'Что смотришь?'
            main_bro 'Да так. Просто ждал.'
            jump chapter2_continue
        
        'Перестать смотреть' if sergy_explore_mode == "return":
            'Хватит. Отхожу.'
            'Сергей возвращается.'
            sergy 'Ну что, готов обсуждать?'
            main_bro 'Да.'
            jump chapter2_continue


label sergy_explore_menu:

    menu:
        'Клавиатуры (разные, в разной степени сборки)' if not sergy_keyboard_examined:
            call sergy_examine_keyboards
            jump sergy_explore_menu
        
        'Фотографии на мониторе' if not sergy_photo_examined:
            call sergy_examine_photo
            jump sergy_explore_menu
        
        'Блокнот с записями' if not sergy_notebook_examined:
            call sergy_examine_notebook
            jump sergy_explore_menu
        
        'Ящик стола (закрыт? приоткрыт?)' if not sergy_drawer_examined:
            call sergy_examine_drawer
            jump sergy_explore_menu
        
        'Вернуться и сесть на место':
            return


# ==================== ОСМОТР КЛАВИАТУР ====================

label sergy_examine_keyboards:
    $ sergy_keyboard_examined = True
    'На столе — три клавиатуры в разной степени готовности.'
    
    'Первая — прозрачная, с подсветкой. Внутри переключатели с голубыми каплями.'
    'Вторая — разобранная, плата лежит отдельно, кнопки — в коробке.'
    'Третья — маленькая, без цифрового блока, с тёмно-серыми кнопками.'
    
    'Я провожу пальцем по кнопкам первой. Клацают приятно. Наверное, дорогие.'
    
    menu:
        'Нажать на пробел':
            'Пробел проваливается с глухим, тяжёлым звуком. Хорошо. Надёжно.'
            $ sergy_trust += 0
        
        'Не трогать, просто посмотреть':
            'Лучше не трогать. Сергей заметит, если что-то сдвинуто.'
            $ sergy_trust += 0
    
    return



label sergy_examine_photo:
    $ sergy_photo_examined = True
    'На рамке монитора — старая Polaroid. Группа студентов. Сергей в центре.'
    
    'Я присматриваюсь. Рядом с ним — Алиса. Она смеётся. Сергей тоже.'
    
    'Сейчас они даже не здороваются. Странно, как всё ломается.'
    
    if alice_trust >= 2:
        'Вспоминаю Варю. Она говорила о нём с такой болью... А он просто хранит фото.'
        $ secret_sergy_alice_photo_unlocked = True
        main_bro 'Он всё-таки помнит. Иначе зачем хранить?'
    
    menu:
        'Поставить фотографию на место':
            'Аккуратно ставлю обратно. Пусть стоит.'
        
        'Сфотографировать на телефон (тайком)':
            if alice_trust >= 2:
                'Щёлкаю. Теперь смогу показать Варе? Или не стоит?'
                'Потом решу.'
                $ secret_sergy_alice_photo_copied = True
            else:
                'Телефон сел. Не судьба.'
    
    return


# ==================== ОСМОТР БЛОКНОТА ====================

label sergy_examine_notebook:
    $ sergy_notebook_examined = True
    'Потрёпанный блокнот в клетку. Лежит рядом с клавиатурой, заляпанный кофе.'
    
    'Я открываю. Схемы, формулы, какие-то расчёты. Сергей явно проектирует что-то сложное.'
    
    'На одной странице — заметка. «Алиса, позвони». Перечёркнуто. Ниже — другая: «Забыть. Не получается».'
    
    main_bro '...'
    
    menu:
        'Прочитать ещё':
            'Дальше — схемы. И больше ни слова о ней.'
            'Но я уже знаю. Он помнит. Просто не хочет показывать.'
            $ sergy_trust += 1
        
        'Закрыть блокнот':
            'Закрываю. Неловко копаться в чужом.'
            'Алиса не простила бы, если бы узнала. И Сергей тоже.'
    
    return


# ==================== ОСМОТР ЯЩИКА ====================

label sergy_examine_drawer:
    $ sergy_drawer_examined = True
    'Ящик стола приоткрыт. Ручка болтается.'
    
    'Я выдвигаю. Внутри — провода, старые переходники, моток скотча.'
    
    'И... старый ключ. На брелоке — номер этажа и надпись «хозблок».'
    
    main_bro 'Зачем ему ключ от подсобки?'
    
    menu:
        'Взять ключ (секретный предмет)':
            $ secret_key_office = True
            'Я забираю ключ. Вдруг пригодится.'
            'Если спросит — скажу, что нашёл на полу.'
            $ sergy_trust += 0
        
        'Оставить на месте':
            'Не моё. Кладу обратно.'
            $ sergy_trust += 1
    
    return