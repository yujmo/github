FROM nginx:latest
RUN echo "this is nginx" > /usr/share/nginx/html/index.html
