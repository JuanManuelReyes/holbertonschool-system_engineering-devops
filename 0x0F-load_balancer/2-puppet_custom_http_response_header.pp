#Using Puppet, install flask from pip3
exec { 'apt-update':
  command => 'sudo apt update',
  path  => '/usr/bin/'
}

exec { 'InstallNginx':
  command => 'sudo apt -y install nginx',
  path  => '/usr/bin/'
}

exec { 'append':
 command => 'sudo sed -i "/listen 80 default_server/a add_header X-Served-By \$hostname;" /etc/nginx/sites-enabled/default',
 path => '/usr/bin/'
}

exec { 'NginxRestart':
  command  => 'sudo service nginx restart',
  path => '/usr/bin/'
}
