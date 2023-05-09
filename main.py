import pyAgrum as gum
from itertools import product
import math
import csv


test_file = "tort_unique.csv"
bn_name = "tortlaw.net"

bn = gum.loadBN(bn_name)

f= csv.DictReader(open(test_file))
sum = 0
bad = []
for row in f:
    print(row)
    print(row['dut'])
    evidence = {key: row[key] for key in ["dmg","cau",
                                               "vrt","vst",
                                               "vun","jus",
                                               "ift","ila",
                                               "ico","prp"]}
    print(evidence)
    ie = gum.LazyPropagation(bn)
    try:
        ie.setEvidence(evidence)
        p = gum.getPosterior(bn, evs=evidence, target="duty")
        probability = p[1]
    except Exception as exception:
        # print(exception)
        probability = -1

    print(f"true duty : {row['dut']}, predicted duty : {p[1]}")
    if int(row['dut']) == int(p[1]):
        sum += 1
    else:
        bad.append([evidence, row['dut'], p[1]])

print("=========================")
print(sum)
print("mistakes")
print(bad)
