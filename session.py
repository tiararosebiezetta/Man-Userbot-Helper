#!/usr/bin/env bash
# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

import os
from time import sleep

a = r"""StringSession Telegram Generator by @mrismanaziz"""

def spinner(x):
    if x == "tele":
        print("Memeriksa Telethon diinstal...")
    else:
        print("Memeriksa Pyrogram diinstal...")
    for _ in range(3):
        for frame in r"-\|/-\|/":
            print("\b", frame, sep="", end="", flush=True)
            sleep(0.1)


def clear_screen():
    if os.name == "posix":
        os.system("clear")
    else:
        # for windows platfrom
        os.system("cls")


def get_api_id_and_hash():
    print(
        "Dapatkan APP ID dan API HASH Anda dari my.telegram.org atau @scrapmanbot \n\n",
    )
    try:
        API_ID = int(input("Silakan Masukkan APP ID anda : "))
    except ValueError:
        print("APP ID Yang anda Masukan Salah.")
        exit(0)
    API_HASH = input("Silakan Masukkan API HASH anda : ")
    return API_ID, API_HASH


def telethon_session():
    try:
        spinner("tele")

        x = "\bMenemukan instalasi dari Telethon...\nBerhasil Mengimpor.\n\n"
    except BaseException:
        print("Menginstall Telethon...")
        os.system("pip install telethon")

        x = "\bSelesai. Telethon Berhasil dipasang."
    clear_screen()
    print(a)
    print(x)

    # the imports
    from telethon.errors.rpcerrorlist import ApiIdInvalidError, PhoneNumberInvalidError
    from telethon.sessions import StringSession
    from telethon.sync import TelegramClient

    API_ID, API_HASH = get_api_id_and_hash()

    # logging in
    try:
        with TelegramClient(StringSession(), API_ID, API_HASH) as manuserbot:
            print("Berhasil Membuat String Session untuk Man-Userbot...")
            ult = manuserbot.send_message(
                "me",
                f"⛑ **Man-Userbot SESSION** ⛑\n\n`{manuserbot.session.save()}`\n\n**Support: @Lunatic0de & @SharingUserbot**",
            )
            print(
                "Periksa Pesan Tersimpan Telegram Anda untuk menyalin nilai STRING_SESSION"
            )
            exit(0)
    except ApiIdInvalidError:
        print(
            "APP ID/API HASH Yang Anda Masukan Tidak Valid. Mohon Periksa Kembali."
        )
        exit(0)
    except ValueError:
        print("API HASH Wajib diisi!")
        exit(0)
    except PhoneNumberInvalidError:
        print("Nomor Telepon Yang Anda Masukan Tidak Valid!")
        exit(0)


def pyro_session():
    try:
        spinner("pyro")
        from pyrogram import Client

        x = "\bMenemukan instalasi dari Pyrogram...\nBerhasil Mengimpor.\n\n"
    except BaseException:
        print("Menginstall Pyrogram...")
        os.system("pip install pyrogram tgcrypto")
        x = "\bSelesai. Pyrogram Berhasil diinstall."
    clear_screen()
    print(a)
    print(x)

    # generate a session
    API_ID, API_HASH = get_api_id_and_hash()
    print("Masukkan Nomor Telepon saat ditanya.\n\n")
    with Client(":memory:", api_id=API_ID, api_hash=API_HASH) as pyro:
        ss = pyro.export_session_string()
        pyro.send_message(
            "me",
            f"⛑ **Pyrogram Session** ⛑\n\n`{ss}`\n\n**Support: @Lunatic0de & @SharingUserbot**",
        )
        print("Periksa Pesan Tersimpan Telegram Anda untuk menyalin nilai STRING_SESSION")
        exit(0)


def main():
    clear_screen()
    print(a)
    try:
        type_of_ss = int(
            input(
                "String Session Mana Yang ingin Anda Buat?\n1. Telethon (Man-Userbot)\n2. Pyrogram (BOT Music)\n\nMasukkan Pilihan 1 atau 2 :  "
            )
        )
    except Exception as e:
        print(e)
        exit(0)
    if type_of_ss == 1:
        telethon_session()
    elif type_of_ss == 2:
        pyro_session()
    else:
        print("Ga Bisa Bahasa Enggres.")
        x = input("Ingin Mengambil STRING lagi? (y/n")
        if x == "y":
            main()
        else:
            exit(0)
main()
