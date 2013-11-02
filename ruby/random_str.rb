'''
Random string of letters generated
'''

('a'..'z').to_a.shuffle[0..7].join


	inputs.each do |input|
		puts "(#{input}: %s) == " % reverse_str(input) == ''
		puts "(#{input}: %s) == " % reverse_str2(input)	== 	
	end