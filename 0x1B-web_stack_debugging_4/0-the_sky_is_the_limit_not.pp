#  This Puppet manifest configures Nginx

exec { 'fix--for-nginx':
  command => '/usr/sbin/nginx -s reload',
  path    => ['/usr/sbin', '/usr/bin', '/sbin', '/bin'],
  notify  => Service['nginx'],
}

file { '/etc/nginx/nginx.conf':
  ensure  => file,
  source  => 'puppet:///modules/nginx/nginx.conf',
  notify  => Exec['fix--for-nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
}