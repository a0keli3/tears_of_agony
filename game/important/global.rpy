#  глобальные изменения или какие-то штучки


init python:
    def flash_text(message,duration = 2.5,size=60):
        renpy.show('flash_screen',what =Text(message,size=size,color='#FFFFFF',text_align = 0.5,xalign = 0.5,yalign =0.5),zorder=1000,layer = 'screens')
        renpy.pause(duration)
        renpy.hide('flash_screen',layer = 'screens')


default gosha_67 = False
default trust_partner = 0
default happy_bro = 0