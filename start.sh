rm -rf .git
git clone -b Man-Userbot https://github.com/mrismanaziz/Man-Userbot tmp
mv tmp/.git .
rm -rf tmp
git reset --hard
mkdir bin
python3 -m userbot
