#Using Puppet, install flask from pip3
package { 'InstallFlask':
  name: 'flask',
  provider: 'pip3',
  ensure: '2.1.0',
}
