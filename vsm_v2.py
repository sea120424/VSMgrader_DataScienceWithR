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

#black_list = ['and', 'the', 'a', 'an', 'to', 'on', 'is', 'are', 'i', 'you', 'am']
black_list = []

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
    context = context.replace('?', ' ')
    context = context.replace("'", '')
    return context.lower()

def load_csv(path, dictionary, number, length):
    fp = open(path)
    line = fp.readline()
    assert(line == 'word, tf, idf\n')
    line = fp.readline()
   
    #number *= 200
    while line:
        element = line.split(',')


        if element[0] in black_list:
            line = fp.readline()
            continue

        dictionary[element[0]] = {'tf': (float(element[1]) / length) + b, 'idf': math.log(number / (float(element[2]) + 1), 2) }
        if element[0] not in total_dict:
            total_dict[element[0]] = {'tf': float(element[1]), 'idf': float(element[2]) }
        else:
            total_dict[element[0]]['tf'] += float(element[1])
            total_dict[element[0]]['idf'] += float(element[2])

        line = fp.readline()
    fp.close()

def print_result(score):
    total_score = 0
    letter = 6
    score['medium'] *= math.log(2)
    score['professional'] *= math.log(4)
    score['native'] *= math.log(10)
    for key in score:
        total_score += score[key]
    
    
    print('|======= English Level =======|')
    print('|                             |')
    print('|  beginner:    ', str(round(100*score['beginner']/total_score, letter)).zfill(9) , '%  |')
    print('|  medium:      ', str(round(100*score['medium']/total_score, letter)).zfill(9) , '%  |')
    print('|  professional:', str(round(100*score['professional']/total_score, letter)).zfill(9) , '%  |')
    print('|  native:      ', str(round(100*score['native']/total_score, letter)).zfill(9) , '%  |')
    print('|                             |')
    print('|=============================|')


def make_total_dict(dictionary):
    for key in dictionary:
        dictionary[key]['idf'] = math.log(essay_num / (dictionary[key]['idf'] + 1), 2)
        dictionary[key]['tf'] /= total_len 
        dictionary[key]['tf'] += b

def uni_score(context):
    
    score_list = {'beginner': 0, 'medium': 0, 'professional': 0, 'native': 0 }
    for word in context:
        if word in total_dict:
            tf = total_dict[word]['tf']
            idf = total_dict[word]['idf']
            if word in beginner_dict:
                #score_list['beginner'] += tf * idf * beginner_dict[word]['tf'] * beginner_dict[word]['idf']
                score_list['beginner'] += tf * idf * beginner_dict[word]['tf'] * idf
            else:
                score_list['beginner'] += tf * idf * b * idf
            
            if word in medium_dict:
                #score_list['medium'] += tf * idf * medium_dict[word]['tf'] * medium_dict[word]['idf']
                score_list['medium'] += tf * idf * medium_dict[word]['tf'] * idf
            else:
                score_list['medium'] += tf * idf * b * idf
            
            if word in professional_dict:
                #score_list['professional'] += tf * idf * professional_dict[word]['tf'] * professional_dict[word]['idf']
                score_list['professional'] += tf * idf * professional_dict[word]['tf'] * idf
            else:
                score_list['professional'] += tf * idf * b * idf
            
            if word in native_dict:
                #score_list['native'] += tf * idf * native_dict[word]['tf'] * native_dict[word]['idf']
                score_list['native'] += tf * idf * native_dict[word]['tf'] * idf
            else:
                score_list['native'] += tf * idf * b * idf
    
    return score_list 

def bi_score(context):
    
    score_list = {'beginner': 0, 'medium': 0, 'professional': 0, 'native': 0 }
    for index, word in enumerate(context):
        if index == len(context) - 1:
            break
        word = word + ' ' + context[index + 1]
        if word in total_dict:
            tf = total_dict[word]['tf']
            idf = total_dict[word]['idf']
            if word in beginner_dict:
                #score_list['beginner'] += tf * idf * beginner_dict[word]['tf'] * beginner_dict[word]['idf']
                score_list['beginner'] += tf * idf * beginner_dict[word]['tf'] * idf
            else:
                score_list['beginner'] += tf * idf * b * idf
            
            if word in medium_dict:
                #score_list['medium'] += tf * idf * medium_dict[word]['tf'] * medium_dict[word]['idf']
                score_list['medium'] += tf * idf * medium_dict[word]['tf'] * idf
            else:
                score_list['medium'] += tf * idf * b * idf
            
            if word in professional_dict:
                #score_list['professional'] += tf * idf * professional_dict[word]['tf'] * professional_dict[word]['idf']
                score_list['professional'] += tf * idf * professional_dict[word]['tf'] * idf
            else:
                score_list['professional'] += tf * idf * b * idf
            
            if word in native_dict:
                #score_list['native'] += tf * idf * native_dict[word]['tf'] * native_dict[word]['idf']
                score_list['native'] += tf * idf * native_dict[word]['tf'] * idf
            else:
                score_list['native'] += tf * idf * b * idf
    
    return score_list 

def predict(path, dictionary):
    fp = open(path)
    context = fp.read()
    context = clean_str(context)
    context = context.split()
    uni = uni_score(context)
    bi = bi_score(context)
    score = {}
    for key in uni:
        score[key] = uni[key] + bi[key] * 10
    print_result(score)

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
    predict('query.txt', total_dict)

    #print(native_dict)

if __name__ == '__main__':
    main()

