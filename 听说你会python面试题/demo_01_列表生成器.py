
class A(object):
    x=1
    gen=(x for x in range(10))
    # gen =(lambda x:(x for _ in range(10)))(x)

if __name__=="__main__":
    print(list(A.gen))