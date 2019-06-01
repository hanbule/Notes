# Ex:
# print_df_tabular(df)
# print_df_tabular(df, index=True)
# Note: indeces are printed AS IS from df
def print_df_tabular(df, index=False):
	import os.path
	import sys
	import pandas as pd
	if(not isinstance(df, pd.DataFrame)):
		print('ERROR:')
		print('Object for display is not DataFrame\n')
		sys.exit(0)

	cols_ls = df.columns.values.tolist()
	cols_maxWidth_dict = {}
	enlarge = 2

	# calculate width for each column
	for i, col in enumerate(cols_ls):
		max_l = df[col].map(lambda x: len(str(x))).max()  # get length of longest string value
		max_l = max(len(col),max_l)                       # get length of column name if it is longer
		cols_maxWidth_dict[i] = max_l
		#print(max_l)

	# calculate index column width
	if(index):
		df_row_count = df.shape[0]
		index_width = len(str(df_row_count))
		index_col_name = 'ix'

	# ------------------------------------------------------------------------------------
	# print top line of header
	sep_ = ''
	if(index):
		sep_ = '-'*(index_width+enlarge)
		sep_ = sep_ + '+'
	for i, col in enumerate(cols_ls):	
		sep_ = sep_ + '-'*(cols_maxWidth_dict[i]+enlarge)
		sep_ = sep_ + '+'
	print(sep_)
	#file_out.write(sep_+'\n')

	# ------------------------------------------------------------------------------------
	# print header
	sep_ = ''
	if(index):
		sep_ = sep_ + index_col_name + ' '*(index_width-len(index_col_name)+enlarge)
		sep_ = sep_ + '|'
	for i, col in enumerate(cols_ls):	
		sep_ = sep_ + col + ' '*(cols_maxWidth_dict[i]-len(col)+enlarge)
		sep_ = sep_ + '|'
	print(sep_)
	#file_out.write(sep_+'\n')

	# ------------------------------------------------------------------------------------
	# print bottom line of header
	sep_ = ''
	if(index):
		sep_ = '-'*(index_width+enlarge)
		sep_ = sep_ + '+'
	for i, col in enumerate(cols_ls):	
		sep_ = sep_ + '-'*(cols_maxWidth_dict[i]+enlarge)
		sep_ = sep_ + '+'
	print(sep_)
	#file_out.write(sep_+'\n')

	# ------------------------------------------------------------------------------------
	# print row values
	for ix, row in df[cols_ls].iterrows():
		sep_ = ''
		if(index):
			ix_str = str(int(ix))
			sep_ = sep_ + ix_str + ' '*(index_width-len(ix_str)+enlarge)
			sep_ = sep_ + '|'
		for i,v in enumerate(list(row)):
			#print(i,v)
			sep_ = sep_ + str(v) + ' '*(cols_maxWidth_dict[i]-len(str(v))+enlarge)
			sep_ = sep_ + '|'
		print(sep_)
		#file_out.write(sep_+'\n')
	print()

# Ex:
# df_to_txt_tabular(df, 'df_formatted.txt')
# df_to_txt_tabular(df, 'df_formatted.txt', ask_if_file_exists=False, index=True)
# Note: indeces are printed AS IS from df
def df_to_txt_tabular(df, file_name, ask_if_file_exists=True, index=False):
	import os.path
	import sys
	import pandas as pd

	# check if object for display is pandas df
	if(not isinstance(df, pd.DataFrame)):
		print('ERROR:')
		print('Object for display is not DataFrame\n')
		sys.exit(0)

	# check if given name file already exists
	if(os.path.isfile(file_name) and ask_if_file_exists):
		msg = '\nWARNING:\nFile '+file_name+' already exists, if you continue exporting, ' \
				+'it will be overritten \nDo you still want to continue exporting, Y/N: '
		user_input = str(input(msg))
		while user_input.lower() not in ('y','n'):
			user_input = str(input('Try again, you should input Y or N: '))
		if user_input.lower() == 'n':
			print('WARNING:')
			print('Program stopped by you ...')
			sys.exit(0)


	cols_ls = df.columns
	cols_maxWidth_dict = {}
	enlarge = 2

	# calculate width for each column
	for i, col in enumerate(cols_ls):
		max_l = df[col].map(lambda x: len(str(x))).max()  # get length of longest string value. Note: if df has >1 columns with same name, map will throw error as df[col] will return DataFrame instaed Series.
		max_l = max(len(col),max_l)                       # get length of column name if it is longer
		cols_maxWidth_dict[i] = max_l
		#print(max_l)

	# calculate index column width
	if(index):
		df_row_count = df.shape[0]
		index_width = len(str(df_row_count))
		index_col_name = 'ix'


	#file_out = open('/Users/altay.amanbay/Desktop/'+file_name+'.txt','w')
	file_out = open(file_name,'w')

	# ------------------------------------------------------------------------------------
	# write top line of header
	sep_ = ''
	if(index):
		sep_ = '-'*(index_width+enlarge)
		sep_ = sep_ + '+'
	for i, col in enumerate(cols_ls):	
		sep_ = sep_ + '-'*(cols_maxWidth_dict[i]+enlarge)
		sep_ = sep_ + '+'
	#print(sep_)
	file_out.write(sep_+'\n')

	# ------------------------------------------------------------------------------------
	# write header
	sep_ = ''
	if(index):
		sep_ = sep_ + index_col_name + ' '*(index_width-len(index_col_name)+enlarge)
		sep_ = sep_ + '|'
	for i, col in enumerate(cols_ls):	
		sep_ = sep_ + col + ' '*(cols_maxWidth_dict[i]-len(col)+enlarge)
		sep_ = sep_ + '|'
	#print(sep_)
	file_out.write(sep_+'\n')

	# ------------------------------------------------------------------------------------
	# write bottom line of header
	sep_ = ''
	if(index):
		sep_ = '-'*(index_width+enlarge)
		sep_ = sep_ + '+'
	for i, col in enumerate(cols_ls):	
		sep_ = sep_ + '-'*(cols_maxWidth_dict[i]+enlarge)
		sep_ = sep_ + '+'
	#print(sep_)
	file_out.write(sep_+'\n')

	# ------------------------------------------------------------------------------------
	# write row values
	for ix, row in df[cols_ls].iterrows():
		sep_ = ''
		if(index):
			ix_str = str(int(ix))
			sep_ = sep_ + ix_str + ' '*(index_width-len(ix_str)+enlarge)
			sep_ = sep_ + '|'
		for i,v in enumerate(list(row)):
			#print(i,v)
			sep_ = sep_ + str(v) + ' '*(cols_maxWidth_dict[i] - len(str(v))+enlarge)
			sep_ = sep_ + '|'
		#print(sep_)
		file_out.write(sep_+'\n')

	file_out.close()


def check_if_file_exists_1(file_path):
    try:
        with open(file_path) as infile:
            pass
    except IOError:
        print('  ERROR: '+file_path+' file not found\n')
        sys.exit()


def check_if_file_exists_2(file_path):
	import os.path
	import sys
	if(os.path.isfile(file_path)):
		return True
	else:
		return False


# Ex:
# file_1 = path = "/Users/altay.amanbay/Desktop/10_lines.csv"
# file_2 = path = "/Users/altay.amanbay/Desktop/10_lines.csv"
# join_cols_ls = ['description_mod1_norm','description_mod1_norm']
# out_file_path = '/Users/altay.amanbay/Desktop/tempo.csv'
# cols_1 = ['description_mod1','description_mod1_norm']
# cols_2 = ['description_mod1','description_mod1_norm','category_full_path_mod1','year']
# df1_in_df2_match(file_1, file_2, join_cols_ls, out_file_path, cols_1, cols_2)

# Performs following sql query logic on csv files:
# SELECT cols_1, cols_2 
# INTO out_file_path
# FROM file_1 LEFT JOIN file_2
# ON REGEXP_REPLACE(LOWER(join_cols_ls[0]), '[^a-z0-9]', '') LIKE '%'+REGEXP_REPLACE(LOWER(join_cols_ls[1]), '[^a-z0-9]', '')+'%'
# WHERE join_cols_ls[1] is not null

def df1_in_df2_match(in_csv_path_1_str_, in_csv_path_2_str_, join_cols_ls_, out_csv_path_str_, in_csv_1_cols_ls_, in_csv_2_cols_ls_):
    import pandas as pd
    import numpy as np
    import time
    import csv
    import re
    start = time.time()

    infile_1 = open(in_csv_path_1_str_, encoding='utf-8-sig')
    csv_reader_1 = csv.reader(infile_1)

    infile_2 = open(in_csv_path_2_str_, encoding='utf-8-sig')
    csv_reader_2 = csv.reader(infile_2)

    outfile_1 = open(out_csv_path_str_,'w', encoding='utf-8-sig')
    csv_writer = csv.writer(outfile_1, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    csv_writer.writerow(in_csv_1_cols_ls_ + in_csv_2_cols_ls_)

    # read first row (column names) and check for presence of non-printable characters
    csv_1_all_cols_ls = next(csv_reader_1)  # read line from 1st file
    csv_2_all_cols_ls = next(csv_reader_2)  # read line from 2nd file
    
    # check and correct 1st file column names
    for i, col_name in enumerate(csv_1_all_cols_ls):
        if('\ufeff' in col_name):
            extracted_match = re.match('\ufeff\"(.*)\"', col_name)
            corrected_col_name = extracted_match.group(1)
            csv_1_all_cols_ls[i] = corrected_col_name
            print('ATTENTION:')
            print('Correction made to column name for output file:')
            print('Column name: '+col_name)
            print('File: '+in_csv_path_1_str_+'\n')
            
    
    # check and correct 2nd file column names
    for i, col_name in enumerate(csv_2_all_cols_ls):
        if('\ufeff' in col_name):
            extracted_match = re.match('\ufeff\"(.*)\"', col_name)
            corrected_col_name = extracted_match.group(1)
            csv_2_all_cols_ls[i] = corrected_col_name
            print('ATTENTION:')
            print('Correction made to column name for output file:')
            print('Column name: '+col_name)
            print('File: '+in_csv_path_2_str_+'\n')
    
    
    # get queue numbers of specified outfile columns
    csv1_col_nums_ls = []
    csv2_col_nums_ls = []
    
    for spec_col_name in in_csv_1_cols_ls_:
        for j, col_name in enumerate(csv_1_all_cols_ls):
            #print(i,c)
            if(spec_col_name == col_name):
                csv1_col_nums_ls.append(j)
    infile_1.seek(0)
    
    for spec_col_name in in_csv_2_cols_ls_:
        for j, col_name in enumerate(csv_2_all_cols_ls):
            #print(i,c)
            if(spec_col_name == col_name):
                csv2_col_nums_ls.append(j)
    infile_2.seek(0)
    

    # get queue numbers of specified join columns
    join_col_num_1 = None
    join_col_num_2 = None
    
    for j, col_name in enumerate(csv_1_all_cols_ls):
        #print(j,col_name)
        if(join_cols_ls_[0] == col_name):
            join_col_num_1 = j
    
    for j, col_name in enumerate(csv_2_all_cols_ls):
        #print(j,col_name)
        if(join_cols_ls_[1] == col_name):
            join_col_num_2 = j
    
    
    c = 0
    next(csv_reader_1)      # skip header
    for row_1 in csv_reader_1:
        next(csv_reader_2)  # skip header
        for row_2 in csv_reader_2:
            if(row_2[join_col_num_2] in row_1[join_col_num_1]):
                c=c+1
                row_values_ls = []
                for i in csv1_col_nums_ls:
                    row_values_ls.append(row_1[i])
                for i in csv2_col_nums_ls:
                    row_values_ls.append(row_2[i])

                csv_writer.writerow(row_values_ls)
        infile_2.seek(0)    # return to the top of the file
    print('\nNumber of lines in file:',c)


    infile_1.close()
    infile_2.close()
    outfile_1.close()
    print('Process time %g s' % (time.time()-start))


# Keeps alpha-numeric symbols only
# Ex:
# str_to_alnum('London now !! good $')
# Output: 'London now  good '
def str_to_alnum(sentence_):
    printable_ = 'abcdefghijklmnopqrstuvwxyz0123456789 '
    sentence_processed = "".join((char if char in printable_ else "") for char in str(sentence_).lower())
    
    return sentence_processed


# Ex:
# NGramGenerator_wordwise_interval('aa bb cc',1,1)
# Output: ['aa', 'bb', 'cc']
# NGramGenerator_wordwise_interval('aa bb cc',2,2)
# Output: ['aa bb', 'bb cc']
# NGramGenerator_wordwise_interval('aa bb cc',1,2)
# Output: ['aa bb', 'bb cc', 'aa', 'bb', 'cc']
def NGramGenerator_wordwise_interval(phrase, min_ngram, max_ngram):
    all_ngram_lists = []

    # Keeps alpha-numeric symbols only and split into tokens
    printable_ = 'abcdefghijklmnopqrstuvwxyz0123456789 '
    s_split = "".join((char if char in printable_ else "") for char in phrase).split()
    
    for n in range(max_ngram, min_ngram - 1, -1):
        n_gram = [s_split[i:i+n] for i in range(len(s_split)-n+1)]
        all_ngram_lists.extend(n_gram)
        
    all_ngrams = []
    for n_gram in all_ngram_lists:
        all_ngrams.extend([' '.join(n_gram)])
    
    return all_ngrams


# Ex:
# get_ranges_for_df(10,5)
# Output: [(0, 4), (5, 9)]
# get_ranges_for_df(10,2)
# Output: [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]
# get_ranges_for_df(10,3)
# Output: [(0, 2), (3, 5), (6, 8), (9, 9)]
def get_ranges_for_df(input_df_size_, insertion_chunk_size_):
    ranges_ = []

    c = 0
    while(True):
        if(input_df_size_ >= insertion_chunk_size_):
            input_df_size_ = input_df_size_ - insertion_chunk_size_
            range_ = (c * insertion_chunk_size_ , (c+1) * insertion_chunk_size_ - 1)
            ranges_.extend([range_])
            c = c + 1
            if(input_df_size_ == 0):
                break
        else:
            if(input_df_size_-1 < c*insertion_chunk_size_):
                range_ = (c * insertion_chunk_size_, (c*insertion_chunk_size_) + input_df_size_ - 1)
            else:
                range_ = (c * insertion_chunk_size_, input_df_size_ - 1)
            ranges_.extend([range_])
            break

    return ranges_


def get_incremental_ranges(input_df_size_, insertion_chunk_size_):
    ranges_ = []

    c = 0
    while(True):
        if(input_df_size_ >= insertion_chunk_size_):
            input_df_size_ = input_df_size_ - insertion_chunk_size_
            range_ = (0 , (c+1) * insertion_chunk_size_ - 1)
            ranges_.extend([range_])
            c = c + 1
            if(input_df_size_ == 0):
                break
        else:
            if(input_df_size_-1 < c*insertion_chunk_size_):
                range_ = (0, (c*insertion_chunk_size_) + input_df_size_ - 1)
            else:
                range_ = (0, input_df_size_ - 1)
            ranges_.extend([range_])
            break

    return ranges_

# Make sure that column types of dataframe to be inserted and db table name are consistent
def insert_df_into_db(df, insert_chunk_size, schema_table_name, columns_list, engine):
	from sqlalchemy import text
	conn = engine.connect()

	# get insert chunk ranges
	ranges = get_ranges_for_df(df.shape[0], insert_chunk_size)

    # get query template
	qry_template = "insert into " + schema_table_name + " (" + ','.join(columns_list) + ") values "

	values_holder_dict = {}
	for range_ in ranges:
		qry = qry_template
        #print(range_)
		for i in range(range_[0], range_[1]+1):
			for col_name in columns_list:
				value = df.loc[i, col_name]
				value = str(value)
				value = value.replace("'","''")   # replace special characters
				value = value.replace(":","\:")   # replace special characters
				values_holder_dict[col_name] = value

				comma = ","
				if(i == range_[0]):
					comma = ""

			values_line_ls = [values_holder_dict[col_name] for col_name in columns_list]
			values_line_ls = ["'"+value_+"'" for value_ in values_line_ls]
			values_line_str = ','.join(values_line_ls)
			values_line_str = comma + "(" + values_line_str + ")"
			#line = comma + "('" + description + "','" + str(order) + "')"
			qry = qry + values_line_str
         
		#print('\n'+qry)   
		conn.execute(text(qry))
        
	conn.close()
	print('\nData insertion into db is complete ...')

