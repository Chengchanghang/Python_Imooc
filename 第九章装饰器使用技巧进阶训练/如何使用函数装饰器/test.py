#coding:utf-8
#1斐波那契数列问题
def fibonacci(n,cache=None):
    if cache is None:
        cache={}
    if n in cache:
        return cache[n]
    if n<=1:
        return 1
    cache[n]=fibonacci(n-1,cache)+fibonacci(n-2,cache)
    return cache[n]

def memo(func):
    cache={}
    def wrap(*args):
        if args not in cache:
            cache[args]=func(*args)
        return cache[args]
    return wrap
def fibonacci2(n):
    if n<=1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

fibonacci2=memo(fibonacci2)
print fibonacci2(50)

2#一共有十个台阶，从下走到上面，一次只能迈1-3个台阶，
#并且不能后退，走完这个楼梯共有多少种方法

@memo
def climb(n,steps):
    count=0
    if n==0:
        count=1
    elif n>0:
        for step in steps:
            count+=climb(n-step,steps)
    return count
print climb(10,(1,2,3))