# This manifest handles the task of creating a custom HTTP header response
file_line {'Cutsom http response':
    path  => '/etc/nginx/sites-available/default'
    after => 'listen \[::\]:80 default_server'
    line  => 'add_header X-Served-By $hostname;'
}
