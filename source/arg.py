def mydec(function):
    print("i am here in mydec")
    def wrappera(*args,**kwargs):
       return function(*args,**kwargs)
    print("i am dec")
    return wrappera
@mydec
def hello(person):
    print(f"hello world {person}")

print(hello("mike"))