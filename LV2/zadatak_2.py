import numpy as np 
import matplotlib.pyplot as plt

data = np.genfromtxt('data.csv', delimiter=',', skip_header=1)

gender = data[:,0] #svi ispitanici 
height = data[:,1]
weight = data[:,2]

step = 50
x = height[::step]
y = weight[::step] # svaki 50-ti ispitanik

index_muski = data[:,0] == 1
index_zenski = data[:,0] == 0

heigh_muski = height[index_muski]
heigh_zenski = height[index_zenski]
 
brojIspitanika = np.size(gender)
print(f"Ukupno je napravljeno mjerenja za {brojIspitanika} ispitanika.")
print(f"Najmanja visina je : {np.min(height)} cm, a najveća visina je : {np.max(height)} cm, dok je prosječna visina : {np.mean(height)} cm.")
print("Muškarci – min:", np.min(heigh_muski), "max:", np.max(heigh_muski), "mean:", np.mean(heigh_muski))
print("Žene    – min:", np.min(heigh_zenski), "max:", np.max(heigh_zenski), "mean:", np.mean(heigh_zenski))
plt.scatter(x, y, color='blue', marker='o')
plt.ylabel('masa [kg]')
plt.xlabel('visina [cm]')
plt.title('Visina u usporedbi s masom ispitanika')
plt.show()