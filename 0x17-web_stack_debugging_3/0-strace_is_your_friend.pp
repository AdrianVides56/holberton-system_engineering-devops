# find out why Apache is returning a 500 error
# a misspelling error
exec { 'Solution':
  command => '/bin/sed -i \'s/.phpp/.php/\' /var/www/html/wp-settings.php',
}
