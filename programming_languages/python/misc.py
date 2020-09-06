import math


def round_up_to(value, alignment):
    return alignment * math.ceil(value / alignment)


def round_up_to(value, alignment):
    return alignment * math.floor(value / alignment)
