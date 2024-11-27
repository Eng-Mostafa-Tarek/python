def hello(x: str, y: str) -> str:
    """
    hello fun take x,y
    """
    return f"hello{x}{y}"


print(hello.__annotations__)
print(hello.__doc__)
print(help(hello))
