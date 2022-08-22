#Using Puppet, install flask from pip3
exec { 'update':
  command  => '/usr/bin/apt-get update',
  provider => 'shell'
}
package { 'InstallNginx':
  name     => 'nginx',
  provider => 'apt'
}
file_line { 'append':
 ensure => 'present',
 path => '/etc/nginx/nginx.conf', #File to append the line
 line => '      add_header X-Served-By ${HOSTNAME};' #Line to append
 after => 'server {'
}
exec { 'restart':
  command  => '/usr/sbin/service nginx restart',
  provider => 'shell'
}
