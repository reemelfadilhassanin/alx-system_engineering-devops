#!/usr/bin/env ruby
reg = /hb?tn/
puts ARGV[0].scan(reg).join
