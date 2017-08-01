import numpy as np
import matplotlib.pylab as plt

from scipy.signal import hilbert as scipy_hilbert
from numpy import sin, cos, tan, pi


def hilbert(x):
	"""
	Compute the analytic signal, using the Hilbert transform with Hanh's method [1].

	[1] S. Hanh, Hilbert Transform in Signal Processing, Artech House, Boston 1996

	:param x: array_like
	:return xa: ndarray
			Analytic signal of x
	"""

	N = len(x)

	if N%2 == 0: N -= 1

	cot = lambda theta: 1 / tan(theta)
	h = lambda n: (2/N) * cot(n*pi/N) * (sin(n*pi/2)**2) if n != 0 else 0

	y = np.zeros(len(x))

	for i in np.arange(len(x)):
		for m in np.arange(N):
			y[i] += h(i-m)*x[m]

	print(y)

	return y


if __name__ == '__main__':
	# x = np.random.rand(100)
	x = 4*pi*np.arange(100)/100

	# print((hilbert(x) - scipy_hilbert(x))/scipy_hilbert(x))

	plt.figure()
	# u = np.imag(hilbert(cos(x)))
	u = hilbert(cos(x))

	print(hilbert(cos(x)))

	plt.plot(u, 'b', label='H')
	plt.plot(np.imag(scipy_hilbert(cos(x))), 'k', label='H')
	plt.plot(sin(x), '--r', label='sin')
	plt.ylim(-1, 1)

	# print((np.imag(hilbert(cos(x))) - sin(x)) / sin(x))

	plt.show()