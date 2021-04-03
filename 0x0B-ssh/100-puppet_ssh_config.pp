# This manifest will edit the ~/etc/ssh/ssh_config file and add these lines if not already there
include stdlib
file_line{'Turn off passwd auth':
    path    => '/etc/ssh/ssh_config',
    match   => '^PasswordAuthentication yes',
    line    => 'PasswordAuthentication no',
}
file_line{'Declare identity file':
    path    => '/etc/ssh/ssh_config',
    match   => '^IdentityFile'
    line    => 'IdentityFile ~/.ssh/holberton',
}
