## import library matematika
import math

#fungsi fungsi statistik yang ingin dicari

#fungsi untuk mencari nilai rata-rata
def cari_mean(data_list):
    
    jumlah_data = 0
    #panjang data
    panjang_data = len(data_list) 
    for bilangan in data_list:
        jumlah_data += bilangan
    #hitung rata-rata = jumlah data / panjang data
    rata_rata_data = jumlah_data/panjang_data
    return rata_rata_data

#fungsi untuk mencari nilai median
def cari_median(data_list):
    data_list.sort() #pengurutan data
    panjang_data=len(data_list) #panjang data
    i_tengah=panjang_data//2 #pembulatan ke bawah
    
    if panjang_data % 2 == 1: #jika data ganjil
        return data_list[i_tengah] #maka nilainya adalah nilai tengah
    else: #jika panjang data genap
        return ((data_list[i_tengah]-1)+data_list[i_tengah])/2 
        #data ganjil + data genap di bagi 2
    
#fungsi modus
def cari_modus(data_list):
    
    #dictionary untuk mapping nilai terbanyak
    #pakek map() juga bisa
    peta_kemunculan = {}
    
    #perulangan bilangan dalam list, pengecekan 
    for bilangan in data_list:
        if bilangan in peta_kemunculan:
            peta_kemunculan[bilangan] += 1
        else:
            peta_kemunculan[bilangan] = 1
        
    #menghitung data yang sering muncul
    Modus = data_list[0]
    for bilangan in peta_kemunculan.keys():
        jumlah = peta_kemunculan[bilangan]
        
        if jumlah > peta_kemunculan[Modus]:
            Modus = bilangan
    return Modus

#fungsi cari_varians(ragam)
def cari_varians(data_list):
    #fungsi rata-rata
    rata_rata = cari_mean(data_list)
    
    panjang_data = len(data_list) #panjang data
    #variabel ini untuk menyimpan x - x_rata_rata
    #kuadrat_selisih_rata_rata
    kuadrat_selisih_rata_rata = []
    
    #variabel ini untuk menampung nilai jumlahannya kuadrat_selisih_rata_rata
    total_selisih_rata_rata = 0
    
    for bilangan in data_list:
        kuadrat_selisih_rata_rata.append((bilangan-rata_rata)**2)
        
    #menghitung hasil jumlahannya
    for nilai in kuadrat_selisih_rata_rata:
        total_selisih_rata_rata += nilai
        
    varians = total_selisih_rata_rata / panjang_data 
    return varians

#fungsi cari_simpangan baku atau standart devasi
def cari_simpangan_baku(data_list):
    #standart deviasi atau simpangan baku = akar dari Varians
    
    #panggil fungsi varians kedalam fungsi simpangan baku
    Varians = cari_varians(data_list)
    #hitung simpangan baku
    simpangan_baku = math.sqrt(Varians)
    return simpangan_baku

#fungsi cari_jangkauan
def cari_jangkauan(data_list):
    #mencari nilai terbesar
    nilai_terbesar = data_list[0]
    for bilangan in data_list:
        if bilangan > nilai_terbesar:
            nilai_terbesar = bilangan 
    #mencari nilai terkecil
    nilai_terkecil = data_list[0]
    for nilai in data_list:
        if nilai < nilai_terkecil:
            nilai_terkecil = nilai 
            
    jangkauan =nilai_terbesar-nilai_terkecil
    return jangkauan

#fungsi cari_kuartil
def kuartil():
    def cari_kuartil(data_list):
        data_list.sort()
        index = []
        panjang_data = len(data_list)
        Q2 = 0
        if panjang_data % 2 == 0: 
            index.append(int(panjang_data/2)-1)
            index.append(int(panjang_data/2))
        
            Q2 = (data_list[index[0]] + data_list[index[1]])/2
            pass
        else:
            index.append(int(panjang_data/2))
        
            Q2 = data_list[index[0]]
        return Q2, index
    Q2, Q2_index = cari_kuartil(data_list)
    Q1, Q1_index = cari_kuartil(data_list[ :Q2_index[0]])
    Q3, Q3_index = cari_kuartil(data_list[Q2_index[-1]+1:])
    return Q1, Q2, Q3

#fungsi untuk mencari nilai rata-rata kuartil
def cari_rata_rata_kuartil():
    Kuartil = kuartil()
    jumlah_kuartil = 0
    for bilangan in Kuartil:
        jumlah_kuartil += bilangan
    return jumlah_kuartil

#fungsi untuk mencari nilai jangkauan kuartil
def cari_jangkauan_kuartil():
    Quartile = kuartil()
    Q_1 = Quartile[0]
    Q_3 = Quartile[2]
    jangkauan_kuartil = (Q_3 - Q_1)
    return jangkauan_kuartil

#fungsi untuk mencari simpangan kuartil
def cari_simpangan_kuartil():
    jangkauan_kuartil = cari_jangkauan_kuartil()
    simpangan_kuartil = jangkauan_kuartil/2
    return simpangan_kuartil

#fungsi untuk mencari nilai desil
def cari_desil(data_list):
    if len(data_list) < 10:
        print("Data kurang panjang untuk mencari desil")
    else:
        def desil(data_list):
            data_list.sort()
    
            panjang_data = len(data_list)
    
            # nilai desil ada 9 yaitu D1 sampai D9
            index_list=[] #list untuk menyimpan index
            for i in  range(1,10): #sepuluh batas atas yang tidak di ikutkan
                index=index_list.append((i*(panjang_data+1))/10)
        
            #pemisahan bilangan bulat dan desimal  
            int_desil_i = [] #list untuk menyimpan bilangan bulat ke i
            desimal_desil_i = [] #list untuk menyimpan bilangan desimalnya ke i
            for bilangan in index_list:
                int_desil = int_desil_i.append(int(bilangan))
                desimal_desil= desimal_desil_i.append(round(bilangan-int(bilangan),2))
        
            #menghitung yang nilai bulat
            Desil_int = []
            for j in range(0,9):
                hitung = Desil_int.append(data_list[int_desil_i[j]-1])
    
            #menghitung yang nilai desimal
            Desil_desimal = []
            for k in range(0,9):
                desimal = Desil_desimal.append(
                    round((desimal_desil_i[k])*(data_list[int_desil_i[k]]-data_list[int_desil_i[k]-1]),2)
                    )
            Desil_total = [] #list untuk menghitung total
            #menghitung nilai total bilangan bulat + bilang desimalnya
            for L in range(0,9):
                total= Desil_total.append(Desil_int[L]+Desil_desimal[L])
            return Desil_total
    return desil(data_list)

if __name__ == "__main__":
    
    print("===kalkulator Statistika===")
    #inputan data
    masukkan_data= input("Masukkan data (pisahkan data dengan tanda koma ( , )) : ")
    data_list = []
    #konversi inputan ke dalam list
    for bilangan in masukkan_data.split(','):
        data_list.append(int(bilangan))
        
    #masuk calculator
    print('\nData list',data_list)
    while True:
        print("\n===Menu Kalkulator===")
        print( 
        """1.Mean \n2.Median \n3.Modus \n4.Varians/Ragam \n5.Simpangan Baku 
6.Jangkauan/Range\n7. Kuartil 8. Rata-rata Kuartil
9.Jangkauan Antar kuartil \n10. Simpangan Kuartil \n11.Desil  """
         )
        while True:
            #conditonal if
            menu= input("\nMasukkan plihan menu 1-12 : ")
            if menu == '1':
                print('\nNilai rata-ratanya adalah : ', cari_mean(data_list))
                break
            elif menu == '2':
                print('\nNilai mediannya adalah : ', cari_median(data_list))
                break
            elif menu == '3':
                print("\nNilai modusnya adalah : ", cari_modus(data_list))
                break
            elif menu == '4':
                print("\nNilai Variansnya adalah : ", cari_varians(data_list))
                break
            elif menu == '5':
                print("\nNilai Simpangan Bakunya adalah : ", cari_simpangan_baku(data_list))
                break
            elif menu == '6':
                print("\nNilai jangkauannya adalah : ", cari_jangkauan(data_list))
                break
            elif menu == '7':
                print ("\nNilai kuartilnya adalah : ", kuartil())
                break
            elif menu == '8':
                print("\nNilai Rataan kuartilnya adalah : ", cari_rata_rata_kuartil())
                break
            elif menu == '9':
                print("\nNilai Jangkauan antar kuartilnya adalah  : ", cari_jangkauan_kuartil())
                break
            elif menu == '10':
                print("\nNilai Simpangan kuartilnya adalah : ", cari_simpangan_kuartil())
                break
            elif menu == '11':
                print("\nNilai Desilnya adalah : ", cari_desil(data_list))
                break
            else:
                print('Menu kosong')
                break
        #code untuk kembali ke menu atau keluar
        Ulang = int(input("\n kembali ke Menu \n1.YA \n2.exit() :\n"))
        if Ulang == 2:
            print ("==Kalkulator statistika ditutup===")
            print("========TERIMAKASIH BANYAK=========")
            print("===========Kelompok XX=============")
            break
        else:
            print("====================================")