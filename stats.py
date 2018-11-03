import numpy as np


def mean_(val, freq):
    return np.average(val, weights=freq)


def median_(val, freq):
    ord = np.argsort(val)
    cdf = np.cumsum(freq[ord])
    return val[ord][np.searchsorted(cdf[-1] // 2, cdf)]


def mode_(val, freq):
    return val[np.argmax(freq)]


def var_(val, freq):
    avg = mean_(val, freq)
    dev = freq * (val - avg) ** 2
    return sum(dev) / (sum(freq) - 1)


def std_(val, freq):
    return np.sqrt(var_(val, freq))
