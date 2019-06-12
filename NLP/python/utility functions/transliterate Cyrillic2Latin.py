# 1
'''
python version: 2.7.15
'''

# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import pandas as pd
  
  
def transliterate_string_Cyrillic2Latin(str_):
	answer = ""

	# 1.1
	# cyrillic2latin dict
	a = dict()
	a["А"]="A"; a["Б"]="B"; a["В"]="V"; a["Г"]="G"; a["Д"]="D"; a["Е"]="E"; a["Ё"]="YO"; a["Ж"]="ZH"; a["З"]="Z"; a["И"]="I"; a["Й"]="I"; a["К"]="K"; a["Л"]="L"; a["М"]="M"; a["Н"]="N"; a["О"]="O"; a["П"]="P"; a["Р"]="R"; a["С"]="S"; a["Т"]="T"; a["У"]="U"; a["Ф"]="F"; a["Х"]="H"; a["Ц"]="TS"; a["Ч"]="CH"; a["Ш"]="SH"; a["Щ"]="SCH"; a["Ъ"]="'"; a["Ы"]="I"; a["Ь"]="'"; a["Э"]="E"; a["Ю"]="YU"; a["Я"]="YA"; 
	a["а"]="a"; a["б"]="b"; a["в"]="v"; a["г"]="g"; a["д"]="d"; a["е"]="e"; a["ё"]="yo"; a["ж"]="zh"; a["з"]="z"; a["и"]="i"; a["й"]="i"; a["к"]="k"; a["л"]="l"; a["м"]="m"; a["н"]="n"; a["о"]="o"; a["п"]="p"; a["р"]="r"; a["с"]="s"; a["т"]="t"; a["у"]="u"; a["ф"]="f"; a["х"]="h"; a["ц"]="ts"; a["ч"]="ch"; a["ш"]="sh"; a["щ"]="sch"; a["ъ"]="'"; a["ы"]="i"; a["ь"]="'"; a["э"]="e"; a["ю"]="yu"; a["я"]="ya"; 

	# kazakh letters (in case if needed)
	# a["ә"]="á"; a["і"]="i"; a["ң"]="ń"; a["ғ"]="ǵ"; a["ү"]="ú"; a["ұ"]="u"; a["қ"]="q"; a["ө"]="ó"; a["һ"]="h";  
	# a["Ә"]="Á"; a["І"]="I"; a["Ң"]="Ń"; a["Ғ"]="Ǵ"; a["Ү"]="Ú"; a["Ұ"]="U"; a["Қ"]="Q"; a["Ө"]="Ó"; a["Һ"]="H";

	# 1.2 (optional)
	# dict keys to utf-8
	# a = dict((k.decode('utf-8'), v) for (k, v) in a.items())


	for i in range(0, len(str_)):
		if(i == 0):  # if it's just start
			# print "P 1"
			if (str_[i] in a):
				answer = answer + a[str_[i]]
			else:			
				answer = answer + str_[i]

		elif(str_[i-1] in a and str_[i] in a):
			# print "P 2"	
			answer = answer + "_" + a[str_[i]]	

		elif (str_[i-1] not in a and str_[i] in a):
			# print "P 3"
			answer = answer + a[str_[i]]

		elif (str_[i] not in a):
			# print "P 4"
			answer = answer + str_[i]

	return answer

 
  
if __name__ == '__main__':
	ss = ['домой', 'Я иду домой']
	for s in ss:
		tr = transliterate_string_Cyrillic2Latin(s)
		print(tr)
  
Out:
  d_o_m_o_i
  YA i_d_u d_o_m_o_i
  
  # if load file with cyrillic text, make sure it's in utf-8 encoding
  # or if file has different encoding, indicate accordingly when loading
  df = pd.read_csv("...", encoding="utf-8")
  
  
  
