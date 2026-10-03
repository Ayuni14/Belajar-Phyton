#Tugas 2 Prak. Pemograman Lanjutan 3F
#Membuat program dictionary dari 10 baris Riwayat terakhir Spotify/Youtube dan mengekstrak data secara manual

#Bagian ini berfungsi sebagai tampilan awal program untuk menampilkan judul program, nama,NIM dan ucapan selamat datang.
print("=====================================================================")
print("======================== Riwayat Music Spotify ======================")
print("=========================== Ayuni Maynisa ===========================")
print("============================ 2503015079 =============================")

print("Hai! Selamat datang di Riwayat Music Spotify Ayuni Maynisa")


# Dictionary berisi 10 riwayat lagu Spotify
# ini adalah variabel riwayatSpotify bertipe data Dictionary
# angka 1-10 adalah Key (kunci luar/ID lagu), nah didalamnya ada inner key, yaitu "judul", "artis", dan "platform"
riwayatSpotify = {
    1: {
        "judul": "Anything You Want",
        "artis": "Reality Club",
        "platform": "Spotify"
    },
    2: {
        "judul": "Man Upon The Hill",
        "artis": "Stars and Rabbit",
        "platform": "Spotify"
    },
    3: {
        "judul": "Training Season",
        "artis": "Dua Lipa",
        "platform": "Spotify"
    },
    4: {
        "judul": "Janji Palsu",
        "artis": "Hindia",
        "platform": "Spotify"
    },
    5: {
        "judul": "Duniawi",
        "artis": "rumahsakit",
        "platform": "Spotify"
    },
    6: {
        "judul": "Berpayung Tuhan",
        "artis": "Nadin Amizah",
        "platform": "Spotify"
    },
    7: {
        "judul": "A Sorrowful Reunion",
        "artis": "Reality Club",
        "platform": "Spotify"
    },
    8: {
        "judul": "Jikalau",
        "artis": "Naif",
        "platform": "Spotify"
    },
    9: {
        "judul": "Aku Ada Untukmu",
        "artis": "Perunggu",
        "platform": "Spotify"
    },
    10: {
        "judul": "Argata",
        "artis": "Romi Jahat, Nully",
        "platform": "Spotify"
    }
}

#\n = simbol newline untuk memberi jarak baris baru di atasnya
#riwayatSpotify[1] = memanggil seluruh isi data lagu ke-1 (hasilnya berbentuk dictionary utuh)
print("\nLagu terakhir yang saya dengar adalah :", riwayatSpotify[1])
print("======================================================================")

# menampilkan riwayat lagu satu per satu
# riwayatSpotify[1]["artis"] = mengambil nilai artis pada lagu ke-1.
# riwayatSpotify[1]["judul"] = mengambil nilai judul pada lagu ke-1
print("Riwayat lagu Spotify saya adalah :", riwayatSpotify[1]["artis"], ",", riwayatSpotify[1]["judul"])
print("Riwayat lagu Spotify saya adalah :", riwayatSpotify[2]["artis"], ",", riwayatSpotify[2]["judul"])
print("Riwayat lagu Spotify saya adalah :", riwayatSpotify[3]["artis"], ",", riwayatSpotify[3]["judul"])
print("Riwayat lagu Spotify saya adalah :", riwayatSpotify[4]["artis"], ",", riwayatSpotify[4]["judul"])
print("Riwayat lagu Spotify saya adalah :", riwayatSpotify[5]["artis"], ",", riwayatSpotify[5]["judul"])
print("Riwayat lagu Spotify saya adalah :", riwayatSpotify[6]["artis"], ",", riwayatSpotify[6]["judul"])
print("Riwayat lagu Spotify saya adalah :", riwayatSpotify[7]["artis"], ",", riwayatSpotify[7]["judul"])
print("Riwayat lagu Spotify saya adalah :", riwayatSpotify[8]["artis"], ",", riwayatSpotify[8]["judul"])
print("Riwayat lagu Spotify saya adalah :", riwayatSpotify[9]["artis"], ",", riwayatSpotify[9]["judul"])
print("Riwayat lagu Spotify saya adalah :", riwayatSpotify[10]["artis"], ",", riwayatSpotify[10]["judul"])


# ini untuk menampilkan seluruh rincian informasi lagu (judul, artis, dan platform) secara rapi satu per satu
print("======================================================================")
print("ini adalah riwayat lagu yang saya dengarkan tadi:")

# menampilkan detail seluruh lagu secara manual
print("1. Judul    :", riwayatSpotify[1]["judul"])
print("   Artis    :", riwayatSpotify[1]["artis"])
print("   Platform :", riwayatSpotify[1]["platform"])

print("2. Judul    :", riwayatSpotify[2]["judul"])
print("   Artis    :", riwayatSpotify[2]["artis"])
print("   Platform :", riwayatSpotify[2]["platform"])

print("3. Judul    :", riwayatSpotify[3]["judul"])
print("   Artis    :", riwayatSpotify[3]["artis"])
print("   Platform :", riwayatSpotify[3]["platform"])

print("4. Judul    :", riwayatSpotify[4]["judul"])
print("   Artis    :", riwayatSpotify[4]["artis"])
print("   Platform :", riwayatSpotify[4]["platform"])

print("5. Judul    :", riwayatSpotify[5]["judul"])
print("   Artis    :", riwayatSpotify[5]["artis"])
print("   Platform :", riwayatSpotify[5]["platform"])

print("6. Judul    :", riwayatSpotify[6]["judul"])
print("   Artis    :", riwayatSpotify[6]["artis"])
print("   Platform :", riwayatSpotify[6]["platform"])

print("7. Judul    :", riwayatSpotify[7]["judul"])
print("   Artis    :", riwayatSpotify[7]["artis"])
print("   Platform :", riwayatSpotify[7]["platform"])

print("8. Judul    :", riwayatSpotify[8]["judul"])
print("   Artis    :", riwayatSpotify[8]["artis"])
print("   Platform :", riwayatSpotify[8]["platform"])

print("9. Judul    :", riwayatSpotify[9]["judul"])
print("   Artis    :", riwayatSpotify[9]["artis"])
print("   Platform :", riwayatSpotify[9]["platform"])

print("10. Judul   :", riwayatSpotify[10]["judul"])
print("    Artis   :", riwayatSpotify[10]["artis"])
print("    Platform:", riwayatSpotify[10]["platform"])