'''
Check if there is a palindrome - Ruby
'''

#Standard Ruby class and check for reverse string
class Word

    def palindrome?(string)
        if string == string.reverse
    end

end

#Alternative Ruby class to inheret from String class and check for reverse string

class Word2 < String

    def palindrome?
        self == self.reverse
    end

end

#test
w = Word.new #create new instance
w.palindrome?("anagram")
w.palindrome?("laal")