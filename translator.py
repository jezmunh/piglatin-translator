def TranslateText(inputtext):
    pl_text = inputtext.split()
    result = ''
    clean_word = ''
    for i in pl_text:
        if len(i) == 1:
            result += i
        else:            
            if i[-2:] == 'ay':
                clean_word = i.replace(i[-2:], '')
        translated_word = clean_word[-1] + clean_word[:-1]
        result += ' ' + translated_word
    return result
    #print(f"Translated text: {result}")
