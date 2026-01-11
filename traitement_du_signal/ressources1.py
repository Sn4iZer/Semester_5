import numpy as np
import matplotlib.pyplot as plt


def fourier1D(s, fe):
    # s est le signal d'entrée et fe est la fréquence d'échantillonnage
    
    N = len(s)
    n = len(s) / 2

    # Calcul de la transformée de Fourier
    a = np.abs(np.fft.fftshift(np.fft.fft(s))) / N

    # Axe des fréquences
    x = fe * (np.arange(-np.floor(n), np.ceil(n))) / N

    # Affichage
    plt.bar(x, a)
    plt.xlabel('Fréquence (Hz)')
    plt.ylabel('Amplitude')
    plt.title('Spectre de Fourier')
    plt.grid(True)
    plt.show()

    return a


def wave(n, m, fy, fx):
    e1 = np.exp(-1j * 2 * np.pi * fx * np.arange(m))
    e2 = np.exp(1j * 2 * np.pi * fy * np.arange(n))
    img = np.outer(e2, e1).real
    return img


def fourier2d_single_frenquency(img):
    f = np.fft.fft2(img - np.mean(img))
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20 * np.log(np.abs(fshift))

    rows, cols = img.shape
    freq_x = np.fft.fftfreq(cols)
    freq_y = np.fft.fftfreq(rows)

    plt.imshow(magnitude_spectrum, cmap='gray',
               extent=(freq_x.min(), freq_x.max(), freq_y.min(), freq_y.max()))
    plt.xlabel('Frequency (cycles per pixel)')
    plt.ylabel('Frequency (cycles per pixel)')
    plt.title('2D Fourier Spectrum')
    plt.show()


def fourier2d_vue3d_old(img, fe):
    M, N = img.shape

    cx = np.arange(N) - np.floor(N / 2)
    cy = np.arange(M) - np.floor(M / 2)

    max_fx = fe * N
    max_fy = fe * M

    X, Y = np.meshgrid(fe * cx / max_fx, fe * cy / max_fy)

    Z = np.abs(np.fft.fft2(img - np.mean(img)))
    Z = np.fft.fftshift(Z) / (N * M)

    fig = plt.figure(figsize=(12, 6))

    ax1 = fig.add_subplot(121)
    ax1.imshow(img, cmap='gray')
    ax1.set_title('Image originale')

    ax2 = fig.add_subplot(122, projection='3d')
    ax2.set_title('Module de la transformée de Fourier 2D')
    ax2.set_xlabel('Fx (Hz)')
    ax2.set_ylabel('Fy (Hz)')
    ax2.set_zlabel('Module')

    ax2.plot_surface(X, Y, Z, cmap='viridis')

    plt.show()


def fourier2d_many_frequencies(img):
    f = np.fft.fft2(img - np.mean(img))
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20 * np.log(np.abs(fshift))

    rows, cols = img.shape
    freq_x = np.fft.fftfreq(cols)
    freq_y = np.fft.fftfreq(rows)

    plt.subplot(2, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')

    plt.subplot(2, 2, 2)
    plt.imshow(magnitude_spectrum, cmap='gray',
               extent=(freq_x.min(), freq_x.max(), freq_y.min(), freq_y.max()))
    plt.title('Magnitude Spectrum')
    plt.xlabel('Frequency (cycles per pixel)')
    plt.ylabel('Frequency (cycles per pixel)')

    plt.subplot(2, 2, 3, projection='3d')
    X, Y = np.meshgrid(freq_x, freq_y)
    Z = 20 * np.log(np.abs(f))
    ax = plt.gca(projection='3d')
    ax.plot_surface(X, Y, Z, cmap='gray')
    ax.set_xlabel('Frequency X (cycles per pixel)')
    ax.set_ylabel('Frequency Y (cycles per pixel)')
    ax.set_zlabel('Magnitude')
    plt.title('3D Fourier Spectrum')

    plt.show()


def fourier2d_all(img):
    f_x = np.fft.fft(img, axis=0)
    f_y = np.fft.fft(img, axis=1)

    max_freq_x = np.argmax(np.abs(f_x))
    max_freq_y = np.argmax(np.abs(f_y))

    if (max_freq_x == 0 and max_freq_y != 0) or (max_freq_x != 0 and max_freq_y == 0):
        fourier2d_single_frenquency(img)
    else:
        fourier2d_many_frequencies(img)
