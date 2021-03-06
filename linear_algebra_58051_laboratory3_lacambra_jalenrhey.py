# -*- coding: utf-8 -*-
"""Linear_Algebra_58051_Laboratory3_Lacambra_JalenRhey.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/Jalen18/Laboratory-3-Linear-Algebra/blob/main/Linear_Algebra_58051_Laboratory3_Lacambra_JalenRhey.ipynb

###ACTIVITY TASK 1

The general linear equation form 
$$ A = 4\hat{x} + 3\hat{y} \\ B = 7\hat{x} + 4\hat{y}$$.

The vector form 
$$ S = \begin{Bmatrix}scalar_1\cdot\begin{bmatrix}  4 \\ 3\\\end{bmatrix}, scalar_2\cdot \begin{bmatrix} 7 \\ 4\\\end{bmatrix}\end {Bmatrix} $$
"""

import numpy as np
import matplotlib.pyplot as plt

vectorA = np.array([4,3])
vectorB = np.array([7,4])

scalar = np.arange(-5,5,.5)

scalar1, scalar2 = np.meshgrid(scalar,scalar)
spanRx = scalar1 * vectorA[0] + scalar2 * vectorB[0]
spanRy = scalar1 * vectorB[1] + scalar2 * vectorB[1]
plt.scatter(spanRx, spanRy, s=5, alpha=0.75, color="blue")

plt.xlim(-50,50)
plt.ylim(-50,50)
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.grid()
plt.show()

"""###ACTIVITY TASK 2

The general linear equation form
$$ A = 3\hat{x} + 4\hat{y} \\ B = 4\hat{x} - 4\hat{y}$$.

The vector form 
$$ scalarA = \begin{bmatrix} 3 \\ 4\end{bmatrix} , scalarB = \begin{bmatrix} 4 \\ - 4\end{bmatrix}\\ $$
$$ scalarC = \begin{bmatrix} 3 \\ 4\end{bmatrix} , scalarD = \begin{bmatrix} 4 \\ - 4\end{bmatrix}\\ $$
$$ scalarE = \begin{bmatrix} 3 \\ 4\end{bmatrix} , scalarF = \begin{bmatrix} 4 \\ - 4\end{bmatrix}\\ $$
"""

import numpy as np
import matplotlib.pyplot as plt

vectorA = np.array([3,4])
vectorB = np.array([4,-4])

scalar1 = np.arange(-1,1,.1)
scalar2 = np.arange(-5,5,.5)
scalar3 = np.arange(-10,10,.5)

scalarA, scalarB = np.meshgrid(scalar1,scalar1)
scalarC, scalarD = np.meshgrid(scalar2,scalar2)
scalarE, scalarF = np.meshgrid(scalar3,scalar3)

spanRxA = scalarE * vectorA[0] + scalarF * vectorB[0]
spanRyA = scalarE * vectorB[1] + scalarF * vectorB[1]
spanRxB = scalarC * vectorA[0] + scalarD * vectorB[0]
spanRyB = scalarC * vectorB[1] + scalarD * vectorB[1]
spanRxC = scalarA * vectorA[0] + scalarB * vectorB[0]
spanRyC = scalarA * vectorA[1] + scalarB * vectorB[1]

plt.scatter(spanRxA, spanRyA, s=5, alpha=0.75, color="red")
plt.scatter(spanRxB, spanRyB, s=5, alpha=0.75, color="yellow")
plt.scatter(spanRxC, spanRyC, s=5, alpha=0.75, color="black")

plt.xlim(-100,100)
plt.ylim(-100,100)
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.grid()
plt.show()