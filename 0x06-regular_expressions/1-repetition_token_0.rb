#!/usr/bin/env ruby
# Ruby script that accepts one argument and pass it to a regular expression

puts ARGV[0].scan(/hbt{2,5}n/).join
