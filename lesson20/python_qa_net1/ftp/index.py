from ftplib import FTP

HOST = "192.168.1.75"
USER = "ftpuser"
PASSWORD = "ftpuser"

ftp = FTP(host=HOST, user=USER, passwd=PASSWORD)

print(ftp.dir())

# Переходим в папку
ftp.cwd('files')

# Смотрим что в директории
print(ftp.dir())
print(ftp.retrlines('LIST'))

# Скачиваем нужный файл
with open('Habr.py', 'wb') as fp:
    ftp.retrbinary('RETR Habr.py', fp.write)

# Создание папки
# ftp.mkd('my_dir')
# print(ftp.dir())

# Загружаем наш файл в эту папку
with open('logo.png', 'rb') as fp:
    ftp.storbinary('STOR logo.png', fp)

ftp.quit()
