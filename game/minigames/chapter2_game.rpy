# ==================== МИНИ-ИГРА: ОБРАБОТКА ЗАЯВОК ====================

screen minigame_approvals_screen:
    zorder 100
    add "office_desk_blur"
    
    # ТАЙМЕР
    timer 0.01 repeat True action If(
        time_left > 0 and not game_over,
        [SetVariable('time_left', time_left - 0.01)],
        [SetVariable('game_over', True), Return()]
    )
    
    # ВИЗУАЛЬНЫЕ ЭФФЕКТЫ
    if last_result == "correct":
        timer 0.3 action SetVariable('last_result', None)
        add "effect_correct":
            alpha 0.8
            xalign 0.5
            yalign 0.5
    
    if last_result == "wrong":
        timer 0.3 action SetVariable('last_result', None)
        add "effect_wrong":
            alpha 0.8
            xalign 0.5
            yalign 0.5
    
    frame:
        background "#000000cc"
        xfill True
        yfill True
        
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20
            
            hbox:
                spacing 80
                xalign 0.5
                text "ОДОБРЕНО: [stars]" size 24 color "#88ff88" outlines [(1, "#000000", 0, 0)]
                text "ОШИБОК: [mistakes]" size 24 color "#ff8888" outlines [(1, "#000000", 0, 0)]
                text "ОСТАЛОСЬ: [int(time_left)] сек" size 24 color "#ffaa44" outlines [(1, "#000000", 0, 0)]
            
            frame:
                background "#1a1a1a"
                xsize 720
                ysize 340
                padding (25, 25)
                
                vbox:
                    spacing 12
                    text "ЗАЯВКА [current_question + 1] из [total_questions]" size 18 color "#aaaaaa" text_align 0.5 xalign 0.5
                    null height 5
                    
                    if current_question == 0:
                        text "Клиент: ООО «ТехноСервис»" size 18 color "#cccccc"
                        text "Проблема: Задержка поставки оборудования на 2 недели" size 16 color "#bbbbbb"
                        text "Причина: Проблемы с логистикой из-за погодных условий" size 16 color "#bbbbbb"
                        text "Сумма ущерба: 120 000 руб." size 16 color "#ff8888"
                        text "Статус клиента: Постоянный, 5 лет сотрудничества" size 16 color "#88ff88"
                    elif current_question == 1:
                        text "Клиент: ИП «Смирнов»" size 18 color "#cccccc"
                        text "Проблема: Жалоба на качество товара (брак 3% от партии)" size 16 color "#bbbbbb"
                        text "Требование: Полный возврат денег на сумму 15 000 руб." size 16 color "#bbbbbb"
                        text "История: Третья жалоба за полгода" size 16 color "#ff8888"
                        text "Статус клиента: Новый, на грани блокировки" size 16 color "#ff8888"
                    elif current_question == 2:
                        text "Клиент: АО «СеверПром»" size 18 color "#cccccc"
                        text "Проблема: Несоответствие спецификации (не тот цвет)" size 16 color "#bbbbbb"
                        text "Дополнительно: Клиент сам не указал точный цвет в заказе" size 16 color "#ffaa44"
                        text "Сумма ущерба: 0 руб., отказ от замены" size 16 color "#88ff88"
                        text "Статус клиента: Крупный, 10 лет сотрудничества" size 16 color "#88ff88"
                    elif current_question == 3:
                        text "Клиент: ООО «СтройМаркет»" size 18 color "#cccccc"
                        text "Проблема: Задержка оплаты от клиента на 30 дней" size 16 color "#bbbbbb"
                        text "Требование: Перенести поставку без штрафов" size 16 color "#bbbbbb"
                        text "Комментарий: Проблемы с банком, документы приложены" size 16 color "#ffaa44"
                        text "Статус клиента: Надёжный, платит всегда" size 16 color "#88ff88"
                    elif current_question == 4:
                        text "Клиент: ЧП «Коваленко»" size 18 color "#cccccc"
                        text "Проблема: Претензия к сроку гарантии (пропустили 1 день)" size 16 color "#bbbbbb"
                        text "Требование: Бесплатный ремонт на сумму 45 000 руб." size 16 color "#bbbbbb"
                        text "История: Часто судится, два иска за год" size 16 color "#ff8888"
                        text "Статус клиента: Неблагонадёжный" size 16 color "#ff8888"
                    elif current_question == 5:
                        text "Клиент: ООО «ЛогистикТранс»" size 18 color "#cccccc"
                        text "Проблема: Заявка на увеличение кредитного лимита" size 16 color "#bbbbbb"
                        text "Текущий лимит: 500 000 руб., запрашивает: 1 500 000 руб." size 16 color "#ffaa44"
                        text "Годовой оборот: 3 000 000 руб., без просрочек" size 16 color "#88ff88"
                        text "Статус: Надёжный партнёр" size 16 color "#88ff88"
                    elif current_question == 6:
                        text "Клиент: ИП «Петрова»" size 18 color "#cccccc"
                        text "Проблема: Потеря документов при доставке" size 16 color "#bbbbbb"
                        text "Требование: Выслать копии срочно, таможня ждёт" size 16 color "#bbbbbb"
                        text "VIP-клиент, личное знакомство с директором" size 16 color "#88ff88"
                        text "Статус: Высший приоритет" size 16 color "#88ff88"
                    elif current_question == 7:
                        text "Клиент: ЗАО «ЭнергоСбыт»" size 18 color "#cccccc"
                        text "Проблема: Счёт выставлен с ошибкой (завышен на 200%)" size 16 color "#bbbbbb"
                        text "Сумма переплаты: 340 000 руб. по нашей вине" size 16 color "#ff8888"
                        text "Требование: Перерасчёт и извинения" size 16 color "#ffaa44"
                        text "Вердикт: Пусть переделывают заявку" size 16 color "#ff8888"
                    elif current_question == 8:
                        text "Клиент: ООО «МедТех»" size 18 color "#cccccc"
                        text "Проблема: Новый срочный заказ, нужно за 24 часа" size 16 color "#bbbbbb"
                        text "Стандартный срок: 5 дней, доплата 30%" size 16 color "#ffaa44"
                        text "Сумма: 450 000 руб." size 16 color "#88ff88"
                        text "Статус: Срочный платный заказ" size 16 color "#88ff88"
                    elif current_question == 9:
                        text "Клиент: ООО «СтройИнвест»" size 18 color "#cccccc"
                        text "Проблема: Требуют штраф за нашу задержку" size 16 color "#bbbbbb"
                        text "Задержка: 3 дня, причина: авария на складе" size 16 color "#ff8888"
                        text "Сумма штрафа: 75 000 руб., документов о форс-мажоре нет" size 16 color "#ff8888"
                        text "Вердикт: Отказать, пусть доказывают" size 16 color "#ff8888"
                    elif current_question == 10:
                        text "Клиент: ООО «ФиналТест»" size 18 color "#cccccc"
                        text "Проблема: Тестовая заявка на проверку системы" size 16 color "#bbbbbb"
                        text "Сумма: 0 руб., реальной операции нет" size 16 color "#ffaa44"
                        text "Решение: Одобрить для проверки" size 16 color "#88ff88"
                        text "Статус: Внутренний тест" size 16 color "#88ff88"
                    else:
                        text "Клиент: ЗАО «Контрольная»" size 18 color "#cccccc"
                        text "Проблема: Стандартная заявка" size 16 color "#bbbbbb"
                        text "Без проблем, всё в порядке" size 16 color "#88ff88"
                        text "Статус: Одобрить" size 16 color "#88ff88"
                    
                    null height 15
                    
                    hbox:
                        spacing 40
                        xalign 0.5
                        
                        textbutton "ОДОБРИТЬ ЗАЯВКУ":
                            xsize 220 ysize 55
                            background "#2a5a2a"
                            hover_background "#3a7a3a"
                            text_size 16
                            action [
                                Function(check_approval, True),  # ← добавляем проверку
                                If(current_question + 1 >= total_questions, Return(), None)
                            ]
                        
                        textbutton "ОТКЛОНИТЬ ЗАЯВКУ":
                            xsize 220 ysize 55
                            background "#5a2a2a"
                            hover_background "#7a3a3a"
                            text_size 16
                            action [
                                Function(check_approval, False),  # ← добавляем проверку
                                If(current_question + 1 >= total_questions, Return(), None)
                            ]
            
            text "Читайте внимательно. Одобряйте надёжных клиентов, отклоняйте проблемных" size 13 color "#666666"


# ==================== ЭТО ДОБАВИТЬ (ФУНКЦИЯ ПРОВЕРКИ) ====================

init python:
    def check_approval(is_approved):
        global stars, mistakes, current_question, last_result, apathy
        
        correct_answers = [
            True, False, True, True, False, True, True, False, True, False, True, True
        ]
        
        idx = current_question
        
        if idx >= len(correct_answers):
            return
        
        if is_approved == correct_answers[idx]:
            stars += 1
            last_result = "correct"
        else:
            mistakes += 1
            last_result = "wrong"
            apathy += 1
        
        current_question += 1