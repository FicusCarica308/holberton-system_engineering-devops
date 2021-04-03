# This manifest will edit the ~/etc/ssh/ssh_config file and add these lines if not already there
file { '/etc/ssh/ssh_config':
  ensure => present,
}
file_line { 'Turn off passwd auth':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}
file_line { 'Declare identity file':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/holberton',
}
