"""Вариант 2. В холодильнике 10 брикетов мороженого разного вида. Ребенку разрешается взять вечером не более 2 брикетов.
Подготовьте различные варианты поедания мороженного ребенком на неделю."""

import random
import tkinter as tk
from tkinter import ttk, messagebox


class IceCream:
    def __init__(self, flavor, quality, calories):
        self.flavor = flavor
        self.quality = quality
        self.calories = calories


class Schedule:
    def __init__(self, ice_creams):
        self.ice_creams = ice_creams
        self.schedule = {}
        self.daily_calories = {}
        self.overall_calories = 0
        self.window_schedule = []

    def allocate_ice_creams(self):
        days_of_week = ["День 1", "День 2", "День 3", "День 4", "День 5", "День 6", "День 7"]
        ice_cream_pool = self.ice_creams.copy()
        random.shuffle(ice_cream_pool)

        for day in days_of_week:
            self.schedule[day] = []
            self.daily_calories[day] = 0

            while len(self.schedule[day]) < random.randint(1, 2) and ice_cream_pool:
                ice_cream = ice_cream_pool.pop(0)

                if not self.check_duplicate_flavor(day, ice_cream.flavor):
                    self.schedule[day].append(ice_cream)
                    self.update_calories(day, ice_cream.calories)

    def check_duplicate_flavor(self, day, flavor):
        for ice_cream in self.schedule[day]:
            if ice_cream.flavor == flavor:
                return True
        return False

    def update_calories(self, day, calories):
        self.daily_calories[day] += calories
        self.overall_calories += calories

    def print_schedule(self):
        for day, ice_creams in self.schedule.items():
            self.window_schedule.append(str(day) + '\n')
            for ice_cream in ice_creams:
                self.window_schedule.append("Вкус: " + ice_cream.flavor)
                self.window_schedule.append("Качество: " + ice_cream.quality)
                self.window_schedule.append("Калории: " + str(ice_cream.calories))
                self.window_schedule.append("Калорий за день: " + str(self.daily_calories[day]))
        self.window_schedule.append("Всего калорий: " + str(self.overall_calories))
        return self.window_schedule


ice_creams = [
    (IceCream("Шоколад", "качественное", 100)),
    (IceCream("Банан", "некачественное", 150)),
    (IceCream("Клубника", "некачественное", 120)),
    (IceCream("Апельсин", "качественное", 80)),
    (IceCream("Ваниль", "некачественное", 110)),
    (IceCream("Лесные ягоды", "качественное", 90)),
    (IceCream("Облепиха", "некачественное", 130)),
    (IceCream("Смородина", "качественное", 70)),
    (IceCream("Крем-брюле", "некачественное", 140)),
    (IceCream("Сыр", "качественное", 60)),
]

schedule = Schedule(ice_creams)
schedule.allocate_ice_creams()


shift_maker_window = tk.Tk()

shift_maker_window.geometry("350x300")
shift_maker_window.resizable(False, False)

shift_maker_window.title("Мороженое")

label_function_name1 = tk.Label(shift_maker_window, text="Введите 1 для выведения расписания\n поедания мороженого", font='Arial 12')
label_function_name1.place(x=20, y=30)

text_box = ttk.Entry(shift_maker_window, font="Arial 12")
text_box.place(x=78, y=90)


def inserter(controller):
    if controller == "1":
        shift_maker_window.destroy()
        newWindow = tk.Tk()
        newWindow.title("Мороженное")
        newWindow.geometry("320x320")
        ice_creams_list = schedule.print_schedule()
        languages_var = tk.StringVar(value=ice_creams_list)
        listbox = tk.Listbox(newWindow, listvariable=languages_var, font="Arial 12")
        listbox.pack(side="left", fill="both", expand=1)
        scrollbar = tk.Scrollbar(newWindow, orient="vertical", command=listbox.yview)
        scrollbar.pack(side="right", fill="y")
    else:
        tk.messagebox.showwarning(title="Ошибка!", message="Введите корректное значение!")


shift_creator = tk.Button(shift_maker_window, text="Вывести список", font="Arial 16", command=lambda: inserter(text_box.get()), bg="gray", fg="black", height=1)
shift_creator.place(x=87, y=125)

shift_maker_window.mainloop()
