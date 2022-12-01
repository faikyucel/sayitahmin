import random
import time
print('''
******************************************
Sayı Oyununa Hoşgeldiniz
Kaç hakknız kalırsa o kadar x alırsınız
sayı 1 ile 100 arsında
*******************************************
''')
tahmin_hak=5
rastgele_sayi=random.randint(1,100)
bakiye=0
bahis_miktar=int(input('bahis miktarı:'))
while True:


    tahmin=int(input('tahmininizi giriniz:'))


    if (rastgele_sayi<tahmin):
        print("{}'sayısından küçük".format(tahmin))
        tahmin_hak-=1

    elif (rastgele_sayi>tahmin):
        print("{}'sayısından büyük".format(tahmin))
        tahmin_hak-=1

    elif (rastgele_sayi==tahmin):
        print('kontrol ediliyor')
        time.sleep(2)
        print('aferin')
        if tahmin_hak==5:
            print('ÇOK İYİ 5x ')
            bakiye+=bahis_miktar*5
            print('kasadaki paranız:{}'.format(bakiye))
        elif tahmin_hak==4:
            print('İYİ 4x')
            bakiye += bahis_miktar * 4
            print('kasadaki paranız:{}'.format(bakiye))
        elif tahmin_hak == 3:
            print('EH İŞTE 3x')
            bakiye += bahis_miktar * 3
            print('kasadaki paranız:{}'.format(bakiye))
        elif tahmin_hak == 2:
            print('BAŞARILI 2x')
            bakiye += bahis_miktar * 2
            print('kasadaki paranız:{}'.format(bakiye))
        else:
            print('amorti')
            bakiye += bahis_miktar
            print('kasadaki paranız:{}'.format(bakiye))
        break


    if (tahmin_hak==0):
        print(""
            "*************"
              " HAKKIN BİTTİ "
              "************")
        print('sayımız:{}'.format(rastgele_sayi))
        x=0-bahis_miktar
        print('kasadaki paranız:{}'.format(x))
        break

