
import numpy as np
from scipy.stats import genextreme
from scipy.spatial.distance import pdist, cdist
import time as t


def estat(
    x, y, nboot=1000, maxt=60., replace=False, method='log',
        fitting=False):
    """
    Energy distance statistics test.

    References
    ----------

    * Aslan, B, Zech, G (2005) Statistical energy as a tool for binning-free
      multivariate goodness-of-fit tests, two-sample comparison and unfolding.
      Nuc Instr and Meth in Phys Res A 537: 626-636

    * Szekely, G, Rizzo, M (2014) Energy statistics: A class of statistics
      based on distances. J Stat Planning & Infer 143: 1249-1272

    * Brian Lau, multdist, https://github.com/brian-lau/multdist

    """

    n, N = len(x), len(x) + len(y)
    stack = np.vstack([x, y])
    # stack = (stack - stack.mean(0)) / stack.std(0)
    stack = (stack - np.nanmean(stack, 0)) / np.nanstd(stack, 0)
    if replace:
        def rand(x):
            return np.random.randint(x, size=x)
        # rand = lambda x: np.random.randint(x, size=x)
    else:
        rand = np.random.permutation

    en = energy(stack[:n], stack[n:], method)
    en_boot = np.zeros(nboot, 'f')
    s = t.time()
    for i in range(nboot):
        idx = rand(N)
        en_boot[i] = energy(stack[idx[:n]], stack[idx[n:]], method)
        if t.time() - s > maxt:
            print("Time consumed, exit bootstrap (N={})".format(i))
            en_boot, nboot = en_boot[:i], i + 1
            break

    if fitting:
        param = genextreme.fit(en_boot)
        p = genextreme.sf(en, *param)
        return p, en, param
    else:
        p = (en_boot >= en).sum() / nboot
        return p, en, en_boot


def energy(x, y, method='log'):
    dx, dy, dxy = pdist(x), pdist(y), cdist(x, y)
    n, m = len(x), len(y)
    if method == 'log':
        dx, dy, dxy = np.log(dx), np.log(dy), np.log(dxy)
    elif method == 'gaussian':
        raise NotImplementedError
    elif method == 'linear':
        pass
    else:
        raise ValueError
    # z = dxy.sum() / (n * m) - dx.sum() / n**2 - dy.sum() / m**2
    z = np.nansum(dxy) / (n * m) - np.nansum(dx) / n**2 - np.nansum(dy) / m**2
    # z = ((n*m)/(n+m)) * z # ref. SR
    return z
