import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
from explicit_heat_scheme import ExplicitForm
from tkinter import Toplevel

mainColor = '#C0D9E6'
textColor = '#000000'
drawingColor = '#FFFFFF'
class EquationForms(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Разработка электронного ресурса для поддержки курса ММПС.")

        self.menubar = tk.Menu(self, font=('Arial', 12))
        self.config(menu=self.menubar)

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=1, fill="both")

        self.heatEquationSolver_tab = HeatEquationSolver(self.notebook)
        self.notebook.add(self.heatEquationSolver_tab, text="Уравнение теплопроводности")

        self.waveEquationSolver_tab = WaveEquationSolver(self.notebook)
        self.notebook.add(self.waveEquationSolver_tab, text="Волновое уравнение")

        self.LaplassEquationSolver_tab = LaplassEquationSolver(self.notebook)
        self.notebook.add(self.LaplassEquationSolver_tab, text="Уравнение Лапласса")

        self.submenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Постановка задачи", menu=self.submenu)
        self.submenu.add_separator()
        self.submenu.add_command(label="Выход", command=self.quit)
        file_menu1 = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Уравнение теплопроводности", menu=file_menu1, font=('Arial', 12, 'bold'))
        file_menu1.add_command(label="Явная схема", command=self.open_explicit_form)
        file_menu2 = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Волновое уравнение", menu=file_menu2, font=('Arial', 12, 'bold'))
        file_menu3 = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Методы прогонки", menu=file_menu3, font=('Arial', 12, 'bold'))

    def open_explicit_form(self):
        explicit_form = ExplicitForm()
        explicit_form_images = explicit_form.get_images()
        for i, image_path in enumerate(explicit_form_images):
            explicit_form.show_image(image_path, position=(i * 50, i * 50))
        explicit_form.mainloop()

    def on_explicit_form_close(self):
        self.deiconify()

    def on_implicit_form_close(self):
        self.deiconify()

    def quit_form(self, event=None):
        self.destroy()

    def show_heatEquationSolver(self):
        self.notebook.select(self.heatEquationSolver_tab)

    def show_waveEquationSolver(self):
        self.notebook.select(self.waveEquationSolver_tab)

    def show_explicit_form(self):
        explicit_form = ExplicitForm(self)
        explicit_form.mainloop()


class HeatEquationSolver(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.image = ImageTk.PhotoImage(Image.open('images/wallpaper.png'))  # Фоновая картинка
        self.background_label = tk.Label(self, image=self.image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.title_label = tk.Label(self, text="КРАЕВАЯ ЗАДАЧА ДЛЯ УРАВНЕНИЯ ТЕПЛОПРОВОДНОСТИ",
                                    font=('Arial', 16, 'bold'), bg='#C0D9E6')
        self.title_label.pack(pady=20)
        # Add text labels
        text_below_title = ("Найти функцию u=u(x, t), удовлетворяющую в области определения Du,"
                            "\nуравнению теплопроводности и принимающую на Gu - границе области Du"
                            "\nDu = {x: 0 ≤ x ≤ 1, t: 0 ≤ t ≤ T }. "
                            "\nзначения g(x, t)"
                            "\При t=0  заданы начальные условия u(x, 0) = 𝜑(𝑥)"
                            "\n На границе области Gu заданы граничные (краевые условия)"
                            "\n g(x, t) : 𝑢(0,𝑡)=𝑢(1,𝑡)=0 – граничные условия"
                            )
        self.text_label = tk.Label(self, text=text_below_title, bg="white",
                                       font=('Arial', 14, 'bold'),
                                       anchor='w')
        self.text_label.pack(pady=10, padx=15, anchor='w')

        text_below_title_0 = "Геометрия области"
        self.text_label_0 = tk.Label(self, text=text_below_title_0, font=('Arial', 12, 'bold'), bg='#C0D9E6',
                                     anchor='w')
        self.text_label_0.pack(pady=19, padx=55, anchor='w')

        image_data_1 = [{"file": "wavely_graph.png", "text": "", "position": (305, 180)}]

        for item in image_data_1:
            image_path_1 = os.path.join("images", item["file"])
            image_1 = Image.open(image_path_1)
            photo_1 = ImageTk.PhotoImage(image_1)
            canvas_1 = tk.Canvas(self, width=image_1.width, height=image_1.height, bg='white', bd=1, relief='solid')
            canvas_1.place(x=35, y=258, anchor="w")
            canvas_1.create_image(0, 0, anchor=tk.NW, image=photo_1)
            canvas_1.photo = photo_1
            text_widget_1 = tk.Label(self, text=item["text"], font=('Arial', 12, 'bold'), bg='#C0D9E6')
            text_widget_1.place(x=item["position"][0], y=item["position"][1] - text_widget_1.winfo_reqheight() - 20)

        image_data_2 = [{"file": "heat_eq_1.png", "text": """где a - коэффициент теплопроводности(если u - температура) и массопроводности (если u - концентрация,давление в задачах фильтрации и т.п.)
               \nПоскольку в общий вид уравнения входит производная по времени, то необходимо задавать начальные условия при t = 0
                \nи граничные условия при x = 0, x = l, t > 0. """
                            , "position": (300, 425)}]

        for item_1 in image_data_2:
            image_path_2 = os.path.join("images", item_1["file"])
            image_2 = Image.open(image_path_2)
            photo_2 = ImageTk.PhotoImage(image_2)

            canvas_2 = tk.Canvas(self, width=image_2.width, height=image_2.height, bg='white', bd=1, relief='solid')
            canvas_2.place(x=300, y=200, anchor="w")
            canvas_2.create_image(0, 0, anchor=tk.NW, image=photo_2)
            canvas_2.photo = photo_2
            text_widget_2 = tk.Label(self, text=item_1["text"], font=('Arial', 12, 'bold'), bg='#C0D9E6',
                                     justify=tk.LEFT)
            text_widget_2.place(x=item_1["position"][0], y=item_1["position"][1] - text_widget_2.winfo_reqheight() - 20,
                                anchor='w')

        ###################  ПЕРВАЯ КРАЕВАЯ ЗАДАЧА ##########################################

        div_container = tk.Frame(self, bg=mainColor, bd=1, relief='solid')
        div_container.pack(padx=500, pady=600, anchor='w')
        div_container.pack_propagate(False)
        div_container.config(width=390, height=270)
        image_data_1_3 = [{"file": "therm_cond_bnd1.png", "text": """ПЕРВАЯ КРАЕВАЯ ЗАДАЧА
                                                                                     \n Краевые условия:""",
                           "position": (200, 300)}]
        for item_2 in image_data_1_3:
            # Добавление текста на холст
            text_widget_1_3 = tk.Label(div_container, text=item_2["text"], font=('Arial', 12, 'bold'), bg=mainColor,
                                       fg=textColor)
            text_widget_1_3.pack(anchor='center')  # Используем pack для text_widget_Laplass1

            # Загрузка изображения
            image_path_1_3 = os.path.join("images", item_2["file"])
            image_1_3 = Image.open(image_path_1_3)
            photo_1_3 = ImageTk.PhotoImage(image_1_3)

            # Создание холста внутри div-контейнера с размерами изображения и белым фоном
            canvas_Laplass1 = tk.Canvas(div_container, width=image_1_3.width, height=image_1_3.height, bg=drawingColor,
                                        bd=1,
                                        relief='solid')
            canvas_Laplass1.pack()

            # Размещение изображения на холсте
            canvas_Laplass1.create_image(0, 0, anchor=tk.NW, image=photo_1_3)
            # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
            canvas_Laplass1.photo = photo_1_3

        photo_1_4 = [{"file": "therm_cond_bnd1_st_data.png", "text": "Начальные данные", "position": (400, 400)}]

        for item_3 in photo_1_4:
            # Добавление текста на холст
            text_widget_1_4 = tk.Label(div_container, text=item_3["text"], font=('Arial', 12, 'bold'), bg=mainColor,
                                       fg=textColor)
            text_widget_1_4.pack(anchor='center')  # Используем pack для text_widget_Laplass1

            # Загрузка изображения
            image_path_1_4 = os.path.join("images", item_3["file"])
            image_1_4 = Image.open(image_path_1_4)
            photo_1_4 = ImageTk.PhotoImage(image_1_4)

            # Создание холста внутри div-контейнера с размерами изображения и белым фоном
            canvas_1_4 = tk.Canvas(div_container, width=image_1_4.width, height=image_1_4.height, bg=drawingColor, bd=1,
                                   relief='solid')
            canvas_1_4.pack()

            # Размещение изображения на холсте
            canvas_1_4.create_image(0, 0, anchor=tk.NW, image=photo_1_4)
            # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
            canvas_1_4.photo = photo_1_4

            # Размещение div-контейнера
            div_container.place(x=200, y=815, anchor="sw")

        # добавление всплывающего виджета с подсказкой

        bubble_container = tk.Frame(self, bg='#ffffff', bd=1, relief='solid')
        bubble_container.pack_propagate(False)
        bubble_container.config(width=390, height=370)
        etl_title = tk.Label(bubble_container, font=('Arial', 12, 'bold'), bg=drawingColor,
                             text='Первая краевая задача\n(Задача Дирихле)')
        etl_main = tk.Label(bubble_container, font=('Arial', 11), justify='left', wraplength=370, bg=drawingColor, text=
        '''значение темепературы задаётся на границах области (концентрации). 
        Граница поддерживается при постоянной температуре (концентрации) за счет внешнего источника тепла (вещества).
        Так, краевые условия задают температуру/концентрацию на разных концах стержня,
        В то время как начальные данные задают однородность температуры (концентрации) в начальный момент времени''')

        etl_title.place(x=195, y=50, anchor='s')
        etl_main.place(x=5, y=120, anchor='nw')

        bubble_container.pack_forget()

        def on_enter(event):
            bubble_container.place(x=200, y=540, anchor='sw')

        def on_leave(event):
            bubble_container.place_forget()

        div_container.bind("<Enter>", on_enter)
        div_container.bind("<Leave>", on_leave)

        ###################  ВТОРАЯ КРАЕВАЯ ЗАДАЧА ##########################################

        # Создание div-контейнера с белой рамкой
        div_container_1 = tk.Frame(self, bg=mainColor, bd=1, relief='solid')
        div_container_1.pack(pady=500, padx=600, anchor='w')  # Используем pack для div_container
        div_container_1.pack_propagate(False)
        div_container_1.config(width=390, height=270)
        image_data_2_1 = [{"file": "therm_cond_bnd2.png", "text": """ВТОРАЯ КРАЕВАЯ ЗАДАЧА
                                                                                       \n Краевые условия:""",
                           "position": (200, 300)}]

        for item_4 in image_data_2_1:
            # Добавление текста на холст
            text_widget_2_1 = tk.Label(div_container_1, text=item_4["text"], font=('Arial', 12, 'bold'), bg=mainColor,
                                       fg=textColor)
            text_widget_2_1.pack(anchor='center')  # Используем pack для text_widget_Laplass1

            # Загрузка изображения
            image_path_2_1 = os.path.join("images", item_4["file"])
            image_2_1 = Image.open(image_path_2_1)
            photo_2_1 = ImageTk.PhotoImage(image_2_1)

            # Создание холста внутри div-контейнера с размерами изображения и белым фоном
            canvas_Laplass2 = tk.Canvas(div_container_1, width=image_2_1.width, height=image_2_1.height,
                                        bg=drawingColor, bd=1,
                                        relief='solid')
            canvas_Laplass2.pack()

            # Размещение изображения на холсте
            canvas_Laplass2.create_image(0, 0, anchor=tk.NW, image=photo_2_1)
            # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
            canvas_Laplass2.photo = photo_2_1

        image_data_2_2 = [{"file": "therm_cond_bnd2_st_data.png", "text": "Начальные данные", "position": (300, 500)}]

        for item_5 in image_data_2_2:
            # Добавление текста на холст
            text_widget_2_2 = tk.Label(div_container_1, text=item_5["text"], font=('Arial', 12, 'bold'), bg=mainColor,
                                       fg=textColor)
            text_widget_2_2.pack(anchor='center')  # Используем pack для text_widget_Laplass1

            # Загрузка изображения
            image_path_2_2 = os.path.join("images", item_5["file"])
            image_2_2 = Image.open(image_path_2_2)
            photo_2_2 = ImageTk.PhotoImage(image_2_2)

            # Создание холста внутри div-контейнера с размерами изображения и белым фоном
            canvas_WEGREQ_2st = tk.Canvas(div_container_1, width=image_2_2.width, height=image_2_2.height,
                                          bg=drawingColor, bd=1,
                                          relief='solid')
            canvas_WEGREQ_2st.pack()

            # Размещение изображения на холсте
            canvas_WEGREQ_2st.create_image(0, 0, anchor=tk.NW, image=photo_2_2)
            # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
            canvas_WEGREQ_2st.photo = photo_2_2

            # Размещение div-контейнера
            div_container_1.place(x=930, y=815, anchor="s")

        # добавление всплывающего виджета с подсказкой
        bubble_container_1 = tk.Frame(self, bg='#ffffff', bd=1, relief='solid')
        bubble_container_1.pack_propagate(False)
        bubble_container_1.config(width=390, height=370)
        etl_1_title = tk.Label(bubble_container_1, font=('Arial', 12, 'bold'), bg=drawingColor,
                               text='Вторая краевая задача\n(Задача Неймана)')
        etl_1_main = tk.Label(bubble_container_1, font=('Arial', 11), justify='left', wraplength=370, bg=drawingColor,
                              text=
                              '''значения потока тепла (вещества) задается на границах области. 
        Через границы происходит теплообмен (диффузия) с определённой интенсивностью.
        Так, краевые условия задают потоки тепла на левом и на правом концах стержня,
        В то время как начальные данные задают однородность температуры (концентрации) в начальный момент времени''')

        etl_1_title.place(x=195, y=50, anchor='s')
        etl_1_main.place(x=5, y=120, anchor='nw')
        bubble_container_1.pack_forget()

        def on_enter(event):
            bubble_container_1.place(x=930, y=540, anchor='s')

        def on_leave(event):
            bubble_container_1.place_forget()

        div_container_1.bind("<Enter>", on_enter)
        div_container_1.bind("<Leave>", on_leave)

        ###################  ТРЕТЬЯ КРАЕВАЯ ЗАДАЧА ##########################################

        # Создание div-контейнера с белой рамкой
        div_container_2 = tk.Frame(self, bg=mainColor, bd=1, relief='solid', width=800, height=400)
        div_container_2.pack(pady=500, padx=600, anchor='w')  # Используем pack для div_container
        div_container_2.pack_propagate(False)
        div_container_2.config(width=390, height=270)
        image_data_3_1 = [{"file": "therm_cond_bnd3.png", "text": """ТРЕТЬЯ КРАЕВАЯ ЗАДАЧА
                                                                                             \n Краевые условия:""",
                           "position": (250, 300)}]

        for item_6 in image_data_3_1:
            # Добавление текста на холст
            text_widget_3_1 = tk.Label(div_container_2, text=item_6["text"], font=('Arial', 12, 'bold'),
                                       bg=mainColor, fg=textColor)
            text_widget_3_1.pack(anchor='center')  # Используем pack для text_widget_Laplass1

            # Загрузка изображения
            image_path_3_1 = os.path.join("images", item_6["file"])
            image_3_1 = Image.open(image_path_3_1)
            photo_3_1 = ImageTk.PhotoImage(image_3_1)

            # Создание холста внутри div-контейнера с размерами изображения и белым фоном
            canvas_3_1 = tk.Canvas(div_container_2, width=image_3_1.width, height=image_3_1.height, bg=drawingColor,
                                   bd=1, relief='solid')
            canvas_3_1.pack()

            # Размещение изображения на холсте
            canvas_3_1.create_image(0, 0, anchor=tk.NW, image=photo_3_1)
            # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
            canvas_3_1.photo = photo_3_1

            image_data_3_2 = [
                {"file": "therm_cond_bnd3_st_data.png", "text": "Начальные данные", "position": (300, 500)}]

            for item_7 in image_data_3_2:
                # Добавление текста на холст
                text_widget_3_2 = tk.Label(div_container_2, text=item_7["text"], font=('Arial', 12, 'bold'),
                                           bg=mainColor, fg=textColor)
                text_widget_3_2.pack(anchor='center')  # Используем pack для text_widget_Laplass1

                # Загрузка изображения
                image_path_3_2 = os.path.join("images", item_7["file"])
                image_3_2 = Image.open(image_path_3_2)
                photo_3_2 = ImageTk.PhotoImage(image_3_2)

                # Создание холста внутри div-контейнера с размерами изображения и белым фоном
                canvas_3_2 = tk.Canvas(div_container_2, width=image_3_2.width, height=image_3_2.height, bg=drawingColor,
                                       bd=1, relief='solid')
                canvas_3_2.pack()

                # Размещение изображения на холсте
                canvas_3_2.create_image(0, 0, anchor=tk.NW, image=photo_3_2)
                # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
                canvas_3_2.photo = photo_3_2

                # Размещение div-контейнера
                div_container_2.place(x=1670, y=815, anchor="se")

        # добавление всплывающего виджета с подсказкой

        bubble_container_2 = tk.Frame(self, bg='#ffffff', bd=1, relief='solid')
        bubble_container_2.pack_propagate(False)
        bubble_container_2.config(width=390, height=370)
        etl_2_title = tk.Label(bubble_container_2, font=('Arial', 12, 'bold'), bg=drawingColor,
                               text='Третья краевая задача\n(Задача Робина)')
        etl_2_main = tk.Label(bubble_container_2, font=('Arial', 11), justify='left', wraplength=370, bg=drawingColor,
                              text=
                              '''Комбинация значений температуры (концентрации) и потока тепла (вещества) задается на границах области. 
        Происходит теплообмен (диффузия) с окружающей средой, температура (концентрация) которой отличается от температуры (концентрации) на границе.
        Так, краевые условия задают теплообмен с окружающей средой (с указанной температурой), на левом и на правом концах стержня,
        В то время как начальные данные задают однородность температуры (концентрации) в начальный момент времени''')

        etl_2_title.place(x=195, y=50, anchor='s')
        etl_2_main.place(x=5, y=120, anchor='nw')
        bubble_container_2.pack_forget()

        def on_enter(event):
            bubble_container_2.place(x=1670, y=540, anchor='se')

        def on_leave(event):
            bubble_container_2.place_forget()

        div_container_2.bind("<Enter>", on_enter)
        div_container_2.bind("<Leave>", on_leave)


class WaveEquationSolver(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.image = ImageTk.PhotoImage(Image.open('images/wallpaper.png'))  # Фоновая картинка
        self.background_label = tk.Label(self, image=self.image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.title_label = tk.Label(self, text="Постановка задач для уравнений гиперболического типа",
                                    font=('Arial', 16, 'bold'), bg='#C0D9E6')
        self.title_label.pack(pady=20)
        text_below_title = "ВОЛНОВОЕ уравнение в области [ 0, l ] на отрезке времени [ 0, t ]:"
        self.text_label = tk.Label(self, text=text_below_title, font=('Arial', 12, 'bold'), bg='#C0D9E6', anchor='w')
        self.text_label.pack(pady=10, padx=15, anchor='w')

        text_below_title_0 = "Геометрия области"
        self.text_label_0 = tk.Label(self, text=text_below_title_0, font=('Arial', 12, 'bold'), bg='#C0D9E6',
                                     anchor='w')
        self.text_label_0.pack(pady=19, padx=55, anchor='w')

        image_data_1 = [{"file": "wavely_graph.png", "text": "Общий вид одномерного уравнения:", "position": (305, 180)}]

        for item in image_data_1:
            image_path_1 = os.path.join("images", item["file"])
            image_1 = Image.open(image_path_1)
            photo_1 = ImageTk.PhotoImage(image_1)
            canvas_1 = tk.Canvas(self, width=image_1.width, height=image_1.height, bg='white', bd=1, relief='solid')
            canvas_1.place(x=35, y=258, anchor="w")

            canvas_1.create_image(0, 0, anchor=tk.NW, image=photo_1)
            canvas_1.photo = photo_1
            text_widget_1 = tk.Label(self, text=item["text"], font=('Arial', 12, 'bold'), bg='#C0D9E6')
            text_widget_1.place(x=item["position"][0], y=item["position"][1] - text_widget_1.winfo_reqheight() - 20)

        image_data_2 = [{"file": "wave_equation_general_both.png", "text": """где a - скорость распространения малых возмущений в материале, из которого изготовлена струна, и
               \nu(x,t) - поперечные перемещения струны.
                \nГраничные условия при x = 0, x = l, t > 0. """
                            , "position": (300, 425)}]

        for item_1 in image_data_2:
            image_path_2 = os.path.join("images", item_1["file"])
            image_2 = Image.open(image_path_2)
            photo_2 = ImageTk.PhotoImage(image_2)
            canvas_2 = tk.Canvas(self, width=image_2.width, height=image_2.height, bg='white', bd=1, relief='solid')
            canvas_2.place(x=300, y=200, anchor="w")
            canvas_2.create_image(0, 0, anchor=tk.NW, image=photo_2)
            canvas_2.photo = photo_2
            text_widget_2 = tk.Label(self, text=item_1["text"], font=('Arial', 12, 'bold'), bg='#C0D9E6',
                                     justify=tk.LEFT)
            text_widget_2.place(x=item_1["position"][0], y=item_1["position"][1] - text_widget_2.winfo_reqheight() - 20,
                                anchor='w')

            ###################  ПЕРВАЯ НАЧАЛЬНО-КРАЕВАЯ ЗАДАЧА ##########################################

            # Создание div-контейнера с белой рамкой
            div_container = tk.Frame(self, bg=mainColor, bd=1, relief='solid')
            div_container.pack(padx=600, pady=800, anchor='w')
            div_container.pack_propagate(False)
            div_container.config(width=390, height=270)
            Image_data_WEG_1_1 = [{"file": "wavely_bnd1.png", "text": """ПЕРВАЯ НАЧАЛЬНО-КРАЕВАЯ ЗАДАЧА
                                                                                                    \n Краевые условия:""",
                                   "position": (200, 300)}]

            for item_2 in Image_data_WEG_1_1:
                # Добавление текста на холст
                text_widget_WEG_1_1 = tk.Label(div_container, text=item_2["text"], font=('Arial', 12, 'bold'),
                                               bg=mainColor, fg=textColor)
                text_widget_WEG_1_1.pack(anchor='center')  # Используем pack для text_widget_Laplass1

                # Загрузка изображения
                Image_path_WEG_1_1 = os.path.join("images", item_2["file"])
                Image_WEG_1_1 = Image.open(Image_path_WEG_1_1)
                photo_WEG_1_1 = ImageTk.PhotoImage(Image_WEG_1_1)

                # Создание холста внутри div-контейнера с размерами изображения и белым фоном
                canvas_WEG_1_1 = tk.Canvas(div_container, width=Image_WEG_1_1.width, height=Image_WEG_1_1.height,
                                           bg=drawingColor,
                                           relief='solid')
                canvas_WEG_1_1.pack()

                # Размещение изображения на холсте
                canvas_WEG_1_1.create_image(0, 0, anchor=tk.NW, image=photo_WEG_1_1)
                # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
                canvas_WEG_1_1.photo = photo_WEG_1_1

            photo_WEG_1_2 = [{"file": "wavely_bnd1_st_data.png", "text": "Начальные данные", "position": (400, 400)}]

            for item_3 in photo_WEG_1_2:
                # Добавление текста на холст
                text_widget_WEG_1_2 = tk.Label(div_container, text=item_3["text"], font=('Arial', 12, 'bold'),
                                               bg=mainColor, fg=textColor)
                text_widget_WEG_1_2.pack(anchor='center')  # Используем pack для text_widget_Laplass1

                # Загрузка изображения
                image_path_WEG_1_2 = os.path.join("images", item_3["file"])
                image_WEG_1_2 = Image.open(image_path_WEG_1_2)
                photo_WEG_1_2 = ImageTk.PhotoImage(image_WEG_1_2)

                # Создание холста внутри div-контейнера с размерами изображения и белым фоном
                canvas_WEGREQ1st = tk.Canvas(div_container, width=image_WEG_1_2.width, height=image_WEG_1_2.height,
                                             bg=drawingColor, bd=1,
                                             relief='solid')
                canvas_WEGREQ1st.pack()

                # Размещение изображения на холсте
                canvas_WEGREQ1st.create_image(0, 0, anchor=tk.NW, image=photo_WEG_1_2)
                # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
                canvas_WEGREQ1st.photo = photo_WEG_1_2

                # Размещение div-контейнера
                div_container.place(x=200, y=815, anchor="sw")

            # добавление всплывающего виджета с подсказкой

            bubble_container = tk.Frame(self, bg='#ffffff', bd=1, relief='solid')
            bubble_container.pack_propagate(False)
            bubble_container.config(width=390, height=370)
            etl_title = tk.Label(bubble_container, font=('Arial', 12, 'bold'), bg=drawingColor,
                                 text='Первая краевая задача\n(Задача Дирихле)')
            etl_main = tk.Label(bubble_container, font=('Arial', 11), justify='left', wraplength=370, bg=drawingColor,
                                text=
                                ''' 
            Происходит распространение волн в окружающей среде, скорость колебаний которой отличается от скорости колебаний на границе.
            Так, краевые условия задают фиксированное значение колебаний на границах пространства,
            В то время как начальные данные задают характер колебаний в начальный момент времени''')

            etl_title.place(x=195, y=50, anchor='s')
            etl_main.place(x=5, y=120, anchor='nw')
            bubble_container.pack_forget()

            def on_enter(event):
                bubble_container.place(x=200, y=540, anchor='sw')

            def on_leave(event):
                bubble_container.place_forget()

            div_container.bind("<Enter>", on_enter)
            div_container.bind("<Leave>", on_leave)

            ###################  ВТОРАЯ НАЧАЛЬНО-КРАЕВАЯ ЗАДАЧА ##########################################

            # Создание div-контейнера с белой рамкой
            div_container_1 = tk.Frame(self, bg=mainColor, bd=1, relief='solid')
            div_container_1.pack(pady=500, padx=600, anchor='w')  # Используем pack для div_container
            div_container_1.pack_propagate(False)
            div_container_1.config(width=390, height=270)
            image_data_WEG_2_1 = [{"file": "wavely_bnd2.png", "text": """ВТОРАЯ КРАЕВАЯ ЗАДАЧА
                                                                                                           \n Краевые условия:""",
                                   "position": (200, 300)}]

            for item_4 in image_data_WEG_2_1:
                # Добавление текста на холст
                text_widget_WEG_2_1 = tk.Label(div_container_1, text=item_4["text"], font=('Arial', 12, 'bold'),
                                               bg=mainColor, fg=textColor)
                text_widget_WEG_2_1.pack(anchor='center')  # Используем pack для text_widget_Laplass1

                # Загрузка изображения
                image_path_WEG_2_1 = os.path.join("images", item_4["file"])
                image_WEG_2_1 = Image.open(image_path_WEG_2_1)
                photo_WEG_2_1 = ImageTk.PhotoImage(image_WEG_2_1)

                # Создание холста внутри div-контейнера с размерами изображения и белым фоном
                canvas_Laplass2 = tk.Canvas(div_container_1, width=image_WEG_2_1.width, height=image_WEG_2_1.height,
                                            bg=drawingColor,
                                            bd=1,
                                            relief='solid')
                canvas_Laplass2.pack()

                # Размещение изображения на холсте
                canvas_Laplass2.create_image(0, 0, anchor=tk.NW, image=photo_WEG_2_1)
                # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
                canvas_Laplass2.photo = photo_WEG_2_1

            image_data_WEGREQ_2st = [
                {"file": "wavely_bnd2_st_data.png", "text": "Начальные данные", "position": (300, 500)}]

            for item_5 in image_data_WEGREQ_2st:
                # Добавление текста на холст
                text_widget_WEGREQ_2st = tk.Label(div_container_1, text=item_5["text"], fg=textColor,
                                                  font=('Arial', 12, 'bold'),
                                                  bg=mainColor)
                text_widget_WEGREQ_2st.pack(anchor='center')  # Используем pack для text_widget_Laplass1

                # Загрузка изображения
                image_path_WEGREQ_2st = os.path.join("images", item_5["file"])
                image_WEGREQ_2st = Image.open(image_path_WEGREQ_2st)
                photo_WEGREQ_2st = ImageTk.PhotoImage(image_WEGREQ_2st)

                # Создание холста внутри div-контейнера с размерами изображения и белым фоном
                canvas_WEGREQ_2st = tk.Canvas(div_container_1, width=image_WEGREQ_2st.width,
                                              height=image_WEGREQ_2st.height, bg=drawingColor,
                                              bd=1,
                                              relief='solid')
                canvas_WEGREQ_2st.pack()

                # Размещение изображения на холсте
                canvas_WEGREQ_2st.create_image(0, 0, anchor=tk.NW, image=photo_WEGREQ_2st)
                # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
                canvas_WEGREQ_2st.photo = photo_WEGREQ_2st

                # Размещение div-контейнера
                div_container_1.place(x=930, y=815, anchor="s")

            # добавление всплывающего виджета с подсказкой

            bubble_container_1 = tk.Frame(self, bg='#ffffff', bd=1, relief='solid')
            bubble_container_1.pack_propagate(False)
            bubble_container_1.config(width=390, height=370)
            etl_title_1 = tk.Label(bubble_container_1, font=('Arial', 12, 'bold'), bg=drawingColor,
                                   text='Вторая краевая задача\n(Задача Неймана)')
            etl_main_1 = tk.Label(bubble_container_1, font=('Arial', 11), justify='left', bg=drawingColor,
                                  wraplength=370, text=
                                  ''' 
            Происходит распространение волн в окружающей среде, скорость колебаний которой отличается от скорости колебаний на границе.
            Так, краевые условия задают скорость изменения колебаний на границах пространства,
            В то время как начальные данные задают характер колебаний в начальный момент времени''')

            etl_title_1.place(x=195, y=50, anchor='s')
            etl_main_1.place(x=5, y=120, anchor='nw')
            bubble_container_1.pack_forget()

            def on_enter(event):
                bubble_container_1.place(x=930, y=540, anchor='s')

            def on_leave(event):
                bubble_container_1.place_forget()

            div_container_1.bind("<Enter>", on_enter)
            div_container_1.bind("<Leave>", on_leave)

            ###################  ТРЕТЬЯ НАЧАЛЬНО-КРАЕВАЯ ЗАДАЧА ##########################################

            # Создание div-контейнера с белой рамкой
            div_container_2 = tk.Frame(self, bg=mainColor, bd=1, relief='solid')
            div_container_2.pack(pady=500, padx=600, anchor='w')  # Используем pack для div_container
            div_container_2.pack_propagate(False)
            div_container_2.config(width=390, height=270)
            image_data_WEG_3_1 = [{"file": "wavely_bnd3.png", "text": """ТРЕТЬЯ НАЧАЛЬНО-КРАЕВАЯ ЗАДАЧА
                                                                                                                 \n Краевые условия:""",
                                   "position": (200, 300)}]

            for item_6 in image_data_WEG_3_1:
                # Добавление текста на холст
                image_data_WEG_3_1 = tk.Label(div_container_2, text=item_6["text"], font=('Arial', 12, 'bold'),
                                              bg=mainColor, fg=textColor)
                image_data_WEG_3_1.pack(anchor='center')  # Используем pack для text_widget_Laplass1

                # Загрузка изображения
                image_path_WEG_3_1 = os.path.join("images", item_6["file"])
                image_WEG_3_1 = Image.open(image_path_WEG_3_1)
                photo_WEG_3_1 = ImageTk.PhotoImage(image_WEG_3_1)

                # Создание холста внутри div-контейнера с размерами изображения и белым фоном
                canvas_WEG_3_1 = tk.Canvas(div_container_2, width=image_WEG_3_1.width, height=image_WEG_3_1.height,
                                           bg=drawingColor,
                                           bd=1, relief='solid')
                canvas_WEG_3_1.pack()

                # Размещение изображения на холсте
                canvas_WEG_3_1.create_image(0, 0, anchor=tk.NW, image=photo_WEG_3_1)
                # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
                canvas_WEG_3_1.photo = photo_WEG_3_1

            image_data_WEG_3_2 = [
                {"file": "wavely_bnd3_st_data.png", "text": "Начальные данные", "position": (300, 500)}]
            for item_7 in image_data_WEG_3_2:
                # Добавление текста на холст
                text_widget_WEG_3_2 = tk.Label(div_container_2, text=item_7["text"], font=('Arial', 12, 'bold'),
                                               bg=mainColor, fg=textColor)
                text_widget_WEG_3_2.pack(anchor='center')  # Используем pack для text_widget_Laplass1

                # Загрузка изображения
                image_path_WEG_3_2 = os.path.join("images", item_7["file"])
                image_WEG_3_2 = Image.open(image_path_WEG_3_2)
                photo_WEG_3_2 = ImageTk.PhotoImage(image_WEG_3_2)

                # Создание холста внутри div-контейнера с размерами изображения и белым фоном
                canvas_WEG_3_2 = tk.Canvas(div_container_2, width=image_WEG_3_2.width, height=image_WEG_3_2.height,
                                           bg=drawingColor,
                                           bd=1, relief='solid')
                canvas_WEG_3_2.pack()

                # Размещение изображения на холсте
                canvas_WEG_3_2.create_image(0, 0, anchor=tk.NW, image=photo_WEG_3_2)
                # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
                canvas_WEG_3_2.photo = photo_WEG_3_2

                # Размещение div-контейнера
                div_container_2.place(x=1670, y=815, anchor="se")

            # добавление всплывающего виджета с подсказкой

            bubble_container_2 = tk.Frame(self, bg='#ffffff', bd=1, relief='solid')
            bubble_container_2.pack_propagate(False)
            bubble_container_2.config(width=390, height=370)
            etl_title_2 = tk.Label(bubble_container_2, font=('Arial', 12, 'bold'), bg=drawingColor,
                                   text='Третья краевая задача\n(Задача Робина)')
            etl_main_2 = tk.Label(bubble_container_2, font=('Arial', 11), justify='left', bg=drawingColor,
                                  wraplength=370, text=
                                  ''' 
            Происходит распространение волн в окружающей среде, скорость колебаний которой отличается от скорости колебаний на границе.
            Так, краевые условия задают взаимодействие физической величины (отражения, поглощения, преломления волн) на границе пространства с окружающим пространством,
            В то время как начальные данные задают характер колебаний в начальный момент времени''')

            etl_title_2.place(x=195, y=50, anchor='s')
            etl_main_2.place(x=5, y=120, anchor='nw')
            bubble_container_2.pack_forget()

            def on_enter(event):
                bubble_container_2.place(x=1670, y=540, anchor='se')

            def on_leave(event):
                bubble_container_2.place_forget()

            div_container_2.bind("<Enter>", on_enter)
            div_container_2.bind("<Leave>", on_leave)

class LaplassEquationSolver(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.image = ImageTk.PhotoImage(Image.open('images/wallpaper.png'))  # Фоновая картинка
        self.background_label = tk.Label(self, image=self.image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Заголовок формы
        self.title_label = tk.Label(self, text="Постановка задач для уравнений эллиптического типа",
                                    font=('Arial', 16, 'bold'), bg=mainColor, fg=textColor)
        self.title_label.pack(pady=20)

        # Текст под заголовком
        text_below_title = "Уравнение Лапласа в системе координат (X;Y):"
        self.text_label = tk.Label(self, text=text_below_title, font=('Arial', 12, 'bold'), bg=mainColor, anchor='w')
        self.text_label.pack(pady=10, padx=15, anchor='w')

        # Текст под заголовком
        text_below_title_0 = "Геометрия области"
        self.text_label_0 = tk.Label(self, text=text_below_title_0, font=('Arial', 12, 'bold'), bg=mainColor, fg=textColor,
                                     anchor='w')
        self.text_label_0.pack(pady=19, padx=55, anchor='w')

        # Список имен файлов изображений и соответствующих текстов
        image_data_1 = [{"file": "laplass_graph.png", "text": "Общий вид одномерного уравнения:", "position": (305, 170)}]

        for item in image_data_1:
            # Загрузка изображения
            image_path_1 = os.path.join("images", item["file"])
            image_1 = Image.open(image_path_1)
            photo_1 = ImageTk.PhotoImage(image_1)

            # Создание холста с размерами изображения и drawingColor фоном
            canvas_1 = tk.Canvas(self, width=image_1.width, height=image_1.height, bg=drawingColor, bd=1, relief='solid')
            canvas_1.place(x=35, y=258, anchor="w")

            # Размещение изображения на холсте
            canvas_1.create_image(0, 0, anchor=tk.NW, image=photo_1)

            # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
            canvas_1.photo = photo_1

            # Добавление текста на холст
            text_widget_1 = tk.Label(self, text=item["text"], font=('Arial', 12, 'bold'), bg=mainColor, fg=textColor)
            text_widget_1.place(x=item["position"][0], y=item["position"][1] - text_widget_1.winfo_reqheight() - 20)

            # Список имен файлов изображений и соответствующих текстов
        image_data_2 = [{"file": "laplass_general.png", "text": """где u(x,y) - может быть:
                    \n1.\tстационарным (не зависящим от времени) распределением температуры, 
                    \n2.\tскоростью потенциального (безвихревого) течения идеальной жидкости,
                    \n3.\tраспределение напряжённости электрического и магнитного полей 
                    \nи т.д."""
                            , "position": (300, 550)}]

        for item_1 in image_data_2:
            # Загрузка изображения
            image_path_2 = os.path.join("images", item_1["file"])
            image_2 = Image.open(image_path_2)
            photo_2 = ImageTk.PhotoImage(image_2)

            # Создание холста с размерами изображения и drawingColor фоном
            canvas_2 = tk.Canvas(self, width=image_2.width, height=image_2.height, bg=drawingColor, bd=1, relief='solid')
            canvas_2.place(x=300, y=200, anchor="w")

            # Размещение изображения на холсте
            canvas_2.create_image(0, 0, anchor=tk.NW, image=photo_2)

            # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
            canvas_2.photo = photo_2

            # Добавление текста на холст
            text_widget_2 = tk.Label(self, text=item_1["text"], font=('Arial', 12, 'bold'), bg=mainColor, fg=textColor,
                                     justify=tk.LEFT)
            text_widget_2.place(x=item_1["position"][0], y=item_1["position"][1] - text_widget_2.winfo_reqheight() - 20,
                                anchor='w')


            ###################  ПЕРВАЯ НАЧАЛЬНО-КРАЕВАЯ ЗАДАЧА ##########################################

            # Создание div-контейнера с белой рамкой
            div_container = tk.Frame(self, bg=mainColor, bd=1, relief='solid')
            div_container.pack(padx=600, pady=800, anchor='w')
            div_container.pack_propagate(False)
            div_container.config(width=500, height=250)
            Image_data_LPS_1_1 = [{"file": "laplass_bnd1.png", "text": """ПЕРВАЯ НАЧАЛЬНО-КРАЕВАЯ ЗАДАЧА
                                                                                                \n Краевые условия:""",
                                  "position": (200, 300)}]

            for item_2 in Image_data_LPS_1_1:
                # Добавление текста на холст
                text_widget_LPS_1_1 = tk.Label(div_container, text=item_2["text"], font=('Arial', 12, 'bold'), bg=mainColor, fg=textColor)
                text_widget_LPS_1_1.pack(anchor='center')  # Используем pack для text_widget_Laplass1

                # Загрузка изображения
                Image_path_LPS_1_1 = os.path.join("images", item_2["file"])
                Image_LPS_1_1 = Image.open(Image_path_LPS_1_1)
                photo_LPS_1_1 = ImageTk.PhotoImage(Image_LPS_1_1)

                # Создание холста внутри div-контейнера с размерами изображения и белым фоном
                canvas_LPS_1_1 = tk.Canvas(div_container, width=Image_LPS_1_1.width, height=Image_LPS_1_1.height, bg=drawingColor,
                                       bd=1,
                                       relief='solid')
                canvas_LPS_1_1.pack()

                # Размещение изображения на холсте
                canvas_LPS_1_1.create_image(0, 0, anchor=tk.NW, image=photo_LPS_1_1)
                # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
                canvas_LPS_1_1.photo = photo_LPS_1_1

            photo_WEGREQ1st = [{"file": "laplass_bnd1_st_data.png", "text": "Начальные данные", "position": (400, 400)}]

            for item_3 in photo_WEGREQ1st:
               # Добавление текста на холст
                text_widget_1_4 = tk.Label(div_container, text=item_3["text"], font=('Arial', 12, 'bold'), bg=mainColor)
                text_widget_1_4.pack(anchor='center')  # Используем pack для text_widget_Laplass1

                # Загрузка изображения
                image_path_WEGREQ1st = os.path.join("images", item_3["file"])
                image_WEGREQ1st = Image.open(image_path_WEGREQ1st)
                photo_WEGREQ1st = ImageTk.PhotoImage(image_WEGREQ1st)

                # Создание холста внутри div-контейнера с размерами изображения и белым фоном
                canvas_WEGREQ1st = tk.Canvas(div_container, width=image_WEGREQ1st.width, height=image_WEGREQ1st.height,
                                             bg=drawingColor, bd=1,
                                             relief='solid')
                canvas_WEGREQ1st.pack()

                # Размещение изображения на холсте
                canvas_WEGREQ1st.create_image(0, 0, anchor=tk.NW, image=photo_WEGREQ1st)
                # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
                canvas_WEGREQ1st.photo = photo_WEGREQ1st

                # Размещение div-контейнера
                div_container.place(x=50, y=865, anchor="sw")

            # добавление всплывающего виджета с подсказкой

            bubble_container = tk.Frame(self, bg='#ffffff', bd=1, relief='solid')
            bubble_container.pack_propagate(False)
            bubble_container.config(width=500, height=370)

            etl_title = tk.Label(bubble_container, font=('Arial', 11, 'bold'),
                                 text='Первая краевая задача\n(Задача Дирихле)', bg = drawingColor)
            etl_title.place(x=205, y=45, anchor='s')
            extra_text_label_1 = tk.Label(bubble_container,justify='left', wraplength=200, bg=drawingColor, text=
            '''
            Параметры a и b задают прямоугольную область, внутри которой предлагается найти такую функцию U(x,y), которая бы удовлетворяла уравнению Лапласа. 
            Краевые задачи (на графике) задают значения на границах области. Также, будем считать, что U(x,y) - непрерывна на границе области, и значения функций 
            в соответствующих краевых точках равны друг другу.
            ''')
            extra_text_label_1.place(x=220, y=50)

            extra_text_label_2 = tk.Label(bubble_container, justify='left', wraplength=400, bg=drawingColor, text=
            '''
            Функция U может описывать множество явлений. Важно, чтобы на границе области задавались фиксированные значения, с помощью заданных краевых функций f (на графике обозначены как t).
            ''')
            extra_text_label_2.place(x=10, y=270)
            extra_image = [
                {"file": "Laplass_bnd_addict.png", "text": "Геометрия области уравнения:", "position": (305, 200)}]

            for item in extra_image:
                # Загрузка изображения
                image_path_1 = os.path.join("images", item["file"])
                image_1 = Image.open(image_path_1)
                photo_1 = ImageTk.PhotoImage(image_1)

                # Создание холста с размерами изображения и drawingColor фоном
                canvas_1 = tk.Canvas(bubble_container, width=image_1.width, height=image_1.height, bd=1,
                                     relief='solid')
                canvas_1.place(x=15, y=175, anchor="w")

                # Размещение изображения на холсте
                canvas_1.create_image(0, 0, anchor=tk.NW, image=photo_1)

                # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
                canvas_1.photo = photo_1

                # Добавление текста на холст
                text_widget_1 = tk.Label(bubble_container, text=item["text"], font=('Arial', 8, 'bold'), bg=drawingColor,
                                         fg=textColor)
                text_widget_1.place(x=20, y=50)



            bubble_container.pack_forget()

            def on_enter(event):
                bubble_container.place(x=50, y=610, anchor='sw')

            def on_leave(event):
                bubble_container.place_forget()

            div_container.bind("<Enter>", on_enter)
            div_container.bind("<Leave>", on_leave)
            ###################  ВТОРАЯ НАЧАЛЬНО-КРАЕВАЯ ЗАДАЧА ##########################################

            # Создание div-контейнера с белой рамкой
            div_container_1 = tk.Frame(self, bg=mainColor, bd=1, relief='solid')
            div_container_1.pack(pady=500, padx=600, anchor='w')  # Используем pack для div_container
            div_container_1.pack_propagate(False)
            div_container_1.config(width=520, height=250)
            image_data_LPS_2_1 = [{"file": "laplass_bnd2.png", "text": """ВТОРАЯ КРАЕВАЯ ЗАДАЧА\n
                                                                                                       \n Краевые условия:""",
                                       "position": (200, 300)}]

            for item_4 in image_data_LPS_2_1:
                # Добавление текста на холст
                text_widget_LPS_2_1 = tk.Label(div_container_1, text=item_4["text"], font=('Arial', 12, 'bold'),
                                                   bg=mainColor, fg=textColor)
                text_widget_LPS_2_1.pack(anchor='center')  # Используем pack для text_widget_Laplass1

                # Загрузка изображения
                image_path_LPS_2_1 = os.path.join("images", item_4["file"])
                image_LPS_2_1 = Image.open(image_path_LPS_2_1)
                photo_LPS_2_1 = ImageTk.PhotoImage(image_LPS_2_1)

                # Создание холста внутри div-контейнера с размерами изображения и белым фоном
                canvas_LPS_2_1 = tk.Canvas(div_container_1, width=image_LPS_2_1.width, height=image_LPS_2_1.height,
                                           bg=drawingColor,
                                           bd=1,
                                           relief='solid')
                canvas_LPS_2_1.pack()

                # Размещение изображения на холсте
                canvas_LPS_2_1.create_image(0, 0, anchor=tk.NW, image=photo_LPS_2_1)
                # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
                canvas_LPS_2_1.photo = photo_LPS_2_1

            image_data_WEGREQ_2st = [{"file": "laplass_bnd2_st_data.png", "text": "Начальные данные", "position": (300, 500)}]

            for item_5 in image_data_WEGREQ_2st:
                    # Добавление текста на холст
               text_widget_WEGREQ_2st = tk.Label(div_container_1, text=item_5["text"], font=('Arial', 12, 'bold'),
                                                      bg=mainColor)
               text_widget_WEGREQ_2st.pack(anchor='center')  # Используем pack для text_widget_Laplass1

                    # Загрузка изображения
               image_path_WEGREQ_2st = os.path.join("images", item_5["file"])
               image_WEGREQ_2st = Image.open(image_path_WEGREQ_2st)
               photo_WEGREQ_2st = ImageTk.PhotoImage(image_WEGREQ_2st)

                    # Создание холста внутри div-контейнера с размерами изображения и белым фоном
               canvas_WEGREQ_2st = tk.Canvas(div_container_1, width=image_WEGREQ_2st.width,
                                                  height=image_WEGREQ_2st.height, bg=drawingColor,
                                                 bd=1,
                                                  relief='solid')
               canvas_WEGREQ_2st.pack()

               # Размещение изображения на холсте
               canvas_WEGREQ_2st.create_image(0, 0, anchor=tk.NW, image=photo_WEGREQ_2st)
               # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
               canvas_WEGREQ_2st.photo = photo_WEGREQ_2st

                    # Размещение div-контейнера
            div_container_1.place(x=864, y=865, anchor="s")

            # добавление всплывающего виджета с подсказкой

            bubble_container_1 = tk.Frame(self, bg='#ffffff', bd=1, relief='solid')
            bubble_container_1.pack_propagate(False)
            bubble_container_1.config(width=520, height=370)
            etl_title = tk.Label(bubble_container_1, font=('Arial', 11, 'bold'),
                                 text='Вторая краевая задача\n(Задача Неймана)', bg=drawingColor)
            etl_title.place(x=205, y=45, anchor='s')
            extra_text_label_1 = tk.Label(bubble_container_1, justify='left', wraplength=290, bg=drawingColor, text=
            '''
            Параметры a и b задают прямоугольную область, внутри которой предлагается найти такую функцию U(x,y), которая бы удовлетворяла уравнению Лапласа. 
            Вторая краевая задача, также известная как задача Неймана, задает производные (производные по нормали к границе) функции U(x,y) на границе области. 
            Также, будем считать, что U(x,y) - непрерывна на границе области, и значения функций в соответствующих краевых точках равны друг другу.
            ''')
            extra_text_label_1.place(x=220, y=50)

            extra_text_label_2 = tk.Label(bubble_container_1, justify='left', wraplength=400, bg=drawingColor, text=
            '''
            Функция U может описывать множество явлений. Важно, чтобы на границе области задавались фиксированные значения, с помощью заданных краевых функций f (на графике обозначены как t).
            ''')
            extra_text_label_2.place(x=10, y=270)
            extra_image = [
                {"file": "Laplass_bnd_addict.png", "text": "Геометрия области уравнения:", "position": (305, 200)}]

            for item in extra_image:
                # Загрузка изображения
                image_path_1 = os.path.join("images", item["file"])
                image_1 = Image.open(image_path_1)
                photo_1 = ImageTk.PhotoImage(image_1)

                # Создание холста с размерами изображения и drawingColor фоном
                canvas_1 = tk.Canvas(bubble_container_1, width=image_1.width, height=image_1.height, bd=1,
                                     relief='solid')
                canvas_1.place(x=15, y=175, anchor="w")

                # Размещение изображения на холсте
                canvas_1.create_image(0, 0, anchor=tk.NW, image=photo_1)

                # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
                canvas_1.photo = photo_1

                # Добавление текста на холст
                text_widget_1 = tk.Label(bubble_container_1, text=item["text"], font=('Arial', 8, 'bold'),
                                         bg=drawingColor,
                                         fg=textColor)
                text_widget_1.place(x=20, y=50)

            bubble_container_1.pack_forget()

            def on_enter(event):
                bubble_container_1.place(x=864, y=610, anchor='s')

            def on_leave(event):
                bubble_container_1.place_forget()

            div_container_1.bind("<Enter>", on_enter)
            div_container_1.bind("<Leave>", on_leave)

            ###################  ТРЕТЬЯ НАЧАЛЬНО-КРАЕВАЯ ЗАДАЧА ##########################################

            # Создание div-контейнера с белой рамкой
            div_container_2 = tk.Frame(self, bg=mainColor, bd=1, relief='solid')
            div_container_2.pack(pady=500, padx=600, anchor='w')  # Используем pack для div_container
            div_container_2.pack_propagate(False)
            div_container_2.config(width=706, height=250)
            image_data_LPS_3_1 = [{"file": "laplass_bnd3.png", "text": """ТРЕТЬЯ НАЧАЛЬНО-КРАЕВАЯ ЗАДАЧА\n
                                                                                                     \n Краевые условия:""",
                                       "position": (200, 300)}]

            for item_6 in image_data_LPS_3_1:
                # Добавление текста на холст
                text_widget_LPS_3_1 = tk.Label(div_container_2, text=item_6["text"], font=('Arial', 12, 'bold'),
                                                   bg=mainColor, fg=textColor)
                text_widget_LPS_3_1.pack(anchor='center')  # Используем pack для text_widget_Laplass1

                # Загрузка изображения
                image_path_LPS_3_1 = os.path.join("images", item_6["file"])
                image_LPS_3_1 = Image.open(image_path_LPS_3_1)
                photo_LPS_3_1 = ImageTk.PhotoImage(image_LPS_3_1)

                # Создание холста внутри div-контейнера с размерами изображения и белым фоном
                canvas_LPS_3_1 = tk.Canvas(div_container_2, width=image_LPS_3_1.width, height=image_LPS_3_1.height,
                                               bg=drawingColor,
                                               bd=1, relief='solid')
                canvas_LPS_3_1.pack()

                # Размещение изображения на холсте
                canvas_LPS_3_1.create_image(0, 0, anchor=tk.NW, image=photo_LPS_3_1)
                # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
                canvas_LPS_3_1.photo = photo_LPS_3_1

            image_data_WEGREQ_3st = [{"file": "laplass_bnd3_st_data.png", "text": "Начальные данные", "position": (300, 500)}]
            for item_7 in image_data_WEGREQ_3st:
                # Добавление текста на холст
                text_widget_WEGREQ_3st = tk.Label(div_container_2, text=item_7["text"], font=('Arial', 12, 'bold'),
                                                   bg=mainColor)
                text_widget_WEGREQ_3st.pack(anchor='center')  # Используем pack для text_widget_Laplass1

                        # Загрузка изображения
                image_path_WEGREQ_3st = os.path.join("images", item_7["file"])
                image_1_8 = Image.open(image_path_WEGREQ_3st)
                photo_1_8 = ImageTk.PhotoImage(image_1_8)

                # Создание холста внутри div-контейнера с размерами изображения и белым фоном
                canvas_1_8 = tk.Canvas(div_container_2, width=image_1_8.width, height=image_1_8.height,
                                               bg=drawingColor,
                                               bd=1, relief='solid')
                canvas_1_8.pack()

                # Размещение изображения на холсте
                canvas_1_8.create_image(0, 0, anchor=tk.NW, image=photo_1_8)
                # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
                canvas_1_8.photo = photo_1_8

                           # Размещение div-контейнера
            div_container_2.place(x=1870, y=865, anchor="se")

        # добавление всплывающего виджета с подсказкой

        bubble_container_2 = tk.Frame(self, bg='#ffffff', bd=1, relief='solid')
        bubble_container_2.pack_propagate(False)
        bubble_container_2.config(width=690, height=370)
        etl_title = tk.Label(bubble_container_2, font=('Arial', 11, 'bold'),
                             text='Третья краевая задача\n(Задача Робина)', bg=drawingColor)
        etl_title.place(x=205, y=45, anchor='s')
        extra_text_label_1 = tk.Label(bubble_container_2, justify='left', wraplength=420, bg=drawingColor, text=
        '''
        Параметры a и b задают прямоугольную область, внутри которой предлагается найти такую функцию U(x,y), которая бы удовлетворяла уравнению Лапласа. 
        Краевые задачи (на графике) задают комбинацию значений функции U(x,y) и ее нормальной производной на границе области.
        Заметим, что при коэффициентах a, равных нулю - задача сводится к второй начально-краевой (задаче Неймана).
        Также, будем считать, что U(x,y) - непрерывна на границе области, и значения функций в соответствующих краевых точках равны друг другу.
        Обратите внимение: Третья краевая задача объединяет характеристики первой и второй краевых задач.  Она позволяет моделировать более сложные физические явления, учитывая  как значение функции, так и ее производную на границе.
        ''')

        extra_text_label_1.place(x=220, y=50)

        extra_text_label_2 = tk.Label(bubble_container_2, justify='left', wraplength=400, bg=drawingColor, text=
        '''
        Функция U может описывать множество явлений. Важно, чтобы на границе области задавались фиксированные значения, с помощью заданных краевых функций f (на графике обозначены как t).
        ''')
        extra_text_label_2.place(x=10, y=270)
        extra_image = [
            {"file": "Laplass_bnd_addict.png", "text": "Геометрия области уравнения:", "position": (305, 200)}]

        for item in extra_image:
            # Загрузка изображения
            image_path_1 = os.path.join("images", item["file"])
            image_1 = Image.open(image_path_1)
            photo_1 = ImageTk.PhotoImage(image_1)

            # Создание холста с размерами изображения и drawingColor фоном
            canvas_1 = tk.Canvas(bubble_container_2, width=image_1.width, height=image_1.height, bd=1,
                                 relief='solid')
            canvas_1.place(x=15, y=175, anchor="w")

            # Размещение изображения на холсте
            canvas_1.create_image(0, 0, anchor=tk.NW, image=photo_1)

            # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
            canvas_1.photo = photo_1

            # Добавление текста на холст
            text_widget_1 = tk.Label(bubble_container_2, text=item["text"], font=('Arial', 8, 'bold'), bg=drawingColor,
                                     fg=textColor)
            text_widget_1.place(x=20, y=50)
        bubble_container_2.pack_forget()

        def on_enter(event):
            bubble_container_2.place(x=1870, y=610, anchor='se')

        def on_leave(event):
            bubble_container_2.place_forget()

        div_container_2.bind("<Enter>", on_enter)
        div_container_2.bind("<Leave>", on_leave)



if __name__ == "__main__":
    app = EquationForms()
    app.geometry(f'{app.winfo_screenwidth()}x{app.winfo_screenheight()}')
    app.bind('<KeyPress-q>', app.quit_form)
    app.mainloop()
