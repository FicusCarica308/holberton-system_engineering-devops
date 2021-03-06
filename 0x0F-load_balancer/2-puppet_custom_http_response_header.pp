# This manifest handles the task of creating a custom HTTP header response
# does not setup server like task 0 just the custom header !!!!
exec {'Install nginx':
    path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
    command => 'sudo apt-get -y update; sudo apt-get -y install nginx'
}
file_line {'Http header':
    path    => '/etc/nginx/sites-available/default',
    after   => ':80 default_server;',
    line    => "\tadd_header X-Served-By ${hostname};",
    require => Exec['Install nginx'],
}
exec {'Restart nginx':
    path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
    command => 'sudo service nginx restart',
    require => File_line['Http header'],
}
