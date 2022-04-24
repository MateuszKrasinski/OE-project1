import math
import random
import numpy as np

import config


def objective(x):
    return config.OBJECTIVE(x)

if __name__ == '__main__':
    best = (random.uniform(-1.5,4), random.uniform(-1.5,4))

    for x in range(0, 400):
        tmp = random.uniform(-1.5,4), random.uniform(-1.5,4)
        if(objective(tmp)<objective(best)):
            best = tmp
        print(objective(tmp))

    print('Result:')
    print('x:', best)
    print('Fitness:', objective(best))