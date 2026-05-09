# ==================== КОМНАТА ВАРИ — ИНТЕРАКТИВНЫЙ ОСМОТР ====================

label chapter3_varya_room_explore:

    'Варя вышла на кухню за чаем. Я остаюсь в комнате один.'

    if not hasattr(store, 'varya_desk_examined'):
        $ varya_desk_examined = False
        $ varya_shelf_examined = False
        $ varya_bed_examined = False
        $ varya_photos_examined = False
        $ varya_notebook_opened = False
        $ varya_explore_mode = "first"

    menu:
        'Осмотреться' if not (varya_desk_examined and varya_shelf_examined and varya_bed_examined and varya_photos_examined):
            $ varya_explore_mode = "return"
            call varya_explore_menu
            jump chapter3_varya_room_explore
        
        'Ничего не трогать' if varya_explore_mode == "first":
            'Не лезу. Сижу, смотрю в окно.'
            'Варя возвращается с чаем. Кивает.'
            varya 'Молодец, что не лазил. Я бы не хотела... всякого.'
            $ varya_trust += 1
            jump chapter3_office_slow
        
        'Перестать смотреть' if varya_explore_mode == "return":
            'Хватит. Отхожу от стола. Неловко.'
            'Варя возвращается с чаем.'
            varya 'Всё в порядке?'
            main_bro 'Да. Просто... задумался.'
            jump chapter3_office_slow


label varya_explore_menu:

    menu:
        'Посмотреть на стол (бумаги, блокноты)' if not varya_desk_examined:
            call varya_examine_desk
            jump varya_explore_menu
        
        'Посмотреть на полку с вещами' if not varya_shelf_examined:
            call varya_examine_shelf
            jump varya_explore_menu
        
        'Посмотреть на кровать (плед, подушка)' if not varya_bed_examined:
            call varya_examine_bed
            jump varya_explore_menu
        
        'Посмотреть на фотографии на стене' if not varya_photos_examined:
            call varya_examine_photos
            jump varya_explore_menu
        
        'Вернуться и сесть на место':
            return


label varya_examine_desk:

    $ varya_desk_examined = True
    'На столе — горка бумаг, старый ноутбук, блокнот в твёрдой обложке.'
    
    menu:
        'Открыть блокнот':
            if varya_trust >= 2:
                $ secret_varya_poems_unlocked = True
                $ varya_trust += 1
                'Это её стихи. Пронзительные, резкие. Про одиночество.'
                'Про Егора — ни строчки. Только про себя.'
                'В конце — дата. Вчерашняя.'
                'Я закрываю блокнот. Стыдно? Немного.'
            else:
                'Я открываю, но сразу закрываю. Это слишком личное. Не имею права.'
        
        'Не трогать':
            'Не лезу в чужое. Просто смотрю на стопку бумаг. Рабочие отчеты.'

    return


label varya_examine_shelf:

    $ varya_shelf_examined = True
    'На полке — старая флешка, пузырёк с лаком, стопка открыток, маленькая керамическая собачка (похожа на корги).'
    
    if varya_trust >= 3:
        'Я замечаю фотографию. Варя и кто-то ещё... Мужчина. Седой. Похож на отца.'
        'На обороте — «2009».'
        
        menu:
            'Взять в руки и рассмотреть':
                'Варя возвращается. Замечает, что я смотрю.'
                varya 'Это мой папа. Он умер.'
                main_bro 'Извини.'
                varya 'Ничего. Ты хороший. Что хочешь спросить — спрашивай.'
                $ varya_trust += 1
            'Не трогать':
                'Просто смотрю. Кладу обратно. Варя не замечает.'
    else:
        'Я не решаюсь разглядывать. Отхожу.'

    return


label varya_examine_bed:

    $ varya_bed_examined = True
    'Аккуратно. Плед вязаный. Подушка с вышивкой. Просто и тепло.'
    'На тумбочке — старая книга стихов. Ахматова.'
    main_bro 'Она это читает? Странно. Но понятно.'
    'Больше ничего. Отхожу.'

    return


label varya_examine_photos:

    $ varya_photos_examined = True
    'На стене — несколько Polaroid. Варя с одногруппниками.'
    
    'Вот она смеётся с какой-то девушкой. Вот на фоне универа. Вот — толпа людей.'
    
    'Я присматриваюсь. На одной из фотографий — Егор. Молодой, длинные волосы. Стоит в стороне, не улыбается.'
    
    'Сейчас он другой. Но глаза те же.'
    
    if secret_egor_varya_photo_unlocked:
        'Похоже на ту фотографию, что я видел у Егора на столе. Только здесь они не вместе — он отдельно.'
        'Странно. Как будто два мира.'

    return