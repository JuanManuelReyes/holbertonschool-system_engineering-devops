#Using Puppet, install flask from pip3
package { 'InstallFlask':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => 'pip3'
}
