import os
import math

essay_num = 312
beginner_num = 100
native_num = 60
medium_num = 43
professional_num = 109
beginner_len = 6529
medium_len = 11764
professional_len = 39555
native_len = 69943
total_len = beginner_len + medium_len + professional_len + native_len

beginner_dict = {}
native_dict = {}
professional_dict = {}
medium_dict = {}
total_dict = {}
b = 1e-9

black_list = []
#black_list = ['the', 'in', 'it', 'to', 'a', 'and', 'for', 'as', 'that', 'is', 'of', 'this', 'with', 'they', 'on', 'i', 'be', 'when', 'so', 'my', 'have', 'but', 'by', 'can', 'are', 'not', 'people', 'all', 'we', 'their', 'if', 'from', 'an', 'there', 'at', 'one', 'because', 'more', 'or', 'will', 'also', 'time', 'some', 'other', 'do', 'what', 'about', 'he', 'was', 'such']

def welcome():
    print('|===================================|')
    print('|                                   |')
    print('|     EssAy EyE: EyE Of EssAy!!     |')
    print('|                                   |')
    print('|===================================|')

def clean_str(context):
    context = context.replace('.', ' ')
    context = context.replace(',', ' ')
    context = context.replace('%', ' ')
    context = context.replace('(', ' ')
    context = context.replace(')', ' ')
    context = context.replace('\\', ' ')
    context = context.replace(';', ' ')
    context = context.replace(':', ' ')
    context = context.replace('!', ' ')
    context = context.replace('"', ' ')
    context = context.replace('/', ' ')
    context = context.replace('?', ' ')
    return context.lower()

def load_csv(path, dictionary, number, length):
    fp = open(path)
    line = fp.readline()
    assert(line == 'word, tf, idf\n')
    line = fp.readline()
    while line:
        element = line.split(',')
        if len(element[0].split()) == 2:
            line = fp.readline()
            continue

        if element[0] in black_list:
            line = fp.readline()
            continue

        dictionary[element[0]] = {'tf': (float(element[1])) / (length) + b, 'idf': math.log(number / (float(element[2]) + 1), 10) + b }
        if element[0] not in total_dict:
            total_dict[element[0]] = {'tf': float(element[1]) / (length), 'idf': float(element[2]) }
        else:
            total_dict[element[0]]['tf'] += float(element[1]) / (length)
            total_dict[element[0]]['idf'] += float(element[2])

        line = fp.readline()
    fp.close()

def make_total_dict(dictionary):

    for key in dictionary:
        dictionary[key]['idf'] = math.log((essay_num) / (dictionary[key]['idf'] + 1), 10)
        dictionary[key]['tf'] += b

def introduction():
   print('') 
   print('We will like to read the context in query.txt :)') 
   print('') 

def find_key_word():
    fp = open('query.txt')
    context = fp.read()
    context = clean_str(context)
    context = context.split()
    score = {}
    
    for word in context:
        if word in black_list:
            continue
        if word in total_dict:
            if word in score:
                score[word] += 1 * total_dict[word]['tf'] * total_dict[word]['idf'] * total_dict[word]['idf']
            else:
                score[word] = 1 * total_dict[word]['tf'] * total_dict[word]['idf'] * total_dict[word]['idf']
        else:
            if word in score:
                score[word] += 1 * math.log(essay_num*10 ,10) * math.log(essay_num*10 ,10) / total_len
            else:
                score[word] = 1 * math.log(essay_num*10 ,10) * math.log(essay_num*10 ,10) / total_len
    
    score_list = sorted(score.items(), key=lambda item:item[1], reverse= True)
    #print(score_list)
    return score_list

def print_ans(_score_list):
   
    print('They are key words of your essay')
    
    _score = 0
    for _, point in _score_list:
        _score += point
    
    print('word, importance')
    for index in range(5):
        print(_score_list[index][0], _score_list[index][1])

def main():
    beginner = 'data/dictionary/beginner.csv'
    native = 'data/dictionary/native.csv'
    professional = 'data/dictionary/professional.csv'
    medium = 'data/dictionary/medium.csv'
    load_csv(beginner, beginner_dict, beginner_num, beginner_len)
    load_csv(native, native_dict, native_num, native_len)
    load_csv(professional, professional_dict, professional_num, professional_len)
    load_csv(medium, medium_dict, medium_num, medium_len)
    make_total_dict(total_dict)
    
    beginner_score = sorted(beginner_dict.items(), key=lambda item:item[1]['idf']) 
    
    fp = open('data/idf_rank/beginner.csv', 'w')
    for key, ele in beginner_score:
        fp.write(key + ', ' + str(essay_num/ele['idf']) + '\n')
    fp.close()

    fp = open('data/idf_rank/native.csv', 'w')
    native_score = sorted(native_dict.items(), key=lambda item:item[1]['idf']) 
    for key, ele in native_score:
        fp.write(key + ', ' + str(essay_num/ele['idf']) + '\n')
    fp.close()
   
    medium_score = sorted(medium_dict.items(), key=lambda item:item[1]['idf']) 
    fp = open('data/idf_rank/medium.csv', 'w')
    for key, ele in medium_score:
        #print(key, ele['idf'])
        fp.write(key + ', ' + str(essay_num/ele['idf']) + '\n')
    fp.close()

    fp = open('data/idf_rank/professional.csv', 'w')
    professional_score = sorted(professional_dict.items(), key=lambda item:item[1]['idf']) 
    for key, ele in native_score:
        fp.write(key + ', ' + str(essay_num/ele['idf']) + '\n')
    fp.close()

    welcome()
    introduction()
    score_list = find_key_word()
    print_ans(score_list)
    
    total_score = sorted(total_dict.items(), key=lambda item:item[1]['idf']) 
    for key, ele in total_score[:50]:
        print("'"+ key + "'" + ', ', end = '')

if __name__ == '__main__':
    main()

