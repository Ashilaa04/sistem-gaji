import streamlit as st

st.write(""" # Sistem Hitung Gaji Karyawan Caffe Senja """)
kode_pegawai = st.number_input('Masukan kode', 0)
nama = st.text_input('Masukan Nama')
st.write("1. Manajer \n2. Supervisor \n3. Barista Full Time \n4. Barista Part Time \n5. Cleaning Service")
jabatan = st.text_input('Masukan jabatan karyawan', 0)
alamat = st.text_input('Masukan Alamat')
st.write('1. Mahasiswa/Pelajar \n2. Sudah Menikah \n3. Belum Menikah')
status = st.text_input ('Masukan Status')
jml_anak = st.text_input('Masukan Jumlah Anak', 0)

if (jabatan=='1'):
    gaji_pokok=6500000
    jab="Manajer"
elif(jabatan=='2'):
    gaji_pokok=3500000
    jab="Supervisor"
elif(jabatan=='3'):
    gaji_pokok=1500000
    jab="Barista Full Time"
elif(jabatan=='4'):
    gaji_pokok=1000000
    jab="Barista Part Time"
elif(jabatan=='5'):
    gaji_pokok=800000
    jab="Cleaning Service"

if(status== '1'):
    tambahan = gaji_pokok*10/100
elif(status== '2'):
    tambahan = gaji_pokok*10/100
elif(status== '3'):
    tambahan = gaji_pokok*10/100

jumlah_gaji = gaji_pokok+tambahan

if(jml_anak=='3'):
    tunjangan=1000000
elif(jml_anak =='2'):
    tunjangan=750000
elif(jml_anak =='1'):
    tunjangan= 500000
else:
    tunjangan=0

gaji_bersih = jumlah_gaji+tunjangan

if (st.button('HITUNG GAJI')):
    st.success('Gaji Bersih adalah {}.'.format(gaji_bersih))
    st.write ("\n")
    st.write ("===============================================================================")
    st.write ("Slip Gaji Karyawan")
    st.write ("===============================================================================")
    st.write ("")
    st.write ("Kode Pegawai: ",kode_pegawai)
    st.write ("Nama        : ",nama)
    st.write ("Jabatan     : ",jab)
    st.write ("Alamat      : ",alamat)
    st.write ("===============================================================================")
    st.write ("Jumlah Anak :",jml_anak)
    st.write ("Gaji Kotor  : ",jumlah_gaji)
    st.write ("*******************************************************************************")
    st.write ("Status      : ",status)
    st.write ("Gaji bersih : ",gaji_bersih)
    st.write ("")
    st.write ("===============================================================================")
    st.write ("")