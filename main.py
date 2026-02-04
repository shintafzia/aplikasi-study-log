catatan = []
# target harian (dalam menit). None berarti belum disetel
target_harian = None

def tambah_catatan():
    print("\n--- Tambah Catatan Belajar ---")
    mapel = input("Masukkan mata pelajaran: ").strip()
    if not mapel:
        print("Mapel tidak boleh kosong.")
        return

    topik = input("Masukkan topik: ").strip()
    if not topik:
        print("Topik tidak boleh kosong.")
        return

    while True:
        durasi_input = input("Masukkan durasi belajar (menit): ").strip()
        if not durasi_input:
            print("Durasi tidak boleh kosong. Silakan coba lagi.")
            continue
        if not durasi_input.isdigit():
            print("Durasi harus berupa angka (menit). Silakan masukkan angka bulat tanpa tanda.")
            continue
        durasi = int(durasi_input)
        if durasi <= 0:
            print("Durasi harus lebih dari 0. Silakan coba lagi.")
            continue
        break

    catatan.append({"mapel": mapel, "topik": topik, "durasi": durasi})
    print(f"Catatan untuk {mapel} - {topik} ({durasi} menit) berhasil disimpan.")

def lihat_catatan():
    print("\n--- Daftar Catatan Belajar ---")
    if not catatan:
        print("Belum ada catatan belajar. Silakan tambah catatan terlebih dahulu.")
        return

    # hitung lebar kolom secara dinamis agar tampilan rapi
    idx_w = len(str(len(catatan)))
    mapel_w = max(len("Mapel"), max(len(c["mapel"]) for c in catatan))
    topik_w = max(len("Topik"), max(len(c["topik"]) for c in catatan))
    durasi_w = max(len("Durasi"), max(len(str(c["durasi"])) for c in catatan))

    # header
    print(f"{'No.':>{idx_w}}  {'Mapel':<{mapel_w}}  {'Topik':<{topik_w}}  {'Durasi':>{durasi_w}}")
    print("-" * (idx_w + 2 + mapel_w + 2 + topik_w + 2 + durasi_w))

    # baris data
    for i, c in enumerate(catatan, 1):
        print(f"{i:>{idx_w}}.  {c['mapel']:<{mapel_w}}  {c['topik']:<{topik_w}}  {c['durasi']:>{durasi_w}} menit")

def total_waktu():
    total = sum(c["durasi"] for c in catatan)
    print("\n--- Total Waktu Belajar ---")
    print(f"Total waktu belajar: {total} menit")
    return total


def set_target_harian():
    global target_harian
    print("\n--- Atur Target Harian ---")
    while True:
        t_input = input("Masukkan target harian (menit): ").strip()
        if not t_input:
            print("Pengaturan target dibatalkan.")
            return
        if not t_input.isdigit():
            print("Target harus berupa angka (menit). Silakan coba lagi.")
            continue
        t = int(t_input)
        if t <= 0:
            print("Target harus lebih dari 0. Silakan coba lagi.")
            continue
        target_harian = t
        print(f"Target harian disetel: {target_harian} menit")
        return


def lihat_target_harian():
    print("\n--- Target Harian ---")
    if target_harian is None:
        print("Belum ada target harian. Gunakan menu untuk mengatur target.")
        return
    total = sum(c["durasi"] for c in catatan)
    if total >= target_harian:
        status = "TERCAPAI 🎉"
    else:
        sisa = target_harian - total
        status = f"Belum tercapai ({sisa} menit lagi)"
    print(f"Target harian: {target_harian} menit")
    print(f"Total saat ini: {total} menit -> {status}")


def menu():
    print("\n=== Study Log App ===")
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
    print("4. Target harian")
    print("5. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_catatan()
    elif pilihan == "2":
        lihat_catatan()
    elif pilihan == "3":
        total_waktu()
    elif pilihan == "4":
        # submenu kecil untuk fitur target
        print("\n--- Menu Target Harian ---")
        print("1. Atur target harian")
        print("2. Lihat target harian")
        sub = input("Pilih: ")
        if sub == "1":
            set_target_harian()
        elif sub == "2":
            lihat_target_harian()
        else:
            print("Pilihan tidak valid atau kembali ke menu utama")
    elif pilihan == "5":
        print("Terima kasih, terus semangat belajar!")
        break
    else:
        print("Pilihan tidak valid")