# для скачивания библиотек в консоли необходимо прописать
# pip install -r requirements.txt

from tkinter import *
from pygame import mixer #библиотека для работы со звуком
from PIL import Image, ImageTk
#-----------Работаем со звуком--------
mixer.init()
def play_music():
    mixer.music.load("BT-7274.mp3")
    mixer.music.play(loops=-1)

# ---------Класс для анимированного GIF-----------
class AnimatedGIF(Label):
    def __init__(self, master, path):
        Label.__init__(self, master)
        self.frames = []
        self.load_gif(path)
        self.index = 0
        self.update()

    def load_gif(self, path):
        img = Image.open(path)
        for frame in range(img.n_frames):
            img.seek(frame)
            self.frames.append(ImageTk.PhotoImage(img.copy()))

    def update(self):
        self.configure(image=self.frames[self.index])
        self.index += 1
        if self.index >= len(self.frames):
            self.index = 0
        self.after(100, self.update)  # обновление каждые 100 мс

# ---------Создаем "голое" окно-------
window = Tk()
width = 718
height = 404
window.title("Добро пожаловать в приложение PythonRu")
window.geometry(f"{width}x{height}+400+150")  # устанавливаем размер окна width*height
                                                    # в точку с коррдинатами(40, 150)

# ------------Создаем фон-----------

background_image = PhotoImage(file='res_ttnf.png')  # Загружаем изображение
lbl_bg = Label(window, image=background_image)

lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

# --------Создание фрейма, в котором будут хранится все метки-----------
frame = Frame(window)
frame.place(relx=0.5, rely=0.5, anchor='center')

# -------------Функция для сохранения значения из окна ввода-------------
entry_var = StringVar()  # Здесь мы создаем объект StringVar, который будет храниться в переменной entry_var.
                            # Этот объект будет отслеживать изменения в поле ввода.

def save_entry_value():
    saved_value = entry_var.get()
    temp = str(int(saved_value, 16))
    print(f"Сохраненное значение: {temp}")

    rez = f'DS{temp[0]}BG-{temp[1]}09KJ-T6{temp[2]}K8 {temp[-2:]}'

    print(f"Ключ: {rez}")
    lbl_result.configure(text=rez)


# ----------Создаём надпись, которая будет пояснять, что именно нужно ввести------------------
lbl_roots = Label(frame, text='Введите число в HEX, по которому будет сгенерирован ключ')
lbl_roots.grid(column=0, row=0)

# ---------Создаем поле ввода-----------

entry = Entry(frame, textvariable=entry_var, width=30)
entry.grid(column=0, row=1, padx=10, pady=15)

# ---------Создаем кнопку сохранения значения-----------
save_button = Button(frame, text="Сгенерировать", command=save_entry_value)
save_button.grid(column=1, row=1, padx=10, pady=15)

# ---------------Сгенерированный ключ-----------
lbl_result = Label(frame, text='Marvin is waiting for your code to generate the key!)', font=('Arial', 10))
lbl_result.grid(column=0, row=2)

# -----------Добавление анимации GIF-----------
gif_animation = AnimatedGIF(frame, "MARVIN_NEW.gif")
gif_animation.grid(column=0, row=3)

play_music() # включаем музыку
window.mainloop()  # Эта функция вызывает бесконечный цикл окна,
                        # поэтому окно будет ждать любого взаимодействия с пользователем,
                            # пока не будет закрыто.
