#!/usr/bin/env ruby
# Script output: [SENDER],[RECEIVER],[FLAGS]

puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
