import pandas
library pandas
library plyr
dataCOVID = pandas.read_csv('covid.csv')

df = dataCOVID.dataframe


coviddb %>% ggplot(aes(x =Fri May 08 02:49:51 +0000 2020  y = 1258589905065828352)) +
            geom_point() +
            geom_point(method = "lm") +
            labs(x = "Time of day",
                 y = "  count of corona in tweets",
                 title = "Plot of Corona on Twitter")



def checkDuplicates1(listof):
    ''' Check if given list contains any duplicates '''
    if len(listof) == len(set(listof)):
        return False
    else:
        return True

plt.plot( 'covid', 'tweets', data=df, marker='o', markerfacecolor='black', markersize=12, color='green', linewidth=2)
plt.plot( 'corona virus', 'tweets', data=df, marker='', color='blue', linewidth=2)
plt.plot( 'pandemic', 'tweets', data=df, marker='', color='red', linewidth=2, linestyle='solid', label="f")
plt.legend()