import os
from docx import Document
from docx.shared import Pt

#Вызываем функцию, для изменения документов
#тут же указываем путь к документам, желаемый шрифт, размер и межстрочный интервал
def change_document_style(file_path, font_name="Times New Roman", font_size=14, line_spacing=1.5):
    
    try:
        doc = Document(file_path)
        style = doc.styles['Normal']
        font = style.font
        font.name = font_name
        font.size = Pt(font_size)
        style.paragraph_format.line_spacing = line_spacing
        doc.save(file_path)
        print(f"Документ '{file_path}' успешно изменен.")
    except Exception as e:
        print(f"Ошибка в обработке документа '{file_path}': {e}")