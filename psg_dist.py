import os
import math
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    type = int(input("Input type of distribution:\n"
                 "1 for pseudo-geometric distribution\n"
                 "2 for geometric distribution\n"
                 ": "))

    if type == 1:
        k = int(input("Input k: "))
        p0 = float(input("Input p: "))
        q = 1 - p0
        p = []
        MX = 0
        MX2 = 0
        DX = 0

        for i in range(0, k):
            p.append(round(q**i*p0, 8))
            MX += (i+1)*p[i]
            MX2 += (i+1)**2*p[i]
        DX = MX2 - MX**2

        res = "M(X) = %f\nD(X) = %f" % (MX, DX)

        print(p)
        print(res)

        fig1 = plt.figure(figsize=(8, 6), dpi=100)
        fig1.canvas.set_window_title("Pseudo-geometric distribution by Dmit0k")
        fig1.subplots_adjust(hspace=0.35)

        ax1 = fig1.add_subplot(1, 1, 1)
        ax1.plot(range(0, k), p, marker='o')
        ax1.set_axisbelow(True)
        ax1.grid(which='major', linestyle='-', linewidth='0.2', color='black')
        ax1.set_title('Polygon distribution')

        ax2 = fig1.add_subplot(2, 2, 2, frameon=False)
        row_labels = ['x[i]', 'p[i]']
        plt.setp(ax2, xticks=[], yticks=[])
        ax2.table(cellText=[range(0, k), p], loc='upper center', rowLabels=row_labels)
        ax2.text(0.18, 0.65, res, transform=ax2.transAxes)

        plt.tight_layout()
        plt.show()

    if type == 2:
        p = float(input("Input p: "))
        q = round(1 - p, 8)
        MX = round(1/p, 8)
        DX = round(q/p**2, 8)
        sigma = round(math.sqrt(q)/p, 8)
        AX = round((2-p)/math.sqrt(1-p), 8)
        EX = round(sigma + p**2/(1-p), 8)

        print("q = %f\n"
              "M(X) = %f\n"
              "D(X) = %f\n"
              "σ(X) = %f\n"
              "A(X) = %f\n"
              "E(X) = %f\n" % (q, MX, DX, sigma, AX, EX))