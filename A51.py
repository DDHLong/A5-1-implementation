def shift(arg, new):
    arg.insert(0, new)
    arg.pop()
    return arg


def get_majority(x, y, z):
    if(x + y + z > 1):
        return 1
    else:
        return 0

def str_to_list(S):
    return [int(c) for c in S]

def gen_key(X, Y, Z, n = 10):
    X = str_to_list(X)
    Y = str_to_list(Y)
    Z = str_to_list(Z)

    key = ''
    for i in range(n):
        key = key + str(X[18] ^ Y[21] ^ Z[22])
        m = get_majority(X[8], Y[10], Z[10])
        if m == X[8]:
            new_X = X[13] ^ X[16] ^ X[17] ^ X[18]
            j = 1
            shift(X, new_X)

        if m == Y[10]:
            new_Y = Y[20] ^ Y[21]
            k = 1
            shift(Y, new_Y)

        if m == Z[10]:
            new_Z = Z[7] ^ Z[20] ^ Z[21] ^ Z[22]
            n = 1
            shift(Z, new_Z)

    return key

if __name__ == "__main__":
    X = '1111101010101010101'
    Y = '1100110011001100110011'
    Z = '11100001111000011110000'
    print(gen_key(X, Y, Z))