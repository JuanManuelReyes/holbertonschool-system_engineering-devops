#Using Puppet
exec { 'apt-get update':
  command  => 'sudo apt-get update',
}

package { 'install-nginx':
  ensure  => installed,
  require => Exec['apt-get update'],
}

file_line { 'append':
  ensure  => present,
  path    => '/etc/nginx/sites-enabled/default',
  after   => ':80 default_server;',
  line    => "add_header X-Served-By ${hostname};",
  require => Package['install-nginx'],
}

service { 'run-nginx':
  ensure  => running,
  require => File_line['append'],
}
