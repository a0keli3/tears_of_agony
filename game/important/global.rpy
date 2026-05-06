#  глобальные изменения или какие-то штучки
init python:
    def flash_text(message, duration=2.5, size=60):
        renpy.show('flash_screen', what=Text(message, size=size, color='#FFFFFF', text_align=0.5, xalign=0.5, yalign=0.5), zorder=1000, layer='screens')
        renpy.pause(duration)
        renpy.hide('flash_screen', layer='screens')

init python:
    # Функция для мини-игры, чтобы Ren'Py не ругался тут
    def process_approval(choice):
        pass

#----------------отсылочки мои любимые
default gosha_67 = False        # отсылка на Гошу

# --------------состоянияя
default apathy = 0              # уровень апатии (чем выше, тем хуже)
default energy = 2              # энергия (работоспособность)
default work_points = 0         # очки работы (влияют на карьерную ветку)

# ---------------отношения с нпсишками

default trust_max = 0           # доверие к Максу
default trust_kristina = 0      # доверие к Кристине

# --------------сюжетные штучки
default met_curator = False     # встретил ли куратора
default helped_sister = False    # помог ли сестре
default embraced_alter = False   # обнял ли Альтер эго