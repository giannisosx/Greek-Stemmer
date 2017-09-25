#!/usr/bin/env python
# -*- coding: utf-8 -*-

import stop_list

"""
ntais
    source code: https://bitbucket.org/akalapodis/grstemmer
    paper: https://people.dsv.su.se/~hercules/papers/Ntais_greek_stemmer_thesis_final.pdf

skroutzstem
    Skroutz Team
    https://github.com/skroutz/greek_stemmer

saroukosstem
     Enhancing a Greek Language Stemmer-Efficiency and Accuracy Improvements by Spyridon Saroukos
     http://uta32-kk.lib.helsinki.fi/bitstream/handle/10024/80480/gradu03463.pdf?sequence=1

mystem
    my additions
"""


VOWELS = ['Α', 'Ε', 'Η', 'Ι', 'Ο', 'Υ', 'Ω', '’', 'Έ', 'Ή', 'Ί', 'Ό', 'Ύ', 'Ώ', 'Ϊ', 'Ϋ']

def ends_with(word, suffix):
    return word[len(word) - len(suffix):] == suffix

def stem(word,input_list):
    done = len(word) <= 3
    




        #---------saroukos rules----------------
    if 'saroukos' in input_list:
        exception = stop_list.exceptions(word)  # saroukosstem
        if exception:
            word = exception
            done = True


        # S1 RULE page 31   saroukosstem
        if not done:
            for suffix in ['ΙΖΑ','ΙΖΕΣ','ΙΖΕ','ΙΖΑΜΕ','ΙΖΑΤΕ','ΙΖΑΝ','ΙΖΑΝΕ','ΙΖΩ','ΙΖΕΙΣ','ΙΖΕΙ','ΙΖΟΥΜΕ','ΙΖΕΤΕ','ΙΖΟΥΝ','ΙΖΟΥΝΕ']:
                if ends_with(word, suffix):
                    word = word[:len(word) - len(suffix)]
                    root_list1 = ['ΑΝΑΜΠΑ','ΕΜΠΑ','ΕΠΑ','ΞΑΝΑΠΑ','ΠΑ','ΠΕΡΙΠΑ','ΑΘΡΟ','ΣΥΝΑΘΡΟ','ΔΑΝΕ']
                    root_list2 = ['ΤΡΙΛ','ΜΑΡΚ','ΚΟΡΝ','ΑΜΠΑΡ','ΑΡΡ','ΒΑΘΥΡΙ','ΒΑΡΚ','Β','ΒΟΛΒΟΡ','ΓΚΡ','ΓΛΥΚΟΡ','ΓΛΥΚΥΡ','ΙΜΠ','Λ','ΛΟΥ','ΜΑΡ','Μ','ΠΡ','ΜΠΡ','ΠΟΛΥΡ','Π','Ρ','ΠΙΠΕΡΟΡ']
                    
                    if 'mystem' in input_list:
                        root_list1 = root_list1 + ['ΝΟΜ'] #mystem
                        root_list2 = root_list2 + ['ΑΞ'] #mystem

                    if word in root_list1:
                        word = word +'I'
                    elif word in root_list2:
                        word = word +'IΖ'
                    done = True
                    break

       

        # S2 RULE page 31   saroukosstem
        if not done:
            for suffix in ['ΩΘΗΚΑ','ΩΘΗΚΕΣ','ΩΘΗΚΕ','ΩΘΗΚΑΜΕ','ΩΘΗΚΑΤΕ','ΩΘΗΚΑΝ','ΩΘΗΚΑΝΕ']:
                if ends_with(word, suffix):
                    word = word[:len(word) - len(suffix)]
                    root_list = ['ΑΛ','ΒΙ','ΕΝ','ΥΨ','ΛΙ','ΖΩ','Σ','Χ']
                    if 'mystem' in input_list:
                        root_list = root_list + ['ΣΗΚ','ΚΑΡΦ','ΑΓΧ','ΣΗΜΕΙ','ΣΚΟΤ'] #mystem
                    if word in root_list: #ΤΑ ΠΡΟΣΘΕΣΑ<----  #ΣΗΚΩΘΗΚΑ,ΚΑΡΦΩΘΗΚΑ,ΑΓΧΩΘΗΚΑ,....    #ΖΩΩΘΗΚΑ?????
                        word = word + 'ΩΝ'
                    done = True
                    break


        # S3 RULE page 31   saroukosstem
        if not done:
            for suffix in  ['ΙΣΑ','ΙΣΕΣ','ΙΣΕ','ΙΣΑΜΕ','ΙΣΑΤΕ','ΙΣΑΝ','ΙΣΑΝΕ']:
                if ends_with(word, suffix):
                    if word=='ΙΣΑ':
                        word = 'ΙΣ'
                        done = True
                        break
                    word = word[:len(word) - len(suffix)]
                    root_list1 = ['ΑΝΑΜΠΑ','ΑΘΡΟ','ΕΜΠΑ','ΕΣΕ','ΕΣΩΚΛΕ','ΕΠΑ','ΞΑΝΑΠΑ','ΕΠΕ','ΠΕΡΙΠΑ','ΑΘΡΟ','ΣΥΝΑΘΡΟ','ΔΑΝΕ','ΚΛΕ','ΧΑΡΤΟΠΑ','ΕΞΑΡΧΑ','ΜΕΤΕΠΕ','ΑΠΟΚΛΕ','ΑΠΕΚΛΕ','ΕΚΛΕ','ΠΕ','ΠΕΡΙΠΑ']
                    if 'mystem' in input_list:
                        root_list1 = root_list1 + ['ΝΟΜ'] # mystem
                    if word in root_list1:
                        word = word + 'Ι'
                    elif word in ['ΑΝ','ΑΦ','ΓΕ','ΓΙΓΑΝΤΟΑΦ','ΓΚΕ','ΔΗΜΟΚΡΑΤ','ΚΟΜ','ΓΚ','Μ','Π','ΠΟΥΚΑΜ','ΟΛΟ','ΛΑΡ']:
                        word = word + 'ΙΣ'
                    done = True
                    break


        # S4 RULE    saroukosstem        #λαθη: 'ΕΣΕ',  
        if not done:
            for suffix in  ['ΙΣΩ','ΙΣΕΙΣ','ΙΣΕΙ','ΙΣΟΥΜΕ','ΙΣΕΤΕ','ΙΣΟΥΝ','ΙΣΟΥΝΕ']:
                if ends_with(word, suffix):
                    word = word[:len(word) - len(suffix)]
                    if word in ['ΑΝΑΜΠΑ','ΑΘΡΟ','ΕΜΠΑ','ΕΣΕ','ΕΣΩΚΛΕ','ΕΠΑ','ΞΑΝΑΠΑ','ΕΠΕ','ΠΕΡΙΠΑ','ΣΥΝΑΘΡΟ','ΔΑΝΕ','ΚΛΕ','ΧΑΡΤΟΠΑ','ΕΞΑΡΧΑ','ΜΕΤΕΠΕ','ΑΠΟΚΛΕ','ΑΠΕΚΛΕ','ΕΚΛΕ','ΠΕ','ΠΕΡΙΠΑ']:
                        word = word + 'Ι'
                    done = True
                    break

        # S5 RULE   saroukosstem    #λαθη: 'M',λεξη 'ΙΣΤΟΣ' διαγραφεται
        if not done:
            for suffix in  ['ΙΣΤΟΣ','ΙΣΤΟΥ','ΙΣΤΟ','ΙΣΤΕ','ΙΣΤΟΙ','ΙΣΤΩΝ','ΙΣΤΟΥΣ','ΙΣΤΗ','ΙΣΤΗΣ','ΙΣΤΑ','ΙΣΤΕΣ']:
                if 'mystem' in input_list:
                    if word==suffix: # ΙΣΤΟΣ,ΙΣΤΟΙ,κλπ  # mystem
                            word = 'ΙΣΤ'
                            done = True
                            break
                if ends_with(word, suffix):
                    word = word[:len(word) - len(suffix)]
                    root_list = ['Μ','Π','ΑΠ','ΑΡ','ΗΔ','ΚΤ','ΣΚ','ΣΧ','ΥΨ','ΦΑ','ΧΡ','ΧΤ','ΑΚΤ','ΑΟΡ','ΑΣΧ','ΑΤΑ','ΑΧΝ','ΑΧΤ','ΓΕΜ','ΓΥΡ','ΕΜΠ','ΕΥΠ','ΕΧΘ','ΗΦΑ','ΉΦΑ','ΚΑΘ','ΚΑΚ','ΚΥΛ','ΛΥΓ','ΜΑΚ','ΜΕΓ','ΤΑΧ','ΦΙΛ','ΧΩΡ']
                    if 'mystem' in input_list:
                        root_list = root_list + ['Λ','ΜΕΓ','ΕΛΑΧ','ΕΥΧΑΡ'] #mystem
                    if word in root_list:
                        word = word + 'ΙΣΤ'
                    elif word in ['ΔΑΝΕ','ΣΥΝΑΘΡΟ','ΚΛΕ','ΣΕ','ΕΣΩΚΛΕ','ΑΣΕ','ΠΛΕ']:
                        word = word + 'Ι'
                    done = True
                    break


        # S6 RULE   saroukosstem
        if not done:
            for suffix in  ['ΙΣΜΟ','ΙΣΜΟΙ','ΙΣΜΟΣ','ΙΣΜΟΥ','ΙΣΜΟΥΣ','ΙΣΜΩΝ']:
                if ends_with(word, suffix):
                    word = word[:len(word) - len(suffix)]
                    if word in ['ΑΓΝΩΣΤΙΚ','ΑΤΟΜΙΚ','ΓΝΩΣΤΙΚ','ΕΘΝΙΚ','ΕΚΛΕΚΤΙΚ','ΣΚΕΠΤΙΚ','ΤΟΠΙΚ']: 
                        word = word[:-4] #removes 'IK'
                    elif word in ['ΣΕ','ΜΕΤΑΣΕ','ΜΙΚΡΟΣΕ','ΕΓΚΛΕ','ΑΠΟΚΛΕ']:
                        word = word + 'ΙΣΜ'
                    elif word in ['ΔΑΝΕ','ΑΝΤΙΔΑΝΕ']:
                        word = word + 'Ι'
                    elif word in ['ΑΛΕΞΑΝΔΡΙΝ','ΒΥΖΑΝΤΙΝ','ΘΕΑΤΡΙΝ']:
                        word = word[:-4] #removes 'IN'
                    done = True
                    break

        # S7 RULE   saroukosstem    
            for suffix in  ['ΑΡΑΚΙ','ΑΡΑΚΙΑ','ΟΥΔΑΚΙ','ΟΥΔΑΚΙΑ']:
                if ends_with(word, suffix):
                    word = word[:len(word) - len(suffix)]
                    if word in ['X','Σ']:
                        word = word + 'ΑΡΑΚΙ'
                    elif 'mystem' in input_list and word in ['ΚΛΩΝ','ΘΥΜ']: # mystem
                        word = word + 'ΑΡ'
                    done = True
                    break


        # S8 rule   saroukosstem
        if not done:
            for suffix in  ['ΑΚΙ','ΑΚΙΑ','ΙΤΣΑ','ΙΤΣΑΣ','ΙΤΣΕΣ','ΙΤΣΩΝ','ΑΡΑΚΙ','ΑΡΑΚΙΑ']:
                if ends_with(word, suffix):
                    word = word[:len(word) - len(suffix)]
                    if word in ['ΑΝΘΡ','ΒΑΜΒ','ΒΡ','ΚΑΙΜ','ΚΟΝ','ΚΟΡ','ΛΑΒΡ','ΛΟΥΛ','ΜΕΡ','ΜΟΥΣΤ','ΝΑΓΚΑΣ','ΠΛ','Ρ','ΡΥ','Σ','ΣΚ','ΣΟΚ','ΣΠΑΝ','ΤΖ','ΦΑΡΜ','Χ','ΚΑΠΑΚ','ΑΛΙΣΦ','ΑΜΒΡ','ΑΝΘΡ','Κ','ΦΥΛ','ΚΑΤΡΑΠ','ΚΛΙΜ','ΜΑΛ','ΣΛΟΒ','ΣΦ','ΤΣΕΧΟΣΛΟΒ']:
                        word = word + 'ΑΚ'
                    elif word in ['Β','ΒΑΛ','ΓΙΑΝ','ΓΛ','Ζ','ΗΓΟΥΜΕΝ','ΚΑΡΔ','ΚΟΝ','ΜΑΚΡΥΝ','ΝΥΦ','ΠΑΤΕΡ','Π','ΣΚ','ΤΟΣ','ΤΡΙΠΟΛ']:
                        word = word + 'ΙΤΣ'
                    elif ends_with(word,'ΚΟΡ'):
                        word = word + 'ΙΤΣ'
                    done = True
                    break

        # S9 RULE   saroukosstem
        if not done:
            for suffix in ['ΙΔΙΟ','ΙΔΙΑ','ΙΔΙΩΝ']:
               if ends_with(word, suffix):
                    word = word[:len(word) - len(suffix)]
                    root_list = ['Ε','ΠΑΙΧΝ']
                    if 'mystem' in input_list:
                        root_list = root_list + ['ΠΑ'] #mystem
                    for s in root_list:
                       if ends_with(word, s):
                             word = word + 'ΙΔ'
                             break
                    if word in ['ΑΙΦΝ','ΙΡ','ΟΛΟ','ΨΑΛ']:
                        word = word + 'ΙΔ'
                    done=True
                    break


        # S10 RULE      saroukosstem
        if not done:
            for suffix in ['ΙΣΚΟΣ','ΙΣΚΟΥ','ΙΣΚΟ','ΙΣΚΕ']:
               if ends_with(word, suffix):
                    word = word[:len(word) - len(suffix)]
                    if word in ['Δ','ΙΒ','ΜΗΝ','Ρ','ΦΡΑΓΚ','ΛΥΚ','ΟΒΕΛ']:
                         word = word + 'ΙΣΚ'
                    done=True
                    break



    #--------------ΝΤΑΗΣ RULES-----------------
                
    ##rule-set  1   #SKROUTZ
    ##ΓΙΑΓΙΑΔΕΣ->ΓΙΑΓ, ΟΜΑΔΕΣ->ΟΜΑΔ
    if not done:
        suffix_list = ['ΙΑΔΕΣ','ΑΔΕΣ','ΑΔΩΝ']   #'ΙΑΔΕΣ' NOT IN ΝΤΑΗΣ
        if 'mystem' in input_list:
            suffix_list = ['ΙΑΔΩΝ','ΙΑΔΑ'] + suffix_list # mystem

        for suffix in suffix_list:   
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                remaining_part_does_not_end_on = True
                root_list = ['ΟΚ', 'ΜΑΜ', 'ΜΑΝ', 'ΜΠΑΜΠ', 'ΠΑΤΕΡ', 'ΓΙΑΓ', 'ΝΤΑΝΤ', 'ΚΥΡ', 'ΘΕΙ', 'ΠΕΘΕΡ']
                if 'skroutz' in input_list:
                    root_list = root_list + ['ΠΕΘΕΡ','ΜΟΥΣΑΜ','ΚΑΠΛΑΜ','ΠΑΡ','ΨΑΡ','ΤΖΟΥΡ','ΤΑΜΠΟΥΡ'] # skroutzstem
                if 'mystem' in input_list:
                    root_list = root_list + ['ΧΙΛ','ΜΥΡ','ΟΛΥΜΠ'] # mystem
                for s in root_list:
                    if ends_with(word, s):
                        remaining_part_does_not_end_on = False
                        break
                if remaining_part_does_not_end_on:
                    word = word + 'ΑΔ'
                done = True
                break

    ##rule-set  2
    ##ΚΑΦΕΔΕΣ->ΚΑΦ, ΓΗΠΕΔΩΝ->ΓΗΠΕΔ
    if not done:
        for suffix in ['ΕΔΕΣ', 'ΕΔΩΝ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                for s in ['ΟΠ', 'ΙΠ', 'ΕΜΠ', 'ΥΠ', 'ΓΗΠ', 'ΔΑΠ', 'ΚΡΑΣΠ', 'ΜΙΛ']:
                    if ends_with(word, s):
                        word = word + 'ΕΔ'
                        break
                done = True
                break

    ##rule-set  3
    ##ΠΑΠΠΟΥΔΩΝ->ΠΑΠΠ, ΑΡΚΟΥΔΕΣ->ΑΡΚΟΥΔ
    if not done:
        for suffix in ['ΟΥΔΕΣ', 'ΟΥΔΩΝ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                for s in ['ΑΡΚ', 'ΚΑΛΙΑΚ', 'ΠΕΤΑΛ', 'ΛΙΧ', 'ΠΛΕΞ', 'ΣΚ', 'Σ', 'ΦΛ', 'ΦΡ', 'ΒΕΛ', 'ΛΟΥΛ', 'ΧΝ', 'ΣΠ', 'ΤΡΑΓ', 'ΦΕ']:
                    if ends_with(word, s):
                        word = word + 'ΟΥΔ'
                        break
                done = True
                break

    ##rule-set  4   #SKROUTZ
    ## ΥΠΟΘΕΣΕΩΣ->ΥΠΟΘΕΣ, ΘΕΩΝ->ΘΕ
    if not done:
        suffix_list = ['ΕΩΣ', 'ΕΩΝ']
        if 'skroutz' in input_list:
            suffix_list = suffix_list + ['ΕΑΣ','ΕΑ'] # skroutzstem
        for suffix in suffix_list: 
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                root_list = ['Θ', 'Δ', 'ΕΛ', 'ΓΑΛ', 'Ν', 'Π', 'ΙΔ','ΠΑΡ']
                if 'skroutz' in input_list:
                    root_list = root_list + ['ΣΤΕΡ','ΟΡΦ','ΑΝΔΡ','ΑΝΤΡ'] # skroutzstem
                if 'mystem' in input_list:
                    root_list = root_list + ['ΦΟΡ'] # mystem
                for s in root_list:
                    if ends_with(word, s):
                        word = word + 'Ε'
                        break
                done = True
                break


    # step 3a apo skroutz  
    #skroutzstem    #skroutzrule
    # be conservative with this rule, take care for overstemming. πχ το 'ΣΤΟΙΧΕΙΑ'-->'ΣΤΟΙΧ'
    if 'skroutz' in input_list:
        if not done:
            suffix_list = ['ΕΙΟ','ΕΙΟΣ','ΕΙΟΙ','ΕΙΑ','ΕΙΑΣ','ΕΙΕΣ','ΕΙΟΥ','ΕΙΟΥΣ','ΕΙΩΝ']
            for suffix in suffix_list: 
                if ends_with(word, suffix):
                    if len(word) - len(suffix)>4:
                        word = word[:len(word) - len(suffix)]
                        done = True
                        break


    ##rule-set  5   #SKROUTZ
    ##ΠΑΙΔΙΑ->ΠΑΙΔ, ΤΕΛΕΙΟΥ->ΤΕΛΕΙ
    if not done:
        suffix_list = ['ΙΑ', 'ΙΟΥ', 'ΙΩΝ']
        if 'skroutz' in input_list:
            suffix_list = suffix_list + ['ΙΟΥΣ','ΙΑΣ','ΙΕΣ','ΙΟΣ','ΙΟΙ','ΙΟΝ','ΙΟ'] # skroutzstem
        for suffix in suffix_list:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                for s in VOWELS:
                    if ends_with(word, s):
                        word = word + 'Ι'
                        break
                if 'skroutz' in input_list:
                    root_list = ['ΑΓ','ΑΓΓΕΛ','ΑΓΡ','ΑΕΡ','ΑΘΛ','ΑΚΟΥΣ','ΑΞ','ΑΣ','Β','ΒΙΒΛ','ΒΥΤ','Γ','ΓΙΑΓ','ΓΩΝ','Δ','ΔΑΝ','ΔΗΛ','ΔΗΜ',
                         'ΔΟΚΙΜ','ΕΛ','ΖΑΧΑΡ','ΗΛ','ΗΠ','ΙΔ','ΙΣΚ','ΙΣΤ','ΙΟΝ','ΙΩΝ','ΚΙΜΩΛ','ΚΟΛΟΝ','ΚΟΡ',
                         'ΚΤΗΡ','ΚΥΡ','ΛΑΓ','ΛΟΓ','ΜΑΓ','ΜΠΑΝ','ΜΠΕΤΟΝ','ΜΠΡ','ΝΑΥΤ','ΝΟΤ','ΟΠΑΛ','ΟΞ','ΟΡ','ΟΣ',
                         'ΠΑΝΑΓ','ΠΑΤΡ','ΠΗΛ','ΠΗΝ','ΠΛΑΙΣ','ΠΟΝΤ','ΡΑΔ','ΡΟΔ','ΣΚ','ΣΚΟΡΠ','ΣΟΥΝ','ΣΠΑΝ',
                         'ΣΤΑΔ','ΣΥΡ','ΤΗΛ','ΤΙΜ','ΤΟΚ','ΤΟΠ','ΤΡΟΧ','ΦΙΛ','ΦΩΤ','Χ','ΧΙΛ','ΧΡΩΜ','ΧΩΡ']    #skroutzstem
                    if word in root_list:
                         word = word + 'Ι'
                    elif word == 'ΠΑΛ': #skroutzstem
                        word = word + 'ΑΙ'
                done = True
                break
    
    ##rule-set  6   #SKROUTZ 
    ##ΖΗΛΙΑΡΙΚΟ->ΖΗΛΙΑΡ, ΑΓΡΟΙΚΟΣ->ΑΓΡΟΙΚ
    if not done:
        suffix_list = ['ΙΚΑ', 'ΙΚΟΥ', 'ΙΚΩΝ', 'ΙΚΟΣ', 'ΙΚΟ', 'ΙΚΗ']
        if 'skroutz' in input_list:
            suffix_list = suffix_list + ['ΙΚΟΝ','ΙΚΕΙΣ','ΙΚΟΙ','ΙΚΕΣ','ΙΚΟΥΣ','ΙΚΗΣ','ΙΚΩΣ'] #skroutzstem
        for suffix in suffix_list:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                root_list = ['ΑΛ', 'ΑΔ', 'ΕΝΔ', 'ΑΜΑΝ', 'ΑΜΜΟΧΑΛ', 'ΗΘ', 'ΑΝΗΘ', 'ΑΝΤΙΔ', 'ΦΥΣ', 'ΒΡΩΜ', 'ΓΕΡ', 'ΕΞΩΔ', 'ΚΑΛΠ',
                            'ΚΑΛΛΙΝ', 'ΚΑΤΑΔ', 'ΜΟΥΛ', 'ΜΠΑΝ', 'ΜΠΑΓΙΑΤ', 'ΜΠΟΛ', 'ΜΠΟΣ', 'ΝΙΤ', 'ΞΙΚ', 'ΣΥΝΟΜΗΛ', 'ΠΕΤΣ', 'ΠΙΤΣ',
                            'ΠΙΚΑΝΤ', 'ΠΛΙΑΤΣ', 'ΠΟΝΤ', 'ΠΟΣΤΕΛΝ', 'ΠΡΩΤΟΔ', 'ΣΕΡΤ', 'ΣΥΝΑΔ', 'ΤΣΑΜ', 'ΥΠΟΔ', 'ΦΙΛΟΝ', 'ΦΥΛΟΔ',
                            'ΧΑΣ']
                if 'skroutz' in input_list:
                    root_list = root_list + ['ΑΜΕΡ','ΑΠΛ','ΑΤΤ','ΑΦΡ','ΒΑΣ','ΓΕΝ',
                                             'Δ','ΔΙΚΑΝ','ΔΥΤ','ΕΙΔ','ΘΕΤ','ΚΟΥΖΙΝ','ΚΡ','ΚΩΔ','ΛΟΓ','Μ','ΜΕΡ','ΜΟΝΑΔ','ΜΟΥΣ',
                                             'ΜΥΣΤ','Ν','ΟΠΤ','ΠΑΝ''ΠΛΑΣΤ','ΣΗΜΑΝΤ','ΣΤΑΤ','ΤΕΛ','ΤΕΧΝ','ΤΡΟΠ','Φ','ΦΟΙΝ',] #skroutzstem
                if 'mystem' in input_list:                        
                    root_list = root_list + ['ΕΘΝ']  #mystem    
                if word in root_list:
                    word = word + 'ΙΚ'
                else:
                    for s in VOWELS:
                        if ends_with(word, s):
                            word = word + 'ΙΚ'
                            break
                done = True
                break

    ##rule-set  7
    ##ΑΓΑΠΑΓΑΜΕ->ΑΓΑΠ, ΑΝΑΠΑΜΕ->ΑΝΑΠΑΜ
    if not done:
        if word == 'ΑΓΑΜΕ': word = 2*word
        for suffix in ['ΗΘΗΚΑΜΕ', 'ΑΓΑΜΕ', 'ΗΣΑΜΕ', 'ΟΥΣΑΜΕ', 'ΗΚΑΜΕ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in ['Φ']:       #not in skroutz or ntais
                    word = word + 'ΑΓΑΜ'    
                done = True
                break
        if not done and ends_with(word, 'ΑΜΕ'):
            word = word[:len(word) - len('ΑΜΕ')]
            if word in ['ΑΝΑΠ', 'ΑΠΟΘ', 'ΑΠΟΚ', 'ΑΠΟΣΤ', 'ΒΟΥΒ', 'ΞΕΘ', 'ΟΥΛ', 'ΠΕΘ', 'ΠΙΚΡ', 'ΠΟΤ', 'ΣΙΧ', 'Χ']:
                word = word + 'ΑΜ'
            done = True

    ##rule-set  8
    ##ΑΓΑΠΗΣΑΜΕ->ΑΓΑΠ, ΤΡΑΓΑΝΕ->ΤΡΑΓΑΝ
    if not done:
        for suffix in ['ΙΟΥΝΤΑΝΕ', 'ΙΟΝΤΑΝΕ', 'ΟΥΝΤΑΝΕ', 'ΗΘΗΚΑΝΕ', 'ΟΥΣΑΝΕ', 'ΙΟΤΑΝΕ', 'ΟΝΤΑΝΕ', 'ΑΓΑΝΕ', 'ΗΣΑΝΕ',
                       'ΟΤΑΝΕ', 'ΗΚΑΝΕ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in ['ΤΡ', 'ΤΣ', 'Φ']:
                    word = word + 'ΑΓΑΝ'
                done = True
                break
        if not done and ends_with(word, 'ΑΝΕ'):
            word = word[:len(word) - len('ΑΝΕ')] 
            root_list = ['ΒΕΤΕΡ', 'ΒΟΥΛΚ', 'ΒΡΑΧΜ', 'Γ', 'ΔΡΑΔΟΥΜ', 'Θ', 'ΚΑΛΠΟΥΖ', 'ΚΑΣΤΕΛ', 'ΚΟΡΜΟΡ', 'ΛΑΟΠΛ', 'ΜΩΑΜΕΘ', 'Μ',
                        'ΜΟΥΣΟΥΛΜ', 'Ν', 'ΟΥΛ', 'Π', 'ΠΕΛΕΚ', 'ΠΛ', 'ΠΟΛΙΣ', 'ΠΟΡΤΟΛ', 'ΣΑΡΑΚΑΤΣ', 'ΣΟΥΛΤ', 'ΤΣΑΡΛΑΤ', 
                        'ΤΣΙΓΓ', 'ΤΣΟΠ', 'ΦΩΤΟΣΤΕΦ', 'Χ', 'ΨΥΧΟΠΛ', 'ΑΓ', 'ΓΑΛ', 'ΓΕΡ', 'ΔΕΚ', 'ΔΙΠΛ', 'ΑΜΕΡΙΚΑΝ', 'ΟΥΡ',
                        'ΠΙΘ', 'ΠΟΥΡΙΤ', 'Σ', 'ΖΩΝΤ', 'ΙΚ', 'ΚΑΣΤ', 'ΚΟΠ', 'ΛΙΧ', 'ΛΟΥΘΗΡ', 'ΜΑΙΝΤ', 'ΜΕΛ', 'ΣΙΓ', 'ΣΠ', 'ΣΤΕΓ',
                        'ΤΡΑΓ', 'ΤΣΑΓ', 'Φ', 'ΕΡ', 'ΑΔΑΠ', 'ΑΘΙΓΓ', 'ΑΜΗΧ', 'ΑΝΙΚ', 'ΑΝΟΡΓ', 'ΑΠΗΓ', 'ΑΠΙΘ', 'ΑΤΣΙΓΓ', 'ΒΑΣ',
                        'ΒΑΣΚ', 'ΒΑΘΥΓΑΛ', 'ΒΙΟΜΗΧ', 'ΒΡΑΧΥΚ', 'ΔΙΑΤ', 'ΔΙΑΦ', 'ΕΝΟΡΓ', 'ΘΥΣ', 'ΚΑΠΝΟΒΙΟΜΗΧ', 'ΚΑΤΑΓΑΛ', 'ΚΛΙΒ',
                        'ΚΟΙΛΑΡΦ', 'ΛΙΒ', 'ΜΕΓΛΟΒΙΟΜΗΧ', 'ΜΙΚΡΟΒΙΟΜΗΧ', 'ΝΤΑΒ', 'ΞΗΡΟΚΛΙΒ', 'ΟΛΙΓΟΔΑΜ', 'ΟΛΟΓΑΛ', 'ΠΕΝΤΑΡΦ',
                        'ΠΕΡΗΦ', 'ΠΕΡΙΤΡ', 'ΠΛΑΤ', 'ΠΟΛΥΔΑΠ', 'ΠΟΛΥΜΗΧ', 'ΣΤΕΦ', 'ΤΑΒ', 'ΤΕΤ', 'ΥΠΕΡΗΦ', 'ΥΠΟΚΟΠ', 'ΧΑΜΗΛΟΔΑΠ',
                        'ΨΗΛΟΤΑΒ']
            if 'skroutz' in input_list:
                root_list = root_list + ['ΟΡΦ'] #skroutzstem
            if word in root_list:
                word = word + 'ΑΝ'
            else:
                for s in VOWELS:
                    if ends_with(word, s):
                        word = word + 'ΑΝ'
                        break
            done = True

    ##rule-set  9
    ##ΑΓΑΠΗΣΕΤΕ->ΑΓΑΠ, ΒΕΝΕΤΕ->ΒΕΝΕΤ
    if not done:
        if ends_with(word, 'ΗΣΕΤΕ'):
            word = word[:len(word) - len('ΗΣΕΤΕ')]
            done = True
        elif ends_with(word, 'ΕΤΕ'):
            word = word[:len(word) - len('ΕΤΕ')]
            if word in ['ΑΒΑΡ', 'ΒΕΝ', 'ΕΝΑΡ', 'ΑΒΡ', 'ΑΔ', 'ΑΘ', 'ΑΝ', 'ΑΠΛ', 'ΒΑΡΟΝ', 'ΝΤΡ', 'ΣΚ', 'ΚΟΠ', 'ΜΠΟΡ', 'ΝΙΦ', 'ΠΑΓ',
                        'ΠΑΡΑΚΑΛ', 'ΣΕΡΠ', 'ΣΚΕΛ', 'ΣΥΡΦ', 'ΤΟΚ', 'Υ', 'Δ', 'ΕΜ', 'ΘΑΡΡ', 'Θ']:
                word = word + 'ΕΤ'
            else:
                for s in ['ΟΔ', 'ΑΙΡ', 'ΦΟΡ', 'ΤΑΘ', 'ΔΙΑΘ', 'ΣΧ', 'ΕΝΔ', 'ΕΥΡ', 'ΤΙΘ', 'ΥΠΕΡΘ', 'ΡΑΘ', 'ΕΝΘ', 'ΡΟΘ', 'ΣΘ', 'ΠΥΡ',
                          'ΑΙΝ', 'ΣΥΝΔ', 'ΣΥΝ', 'ΣΥΝΘ', 'ΧΩΡ', 'ΠΟΝ', 'ΒΡ', 'ΚΑΘ', 'ΕΥΘ', 'ΕΚΘ', 'ΝΕΤ', 'ΡΟΝ', 'ΑΡΚ', 'ΒΑΡ', 'ΒΟΛ',
                          'ΩΦΕΛ'] + VOWELS:
                    if ends_with(word, s):
                        word = word + 'ΕΤ'
                        break
            done = True

    ##rule-set 10
    ##ΑΓΑΠΩΝΤΑΣ->ΑΓΑΠ, ΞΕΝΟΦΩΝΤΑΣ->ΞΕΝΟΦΩΝ
    if not done:
        for suffix in ['ΟΝΤΑΣ', 'ΩΝΤΑΣ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in ['ΑΡΧ']:
                    word = word + 'ΟΝΤ'
                elif word in ['ΞΕΝΟΦ', 'ΚΡΕ']: #'ΞΕΝΟΦ' not in skroutz or ntais
                    word = word + 'ΩΝΤ'
                done = True
                break

    ##rule-set 11
    ##ΑΓΑΠΙΟΜΑΣΤΕ->ΑΓΑΠ, ΟΝΟΜΑΣΤΕ->ΟΝΟΜΑΣΤ
    if not done:
        for suffix in ['ΙΟΜΑΣΤΕ', 'ΟΜΑΣΤΕ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in ['ΟΝ']:
                    word = word + 'ΟΜΑΣΤ'
                done = True
                break

    ##rule-set 12
    ##ΑΓΑΠΙΕΣΤΕ->ΑΓΑΠ, ΠΙΕΣΤΕ->ΠΙΕΣΤ
    if not done:
        for suffix in ['ΙΕΣΤΕ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in ['Π', 'ΑΠ', 'ΣΥΜΠ', 'ΑΣΥΜΠ', 'ΑΚΑΤΑΠ', 'ΑΜΕΤΑΜΦ']: #correction from ntais 'ΑΚΑΤΑΠ', 'ΑΜΕΤΑΜΦ'
                    word = word + 'ΙΕΣΤ'
                done = True
                break
    if not done:
        for suffix in ['ΕΣΤΕ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in ['ΑΛ', 'ΑΡ', 'ΕΚΤΕΛ', 'Ζ', 'Μ', 'Ξ', 'ΠΑΡΑΚΑΛ', 'ΑΡ', 'ΠΡΟ', 'ΝΙΣ']:
                    word = word + 'ΕΣΤ'
                done = True
                break

    ##rule-set 13
    ##ΧΤΙΣΤΗΚΕ->ΧΤΙΣΤ, ΔΙΑΘΗΚΕΣ->ΔΙΑΘΗΚ
    if not done:
        for suffix in ['ΗΘΗΚΑ', 'ΗΘΗΚΕΣ', 'ΗΘΗΚΕ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                done = True
                break
    if not done:
        for suffix in ['ΗΚΑ', 'ΗΚΕΣ', 'ΗΚΕ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in ['ΔΙΑΘ', 'Θ', 'ΠΑΡΑΚΑΤΑΘ', 'ΠΡΟΣΘ', 'ΣΥΝΘ']:
                    word = word + 'ΗΚ'
                else:
                    for suffix in ['ΣΚΩΛ', 'ΣΚΟΥΛ', 'ΝΑΡΘ', 'ΣΦ', 'ΟΘ', 'ΠΙΘ']:
                        if ends_with(word, suffix):
                            word = word + 'ΗΚ'
                            break
                done = True
                break
       
    
       # step 5h apo skroutz
    ##rule-set 14
    ##ΧΤΥΠΟΥΣΕΣ->ΧΤΥΠ, ΜΕΔΟΥΣΕΣ->ΜΕΔΟΥΣ
    if not done:
        for suffix in ['ΟΥΣΑ', 'ΟΥΣΕΣ', 'ΟΥΣΕ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in ['ΦΑΡΜΑΚ', 'ΧΑΔ', 'ΑΓΚ', 'ΑΝΑΡΡ', 'ΒΡΟΜ', 'ΕΚΛΙΠ', 'ΛΑΜΠΙΔ', 'ΛΕΧ', 'Μ', 'ΠΑΤ', 'Ρ', 'Λ', 'ΜΕΔ', 'ΜΕΣΑΖ',
                            'ΥΠΟΤΕΙΝ', 'ΑΜ', 'ΑΙΘ', 'ΑΝΗΚ', 'ΔΕΣΠΟΖ', 'ΕΝΔΙΑΦΕΡ', 'ΔΕ', 'ΔΕΥΤΕΡΕΥ', 'ΚΑΘΑΡΕΥ', 'ΠΛΕ', 'ΤΣΑ']:
                    word = word + 'ΟΥΣ'
                else:
                    for s in ['ΠΟΔΑΡ', 'ΒΛΕΠ', 'ΠΑΝΤΑΧ', 'ΦΡΥΔ', 'ΜΑΝΤΙΛ', 'ΜΑΛΛ', 'ΚΥΜΑΤ', 'ΛΑΧ', 'ΛΗΓ', 'ΦΑΓ', 'ΟΜ', 'ΠΡΩΤ'] + VOWELS:
                        if ends_with(word, s):
                            word = word + 'ΟΥΣ'
                            break
                done = True
                break

    ##rule-set 15
    #ΚΟΛΛΑΓΕΣ->ΚΟΛΛ, ΑΒΑΣΤΑΓΑ->ΑΒΑΣΤ
    if not done:
        for suffix in ['ΑΓΑ', 'ΑΓΕΣ', 'ΑΓΕ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in ['ΑΒΑΣΤ', 'ΠΟΛΥΦ', 'ΑΔΗΦ', 'ΠΑΜΦ', 'Ρ', 'ΑΣΠ', 'ΑΦ', 'ΑΜΑΛ', 'ΑΜΑΛΛΙ', 'ΑΝΥΣΤ', 'ΑΠΕΡ', 'ΑΣΠΑΡ', 'ΑΧΑΡ',
                            'ΔΕΡΒΕΝ', 'ΔΡΟΣΟΠ', 'ΞΕΦ', 'ΝΕΟΠ', 'ΝΟΜΟΤ', 'ΟΛΟΠ', 'ΟΜΟΤ', 'ΠΡΟΣΤ', 'ΠΡΟΣΩΠΟΠ', 'ΣΥΜΠ', 'ΣΥΝΤ', 'Τ',
                            'ΥΠΟΤ', 'ΧΑΡ', 'ΑΕΙΠ', 'ΑΙΜΟΣΤ', 'ΑΝΥΠ', 'ΑΠΟΤ', 'ΑΡΤΙΠ', 'ΔΙΑΤ', 'ΕΝ', 'ΕΠΙΤ', 'ΚΡΟΚΑΛΟΠ', 'ΣΙΔΗΡΟΠ',
                            'Λ', 'ΝΑΥ', 'ΟΥΛΑΜ', 'ΟΥΡ', 'Π', 'ΤΡ', 'Μ']:
                    word = word + 'ΑΓ'
                else:
                    for s in ['ΟΦ', 'ΠΕΛ', 'ΧΟΡΤ', 'ΣΦ', 'ΡΠ', 'ΦΡ', 'ΠΡ', 'ΛΟΧ', 'ΣΜΗΝ']:
                        # ΑΦΑΙΡΕΘΗΚΕ: 'ΛΛ'
                        if ends_with(word, s):
                            if not word in ['ΨΟΦ', 'ΝΑΥΛΟΧ']:
                                word = word + 'ΑΓ'
                            break
                done = True
                break

    ##rule-set 16
    ##ΑΓΑΠΗΣΕ->ΑΓΑΠ, ΝΗΣΟΥ->ΝΗΣ
    if not done:
        for suffix in ['ΗΣΕ', 'ΗΣΟΥ', 'ΗΣΑ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in ['Ν', 'ΧΕΡΣΟΝ', 'ΔΩΔΕΚΑΝ', 'ΕΡΗΜΟΝ', 'ΜΕΓΑΛΟΝ', 'ΕΠΤΑΝ', 'ΑΓΑΘΟΝ']:
                    word = word + 'ΗΣ'
                done = True
                break
            
    ##rule-set 17
    ##ΑΓΑΠΗΣΤΕ->ΑΓΑΠ, ΣΒΗΣΤΕ->ΣΒΗΣΤ
    if not done:
        for suffix in ['ΗΣΤΕ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in ['ΑΣΒ', 'ΣΒ', 'ΑΧΡ', 'ΧΡ', 'ΑΠΛ', 'ΑΕΙΜΝ', 'ΔΥΣΧΡ', 'ΕΥΧΡ', 'ΚΟΙΝΟΧΡ', 'ΠΑΛΙΜΨ']:
                    word = word + 'ΗΣΤ'
                done = True
                break
            
    ##rule-set 18
    ##ΑΓΑΠΟΥΝΕ->ΑΓΑΠ, ΣΠΙΟΥΝΕ->ΣΠΙΟΥΝ
    if not done:
        for suffix in ['ΟΥΝΕ', 'ΗΣΟΥΝΕ', 'ΗΘΟΥΝΕ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in ['Ν', 'Ρ', 'ΣΠΙ', 'ΣΤΡΑΒΟΜΟΥΤΣ', 'ΚΑΚΟΜΟΥΤΣ', 'ΕΞΩΝ']:
                    word = word + 'OYN'
                done = True
                break
            
    ##rule-set 19
    ##ΑΓΑΠΟΥΜΕ->ΑΓΑΠ, ΦΟΥΜΕ->ΦΟΥΜ
    if not done:
        for suffix in ['ΟΥΜΕ', 'ΗΣΟΥΜΕ', 'ΗΘΟΥΜΕ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if word in ['ΠΑΡΑΣΟΥΣ', 'Φ', 'Χ', 'ΩΡΙΟΠΛ', 'ΑΖ', 'ΑΛΛΟΣΟΥΣ', 'ΑΣΟΥΣ']:
                    word = word + 'ΟΥΜ'
                done = True
                break
            
    ##rule-set 20   #SKROUTZ
    ##ΚΥΜΑΤΑ->ΚΥΜ, ΧΩΡΑΤΟ->ΧΩΡΑΤ
    if not done:
        suffix_list = ['ΜΑΤΑ', 'ΜΑΤΩΝ', 'ΜΑΤΟΣ']
        if 'skroutz' in input_list:
            suffix_list = suffix_list + ['ΜΑΤΟΙ','ΜΑΤΟΥΣ','ΜΑΤΟ','ΜΑΤΩΣ','ΜΑΤΕΣ','ΜΑΤΗ','ΜΑΤΗΣ','ΜΑΤΟΥ'] #skroutzstem
        for suffix in suffix_list:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                word = word + 'Μ'
                if 'skroutz' in input_list:
                    if word in ['ΓΕ','ΣΤΑ']:    #skroutzstem
                        word = word + 'ΑΤ'
                    elif word == 'ΓΡΑΜ':    #skroutzstem
                         word = word + 'Α'
                done = True
                break
    

    #SKROUTZ step 6b #not in ntais
    #skroutzstem    #skroutzrule
    if 'skroutz' in input_list:
        if not done:    #periergo rule eg.ΝΙΚΑΡΑΓΟΥΑ
            suffix = 'ΟΥΑ'
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                word = word + 'ΟΥ'
                done = True
                # break


    #rule-set 21'   #SKROUTZ  #step 6 apo saloustro
    if not done:
        suffix_list = [ 'ΙΟΝΤΟΥΣΑΝ', 'ΙΟΥΜΑΣΤΕ', 'ΙΟΜΑΣΤΑΝ', 'ΙΟΣΑΣΤΑΝ', 'ΟΝΤΟΥΣΑΝ', 'ΙΟΣΑΣΤΕ', 'ΙΕΜΑΣΤΕ', 'ΙΕΣΑΣΤΕ', 'ΙΟΜΟΥΝΑ',
                       'ΙΟΣΟΥΝΑ', 'ΙΟΥΝΤΑΙ', 'ΙΟΥΝΤΑΝ', 'ΗΘΗΚΑΤΕ', 'ΟΜΑΣΤΑΝ', 'ΟΣΑΣΤΑΝ', 'ΟΥΜΑΣΤΕ', 'ΙΟΜΟΥΝ', 'ΙΟΝΤΑΝ', 'ΙΟΣΟΥΝ',
                       'ΗΘΕΙΤΕ', 'ΗΘΗΚΑΝ', 'ΟΜΟΥΝΑ', 'ΟΣΑΣΤΕ', 'ΟΣΟΥΝΑ', 'ΟΥΝΤΑΙ', 'ΟΥΝΤΑΝ', 'ΟΥΣΑΤΕ',  'ΑΓΑΤΕ', 'ΕΙΤΑΙ', 'ΙΕΜΑΙ',
                       'ΙΕΤΑΙ', 'ΙΕΣΑΙ', 'ΙΟΤΑΝ', 'ΙΟΥΜΑ', 'ΗΘΕΙΣ', 'ΗΘΟΥΝ', 'ΗΚΑΤΕ', 'ΗΣΑΤΕ', 'ΗΣΟΥΝ', 'ΟΜΟΥΝ',  'ΟΝΤΑΙ',
                       'ΟΝΤΑΝ', 'ΟΣΟΥΝ', 'ΟΥΜΑΙ', 'ΟΥΣΑΝ',  'ΑΓΑΝ', 'ΑΜΑΙ', 'ΑΣΑΙ', 'ΑΤΑΙ', 'ΕΙΤΕ', 'ΕΣΑΙ', 'ΕΤΑΙ', 'ΗΔΕΣ',
                       'ΗΔΩΝ', 'ΗΘΕΙ', 'ΗΚΑΝ', 'ΗΣΑΝ', 'ΗΣΕΙ', 'ΗΣΕΣ', 'ΟΜΑΙ', 'ΟΤΑΝ',  'ΑΕΙ',  'ΕΙΣ',  'ΗΘΩ',  'ΗΣΩ', 'ΟΥΝ',
                       'ΟΥΣ',  'ΑΝ', 'ΑΣ', 'ΑΩ', 'ΕΙ', 'ΕΣ', 'ΗΣ', 'ΟΙ', 'ΟΝ', 'ΟΣ', 'ΟΥ', 'ΥΣ', 'ΩΝ', 'ΩΣ', 'Ι','Α', 'Ε', 'Η',
                       'Ο',  'Υ', 'Ω']
        if 'skroutz' in input_list:
            suffix_list = ['ΥΑ','ΟΙΣ'] + suffix_list #skroutzstem

        for suffix in suffix_list: 
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                done = True
                break

    ##rule-set 22   #SKROUTZ 
    ##ΠΛΗΣΙΕΣΤΑΤΟΣ->ΠΛΥΣΙ, ΜΕΓΑΛΥΤΕΡΗ->ΜΕΓΑΛ, ΚΟΝΤΟΤΕΡΟ->ΚΟΝΤ
    if not done:
        for suffix in ['ΕΣΤΕΡ', 'ΕΣΤΑΤ', 'ΟΤΕΡ', 'ΟΤΑΤ', 'ΥΤΕΡ', 'ΥΤΑΤ', 'ΩΤΕΡ', 'ΩΤΑΤ']:
            if ends_with(word, suffix):
                word = word[:len(word) - len(suffix)]
                if 'skroutz' in input_list:
                    if word in ['ΕΞ','ΕΣ','ΑΝ','ΚΑΤ','Κ','ΠΡ']: # skroutzstem #unless tis ruby
                        word = word + suffix
                    if word in ['ΚΑ','Μ','ΕΛΕ','ΛΕ','ΔΕ']: # skroutzstem
                        word = word + 'ΥΤ'
                break
           


    return word
    # additions based on Enhancing a Greek Language Stemmer-Efficiency and Accuracy Improvements by Spyridon Saroukos



    


