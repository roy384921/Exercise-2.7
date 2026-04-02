import numpy as np
import os

# Define channel parameters
# You can increase these numbers later, but small numbers are good for quick testing
num_train = 100000  
num_test = 100000   
L = 16             # Length of the channel impulse response (CP length = 64 // 4)

print("Generating mock channel data...")

# Generate Rayleigh fading channel (complex Gaussian)
# The total power of the channel taps is normalized to 1
channel_train = (np.random.randn(num_train, L) + 1j * np.random.randn(num_train, L)) / np.sqrt(2 * L)
channel_test = (np.random.randn(num_test, L) + 1j * np.random.randn(num_test, L)) / np.sqrt(2 * L)

# Ensure the 'tools' directory exists
if not os.path.exists('tools'):
    os.makedirs('tools')

# Save the generated arrays to .npy files in the tools folder
np.save('tools/channel_train.npy', channel_train)
np.save('tools/channel_test.npy', channel_test)

print(f"Successfully generated tools/channel_train.npy with shape: {channel_train.shape}")
print(f"Successfully generated tools/channel_test.npy with shape: {channel_test.shape}")
