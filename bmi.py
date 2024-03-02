import tkinter
from tkinter import messagebox

#window oluşturma
win = tkinter.Tk()
win.title("BMI Hesaplayıcı")
win.minsize(width=300, height=300)
win.config(pady=30)

# BMI değerlerine göre açıklamalar
def bmi_aciklama(bmi):
    if bmi < 18.5:
        return "Kişiler zayıftır. Boya göre kilonun yetersiz olduğu düşünülür. Diyetisyen ile beraber hazırlanacak program çerçevesinde kilo alması beklenir."
    elif 18.5 <= bmi <= 24.9:
        return "Normal değerdir. Kişiler ideal kilodadır. Düzenli, dengeli ve sağlıklı beslenme yapılması, egzersize hayat rutininde yer verilmesi önerilir."
    elif 25 <= bmi <= 29.9:
        return "Fazla kilolu değerdir. Kişilerin kilosu, boyuna oranla yüksektir. Diyetisyen eşliğinde kişilerin kilo vermesi için çalışmalar yapılmalı, bol spor önerilmelidir."
    elif 30 <= bmi <= 34.9:
        return "Şişman olarak düşünülen bu kişiler, obezite değerleri aralığındadır. Kişilerin kilosu risk oluşturabilecek düzeydedir. Kilo verilmesi önerilir."
    elif 35 <= bmi <= 44.9:
        return "İkinci derece obez olan kişilerin kalp hastalıkları riski görülür. Kişilerin kilo vermesi gerekmektedir. Bu konuda diyetisyen ile beraber bir program oluşturmaları önem arz eder."
    else:
        return "Aşırı kilolu olan kişiler üçüncü derece obezdir. Hastalık riskleri çok yüksek olan bu kişiler, doktor ve diyetisyen kontrolü ile sağlık taramasından geçirilmeli ve kilo vermelidir."

#bmi hesaplayıcı
def bmi_hesaplama():
    try:
        kilo = float(entry.get())
        boy = float(entry2.get()) / 100  # cm'yi metreye çevir
        bmi = kilo / (boy * boy)
        sonuc_label.config(text="BMI : {:.2f}".format(bmi))
        messagebox.showinfo("BMI Açıklama", bmi_aciklama(bmi))  # BMI değerine göre açıklama mesajı göster
    except ValueError:
        sonuc_label.config(text="Lütfen bir sayı giriniz!")

#label  (kilo için)
lab = tkinter.Label(text="Kilonuzu giriniz (kg)")
lab.config(pady=5)
lab.pack()

#entry oluşturma (kilo için)
entry = tkinter.Entry(width=20)
entry.pack()

#label (boy için)
lab2 = tkinter.Label(text="Boyunuzu giriniz (cm)")
lab2.config(pady=5)
lab2.pack()

#entry oluşturma (boy için)
entry2 = tkinter.Entry(width=20)
entry2.pack()

#buton oluşturma
buton = tkinter.Button(text="Hesapla", command=bmi_hesaplama)
buton.place(x=120, y=100)

#sonuc labeli (bmi sonucunu ekrana yazdırmak için)
sonuc_label = tkinter.Label()
sonuc_label.place(x=100, y=160)

tkinter.mainloop()
