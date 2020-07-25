#!/usr/bin/python3
# coding : utf-8

import mycli, sys

output = mycli.open_mylogin_cnf(sys.argv[1])

print(output.readlines())