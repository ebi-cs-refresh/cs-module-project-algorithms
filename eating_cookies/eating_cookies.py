'''
Input: an integer
Returns: an integer
'''
# cache = {}

# {
#     n: nth-fib(n)
#     n-1:nt-fib(n-1)
# }


# def eating_cookiesInCache(n, cache=None):

#     # Your code here
#     # pass

#     if n < 2:
#         return n
#     elif n in cache:
#         return cache[n]
#     else:
#         cache[n] = eating_cookiesInCache(
#             n-1, cache)+eating_cookiesInCache(n-2, cache)+eating_cookiesInCache(n-3, cache)
#         return cache[n]


def eating_cookies(n, cache=None):
    # Your code here
    if n < 0:
        return 0
    if n == 0:
        return 1

    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    cache[n] = eating_cookies(n-1)+eating_cookies(n-2)+eating_cookies(n-3)
    return cache[n]


ca = {}


def eat_cook(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n in ca:
        return ca[n]
    else:
        ca[n] = eat_cook(n-1)+eat_cook(n-1)+eat_cook(n-3)
    return ca[n]


c = {}


def e_c(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n in c:
        return c[n]
    else:
        c[n] = e_c(n-1)+e_c(n-2)+e_c(n-3)
    return c[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    # print(
    #     f"There are {eating_cookiesInCache(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

    print(
        f"There are {eat_cook(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

    print(
        f"There are {e_c(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
