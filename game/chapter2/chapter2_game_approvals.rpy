
label chapter2_game_approvals:

    'Возвращаюсь за стол. Раскрываю первую заявку. Глаза разбегаются.'

    main_bro 'Пятьдесят штук... За день... Он издевается.'

    alter 'Не ной. Просто делай. Я помогу.'

    'Странно. Обычно она только мешает. А сегодня... хочет помочь?'

    # ИНИЦИАЛИЗАЦИЯ ПЕРЕМЕННЫХ ДЛЯ МИНИ-ИГРЫ
    python:
        stars = 0
        mistakes = 0
        current_question = 0
        total_questions = 12
        time_left = 45
        game_over = False
        last_result = None
        mini_confidence = 50.0 
    

    call screen minigame_approvals_screen
    
    if stars >= 9:
        'Последняя заявка. Ставлю подпись. Всё. Сделано.'
        main_bro 'Чёрт... Я сделал это.'
        alter 'А я говорила. Ты можешь больше, чем думаешь.'
        $ met_curator = True
        $ work_points += 10
        $ apathy -= 2
    elif stars >= 6:
        'Кое-как дотянул до конца. Не провал, но и не успех.'
        main_bro 'Сойдёт... Наверное.'
        $ met_curator = True
        $ work_points += 4
    else:
        'Цифры сливаются в одно пятно. Голова гудит. Я не успеваю.'
        main_bro 'Я не смог...'
        alter 'Ты не смог. Потому что не дал мне помочь до конца.'
        $ met_curator = False
        $ apathy += 4

    jump chapter2_after_curator