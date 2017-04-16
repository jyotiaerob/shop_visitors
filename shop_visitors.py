import pandas as pd
web_statics={
	"day":['sun','mon','tue','wed','thu','fri','sat'],
	'visitors':[1000,1500,120,1300,1230,560,4563],
	'clicks':[120,150,130,200,265,210,600]
}
df=pd.DataFrame(web_statics)
print(df.head())


import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

print(df['visitors'])
df.plot()
plt.show()


