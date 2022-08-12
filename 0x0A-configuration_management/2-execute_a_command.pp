#Using Puppet, create a manifest that kills a process named killmenow
exec { 'KillMenow':
  command  => 'pkill killmenow',
  provider => 'shell'
}
