import numpy as np
import matplotlib.pyplot as plt

# plot figure awal
fig, ax = plt.subplots(figsize=(10, 7))

# plot koordinat kartesius
ax.spines[["left", "bottom"]].set_position(("data", 0))
ax.spines[["top", "right"]].set_visible(False)
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)


# fungsi yang akan dicari akar persamaannya
def fungsi(x):
    return (3 * (x ** 3) - (2 * (x ** 2)) + 1)


# plot grafik
x = np.linspace(-7, 7, 100)
ax.plot(x, fungsi(x))

# tampil plot
ax.set_title(f"Program Mencari Akar Persamaan Dengan Metode Bolzano\n"
             f"Pilihlah nilai x0 dan x1", fontsize=21)
plt.ylim([-7, 7])
plt.show()

# input x0, x1 dan n
print('Masukan nilai x0, x1 dan banyaknya iterasi')
x0 = int(input())
x1 = int(input())
n = int(input())


# fungsi bolzano
def bolzano(x0, x1, n):
    # cek nilai x0 dan x1
    if fungsi(x0) * fungsi(x1) >= 0:
        print(f"Fungsi tidak memotong sumbu x antara x = {x0} dan x = {x1}")
        return

    # iterasi
    for i in range(1, n + 1):
        # metode bolzano
        c = (x0 + x1) / 2

        #  print nilai c atau nilai tengah
        print(f"Iterasi ke-{i} = {c}")

        # plot figure iterasi
        fig2, ax2 = plt.subplots(figsize=(6, 6))

        # koordinat kartesius
        ax2.spines[["left", "bottom"]].set_position(("data", 0))
        ax2.spines[["top", "right"]].set_visible(False)
        ax2.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
        ax2.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

        # tanda nilai c
        tanda = plt.Circle((c, 0), 0.07, color='r', fill=True)
        ax2.add_patch(tanda)

        # tampil grafik
        ax2.plot(x, fungsi(x))
        ax2.set_title(f"Iterasi ke-{i} = {c}")
        plt.ylim([-7, 7])
        plt.show()

        # update nilai c
        if fungsi(x0) * fungsi(c) >= 0:
            x0 = c
        elif fungsi(x1) * fungsi(c) >= 0:
            x1 = c

    # print hasil akhir akar persamaan
    print(f"Akar persamaan dari fungsi 3x^3 - 2x^2 + 1 adalah {c}")

    # plot figure hasil
    fig3, ax3 = plt.subplots(figsize=(10, 1))

    # ax3.spines[["top", "right", "left", "bottom"]].set_visible(False)
    fig3.clear(True)
    fig3.suptitle(f"Akar persamaan dari fungsi 3x^3 - 2x^2 + 1 adalah {c}")
    plt.show()

    return


bolzano(x0, x1, n)
