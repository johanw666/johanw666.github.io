#!/bin/sh

# This will change permissions of all files to rw-r--r--
# and all directories to rwx--x--x

find . -type f -exec chmod 644 {} \;
find . -type d -exec chmod 711 {} \;
