import numpy as np
# Define two arrays
x1 = np.array([1, 2, 3, 4])
x2 = np.array([4, 3, 2, 1])

# Define constants
a = 2
b = 5

# Linear combination of x1 and x2
x = a * x1 + b * x2

# Perform DTFT on x1, x2, and x
X1 = np.fft.fft(x1)
X2 = np.fft.fft(x2)
X = np.fft.fft(x)

# Verify linear property
print("Linear property verified:", np.allclose(X, a * X1 + b * X2))
def dft(x):
    N=len(x)
    x=np.zeroes(N,dtype=complex)
    for k in range(N):
        X[k]=sum(x[n]*np.exp(-2j*np.pi*k*n/N)for n in range(N))
        return X