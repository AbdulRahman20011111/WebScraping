    # print("h")
    # a=10
    # b=30
    # k=70
    # c="rahman "
    # d="habeeb"
    # print(c.count("a"))

    # # e=str(input("enter name")) 
    # # print(e )
    # # if(e.endswith("an")==True):
    # #     print("yes")
    # # else:
    # #     print("no")


    # # if(a>b and a>k):
    # #     print(a +"is big")
    # # elif(b>k):
    # #     print(b ,"is big")
    # # else:
    # #     print(k," is big" )

    # k=[99,77]  
    # k.sort()
    # print(k)

    # k.sort(reverse=True)
    # print(k)

    # print(type(k))
    # print(len(k))


    # tup=(4,1,2,3,)
    # tup2=(2,)


    # info = {
    #     "name":"rahman",
    #     "surname":"habeeb",
    #     "hobbies":{
    #         "1":"jkj",
    #         "2":"kldsjfh"
    #     }
    # }

    # print(info["name"])


    # s={1,2,3,(2,3,4)}
    # s2={4,5,6,7}
    # s3=s.union(s2)

    # print(s3)


# l=[1,2,3,4,5,6,7,8,9]

# s=5
# count=0
# low=0
# high=len(l)-1
# while low<high:
#     mid=(low+high)//2
#     if(l[mid]==s):
#         print(True,count+1)
#     elif(s<l[mid]):
#         high=mid-1
#     else:
#         low=mid+1        


# l = [1,2,3,4,5,6,7,8,9]
# for x in l:
#     if x==10:
#         print (x)
#         break

# else:
#     print("end")    

# s = 10
# low = 0
# high = len(l) - 1

# while low <= high:
#     mid = (low + high) // 2
#     if l[mid] == s:
#         print(True, mid + 1)   # 1-based position
#         break
#     elif s < l[mid]:
#         high = mid - 1
#     else:
#         low = mid + 1
# else:
#     print(False)

# i = 1
# while i <= 6:
#     if i == 3:
#         i += 1
#         continue

#     print(i)
#     i += 1


# j=1
# while j<7:
#     if j==4:
#         j+=1
#         continue

#     print(j)
#     j+=1

# seq= range(0,20,2)

# for k in seq:
#     print(k)


# p=3
# y=1
# for x in range(1,p+1):
#     y*=x
# print(y)    

def hello ():
    print("hello")

def num(a):

    if(a%2==0):
        print("even ")
    else:
        print("odd")        

hello() 
num(57)   

def show(n):
    if n==1 or n==1:
        return 1
    else:
        return n*show(n-1)
z=show(5)   
print(z) 