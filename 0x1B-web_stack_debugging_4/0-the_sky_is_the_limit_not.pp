exec { 'fix_error':
  command  => "/usr/bin/env sudo sed -i 's/ULIMIT=\'-n 15\'/ULIMIT=\'-n 2000\'/' /etc/default/nginx",
  provider => 'shell'
}
exec { 'restart':
  command  => 'sudo service nginx restart',
  provider => 'shell'
}
