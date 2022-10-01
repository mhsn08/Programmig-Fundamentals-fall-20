### YOUR CODE FOR openLocks() FUNCTION GOES HERE ###

def openLocks(number_of_lockers,number_of_students):
    if number_of_lockers<0 or number_of_students<0:
        return None
    if number_of_lockers == 0 or number_of_students==0:
        return 0
    else:
        a = [False]*number_of_lockers
        for i in range (1,number_of_students+1):
            for j in range (1,number_of_lockers+1):
                if j%i==0:
                    a[j-1]=not a[j-1]
        b = a.count(True)
        return b

#### End OF MARKER





### YOUR CODE FOR mostTouchableLocker() FUNCTION GOES HERE ###


def most_factors(x):
    guess = 2                                                        
    counter = 1
    while guess<=x:
        if x%guess==0:
            counter = counter +1
            guess = guess+1
        else :
            guess = guess+1
    return counter

def most_factors_Lim(x,y):
    guess = 2                                                        
    counter = 1
    while guess<=y:
        if x%guess==0:
            counter = counter +1
            guess = guess+1
        else :
            guess = guess+1
    return counter


def mostTouchableLocker(number_of_lockers,number_of_students):
    if number_of_lockers<0 or number_of_students<0:
        return None
    if number_of_lockers == 0 or number_of_students==0:
        return 0
    else:
        a = []
        b = []
        for i in range (1,number_of_lockers+1):
            a.append(i)
        for j in range(number_of_lockers):
            if j>number_of_students:
                c = most_factors_Lim(a[j],number_of_students)
                b.append(c)
            else:
                c = most_factors(a[j])
                b.append(c)
        max_value=max(b)
        c = [i for i, j in enumerate(b) if j == max_value]
        d = c[-1]
        return d+1
#### End OF MARKER


