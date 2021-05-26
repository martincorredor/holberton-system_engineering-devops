# Change the OS configuration so that it is possible to login with the holberton user

exec { 'Change config':
  command => 'sudo sed -i "s/5/1000/g; s/4/1000/g" /etc/security/limits.conf',
  path    => '/usr/bin/:/bin/',
}
