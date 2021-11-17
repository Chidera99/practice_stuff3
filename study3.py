def make_tuple(a, b ,c):
    return (a, b,c)


def reverse_tuple(a_sequence):
    a_sequence.sort(reverse=True)
    return tuple(a_sequence)

def main():
    print(make_tuple(1,2,3))
    print(reverse_tuple([1,2,3,4]))

if __name__=="__main__":
    main()
