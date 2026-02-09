def yüzde(sayi,oran):
   sonuç = sayi * oran/100 
   return sonuç
def enflasyon(enflasyon_orani):
    anaoran = 1
    anaoran = anaoran - enflasyon_orani/1000
    return anaoran 

def yatirilan_para_artis(sayi1,oran):
  sonuc_yatirilan_para = sayi1 * oran/100 
  return sonuc_yatirilan_para

def hesap(a,b,c,d,e,f):
 i = 0
 
 while i < a:
  artis_kazanci = yüzde(b,c)
  b = b + artis_kazanci
  enflasyon_farki = enflasyon(e)
  b = b * enflasyon_farki
  yatirilan_artan = yatirilan_para_artis(d,f)
  d = d + yatirilan_artan
  b = b + d
  i = i + 1
  sonuç = b
 return sonuç 

yil = int(input("yili giriniz: "))
anapara = int(input("anaparayi giriniz: "))
yillik_artiş = int(input("yillik artiş yğzdesini giriniz: "))
eklenecek_para = int(input("yillik eklenecek parayi giriniz: "))
yatirilan_para_artisi = int(input("yillik eklenecek paranin artisini yüzde olarak giriniz: "))
yillik_enflasyon = int(input("yillik enflasyonu giriniz(abd dolari ise %4): "))
yasam_maliyeti = int(input("günümüzdeki aylik  yaşam maliyetini giriniz: "))
sonuç = hesap(yil,anapara,yillik_artiş,eklenecek_para,yillik_enflasyon,yatirilan_para_artisi)
print("/n/n")
print(f"{yil} yil sonunda elinizdeki para: {sonuç} dolar")
sonuc_emekli_ay = sonuç/yasam_maliyeti
print(f"{yil} yil sonunda {sonuc_emekli_ay} ay boyunca ayda {yasam_maliyeti} dolar harcayabilirsiniz.")
print("tüm hesaplar günümüz alim gücü baz alinarak hesaplanmiştir")
