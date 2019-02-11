
# https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386819879946007bbf6ad052463ab18034f0254bf355000
import time, datetime, functools
def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

def log_update(text=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if text is not None:
                print '%s, %s():' % (text, func.__name__)
            else:
                print 'call %s():' % func.__name__
            return func(*args, **kw)
        return wrapper
    return decorator

@log
def now():
    print datetime.datetime.now()

@log_update('hi')
def now1():
    print datetime.datetime.now()

@log_update()
def now2():
    print datetime.datetime.now()

if __name__ == "__main__":
    now()
    print now.__name__
    now1()
    print now1.__name__
    now2()
    print now2.__name__