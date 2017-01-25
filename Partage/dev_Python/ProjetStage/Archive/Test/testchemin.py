from tkinter.filedialog import *

def main():
	
	filename = askdirectory()
	print (filename)
	
	return 0

if __name__ == '__main__':
	main()

