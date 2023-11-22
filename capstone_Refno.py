Data_Pasien = [
    {
        'No_Rekam_Medis' : 23100001,
        'Nama_Pasien' : 'Adam',
        'Jenis_Kelamin' : 'Laki-laki',
        'Usia' : '34',
        'Diagnosa' : 'Flu',
        'Dokter' : 'dr. Aubrie',
        'Perawatan' : 'Rawat Jalan',
    },
    {
        'No_Rekam_Medis' : 23100002,
        'Nama_Pasien' : 'Yanti',
        'Jenis_Kelamin' : 'Perempuan',
        'Usia' : '46',
        'Diagnosa' : 'Asma',
        'Dokter' : 'dr. Aubrie',
        'Perawatan' : 'Rawat Jalan',
    },
    {
        'No_Rekam_Medis' : 23100003,
        'Nama_Pasien' : 'Budi',
        'Jenis_Kelamin' : 'Laki-laki',
        'Usia' : '23',
        'Diagnosa' : 'Asma',
        'Dokter' : 'dr. Ashraf',
        'Perawatan' : 'Rawat Jalan',
    },
    {
        'No_Rekam_Medis' : 23100004,
        'Nama_Pasien' : 'Bayu',
        'Jenis_Kelamin' : 'Laki-laki',
        'Usia' : '31',
        'Diagnosa' : 'Asma',
        'Dokter' : 'dr. Aubrie',
        'Perawatan' : 'Rawat Inap',
    },
    {
        'No_Rekam_Medis' : 23100005,
        'Nama_Pasien' : 'Siska',
        'Jenis_Kelamin' : 'Perempuan',
        'Usia' : '42',
        'Diagnosa' : 'Jantung',
        'Dokter' : 'dr. Aubrie',
        'Perawatan' : 'Rawat Inap',
    },
    {
        'No_Rekam_Medis' : 23100006,
        'Nama_Pasien' : 'Dodi',
        'Jenis_Kelamin' : 'Laki-laki',
        'Usia' : '24',
        'Diagnosa' : 'Asma',
        'Dokter' : 'dr. Ashraf',
        'Perawatan' : 'Rawat Inap',
    },
]

def refno():
    print(f'''
        Selamat Datang di RS Kasih Bunda Sepanjang Masa
        List Menu :
        1. Data Pasien
        2. Menambah Data Pasien
        3. Menghapus Data Pasien
        4. Mengupdate Data Pasien
        5. Keluar Program
    ''')

def pilih_opsi():
    pilih = int(input('Masukkan Pilihan Anda :'))
    return pilih

def refno1():
    print(f'''
    =============== Menu #1: Data Pasien ==============
        1. Semua Data Pasien
        2. Data Pasien Tertentu
        3. Back
''')

def refno2():
    print(f'''
    =============== Menu #2: Menambah Pasien ==============
        1. Menambah Data Pasien
        2. Back to Menu Utama
''')
    
def kembali():
    pilih = str(input('Kembali ke Menu sebelumnya ? (Y/N):').capitalize())
    return pilih

def lihat_pasien(Data_Pasien):
    print('index\t| No. Rekam Medis| Nama Pasien\t|   Jenis Kelamin   |   Usia    |   Diganosa    |   Dokter    \t|   Perawatan   |')
    for i in range(len(Data_Pasien)):
        print(f"{i}\t| {Data_Pasien[i]['No_Rekam_Medis']}\t | {Data_Pasien[i]['Nama_Pasien']} \t|   {Data_Pasien[i]['Jenis_Kelamin']}\t    | {Data_Pasien[i]['Usia']}\t|    {Data_Pasien[i]['Diagnosa']}\t|   {Data_Pasien[i]['Dokter']}\t|   {Data_Pasien[i]['Perawatan']}\t|")
    return

def Pasien_Tertentu():
    No_Rekam_Medis = int(input('''Silahkan masukkan No Rekam Medis :'''))
    for i in range(len(Data_Pasien)):
        if No_Rekam_Medis == Data_Pasien[i]['No_Rekam_Medis']:
            print(' ======== Data Pasien Tertentu =========')
            print('index\t| No. Rekam Medis| Nama Pasien\t|   Jenis Kelamin   |   Usia    |   Diganosa    |   Dokter    \t|  Perawatan   |')
            print(f"{i}\t| {Data_Pasien[i]['No_Rekam_Medis']}\t | {Data_Pasien[i]['Nama_Pasien']} \t|   {Data_Pasien[i]['Jenis_Kelamin']}\t    | {Data_Pasien[i]['Usia']}\t|    {Data_Pasien[i]['Diagnosa']}\t|   {Data_Pasien[i]['Dokter']}\t|  {Data_Pasien[i]['Perawatan']}\t|")
            break
        elif (i == len(Data_Pasien)-1) and (No_Rekam_Medis != Data_Pasien[i]['No_Rekam_Medis']):
            print('==== Data yang dimasukkan tidak ada ====')

def menambah(Data_Pasien):
    lihat_pasien(Data_Pasien)
    while True:
        No_Rekam_Medis = int(input('masukkan No. Rekam Medis :'))
        for i in range(len(Data_Pasien)):
            if No_Rekam_Medis == (Data_Pasien[i]['No_Rekam_Medis']):
                print("Data dengan No rekam medis tersebut sudah ada")
                break
            else:
                Nama_Pasien = str.title(input('Masukan Nama Pasien : '))
                Jenis_Kelamin = str.title(input('Masukkan Jenis Kelamin :'))
                Usia = int(input('Masukkan Usia :'))
                Diagnosa = str.title(input('Masukkan Diagnosa :'))
                Dokter = str.title(input('Masukkan Nama Dokter :'))
                Perawatan = str.title(input('Masukkan Jenis Perawatan :'))
                cek = str(input('Apakah yakin ingin menambahkakn data tersebut? (Y/N) :'))
                if cek == 'Y':
                    Data_Pasien.append({
                        'No_Rekam_Medis': No_Rekam_Medis,
                        'Nama_Pasien': Nama_Pasien,
                        'Jenis_Kelamin': Jenis_Kelamin,
                        'Usia': Usia,
                        'Diagnosa': Diagnosa,
                        'Dokter': Dokter,
                        'Perawatan': Perawatan,
                    })
                    lihat_pasien(Data_Pasien)
                    break
                else:
                    print('Data tidak jadi di tambahkan')
                    lihat_pasien(Data_Pasien)
                    break
                return

def update():
    lihat_pasien(Data_Pasien)
    No_Rekam_Medis = int(input('=== Masukkan No_Rekam_Medis yang ingin update : '))
    for i in range (len(Data_Pasien)):
        if No_Rekam_Medis == Data_Pasien[i]['No_Rekam_Medis']:
            while True:
                print('====  Data Pasien :  ====')
                print('index\t| No. Rekam Medis| Nama Pasien\t|   Jenis Kelamin   |   Usia    |   Diganosa    |   Dokter    \t|  Perawatan   |')
                print(f"{i}\t| {Data_Pasien[i]['No_Rekam_Medis']}\t | {Data_Pasien[i]['Nama_Pasien']} \t|   {Data_Pasien[i]['Jenis_Kelamin']}\t    | {Data_Pasien[i]['Usia']}\t|    {Data_Pasien[i]['Diagnosa']}\t|   {Data_Pasien[i]['Dokter']}\t|   {Data_Pasien[i]['Perawatan']}\t|")
                break
            Tes = input('Anda yakin untuk update data (Y/T) : ').capitalize()
            if Tes == 'Y':
                update_pasien = input('''Silahkan pilih data yang ingin anda update (No_Rekam_Medis, Nama_Pasien, Jenis_Kelamin, Usia, Diagnosa, Dokter, Perawatan ): ''').capitalize()
                if update_pasien == Data_Pasien[i]['No_Rekam_Medis'] :
                    update_pasien = update_pasien
                else:
                    update_pasien = update_pasien
                    update_data = input(f'Silahkan masukkan {update_pasien} yang baru : ').capitalize()
                while True:
                    cekk = input('Anda yakin untuk update data (Y/T) : ').capitalize()
                    if cekk == 'Y':
                        Data_Pasien[i][update_pasien] = update_data
                        print('==== Data Pasien sudah terupdate ====')
                        lihat_pasien(Data_Pasien)
                        break
                        continue
                    elif cekk == 'T':
                        print('==== Data tidak diubah ====')
                        lihat_pasien(Data_Pasien)
                        break
        elif (i == len(Data_Pasien)-1) and (No_Rekam_Medis != Data_Pasien[i]['No_Rekam_Medis']):
            print('Data yang dimasukkan tidak ada ')
            #kembali()
        else:
            continue
        return
          
def hapus(Data_Pasien):
    lihat_pasien(Data_Pasien)
    while True:
        index_pasien = int(input('Masukkan Index data pasien yang ingin di hapus :'))
        cek = str(input('Apakah anda yakin? (Y/N)')).capitalize()
        if (cek == 'Y'):
            del Data_Pasien[index_pasien]
            lihat_pasien(Data_Pasien)
            print('Data berhasil di hapus')
        else:
            continue
        return

while True:
    refno()
    pilih_menu = int(input('Masukkan angka pilihan yang ingin di jalankan : '))
    if (pilih_menu == 1):
        while True:
            refno1()
            pilih = pilih_opsi()
            if (pilih == 1):
                print('========== Menu #1: Data Pasien =========')
                lihat_pasien(Data_Pasien)
            elif (pilih == 2 ):
                print('========== Menu #1.2: Tampilkan Data Pasien Tertentu ==========')
                Pasien_Tertentu()
            elif (pilih == 3 ):
                break
            else:
                print('Pilihan tidak tersedia')
                continue
            pilih = kembali()
            if (pilih == 'Y'):
                break
            else:
                continue
                        
    elif (pilih_menu == 2):
        while True:
            refno2()
            pilih =  pilih_opsi()
            if (pilih ==  1):
                while True:
                    print('========== Menu #2 :Tambah Pasien =======')
                    menambah(Data_Pasien)
            elif (pilih == 2):
                break
            else:
                print('Pilihan yang anda masukkan tidak tersedia (pilih 1-2)')
                pilih = kembali()
                if (pilih == 'Y'):
                    break
                else:
                    continue
            
    elif (pilih_menu == 3):
        while True:
            print('========== Menu 3 : Menghapus Data Pasien ==========')
            hapus(Data_Pasien)
            pilih = kembali()
            if (pilih == 'Y'):
                break
            else:
                continue
    elif (pilih_menu == 4):
        while True:
            print('========== Menu 4 Update Data Pasien ==========')
            update()
            pilih = kembali()
            if (pilih == 'Y'):
                break
            else:
                continue
    elif (pilih_menu == 5 ):
        break
    else:
        print('Pilihan yang anda masukkan tidak tersedia')
        continue

