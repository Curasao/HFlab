
import gdown
#импортируем библиотеку для чтения файлов с google drive
url = 'https://drive.google.com/uc?id=10sSOzShxYFo1No-JyBei1dSmetwnavqm'
#записываем атрибуты - ссылка на архив, имя архива
output = 'QAtest.zip'
gdown.download(url, output, quiet=False)
#импортируем библиотеку для работы с архивами
from zipfile import ZipFile

with ZipFile('QAtest.zip') as zf:
    zf.extractall(pwd=b'hflabs')
#архив запаролен, указываем пароль в байтном виде
cyrillicA = 'а'
#создаем переменную для хранения а
file = open('QAtest.txt', 'r', encoding='utf8')
#открываем файл
lines = 0
countOfDigitA = 0
#применяем цикл для сортировки строк, для более быстрого перебора используем конструкцию lines % 1000 == 0
for line in file:
    lines += 1
    if (lines % 1000 == 0): print('Checking line: ', lines)
    countOfDigitA += line.count(cyrillicA)


#выводим количество строк на экран и количество вхождений а
print(lines, '----------')
print(lines, 'lines')
print(countOfDigitA, ' a')
#закрываем файл
file.close()










