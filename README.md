# pathy

Convert paths between Windows SMB/CIFS UNC shares and Linux mount points.
Uses the currently mounted CIFS shares and the longest matching prefix.

```
pathy.py '\\server\share\file.txt'   # → /mnt/share/file.txt
pathy.py -r /mnt/share/file.txt      # → \\server\share\file.txt
```

Requires Python 3 and `psutil`.
