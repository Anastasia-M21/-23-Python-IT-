floppy_disk_size_in_Mb = 1.44          # Информационный объем дискеты в мегабайтах
number_of_pages = 100                  # Количество страниц в книге
number_of_lines = 50                   # Число строк на странице
number_of_characters = 25              # Количество символов в строке
weight_of_one_character = 4            # Количество байт для хранения кода одного символа

floppy_disk_size_in_b = floppy_disk_size_in_Mb * 1024**2                         # Объем дискеты в байтах
volume_of_one_book = number_of_pages * number_of_lines \
                         * number_of_characters * weight_of_one_character        # Объем одной книги
number_of_books = floppy_disk_size_in_b // volume_of_one_book

print("Количество книг, помещающихся на дискету:", int(number_of_books))
