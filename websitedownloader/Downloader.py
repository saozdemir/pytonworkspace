"""
 @author saozd
 @project pytonworkspace Downloader
 @date 14 Ağu 2024
 <p>
 @description:
"""
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# İndirme işlemlerini kaydetmek için bir dizin oluştur
base_url = "https://repo1.maven.org/maven2/org/apache/maven/plugins/maven-compiler-plugin/"
download_directory = "maven2/org/apache/maven/plugins/maven-compiler-plugin/"

if not os.path.exists(download_directory):
    os.makedirs(download_directory)

def download_file(url, download_directory):
    local_filename = os.path.join(download_directory, os.path.basename(url))
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print(f"Downloaded: {local_filename}")

def scrape_directory(url, download_directory):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    for link in soup.find_all("a"):
        href = link.get("href")

        if href.endswith("/") and href != "../":
            # Alt dizine gidip onu kazı
            new_directory = os.path.join(download_directory, href[:-1])
            if not os.path.exists(new_directory):
                os.makedirs(new_directory)
            scrape_directory(urljoin(url, href), new_directory)
        elif not href.endswith("/"):
            # Dosya bulduğunda indir
            file_url = urljoin(url, href)
            download_file(file_url, download_directory)

scrape_directory(base_url, download_directory)