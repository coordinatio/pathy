#!/bin/env python

from psutil import disk_partitions
from argparse import ArgumentParser

ap = ArgumentParser()
ap.add_argument('path')
ap.add_argument('-r', action='store_true')
a = ap.parse_args()

u = a.path.replace('\\', '/')
c = []
for p in disk_partitions(all=True):
    if a.r:
        if not p.device or not (p.device.startswith('//') or p.device.startswith('\\\\')):
            continue
        s, d = p.mountpoint, p.device
    else:
        s, d = p.device, p.mountpoint
    if s and u.startswith(s):
        c.append((s, d))
if c:
    c.sort(key=lambda s: len(s[0]), reverse=True)
    o = u.replace(c[0][0], c[0][1])
    if a.r:
        o = o.replace('/', '\\')
    print(o, end='')
