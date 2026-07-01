🔍 UTS — Uncomplicated Traffic Scanner

UTS adalah tool monitoring jaringan ringan berbasis Python yang berjalan di atas interactive shell. Dibuat untuk meng-inspect dan menganalisis paket jaringan secara sederhana menggunakan library Scapy.


⚠️ Disclaimer: Tool ini dibuat untuk keperluan edukasi dan monitoring jaringan pribadi. Jangan gunakan untuk memonitor traffic jaringan tanpa izin.




✨ Fitur

OpsiFungsi-dDebug mode — sniff semua traffic IP secara real-time-TSniff traffic HTTP/HTTPS pada port default (80 & 443)-t [PORT]Sniff traffic TCP pada port tertentu-oARP scan untuk mendeteksi host aktif di jaringan lokal-h / helpTampilkan menu bantuanmanTampilkan halaman manual lengkapclearBersihkan layar terminalexitKeluar dari UTS shell


⚙️ Requirements

Python: 3.8+

Install dependensi dengan:

bashpip install scapy pyfiglet

LibraryKegunaanscapyPacket sniffing & ARP scanningpyfigletASCII art banner saat startup


Linux/macOS: Scapy membutuhkan akses root untuk sniffing. Jalankan dengan sudo.
Windows: Jalankan terminal sebagai Administrator. Pastikan Npcap sudah terinstall.




🚀 Cara Menjalankan

bash# Linux / macOS
sudo python3 UTS.py

# Windows (jalankan terminal sebagai Administrator)
python UTS.py

Setelah masuk ke shell interaktif:

 _   _ _____ ____
| | | |_   _/ ___|
| | | | | | \___ \
| |_| | | |  ___) |
 \___/  |_| |____/

uncomplicated traffic scanner - by Ajam WHO HATES UTS DADAKAN HARI SENIN

Type 'help' or 'man' for commands.

UTS >

Contoh Penggunaan

bash# Sniff semua traffic (debug mode)
UTS > -d

# Sniff traffic HTTP & HTTPS
UTS > -T

# Sniff traffic pada port 8080
UTS > -t 8080

# Scan host aktif di jaringan lokal
UTS > -o

# Tampilkan manual
UTS > man

Tekan Ctrl+C untuk menghentikan proses sniffing yang sedang berjalan dan kembali ke shell.


📁 Struktur File

.
├── UTS.py       # Script utama
└── README.md


📌 Catatan


Tool ini berjalan secara blocking saat sniffing — tekan Ctrl+C untuk berhenti dan kembali ke prompt.
Fitur -o (ARP scan) saat ini melakukan broadcast ke subnet 192.168.1.0/24. Sesuaikan subnet di source code jika jaringan lokal kamu berbeda.
Proyek ini masih dalam tahap pengembangan awal dan dibuat sebagai sarana belajar jaringan & Python.
