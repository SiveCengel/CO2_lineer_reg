import matplotlib.pyplot as plt
yil = [1880, 1890, 1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020]
co2 = [290.8, 294.4, 295.7, 300.1, 303.4, 307.5, 311.3, 311.3, 316.9, 325.7, 338.8, 354.4, 369.6, 389.9, 415.4 ]

yil = yil[7:] # verinin 1950 yılından sonrasını inceledik
co2 = co2[7:] # çalışma yapacak alanı belirledik

# Elde bulunan verilere ile lineer regrasyon ( y = ax + b ) denklemine göre yapar. 
# Katsayı özelliği a değerini verir, sabit özelliği b değerini verir.

class LineerRegresyon:

    def ortalama(self, liste): 
        toplam = 0
        for i in range(len(liste)):
            toplam += liste[i]
        return toplam / len(liste)
    
    # Lineer regresyonu kullanarak, X verilerini Y verilerine uydurmaya çalışır.   
    def uydur(self, x, y):
        ortalama_x=self.ortalama(x)
        ortalama_y=self.ortalama(y)
        ust = 0
        alt = 0
        for i in range(len(x)):
            ust += (x[i] - ortalama_x) * (y[i] - ortalama_y)
            alt += (x[i] - ortalama_x) ** 2    
        self.katsayi = ust / alt
        self.sabit = ortalama_y - self.katsayi * ortalama_x
        print(f" Denklem: CO2 =  {self.sabit} + {self.katsayi} * Yıl")
    
    # Verilen X değeri için uydurulan regresyon formülünü kullanarak, Y değerini tahmin eder.
    def tahmin(self, x):
        return self.katsayi * x + self.sabit
         
    def standart_sapma(self, liste):
        o = self.ortalama(liste)
        toplam = 0
        for i in range(len(liste)):
            toplam += (liste[i] - o) ** 2
        return (toplam / len(liste)) ** 0.5
    
    # Verilen değerleri ve tahmin edilen değerleri aynı grafik üzerinde çizer.
    def oturt(self,x,y):
        ux = [x[0], x[-1]]
        uy = [self.tahmin(x[0]), self.tahmin(x[-1])] 
        plt.plot(ux, uy, "r")
        plt.scatter(x, y)
        plt.show()

model = LineerRegresyon()
model.uydur(yil,co2)
print(model.tahmin(2040))
print(model.standart_sapma(co2))
model.oturt(yil,co2)