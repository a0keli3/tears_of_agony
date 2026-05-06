# ==================== МИНИ-ИГРА: ПРЕЗЕНТАЦИЯ ====================

label minigame_presentation_engine:

    # ИНИЦИАЛИЗАЦИЯ ПЕРЕМЕННЫХ
    python:
        # Красивый текст с переносами (ДЛЯ ПРОСМОТРА)
        full_text_display = """Наша компания — это не просто цифры в отчётах. Это люди, которые каждый день приходят в офис, чтобы делать свою работу.

Даже когда внутри — пустота. Даже когда хочется всё бросить и уйти в никуда. Мы остаёмся. Потому что мы — команда.

Я не буду врать. Мне страшно. Но страх — это не слабость. Это топливо. Если вам не страшно — значит, вы ничего не делаете.

Я готов работать. Не потому что мне нужны деньги. А потому что я хочу доказать себе и вам, что способен на большее."""
        
        # Сплошной текст для СРАВНЕНИЯ (без переносов)
        full_text_compare = ("Наша компания — это не просто цифры в отчётах. Это люди, которые каждый день приходят в офис, чтобы делать свою работу. "
                            "Даже когда внутри — пустота. Даже когда хочется всё бросить и уйти в никуда. Мы остаёмся. Потому что мы — команда. "
                            "Я не буду врать. Мне страшно. Но страх — это не слабость. Это топливо. Если вам не страшно — значит, вы ничего не делаете. "
                            "Я готов работать. Не потому что мне нужны деньги. А потому что я хочу доказать себе и вам, что способен на большее.")
        
        # Упрощаем текст для сравнения
        full_text_normalized = full_text_compare.lower()
        full_text_normalized = full_text_normalized.replace("—", "-")
        full_text_normalized = full_text_normalized.replace("ё", "е")
        full_text_normalized = full_text_normalized.replace("«", '"').replace("»", '"')
        full_text_normalized = full_text_normalized.replace("…", "...")
        
        total_length = len(full_text_normalized)
        
        typed_text = ""
        current_position = 0
        confidence = 50
        time_limit = 600  # 10 минут
        time_left = time_limit
        game_over = False
        presentation_result = "lose"
        minigame_finished = False
        mistakes_count = 0
        reaction_message = ""
        show_transition = True
        scroll_position = 0.0
        
        # Для подсветки текста с учётом переносов
        display_positions = []
        compare_idx = 0
        for i, char in enumerate(full_text_display):
            if char == "\n":
                display_positions.append(-1)
            else:
                display_positions.append(compare_idx)
                compare_idx += 1
    
    if show_transition:
        scene black
        $ renpy.pause(2.0)
        $ show_transition = False
    
    call screen presentation_fulltext_screen
    
    if confidence >= 80:
        $ presentation_result = "win"
    elif confidence >= 50:
        $ presentation_result = "partial"
    else:
        $ presentation_result = "lose"
    
    return


# ==================== ЭКРАН МИНИ-ИГРЫ ====================

screen presentation_fulltext_screen:

    zorder 100
    
    add "presentation_blur"
    
    timer 0.02 repeat True action If(
        time_left > 0 and not game_over and not minigame_finished,
        SetVariable('time_left', time_left - 0.02),
        [SetVariable('game_over', True), Return("timeout")]
    )
    
    if reaction_message:
        timer 0.5 action SetVariable('reaction_message', "")
        if reaction_message == "perfect":
            add "flash_green"
        elif reaction_message == "mistake":
            add "flash_red"
    
    frame:
        background "#000000cc"
        xfill True
        yfill True
        
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 12
            
            hbox:
                spacing 50
                xalign 0.5
                
                text "УВЕРЕННОСТЬ: [confidence]" size 18 color "#ffaa44"
                text "ВРЕМЯ: [int(time_left)] сек" size 18 color "#ffaa44"
                text "ПРОГРЕСС: [int((current_position / total_length) * 100)]%" size 18 color "#88ff88"
                
                if mistakes_count > 0:
                    text "ОШИБОК: [mistakes_count]" size 18 color "#ff8888"
            
            if confidence >= 80:
                text "▷ Зал замер. Ты чувствуешь их внимание." size 13 color "#88ff88" xalign 0.5
            elif confidence >= 60:
                text "▷ Кто-то кивает. Это хороший знак." size 13 color "#aaffaa" xalign 0.5
            elif confidence >= 40:
                text "▷ Лица нейтральны. Ты пока не провалился." size 13 color "#aaaaaa" xalign 0.5
            elif confidence >= 20:
                text "▷ Один в зале смотрит в телефон. Другой зевает." size 13 color "#ffaa66" xalign 0.5
            else:
                text "▷ Шёпот. Кто-то смеётся. Ты теряешь их внимание." size 13 color "#ff6666" xalign 0.5
            
            frame:
                background "#0a0a0a"
                xsize 880
                ysize 280
                padding (20, 20)
                
                viewport:
                    xsize 840
                    ysize 240
                    scrollbars "vertical"
                    draggable True
                    mousewheel True
                    yinitial scroll_position
                    
                    vbox:
                        spacing 8
                        
                        $ colored_text = ""
                        $ idx = 0
                        for char in full_text_display:
                            if char == "\n":
                                $ colored_text += "\n"
                            else:
                                if display_positions[idx] != -1 and display_positions[idx] < current_position:
                                    $ colored_text += "{color=#88ff88}" + char + "{/color}"
                                else:
                                    $ colored_text += "{color=#666666}" + char + "{/color}"
                            $ idx += 1
                        
                        text colored_text:
                            size 18
                            line_spacing 8
            
            if embrace_alter:
                frame:
                    background "#1a1a2a"
                    xsize 880
                    ysize 40
                    padding (15, 8)
                    
                    text "ШЁПОТ: Печатай сплошной строкой, без нажатия Enter. Просто продолжай печатать текст.":
                        size 13
                        color "#8899ff"
                        italic True
            
            frame:
                background "#000000"
                xsize 880
                ysize 140
                padding (20, 15)
                
                vbox:
                    spacing 8
                    
                    text "ТВОЙ ВВОД (печатай сплошной строкой, Enter не нажимай):" size 14 color "#777777"
                    
                    viewport:
                        xsize 840
                        ysize 80
                        draggable True
                        mousewheel True
                        
                        input:
                            color "#ffffff"
                            size 16
                            length total_length + 50
                            changed fulltext_input_handler
                            default typed_text
                            xsize 820
            
            frame:
                xsize 880
                ysize 12
                background "#333333"
                
                bar:
                    value current_position
                    range total_length
                    xsize 880
                    ysize 12
                    left_bar "#3a8a5a"
                    right_bar "#333333"
            
            hbox:
                spacing 25
                xalign 0.5
                
                textbutton "СОРВАТЬ ВЫСТУПЛЕНИЕ" xalign 0.5:
                    xsize 200 ysize 45
                    background "#4a2a2a"
                    hover_background "#6a3a3a"
                    text_size 14
                    action Function(end_presentation)
    
    if minigame_finished:
        timer 0.5 action Return()


# ==================== УВЕДОМЛЕНИЕ ====================

screen notice_screen(message):
    zorder 200
    frame:
        background "#000000aa"
        xalign 0.5
        yalign 0.3
        padding (30, 15)
        
        text message:
            size 16
            color "#ff8888"
            text_align 0.5
    timer 1.5 action Hide("notice_screen")


# ==================== ФУНКЦИИ ====================

init python:
    
    def normalize_char_for_compare(c):
        c = c.lower()
        if c == "ё":
            return "е"
        if c == "—":
            return "-"
        if c in "«»":
            return '"'
        if c == "…":
            return "..."
        return c
    
    def fulltext_input_handler(s):
        global typed_text, current_position, confidence, mistakes_count
        global reaction_message, minigame_finished, total_length
        global full_text_normalized, scroll_position
        
        typed_text = s
        typed_normalized = ""
        
        for c in typed_text:
            typed_normalized += normalize_char_for_compare(c)
        
        old_position = current_position
        
        correct_typed = 0
        
        for i in range(min(len(typed_normalized), total_length)):
            if i < len(typed_normalized) and i < len(full_text_normalized):
                if typed_normalized[i] == full_text_normalized[i]:
                    correct_typed = i + 1
                else:
                    break
        
        current_position = correct_typed
        
        if len(typed_normalized) > old_position and old_position < total_length:
            if old_position < len(typed_normalized) and old_position < len(full_text_normalized):
                if typed_normalized[old_position] != full_text_normalized[old_position]:
                    mistakes_count += 1
                    confidence -= 2
                    reaction_message = "mistake"
                    renpy.show_screen("notice_screen", message="Ошибка! Будь внимательнее.")
        
        if correct_typed > old_position:
            confidence = min(confidence + 0.3, 100)
        
        confidence = min(max(confidence, 0), 100)
        
        if total_length > 0:
            scroll_position = current_position / total_length
        
        if current_position >= total_length:
            if mistakes_count == 0:
                confidence += 20
                reaction_message = "perfect"
                renpy.show_screen("notice_screen", message="Идеально! Выступление удалось.")
            elif mistakes_count <= 5:
                confidence += 10
                reaction_message = "perfect"
                renpy.show_screen("notice_screen", message="Хорошо! Ты справился.")
            else:
                confidence -= 5
                reaction_message = "mistake"
                renpy.show_screen("notice_screen", message="Много ошибок, но ты выступил.")
            
            confidence = min(max(confidence, 0), 100)
            minigame_finished = True
    
    def end_presentation():
        global minigame_finished
        minigame_finished = True
        renpy.hide_screen("presentation_fulltext_screen")
        renpy.return_statement()