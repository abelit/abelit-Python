class Middleware(object):
    def __init__(self,func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Before Request ...")
        ret = self.func(*args, **kwargs)
        print("After Request ...")

        return ret

@Middleware
def hello(name):
    print("hello")
    print(name)
    return "hello"

if __name__ == "__main__":
    hello("world")