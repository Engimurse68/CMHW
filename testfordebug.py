import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9])
plt.savefig(r'C:\Users\jpsim\Documents\GitHub\CMHW\test_plot.png')
print("saved!")
plt.show()