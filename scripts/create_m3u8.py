# scripts/create_m3u8.py
import os

# Read the playlist file and create the .m3u8 file
with open("scripts/playlist.txt", "r") as infile, open("scripts/playlist.m3u8", "w") as outfile:
    outfile.write("#EXTM3U\n")
    for line in infile:
        url = line.strip()
        outfile.write(f"#EXTINF:-1, {url}\n")
        outfile.write(f"{url}\n")
