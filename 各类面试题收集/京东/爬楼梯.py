
import functools
import time

total_time=0
# def user_timer(totaltime):
#     def decorator(func):
#         def wrapper(*args,**kwargs):
#             # 记录进入时间
#             start_time=time.time()
#             # print(start_time)
#             result=func(*args,**kwargs)
#             #记录执行完方法的时间
#             # print(time.time())
#             end_time=time.time()-start_time
#             new_total= totaltime+end_time
#             # totaltime+=end_time
#             print(end_time)
#             return result
#         return wrapper


# def my_time():
#     print(total_time)

def user_timer(func):
    def wrapper(*args,**kwargs):
        # 记录进入时间
        start_time=time.time()
        # print(start_time)
        result=func(*args,**kwargs)
        #记录执行完方法的时间
        # print(time.time())
        end_time=time.time()-start_time
        # now_time=total_time
        global total_time
        now_time = total_time
        total_time=now_time+end_time
        print(end_time)
        return result
    return wrapper

@user_timer
# @functools.lru_cache(maxsize=64)
def climbStairs2(n):
    first3={1:1,2:2,3:4}
    print('当前N为%s'%n)
    if n in first3.keys():
        return first3[n]
    else:
        return climbStairs2(n-1)+climbStairs2(n-2)+climbStairs2(n-3)

n=25
climbStairs2(n)