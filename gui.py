from tkinter import *
from tkinter import ttk

def someotherfunction(e=None):
    print('It works !')


# root window
root = Tk()
root.geometry('600x350')
root.title('Progressbar Demo')

# create all of the main containers
top_frame = Frame(root, bg='cyan', width=600, height=50, pady=3)
center = Frame(root, bg='gray2', width=50, height=40, padx=3, pady=3)
bottom_frame = Frame(root, bg='white', width=600, height=45, pady=3)
# btm_frame2 = Frame(root, bg='lavender', width=450, height=60, pady=3)

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0, sticky="ew")
center.grid(row=1, sticky="nsew")
bottom_frame.grid(row=3, sticky="ew")
# btm_frame2.grid(row=4, sticky="ew")

# Healthbars
player_health_bar = ttk.Progressbar(
    top_frame,
    orient='horizontal',
    mode='determinate',
    length=260
)
enemy_health_bar = ttk.Progressbar(
    top_frame,
    orient='horizontal',
    mode='determinate',
    length=260
)

player_health_bar.grid(column=0, row=0, columnspan=1, padx=10)
enemy_health_bar.grid(column=2, row=0, columnspan=1, padx=50)

# Center Area                              
center.grid_rowconfigure(0, weight=1)
center.grid_columnconfigure(1, weight=1)

ctr_left = Frame(center, bg='blue', width=260, height=190)
ctr_mid = Frame(center, bg='yellow', width=60, height=190,  pady=3)
ctr_right = Frame(center, bg='green', width=260, height=190,  pady=3)

ctr_left.grid(row=0, column=0, sticky="ns")
ctr_mid.grid(row=0, column=1, sticky="nsew")
ctr_right.grid(row=0, column=2, sticky="ns")

bottom_left_left = Frame(bottom_frame, bg='blue', width=150, height=40)
bottom_left = Frame(bottom_frame, bg='yellow', width=150, height=40, pady=3)
bottom_right = Frame(bottom_frame, bg='green', width=150, height=40, pady=3)
bottom_right_right = Frame(bottom_frame, bg='green', width=110, height=40, pady=3)

bottom_left_left.grid(row=0, column=0, sticky="ns", rowspan=2, columnspan=2)
bottom_left.grid(row=0, column=1, sticky="ns", rowspan=2, columnspan=2)
bottom_right.grid(row=0, column=2, sticky="ns", rowspan=2, columnspan=2)
bottom_right_right.grid(row=0, column=3, sticky="ns", rowspan=2, columnspan=2)

weapon_label = Label(bottom_frame, text='Weapon:')
damage_label = Label(bottom_frame, text='Damage:')

weapon_label.grid(row=0, column=0)
damage_label.grid(row=1, column=0)

weapon_field_label = Label(bottom_frame, text='Zweihander')
damage_field_label = Label(bottom_frame, text='35')

weapon_field_label.grid(row=0, column=1)
damage_field_label.grid(row=1, column=1)

armor_label = Label(bottom_frame, text='Armor:')
crit_chance_label = Label(bottom_frame, text='Defense:')

armor_label.grid(row=0, column=2)

armor_field_label = Label(bottom_frame, text='Loin Cloth')
defense_field_label = Label(bottom_frame, text='5')

armor_field_label.grid(row=0, column=3)
defense_field_label.grid(row=1, column=3)

crit_chance_label = Label(bottom_frame, text='Crit Chance:')
crit_percent_label = Label(bottom_frame, text='Crit Damage:')

crit_chance_label.grid(row=0, column=4)
crit_percent_label.grid(row=1, column=4)

crit_chance_field = Label(bottom_frame, text='35%')
crit_percent_field = Label(bottom_frame, text='200%')

crit_chance_field.grid(row=0, column=5)
crit_percent_field.grid(row=1, column=5)

gold_label = Label(bottom_frame, text='Gold:')
gold_field = Label(bottom_frame, text='0')

gold_label.grid(row=1, column=6)
gold_field.grid(row=1, column=7)

root.bind('<a>', someotherfunction)
root.mainloop()