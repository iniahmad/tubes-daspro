from funcsplit import *

def ubah_game (kode_admin) :
    if check_admin(kode_admin):
        id_game = input ("Masukkan ID game: ")
        nama_game = input ("Masukkan nama game: ")
        kategori = input ("Masukkan kategori: ")
        tahun_rilis = input ("Masukkan tahun rilis: ")
        harga = input ("Masukkan harga: ")

        ### kode untuk ubah data game (belum ada)
    else :
        print ("Anda bukan admin, tidak dapat mengubah data game.")

def check_admin (lokasi_kode_admin) :  # check admin
    if lokasi_kode_admin == "admin" :
        return True
    else :
        return False

def check_user (lokasi_kode_user) :  # check user
    if lokasi_kode_user == "user" :
        return True
    else :
        return False

def ubah_stock (kode_admin) :
    if check_admin(kode_admin) :
        id_game = input ("Masukkan ID game: ")
        data = CSVToList(file_path)
        
        list_id = [data[:][0]]
        for data[i][0] in range (1,(data[i]))
        
        if id_game in [list_id] :
            stock_rubah = int (input ("Masukkan jumlah: "))
            
            ## lokasi judul game dari ID yang diminta
            judul_game = "judul game"

            ## lokasi nilai stock dari id, 0 nya nanti diganti
            stock_lama = 0

            if stock_lama + stock_rubah < 0 :
                print ("Stok game" + bold(judul_game) + "gagal dikurangi karena stok kurang. Stok sekarang:" + bold(stock_lama) + "(< {})".format(stock_rubah))

            elif stock_rubah < 0 :
                stock_rubah = int (str (stock_rubah).pop('-'))           # ngilangin minusnya
                print ("Stok game" + (judul_game) + "berhasil dikurangi. Stok sekarang: {}".format((stock_lama - stock_rubah)) )
                ### kode untuk mengurangi stock game (belum ada)

            else :
                print ("Stok game" + (judul_game) + "berhasil ditambah. Stok sekarang: {}".format((stock_lama + stock_rubah)) )
                ### kode untuk menambah stock game (belum ada)

        else : 
            print ("Tidak ada game dengan ID tersebut!")

    else :
        print ("Anda bukan admin, tidak dapat mengubah stock game.")

def buy_game (kode_user):
    if check_user (kode_user):
        id_game = input ("Masukkan ID game: ")

        ## lokasi stock game dari ID yang diminta
        stock_game = 1

        ## lokasi Harga game dari ID yang diminta
        harga_game = 1000

        ## lokasi nama game dari ID yang diminta
        nama_game = "judul game"

        ## lokasi saldo user saat ini
        saldo = 1000

        # cek kepemilikan game oleh user
        if id_game in ["list game yg dimiliki user"]:
            kepemilikan = True
        else :
            kepemilikan = False

        if kepemilikan :
            print ("Anda sudah memiliki Game tersebut!")
        else :
            if saldo_user < harga_game :
                print ("Saldo anda tidak cukup untuk membeli Game tersebut!")
            else :
                if stock_game < 1:
                    print ("Stok Game tersebut sedang habis!")
                else :
                    print ("Game ???" + (nama_game) + "??? berhasil dibeli!")
                    
                    ### kode mengurangi jumlah stock dari game (belum ada)
                    ### kode mengurangi saldo user (belum ada)
    else:
        print ("Anda bukan user. Tidak dapat membeli game.")

def topup (kode_admin) :
    if check_admin(kode_admin) :
        username = input ("Masukkan username: ")

        if username in ["list dari data username"] :
            saldo_rubah = int (input ("Masukkan saldo: "))
            
            ## lokasi jumlah saldo dari username yg diminta
            saldo_awal = 0

            if saldo_rubah + saldo_awal < 0 :
                print ("Masukan tidak valid.")

            elif saldo_rubah < 0 :
                saldo_rubah = int (str (saldo_rubah).pop('-'))           # ngilangin minusnya
                print ("Pengurangan saldo berhasil. Saldo " + (username) + " berkurang menjadi {}.".format((saldo_awal - saldo_rubah)))
                ### kode untuk mengurangi saldo user (belum ada)

            else :
                print ("Top up berhasil. Saldo " + (username) + " bertambah menjadi {}.".format((saldo_awal + saldo_rubah)))
                ### kode untuk menambah saldo user (belum ada)

        else : 
            print ("Username ???" + (username) +"??? tidak ditemukan.")

    else :
        print ("Anda bukan admin, tidak dapat mengubah saldo user.")


## dummy hanya untuk cek sementara
kode_admin = "admin"
kode_user = "user"

start = str (input ("Masukkan perintah : "))

## dummy untuk cek apakah sistem jalan
while start != "exit" :
    if start == "ubah_game":
        ubah_game (kode_admin)
        start = str (input ("\nMasukkan perintah : "))
    elif start == "ubah_stock":
        ubah_stock (kode_admin)
        start = str (input ("\nMasukkan perintah : "))
    elif start == "buy_game":
        buy_game (kode_user)
        start = str (input ("\nMasukkan perintah : "))
    elif start == "topup":
        topup (kode_admin)
        start = str (input ("\nMasukkan perintah : "))
    else :
        print ("Perintah tidak terdaftar di sistem kami.")
        start = str (input ("\nMasukkan perintah : "))

        
        
class color:    ## dummy ngga dipake, simpenan aja
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    


def bold (kata) : 
    return ('\033[1m' + '{}'.format(kata) + '\033[0m')      # bikin kata jadi bold
