#Using Puppet, create a file in /tmp
file { 'FileCreation':
  ensure  => 'present', #accepts any form of file existence, and creates a normal file if the file is missing.
  path    => '/tmp/school'
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
