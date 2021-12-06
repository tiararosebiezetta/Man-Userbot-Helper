FROM mrismanaziz/man-userbot:buster

RUN mkdir /home/manuserbot/ \
    && chmod 777 /home/manuserbot \
    && mkdir /home/manuserbot/bin/

WORKDIR /home/manuserbot/

CMD ["bash", "start.sh"]
