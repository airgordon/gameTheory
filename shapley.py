import math


def _to_permut(k, lst):
    m_list = lst.copy()
    res = []
    while m_list:
        d = len(m_list)
        (k, r) = divmod(k, d)
        item = m_list[r]
        m_list.remove(item)
        res.append(item)

    return res


def _k(lst, item):
    idx = lst.index(item)
    return lst[:idx]


def _k_p(lst, item):
    idx = lst.index(item)
    return lst[:idx + 1]


def shapley_value(players, value_f, important_players=None):
    if important_players is None:
        important_players = players

    if important_players.__class__.__name__ == "list":
        return list(map(lambda p: _shapley_value(players, value_f, p), important_players))
    else:
        return _shapley_value(players, value_f, important_players)


def _shapley_value(players, value_f, player):
    acc = 0
    n = math.factorial(len(players))

    for i in range(0, n):

        p = _to_permut(i, players)

        k1 = set(_k(p, player))
        k2 = set(_k_p(p, player))

        inc = value_f(k2) - value_f(k1)

        # if inc < 0:
        #     raise Exception()

        acc = acc + inc

    return acc / n
