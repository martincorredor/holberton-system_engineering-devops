# Fix a 500 error in Wordpress settings file

exec { 'fix config':
  command => "sed -i 's/.phpp/.php/' /var/www/html/wp-settings.php",
  path    => ['/usr/bin', '/bin'],
}
