def read_specimen_data(filename):
    data = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line.count("\t") == 2:
                numbers = line.split("\t")
                try:
                    numbers = [float(num) for num in numbers]
                    data.append(numbers)
                except ValueError:
                    pass

    return data


import matplotlib.pyplot as plt

"""def plot_data(data, title="Specimen.dat"):
    x = [row[1] for row in data]
    y = [row[2] for row in data]

    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(title)
    plt.show()"""

import matplotlib.pyplot as plt
import numpy as np

from scipy import integrate

def plot_data(data, title="Specimen.dat", fit_n=10, area=6.4):
    x = [row[1] for row in data]
    y = [row[2] for row in data]

    # data set-zero
    x = [i - x[0] for i in x]
    y = [i - y[0] for i in y]

    # x from mm to strain (unitless)

    x = [i / 75 for i in x]

    ### with better data this can be enabled
    # area = np.trapz(y, x)
    # print("Area under the curve:", area)

    plt.plot(x, y)
    plt.xlabel("X")
    plt.ylabel("Y")

    # Fit a linear line using the first fit_n data points
    fit_x = x[:fit_n]
    fit_y = y[:fit_n]
    coefficients = np.polyfit(fit_x, fit_y, 1)

    plt.title(f"{title}: Young's modulus (MPa | N/mm2) = {coefficients[0] / area}")

    coefficients[1] = 0
    coefficients_2 = np.array([coefficients[0], -0.002 * coefficients[0]])
    print(coefficients)
    print(coefficients_2)
    custom_x = [0, max(fit_y) / coefficients[0]]
    custom_x_2 = [0, max(y) / coefficients[0]]
    custom_x_2_mod = [0.002, max(y) / coefficients[0] + 0.002]

    fit_line = np.poly1d(coefficients)
    fit_line_2 = np.poly1d(coefficients_2)

    print(custom_x)
    print(fit_line(custom_x))
    plt.plot(custom_x, fit_line(custom_x), "r", label=f"Linear Fit first {fit_n}")
    plt.plot(
        custom_x_2,
        fit_line(custom_x_2),
        "r--",
        label=f"Linear Extrapolate first {fit_n}",
    )

    plt.plot(
        custom_x_2_mod,
        fit_line_2(custom_x_2_mod),
        "g--",
        label=f"0.2% Linear Extrapolate first {fit_n}",
    )
    plt.legend()
    plt.show()


cross_sectional_areas = {
    "Acrylic.dat": 8 * 3,
    "Aluminium.dat": 8 * 0.8,
    "StainlessSteel.dat": 8 * 0.8,
}

from glob import glob

for filename in glob("*.dat"):
    # Usage example
    # filename = 'specimen.dat'
    result = read_specimen_data(filename)
    # print(result)

    # Usage example
    plot_data(result, filename, 10, cross_sectional_areas[filename])
