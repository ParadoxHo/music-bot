"""
Заглушка для модуля imghdr, который был удален в Python 3.13
"""
def what(file, h=None):
    """
    Упрощенная версия функции what из imghdr
    """
    return 'jpeg'  # Всегда возвращаем jpeg для совместимости

class ImghdrDummy:
    what = staticmethod(what)

# Создаем объект модуля
import sys
sys.modules[__name__] = ImghdrDummy()
