
def ft_filter(func, iterable):
    """
    filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
    """
    if (func is None):
        return iterable
    return [i for i in iterable if func(i)]


# # To Test
# def f(x):
#     return x > 1
# a = ft_filter(f, [1, 2 , 3])

# for i in a:
#     print(i)
