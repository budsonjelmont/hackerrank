# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple

if __name__=='__main__':
    n = int(input())
    header = input().split()   
    scoresum = 0
    Student=namedtuple('Student',header)
    for i in range(0,n):
        s = input().split()
        student = Student(s[0],s[1],s[2],s[3])
        scoresum+=int(student.MARKS)
    print(scoresum / n)
