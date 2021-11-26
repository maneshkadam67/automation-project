# def arm(num):
#     order=len(str(num))#len
#     copy_n=num
#     sum=0
#     while(num!=0):
#         digit=num % 10
#         sum+=digit**order
#         num= num//10
#     if(copy_n==sum):
#         print("arm number")
# arm(162)
#--------------------------------------------swap

# #newList = [12, 35, 9, 56, 24]
# def swapList(newList):
#     size=len(newList)
#     temp=newList[0]
#     newList[0]=newList[size-1]
#     newList[size-1]=temp
#     return newList
#
# newList = [12, 35, 9, 56, 24]
# print(swapList(newList))
#------------------------position change----------------
# def swapPosition(list,pos1,pos2):
#     list[pos1],list[pos2]=list[pos2],list[pos1]
#     return list
#
# list=[12, 35, 9, 56, 24]
# swapPosition(list,1,3)
# print(list)
#------------------poping element from list--------------
#
# def swapPosition(list,pos1,pos2):
#     first_ele=list.pop(pos1)
#     second_ele=list.pop(pos2-1)
#     return list
#
# list=[12, 35, 9, 56, 24]
# swapPosition(list,1,2)
#--------------------------array sum
# arr1=[1,2,3,4,5]
# arr2=[11,22,33,44,55]
# print(sum(arr1))
# arr2=arr1.reverse()
# print(arr1[1:])

#-------------------thislist = ["apple", "banana", "cherry"]--------------------------
# thislist = ["apple", "banana", "cherry","sdsdsd","dasdasdd"]
# lis=[1,2,3,4,5]
# thislist.append(lis)
# print(thislist)
# i=0
# while(i<len(thislist)):
#     print(thislist[i])
#     i+=1
#--------------------------------------------list--------------------\
#fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist=[x for x in fruits if 'a' in x]
#l1=fruits.sort()
#print(l1)
# print(newlist)
#-------------------for-------
# class a:
#     def add(self):
#         print("class a add")
# class b:
#     def add(self):
#         print("class b add")
#
# class c(a,b):
#     def add2(self):
#         print("class c add")
# obj= c()
# obj.add()
#------------------------------Element present-----------------------
import math
from collections import Counter

# class elePresent:
#     def __init__(self):
#         list=[1,2,6,8,9,0,8,9,0]
#         for i in list:
#             print("count of ",i,"is",list.count(i))
#
# obj=elePresent()

####---------------------
# class sum:
#     def __init__(self):
#         list =[12, 67, 98, 34]
#         sum=0
#         for i in list:
#             temp=i % 10
#             temp1=i//10
#             sum=temp+temp1
#             print("sum of ",i,"digit is",sum)
# obj=sum()
#--------------array---------------------------
# class arraySum:
#     def __init__(self):
#         str="malayalam"
#         w=""
#         for i in range((len(str)/2)+1):
#             w=i + w
#         print(w)
#         if w==str:
#             print(str,"is palindrome")
#         else:
#             print("no palindrome")
#
# maxnum=obj=arraySum()

class substring:
    def __init__(self):
        pass
    def isSubstring(self):
        test_dict = {'gfg': [5, 6, 7, 8],
                     'is': [10, 11, 7, 5],
                     'best': [6, 12, 10, 8],
                     'for': [1, 2, 5]}
        print(test_dict.keys())
obj=substring()
obj.isSubstring()
