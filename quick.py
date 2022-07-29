from matplotlib import pyplot as plt
import random
x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]



v1 = 0.1
v2 = 0.2

predict = []
for (item1, item2, item3, item4) in zip(x_values, x_values, x_values, x_values):
    predict.append(random.uniform(v1, v2)*item1 + random.uniform(v1, v2)*item2 + random.uniform(v1,v2) * item3 + random.uniform(v1,v2) * item4)
print(predict)
plt.plot(x_values,y_values)
plt.plot(predict,y_values)
plt.show()

for i in x_values:
    print()