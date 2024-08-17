import itertools
from pyvis.network import Network


def modes(a, b, c, m):
    def impl(p, q):
        return (not p) or q

    if m == 0:
        return b or c, a or c, a or b
    elif m == 1:
        return b and c, a and c, a and b
    elif m == 2:
        return b or c, not (a or c), a or b
    elif m == 3:
        return b and c, not (a and c), a and b
    elif m == 4:
        return b ^ c, not (a ^ c), a ^ b
    elif m == 5:
        return impl(b, c), not impl(a, c), impl(a, b)
    elif m == 6:
        return not (b or c), not (a or c), not (a or b)
    elif m == 7:
        return not (b and c), not (a and c), not (a and b)
    elif m == 8:
        return b or c, a and c, a ^ b


def bool2str(tpl):
    st = ''
    for boolean in tpl:
        if boolean:
            st += '1'
        else:
            st += '0'

    return st


states = tuple(itertools.product([False, True], repeat=3))

for mode in range(9):
    metamorphoses = Network(directed=True)
    passed = set()

    for state in states:
        if state in passed:
            continue
        else:
            current = state

            while current:
                next = modes(current[0], current[1], current[2], mode)

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
