#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import urllib.parse
import time
from datetime import datetime
import os

# Warna untuk output
RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'

# Fungsi untuk menampilkan banner
def print_banner():
    banner = f"""
{GREEN}

▄▄▄█████▓██▄▄▄█████▓▄▄▄      ███▄    █▓█████▄ ▒█████  ██▀███  ██ ▄█▀
▓  ██▒ ▓▓██▓  ██▒ ▓▒████▄    ██ ▀█   █▒██▀ ██▒██▒  ██▓██ ▒ ██▒██▄█▒ 
▒ ▓██░ ▒▒██▒ ▓██░ ▒▒██  ▀█▄ ▓██  ▀█ ██░██   █▒██░  ██▓██ ░▄█ ▓███▄░ 
░ ▓██▓ ░░██░ ▓██▓ ░░██▄▄▄▄██▓██▒  ▐▌██░▓█▄   ▒██   ██▒██▀▀█▄ ▓██ █▄ 
  ▒██▒ ░░██░ ▒██▒ ░ ▓█   ▓██▒██░   ▓██░▒████▓░ ████▓▒░██▓ ▒██▒██▒ █▄
  ▒ ░░  ░▓   ▒ ░░   ▒▒   ▓▒█░ ▒░   ▒ ▒ ▒▒▓  ▒░ ▒░▒░▒░░ ▒▓ ░▒▓▒ ▒▒ ▓▒
    ░    ▒ ░   ░     ▒   ▒▒ ░ ░░   ░ ▒░░ ▒  ▒  ░ ▒ ▒░  ░▒ ░ ▒░ ░▒ ▒░
  ░      ▒ ░ ░       ░   ▒     ░   ░ ░ ░ ░  ░░ ░ ░ ▒   ░░   ░░ ░░ ░ 
         ░               ░  ░        ░   ░       ░ ░    ░    ░  ░   
                                       ░                            

	     Powerful Dorking Tool Created by trystone ©
{RESET}
"""
    print(banner)

# Fungsi untuk mendapatkan nama file output yang tidak saling replace
def get_incremented_filename(base_name, extension):
    i = 1
    while True:
        file_name = f"{base_name}_{i}.{extension}"
        if not os.path.exists(file_name):
            return file_name
        i += 1

# Daftar dorking queries
dorks = [
    # 1. Pencarian File Konfigurasi
    'filetype:env "DB_PASSWORD"',
    'filetype:ini "password"',
    'filetype:sql "password"',
    'filetype:log "password"',
    'filetype:cfg "password"',
    'filetype:env "APP_ENV=local"',
    'filetype:xml "Web.config" password',
    'filetype:txt "password"',
    'filetype:conf inurl:settings',
    'filetype:ini "smtp" inurl:email',

    # 2. Pencarian Informasi Login
    'inurl:admin/login',
    'inurl:admin_area',
    'intitle:"admin login" "password"',
    'inurl:wp-admin intitle:login',

    # 3. Pencarian Informasi Sensitif di Direktori
    'intitle:index.of "parent directory" "password"',
    'intitle:index.of "backup"',
    'intitle:index.of "admin"',
    'intitle:index.of "config"',
    'intitle:"index of" "/private"',
    'intitle:"Index of /" inurl:ftp',
    'intitle:"index of /" "httpd.conf"',
    'intitle:"index of /" "web.config"',
    'intitle:"index of /" "config.json"',
    'inurl:"server-status"',

    # 4. Pencarian Log dan File Backup
    'inurl:/backup/',
    'inurl:/logs/',
    'inurl:logfile',
    'inurl:error.log',

    # 5. Pencarian File dengan Ekstensi Tertentu
    'filetype:bak inurl:"/"',
    'filetype:old inurl:"/"',
    'filetype:sql inurl:"/"',
    'filetype:json inurl:"/"',
    'filetype:log inurl:"/"',
    'filetype:backup inurl:*.backup',
    'inurl:backup intitle:index.of',

    # 6. Pencarian Kode Sumber yang Terekspose
    'filetype:php inurl:"/config"',
    'filetype:asp inurl:"/config"',
    'filetype:js inurl:"/config"',
    'filetype:xml inurl:"/config"',
    'filetype:yaml inurl:"/config"',

    # 7. Pencarian Bug dan Kerentanan Tertentu
    'inurl:"/phpinfo.php"',
    'inurl:"/test.php"',
    'inurl:"/debug"',
    'inurl:"/cgi-bin/"',

    # 8. Pencarian Informasi Sensitif dalam URL
    'inurl:"passwd"',
    'inurl:".git"',
    'inurl:"/proc/self/cwd"',
    'inurl:"/~"',

    # 9. Pencarian File Database
    'filetype:sql inurl:dump',
    'filetype:sql "backup"',
    'filetype:mdb inurl:*.mdb',
    'filetype:db inurl:*.db',
    'filetype:dbf inurl:*.dbf',

    # 10. Pencarian informasi email
    'intext:"email" filetype:xls',
    'filetype:xls inurl:"email"',
    'intext:"email" filetype:csv',
    'filetype:csv inurl:"email"',

    # 11. Pencarian File Konfigurasi Web Server
    'filetype:conf inurl:".htaccess"',
    'filetype:conf inurl:".htpasswd"',
    'filetype:conf inurl:".htgroups"',
    'filetype:conf inurl:"httpd.conf"',
    'filetype:conf inurl:"apache2"',

    # 12. Pencarian API dan Token Kunci
    'inurl:/api filetype:json',
    'filetype:json inurl:apikey',
    'filetype:json inurl:token',
    'inurl:/wp-json/wp/v2/users',

    # 13. Pencarian Direktori Upload yang Terbuka
    'inurl:/uploads/',
    'inurl:/files/',
    'inurl:/documents/',
    'intitle:"Index of /" inurl:/uploads',
    'intitle:"Index of /" inurl:/files',

    # 14. Pencarian Informasi Debug dan Kesalahan
    'inurl:error.log filetype:log',
    'inurl:debug.log filetype:log',
    'inurl:"/debug/" intitle:index.of',
    'intitle:"index of /" "debug.log"',

    # 15. Pencarian Data Pribadi atau Sensitif
    'filetype:pdf "confidential"',
    'filetype:doc "confidential"',
    'filetype:xls "salary"',
    'filetype:xlsx "employee"',

    # 16. Pencarian khusus
    'site:usgeo.gov "https://drive.google.com/folder/"',
    'site:.*.*.usgeo.gov "Server Status" | confidential | “employee only” | proprietary | top secret | classified | trade secret | internal | private',
    'site:*usgeo.gov intext:register',
    'ext:txt | ext:pdf | ext:xml | ext:xls | ext:xlsx | ext:ppt | ext:pptx | ext:doc | ext:docx intext:“confidential” | intext:“Not for Public Release” | intext:”internal use only” || intext:”passwords” | intext:“do not distribute”',
    'inurl:conf | inurl:env | inurl:cgi | inurl:bin | inurl:etc | inurl:root | inurl:sql | inurl:backup | inurl:admin | inurl:php site:example[.]com',
    'intitle:Welcome to Firebase Hosting inurl:firebaseapp *Nasa.gov',
    'ext:log | ext:txt | ext:conf | ext:cnf | ext:ini | ext:env | ext:sh | ext:bak | ext:backup | ext:swp | ext:old | ext:~ | ext:git | ext:svn | ext:htpasswd | ext:htaccess site:*nasa.gov',
    'inurl:q= | inurl:s= | inurl:search= | inurl:query= | inurl:keyword= | inurl:lang= inurl:& site:nasa.gov'
]

def google_dorking(target_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

# Mendapatkan nama file output baru dengan increment
    output_file = get_incremented_filename("dorking_results", "txt")

    # Membuka file untuk menuliskan hasil (mode append untuk menambahkan hasil)
    with open(output_file, "a") as f:
        # Tambahkan timestamp di awal setiap proses dorking
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"\n\n--- Dorking started at {timestamp} for {target_url} ---\n")

        for dork in dorks:
            query = f'site:{target_url} {dork}'
            encoded_query = urllib.parse.quote_plus(query)
            url = f"https://www.google.com/search?q={encoded_query}"

            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Mengambil hasil pencarian
            results = soup.find_all('div', {'class': 'tF2Cxc'})  # elemen yang sering digunakan untuk hasil pencarian

            if results:
                # Tampilkan hasil di terminal dengan warna hijau
                print(f"{GREEN}[+] Found results for: {query}{RESET}")

                # Tulis hasil ke file
                f.write(f"[+] Found results for: {query}\n")

                for result in results:
                    link_tag = result.find('a')
                    if link_tag and 'href' in link_tag.attrs:
                        link = link_tag['href']
                        print(link)  # Tampilkan di terminal
                        f.write(f"{link}\n")  # Simpan ke file
            else:
                # Tampilkan pesan "No results found" di terminal dengan warna merah
                print(f"{RED}[-] No results found for: {query}{RESET}")

                # Tulis pesan "No results found" ke file
                f.write(f"[-] No results found for: {query}\n")

            # Tambahkan jeda untuk menghindari deteksi bot oleh Google
            time.sleep(5)  # jeda 5 detik antara setiap pencarian

if __name__ == "__main__":
    print_banner()  # Menampilkan banner sebelum scanning dimulai
    target_url = input("Enter the target domain (e.g., example.com): ")
    google_dorking(target_url)

