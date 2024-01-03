#!/usr/bin/env ruby
reg = /\[from:(\S+)\] \[to:(\S+)\] \[flags:([^\]]+)\]/
puts ARGV[0].scan(reg).join(",")
