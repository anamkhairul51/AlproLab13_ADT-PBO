class orang(object):
    'Memuat nama, alamat dan list no telp'
    def __init__(self, nama, alamat, lsTelp):
        self.nama = nama
        self.alamat = alamat
        self.lsTelp = lsTelp

    def __str__(self):
        s = ''
        for notelp in sorted(self.lsTelp):
            s = s + self.nama + '\t alamat:' + self.alamat + '\t NoTelp:' +  notelp + '\n'
        
        return s

class bukuTelp(object):
    'Memuat kontak semua orang dan operasinya'
    def __init__(self):
        self.kontak = {}
    
    def tambah(self, nama, alamat, lsTelp):
        p = orang(nama, alamat, lsTelp)
        self.kontak[nama] = p

    def hapus(self, nama):
        del(self.kontak[nama])
    
    def __str__(self):
        s = ''
        for p in sorted(self.kontak):
            s = s + str(self.kontak[p]) + '\n'
        return s

    def __call__(self, nama):
        return self.kontak[nama]

def main():
    b = bukuTelp()
    b.tambah('Bunga', 'Jln. Kembang', ['032674458'])
    b.tambah('Nisa', 'Jln. Mawar', ['0126598', '0211362321'])
    b.tambah('Adi', 'Jln. Melati', ['09856746321'])
    print('Data Awal')
    print(b)
    setattr(b('Nisa'), 'alamat', 'Jln. Pelangi')
    print('Data nisa saja setelah manipulasi')
    print(b('Nisa'))
    b.hapus('Bunga')
    print('Data setelah dihapus')
    print(b)

if __name__=='__main__':
    main()