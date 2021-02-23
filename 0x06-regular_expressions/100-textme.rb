#!/usr/bin/env ruby
cool = ARGV[0].scan(/from:([+A-Za-z0-9]+)/).join
cool1 = ARGV[0].scan(/to:([+A-Za-z0-9]+)/).join
cool2 = ARGV[0].scan(/flags:([-{0,1}\d:{0,1}]+)/).join
puts cool + "," + cool1 + "," + cool2
