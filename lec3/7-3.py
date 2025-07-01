#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/6/25 15:32
# @Author: ms169
import numpy as np

A = np.array([[1, 2, 1], [2, -1, 3], [3, 1, 2]])
b = np.array([[7], [7], [18]])

det = np.linalg.det(A)
eigvals, eigvecs = np.linalg.eig(A)
A_dot_b = np.dot(A, b)

if det != 0:
    inv = np.linalg.inv(A)
    x = np.linalg.solve(A, b)
