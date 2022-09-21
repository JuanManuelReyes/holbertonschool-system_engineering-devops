exec { 'fix_error':
  command  => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
}