# Comment

# Comment
exec { 'fix_error':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 2000\"/" /etc/default/nginx',
}

# Comment
exec { 'restart':
  command  => 'sudo service nginx restart',
  provider => shell
}
