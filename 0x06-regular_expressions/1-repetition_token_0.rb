#!/usr/bin/env ruby
reg = /hbt{2,5}n/
puts ARGV[0].scan(reg).join
