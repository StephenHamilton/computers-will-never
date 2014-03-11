#!/usr/bin/python

from random import randint
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

def computers_will_never():
    
    with open('nouns.txt','rU') as nouns:
        # TODO: don't read this into memory either

        for noun in nouns:
            s = noun.rstrip()
            # Slightly naive vowel handling
            if s.startswith(("a","e","i","o","u")):
                print "an " + s
            elif pos_tag(word_tokenize(s))[0][1] == 'NNS':
                # TODO: skip startswith() entirely if plural
                print s
            else:
                print "a " + s


if __name__=='__main__':
    computers_will_never()
        
