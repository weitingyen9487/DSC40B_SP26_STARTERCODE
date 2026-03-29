def loop(song, num):

    if song or 1/0:
        if num > 5:
            print(song)
        elif num > 3:
            print(num)
        else:
            print(song[num:])

    if not song or num > 7:
        print(len(song)%num)
    else:
        return(shuffle(song, num//2))


def shuffle(song, num):
    if len(song) == num:
        return song*2
    return "shuffled"
    

#print(loop("Lalala", 2))    
#print(loop("HeyHop", 12))


def question(lst):

    while True:
        if len(lst) == 0:
            print("done!")
            break
        else:
            lst = lst[1:-1]
            for i in lst:
                print(lst[::-1])


question([1,2,3,4,5])





'''

Write a function that takes two dictionaries one with Student’s classes and the other with student’s grades, the function should write a file for each student that contains the classes and the grade student got in it.
>>> classes = {“Alice”: [“MATH 18”, “DSC 20”], “John”: [“DSC 10”, “MATH 20C]}
>>> grades = {“Alice”: [90.0, 85.5], “John”: [79.8, 98.7]}


'''



def students_info(lst):
    """
    >>> sts = [('Alice', "MATH 18", 90.0), ("John","DSC10", 79.8),\
    ('John', "MATH 20C", 98.7), ("Alice", "DSC 20", 85.5)]
    >>> students_info(sts)
    {'Alice': ['MATH 18', 'DSC 20'], 'John': ['DSC10', 'MATH 20C']}
    """
    dict1 = {}

    for tup in lst:
        if tup[0] in dict1:
            dict1[tup[0]].append(tup[1])
        else:
            dict1[tup[0]] = [tup[1]]

    return dict1


def class_file(classes, term):
    """
    >>> cl = {'Alice': ['MATH 18', 'DSC 20'], 'John': ['DSC10', 'MATH 20C']}
    >>> class_file(cl)
    """
    line = ''
    for name in classes:
        with open(name+".csv", "w") as f:
            for val in classes[name]:
                line = line + val+", "+term+"\n";
            f.write(line)
            line = ''

class_file({'Alice': ['MATH 18', 'DSC 20'], 'John': ['DSC10', 'MATH 20C']}, 'FALL24')



#EC:

def at_least_one(input_list):
    '''
    >>> lst = ["grape", "peach", "KIWI", "ppl"]
    >>> at_least_one(lst)
    ['grape', 'peach', 'kiwi']
    '''
    output_list = [word.lower().strip() for word in input_list if any(vowel in word.lower() for vowel in "aeiou")]
    return output_list


#print(output_list)



#inp = [('Alice', "MATH 18", 90.0), ("John","DSC10", 79.8),\
    #('John', "MATH 20C", 98.7), ("Alice", "DSC 20", 85.5)]

#print(students_info(inp))

lst = [1, 2, 3]

t = [[(i, j) if i > j else i for j in range (i-1)] for i in lst if i%2 == 0 or i%3==0]
#print(t)


#v2.
lst = [1, 3, 1]
t = [[(i, j) if i > j else j for j in range(i-1)] for i in lst if i%2 == 0 or i%3==0]
#print(t)





def magic_file(file_name):
    num1 = 0
    num2 = 0
    with open(file_name, "r") as f:
        for line in f:
            l = line.strip().split(", ")
            num2 = num2 + int(l[1])
            num1 = num1 + 1
        return(num2//num1)


#print(magic_file("numbers.txt"))




#2

def question(lst):

    while True:
        if len(lst) == 0:
            print("done")
            break
        else:
            lst = lst[1:-1]
            for i in lst:
                print(lst[::-1])

question([5, 3, 2, 1, 4])



