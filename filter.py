import re

#импортируем библиотеку для регулярных выражений
regexp = "140002 ЛЮБЕРЦЫ 2 ОКТЯБРЬСКИЙ ПР 123/4-115"
#составляем регулярное выражение для поиска
replacement = re.search(r'140002.ЛЮБЕРЦЫ.\d.ОКТЯБРЬСКИЙ.ПР.123/4-115', r'140002 ЛЮБЕРЦЫ 2 ОКТЯБРЬСКИЙ ПР 123/4-115')
#заменяем символы в строке методом replace
string_print = regexp
print (string_print.replace(string_print,'140002 ЛЮБЕРЦЫ ОКТЯБРЬСКИЙ ПР 123/4-115'))