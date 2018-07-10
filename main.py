from shapley import shapley_value


def gnomes_v(pls):
    return divmod(len(pls), 2)[0]


def business_v(pls):
    return landlord(pls, lambda x: x)


def landlord(pls, f):
    x = len(pls) - 1

    if 1 in pls:
        return f(x)
    else:
        return 0


def landlord_sq(lst):
    return landlord(lst, lambda x: x * x)


def socks_v(pls):
    if len(pls) >= 2:
        return 1
    else:
        return 0


def shoes_v(pls):
    if 1 in pls and len(pls) >= 2:
        return 1
    else:
        return 0


def shoes_mn_v(pls):
    ll = len([None for x in pls if x < 0])
    rr = len([None for x in pls if x > 0])
    return min(ll, rr)


def road(pls):
    return -max(pls, default=0)


def pipes(pls):
    if pls == {1, 2}:
        return 4
    elif pls == {1, 3}:
        return 1
    elif pls == {1, 2, 3}:
        return 4

    return 0


players = [-3, -2, -1, 1, 2, 3, 4, 5]
v = shoes_mn_v
vect = shapley_value(players, v, [players[0], players[-1]])

print(vect)
print(sum(vect))
print(vect[0] / v(set(players)))
