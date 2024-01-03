#!/usr/bin/env ruby
reg = /hbt+n/
puts ARGV[0].scan(reg).join
