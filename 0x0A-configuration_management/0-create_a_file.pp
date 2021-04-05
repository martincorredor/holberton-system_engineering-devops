# create a file in /tmp
file {'/tmp/holberton': # name of the file
    ensure  => 'file', # ensure the creation of the file
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet',
    mode    => '0744',
}
