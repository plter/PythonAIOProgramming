# 第5章/apache_with_wsgi/web_env/Dockerfile
FROM httpd:2.4.41

RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak
# 替换软件源为清华镜像站
COPY sources.list /etc/apt/
# 更新软件源
RUN apt-get update
# 安装Python运行环境及C语言编译器用以编译wsgi
RUN apt-get install -y python3 python3-dev gcc g++ make
# 将wsgi源码拷贝到镜像中
COPY mod_wsgi-4.7.1.tar.gz /opt
# 切换镜像中的工作目录
WORKDIR /opt
# 解压wsgi源码包
RUN tar -xzvf ./mod_wsgi-4.7.1.tar.gz
# 切换工作目录到wsgi源码目录
WORKDIR /opt/mod_wsgi-4.7.1
# 配置编译环境
RUN ./configure --with-apxs=/usr/local/apache2/bin/apxs \
    --with-python=/usr/bin/python3
# 编译并安装
RUN make&&make install

# 这是对Apache服务器的配置文件进行修改，添加wsgi相关的配置项，
# 包括加载 wsgi 动态库、配置脚本文件、配置脚本文件所在目录的权限
RUN echo 'LoadModule wsgi_module modules/mod_wsgi.so' >>\
    /usr/local/apache2/conf/httpd.conf
RUN echo 'WSGIScriptAlias /app /opt/server/wsgi_app.py' >>\
    /usr/local/apache2/conf/httpd.conf
RUN echo '<Directory /opt/server/>' >>\
    /usr/local/apache2/conf/httpd.conf
RUN echo '  Require all granted' >> \
    /usr/local/apache2/conf/httpd.conf
RUN echo '</Directory>' >> /usr/local/apache2/conf/httpd.conf
