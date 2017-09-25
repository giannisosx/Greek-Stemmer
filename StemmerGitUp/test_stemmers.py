# -*- coding: utf-8 -*-
#!/usr/bin/python

#Word must be in capital greek letters
word = 'ΕΜΦΑΝΙΖΩ'


import osx7stemmer

#Input list defines which extra rules will be used
print osx7stemmer.stem(word,['saroukos','mystem','skroutz'])

