# This manifest handles the task of creating a custom HTTP header response

package{ 'nginx-core':
  ensure => installed,
}

file_line {'Http header':
    path  => '/etc/nginx/sites-available/default',
    after => ':80 default_server;',
    line  => "\tadd_header X-Served-By ${hostname};",
}

 service { 'nginx':
   enable => true,
   ensure => running,
   hasrestart => true,
 }
# listen [::]:80 default_server ipv6only=on;
