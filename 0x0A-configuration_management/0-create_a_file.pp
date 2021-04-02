# This manifests creates a file called holberton in the /tmp directory with following attributes
#   mode => '0744' | owner => 'www-data' | group => 'www-data' | content => 'I love Puppet'
file { '/tmp/holberton':
  ensure  => 'present',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
