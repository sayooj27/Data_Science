import matplotlib.pyplot as plt
import numpy as np
languages=['java','python','php','javascript','c#','c++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]


plt.figure(figsize=(8,5))
plt.bar(languages,popularity,color='blue')
plt.title('Popularity of Programming Languages')
plt.xlabel('Programming Languages')
plt.ylabel('Popularity(%)')
plt.savefig("pgm28.png")

plt.figure(figsize=(8,5))
plt.barh(languages,popularity,color='red')
plt.title('Popularity of Programming Languages(Horizontal)')
plt.xlabel('Popularity(%)')
plt.ylabel('Programming Languages')
plt.savefig("pgm28h.png")

colors=['blue','green','red','orange','purple','cyan']
plt.figure(figsize=(8,5))
plt.bar(languages,popularity,color=colors)
plt.title('Popularity of Programming Languages(Diffrent colors)')
plt.xlabel('Programming Languages')
plt.ylabel('Popularity(%)')
plt.savefig("pgm28d.png")

plt.figure(figsize=(8,5))
plt.pie(popularity,labels=languages,autopct='%1.1f%%',startangle=140)
plt.title('Popularity of Programming Languages(pie chart)')
plt.axis("equal")
plt.savefig("pgm28e.png")