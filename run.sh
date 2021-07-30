pip3 install --upgrade youtube-dl
python3 main.py

for f in musics/*; do
	mega-put "$f" /PC-desktop/musiques/Youtube/ && rm -f "$f"
done
