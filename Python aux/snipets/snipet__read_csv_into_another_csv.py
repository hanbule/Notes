from optparse import OptionParser
import csv
import sys
import os.path

# help text is printed if no argument is passed
help_text = """\n  -f, --csv_file
			"""
parser = OptionParser(usage=help_text)
parser.add_option("-f",   "--in_csv_file",            dest='in_csv_file',            help="",   default='no input')
parser.add_option("-o",   "--out_csv_file",           dest='out_csv_file',           help="",   default='out_csv_file_.csv')


def get_keys_from_odict_as_list(odict_):
	values_ls = []
	for item_ in odict_.items():
		values_ls.append(item_[1])
	
	return values_ls


def write_to_csv(out_csv_file_path, values_ls = None):	
	open_outfile = open(out_csv_file_path, 'a', encoding='utf-8-sig')
	with open_outfile as outfile:
		csv_writer = csv.writer(outfile)
		#for i in values_ls:
		csv_writer.writerow(values_ls)



if __name__ == '__main__':
# Get input CSV file name
	(options, args) = parser.parse_args()
	in_csv_file_path = options.in_csv_file

	if(in_csv_file_path == 'no input'):
		print('Error 1:')
		print('\tNo input csv file path argument passed')
		sys.exit(0)
	else:
		if(not os.path.isfile(in_csv_file_path)):
			print('Error 2:')
			print('\tThe follwing file not found\n\t%s' % in_csv_file_path)
			sys.exit(0)
		
		csv_file = in_csv_file_path.split('/')[-1:][0]
		print('%-20s' % (' '*2 + 'csv file path:'), in_csv_file_path)
		print('%-20s' % (' '*2 + 'csv file:'), csv_file)
		print()

# Get output CSV file name
	out_csv_file_path = options.out_csv_file
	if(out_csv_file_path == 'out_csv_file_.csv'):
		print('Warning 1:')
		print('\tNo output csv file name argument passed')
		print('\tOutput csv file will be %s' % out_csv_file_path)
		open(out_csv_file_path, 'w', encoding='utf-8-sig').close()  # create empty csv file


# Start input reading file
	infile = open(in_csv_file_path, 'r', encoding='utf-8-sig')
	csv_reader = csv.DictReader(infile)
	for row in csv_reader:
		row_vslues_ls = get_keys_from_odict_as_list(row)
		write_to_csv(out_csv_file_path, row_vslues_ls)



