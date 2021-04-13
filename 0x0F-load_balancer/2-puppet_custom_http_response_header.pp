# This manifest handles the task of creating a custom HTTP header response
$commands = 'apt-get -y update; apt-get -y install nginx; ufw allow \'Nginx HTTP\''
exec {'Install nginx':
    path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
    command => $commands
}
file_line {'Http header':
    path  => '/etc/nginx/sites-available/default',
    after => ':80 default_server;',
    line  => "\tadd_header X-Served-By ${hostname};",
}
exec {'Restart nginx':
    path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
    command => 'sudo service nginx restart'
}
