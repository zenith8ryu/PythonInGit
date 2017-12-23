class logger(object):
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        print("decor starts.")
        self._func(*args, **kwargs)
        print("decor starts.")


@logger
def food(name="ramen", favor="salty", price=None):
    print("Give me a %s %s, with %s." % (favor, name, price))


food("noddle", "soy sauce", "2$")