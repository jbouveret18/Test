import pandas as pd

df = pd.read_excel("C:/Users/jbouv/OneDrive/Masaüstü/PI work/country_vaccination_stats _coded.xlsx")

def fillBlanks(Country) :
    Min = df.loc[df['country'] == Country, 'daily_vaccinations'].min()
    numberOfRows = len(df.loc[df['country'] == Country, 'daily_vaccinations']) 
    if(numberOfRows==2) :
        CountryData = df.loc[df['country'] == Country, 'daily_vaccinations'].fillna(Min)
    else :
        CountryData = df.loc[df['country'] == Country, 'daily_vaccinations'].fillna("0")
    print(CountryData)


fillBlanks("Argentina")
fillBlanks("Austria")
fillBlanks("Bahrain")
fillBlanks("Belgium")
fillBlanks("Brazil")
fillBlanks("Bulgaria")
fillBlanks("Canada")
fillBlanks("Chile")
fillBlanks("China")
fillBlanks("Costa Rica")
fillBlanks("Croatia")
fillBlanks("Cyprus")
fillBlanks("Czechia")
fillBlanks("Denmark")
fillBlanks("Ecuador")
fillBlanks("England")
fillBlanks("Estonia")
fillBlanks("Finland")
fillBlanks("France")
fillBlanks("Germany")
fillBlanks("Gilbraltar")
fillBlanks("Greece")
fillBlanks("Hungary")
fillBlanks("Iceland")
fillBlanks("India")
fillBlanks("Indonesia")
fillBlanks("Ireland")
fillBlanks("Isle of Man")
fillBlanks("Israel")
fillBlanks("Italy")
fillBlanks("Kuwait")
fillBlanks("Latvia")
fillBlanks("Lithuania")
fillBlanks("Luxembourg")
fillBlanks("Malta")
fillBlanks("Mexico")
fillBlanks("Netherlands")
fillBlanks("Northern Ireland")
fillBlanks("Norway")
fillBlanks("Oman")
fillBlanks("Panama")
fillBlanks("Poland")
fillBlanks("Portugal")
fillBlanks("Romania")
fillBlanks("Russia")
fillBlanks("Saudi Arabia")
fillBlanks("Scotland")
fillBlanks("Serbia")
fillBlanks("Seychelles")
fillBlanks("Singapore")
fillBlanks("Slovakia")
fillBlanks("Slovenia")
fillBlanks("Spain")
fillBlanks("Sweden")
fillBlanks("Switzerland")
fillBlanks("Turkey")
fillBlanks("United Arab Emirates")
fillBlanks("United Kingdom")
fillBlanks("United States")
fillBlanks("Wales")









