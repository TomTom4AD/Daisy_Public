import matplotlib.pyplot as plt
import random

names = ['Kamil', 'Kasia', 'Bartosz', 'MAja', 'piesek']
points = [random.randint(3, 15) for name in names]
#points = [12, 4, 17, 31, 2]

plt.bar(names, points, color = ['green', 'blue', 'yellow'])
plt.xticks(names)
plt.yticks(points)
plt.show()

