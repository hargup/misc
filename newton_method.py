# import seaborn
import matplotlib.pyplot as plt
import numpy as np
from numba import jit

# seaborn.set()

@jit(nopython=True)
def fx(x):
    return x**3 - 1


@jit(nopython=True)
def dfx(x):
    return 3*x**2


@jit(nopython=True)
def newton_method(x, N):
    for i in xrange(N):
        x = x - fx(x)/dfx(x)
    return x


@jit(nopython=True)
def newton_method_close(x, N):
    eps = 0.01
    f_x = fx(x)
    while np.abs(f_x) > eps:
        x = x - f_x/dfx(x)
    return x


# SOLS = np.array([1, -0.5 + np.sqrt(3.0/2), -0.5 - np.sqrt(3.0/2)])


@jit(nopython=True)
def sol_num(x):
    # NOTE: numba doesn't support np.array construct
    # SOLS_list = [1, -0.5 + np.sqrt(3.0/2), -0.5 - np.sqrt(3.0/2)]
    SOLS = np.zeros(3, dtype=np.complex64)
    SOLS[0] = 1
    SOLS[1] = -0.5 + np.sqrt(3.0/2)
    SOLS[2] = -0.5 - np.sqrt(3.0/2)

    # for i in range(3):
    #     SOLS[i] = SOLS_list[i]

    dist = np.abs(SOLS - x)
    return dist.argmin()


@jit(nopython=True)
def get_image(RES, iter_num):
    plane = np.zeros((RES, RES, 3), dtype=np.uint8)

    rel = np.linspace(-1, 1, RES)
    img = np.linspace(-1j, 1j, RES)

    for n, x in enumerate(rel):
        for m, y in enumerate(img):
            c = newton_method(x + y, iter_num)
            color = sol_num(c)
            plane[n, m, color] = 255
    return plane

import sys
RES = int(sys.argv[1])
iter_num = int(sys.argv[2])
plane = get_image(RES=RES, iter_num=iter_num)
plt.imshow(plane)
plt.savefig('newton_method_%s_%s.png' % (RES, iter_num))
