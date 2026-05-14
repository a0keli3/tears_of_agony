# ==================== КОМНАТА ВАРИ — ИНТЕРАКТИВНЫЙ ОСМОТР ====================

label chapter3_alice_room_explore:

    'Алиса вышла на кухню за чаем. Я остаюсь в комнате один.'

    if not hasattr(store, 'alice_desk_examined'):
        $ alice_desk_examined = False
        $ alice_shelf_examined = False
        $ alice_bed_examined = False
        $ alice_photos_examined = False
        $ alice_notebook_opened = False
        $ alice_explore_mode = "first"

    menu:
        'Осмотреться' if not (alice_desk_examined and alice_shelf_examined and alice_bed_examined and alice_photos_examined):
            $ alice_explore_mode = "return"
            call alice_explore_menu
            jump chapter3_alice_room_explore
        
        'Ничего не трогать' if alice_explore_mode == "first":
            'Не лезу. Сижу, смотрю в окно.'
            'Алиса возвращается с чаем. Кивает.'
            alice 'Молодец, что не лазил. Я бы не хотела... всякого.'
            $ alice_trust += 1
            jump chapter3_office_slow
        
        'Перестать смотреть' if alice_explore_mode == "return":
            'Хватит. Отхожу от стола. Неловко.'
            'Алиса возвращается с чаем.'
            alice 'Всё в порядке?'
            main_bro 'Да. Просто... задумался.'
            jump chapter3_office_slow


label alice_explore_menu:

    menu:
        'Посмотреть на стол (бумаги, блокноты)' if not alice_desk_examined:
            call alice_examine_desk
            jump alice_explore_menu
        
        'Посмотреть на полку с вещами' if not alice_shelf_examined:
            call alice_examine_shelf
            jump alice_explore_menu
        
        'Посмотреть на кровать (плед, подушка)' if not alice_bed_examined:
            call alice_examine_bed
            jump alice_explore_menu
        
        'Посмотреть на фотографии на стене' if not alice_photos_examined:
            call alice_examine_photos
            jump alice_explore_menu
        
        'Вернуться и сесть на место':
            return


label alice_examine_desk:

    $ alice_desk_examined = True
    'На столе — горка бумаг, старый ноутбук, блокнот в твёрдой обложке.'
    
    menu:
        'Открыть блокнот':
            if alice_trust >= 2:
                $ secret_alice_poems_unlocked = True
                $ alice_trust += 1
                'Это её стихи. Пронзительные, резкие. Про одиночество.'
                'Про Сергейа — ни строчки. Только про себя.'
                'В конце — дата. Вчерашняя.'
                'Я закрываю блокнот. Стыдно? Немного.'
            else:
                'Я открываю, но сразу закрываю. Это слишком личное. Не имею права.'
        
        'Не трогать':
            'Не лезу в чужое. Просто смотрю на стопку бумаг. Рабочие отчеты.'

    return


label alice_examine_shelf:

    $ alice_shelf_examined = True
    'На полке — старая флешка, пузырёк с лаком, стопка открыток, маленькая керамическая собачка (похожа на корги).'
    
    if alice_trust >= 3:
        'Я замечаю фотографию. Алиса и кто-то ещё... Мужчина. Седой. Похож на отца.'
        'На обороте — «2009».'
        
        menu:
            'Взять в руки и рассмотреть':
                'Алиса возвращается. Замечает, что я смотрю.'
                alice 'Это мой папа. Он умер.'
                main_bro 'Извини.'
                alice 'Ничего. Ты хороший. Что хочешь спросить — спрашивай.'
                $ alice_trust += 1
            'Не трогать':
                'Просто смотрю. Кладу обратно. Алиса не замечает.'
    else:
        'Я не решаюсь разглядывать. Отхожу.'

    return


label alice_examine_bed:

    $ alice_bed_examined = True
    'Аккуратно. Плед вязаный. Подушка с вышивкой. Просто и тепло.'
    'На тумбочке — старая книга стихов. Ахматова.'
    main_bro 'Она это читает? Странно. Но понятно.'
    'Больше ничего. Отхожу.'

    return


label alice_examine_photos:

    $ alice_photos_examined = True
    'На стене — несколько Polaroid. Алиса с одногруппниками.'
    
    'Вот она смеётся с какой-то девушкой. Вот на фоне универа. Вот — толпа людей.'
    
    'Я присматриваюсь. На одной из фотографий — Сергей. Молодой, длинные волосы. Стоит в стороне, не улыбается.'
    
    'Сейчас он другой. Но глаза те же.'
    
    if secret_sergy_alice_photo_unlocked:
        'Похоже на ту фотографию, что я видел у Сергейа на столе. Только здесь они не вместе — он отдельно.'
        'Странно. Как будто два мира.'

    return