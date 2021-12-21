#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    u = set("abcdefghijklmnopqrstuvwxyz")

    a = {'a', 'b', 'f', 'g', 'i'}
    b = {'c', 'f', 'g', 'i', 's', 'v'}
    c = {'a', 'g', 'h', 'i'}
    d = {'f', 'w', 'x'}

    x = (a.intersection(c)).union(b)

    an = u.difference(a)

    y = (an.intersection(d)).union(c.difference(b))

    print(
        f"X = {x}\n"
        f"Y = {y}"
        )

