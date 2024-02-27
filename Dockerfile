FROM ubuntu:latest
ARG DEBIAN_FRONTEND=noninteractive
WORKDIR /var/photogram
RUN apt update
RUN apt upgrade -y
RUN apt install -y apache2
RUN apt install -y php libapache2-mod-php php-mysql
RUN apt install -y nano git
# CMD /var/photogram/main.sh