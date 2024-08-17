def old_man(n):
    print(n, '→', end=' ')

    if n == 1:
        return '4 → …'
    elif n % 2 == 0:
        return old_man(n // 2)
    else:
        return old_man(3 * n + 1)


print(old_man(2023))
