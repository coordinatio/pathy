#!/bin/env python

from psutil import disk_partitions
from argparse import ArgumentParser

ap = ArgumentParser()
ap.add_argument('path')
a = ap.parse_args()

u = a.path.replace('\\', '/')
c = []
for p in disk_partitions(all=True):
    if p.device and u.startswith(p.device):
        c.append((p.device, p.mountpoint))
if c:
    c.sort(key=lambda s: len(s[0]), reverse=True)
    print(u.replace(c[0][0], c[0][1]), end='')
