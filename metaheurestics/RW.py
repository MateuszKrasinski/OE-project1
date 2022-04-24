import math
import random
import numpy as np

import config


def objective(x):
    return config.OBJECTIVE(x)

if __name__ == '__main__':
    best = (random.uniform(-1.5, 4), random.uniform(-1.5, 4))
    step_size = 0.5

    for x in range(0, 200):
        tmp = best[0] + random.uniform(-1.5, 4) * step_size, best[1] + random.uniform(-1.5, 4) * step_size
        best = tmp
        print(objective(tmp))

    print('Result:')
    print('x:', best)
    print('Fitness:', objective(best))
