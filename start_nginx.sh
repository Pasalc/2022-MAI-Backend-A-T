#!bash

echo "Using $PWD/nginx.conf file" 
sudo nginx -p $PWD/nginx -c nginx.conf
