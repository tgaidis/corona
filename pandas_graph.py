import pandas
library pandas
library plyr
dataCOVID = pandas.read_csv('covid.csv')

df = dataCOVID.dataframe

plt.plot( 'covid', 'tweets', data=df, marker='o', markerfacecolor='black', markersize=12, color='green', linewidth=2)
plt.plot( 'corona virus', 'tweets', data=df, marker='', color='blue', linewidth=2)
plt.plot( 'pandemic', 'tweets', data=df, marker='', color='red', linewidth=2, linestyle='solid', label="f")
plt.legend()
