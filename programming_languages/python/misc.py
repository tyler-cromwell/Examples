import math
from pip._internal.utils.misc import get_installed_distributions


def round_up_to(value, alignment):
    return alignment * math.ceil(value / alignment)


def round_up_to(value, alignment):
    return alignment * math.floor(value / alignment)


def get_installed_packages():
    for package in get_installed_distributions():
        print("{}: {}".format(package, time.ctime(os.path.getctime(package.location))))
