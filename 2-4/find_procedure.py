# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

import os

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
	files = os.listdir(os.path.join(current_dir, migrations))

	def found_sql_files(files, sql_files):
		for f in files:
			if f[-4:] == '.sql':
				sql_files.append(f)
			else:
				continue
		return(sql_files)

	def search_files_by_text(sql_files):
		text = input('Введите строку ').upper()
		true_files = []
		for file in sql_files:
			s = False
			with open(os.path.join(current_dir, migrations, file), 'r') as f:
				for line in f:
					if text in line.upper():
						s = True
						true_files.append(file)
						print(os.path.join(migrations, file))
						break
					else:
						continue

		sql_files = sql_files and true_files
		print('Всего:', len(sql_files))
		search_files_by_text(sql_files)
	
		

	def program():
		sql_files = []
		found_sql_files(files, sql_files)
		search_files_by_text(sql_files)

	program()
	pass
