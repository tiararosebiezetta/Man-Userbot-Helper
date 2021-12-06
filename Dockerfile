FROM mrismanaziz/man-userbot:buster

RUN mkdir /home/manuserbot/ \
    && chmod 777 /home/manuserbot

WORKDIR /home/manuserbot/

CMD ["bash", "start.sh"]
