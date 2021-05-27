# Handling a big amounts of requests
# Puppet commands to fix the issue and restart the service

exec { 'problem solution':
     command => '/bin/sed -i \'s/ULIMIT=/# ULIMIT=/\' /etc/default/nginx',
}

exec { 'restart nginx':
       command => 'service nginx restart',
       path    => [ '/usr/bin', 'usr/sbin' ],
}
