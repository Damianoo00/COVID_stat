import matplotlib.pyplot as plt
import interfaces
list_of_data = interfaces.Data_interface.get_country_list("time_series_covid19_confirmed_global.csv")
i=0
for country in list_of_data:
    try:
        y = interfaces.Data_interface.list_of_cases_in_country(country)
        x = [i for i in range(len(y))]
        plt.plot(x, y)
        
    except:
        i=i+1
        print(country)
print("--------------------------------------")
print("Liczba błędnych danych: ["+ str(i)+"]")