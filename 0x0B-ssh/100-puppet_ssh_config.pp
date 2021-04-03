# This manifest will edit the ~/etc/ssh/ssh_config file with given settings
file { '/etc/ssh/ssh_config':
  content => "Host *
    PasswordAuthentication no
    IdentityFile ~/.ssh/holberton
    SendEnv LANG LC_*
    HashKnownHosts yes
    GSSAPIAuthentication yes
    GSSAPIDelegateCredentials no"
}
