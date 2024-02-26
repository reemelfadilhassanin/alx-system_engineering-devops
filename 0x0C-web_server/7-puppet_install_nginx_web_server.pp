# File: 7-puppet_install_nginx_web_server.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx server
file { '/var/www/html/index.html':
  ensure  => present,
  content => "Hello World!\n",
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  source  => 'puppet:///modules/nginx/default',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

file { '/etc/nginx/sites-enabled/default':
  ensure  => link,
  target  => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
}

# Redirect /redirect_me with a 301 status code
file { '/etc/nginx/sites-available/redirect_me':
  ensure  => present,
  content => "server {
    listen 80;
    server_name _;
    location /redirect_me {
      return 301 https://www.example.com;
    }
  }",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

file { '/etc/nginx/sites-enabled/redirect_me':
  ensure  => link,
  target  => '/etc/nginx/sites-available/redirect_me',
  require => File['/etc/nginx/sites-available/redirect_me'],
  notify  => Service['nginx'],
}
