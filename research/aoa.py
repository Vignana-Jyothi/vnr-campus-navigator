import numpy as np
from scipy.linalg import eigh

def estimate_aoa(signal_data, antenna_positions, signal_frequency):
    """
    Estimate the Angle of Arrival (AoA) of a Wi-Fi signal using the MUSIC algorithm.

    Parameters:
    signal_data (ndarray): Complex signal data from the antenna array.
    antenna_positions (ndarray): Positions of the antennas in the array.
    signal_frequency (float): Frequency of the Wi-Fi signal in Hz.

    Returns:
    float: Estimated Angle of Arrival (AoA) in degrees.
    """
    # Speed of light
    c = 3e8

    # Number of antennas
    num_antennas = antenna_positions.shape[0]

    # Calculate the covariance matrix of the received signals
    R = np.dot(signal_data, signal_data.conj().T) / signal_data.shape[1]

    # Eigenvalue decomposition
    eigenvalues, eigenvectors = eigh(R)

    # Sort eigenvalues and eigenvectors
    idx = eigenvalues.argsort()[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]

    # Determine the number of signal sources (assuming one for simplicity)
    num_signals = 1

    # Noise subspace
    noise_subspace = eigenvectors[:, num_signals:]

    # Define a grid of potential AoA values
    aoa_grid = np.linspace(-90, 90, 181)  # AoA values from -90 to 90 degrees
    spatial_spectrum = np.zeros(aoa_grid.shape)

    # Calculate the MUSIC pseudo-spectrum
    for i, theta in enumerate(aoa_grid):
        steering_vector = np.exp(
            -1j * 2 * np.pi * signal_frequency / c * antenna_positions @ np.array([np.sin(np.radians(theta)), np.cos(np.radians(theta))])
        )
        spatial_spectrum[i] = 1 / np.linalg.norm(noise_subspace.conj().T @ steering_vector)**2

    # Find the AoA corresponding to the peak of the pseudo-spectrum
    aoa_estimated = aoa_grid[np.argmax(spatial_spectrum)]

    return aoa_estimated

# Example usage:
if __name__ == "__main__":
    # Example signal data (complex values), antenna positions (in meters), and signal frequency (in Hz)
    signal_data = np.array([
        [1 + 1j, 0.8 + 0.6j, 0.6 + 0.2j],
        [0.8 + 0.6j, 1 + 1j, 0.8 + 0.6j],
        [0.6 + 0.2j, 0.8 + 0.6j, 1 + 1j]
    ])
    antenna_positions = np.array([
        [0, 0],
        [0.05, 0],
        [0.1, 0]
    ])
    signal_frequency = 2.4e9  # 2.4 GHz

    aoa = estimate_aoa(signal_data, antenna_positions, signal_frequency)
    print(f"Estimated AoA: {aoa:.2f} degrees")

