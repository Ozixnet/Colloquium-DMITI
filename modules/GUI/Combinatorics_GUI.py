import tkinter as tk
from tkinter import messagebox
from modules.С.C_NUM import Permutation
from modules.С.COMPOSE_PP_P import COMPOSE_PP_P_f
from modules.С.INVERSE_P_P import INVERSE_P_P_f
from modules.С.TO_CYCLES_P_L import TO_CYCLES_P_L_f
from modules.С.SIGN_P_I import SIGN_P_I_f
from modules.С.ORDER_P_N import ORDER_P_N_f


def parse_permutation(perm_str):
    """Парсит строку в Permutation. Формат: 1,2,3,4 или [1,2,3,4]"""
    perm_str = perm_str.strip()
    if not perm_str:
        raise ValueError("Пустая строка")
    
    # Убираем скобки если есть
    perm_str = perm_str.replace('[', '').replace(']', '').replace('(', '').replace(')', '')
    
    # Разделяем по запятой или пробелу
    if ',' in perm_str:
        parts = perm_str.split(',')
    else:
        parts = perm_str.split()
    
    # Преобразуем в числа
    try:
        mapping = [int(p.strip()) for p in parts if p.strip()]
    except ValueError:
        raise ValueError("Некорректный формат перестановки")
    
    return Permutation(mapping)


def permutation_to_string(perm):
    """Преобразует Permutation в строку"""
    return '[' + ', '.join(map(str, perm.as_list())) + ']'


def cycles_to_string(cycles):
    """Преобразует список циклов в строку"""
    if not cycles:
        return "id (тождественная перестановка)"
    result = []
    for cycle in cycles:
        result.append('(' + ' '.join(map(str, cycle)) + ')')
    return ' '.join(result)


class CombinatoricsApp:
    def __init__(self, root, theme='orange'):
        # Оранжевая цветовая схема
        self.bg_color = "#1A1A1A"
        self.window_color = "#2D2D2D"
        self.text_color = "#FFFFFF"
        self.backlight = "#FF6B35"
        self.label_color = "#FFB366"
        self.hover_color = "#FF8C42"
        self.button_color = "#FF6B35"
        self.button_active = "#D45A2A"
        self.entry_bg = "#2D2D2D"
        self.entry_fg = "#FFFFFF"
        self.entry_border = "#FF6B35"
        
        self.root = root
        self.root.title("Операции с перестановками")
        self.root.geometry("450x650")
        self.root.configure(bg=self.bg_color)
        self.center_window(450, 650)

        self.method_var = tk.StringVar(value="Композиция перестановок")

        # Заголовок
        from tkinter import font
        title_font = font.Font(family="Segoe GUI", size=20, weight="bold")
        title_label = tk.Label(root, text="Операции с перестановками", 
                              bg=self.bg_color, fg=self.backlight, font=title_font)
        title_label.pack(pady=(20, 15))

        # Выбор метода
        methods = [
            "Композиция перестановок",
            "Обратная перестановка",
            "Разложение на циклы",
            "Знак перестановки",
            "Порядок перестановки"
        ]

        method_frame = tk.Frame(root, bg=self.bg_color)
        method_frame.pack(pady=15, padx=20, fill=tk.X)

        label_font = font.Font(family="Segoe GUI", size=11)
        tk.Label(method_frame, text="Операция: ", bg=self.bg_color, fg=self.label_color, font=label_font).pack(side=tk.LEFT, padx=(0, 10))

        self.method_menu = tk.OptionMenu(method_frame, self.method_var, *methods, command=self.on_option_change)
        self.method_menu.config(bg=self.window_color, fg=self.text_color, 
                                highlightbackground=self.button_color,
                                relief=tk.FLAT, activebackground=self.button_color,
                                activeforeground=self.text_color,
                                highlightthickness=2, font=label_font, bd=0)
        self.method_menu.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.method_menu.bind("<Enter>", lambda e: self.method_menu.config(bg=self.hover_color))
        self.method_menu.bind("<Leave>", lambda e: self.method_menu.config(bg=self.window_color))

        # Контейнер для полей ввода
        input_frame = tk.Frame(root, bg=self.bg_color)
        input_frame.pack(pady=15, padx=20, fill=tk.BOTH, expand=False)

        # Ввод первой перестановки
        input_font = font.Font(family="Segoe GUI", size=10)
        self.first_perm_label = tk.Label(input_frame, text="Первая перестановка (например: 2,1,3):", 
                                         bg=self.bg_color, fg=self.label_color, font=input_font)
        self.first_perm_label.pack(anchor=tk.W, pady=(0, 5))
        self.first_perm_entry = tk.Entry(input_frame, bg=self.entry_bg, fg=self.entry_fg, 
                                         insertbackground='white', 
                                         font=font.Font(family="Segoe GUI", size=12),
                                         relief=tk.FLAT, bd=2, highlightthickness=1,
                                         highlightbackground=self.entry_border,
                                         highlightcolor=self.backlight)
        self.first_perm_entry.pack(fill=tk.X, pady=(0, 15), ipady=8)

        # Ввод второй перестановки
        self.second_perm_label = tk.Label(input_frame, text="Вторая перестановка (например: 3,2,1):", 
                                          bg=self.bg_color, fg=self.text_color, font=input_font)
        self.second_perm_label.pack(anchor=tk.W, pady=(0, 5))
        self.second_perm_entry = tk.Entry(input_frame, bg=self.entry_bg, fg=self.entry_fg, 
                                          insertbackground='white', 
                                          font=font.Font(family="Segoe GUI", size=12),
                                          relief=tk.FLAT, bd=2, highlightthickness=1,
                                          highlightbackground=self.entry_border,
                                          highlightcolor=self.backlight)
        self.second_perm_entry.pack(fill=tk.X, pady=(0, 15), ipady=8)

        # Фрейм для результата с прокруткой
        result_frame = tk.Frame(input_frame, bg=self.bg_color)
        result_frame.pack(pady=10, fill=tk.BOTH, expand=False)

        # Скроллбар
        result_scrollbar = tk.Scrollbar(result_frame, bg=self.window_color, troughcolor=self.bg_color)
        result_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Text виджет вместо Label
        result_font = font.Font(family="Segoe GUI", size=13, weight="bold")
        self.result_text = tk.Text(result_frame, bg=self.entry_bg, fg=self.backlight,
                                   font=result_font, wrap=tk.WORD,
                                   height=5, relief=tk.FLAT, bd=2,
                                   highlightthickness=1, highlightbackground=self.entry_border,
                                   yscrollcommand=result_scrollbar.set, state=tk.DISABLED)
        self.result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        result_scrollbar.config(command=self.result_text.yview)

        # Кнопка для выполнения операции
        button_font = font.Font(family="Segoe GUI", size=13, weight="bold")
        self.calculate_button = tk.Button(root, text="Выполнить", command=self.calculate, 
                                         bg=self.button_color, fg="white", 
                                         font=button_font, relief=tk.FLAT, bd=0,
                                         padx=30, pady=12, cursor="hand2",
                                         activebackground=self.button_active,
                                         activeforeground="white")
        self.calculate_button.pack(pady=20, ipadx=20, ipady=5)
        self.calculate_button.bind("<Enter>", lambda e: self.calculate_button.config(bg=self.hover_color))
        self.calculate_button.bind("<Leave>", lambda e: self.calculate_button.config(bg=self.button_color))
    
    def center_window(self, width, height):
        """Центрирует окно на экране"""
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def on_option_change(self, value):
        method_name = self.method_var.get()
        if method_name == "Композиция перестановок":
            self.second_perm_label.config(fg=self.backlight, text="Вторая перестановка: ✓")
        else:
            self.second_perm_label.config(fg=self.text_color, text="Вторая перестановка:")

    def calculate(self):
        method_name = self.method_var.get()
        first_perm_str = self.first_perm_entry.get()
        self._set_result('')

        try:
            first_perm = parse_permutation(first_perm_str)
        except ValueError as e:
            if first_perm_str == '':
                messagebox.showerror("Ошибка", "Первая перестановка не введена\nВведите перестановку, например: 2,1,3")
            else:
                messagebox.showerror("Ошибка", f"Некорректная перестановка\nВведите перестановку, например: 2,1,3")
            return

        if method_name == "Композиция перестановок":
            second_perm_str = self.second_perm_entry.get()

            try:
                second_perm = parse_permutation(second_perm_str)
            except ValueError:
                if second_perm_str == '':
                    messagebox.showerror("Ошибка", "Вторая перестановка не введена ( ´•︵•` )\nВведите перестановку, например: 3,2,1")
                else:
                    messagebox.showerror("Ошибка", "Некорректная перестановка ( ´•︵•` )\nВведите перестановку, например: 3,2,1")
                return

            try:
                result = COMPOSE_PP_P_f(first_perm, second_perm)
                self._set_result(f"{permutation_to_string(first_perm)} ∘ {permutation_to_string(second_perm)} = {permutation_to_string(result)}")
            except ValueError as e:
                messagebox.showerror("Ошибка", str(e))
                return

        elif method_name == "Обратная перестановка":
            result = INVERSE_P_P_f(first_perm)
            self._set_result(f"{permutation_to_string(first_perm)}⁻¹ = {permutation_to_string(result)}")

        elif method_name == "Разложение на циклы":
            cycles = TO_CYCLES_P_L_f(first_perm, include_fixed_points=False)
            cycles_str = cycles_to_string(cycles)
            self._set_result(f"{permutation_to_string(first_perm)} = {cycles_str}")

        elif method_name == "Знак перестановки":
            sign = SIGN_P_I_f(first_perm)
            sign_str = "чётная (+1)" if sign == 1 else "нечётная (-1)"
            self._set_result(f"sgn({permutation_to_string(first_perm)}) = {sign_str}")

        elif method_name == "Порядок перестановки":
            order = ORDER_P_N_f(first_perm)
            self._set_result(f"ord({permutation_to_string(first_perm)}) = {order}")

    def _set_result(self, text):
        """Устанавливает текст результата в Text виджет"""
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(1.0, text)
        self.result_text.config(state=tk.DISABLED)
        # Прокручиваем в начало
        self.result_text.see(1.0)


def create_CombinatoricsApp(root, theme):
    new_root = tk.Toplevel(root)
    app = CombinatoricsApp(new_root, theme=theme)
    return app

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Combinatorics Operations App')
    parser.add_argument('--theme', type=str, choices=['light', 'dark'], default='dark',
                        help='Choose the theme of the application')

    args = parser.parse_args()

    root = tk.Tk()
    app = CombinatoricsApp(root, theme=args.theme)
    root.mainloop()

