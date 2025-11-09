from modules.GUI.Natural_GUI import create_NaturalApp
from modules.GUI.Integer_GUI import create_IntegerApp
from modules.GUI.Rational_GUI import create_RationalApp
from modules.GUI.Polynomial_GUI import create_PolynomialApp
import tkinter as tk
from tkinter import font


class App:
    def __init__(self, root):
        # Оранжевая цветовая схема
        self.orange_theme = {
            "bg": "#1A1A1A",  # Темный фон
            "title": "#FF6B35",  # Яркий оранжевый для заголовка
            "subtitle": "#FFB366",  # Светлый оранжевый
            "button_bg": "#FF6B35",  # Оранжевые кнопки
            "button_fg": "#FFFFFF",  # Белый текст
            "button_hover": "#FF8C42",  # Светлее при наведении
            "button_active": "#D45A2A",  # Темнее при нажатии
            "border": "#FF8C42",  # Оранжевая рамка
            "accent": "#FFB366"  # Акцентный цвет
        }

        self.current_theme = self.orange_theme

        # Создание окна
        self.root = root
        self.root.title("Калькулятор модулей")
        self.root.geometry("650x650")
        self.root.configure(bg=self.current_theme["bg"])
        self.root.resizable(False, False)
        
        # Центрируем окно
        self.center_window(650, 650)

        # Создаем стильный заголовок
        header_frame = tk.Frame(root, bg=self.current_theme["bg"])
        header_frame.pack(pady=(30, 20), fill=tk.X)
        
        # Главный заголовок
        title_font = font.Font(family="Segoe UI", size=28, weight="bold")
        self.title_label = tk.Label(header_frame, text="Калькулятор модулей", 
                                     bg=self.current_theme["bg"],
                                     fg=self.current_theme["title"], 
                                     font=title_font)
        self.title_label.pack()
        
        # Подзаголовок
        subtitle_font = font.Font(family="Segoe UI", size=11)
        subtitle_label = tk.Label(header_frame, text="Выберите модуль для работы", 
                                  bg=self.current_theme["bg"],
                                  fg=self.current_theme["subtitle"], 
                                  font=subtitle_font)
        subtitle_label.pack(pady=(5, 0))

        # Основной контейнер для кнопок
        main_container = tk.Frame(root, bg=self.current_theme["bg"])
        main_container.pack(fill=tk.BOTH, expand=True, padx=70, pady=10)
        
        # Контейнер для кнопок (центрируем)
        buttons_frame = tk.Frame(main_container, bg=self.current_theme["bg"])
        buttons_frame.pack(expand=True)

        
        button_font = font.Font(family="Segoe UI", size=13, weight="normal")
        
        
        btn_natural = self.create_button(buttons_frame, "🔢 Натуральные числа", self.run_file1, button_font)
        btn_integer = self.create_button(buttons_frame, "🔷 Целые числа", self.run_file2, button_font)
        btn_rational = self.create_button(buttons_frame, "🔶 Рациональные числа", self.run_file3, button_font)
        btn_polynomial = self.create_button(buttons_frame, "📊 Многочлены", self.run_file4, button_font)
        
        # Добавляем подсказку внизу окна
        footer_frame = tk.Frame(root, bg=self.current_theme["bg"])
        footer_frame.pack(side=tk.BOTTOM, pady=10)
        
        hint_font = font.Font(family="Segoe UI", size=9)
        hint_label = tk.Label(footer_frame, text="Доступно 4 раздела",
                             bg=self.current_theme["bg"],
                             fg=self.current_theme["subtitle"],
                             font=hint_font)
        hint_label.pack()

    def center_window(self, width, height):
        """Центрирует окно на экране"""
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = max(0, (screen_width - width) // 2)
        y = max(0, (screen_height - height) // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def create_button(self, parent, text, command, font_style):
        """Создает стильную кнопку с эффектами"""
        # Фрейм для кнопки с отступами
        button_frame = tk.Frame(parent, bg=self.current_theme["bg"])
        button_frame.pack(pady=8, fill=tk.X, padx=5)
        
        button = tk.Button(button_frame, 
                          text=text,
                          command=command,
                          bg=self.current_theme["button_bg"],
                          fg=self.current_theme["button_fg"],
                          font=font_style,
                          relief=tk.FLAT,
                          bd=0,
                          padx=30,
                          pady=13,
                          cursor="hand2",
                          activebackground=self.current_theme["button_active"],
                          activeforeground=self.current_theme["button_fg"],
                          anchor=tk.CENTER,
                          justify=tk.CENTER)
        
        button.pack(fill=tk.X, ipady=11)
        
        # Эффекты при наведении
        def on_enter(e):
            button.config(bg=self.current_theme["button_hover"])
            button.config(relief=tk.RAISED, bd=2)
        
        def on_leave(e):
            button.config(bg=self.current_theme["button_bg"])
            button.config(relief=tk.FLAT, bd=0)
        
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
        
        return button

    def run_file1(self):
        window = create_NaturalApp(root, 'orange')

    def run_file2(self):
        window = create_IntegerApp(root, 'orange')

    def run_file3(self):
        window = create_RationalApp(root, 'orange')

    def run_file4(self):
        window = create_PolynomialApp(root, 'orange')


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

