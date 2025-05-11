import math


def frequency_bit_test(sequence: str) -> float:
    n = len(sequence)
    x = 0
    for i in sequence:
        match i:
            case '1':
                x += 1
            case '0':
                x += -1

    s_n = abs(x) / math.sqrt(n)
    p_value = math.erfc(s_n / math.sqrt(2))
    return p_value


def identical_consecutive_bits_test(sequence: str) -> float:
    n = len(sequence)
    zeta = sequence.count('1') / n

    if abs(zeta - 0.5) >= (2 / math.sqrt(n)):
        return 0.0
    else:
        v_n = sum(1 for i in range(n - 1) if sequence[i] != sequence[i + 1])
        p_value = math.erfc(abs(v_n - 2 * n * zeta * (1 - zeta)) / (2 * math.sqrt(2 * n) * zeta * (1 - zeta)))
        return p_value


