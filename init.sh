# Run Bush

# Nginx - configuration
# if [ -f /etc/nginx/sites-enabled/default ]; then
#  sudo rm -rf /etc/nginx/sites-enabled/default
# fi
# touch /home/box/nginx.log
# sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

# WSGI
sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/gunicorn.conf
# sudo /etc/init.d/gunicorn restart
sudo service gunicorn restart