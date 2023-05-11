import pyAgrum as gum
from itertools import product
import math
import csv
import pandas as pd
import numpy as np
import os
from tabulate import tabulate

def find_posteriors(bn_name):
    test_file = "tort_unique.csv"
    bn_name = bn_name

    bn = gum.loadBN(bn_name)

    f= csv.DictReader(open(test_file))
    sum = 0
    bad = []
    for row in f:
        evidence = {key: row[key] for key in ["dmg","cau",
                                                   "vrt","vst",
                                                   "vun","jus",
                                                   "ift","ila",
                                                   "ico","prp"]}
        #print(evidence)
        ie = gum.LazyPropagation(bn)
        try:
            ie.setEvidence(evidence)
            p = gum.getPosterior(bn, evs=evidence, target="duty")
            probability = p[1]
        except Exception as exception:
            print(exception)
            probability = -1

        #print(f"true duty : {row['dut']}, predicted duty : {int(probability)}")
        print(probability, type(probability))
        if probability == 1.0 and int(row['dut']) == 1 or\
                probability == 0.0 and int(row['dut']) == 0:
            sum += 1
        else:
            bad.append([evidence, row['dut'], probability])

    #print("=========================")
    #print(bn_name)
    #print(sum)
    #print("mistakes")
    #print(len(bad))
    return sum, len(bad), bn.sizeArcs()

def tort_law_extended():
    df = pd.read_csv('tort_unique.csv')
    df['c1'] = np.where(df['cau'] == 1, 1, 0)
    df['c2'] = np.where(((df['ico'] == 1) |
                         (df['ila'] == 1) |
                         (df['ift'] == 1)), 1, 0)
    df['c3'] = np.where((df['vun'] == 1) |
                        ((df['vst'] == 1) & (df['jus'] == 0)) |
                        ((df['vrt'] == 1) & (df['jus'] == 0)), 1, 0)
    df['c4'] = np.where(df['dmg'] == 1, 1, 0)
    df['c5'] = np.where((df['vst'] == 1) & (df['prp'] == 0), 1, 0)
    df.to_csv('tort_extended.csv')



def learn_networks():
    case_file = "tort_extended.csv"

    learner = gum.BNLearner(case_file)
    learner.useGreedyHillClimbing()
    print(learner)
    bn2 = learner.learnBN()
    gum.saveBN(bn2, "generatedBNs/tortlawGHC.net")

    '''
    learner = gum.BNLearner(case_file)
    learner.useLocalSearchWithTabuList()
    print(learner)
    bn2 = learner.learnBN()
    gum.saveBN(bn2, "generatedBNs/tortlawTabu.net")


    learner = gum.BNLearner(case_file)
    #learner.useK2(["dmg","cau","vrt","vst","vun","jus","ift","ila","ico","prp", "c1","c2","c3","c4","c5","dut"])

    learner.useK2()
    print(learner)
    bn2 = learner.learnBN()
    gum.saveBN(bn2, "generatedBNs/tortlawK2.net")
    '''


tort_law_extended()
#learn_networks()

'''
The rule-based Bayesian Network correctly predicts the 
duty
'''
correct, mistakes, arcs = find_posteriors("tortlaw.net")

# , "generatedBNs/tortlawK2.net"


'''
automatic bayesian networks seem unable to do it (but there's no information about the C's)
what if we include information about the C's?

Import learned networks from bnlearn

'''

results = [["algorithm", "correct", "mistakes", "arcs"], ["manual", correct, mistakes, arcs]]
for name in os.listdir("automaticBNs"):
    algo = name.split(".net")[0]
    if ".net" in name:
        correct, mistakes, arcs = find_posteriors(os.path.join("automaticBNs", name))
        #print(f"{algo}    |  {correct}  | {mistakes}  | {arcs}")
        results.append([algo, correct, mistakes, arcs])


print(tabulate(results, headers='firstrow', tablefmt="rounded_outline"))

