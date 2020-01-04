import numpy as np
conj_and_prep = ('in','on','at','of','for','with','from','and','but','or','so','because','when','before','although')
def counter(txt,array):
    for i in np.arange(len(txt)):
        for j in np.arange(len(conj_and_prep)):
            if txt[i] == conj_and_prep[j]:
                array[j] = array[j] + 1
            else:
                continue
    return array