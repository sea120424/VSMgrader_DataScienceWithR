import os

def clean_str(context):
    context = context.replace('.', ' ')
    context = context.replace(',', ' ')
    context = context.replace('\\', ' ')
    context = context.replace('%', ' ')
    context = context.replace("'", '')
    context = context.replace(')', ' ')
    context = context.replace('(', ' ')
    context = context.replace(';', ' ')
    context = context.replace(':', ' ')
    context = context.replace('!', ' ')
    context = context.replace('/', ' ')
    context = context.replace('"', ' ')
    context = context.replace('?', ' ')
    return context

def save_uni(dictionary, context):
    idf_dict = {}
    for word in context:
        if word not in dictionary:
            dictionary[word] = {'tf': 1, 'idf': 1}
            idf_dict[word] = True
        else:
            dictionary[word]['tf'] += 1 
            if word not in idf_dict:
                idf_dict[word] = True
                dictionary[word]['idf'] += 1

def save_bi(dictionary, context):
    idf_dict = {}
    for index, word in enumerate(context):
        if index == len(context) - 1:
            break
        words = word + ' ' + context[index + 1]
        if words not in dictionary:
            dictionary[words] = {'tf': 1, 'idf': 1}
            idf_dict[words] = True
        else:
            dictionary[words]['tf'] += 1
            if words not in idf_dict:
                idf_dict[words] = True
                dictionary[words]['idf'] += 1


def handle_level(path, dictionary):
    essay_num = 0
    length = 0
    for i in os.listdir(path):
        if i[0] == '.':
            continue
        essay_num += 1
        file_name = path + '/' + i
        fp = open(file_name)
        context = fp.read()
        fp.close()
        context = clean_str(context)
        context = context.split()
        length += len(context)
        save_uni(dictionary, context)
        save_bi(dictionary, context)
    return essay_num, length

def print_header(fp):
    fp.write('word, tf, idf\n')

def write2csv(dictionary, target):
    fp = open(target, 'w')
    print_header(fp)
    for key in dictionary:
        new_line = key.lower() + ', ' + str(dictionary[key]['tf']) + ', ' + str(dictionary[key]['idf']) + '\n'
        fp.write(new_line)

    fp.close()

def main():
    beginner = 'data/beginner'
    native = 'data/native'
    professional = 'data/professional'
    medium = 'data/medium'
    beginner_dict = {}
    native_dict = {}
    professional_dict = {}
    medium_dict = {}
    beginner_num, beginner_length = handle_level(beginner, beginner_dict)
    native_num, native_length = handle_level(native, native_dict)
    medium_num, medium_length = handle_level(medium, medium_dict)
    professional_num, professional_length = handle_level(professional, professional_dict)
    essay_num = beginner_num + native_num + medium_num + professional_num
    
    write2csv(beginner_dict, 'data/dictionary/beginner.csv')
    write2csv(medium_dict, 'data/dictionary/medium.csv')
    write2csv(native_dict, 'data/dictionary/native.csv')
    write2csv(professional_dict, 'data/dictionary/professional.csv')
    print(beginner_num, 'beginner essays totally and length is ', beginner_length)
    print(native_num, 'native_essays totally and length is ', native_length)
    print(medium_num, 'medium essays totally and length is ', medium_length)
    print(professional_num, 'professional essays totally and length is ', professional_length)
    print(essay_num, 'essays totally')

if __name__ == '__main__':
    main()

