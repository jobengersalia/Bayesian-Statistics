# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 15:25:56 2025

@author: Joben Gersalia
"""

import scipy.stats as sts
import numpy as np
import matplotlib.pyplot as plt

mu = np.linspace(1.65, 1.8, num = 50)
test = np.linspace(0, 2)
uniform_dist = sts.uniform.pdf(mu) + 1 

uniform_dist = uniform_dist/uniform_dist.sum()
beta_dist = sts.beta.pdf(mu, 2, 5, loc = 1.65, scale = 0.2)
beta_dist = beta_dist/beta_dist.sum()
plt.plot(mu, beta_dist, label = 'Beta Dist')
plt.plot(mu, uniform_dist, label = 'Uniform Dist')
plt.xlabel("Value of $\mu$ in meters")
plt.ylabel("Probability density")
plt.legend()

