def make_tuple(a, b ,c):
    return (a, b,c)


def reverse_tuple(a_sequence):
    a_sequence.sort(reverse=True)
    return tuple(a_sequence)

def make_list(a,b,c):
    return [a,b,c]

def nth_list(a_sequence,n):
    a=[]
    for i in range(0,len(a_sequence)-1):
        if i%n==0:
            a.append(a_sequence[i+1])
    return a

def splice(a_list,b_list):
    for i in b_list:
        a_list.append(i)


def main():
    print(make_tuple(1,2,3))
    print(reverse_tuple([1,2,3,4]))
    print(make_list("a","b","c"))
    print(nth_list(range(1,11),2))
    print(nth_list("Chidera is a girl",2))
    print(nth_list((1,"chidera", True, 99),2))
    a_list=[1,2]
    b_list=["a","b"]
    print(a_list)
    splice(a_list,b_list)
    print(a_list)

if __name__=="__main__":
    main()
