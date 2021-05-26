# Fixing: receiving a large number of failed requests.

exec {'max limit of open files':
  command => 'sudo sed -i "s/15/10000/" /etc/default/nginx && sudo service nginx restart',
  path    => '/bin:/usr/bin:/usr/sbin:/sbin',
}
