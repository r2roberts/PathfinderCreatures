FROM nginx
COPY favicon.ico /usr/share/nginx/html/
COPY AoN-PNGs /usr/share/nginx/html/AoN-PNGs
COPY CSS /usr/share/nginx/html/CSS
COPY js /usr/share/nginx/html/js
COPY *.html /usr/share/nginx/html/
