#!/bin/env python

from psutil import disk_partitions
from argparse import ArgumentParser

ap = ArgumentParser()
ap.add_argument('path')
ap.add_argument('-r', action='store_true')
a = ap.parse_args()

u = a.path.replace('\\', '/')
# Bash double-quotes turn \\server into \server; CIFS devices are //server/share.
if not a.r and u.startswith('/') and not u.startswith('//'):
    u = '/' + u
c = []
for p in disk_partitions(all=True):
    if a.r:
        if not p.device or not (p.device.startswith('//') or p.device.startswith('\\\\')):
            continue
        s, d = p.mountpoint, p.device
    else:
        s, d = p.device, p.mountpoint
    if s and (u.startswith(s) if a.r else u[:len(s)].casefold() == s.casefold()):
        c.append((s, d))
if c:
    c.sort(key=lambda s: len(s[0]), reverse=True)
    o = c[0][1] + u[len(c[0][0]):]
    if a.r:
        o = o.replace('/', '\\')
    print(o, end='')
