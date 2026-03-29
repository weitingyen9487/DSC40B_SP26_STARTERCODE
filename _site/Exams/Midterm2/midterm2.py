# map:


def pizza_total(quant, prices):
    """
    >>> q = [10, 5, 1]
    >>> p = [5, 2, 10]
    >>> pizza_total(p, q)
    70
    """
    result = sum(list(map(lambda x, y: x*y, quant, prices)))
    return result



def topings_total(all_top, want):
    """
    >>> all_top = [(2, "cheese"), (5, "salami"), (3, "tomatos")]
    >>> want = ["cheese", "salami"]
    >>> topings_total(all_top, want)
    7
    """

    can_have = filter(lambda w: w[1] in want, all_top)
    cheep = map(lambda c: c[0], can_have)
    print(sum(cheep))

#all_top = [(2, "cheese"), (5, "salami"), (3, "tomatos")]
#want = ["cheese", "salami"]
#topings_total(all_top, want)

def func1(a, f):
    a = 20
    return f(a) + f(a, a*2)

def func2(a, b=10):
    return a + b

#print(func1(30, func2))


def div(a, b):
    """
    >>> div(10, 4)
    2
    >>> div(10, 10)
    1
    >>> div(4, 10)
    0
    """
    if a < b:
        return 0
    else:
        return 1 + div(a-b, b)




def magic (lst1, lst2):
    print(lst1, lst2)
    if len(lst1) == len(lst2):
        print("done")
    else:
        if lst1[0] > lst2[-1]:
            magic(lst1[1:], lst2)
        elif lst1[-1] < lst2[0]:
            magic(lst1, lst2[1:])
        else:
            magic(lst1[1:-1], lst2[1:-1])

magic([3, 2, -5, 6], [-2, -3, 4])




# nested function 


def pizza_price(base_prices, topping_price):
    """
    >>> base_prices = {'small': 10, 'medium': 12, 'large': 15}
    >>> topping_price = 2.0
    >>> pizza_price(base_prices, topping_price)('small', 1)
    13.2
    >>> pizza_price(base_prices, topping_price)('large', 10)
    38.5
    >>> pizza_price(base_prices, topping_price)('tiny', 4)
    0
    """
    
    def inner(size, topping_num):
        if size not in base_prices:
            return 0
        base_price = base_prices[size]
        topping_cost = topping_price * topping_num
        total_price = base_price + topping_cost
        return total_price + total_price*0.1
    return inner



# kwarg:

def func(*args, **kwargs):
    """
    >>> func("cheese", "salami", cheese = (10, 0.1), tomatoes = (20, 0.2))
    9.0
    """
    price = 0
    for key, value in kwargs.items():
        if key in args:
            price += value[0]-value[0]*value[1]
    return price

# bonus

def bonus(lst):
    """
    >>> bonus([1])
    [[1]]
    >>> bonus([1, 2])
    [[1, [2]]]
    >>> bonus([1,2,3])
    [[1, [2, [3]]]]
    """
    if len(lst) == 0:
        return []
    return [[lst[0]]+bonus(lst[1:])]





