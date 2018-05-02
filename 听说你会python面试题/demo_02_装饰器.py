
import time
from functools import wraps

class Timeit(object):
    def __init__(self,func):
        self._wrapped=func

    @wraps(getattr())
    def __call__(self, *args, **kwargs):
        start_time=time.time()
        result=self._wrapped(*args,**kwargs)
        print("花费时间：%s"%(time.time()-start_time))
        return result