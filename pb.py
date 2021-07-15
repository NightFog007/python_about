
import time
import functools

#~ 装饰器
# 输出调用的方法运行时间
def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print('{} took {} ms'.format(func.__name__, (end - start) * 1000))
        return res
    return wrapper

    
@log_execution_time
def calculate_similarity():
    print("this is tesxjdjf")
    
