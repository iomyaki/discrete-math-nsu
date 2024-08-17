import itertools
from pyvis.network import Network


def modes(a, b, c, d, m):
    def impl(p, q):
        return (not p) or q

    if m == 0:
        return c or d, a or d, a or b, b or c
    elif m == 1:
        return c and d, a and d, a and b, b and c
    elif m == 2:
        return c or d, not (a or d), a or b, not (b or c)
    elif m == 3:
        return c and d, not (a and d), a and b, not (b and c)
    elif m == 4:
        return c ^ d, not (a ^ d), a ^ b, not (b ^ c)
    elif m == 5:
        return impl(c, d), not impl(a, d), impl(a, b), not impl(b, c)
    elif m == 6:
        return not (c or d), not (a or d), not (a or b), not (b or c)
    elif m == 7:
        return not (c and d), not (a and d), not (a and b), not (b and c)
    elif m == 8:
        return c or d, a and d, a ^ b, impl(b, c)


def bool2str(tpl):
    st = ''
    for boolean in tpl:
        if boolean:
            st += '1'
        else:
            st += '0'

    return st


states = tuple(itertools.product([False, True], repeat=4))

for mode in range(9):
    metamorphoses = Network(directed=True)
    passed = set()

    for state in states:
        if state in passed:
            continue
        else:
            current = state

            while current:
                next = modes(current[0], current[1], current[2], current[3], mode)

                metamorphoses.add_node(bool2str(current))
                if next != current:
                    metamorphoses.add_node(bool2str(next))
                metamorphoses.add_edge(bool2str(current), bool2str(next))

                passed.add(current)

                if next in passed:
                    break
                else:
                    current = next

    metamorphoses.show(f'mode_{mode}.html', notebook=False)
