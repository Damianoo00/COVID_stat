from Origin import interfaces

sorce = "prykladowe_dane.csv"
list_of_data = interfaces.DataInterface.get_country_list(sorce)
blad=0
prob=0
lista_blednych_danych = []
for country in list_of_data:
    try:
        y = interfaces.DataInterface.list_of_cases_in_country(country, sorce)
        x = [i for i in range(len(y))]
            #plt.plot(x, y)
        prob = prob + 1
    except:
        blad=blad+1
        print(country)
        lista_blednych_danych.append(country)
print("--------------------------------------")
print("Liczba poprawnych danych: ["+ str(prob)+"]")
print("Liczba błędnych danych: ["+ str(blad)+"]")
print(lista_blednych_danych)

