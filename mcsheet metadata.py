import gspread
import os
import fnmatch
import audio_metadata
import re

pattern = 'Pixel Terror & DYSON - Dilemma*'
track_title = "Mirrors";
# variables
track_album = "";
track_genre = "";
track_bpm = "";
track_B = "";
track_metadata="";

# google sheet initialization
gc = gspread.service_account();
sheet_catalog = gc.open_by_url('https://docs.google.com/spreadsheets/d/116LycNEkWChmHmDK2HM2WV85fO3p3YTYDATpAthL8_g/edit');
sheet_subgenre = gc.open_by_url('https://docs.google.com/spreadsheets/d/13reh863zpVJEnFR8vFJ7dRhaln86ETk9etbE7tFHS2g/edit')

catalog = sheet_catalog.worksheet("Catalog").get_all_records();

# get files
for path,dirs,files in os.walk('/Users/622/Downloads'):
    for filename in fnmatch.filter(files,pattern):
            # find track name and store metadata
            track_metadata=audio_metadata.load(path+"/"+filename)
            track = re.split(' - ', filename)
            track_album = track[-2]
            track_title = re.match(r'(.+)\.[A-Za-z]+',track[-1]).group(1)
            
            # unused attempt at using only re.match
            # track = re.match(r'.*[\-](.+) - (.+)\.[A-Za-z]+',filename)
            # track_title = track.group(2);

            # pull metadata from MCatalog
            for entry in catalog:
                if entry["Track"] == track_title:
                    track_genre = entry["Genre"]
                    track_bpm = entry["BPM"]
                    track_B = entry["B"]
                    if track_B=="U":
                        track_B="Uncaged"
                    elif track_B=="I":
                        track_B="Instinct"
                    elif track_B=="M":
                        track_B="Mix"
                    elif track_B=="P":
                        track_B="Podcast"
                    else:
                        track_B=""
              
# playing with metadata to make sure it works; havent gottten further yet
# track_metadata.tags.album.insert(1,"he")
# print(track_metadata.tags)
# del track_metadata.tags.album[1]
# print(track_metadata.tags)
          
# print(track_title,track_genre,track_B,track_bpm)
