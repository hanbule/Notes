from optparse import OptionParser
import sys
import os.path

# help text is printed if no argument is passed
help_text = """\n  -f, --csv_file
			"""
parser = OptionParser(usage=help_text)
parser.add_option("-f",   "--csv_file",            dest='csv_file',            help="",   default='no input')


if __name__ == '__main__':
	(options, args) = parser.parse_args()
	csv_file_path = options.csv_file

	if(csv_file_path == 'no input'):
		print('Warning:')
		print('\tNo arguments passed')
		print('\tNeed to pass csv file name to be imported into Postgres')
		sys.exit(0)
	else:
		if(not os.path.isfile(csv_file_path)):
			print('Error:')
			print('\tThe follwing file not found\n\t%s' % csv_file_path)
			sys.exit(0)
		
		csv_file = csv_file_path.split('/')[-1:][0]
		print('%-20s' % (' '*2 + 'csv file path:'), csv_file_path)
		print('%-20s' % (' '*2 + 'csv file:'), csv_file)