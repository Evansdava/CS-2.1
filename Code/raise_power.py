#!python


def raise_power(num, pow):
    """Raise the number to the given power"""
    # Negative powers are 1 over the positive version
    if pow < 0:
        result = raise_power(num, -pow)
        return 1 / result

    # Base cases
    if pow == 0:
        return 1
    if pow == 1:
        return num

    # Recurse and multiply until reaching 1
    return num * raise_power(num, pow - 1)


if __name__ == '__main__':
    # Test base cases
    assert raise_power(2, 0) == 1
    assert raise_power(4, 0) == 1
    assert raise_power(2, 1) == 2
    assert raise_power(4, 1) == 4
    print("Base cases successful")

    # Test expected inputs
    assert raise_power(2, 2) == 4
    assert raise_power(2, 3) == 8
    assert raise_power(2, 4) == 16
    assert raise_power(2, 5) == 32
    assert raise_power(2, 7) == 128
    assert raise_power(2, 10) == 1024
    assert raise_power(3, 2) == 9
    assert raise_power(3, 4) == 81
    assert raise_power(4, 2) == 16
    assert raise_power(4, 3) == 64
    assert raise_power(10, 5) == 100000
    print("Positive powers successful")

    # Test negatives
    assert raise_power(3, -2) == 1 / 9
    assert raise_power(3, -4) == 1 / 81
    assert raise_power(4, -2) == 1 / 16
    assert raise_power(4, -3) == 1 / 64
    assert raise_power(10, -5) == 1 / 100000
    print("Negative powers successful")
