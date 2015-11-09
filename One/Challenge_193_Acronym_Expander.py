"""[2014-12-19] Challenge #193 [Easy] Acronym Expander
 The task is to converting an abbreviated sentence into its full version.
 On console input you will be given a string that represents the abbreviated chat message.
 Output should consist of the expanded sentence

 >>>'wtf that was unfair'
 >>>'what the fuck that was unfair'
 >>>imo that was wp. Anyway I've g2g!
 >>>in my opinion that was well played. Anyway I've got to go!
 """
words = ('wtf that was unfair!').split(' ')

acronyms = {
'lol': 'laugh out loud',
"hf": "have fun",
"gg": "good game",
"brb":'be right back',
"g2g": "got to go",
"wtf": "what the fuck",
'dw': "don't worry fuck",
"wp": "well played",
"gl": "good luck",
"imo": "in my opinion"
}

answer = ''

for word in words:
    if word.endswith(('.', ',', ':', ';', '!')):
        word, char = word[:-1], word[-1]
        if word in acronyms.keys():
            answer +=  acronyms[word]  + char
        else:
            answer += word + char
    else:
        if word in acronyms.keys():
            answer += acronyms[word]
        else:
            answer += word
    answer += ' '
print answer