def test01(f):
    def wraps(*args,**kwargs):
        print("test001 start ...")
        ret = f(*args, **kwargs)
        print("test001 end ...")
        return ret
    return wraps


def test02(f):
    def wraps(*args, **kwargs):
        print("test002 start ...")
        ret = f(*args, **kwargs)
        print("test002 end ...")
        return ret
    return wraps

@test02
@test01
def hello001():
    print("hello001")


if __name__ == "__main__":
    hello001()
