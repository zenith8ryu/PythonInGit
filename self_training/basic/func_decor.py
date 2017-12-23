def logger(level):
    def decor(func):
        def wrapper(*args, **kwargs):
            if level == "warning":
                print("[warning]%s starts." % func.__name__)
            elif level == "info":
                print("[info]%s starts." % func.__name__)
            return func(*args)

        return wrapper

    return decor


# @logger(level="info")
@logger(level="warning")
def food(name, favor="soy sauce", price="1$"):
    print("Give me a %s %s, about %s" % (favor, name, price))


food("ramen", "salty", "2$")
