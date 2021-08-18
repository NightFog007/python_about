import time

from httprunner import __version__

def my_debulk_method1():
    return '1'

def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)
