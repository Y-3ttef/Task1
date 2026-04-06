import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
df=sns.load_dataset("titanic")
df.head()
sns.countplot(x="survived",data=df)
plt.title("survived count")
plt.show()

sns.barplot(x="sex",y="survived",data=df)
plt.title("survived rate by sex")
plt.show()

sns.scatterplot(x="age",y="fare",hue="survived",data=df)
plt.title("Age vs fare")
plt.show()

sns.boxenplot(x="pclass",y="fare",data=df)
plt.title("fare distribution by class")
plt.show()

sns.lineplot(x=df.index[:100],y="fare"[:100],data=df[:100])

plt.title("fare for first 100 passenger")

plt.show()


