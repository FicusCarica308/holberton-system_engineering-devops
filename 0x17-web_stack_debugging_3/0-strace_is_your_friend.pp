# This manifest will fix a specific error in a given container
file_line {'fix-error':
    path  => '/var/www/html/wp-settings.php',
    match => '^require_once\( ABSPATH . WPINC . \'/class-wp-locale.phpp\' \);',
    line  => 'require_once( ABSPATH . WPINC . \'/class-wp-locale.php\' );',
}
