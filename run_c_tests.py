"""
Запускает тесты комбинаторики из модуля С

Использование:
    python run_c_tests.py
"""
import sys
import os

# Добавляем корневую директорию в sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Импортируем и запускаем тесты
from modules.С.tests import run_all_tests

if __name__ == "__main__":
    # Для Windows устанавливаем UTF-8 кодировку
    if os.name == 'nt':
        import codecs
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    
    run_all_tests()

