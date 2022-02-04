from os import extsep


mahsulotlar = {'pepsi': 5000,
               'kitkat': 4000,
               'raffaello': 6000,
               '18+': 8000,
               'plitka': 5000,
               'baunty': 4000,
               'snickers': 5000,
               'supper kontic': 5000}

mahsulotlar_raqami = {1: 'pepsi',
                      2: 'kitkat',
                      3: 'raffaello',
                      4: '18+',
                      5: 'plitka',
                      6: 'baunty',
                      7: 'snickers',
                      8: 'supper kontic'}

mahsulotlar_miqdori = {'pepsi': 13,
                       'kitkat': 25,
                       'raffaello': 0,
                       '18+': 4,
                       'plitka': 5,
                       'baunty': 6,
                       'snickers': 7,
                       'supper kontic': 8}


# savol = "Pul kiriting"
# savol += "(agar dasturni toxtatmoqchi bolsangiz 'stop' deb yozing):"
sum = 0


def valyuta():
    try:
        global sum
        kupyuralar = [1000, 2000, 5000, 10000]
        foydalanochi = input("Pul kiriting\n(agar fasturni toxtatmoqchi bolsangiz 'exit' debyozing): ")
        if foydalanochi == 'exit':
            return f'\nbalans:{sum}-sum'
        elif int(foydalanochi) in kupyuralar:
            sum += int(foydalanochi)
            print(f"\nBalans:{sum} sum")
            return ''
        else:
            print(
                f"\n{foydalanochi} - bunday kupyura mavjud eams!\nQayta urinib koring")
            print(valyuta())
            return ''
    except:
        print(valyuta())
   
# print(valyuta())


def mahsulot():
    try:
        global sum
        for i, tavar in enumerate(mahsulotlar, 1):
            print(f"{i}.{tavar}-{mahsulotlar[tavar]} sum, {mahsulotlar_miqdori[tavar]} dona")
        savol = input(
            "\nMahsulotlar raqamini tanlang(dasturni toxtatish uchun 'exit' deb yozing): ")
        if savol == 'exit':
            return ''
        elif int(savol) in mahsulotlar_raqami:
            if mahsulotlar[tavar] <= sum:
                if mahsulotlar_miqdori[mahsulotlar_raqami[int(savol)]] > 0:
                    print(f"\n{mahsulotlar_raqami[int(savol)]} tanlandi")
         
                    mahsulotlar_miqdori[mahsulotlar_raqami[int(savol)]] = mahsulotlar_miqdori[mahsulotlar_raqami[int(savol)]] -1
                    sum = sum - mahsulotlar[mahsulotlar_raqami[int(savol)]]
                elif mahsulotlar_miqdori[mahsulotlar_raqami[int(savol)]] == 0:
                    print(f"\nBunday mahsulot qolmagan uzr!")
            else:
                print("\n Sizda yetarli mablag' mavjud emas!")        
        else:
            print("\nBunday raqam mavjud emas!"
                  "\nQayta urinib koring: ")
            print(mahsulot())
        return ''
    except:
        print(mahsulot())
# print(mahsulot())


def pul_yetadigan_mahsulot():
    try:
        global sum
        for i, tavar in enumerate(mahsulotlar, 1):
            if sum >= mahsulotlar[tavar]:
                print(f"{i}.{tavar} - {mahsulotlar[tavar]} sum, {mahsulotlar_miqdori[tavar]} dona")
        savol = input(
            "\nMahsulotlar raqamini tanlang(dasturni toxtatmoqchi bolsangiz 'exit' deb yozing): ")
        if savol == 'exit':
            return ''
        elif int(savol) in mahsulotlar_raqami:
            print(f"{mahsulotlar_raqami[int(savol)]} tanlandi")
            mahsulotlar_miqdori[mahsulotlar_raqami[int(savol)]] = mahsulotlar_miqdori[mahsulotlar_raqami[int(savol)]] -1
            sum = sum - mahsulotlar[mahsulotlar_raqami[int(savol)]]
        else:
            print("\nBunday raqam mavjud emas!"
                  "\nQayta urunib koring: ")
            print(pul_yetadigan_mahsulot())      
        return ''
    except:
        print(pul_yetadigan_mahsulot())
# print(pul_yetadigan_mahsulot())


def qaytim():
    return f"{sum} sum"


def bankamat():
    while True:
        try:
            mijoz = input("""Tanlang: 
                    1. Pul kiritish: 
                    2.Mahsulotlar royxati: 
                    3.Pulingiz yetadigan mahsulot: 
                    4.Balans
                    5.Qaytim
                    : """)
            if mijoz == '1':
                print(valyuta())
            elif mijoz == '2':
                print(mahsulot())
            elif mijoz == '3':
                print(pul_yetadigan_mahsulot())
            elif mijoz == '4':
                print(qaytim())
            else:
                print(qaytim())
                return ''
                
        
                
        except:
            print(bankamat())

print(bankamat())


