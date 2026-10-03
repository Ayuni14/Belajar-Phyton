# Program Dictionary Riwayat Spotify Ayuni Maynisa

import time

print("--------------------------------")
print("------Riwayat Music Spotify-----")
print("---------Ayuni Maynisa----------")
print("--------------------------------")

# Tanpa input(), langsung menggunakan variabel string
namaLengkap = "Ayuni Maynisa"

print("Halo.. Selamat datang", namaLengkap, "di Riwayat Music Spotify ku ")

# Dictionary 10 riwayat lagu Spotify
riwayatSpotify = {
    1: {
        "judul": "Anything You Want",
        "artis": "Reality Club",
        "platform": "Spotify"
    },
    2: {
        "judul": "Isi Judul Lagu 2",
        "artis": "Nama Artis 2",
        "platform": "Spotify"
    },
    3: {
        "judul": "Isi Judul Lagu 3",
        "artis": "Nama Artis 3",
        "platform": "Spotify"
    },
    4: {
        "judul": "Isi Judul Lagu 4",
        "artis": "Nama Artis 4",
        "platform": "Spotify"
    },
    5: {
        "judul": "Isi Judul Lagu 5",
        "artis": "Nama Artis 5",
        "platform": "Spotify"
    },
    6: {
        "judul": "Isi Judul Lagu 6",
        "artis": "Nama Artis 6",
        "platform": "Spotify"
    },
    7: {
        "judul": "Isi Judul Lagu 7",
        "artis": "Nama Artis 7",
        "platform": "Spotify"
    },
    8: {
        "judul": "Isi Judul Lagu 8",
        "artis": "Nama Artis 8",
        "platform": "Spotify"
    },
    9: {
        "judul": "Isi Judul Lagu 9",
        "artis": "Nama Artis 9",
        "platform": "Spotify"
    },
    10: {
        "judul": "Isi Judul Lagu 10",
        "artis": "Nama Artis 10",
        "platform": "Spotify"
    }
}

print("Lagu terakhir yang kamu dengar adalah :", riwayatSpotify[1])
print("====================================")

# Menampilkan judul satu per satu secara manual
print("Riwayat lagu-lagumu dari Spotify adalah :", riwayatSpotify[1]["judul"])
print("Riwayat lagu-lagumu dari Spotify adalah :", riwayatSpotify[2]["judul"])
print("Riwayat lagu-lagumu dari Spotify adalah :", riwayatSpotify[3]["judul"])
print("Riwayat lagu-lagumu dari Spotify adalah :", riwayatSpotify[4]["judul"])
print("Riwayat lagu-lagumu dari Spotify adalah :", riwayatSpotify[5]["judul"])
print("Riwayat lagu-lagumu dari Spotify adalah :", riwayatSpotify[6]["judul"])
print("Riwayat lagu-lagumu dari Spotify adalah :", riwayatSpotify[7]["judul"])
print("Riwayat lagu-lagumu dari Spotify adalah :", riwayatSpotify[8]["judul"])
print("Riwayat lagu-lagumu dari Spotify adalah :", riwayatSpotify[9]["judul"])
print("Riwayat lagu-lagumu dari Spotify adalah :", riwayatSpotify[10]["judul"])

print("====================================")
print("Lagu Pertama Adalah:")
print("Judul    :", riwayatSpotify[1]["judul"])
print("Artis    :", riwayatSpotify[1]["artis"])
print("Platform :", riwayatSpotify[1]["platform"])