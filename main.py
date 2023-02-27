import webbrowser


def validatior(func):
    def wrapper(args):
        print("before")
        func(args)
        print("after")
    return wrapper

@validatior
def open_url(url):
    webbrowser.open(url)


open_url("http://google.com")