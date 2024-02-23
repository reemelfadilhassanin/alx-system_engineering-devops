# Puppet manifest to kill a process named "killmenow" using pkill

exec { '/usr/bin/env pkill -9 killmenow':
}
