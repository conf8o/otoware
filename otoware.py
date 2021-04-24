import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import numpy as np

file_name = "tansan"
rate, data = wav.read(f"{file_name}.wav")
fig = plt.figure()
plt.plot(data)
fig.savefig("original.png")

def cut(x, n):
    x[x > n] = n
    x[x < -n] = -n
    return x

def cut_and_save(rate, data, n, scalar=1):
    fig = plt.figure()
    cutted_data = cut(data, n) * scalar
    plt.plot(cutted_data)
    fig.savefig(f"{file_name}_cutted{n}.png")
    wav.write(f"{file_name}_otoware{n}.wav", rate, cutted_data)


cut_and_save(rate, data, 1000, 1)
cut_and_save(rate, data, 100, 10)
