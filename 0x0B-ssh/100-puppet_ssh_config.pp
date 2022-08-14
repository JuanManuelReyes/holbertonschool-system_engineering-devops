#Connect with puppet without password
https://doc.wikimedia.org/puppet/puppet_types/file_line.html
file_line { 'Title':
 ensure => 'present',
 path => '/etc/ssh/ssh_config', #File to append the line
 line => 'IdentityFile ~/.ssh/school' #Line to append
}

file_line { 'No_Passwd':
  path => '/etc/ssh/ssh_config', #File to append the line
  line => 'PasswordAuthentication no' #Line to append
}
