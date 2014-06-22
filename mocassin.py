#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def pick_random(parts, length):
    random.shuffle(parts)
    return parts[:length]


def main():
    parts = ['mo', 'ca', 'ssin', 'ber', 'mu', 'da']
    for i in xrange(50):
        print(''.join(pick_random(parts=parts, length=3)))


if __name__ == '__main__':
    main()
