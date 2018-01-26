
import os
import PyPDF2
import re
import sys

full_pdf = ''
keywords = []
paths = []


def clear():
	os.system("cls" if os.name == "nt" else "clear")


def grab_paths_from_user():
	if keywords == []:
		print('''You must add one or more search terms before using this function.'''.upper())
		blank = input("")
		clear()
		menu()
	else:
		doc_path = input("Enter the PATH of your PDF or Drag&Drop PDF onto Terminal window: ").rstrip()
		if doc_path == '' and paths == []:
			exit_to_menu_question(grab_paths_from_user)
			clear()
		elif doc_path == '':
			question_to_use_old_paths = input('Do you wish NOT to ADD any new PDFs, and to search ONLY your previous PDFs instead? [y/N] ').lower()
			if question_to_use_old_paths == 'y':
				use_old_paths()
			else:
				grab_paths_from_user()
		else:
			paths.append(doc_path)
			add_path = input("""You you like to add another document to be searched? [y/N] """)
			print('')
			if add_path == 'y':
				grab_paths_from_user()
			else:
				packets_to_market()


def use_old_paths():
	if paths == []:
		print('''You must add a PDF file to be searched first before you may use this function''')
		blank = input("")
		clear()
		menu()
	else:
		packets_to_market()
		clear()


def packets_to_market():
	""" """
	for a_path in paths:
		pdf_name_regex = re.compile(r'\w*\.pdf')
		pdf_file_name = pdf_name_regex.search(a_path)
		pdf_to_single_string(a_path)
		search_results(pdf_file_name)
		print('')
		global full_pdf
		full_pdf = ''
	blank = input("")


def pdf_to_single_string(path):
	try:
		pdf_file_obj = open(path, 'rb')
	except FileNotFoundError:
		print("""An error has occured. Please check to make sure the PATH you typed was correct: {} """.format(path))
		exit_to_menu_question(grab_paths_from_user)
	else:
		pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
		num_of_pgs = pdf_reader.numPages
		for page in range(0, num_of_pgs):
			page_object = pdf_reader.getPage(page)
			global full_pdf
			full_pdf += (page_object.extractText()).replace('\n', '')


def search_results(pdf_file_name):
	for word in keywords:
		if word or word.upper() or word.lower() or word.title() in full_pdf:
			regex = re.compile(r'{}'.format(word), re.IGNORECASE)
			occurances = regex.findall('{}'.format(full_pdf))
			print("""{} was found {} times in {}
				""".format(word.upper(), len(occurances), pdf_file_name.group().upper()))
		else:
			print("""No occurances of {} were found in {}
				""".format(word.upper(), pdf_file_name.group().upper()))


def clear_paths(paths_list):
	global paths
	paths = []
	print('PDFs CLEARED.')
	blank = input("")


def clear_search_terms(search_terms_list):
	global keywords
	keywords = []
	print('SEARCH TERMS CLEARED.')
	blank = input("")

def add_search_term():
	add_term = input("""What search term would you like to add? """)
	if add_term == '':
		exit_to_menu_question(add_search_term)
	keywords.append(add_term)

def exit_to_menu_question(function_to_be_exited):
	question_to_exit = input("Do you wish to return to the main menu? [y/N] ").lower()
	if question_to_exit == 'y':
		menu()
	else:
		function_to_be_exited()


def menu():
	keyword_option = input("""Your options are...
A: Add a new search term
S: Search a PDF with terms added
R: Reuse PDFs with current search terms
C: Clear search terms
P: Clear PDFs to be searched
Q: Quit
Enter option: """).lower()

	if keyword_option == 'a':
		clear()
		add_search_term()
		clear()
		print("Current Search Terms:", keywords)
		print('*' * 32)
		menu()
	elif keyword_option == 's':
		clear()
		grab_paths_from_user()
		clear()
		menu()
	elif keyword_option == 'r':
		clear()
		use_old_paths()
		menu()
	elif keyword_option == 'c':
		clear()
		clear_search = input("""Are you want to clear your search terms? [y/N] """).lower()
		if clear_search == 'y':
			clear_search_terms(keywords)
			clear()
			menu()
		else:
			clear()
			menu()
	elif keyword_option == 'p':
		clear()
		clear_the_paths = input("""Are you want to clear your PDFs? [y/N] """).lower()
		if clear_the_paths == 'y':
			clear_paths(paths)
			clear()
			menu()
		else:
			clear()
			menu()
	elif keyword_option == 'q':
		sys.exit()
	else:
		clear()
		menu()


def replace_all(text, dic):
	for i, j in dic.items():
		text = text.replace(i, j)
	return text


if __name__ == "__main__":
	clear()
	menu()
