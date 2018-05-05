import functools

# 装饰器版本1：
def positive_result(function):
    def wrapper(*args,**kwargs):
        result=function(*args,**kwargs)
        assert result>=0,function.__name__+"() result isn't>=0"
        return result
    wrapper.__name__=function.__name__
    wrapper.__doc__=function.__doc__
    return wrapper

# 装饰器版本2：
def positive_result(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        assert result >= 0, function.__name__ + "() result isn't>=0"
        return result
    return wrapper

@positive_result
def discriminant(a,b,c):
    return (b**2)-(4*a*c)

discriminant(3,6,1)

'''
带参数的装饰器
需要在装饰器函数外层再套一层函数（带传入的参数），
并最外侧的函数再将装饰器函数返回
'''
def bounded(min,max):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            result=func(*args,**kwargs)
            if result<min:
                return min
            elif result>max:
                return max
            return max
        return wrapper
    return decorator


@bounded(0,100)
def percent(amount,total):
    return (amount/total)*100

print(percent(1000,2))