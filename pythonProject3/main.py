import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os


class MainForm(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Разработка электронного ресурса для поддержки курса ММПС.")

        self.menubar = tk.Menu(self, font=('Arial', 12))
        self.config(menu=self.menubar)

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=1, fill="both")

        self.form1_tab = Form1Tab(self.notebook)
        self.notebook.add(self.form1_tab, text="Уравнение теплопроводности")

        self.form2_tab = Form2Tab(self.notebook)
        self.notebook.add(self.form2_tab, text="Волновое уравнение")

        self.form3_tab = Form3Tab(self.notebook)
        self.notebook.add(self.form3_tab, text="Уравнение Лапласа")

        self.submenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Постановка задачи", menu=self.submenu)
        self.submenu.add_separator()
        self.submenu.add_command(label="Выход", command=self.quit)

        # Пункт меню "Уравнение теплопроводности"
        file_menu1 = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Уравнение теплопроводности", menu=file_menu1, font=('Arial', 12, 'bold'))
        # file_menu1.add_command(label="Явная схема", command=self.show_explicit_form)
        # file_menu1.add_command(label="Неявная схема", command=self.show_implicit_form)
        # file_menu1.add_command(label="Схема Кранка-Николсона", command=self.show_krank_nikolson_form)

        # Пункт меню "Волновое уравнение"
        file_menu2 = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Волновое уравнение", menu=file_menu2, font=('Arial', 12, 'bold'))

        # Пункт меню "Уравнение Лапласа"
        file_menu3 = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Уравнение Лапласа", menu=file_menu3, font=('Arial', 12, 'bold'))

        # Пункт меню "Методы прогонки"
        file_menu4 = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Методы прогонки", menu=file_menu4, font=('Arial', 12, 'bold'))

    def on_explicit_form_close(self):
        self.deiconify()

    def on_implicit_form_close(self):
        self.deiconify()

    def on_krank_nikolson_form_close(self):
        self.deiconify()

    def quit(self, event=None):
        self.destroy()

    def show_form1(self):
        self.notebook.select(self.form1_tab)

    def show_form2(self):
        self.notebook.select(self.form2_tab)

    def show_form3(self):
        self.notebook.select(self.form3_tab)


class Form1Tab(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(bg='#C0D9E6')

        # Бледно-голубой цвет формы
        self.configure(bg='#C0D9E6')

        # Заголовок формы
        self.title_label = tk.Label(self, text="Постановка задач для уравнений параболического типа",
                                    font=('Arial', 16, 'bold'), bg='#C0D9E6')
        self.title_label.pack(pady=20)

        # Текст под заголовком
        text_below_title = "Уравнение ТЕПЛОПРОВОДНОСТИ или ДИФФУЗИИ в области [ 0, l ] на отрезке времени [ 0, t ]:"
        self.text_label = tk.Label(self, text=text_below_title, font=('Arial', 12, 'bold'), bg='#C0D9E6', anchor='w')
        self.text_label.pack(pady=10, padx=15, anchor='w')

        # Текст под заголовком
        text_below_title_0 = "Геометрия области"
        self.text_label_0 = tk.Label(self, text=text_below_title_0, font=('Arial', 12, 'bold'), bg='#C0D9E6',
                                     anchor='w')
        self.text_label_0.pack(pady=19, padx=55, anchor='w')

        # Список имен файлов изображений и соответствующих текстов
        image_data_1 = [{"file": "1.png", "text": "Общий вид одномерного уравнения:", "position": (305, 180)}]

        for item in image_data_1:
            # Загрузка изображения
            image_path_1 = os.path.join("images", item["file"])
            image_1 = Image.open(image_path_1)
            photo_1 = ImageTk.PhotoImage(image_1)

            # Создание холста с размерами изображения и белым фоном
            canvas_1 = tk.Canvas(self, width=image_1.width, height=image_1.height, bg='white', bd=1, relief='solid')
            canvas_1.place(x=35, y=258, anchor="w")

            # Размещение изображения на холсте
            canvas_1.create_image(0, 0, anchor=tk.NW, image=photo_1)

            # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
            canvas_1.photo = photo_1

            # Добавление текста на холст
            text_widget_1 = tk.Label(self, text=item["text"], font=('Arial', 12, 'bold'), bg='#C0D9E6')
            text_widget_1.place(x=item["position"][0], y=item["position"][1] - text_widget_1.winfo_reqheight() - 20)

            # Список имен файлов изображений и соответствующих текстов
        image_data_2 = [{"file": "1_2.png", "text": """где a - коэффициент теплопроводности(если u - температура) и массопроводности (если u - концентрация,давление в задачах фильтрации и т.п.)
               \nПоскольку в общий вид уравнения входит производная по времени, то необходимо задавать начальные условия при t = 0
                \nи граничные условия при x = 0, x = l, t > 0. """
                            , "position": (300, 425)}]

        for item_1 in image_data_2:
            # Загрузка изображения
            image_path_2 = os.path.join("images", item_1["file"])
            image_2 = Image.open(image_path_2)
            photo_2 = ImageTk.PhotoImage(image_2)

            # Создание холста с размерами изображения и белым фоном
            canvas_2 = tk.Canvas(self, width=image_2.width, height=image_2.height, bg='white', bd=1, relief='solid')
            canvas_2.place(x=300, y=200, anchor="w")

            # Размещение изображения на холсте
            canvas_2.create_image(0, 0, anchor=tk.NW, image=photo_2)

            # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
            canvas_2.photo = photo_2

            # Добавление текста на холст
            text_widget_2 = tk.Label(self, text=item_1["text"], font=('Arial', 12, 'bold'), bg='#C0D9E6',
                                     justify=tk.LEFT)
            text_widget_2.place(x=item_1["position"][0], y=item_1["position"][1] - text_widget_2.winfo_reqheight() - 20,
                                anchor='w')

        ###################  ПЕРВАЯ КРАЕВАЯ ЗАДАЧА ##########################################

        # Создание div-контейнера с белой рамкой
        div_container = tk.Frame(self, bg='#C0D9E6', bd=1, relief='solid')
        div_container.pack(padx=600, pady=800, anchor='w')

        image_data_1_3 = [{"file": "1_3.png", "text": """ПЕРВАЯ КРАЕВАЯ ЗАДАЧА
                                                                             \n Краевые условия:""",
                           "position": (200, 300)}]

        for item_2 in image_data_1_3:
            # Добавление текста на холст
            text_widget_1_3 = tk.Label(div_container, text=item_2["text"], font=('Arial', 12, 'bold'), bg='#C0D9E6')
            text_widget_1_3.pack(anchor='w')  # Используем pack для text_widget_Laplass1

            # Загрузка изображения
            image_path_1_3 = os.path.join("images", item_2["file"])
            image_1_3 = Image.open(image_path_1_3)
            photo_1_3 = ImageTk.PhotoImage(image_1_3)

            # Создание холста внутри div-контейнера с размерами изображения и белым фоном
            canvas_Laplass1 = tk.Canvas(div_container, width=image_1_3.width, height=image_1_3.height, bg='white', bd=1,
                                        relief='solid')
            canvas_Laplass1.pack()

            # Размещение изображения на холсте
            canvas_Laplass1.create_image(0, 0, anchor=tk.NW, image=photo_1_3)
            # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
            canvas_Laplass1.photo = photo_1_3

        photo_1_4 = [{"file": "1_4.png", "text": "Начальные данные", "position": (400, 400)}]

        for item_3 in photo_1_4:
            # Добавление текста на холст
            text_widget_1_4 = tk.Label(div_container, text=item_3["text"], font=('Arial', 12, 'bold'), bg='#C0D9E6')
            text_widget_1_4.pack(anchor='center')  # Используем pack для text_widget_Laplass1

            # Загрузка изображения
            image_path_1_4 = os.path.join("images", item_3["file"])
            image_1_4 = Image.open(image_path_1_4)
            photo_1_4 = ImageTk.PhotoImage(image_1_4)

            # Создание холста внутри div-контейнера с размерами изображения и белым фоном
            canvas_1_4 = tk.Canvas(div_container, width=image_1_4.width, height=image_1_4.height, bg='white', bd=1,
                                   relief='solid')
            canvas_1_4.pack()

            # Размещение изображения на холсте
            canvas_1_4.create_image(0, 0, anchor=tk.NW, image=photo_1_4)
            # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
            canvas_1_4.photo = photo_1_4

            # Размещение div-контейнера
            div_container.place(x=95, y=500, anchor="w")

        ###################  ВТОРАЯ КРАЕВАЯ ЗАДАЧА ##########################################

        # Создание div-контейнера с белой рамкой
        div_container_1 = tk.Frame(self, bg='#C0D9E6', bd=1, relief='solid')
        div_container_1.pack(pady=500, padx=600, anchor='w')  # Используем pack для div_container

        image_data_2_1 = [{"file": "2_1.png", "text": """ВТОРАЯ КРАЕВАЯ ЗАДАЧА
                                                                               \n Краевые условия:""",
                           "position": (200, 300)}]

        for item_4 in image_data_2_1:
            # Добавление текста на холст
            text_widget_2_1 = tk.Label(div_container_1, text=item_4["text"], font=('Arial', 12, 'bold'), bg='#C0D9E6')
            text_widget_2_1.pack(anchor='w')  # Используем pack для text_widget_Laplass1

            # Загрузка изображения
            image_path_2_1 = os.path.join("images", item_4["file"])
            image_2_1 = Image.open(image_path_2_1)
            photo_2_1 = ImageTk.PhotoImage(image_2_1)

            # Создание холста внутри div-контейнера с размерами изображения и белым фоном
            canvas_Laplass2 = tk.Canvas(div_container_1, width=image_2_1.width, height=image_2_1.height, bg='white',
                                        bd=1,
                                        relief='solid')
            canvas_Laplass2.pack()

            # Размещение изображения на холсте
            canvas_Laplass2.create_image(0, 0, anchor=tk.NW, image=photo_2_1)
            # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
            canvas_Laplass2.photo = photo_2_1

        image_data_2_2 = [{"file": "2_2.png", "text": "Начальные данные", "position": (300, 500)}]

        for item_5 in image_data_2_2:
            # Добавление текста на холст
            text_widget_2_2 = tk.Label(div_container_1, text=item_5["text"], font=('Arial', 12, 'bold'), bg='#C0D9E6')
            text_widget_2_2.pack(anchor='center')  # Используем pack для text_widget_Laplass1

            # Загрузка изображения
            image_path_2_2 = os.path.join("images", item_5["file"])
            image_2_2 = Image.open(image_path_2_2)
            photo_2_2 = ImageTk.PhotoImage(image_2_2)

            # Создание холста внутри div-контейнера с размерами изображения и белым фоном
            canvas_WEGREQ_2st = tk.Canvas(div_container_1, width=image_2_2.width, height=image_2_2.height, bg='white',
                                          bd=1,
                                          relief='solid')
            canvas_WEGREQ_2st.pack()

            # Размещение изображения на холсте
            canvas_WEGREQ_2st.create_image(0, 0, anchor=tk.NW, image=photo_2_2)
            # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
            canvas_WEGREQ_2st.photo = photo_2_2

            # Размещение div-контейнера
            div_container_1.place(x=595, y=530, anchor="w")

            ###################  ТРЕТЬЯ КРАЕВАЯ ЗАДАЧА ##########################################

            # Создание div-контейнера с белой рамкой
            div_container_2 = tk.Frame(self, bg='#C0D9E6', bd=1, relief='solid')
            div_container_2.pack(pady=500, padx=600, anchor='w')  # Используем pack для div_container

            image_data_3_1 = [{"file": "3_1.png", "text": """ТРЕТЬЯ КРАЕВАЯ ЗАДАЧА
                                                                                     \n Краевые условия:""",
                               "position": (200, 300)}]

            for item_6 in image_data_3_1:
                # Добавление текста на холст
                text_widget_3_1 = tk.Label(div_container_2, text=item_6["text"], font=('Arial', 12, 'bold'),
                                           bg='#C0D9E6')
                text_widget_3_1.pack(anchor='w')  # Используем pack для text_widget_Laplass1

                # Загрузка изображения
                image_path_3_1 = os.path.join("images", item_6["file"])
                image_3_1 = Image.open(image_path_3_1)
                photo_3_1 = ImageTk.PhotoImage(image_3_1)

                # Создание холста внутри div-контейнера с размерами изображения и белым фоном
                canvas_3_1 = tk.Canvas(div_container_2, width=image_3_1.width, height=image_3_1.height, bg='white',
                                       bd=1, relief='solid')
                canvas_3_1.pack()

                # Размещение изображения на холсте
                canvas_3_1.create_image(0, 0, anchor=tk.NW, image=photo_3_1)
                # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
                canvas_3_1.photo = photo_3_1

            image_data_3_2 = [{"file": "3_2.png", "text": "Начальные данные", "position": (300, 500)}]

            for item_7 in image_data_3_2:
                # Добавление текста на холст
                text_widget_3_2 = tk.Label(div_container_2, text=item_7["text"], font=('Arial', 12, 'bold'),
                                           bg='#C0D9E6')
                text_widget_3_2.pack(anchor='center')  # Используем pack для text_widget_Laplass1

                # Загрузка изображения
                image_path_3_2 = os.path.join("images", item_7["file"])
                image_3_2 = Image.open(image_path_3_2)
                photo_3_2 = ImageTk.PhotoImage(image_3_2)

                # Создание холста внутри div-контейнера с размерами изображения и белым фоном
                canvas_3_2 = tk.Canvas(div_container_2, width=image_3_2.width, height=image_3_2.height, bg='white',
                                       bd=1, relief='solid')
                canvas_3_2.pack()

                # Размещение изображения на холсте
                canvas_3_2.create_image(0, 0, anchor=tk.NW, image=photo_3_2)
                # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
                canvas_3_2.photo = photo_3_2

                # Размещение div-контейнера
                div_container_2.place(x=1100, y=530, anchor="w")


class Form2Tab(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(bg='#C0D9E6')

        # Бледно-голубой цвет формы
        self.configure(bg='#C0D9E6')

        # Заголовок формы
        self.title_label = tk.Label(self, text="Постановка задач для уравнений гиперболического типа",
                                    font=('Arial', 16, 'bold'), bg='#C0D9E6')
        self.title_label.pack(pady=20)

        # Текст под заголовком
        text_below_title = "ВОЛНОВОЕ уравнение в области [ 0, l ] на отрезке времени [ 0, t ]:"
        self.text_label = tk.Label(self, text=text_below_title, font=('Arial', 12, 'bold'), bg='#C0D9E6', anchor='w')
        self.text_label.pack(pady=10, padx=15, anchor='w')

        # Текст под заголовком
        text_below_title_0 = "Геометрия области"
        self.text_label_0 = tk.Label(self, text=text_below_title_0, font=('Arial', 12, 'bold'), bg='#C0D9E6',
                                     anchor='w')
        self.text_label_0.pack(pady=19, padx=55, anchor='w')

        # Список имен файлов изображений и соответствующих текстов
        image_data_1 = [{"file": "1.png", "text": "Общий вид одномерного уравнения:", "position": (305, 180)}]

        for item in image_data_1:
            # Загрузка изображения
            image_path_1 = os.path.join("images", item["file"])
            image_1 = Image.open(image_path_1)
            photo_1 = ImageTk.PhotoImage(image_1)

            # Создание холста с размерами изображения и белым фоном
            canvas_1 = tk.Canvas(self, width=image_1.width, height=image_1.height, bg='white', bd=1, relief='solid')
            canvas_1.place(x=35, y=258, anchor="w")

            # Размещение изображения на холсте
            canvas_1.create_image(0, 0, anchor=tk.NW, image=photo_1)

            # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
            canvas_1.photo = photo_1

            # Добавление текста на холст
            text_widget_1 = tk.Label(self, text=item["text"], font=('Arial', 12, 'bold'), bg='#C0D9E6')
            text_widget_1.place(x=item["position"][0], y=item["position"][1] - text_widget_1.winfo_reqheight() - 20)

            # Список имен файлов изображений и соответствующих текстов
        image_data_2 = [{"file": "wave_equation_general_both.png", "text": """где a - скорость распространения малых возмущений в материале, из которого изготовлена струна, и
               \nu(x,t) - поперечные перемещения струны.
                \nГраничные условия при x = 0, x = l, t > 0. """
                            , "position": (300, 425)}]

        for item_1 in image_data_2:
            # Загрузка изображения
            image_path_2 = os.path.join("images", item_1["file"])
            image_2 = Image.open(image_path_2)
            photo_2 = ImageTk.PhotoImage(image_2)

            # Создание холста с размерами изображения и белым фоном
            canvas_2 = tk.Canvas(self, width=image_2.width, height=image_2.height, bg='white', bd=1, relief='solid')
            canvas_2.place(x=300, y=200, anchor="w")

            # Размещение изображения на холсте
            canvas_2.create_image(0, 0, anchor=tk.NW, image=photo_2)

            # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
            canvas_2.photo = photo_2

            # Добавление текста на холст
            text_widget_2 = tk.Label(self, text=item_1["text"], font=('Arial', 12, 'bold'), bg='#C0D9E6',
                                     justify=tk.LEFT)
            text_widget_2.place(x=item_1["position"][0], y=item_1["position"][1] - text_widget_2.winfo_reqheight() - 20,
                                anchor='w')

            ###################  ПЕРВАЯ НАЧАЛЬНО-КРАЕВАЯ ЗАДАЧА ##########################################

            # Создание div-контейнера с белой рамкой
            div_container = tk.Frame(self, bg='#C0D9E6', bd=1, relief='solid')
            div_container.pack(padx=600, pady=800, anchor='w')

            Image_data_WEG_1_1 = [{"file": "WEG_1_1.png", "text": """ПЕРВАЯ НАЧАЛЬНО-КРАЕВАЯ ЗАДАЧА
                                                                                        \n Краевые условия:""",
                                   "position": (200, 300)}]

            for item_2 in Image_data_WEG_1_1:
                # Добавление текста на холст
                text_widget_WEG_1_1 = tk.Label(div_container, text=item_2["text"], font=('Arial', 12, 'bold'),
                                               bg='#C0D9E6')
                text_widget_WEG_1_1.pack(anchor='w')  # Используем pack для text_widget_Laplass1

                # Загрузка изображения
                Image_path_WEG_1_1 = os.path.join("images", item_2["file"])
                Image_WEG_1_1 = Image.open(Image_path_WEG_1_1)
                photo_WEG_1_1 = ImageTk.PhotoImage(Image_WEG_1_1)

                # Создание холста внутри div-контейнера с размерами изображения и белым фоном
                canvas_WEG_1_1 = tk.Canvas(div_container, width=Image_WEG_1_1.width, height=Image_WEG_1_1.height,
                                           bg='white', bd=1,
                                           relief='solid')
                canvas_WEG_1_1.pack()

                # Размещение изображения на холсте
                canvas_WEG_1_1.create_image(0, 0, anchor=tk.NW, image=photo_WEG_1_1)
                # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
                canvas_WEG_1_1.photo = photo_WEG_1_1

            photo_WEG_1_2 = [{"file": "WEG_1_2.png", "text": "Начальные данные", "position": (400, 400)}]

            for item_3 in photo_WEG_1_2:
                # Добавление текста на холст
                text_widget_WEG_1_2 = tk.Label(div_container, text=item_3["text"], font=('Arial', 12, 'bold'),
                                               bg='#C0D9E6')
                text_widget_WEG_1_2.pack(anchor='center')  # Используем pack для text_widget_Laplass1

                # Загрузка изображения
                image_path_WEG_1_2 = os.path.join("images", item_3["file"])
                image_WEG_1_2 = Image.open(image_path_WEG_1_2)
                photo_WEG_1_2 = ImageTk.PhotoImage(image_WEG_1_2)

                # Создание холста внутри div-контейнера с размерами изображения и белым фоном
                canvas_WEGREQ1st = tk.Canvas(div_container, width=image_WEG_1_2.width, height=image_WEG_1_2.height,
                                             bg='white', bd=1,
                                             relief='solid')
                canvas_WEGREQ1st.pack()

                # Размещение изображения на холсте
                canvas_WEGREQ1st.create_image(0, 0, anchor=tk.NW, image=photo_WEG_1_2)
                # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
                canvas_WEGREQ1st.photo = photo_WEG_1_2

                # Размещение div-контейнера
                div_container.place(x=95, y=500, anchor="w")

                ###################  ВТОРАЯ НАЧАЛЬНО-КРАЕВАЯ ЗАДАЧА ##########################################

                # Создание div-контейнера с белой рамкой
                div_container_1 = tk.Frame(self, bg='#C0D9E6', bd=1, relief='solid')
                div_container_1.pack(pady=500, padx=600, anchor='w')  # Используем pack для div_container

                image_data_WEG_2_1 = [{"file": "WEG_2_1.png", "text": """ВТОРАЯ КРАЕВАЯ ЗАДАЧА
                                                                                               \n Краевые условия:""",
                                       "position": (200, 300)}]

                for item_4 in image_data_WEG_2_1:
                    # Добавление текста на холст
                    text_widget_WEG_2_1 = tk.Label(div_container_1, text=item_4["text"], font=('Arial', 12, 'bold'),
                                                   bg='#C0D9E6')
                    text_widget_WEG_2_1.pack(anchor='w')  # Используем pack для text_widget_Laplass1

                    # Загрузка изображения
                    image_path_WEG_2_1 = os.path.join("images", item_4["file"])
                    image_WEG_2_1 = Image.open(image_path_WEG_2_1)
                    photo_WEG_2_1 = ImageTk.PhotoImage(image_WEG_2_1)

                    # Создание холста внутри div-контейнера с размерами изображения и белым фоном
                    canvas_Laplass2 = tk.Canvas(div_container_1, width=image_WEG_2_1.width, height=image_WEG_2_1.height,
                                                bg='white',
                                                bd=1,
                                                relief='solid')
                    canvas_Laplass2.pack()

                    # Размещение изображения на холсте
                    canvas_Laplass2.create_image(0, 0, anchor=tk.NW, image=photo_WEG_2_1)
                    # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
                    canvas_Laplass2.photo = photo_WEG_2_1

                image_data_WEGREQ_2st = [{"file": "WEG_2_2.png", "text": "Начальные данные", "position": (300, 500)}]

                for item_5 in image_data_WEGREQ_2st:
                    # Добавление текста на холст
                    text_widget_WEGREQ_2st = tk.Label(div_container_1, text=item_5["text"], font=('Arial', 12, 'bold'),
                                                      bg='#C0D9E6')
                    text_widget_WEGREQ_2st.pack(anchor='center')  # Используем pack для text_widget_Laplass1

                    # Загрузка изображения
                    image_path_WEGREQ_2st = os.path.join("images", item_5["file"])
                    image_WEGREQ_2st = Image.open(image_path_WEGREQ_2st)
                    photo_WEGREQ_2st = ImageTk.PhotoImage(image_WEGREQ_2st)

                    # Создание холста внутри div-контейнера с размерами изображения и белым фоном
                    canvas_WEGREQ_2st = tk.Canvas(div_container_1, width=image_WEGREQ_2st.width,
                                                  height=image_WEGREQ_2st.height, bg='white',
                                                  bd=1,
                                                  relief='solid')
                    canvas_WEGREQ_2st.pack()

                    # Размещение изображения на холсте
                    canvas_WEGREQ_2st.create_image(0, 0, anchor=tk.NW, image=photo_WEGREQ_2st)
                    # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
                    canvas_WEGREQ_2st.photo = photo_WEGREQ_2st

                    # Размещение div-контейнера
                    div_container_1.place(x=595, y=530, anchor="w")

                    ###################  ТРЕТЬЯ НАЧАЛЬНО-КРАЕВАЯ ЗАДАЧА ##########################################

                    # Создание div-контейнера с белой рамкой
                    div_container_2 = tk.Frame(self, bg='#C0D9E6', bd=1, relief='solid')
                    div_container_2.pack(pady=500, padx=600, anchor='w')  # Используем pack для div_container

                    image_data_WEG_3_1 = [{"file": "WEG_3_1.png", "text": """ТРЕТЬЯ НАЧАЛЬНО-КРАЕВАЯ ЗАДАЧА
                                                                                                     \n Краевые условия:""",
                                           "position": (200, 300)}]

                    for item_6 in image_data_WEG_3_1:
                        # Добавление текста на холст
                        image_data_WEG_3_1 = tk.Label(div_container_2, text=item_6["text"], font=('Arial', 12, 'bold'),
                                                      bg='#C0D9E6')
                        image_data_WEG_3_1.pack(anchor='w')  # Используем pack для text_widget_Laplass1

                        # Загрузка изображения
                        image_path_WEG_3_1 = os.path.join("images", item_6["file"])
                        image_WEG_3_1 = Image.open(image_path_WEG_3_1)
                        photo_WEG_3_1 = ImageTk.PhotoImage(image_WEG_3_1)

                        # Создание холста внутри div-контейнера с размерами изображения и белым фоном
                        canvas_WEG_3_1 = tk.Canvas(div_container_2, width=image_WEG_3_1.width,
                                                   height=image_WEG_3_1.height,
                                                   bg='white',
                                                   bd=1, relief='solid')
                        canvas_WEG_3_1.pack()

                        # Размещение изображения на холсте
                        canvas_WEG_3_1.create_image(0, 0, anchor=tk.NW, image=photo_WEG_3_1)
                        # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
                        canvas_WEG_3_1.photo = photo_WEG_3_1

                    image_data_WEG_3_2 = [{"file": "WEG_3_2.png", "text": "Начальные данные", "position": (300, 500)}]
                    for item_7 in image_data_WEG_3_2:
                        # Добавление текста на холст
                        text_widget_WEG_3_2 = tk.Label(div_container_2, text=item_7["text"], font=('Arial', 12, 'bold'),
                                                       bg='#C0D9E6')
                        text_widget_WEG_3_2.pack(anchor='center')  # Используем pack для text_widget_Laplass1

                        # Загрузка изображения
                        image_path_WEG_3_2 = os.path.join("images", item_7["file"])
                        image_WEG_3_2 = Image.open(image_path_WEG_3_2)
                        photo_WEG_3_2 = ImageTk.PhotoImage(image_WEG_3_2)

                        # Создание холста внутри div-контейнера с размерами изображения и белым фоном
                        canvas_WEG_3_2 = tk.Canvas(div_container_2, width=image_WEG_3_2.width,
                                                   height=image_WEG_3_2.height,
                                                   bg='white',
                                                   bd=1, relief='solid')
                        canvas_WEG_3_2.pack()

                        # Размещение изображения на холсте
                        canvas_WEG_3_2.create_image(0, 0, anchor=tk.NW, image=photo_WEG_3_2)
                        # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
                        canvas_WEG_3_2.photo = photo_WEG_3_2

                        # Размещение div-контейнера
                        div_container_2.place(x=1100, y=530, anchor="w")


class Form3Tab(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Бледно-голубой цвет формы
        self.configure(bg='#C0D9E6')

        # Заголовок формы
        self.title_label = tk.Label(self, text="Постановка задач для уравнений эллиптического типа",
                                    font=('Arial', 16, 'bold'), bg='#C0D9E6')
        self.title_label.pack(pady=20)

        ## Текст под заголовком
        # text_below_title = "ВОЛНОВОЕ уравнение в области [ 0, l ] на отрезке времени [ 0, t ]:"
        # self.text_label = tk.Label(self, text=text_below_title, font=('Arial', 12, 'bold'), bg='#C0D9E6', anchor='w')
        # self.text_label.pack(pady=10, padx=15, anchor='w')

        # Текст под заголовком
        text_below_title_0 = "Геометрия области"
        self.text_label_0 = tk.Label(self, text=text_below_title_0, font=('Arial', 12, 'bold'), bg='#C0D9E6',
                                     anchor='w')
        self.text_label_0.pack(pady=19, padx=55, anchor='w')

        # Список имен файлов изображений и соответствующих текстов
        image_data_1 = [{"file": "1.png", "text": "Общий вид одномерного уравнения:", "position": (305, 180)}]

        for item in image_data_1:
            # Загрузка изображения
            image_path_1 = os.path.join("images", item["file"])
            image_1 = Image.open(image_path_1)
            photo_1 = ImageTk.PhotoImage(image_1)

            # Создание холста с размерами изображения и белым фоном
            canvas_1 = tk.Canvas(self, width=image_1.width, height=image_1.height, bg='white', bd=1, relief='solid')
            canvas_1.place(x=35, y=258, anchor="w")

            # Размещение изображения на холсте
            canvas_1.create_image(0, 0, anchor=tk.NW, image=photo_1)

            # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
            canvas_1.photo = photo_1

            # Добавление текста на холст
            text_widget_1 = tk.Label(self, text=item["text"], font=('Arial', 12, 'bold'), bg='#C0D9E6')
            text_widget_1.place(x=item["position"][0], y=item["position"][1] - text_widget_1.winfo_reqheight() - 20)

            # Список имен файлов изображений и соответствующих текстов
        image_data_2 = [{"file": "LPS_0.png", "text": """где u(x,y) - может быть стационарным (не зависящим от времени) распределением температуры, 
                    \nскоростью потенциального (безвихревого) течения идеальной жидкости, распределение напряжённости электрического и магнитного полей и т.д."""
                            , "position": (300, 425)}]

        for item_1 in image_data_2:
            # Загрузка изображения
            image_path_2 = os.path.join("images", item_1["file"])
            image_2 = Image.open(image_path_2)
            photo_2 = ImageTk.PhotoImage(image_2)

            # Создание холста с размерами изображения и белым фоном
            canvas_2 = tk.Canvas(self, width=image_2.width, height=image_2.height, bg='white', bd=1, relief='solid')
            canvas_2.place(x=300, y=200, anchor="w")

            # Размещение изображения на холсте
            canvas_2.create_image(0, 0, anchor=tk.NW, image=photo_2)

            # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
            canvas_2.photo = photo_2

            # Добавление текста на холст
            text_widget_2 = tk.Label(self, text=item_1["text"], font=('Arial', 12, 'bold'), bg='#C0D9E6',
                                     justify=tk.LEFT)
            text_widget_2.place(x=item_1["position"][0], y=item_1["position"][1] - text_widget_2.winfo_reqheight() - 20,
                                anchor='w')

            ###################  ПЕРВАЯ НАЧАЛЬНО-КРАЕВАЯ ЗАДАЧА ##########################################

            # Создание div-контейнера с белой рамкой
            div_container = tk.Frame(self, bg='#C0D9E6', bd=1, relief='solid')
            div_container.pack(padx=600, pady=800, anchor='w')

            Image_data_LPS_1_1 = [{"file": "LPS_1_1.png", "text": """ПЕРВАЯ НАЧАЛЬНО-КРАЕВАЯ ЗАДАЧА (задача дирихле)
                                                                                                \n Краевые условия:""",
                                   "position": (200, 300)}]

            for item_2 in Image_data_LPS_1_1:
                # Добавление текста на холст
                text_widget_LPS_1_1 = tk.Label(div_container, text=item_2["text"], font=('Arial', 12, 'bold'),
                                               bg='#C0D9E6')
                text_widget_LPS_1_1.pack(anchor='w')  # Используем pack для text_widget_Laplass1

                # Загрузка изображения
                Image_path_LPS_1_1 = os.path.join("images", item_2["file"])
                Image_LPS_1_1 = Image.open(Image_path_LPS_1_1)
                photo_LPS_1_1 = ImageTk.PhotoImage(Image_LPS_1_1)

                # Создание холста внутри div-контейнера с размерами изображения и белым фоном
                canvas_LPS_1_1 = tk.Canvas(div_container, width=Image_LPS_1_1.width, height=Image_LPS_1_1.height,
                                           bg='white',
                                           bd=1,
                                           relief='solid')
                canvas_LPS_1_1.pack()

                # Размещение изображения на холсте
                canvas_LPS_1_1.create_image(0, 0, anchor=tk.NW, image=photo_LPS_1_1)
                # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
                canvas_LPS_1_1.photo = photo_LPS_1_1

                # photo_WEGREQ1st = [{"file": "WEG_1_2.png", "text": "Начальные данные", "position": (400, 400)}]

                # for item_3 in photo_WEGREQ1st:
                #   # Добавление текста на холст
                #   text_widget_1_4 = tk.Label(div_container, text=item_3["text"], font=('Arial', 12, 'bold'), bg='#C0D9E6')
                #   text_widget_1_4.pack(anchor='center')  # Используем pack для text_widget_Laplass1

                #  # Загрузка изображения
                #  image_path_WEGREQ1st = os.path.join("images", item_3["file"])
                #  image_WEGREQ1st = Image.open(image_path_WEGREQ1st)
                #  photo_WEGREQ1st = ImageTk.PhotoImage(image_WEGREQ1st)

                # Создание холста внутри div-контейнера с размерами изображения и белым фоном
                # canvas_WEGREQ1st = tk.Canvas(div_container, width=image_WEGREQ1st.width, height=image_WEGREQ1st.height,
                #                              bg='white', bd=1,
                #                              relief='solid')
                #    canvas_WEGREQ1st.pack()

                # Размещение изображения на холсте
                #    canvas_WEGREQ1st.create_image(0, 0, anchor=tk.NW, image=photo_WEGREQ1st)
                # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
                #    canvas_WEGREQ1st.photo = photo_WEGREQ1st

                # Размещение div-контейнера
                div_container.place(x=95, y=500, anchor="w")

                ###################  ВТОРАЯ НАЧАЛЬНО-КРАЕВАЯ ЗАДАЧА ##########################################

                # Создание div-контейнера с белой рамкой
                div_container_1 = tk.Frame(self, bg='#C0D9E6', bd=1, relief='solid')
                div_container_1.pack(pady=500, padx=600, anchor='w')  # Используем pack для div_container

                image_data_LPS_2_1 = [{"file": "LPS_2_1.png", "text": """ВТОРАЯ КРАЕВАЯ ЗАДАЧА
                                                                                                       \n Краевые условия:""",
                                       "position": (200, 300)}]

                for item_4 in image_data_LPS_2_1:
                    # Добавление текста на холст
                    text_widget_LPS_2_1 = tk.Label(div_container_1, text=item_4["text"], font=('Arial', 12, 'bold'),
                                                   bg='#C0D9E6')
                    text_widget_LPS_2_1.pack(anchor='w')  # Используем pack для text_widget_Laplass1

                    # Загрузка изображения
                    image_path_LPS_2_1 = os.path.join("images", item_4["file"])
                    image_LPS_2_1 = Image.open(image_path_LPS_2_1)
                    photo_LPS_2_1 = ImageTk.PhotoImage(image_LPS_2_1)

                    # Создание холста внутри div-контейнера с размерами изображения и белым фоном
                    canvas_LPS_2_1 = tk.Canvas(div_container_1, width=image_LPS_2_1.width, height=image_LPS_2_1.height,
                                               bg='white',
                                               bd=1,
                                               relief='solid')
                    canvas_LPS_2_1.pack()

                    # Размещение изображения на холсте
                    canvas_LPS_2_1.create_image(0, 0, anchor=tk.NW, image=photo_LPS_2_1)
                    # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
                    canvas_LPS_2_1.photo = photo_LPS_2_1

                    #    image_data_WEGREQ_2st = [{"file": "WEG_2_2.png", "text": "Начальные данные", "position": (300, 500)}]

                    #    for item_5 in image_data_WEGREQ_2st:
                    # Добавление текста на холст
                    #         text_widget_WEGREQ_2st = tk.Label(div_container_1, text=item_5["text"], font=('Arial', 12, 'bold'),
                    #                                           bg='#C0D9E6')
                    #         text_widget_WEGREQ_2st.pack(anchor='center')  # Используем pack для text_widget_Laplass1

                    # Загрузка изображения
                    #         image_path_WEGREQ_2st = os.path.join("images", item_5["file"])
                    #         image_WEGREQ_2st = Image.open(image_path_WEGREQ_2st)
                    #         photo_WEGREQ_2st = ImageTk.PhotoImage(image_WEGREQ_2st)

                    #         # Создание холста внутри div-контейнера с размерами изображения и белым фоном
                    #         canvas_WEGREQ_2st = tk.Canvas(div_container_1, width=image_WEGREQ_2st.width,
                    #                                       height=image_WEGREQ_2st.height, bg='white',
                    #                                      bd=1,
                    #                                       relief='solid')
                    #         canvas_WEGREQ_2st.pack()

                    #         # Размещение изображения на холсте
                    #         canvas_WEGREQ_2st.create_image(0, 0, anchor=tk.NW, image=photo_WEGREQ_2st)
                    #         # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
                    #         canvas_WEGREQ_2st.photo = photo_WEGREQ_2st

                    # Размещение div-контейнера
                    div_container_1.place(x=595, y=530, anchor="w")
                    ###################  ТРЕТЬЯ НАЧАЛЬНО-КРАЕВАЯ ЗАДАЧА ##########################################

                    # Создание div-контейнера с белой рамкой
                    div_container_2 = tk.Frame(self, bg='#C0D9E6', bd=1, relief='solid')
                    div_container_2.pack(pady=500, padx=600, anchor='w')  # Используем pack для div_container

                    image_data_LPS_3_1 = [{"file": "LPS_3_1.png", "text": """ТРЕТЬЯ НАЧАЛЬНО-КРАЕВАЯ ЗАДАЧА
                                                                                                     \n Краевые условия:""",
                                           "position": (200, 300)}]

                    for item_6 in image_data_LPS_3_1:
                        # Добавление текста на холст
                        text_widget_LPS_3_1 = tk.Label(div_container_2, text=item_6["text"], font=('Arial', 12, 'bold'),
                                                       bg='#C0D9E6')
                        text_widget_LPS_3_1.pack(anchor='w')  # Используем pack для text_widget_Laplass1

                        # Загрузка изображения
                        image_path_LPS_3_1 = os.path.join("images", item_6["file"])
                        image_LPS_3_1 = Image.open(image_path_LPS_3_1)
                        photo_LPS_3_1 = ImageTk.PhotoImage(image_LPS_3_1)

                        # Создание холста внутри div-контейнера с размерами изображения и белым фоном
                        canvas_LPS_3_1 = tk.Canvas(div_container_2, width=image_LPS_3_1.width,
                                                   height=image_LPS_3_1.height,
                                                   bg='white',
                                                   bd=1, relief='solid')
                        canvas_LPS_3_1.pack()

                        # Размещение изображения на холсте
                        canvas_LPS_3_1.create_image(0, 0, anchor=tk.NW, image=photo_LPS_3_1)
                        # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
                        canvas_LPS_3_1.photo = photo_LPS_3_1

                    #    image_data_WEGREQ_3st = [{"file": "WEG_3_2.png", "text": "Начальные данные", "position": (300, 500)}]
                    #    for item_7 in image_data_WEGREQ_3st:
                    #        # Добавление текста на холст
                    #        text_widget_WEGREQ_3st = tk.Label(div_container_2, text=item_7["text"], font=('Arial', 12, 'bold'),
                    #                                   bg='#C0D9E6')
                    #        text_widget_WEGREQ_3st.pack(anchor='center')  # Используем pack для text_widget_Laplass1

                    # Загрузка изображения
                    #        image_path_WEGREQ_3st = os.path.join("images", item_7["file"])
                    #        image_1_8 = Image.open(image_path_WEGREQ_3st)
                    #        photo_1_8 = ImageTk.PhotoImage(image_1_8)

                    #        # Создание холста внутри div-контейнера с размерами изображения и белым фоном
                    #        canvas_1_8 = tk.Canvas(div_container_2, width=image_1_8.width, height=image_1_8.height,
                    #                               bg='white',
                    #                               bd=1, relief='solid')
                    #        canvas_1_8.pack()

                    #        # Размещение изображения на холсте
                    #        canvas_1_8.create_image(0, 0, anchor=tk.NW, image=photo_1_8)
                    #        # Сохранение ссылки на объект PhotoImage, чтобы избежать удаления
                    #        canvas_1_8.photo = photo_1_8

                    # Размещение div-контейнера
                    div_container_2.place(x=1100, y=530, anchor="w")


if __name__ == "__main__":
    app = MainForm()
    app.geometry(f'{app.winfo_screenwidth()}x{app.winfo_screenheight()}')  # Открытие на весь экран
    app.bind('<KeyPress-q>', app.quit)
    app.mainloop()
