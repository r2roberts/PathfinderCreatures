FROM nginx
COPY *.html /usr/share/nginx/html/
COPY CSS /usr/share/nginx/html/CSS
COPY js /usr/share/nginx/html/js
COPY AoN-PNGs /usr/share/nginx/html/AoN-PNGs
