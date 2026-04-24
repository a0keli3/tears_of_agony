
init python:
    def flash_text(message,duration = 2.5,size=60):
        renpy.show('flash_screen',what =Text(message,size=size,color='#FFFFFF',text_align = 0.5,xalign = 0.5,yalign =0.5),zorder=1000,layer = 'screens')
        renpy.pause(duration)
        renpy.hide('flash_screen',layer = 'screens')



define main_bro = Character('[viname]', color="#c7c7c7", cps=25)
define sister = Character('Ангелина',color="#c7c7c7", cps=25)
define friend_max = Character('Макс', color ="#c7c7c7", cps = 25) 
define unknown = Character('рандом', color ="#c7c7c7", cps = 25) #МЕГА ПЕРЕДЕЛАТЬ ЧТОБЫ БЫЛО ДВА РАЗНЫХ ПЕРСОНАЖА, А НЕ ОДНИМ.


$ trust_partner = 0

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.


# Игра начинается здесь:
label start:
    'Для начала выберите ваш пол'
    menu:
        'мужчина':
            $ pronoun = 1
        'женщина':
            $ pronoun = 0


    $ viname = renpy.input('Введите ваше имя')
    # прописать отсылки

    jump chapter1

 
   
