#!/bin/env python

from psutil import disk_partitions
from argparse import ArgumentParser

ap = ArgumentParser()
ap.add_argument('path')
a = ap.parse_args()

u = a.path.replace('\\', '/')
for p in disk_partitions(all=True):
    if p.device and u.startswith(p.device):
        print(u.replace(p.device, p.mountpoint))
