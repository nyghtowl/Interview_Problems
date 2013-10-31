def count_bobs(s):
    num = 0
    word_match = 'bob'
    for i, letter in enumerate(s):
        if letter == 'b':
            j = 0
            match = True
            while match:
                if j == 3:
                    num += 1
                    match = False
                elif word_match[j] == s[i]:
                    i += 1
                    j += 1
                    if i < len(s):
                        continue
                    else:
                        i -= 1
                else:
                    match = False
    print("Number of times bob occurs is: %d" % num)

count_bobs('nbobblwbobbobobfssbob')
