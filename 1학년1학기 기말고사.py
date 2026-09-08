def function1(a,b):#ok
    return a**b

def function2(*a): #ok
    L= []
    for i in a:
            if type(i)==int:
                L.append(i)
    if len(L)==0:
        return 0
    else:
        return sum(L)

def function3(a,b):#ok
    if len(a)!=len(b):
        return False
    if a.lower()==b.lower():
        return True
    count = 0
    for i in range(len(a)):
        if a[i].lower()!=b[i].lower():
            count +=1
    if count >=2:
        return False
    else:
        return True
    

def function4(a,b):#ok
    s = set()
    for i in a:
        if b in i:
            s.add(i)
    return s


def function5(a):#ok
    L = []
    n = 2
    while len(L)<=a:
        
        count = 0
        for i in range(1,n+1):
            if n%i == 0:
                count +=1
        if count ==2:
            L.append(n)
        n +=1
    return L[a-1]



def function6(a):#ok
    s = ''
    for i in a:
        if i.isdigit():
            s += i
        else:
            s +=' '
    L =s.split()
    k = 0
    for i in range(len(L)):
        k += int(L[i])
    return k




class Digit:#ok
    def __init__(self,number):
        self.number = number

    def __add__(self, other):
        return self.number + other.number

class Decoder:#ok

    @staticmethod
    def converter(self):
        s =""
        for i in range(0,len(self),2):
            s +=self[i]*int(self[i+1])
        return s

'''
class Singer:
    def __init__(self, name):
        self.name = name


class Group:
    def __init__(self):
        self.members = set()

    
    def add_member(self,*other):
            self.members = self.members.union(list(other))
        
    def remove_member(self,*other):
        self.members = self.members -(set((other)))

    
    def get_member_names(self):
        return self.members
'''

class Triangle:#OK
    def __init__(self,L):
        self.L = L



    def get_perimeter(self):
        return self.L *3


    def __eq__(self,other):
        if self.L == other.L:
            return True
        else:
            return False
        '''두 정삼각형 인스턴스를 비교해서 변의 길이가 서로 같으면 True 리턴, 
           길이가 서로 다르면 False 리턴'''


    def __gt__(self,other):
        if self.L>other.L:
            return True
        else:
            return False
        '''두 정삼각형 인스턴스를 비교해서 왼쪽 인스턴스의 변 길이가 더 크면 True,
           그렇지 않으면 False 리턴'''


    def __lt__(self,other):
        if self.L<other.L:
            return True
        else:
            return False
        

class Beer:
    alcohol = 4.5  # 알콜 도수

    def __init__(self):
        pass
        
 
    @classmethod
    def set_alcohol(self,num):
        self.alcohol = num
        


class Cass(Beer):
    """Do not edit this class"""
    pass


class Terra(Beer):
    """Do not edit this class"""
    pass

    




