import numpy as np
Punctuation_Marks = ('.','[',']','"',"'",'!',',',':','?','´','["','"]')

def clear(file):
    for i in np.arange(len(Punctuation_Marks)):
        file = file.replace(Punctuation_Marks[i],' ')
        return file
    