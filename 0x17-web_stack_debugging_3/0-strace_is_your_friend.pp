# This manifest will fix a specific error in a given container
exec { 'modify_file':
    command => "sed -i '/.phpp/ s/phpp/php/' '/var/www/html/wp-settings.php'",
    path    => '/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
