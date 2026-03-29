def escape(dragon, height, power):
    if dragon and height and power//height:
        return success([dragon, height, power])
    if height and not power:
        print(success([dragon, height, power+5]))
    elif dragon or power:
        success([dragon, 0, power])
    else:
        return False

def success(lst):
    print(lst)
    return sum(lst)



escape(0, 0 , 10)





def f1(num1):
    param = num1 * 2
    
    def f2(num2):
        r = param + num2
        print(r, num2)
        
    f2(10)
#f1(2)



def f1(w1):
    def f2(w2):
        return lambda x: w2 + ' ' + w1 + ' go'
    return f2


#print(f1('it')('Let')(3))


def test(i, j):
    if i > j:
        return j
    else:
        print('*'*i)
        return test(i+1, j-1)

#print(test(3, 6))


def once_upon_a_december(n):
    nums = range(n)
    k = 0
    for i in range(n+2):
        for j in range(1000 * n):
            while k < j:
                k += 5


def be_our_guest(lst):  
        for i in (n*len(n)):
            my_length = len(i)


def interesting_question(n):
    i = 0
    j = n
    while i < n:
        print(j)
        if (i > j):
            i = i//2
        i+=1
        j-=1


def cost(number, *colors, **costs):
    filtered = list(filter(lambda c: c in costs.keys(), colors))
    mapped = sum(map(lambda n: costs[n]*number, filtered))
    print(mapped)


#cost(2, "red", "blue", red=20, blue = 20)

def dance(lst1, lst2):
    """
    >>> dance(["A", "B", "C"], ["E", "F", "G"])
    ['A dances with E', 'B dances with F', 'C dances with G']

    >>> dance(["A", "B", "C"], ["E", "F", "G", "H"])
    ['A dances with E', 'B dances with F', 'C dances with G', 'no partner availalbe']

    >>> dance(["A", "B"], ["E", "F", "G"])
    ['A dances with E', 'B dances with F', 'no partner availalbe']
    """
    if len(lst1)==0 and len(lst2)>0 or len(lst2)==0 and len(lst1)>0:
        return ["no partner availalbe"]
    elif len(lst1) == 0 and len(lst2)==0:
        return []
    else:
        return [lst1[0]+ " dances with " +lst2[0]] + dance(lst1[1:], lst2[1:])

#print(dance(["A", "B"], ["E", "F", "G"]))


lst1 = [10, 5, 30, 40]
lst2 = [3, 10, 5]

def magic(this, that):
    if len(this) == len(that):
        return  "this[0]"

    if this[0] == that[-1]:
        return magic(that[1:], this[1:-1]) + str(that[0])

    elif this[0] < that[-1]:
        return magic(that[:-1], this[:-1]) + str(that[0])

    else:
        return magic(that[1:], this[:-1]) + str(that[0])

#print(magic(lst1, lst2))

#print(len(lst2))



#lst = ['bulbasaur', '', 'squirtle', 'charmander', '']
#print(list(filter(print, filter(len,lst))))


lst = ["My", "old", "friend", ",", "this", "song", "is", "for", "you"]
it = iter(lst)

for i in range(5):
    next(it)

#print(list(it))




friends = ['Moana', '', 'Elsa', 'Cinderella', '']
#print(list(filter(print, filter(len,friends))))

# part 3:
'''d = {1:"1", 2:"2"}
try:
    print(d[3])
    print("done")
except: '''




def f(n):
    if n<0:
        raise TypeError("bad parameter")
    return f(n-1) + n/0


#f(2)


class Castle:
    def __init__(self, room_num, defenses, owner):
        self.room_num = room_num
        self.defenses = defenses
        self.owner = owner
    
    def __str__(self):
        return f'This is {self.owner}\'s castle'

    def __repr__(self):
        return f'It is protected.'
    
    def host_royal_event(self):
        return "Come to our ball every Friday night at 10PM."

class Fortress(Castle):
    warning = 'This is a Fortress.'

    def __init__(self, defenses, owner):
        self.defenses = defenses
        self.owner = owner
        self.bridge_raised = False
        self.__str__ = lambda: f'This Fortress guards {self.owner}'
    
    def raiseDrawbridge():
        return 'Bridge was raised'
        
class Tower(Castle):
    warning = 'Do not climb'
    
    def __init__(self, owner):
        self.height = 1000


f1 = Castle(515, 2000, 'Belle')
f2 = Fortress(5000, 'Elsa')
f3 = Tower('Rapunzel')


#print(f2.owner, f2.room_num)
#print(f1.warning)
#print(f3.warning)
#print(f1.host_royal_event())
#print(str(f2))
print(f3)
#print(Fortress.raiseDrawbridge())



#func = lambda x: lambda: lambda y: "bye bye"

#print(t(1)()(5))

class Kingdom:
    """
    >>> Kingdom.population
    0
    >>> person1 = Kingdom("Moana", 80)
    >>> person2 = Kingdom("Belle", 65)
    >>> Kingdom.population
    2
    >>> person1.kingdom
    'Javania'
    >>> person2.kingdom
    'Pythonia'

    >>> print(person1)
    My grade is 80, I move to Javania.
    >>> print(person2)
    My name is Belle, I stay in Pythonia.

    >>> person1 < person2
    False

    >>> new_person = person1 + person2
    >>> print(new_person)
    We are from different kingdoms.
    
    >>> person3 = Kingdom('Shrek', 90)
    >>> new_person = person1 + person3

    >>> new_person.name
    'new_team'
    >>> new_person.grade
    85
    >>> new_person.kingdom
    'Javania'

    """
    population = 0

    def __init__(self, name, grade):
        self.grade = grade
        self.name = name
        if self.grade >=70:
            self.kingdom = "Javania"
        else:
            self.kingdom = "Pythonia"
        Kingdom.population+=1

    def get_population():
        return Kingdom.population

    def __repr__(self):
        if self.grade<70:
            return f'My name is {self.name}, I stay in Pythonia.'
        else:
            return f'My grade is {self.grade}, I move to Javania.'
      

    def __add__(tt, other):
        if tt.kingdom == other.kingdom:
            return Kingdom("new_team", (tt.grade+other.grade)//2)
        else:
            return "We are from different kingdoms."

    def __lt__(self, other):
        if self.name < other.name:
            return True
        else:
            return False




