# https://support.axway.com/kb/101749/language/en#:~:text=The%20%22Too%20many%20open%20files%22%20message%20means%20that%20the%20operating,command%20displays%20the%20current%20limit.
# http://woshub.com/too-many-open-files-error-linux/

exec { 'hard_limit':
  command => "/usr/bin/env sudo sed -i 's/5/92233720/g' /etc/security/limits.conf",
}

exec { 'soft_limit':
  command => "/usr/bin/env sudo sed -i 's/4/92233720/g' /etc/security/limits.conf",
}
