#Using Puppet, install flask from pip3
exec { 'apt-update':
  command  => '/usr/bin/apt-get update'
}
package { 'nginx':
  ensure => 'installed'
  name     => 'nginx',
}
file_line { 'append':
 path => '/etc/nginx/nginx.conf', #File to append the line
 line => '      add_header X-Served-By ${HOSTNAME};' #Line to append
 after => 'server {',
}
exec { 'sudo service nginx restart':
  command  => '/usr/sbin/service nginx restart',
}
