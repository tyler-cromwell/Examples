#!/usr/bin/env python3

import random
import string
import sys


def group(size, groups):
    samples = []
    population = list(string.ascii_uppercase + string.ascii_lowercase + string.digits)

    if len(population) < groups*size:
        sys.exit(0)

    for i in range(groups):
        sample = random.sample(population, size)

        for member in sample:
            population.remove(member)

        samples.append(''.join(sample))

    return samples


if __name__ == '__main__':
    samples = group(6, 10)

    for i in range(len(samples)):
        print('Group {}: {}'.format(i+1, ''.join(samples[i])))
