#Using Puppet
exec { 'apt-update':
  command => 'sudo apt-get -y update',
  provider => shell,
}

exec { 'InstallNginx':
  command => 'sudo apt -y install nginx',
  provider => shell,
}

exec { 'append':
 command => "sudo sed -i '/listen 80 default_server/a add_header X-Served-By ${hostname};' /etc/nginx/sites-enabled/default",
 provider => shell,
}

exec { 'NginxRestart':
  command  => 'sudo service nginx restart',
  provider => shell,
}
