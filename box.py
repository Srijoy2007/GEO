import matplotlib.pyplot as plt

silica_data = [70.5 , 65.2 , 75.1 , 82.4 , 78.3 , 85.6 , 83.2 , 79.8 , 86.1 , 84.3 , 87.5]
alimunium_data = [15.2 , 13.8 , 17.3 , 19.6 , 18.1 , 20.9 , 19.7 , 18.4 , 21.4 , 20.1 , 22.6]

#storing the dataset in on variable

data =  [silica_data , alimunium_data]

fig, ax = plt.subplots()

ax.boxplot(data)

plt.title("Silica and alimunium content data of various districts in West Bengal")

plt.show()