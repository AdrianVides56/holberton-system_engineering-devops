# User limit
# Login with the holberton user and open a file without any error message.

exec { 'Change hard nofile':
  command => '/bin/sed -i \'s/holberton hard nofile/holberton hard nofile 4096 #/\' /etc/security/limits.conf',
}

exec { 'Change soft nofile':
  command =>'/bin/sed -i \'s/holberton soft nofile/holberton soft nofile 4096 #/\' /etc/security/limits.conf',
}
