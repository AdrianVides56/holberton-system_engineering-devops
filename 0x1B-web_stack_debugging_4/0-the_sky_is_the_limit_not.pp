# Handling a big amounts of requests

exec { 'problem solution':
     command => '/bin/sed -i \'s/ULIMIT="-n 15"/ULIMIT="-n 4096"/\' /etc/default/nginx',
}

exec { 'restart nginx':
       command => '/usr/sbin/service nginx restart',
}
