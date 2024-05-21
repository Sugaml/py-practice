


def add(*args):
    sum=0
    for n in args:
        sum+=n
    return sum

v=add(1,23,23)
print("value ",v)


def Welcome(message,to):
    print(f"{message} {to}")

Welcome(message="Welcome to", to="SOMTU") 