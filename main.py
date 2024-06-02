#Скрипт для изменения в docx файлах шрифт на Times New Roman, 14 и межстрочный интервал на 1.5

import os
from docx import Document
from docx.shared import Pt

from data import change_document_style

#Вызываем функцию main, чтобы обрабатывать сразу несколько файлов
def main():
    docx_files = [f for f in os.listdir('.') if f.endswith('.docx')]
    if len(docx_files) >= 0:  #здесь можно указать ограничение по минимальному                                    кол-ву файлов
        for file in docx_files[:1000]: #а здесь по максимальному
            change_document_style(file)
    else:
        print("Error: Недостаточно .docx файлов для начала обработки.")
if __name__ == "__main__":
    main()