import checkDupes
import countTweets
import covidproj
import pandas_graph

def main():
    checkDupes('COVID.csv')
    checkDupes('CORONA.csv')
    checkDupes('Pandemic.csv')

    countTweets('COVID.csv')
    countTweets('CORONA.csv')
    countTweets('Pandemic.csv')


if __name__=="__main__":
    main()