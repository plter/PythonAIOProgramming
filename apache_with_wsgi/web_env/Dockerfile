FROM httpd:2.4

RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak
COPY sources.list /etc/apt/
RUN apt update
RUN apt install -y python3 python3-dev gcc g++ make
COPY mod_wsgi-4.7.1.tar.gz /opt
WORKDIR /opt
RUN tar -xzvf ./mod_wsgi-4.7.1.tar.gz
WORKDIR /opt/mod_wsgi-4.7.1
RUN ./configure --with-apxs=/usr/local/apache2/bin/apxs --with-python=/usr/bin/python3
RUN make&&make install

RUN echo 'LoadModule wsgi_module modules/mod_wsgi.so' >> /usr/local/apache2/conf/httpd.conf
RUN echo 'WSGIScriptAlias /app /opt/server/wsgi_app.py' >> /usr/local/apache2/conf/httpd.conf
RUN echo '<Directory /opt/server/>' >> /usr/local/apache2/conf/httpd.conf
RUN echo '  Require all granted' >> /usr/local/apache2/conf/httpd.conf
RUN echo '</Directory>' >> /usr/local/apache2/conf/httpd.conf
