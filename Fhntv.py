from random import shuffle, randint
from tkinter import *
from tkinter import messagebox

# Создаем главное окно
root = Tk()
root.title('Таблица чисел')

# Глобальные переменные
nums = []      # список чисел
btns = []      # список кнопок
count = 0      # счетчик правильных нажатий
err = 0        # счетчик ошибок
row, col = 3, 5  # размеры таблицы по умолчанию
v = IntVar()   # переменная для выбора порядка (0 - min, 1 - max)

# Функция обработки нажатия кнопки
def hide(x):
    global nums, btns, count, err, row, col
    
    # Определяем следующее число в зависимости от выбранного режима
    if v.get() == 0:
        w = min(nums)
    else:
        w = max(nums)
    
    # Проверяем, правильная ли кнопка нажата
    if btns[x]['text'] == str(w):
        # Правильный выбор
        btns[x]['text'] = ''
        btns[x]['state'] = 'disabled'
        btns[x]['bg'] = 'lightgreen'
        nums.remove(w)
        count += 1
        
        # Проверяем, закончена ли игра
        if count == row * col:
            yes = messagebox.askyesno(
                'Игра окончена',
                f'Сделано {err} ошибок. Начать новую игру?'
            )
            if yes:
                newgame(row, col)
            else:
                root.destroy()
    else:
        # Неправильный выбор
        btns[x]['bg'] = 'pink'
        err += 1

# Функция создания новой игры
def newgame(n, m):
    global nums, btns, count, err, row, col
    
    # Устанавливаем новые размеры
    row, col = n, m
    count, err = 0, 0
    
    # Генерируем список чисел
    nums = []
    w = 0
    for i in range(row * col):
        w += randint(2, 7)
        nums.append(w)
    shuffle(nums)
    
    # Удаляем старые кнопки, если они есть
    if 'btns' in globals():
        for b in btns:
            b.destroy()
    
    # Создаем новые кнопки
    btns = []
    for i in range(row * col):
        b = Button(
            root,
            width=3,
            height=1,
            text=str(nums[i]),
            font=('Georgia', 16, 'bold'),
            command=lambda x=i: hide(x)
        )
        btns.append(b)
        b.grid(row=i // col, column=i % col)

# Создаем меню
menubar = Menu(root)
root.config(menu=menubar)

# Меню "Параметры" для выбора размера таблицы
submenu = Menu(menubar, tearoff=0)
submenu.add_command(
    label='3 строки, 4 столбца', 
    command=lambda: newgame(3, 4)
)
submenu.add_command(
    label='3 строки, 5 столбцов', 
    command=lambda: newgame(3, 5)
)
submenu.add_command(
    label='4 строки, 6 столбцов', 
    command=lambda: newgame(4, 6)
)
menubar.add_cascade(label='Параметры', menu=submenu)

# Меню "Порядок выбора" для выбора режима игры
dopmenu = Menu(menubar, tearoff=0)
dopmenu.add_radiobutton(
    label='По возрастанию', 
    variable=v, 
    value=0
)
dopmenu.add_radiobutton(
    label='По убыванию', 
    variable=v, 
    value=1
)
menubar.add_cascade(label='Порядок выбора', menu=dopmenu)

# Запускаем первую игру
newgame(3, 5)

# Запускаем главный цикл
root.mainloop()