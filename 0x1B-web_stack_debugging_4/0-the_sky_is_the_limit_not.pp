exec { 'fix_error':
  command  => "sed -i 's/15/20000/g' /etc/default/nginx",
  path => "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
}
exec { 'restart':
  command  => 'sudo service nginx restart',
  path => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}
