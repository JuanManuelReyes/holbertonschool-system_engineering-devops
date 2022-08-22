#Using Puppet
exec { 'apt-get update':
  command  => 'sudo apt-get -y update',
  provider => shell,
  before   => Exec['InstallNginx'],
}

exec {'InstallNginx':
  command  => 'sudo apt-get -y install nginx',
  provider => shell,
  before   => Exec['append'],
}

exec { 'append':
  provider => shell,
  command  => "sudo sed -i '/listen 80 default_server/a add_header X-Served-By ${hostname};' /etc/nginx/sites-enabled/default",
  before   => Exec['restart'],
}

exec { 'restart':
  command  => 'sudo service nginx restart',
  provider => 'shell'
  }
