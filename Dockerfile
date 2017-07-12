FROM ubuntu:latest
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install wget openjdk-8-jdk -y
RUN wget http://mirrors.jenkins.io/war-stable/latest/jenkins.war -P /root
CMD java -jar /root/jenkins.war 
