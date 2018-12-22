from optparse import OptionParser
import sys

# help text is printed if no argument is passed
help_text = """\n  -f, --csv_file
			"""
parser = OptionParser(usage=help_text)
parser.add_option("-f",   "--csv_file",            dest='csv_file',            help="",   default='no input')


if __name__ == '__main__':
	(options, args) = parser.parse_args()
	csv_file = options.csv_file

	if(csv_file == 'no input'):
		print('ERROR 1:')
		print('	No arguments passed')
		print('	Need to pass csv file name to be imported into Postgres')
		sys.exit(0)
	else:
		print('csv file:\n	',csv_file)