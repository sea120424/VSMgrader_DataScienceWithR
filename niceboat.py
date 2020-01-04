###############################################################################
import numpy as np
import clearnods as cr
import freqcount as count
from os import listdir
import pandas as pd
###############################################################################

###############################################################################
filepath_begin = r'C:\Users\n8748\Documents\GitHub\VSMgrader_DataScienceWithR\data\beginner'
files_begin = listdir(filepath_begin)
abspath_begin = ["" for x in range(len(files_begin))]
for i in np.arange(len(files_begin)):
    abspath_begin[i] = filepath_begin + '\\' + files_begin[i] 
###############################################################################

###############################################################################
filepath_medium = r'C:\Users\n8748\Documents\GitHub\VSMgrader_DataScienceWithR\data\medium'
files_medium = listdir(filepath_medium)
abspath_medium = ["" for x in range(len(files_medium))]
for i in np.arange(len(files_medium)):
    abspath_medium[i] = filepath_medium + '\\' + files_medium[i] 
###############################################################################

###############################################################################
filepath_professional = r'C:\Users\n8748\Documents\GitHub\VSMgrader_DataScienceWithR\data\professional'
files_professional = listdir(filepath_professional)
abspath_professional = ["" for x in range(len(files_professional))]
for i in np.arange(len(files_professional)):
    abspath_professional[i] = filepath_professional + '\\' + files_professional[i] 
###############################################################################

###############################################################################
filepath_native = r'C:\Users\n8748\Documents\GitHub\VSMgrader_DataScienceWithR\data\native'
files_native = listdir(filepath_native)
abspath_native = ["" for x in range(len(files_native))]
for i in np.arange(len(files_native)):
    abspath_native[i] = filepath_native + '\\' + files_native[i] 
###############################################################################

###############################################################################
conj_and_prep = ('in','on','at','of','for','with','from','and','but','or','so','because','when','before','although')
freq_begin = np.zeros(len(conj_and_prep))
freq_medium = np.zeros(len(conj_and_prep))
freq_professional = np.zeros(len(conj_and_prep))
freq_native = np.zeros(len(conj_and_prep))
###############################################################################

###############################################################################
for path_begin in abspath_begin:
    txt = open(path_begin,encoding="utf-8")
    str_file = txt.readlines()
    str_file = str(str_file)
    str_file = str_file.lower()
    str_file = cr.clear(str_file)
    str_file = str_file.split(' ')
    freq_begin = count.counter(str_file,freq_begin)
###############################################################################

###############################################################################
for path_medium in abspath_medium:
    txt = open(path_medium,encoding="utf-8")
    str_file = txt.readlines()
    str_file = str(str_file)
    str_file = str_file.lower()
    str_file = cr.clear(str_file)
    str_file = str_file.split(' ')
    freq_medium = count.counter(str_file,freq_medium)
###############################################################################

###############################################################################
for path_professional in abspath_professional:
    txt = open(path_professional,encoding="utf-8",errors = 'ignore')
    str_file = txt.readlines()
    str_file = str(str_file)
    str_file = str_file.lower()
    str_file = cr.clear(str_file)
    str_file = str_file.split(' ')
    freq_professional = count.counter(str_file,freq_professional)
###############################################################################
    
###############################################################################
for path_native in abspath_native:
    txt = open(path_native,encoding="utf-8")
    str_file = txt.readlines()
    str_file = str(str_file)
    str_file = str_file.lower()
    str_file = cr.clear(str_file)
    str_file = str_file.split(' ')
    freq_native = count.counter(str_file,freq_native)
###############################################################################    

###############################################################################
print(conj_and_prep)
print(freq_begin)
print(freq_medium)
print(freq_professional)
print(freq_native)
###############################################################################

###############################################################################
array1 = ['beginner' for x in range(15)]
array2 = ['medium' for x in range(15)]
array3 = ['professional' for x in range(15)]
array4 = ['native' for x in range(15)]
kind = array1 + array2 +array3 +array4
freq = [0]*60
freq[0:14] = freq_begin
#freq[15:29] = freq_medium
#freq[30:44] = freq_professional
#freq[45:59] = freq_native
###############################################################################

###############################################################################
array = [conj_and_prep*4,
         kind,
         freq]
df = pd.DataFrame(array).T
df.to_excel(excel_writer = r"C:\Users\n8748\Desktop\freq_str.xlsx")