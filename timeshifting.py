import numpy as np

# Define two arrays
x = np.array([1,2,3,4,0,0,0])
X = np.fft.fft(x)

# Time shift by 2 samples (manual implementation)
x_shifted = np.zeros(len(x))
x_shifted[2:] = x[:-2]

# Perform DTFT on time-shifted array
X_shifted = np.zeros(len(x), dtype=complex)
for k in range(len(x)):
    for n in range(len(x)):
        X_shifted[k] += x_shifted[n] * np.exp(-2j * np.pi * k * n / len(x))

# Verify time-shifting property
n = np.arange(len(x))
print("Time-shifting property verified:", np.allclose(X_shifted, np.exp(-2j * 2 * np.pi * n / len(x)) * X))

