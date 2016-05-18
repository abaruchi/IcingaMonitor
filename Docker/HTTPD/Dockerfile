FROM fedora:20

# Install httpd
RUN yum install -y httpd

# Change the default docroot
RUN sed -i 's|^DocumentRoot.*|DocumentRoot "/srv"|' /etc/httpd/conf/httpd.conf

# Add in our custom httpd configuration.
ADD extra.conf /etc/httpd/conf.d/root.conf

EXPOSE 80

# Start up httpd.
ENTRYPOINT /usr/sbin/httpd -DFOREGROUND
