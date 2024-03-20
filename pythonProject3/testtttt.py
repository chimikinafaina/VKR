import os
import re
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import numpy as np
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sympy import symbols, lambdify


class PhotoFrame(tk.Frame):
    def __init__(self, parent, image_path, position):
        super().__init__(parent, bd=1, relief='solid', bg='white')
        self.show_image(image_path, position)

    def show_image(self, image_path, position):
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self, image=photo, bg='black')
        label.image = photo
        label.grid(row=0, column=0, pady=0.1, padx=0.1, sticky='w')


class ThreeDivForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.save_resuts = None
        self.fill_entries_and_ploth = None
        self.plot_graph = None
        self.plot_graph = None
        self.canvas_frame = None
        self.canvas_frame_2 = None

        self.configure(bg='#C0D9E6')
        self.title("Явная схема")
        self.geometry("1400x750")
        self.resizable(False, False)
        self.menubar = tk.Menu(self, font=('Arial', 12))
        self.config(menu=self.menubar)
        self.submenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Меню", menu=self.submenu)
        self.submenu.add_separator()
        self.submenu.add_command(label="Выход", command=self.quit)
        self.create_div1()
        self.create_div2()
        self.create_div3()

    def create_div1(self):
        div1 = tk.Frame(self, bg="white", bd=1, relief='solid')
        div1.place(relx=0.01, rely=0.02, relwidth=0.48, relheight=0.6)
        self.title_label_2 = tk.Label(div1, text="Конечно-разностная постановка", font=('Arial', 12, 'bold'),
                                       bg='white')
        self.title_label_2.grid(row=0, column=0, pady=10, padx=30, sticky='w')
        self.title_label_4 = tk.Label(div1, text="Задание расчётной сетки:", font=('Arial', 12, 'bold'), bg='white')
        self.title_label_4.grid(row=1, column=0, pady=5, padx=30, sticky='w')
        self.title_label_5 = tk.Label(div1, text="""N - число интервалов по оси x\nM - число интервалов по оси t""",
                                      font=('Arial', 12, 'bold'), bg='white')
        self.title_label_5.grid(row=3, column=0, pady=12, padx=30, sticky='w')

        # Условие устойчивости
        text_below_title_7 = "Условие устойчивости:"
        self.text_label_7 = tk.Label(div1, text=text_below_title_7, font=('Arial', 12, 'bold'), bg='white', anchor='w')
        self.text_label_7.place(x=440, y=250)  # Установка абсолютных координат для метки

        text_below_title_8 = "Явная схема"
        self.text_label_8 = tk.Label(div1, text=text_below_title_8, font=('Arial', 12, 'bold'), bg='white', anchor='w')
        self.text_label_8.grid(row=4, column=0, pady=195, padx=34, sticky='w')

        self.show_image("images/5_1.png", (455, 142))
        self.show_image("images/5_5.png", (45, 200))
        self.show_image("images/5_6.png", (45, 260))
        self.show_image("images/5_7.png", (45, 320))
        self.show_image("images/5_8.png", (468, 340))
        self.show_image("images/5_3.png", (44, 410))
        self.show_image("images/5_4.png", (490, 420))

    def show_image(self, image_path, position):
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        canvas_1 = tk.Canvas(self, width=image.width, height=image.height, bg='white', bd=1, relief='solid')
        canvas_1.place(x=position[0], y=position[1], anchor="w")
        canvas_1.create_image(0, 0, anchor=tk.NW, image=photo)
        canvas_1.photo = photo

    def create_div2(self):
        div2 = tk.Frame(self, bg="white", bd=1, relief='solid')
        div2.place(relx=0.5, rely=0.021, relwidth=0.49, relheight=0.6)
        label_font = ('Arial', 10, 'bold')
        tk.Label(
            div2, text="Выбор краевых условий и начальных данных", font=label_font, bg="white",
        ).grid(row=0, column=0, pady=(20, 30), padx=(0, 0), sticky='nsew', columnspan=3)

        self.selected_rows = tk.IntVar()
        label_analytical_solution = tk.Label(div2, text="Аналитическое решение:", font=label_font, bg="white")
        label_analytical_solution.grid(row=1, column=0, sticky=tk.W, padx=20, pady=9)

        entry_analytical_solution = tk.Entry(div2,width=20, textvariable=self.selected_rows, font=label_font, bg="white", bd=1,
                                             relief='solid')
        entry_analytical_solution.grid(row=1, column=1, sticky=tk.W, pady=(5, 0), padx=(38, 0))

        tk.Label(div2, text="Интервал по оси x (a):", anchor='ne', font=label_font, bg="white").grid(row=3, column=0,
                                                                                                      sticky=tk.W,
                                                                                                      padx=(20, 0),
                                                                                                      pady=(5, 5))
        self.entry_a = tk.Entry(div2, width=24, bg="white", bd=1, relief='solid')
        self.entry_a.grid(row=3, column=1, pady=(5, 0), padx=(35, 0))
        tk.Label(div2, text=" Коэффициент\nтемпературопроводности (\u03B1) :", anchor='ne', font=label_font,
                 bg="white").grid(row=1, column=2, sticky=tk.W, padx=(65, 0), pady=(0, 5))
        self.entry_k = tk.Spinbox(div2, width=24, bg="white", bd=1, relief='solid', from_=1, to=100, increment=0.1,
                                   format="%10.2f")
        self.entry_k.grid(row=3, column=2, pady=(0, 10), padx=(70, 0))
        tk.Label(div2, text="Интервал по времени (T) :", anchor='ne', font=label_font, bg="white").grid(row=4,
                                                                                                           column=2,
                                                                                                           sticky=tk.W,
                                                                                                           padx=(75, 0),
                                                                                                           pady=(0, 5))
        self.entry_T = tk.Spinbox(div2, width=24, bg="white", bd=1, relief='solid', from_=1, to=100, increment=0.1)
        self.entry_T.grid(row=5, column=2, pady=(0, 12), padx=(65, 0))
        tk.Label(div2, text="Плотность\n теплового потока f(x, t) :", anchor='ne', font=label_font,
                 bg="white").grid(
            row=6, column=2, sticky=tk.W,
            padx=(80, 0), pady=(0, 5))
        self.entry_function = tk.Entry(div2, width=24, bg="white", bd=1, relief='solid')
        self.entry_function.grid(row=7, column=2, pady=(0, 30), padx=(65, 0))
        tk.Label(div2, text="Интервал по оси t (b) :", anchor='ne', font=label_font, bg="white").grid(row=4, column=0,
                                                                                                       sticky=tk.W,
                                                                                                       padx=(20, 0),
                                                                                                       pady=(5, 5))
        self.entry_b = tk.Entry(div2, width=24, bg="white", bd=1, relief='solid')
        self.entry_b.grid(row=4, column=1, pady=(5, 0), padx=(35, 0))
        tk.Label(div2, text=" Начальное условие \u03C8(x) :", anchor='ne', font=label_font, bg="white").grid(row=5,
                                                                                                               column=0,
                                                                                                               sticky=tk.W,
                                                                                                               padx=(16,
                                                                                                                     0),
                                                                                                               pady=(5,
                                                                                                                     5))
        self.entry_phi = tk.Entry(div2, width=24, bg="white", bd=1, relief='solid')
        self.entry_phi.grid(row=5, column=1,  pady=(5, 0), padx=(35, 0))
        tk.Label(div2, text=" Левое\n граничное условие \u03C61 (t) :", anchor='ne', font=label_font,
                 bg="white").grid(
            row=6, column=0, sticky=tk.W, padx=(16, 0), pady=(5, 5))
        self.entry_left = tk.Entry(div2, width=24, bg="white", bd=1, relief='solid')
        self.entry_left.grid(row=6, column=1,  pady=(0, 0), padx=(35, 0))
        tk.Label(div2, text=" Правое\n граничное условие \u03C62 (t) :", anchor='ne', font=label_font,
                 bg="white").grid(
            row=7, column=0, sticky=tk.W, padx=(18, 0), pady=(5, 5))
        self.entry_right = tk.Entry(div2, width=24, bg="white", bd=1, relief='solid')
        self.entry_right.grid(row=7, column=1,  pady=(12, 0), padx=(38, 0), sticky="nw")
        tk.Label(div2, text="Число узлов по оси x (M) :", anchor='ne', font=label_font, bg="white").grid(row=8,
                                                                                                           column=0,
                                                                                                           sticky=tk.W,
                                                                                                           padx=(16,
                                                                                                                 0),
                                                                                                           pady=(5,
                                                                                                                 5))
        self.entry_M = tk.Spinbox(div2, width=23, bg="white", bd=1, relief='solid', from_=1, to=100)
        self.entry_M.grid(row=8, column=1, pady=(5, 0), padx=(35, 0))

        # Метка "Число узлов по оси t (N)"
        label_N_nodes = tk.Label(div2, text="Число узлов по оси t (N) :", anchor='ne', font=label_font, bg="white")
        label_N_nodes.place(relx=0.7, rely=0.65)  # Установка абсолютных координат для метки

        # Текстовое поле для ввода
        self.entry_N = tk.Spinbox(div2, width=24, bg="white", bd=1, relief='solid', from_=1, to=100)
        self.entry_N.place(relx=0.71, rely=0.7)  # Установка абсолютных координат для текстового поля

        buttons = [
            {"text": "Загрузить данные", "command": self.load_file},
            {"text": "Вывести графики ", "command": self.fill_entries_and_plot},
            {"text": "Сохранить результаты ", "command": self. save_resuts}

        ]

        for i, button_info in enumerate(buttons):
            tk.Button(
                div2, text=button_info["text"], command=button_info["command"], bg="#F5F5DC",
                wraplength=80
            ).grid(row=12, column=i, pady=(10, 12), padx=(10, 15), sticky='nsew')

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("LaTeX files", "*.tex")])
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    content = str(content)
                    self.parse_latex_content(content)
            except Exception as e:
                messagebox.showerror("Ошибка", f"Ошибка при чтении файла: {str(e)}")

    def parse_latex_content(self, content):
        lines = content.split('\n')
        for line in lines:
            if 'Интервал по оси x (a):' in line:
                value = re.search(r':\s*([^\\]+)', line).group(1).strip()
                self.entry_a.delete(0, tk.END)
                self.entry_a.insert(0, value)
                self.entry_a.config(state='normal')
            elif 'Интервал по оси t (b):' in line:
                value = re.search(r':\s*([^\\]+)', line).group(1).strip()
                self.entry_b.delete(0, tk.END)
                self.entry_b.insert(0, value)
                self.entry_b.config(state='normal')
            elif 'Начальное условие \\u03C8(x):' in line:
                value = re.search(r':\s*([^\\]+)', line).group(1).strip()
                self.entry_phi.delete(0, tk.END)
                self.entry_phi.insert(0, value)
                self.entry_phi.config(state='normal')
            elif 'Левое\\n граничное условие \\u03C61 (t) :' in line:
                value = re.search(r':\s*([^\\]+)', line).group(1).strip()
                self.entry_left.delete(0, tk.END)
                self.entry_left.insert(0, value)
                self.entry_left.config(state='normal')
            elif 'Правое\\n граничное условие \\u03C62 (t) :' in line:
                value = re.search(r':\s*([^\\]+)', line).group(1).strip()
                self.entry_right.delete(0, tk.END)
                self.entry_right.insert(0, value)
                self.entry_right.config(state='normal')
            elif 'Аналитическое решение: :' in line:
                value = re.search(r':\s*([^\\]+)', line).group(1).strip()
                self.entry_right.delete(0, tk.END)
                self.entry_right.insert(0, value)
                self.entry_right.config(state='normal')


    def print_entries(self):
        print(
            f"Интервал по оси x (a): {self.entry_a.get()}\nИнтервал по оси t (b): {self.entry_b.get()}\nНачальное условие \u03C8(x):{self.entry_phi.get()}"
            f"Левое\n граничное условие \u03C61 (t) :{self.entry_left.get()}\nПравое\n граничное условие \u03C62 (t) :{self.entry_right.get()}")

    def plot_graph_canvas(self, subplot, a, b, phi_expr, left_expr, right_expr, k, T, m, n, function_expr):
        try:
            a = float(self.entry_a.get())
            b = float(self.entry_b.get())
            x, t = symbols('x t')
            phi = self.entry_phi.get()
            phi_func = lambdify(x, phi, modules='numpy')
            k = float(self.entry_k.get())
            T = float(self.entry_T.get())
            m = int(self.entry_M.get())
            n = int(self.entry_N.get())
            dx = (b - a) / m
            dt = T / n
            x_vals = np.linspace(a, b, m + 1)
            t_vals = np.linspace(0, T, n + 1)
            u = np.zeros((n + 1, m + 1))
            u[0, :] = [phi_func(xi) for xi in x_vals]
            f_expr = self.entry_function.get()
            f_func = lambdify((x, t), f_expr, modules='numpy')
            for i in range(0, n):
                for j in range(0, m):
                    try:
                        f_val = f_func(x_vals[j], t_vals[i])
                        if f_val is None:
                            raise ValueError("Функция не может быть вычислена")
                        float(f_val)
                    except Exception as e:
                        messagebox.showerror("Ошибка", f"Ошибка вычисления значения функции: {str(e)}")
                        return
                    u[i + 1, j] = u[i, j] + dt * f_val
            X, T = np.meshgrid(x_vals, t_vals)
            mesh = subplot.plot_surface(X, T, u, cmap='hot')
            subplot.set_xlabel('Пространство (x)')
            subplot.set_ylabel('Время (t)')
            subplot.set_zlabel('Значения функции (u)')
            min_temp = np.min(u)
            max_temp = np.max(u)
            mesh = subplot.plot_surface(X, T, u, cmap='hot', vmin=min_temp, vmax=max_temp)
            cbar = plt.colorbar(mesh, ax=subplot, pad=0.35)  # Добавляем отступ pad=0.1
            cbar.set_label('Значения функции (u)')
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")

    def plot_linear_graph(self, subplot, x, u, _t):
        try:
            # Линейный график
            subplot.plot(x, u[0, :], label='t = 0')
            for j in range(5):  # первые 4 шага по времени
                subplot.plot(x, u[j, :], label=f't = {_t * (j + 1)}')

            subplot.set_xlabel('x')
            subplot.set_ylabel('t')
            subplot.set_title('Распределение температуры')
            subplot.legend()
            subplot.grid(True)
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")

    def create_div3(self):
        self.div3 = tk.Frame(self, bg="white", bd=1, relief='solid')
        self.div3.place(relx=0.01, rely=0.64, relwidth=0.98, relheight=0.35)

        fig = plt.figure(figsize=(14, 6))
        ax1 = fig.add_subplot(121, projection='3d')  # 3D subplot
        self.plot_graph_canvas(ax1, 0, 0, "", "", "", 0, 0, 0, 0, "")

        ax2 = fig.add_subplot(122)  # 2D subplot
        x = np.linspace(0, 10, 100)
        u = np.random.rand(6, 100)
        _t = 0.1
        self.plot_linear_graph(ax2, x, u, _t)

        self.canvas_frame = tk.Frame(self.div3)
        self.canvas_frame.pack(side='top', fill='both', expand=1)
        self.canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side='left', fill='both', expand=1)

    def fill_entries_and_plot(self):
        try:
            a = float(self.entry_a.get())
            b = float(self.entry_b.get())
            phi_expr = self.entry_phi.get()
            left_expr = self.entry_left.get()
            right_expr = self.entry_right.get()
            k = float(self.entry_k.get())
            T = float(self.entry_T.get())
            m = int(self.entry_M.get())
            n = int(self.entry_N.get())
            function_expr = self.entry_function.get()

            # Очистка предыдущего графика, если он был
            if self.canvas_frame is not None:
                self.canvas_frame.destroy()

            # Создание нового графика
            fig = plt.figure(figsize=(14, 6))
            ax1 = fig.add_subplot(121, projection='3d')  # 3D subplot
            ax2 = fig.add_subplot(122)  # 2D subplot

            # Построение графиков
            self.plot_graph_canvas(ax1, a, b, phi_expr, left_expr, right_expr, k, T, m, n, function_expr)
            self.plot_linear_graph(ax2, a, b, phi_expr, left_expr, right_expr, k, T, m, n, function_expr)

            # Создание и настройка Canvas
            self.canvas_frame = tk.Frame(self.div3)
            self.canvas_frame.pack(side='top', fill='both', expand=1)
            self.canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(side='left', fill='both', expand=1)

        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")


if __name__ == "__main__":
    app = ThreeDivForm()
    app.bind('<KeyPress-q>', app.quit)
    app.grid_columnconfigure(0, weight=1)
    app.grid_rowconfigure(0, weight=1)
    app.mainloop()
