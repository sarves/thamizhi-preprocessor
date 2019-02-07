#Developed by Kengatharaiyer Sarveswaran
#sarves@cse.mrt.ac.lk or iamsarves@gmail.com
#Department of Computer Science and Engineering, University of Moratuwa, Sri Lanka
#Licensed under GPLv3 which is outlined here https://www.gnu.org/licenses/gpl-3.0.en.html
#Version 20190206

import re
import os
import subprocess

#Possible starting letter check
def CheckStartingLetter(word):
    uyir=["அ","ஆ","இ","ஈ","உ","ஊ","எ","ஏ","ஐ","ஒ","ஓ","ஔ"] #102
    ka=["க","கா","கி","கீ","கு","கூ","ெக","ேக","ைக","ெகா","கோ","ெகள"] #102
    ca=["ச","சா","சி","சீ","சு","சூ","செ","சே","சை","சொ","சோ","சௌ"] #102
    tha=["த","தா","தி","தீ","து","தூ","தெ","தே","தை","தொ","தோ","தௌ"] #102
    na=["ந","நா","நி","நீ","நு","நூ","நெ","நே","நை","நொ","நோ","நௌ"] #102
    pa=["ப","பா","பி","பீ","பு","பூ","பெ","பே","பை","பொ","போ","பௌ"] #102
    ma=["ம","மா","மி","மீ","மு","மூ","மெ","மே","மை","மொ","மோ","மௌ"] #102
    va=["வ","வா","வி","வீ","வெ","வே","வை","வௌ"] #103
    ya=["ய","யா","யு","யூ","யோ","யௌ"] #104
    gna=["ஞ","ஞா","ஞெ","ஞொ"] #105
 #   ng=["அங்","இங்","உங்","யாங்"] #106
    letters=uyir
    letters[len(letters):]=ka
    letters[len(letters):]=ca
    letters[len(letters):]=tha
    letters[len(letters):]=na
    letters[len(letters):]=pa
    letters[len(letters):]=ma
    letters[len(letters):]=va
    letters[len(letters):]=ya
    letters[len(letters):]=gna
#    letters[len(letters):]=ng
    
    correct_word=0;
    error_code="";
    for x in letters:
        p=re.compile(str(x))
        if p.match(word):
            correct_word=1
    if correct_word==0:
        correct_word="Starting letter is incorrect!"
    return correct_word

def CheckEndingLetter(word):
    uyir_oreluthu_orumozhi=["ஆ","ஈ","ஊ","ஏ","ஐ","ஓ","ஒள"] #107
    uyir_a=["க","ங","ச","ஞ","ட","ண","த","ந","ப","ம","ய","ர","ழ","வ","ள","ல","ற","ன"] #107
    mei=["ஞ்","ண்","ந்","ம்","ன்","ய்","ர்","ல்","வ்","ழ்","ள்"] #நாவலர் இலக்கண விளக்கம் 24
    uyir_rest=["ா","ி","ீ","ு","ூ","ே","ை","ொ","ோ","ௌ"] #107?? நாவலர் இலக்கண விளக்கம்

    letters=uyir_a
    letters[len(letters):]=uyir_rest
    letters[len(letters):]=mei

    correct_word=0;
    error_code="";
    if len(word)==1:
        for x in uyir_oreluthu_orumozhi: #Oreluthu orumozhi check
            if x==word:
                correct_word=1
                break
    else:
        for x in letters: #if it is not oreluthu orumozhi
            p=re.compile(x+"$")
            if p.search(word):
                correct_word=1
    if correct_word==0:
        correct_word="Ending letter is incorrect! Uyiralapedai is not considered here."
    return correct_word



def CheckMeimmayakkam(word):
    #110 - 120
    #121 - is yet to be added. example words: வகரம், லகரம், யகரம்...
    set1=["ங்ச","ங்ஞ","ங்ட","ங்ண","ங்த","ங்ந","ங்ப","ங்ம","ங்ய","ங்ர","ங்ள","ங்வ","ங்ழ","ங்ல","ங்ற","ங்ன"] #invalid combinations for ங்
    set2=["ங்ச்","ங்ஞ்","ங்ட்","ங்ண்","ங்த்","ங்ந்","ங்ப்","ங்ம்","ங்ய்","ங்ர்","ங்ள்","ங்வ்","ங்ழ்","ங்ல்","ங்ற்","ங்ன்"]
    
    set3=["வ்க","வ்ங","வ்ச","வ்ஞ","வ்ட","வ்ண","வ்த","வ்ந","வ்ப","வ்ம","வ்ர","வ்ள","வ்ழ","வ்ல","வ்ற","வ்ன"] #invalid combinations for வ்
    set4=["வ்க்","வ்ங்","வ்ச்","வ்ஞ்","வ்ட்","வ்ண்","வ்த்","வ்ந்","வ்ப்","வ்ம்","வ்ர்","வ்ள்","வ்ழ்","வ்ல்","வ்ற்","வ்ன்"]

    set5=["ஞ்க","ஞ்ங","ஞ்ட","ஞ்ண","ஞ்த","ஞ்ந","ஞ்ப","ஞ்ம","ஞ்ர","ஞ்ள","ஞ்வ","ஞ்ழ","ஞ்ல","ஞ்ற","ஞ்ன"] #Invalid combinations for ஞ்
    set6=["ஞ்க்","ஞ்ங்","ஞ்ட்","ஞ்ண்","ஞ்த்","ஞ்ந்","ஞ்ப்","ஞ்ம்","ஞ்ர்","ஞ்ள்","ஞ்வ்","ஞ்ழ்","ஞ்ல்","ஞ்ற்","ஞ்ன"]

    set7=["ந்க","ந்ங","ந்ச","ந்ஞ","ந்ட","ந்ண","ந்ப","ந்ம","ந்ர","ந்ள","ந்வ","ந்ழ","ந்ல","ந்ற","ந்ன"] #Invalid combinations for ந்
    set8=["ந்க்","ந்ங்","ந்ச்","ந்ஞ்","ந்ட்","ந்ண்","ந்த்","ந்ந்","ந்ப்","ந்ம்","ந்ய்","ந்ர்","ந்ள்","ந்வ்","ந்ழ்","ந்ல்","ந்ற்","ந்ன்"]

    set9=["ட்ங","ட்ஞ","ட்ண","ட்த","ட்ந","ட்ம","ட்ய","ட்ர","ட்ள","ட்வ","ட்ழ","ட்ல","ட்ற","ட்ன"] #Invalid combinations for ட்
    set10=["ட்ங்","ட்ஞ்","ட்ண்","ட்த்","ட்ந்","ட்ம்","ட்ய்","ட்ர்","ட்ள்","ட்வ்","ட்ழ்","ட்ல்","ட்ற்","ட்ன்"]

    set11=["ற்ங","ற்ஞ","ற்ட","ற்ண","ற்த","ற்ந","ற்ம","ற்ய","ற்ர","ற்ள","ற்வ","ற்ழ","ற்ல","ற்ன"] #Invalid combinations for ற்்
    set12=["ற்ங்","ற்ஞ்","ற்ட்","ற்ண்","ற்த்","ற்ந்","ற்ம்","ற்ய்","ற்ர்","ற்ள்","ற்வ்","ற்ழ்","ற்ல்","ற்ன்"]

    set13=["ண்ங","ண்த","ண்ந","ண்ர","ண்ள","ண்ழ","ண்ல","ண்ற","ண்ன"]#Invalid combinations for ண்
    set14=["ண்ங்","ண்த்","ண்ந்","ண்ர்","ண்ள்","ண்ழ்","ண்ல்","ண்ற்","ண்ன்"] 

    set15=["ன்ங","ன்ட","ன்ண","ன்த","ன்ந","ன்ர","ன்ள","ன்ழ","ன்ல"]  #Invalid combinations for ன்
    set16=["ன்ங்","ன்ட்","ன்ண்","ன்த்","ன்ந்","ன்ர்","ன்ள்","ன்ழ்","ன்ல்"]

    set17=["ம்க","ம்ங","ம்ச","ம்ஞ","ம்ட","ம்ண","ம்த","ம்ந","ம்ர","ம்ள","ம்ழ","ம்ல","ம்ற","ம்ன"] #Invalid combinations for ம்
    set18=["ம்க்","ம்ங்","ம்ச்","ம்ஞ்","ம்ட்","ம்ண்","ம்த்","ம்ந்","ம்ர்","ம்ள்","ம்ழ்","ம்ல்","ம்ற்","ம்ன்"]

    set19=["ய்ட","ய்ண","ய்ர","ய்ள","ய்ழ","ய்ல","ய்ற","ய்ன"]#Invalid combinations for ய்
    set20=["ய்ட்","ய்ண்","ய்ர்","ய்ள்","ய்ழ்","ய்ல்","ய்ற்","ய்ன்"]

    set21=["ல்ங","ல்ஞ","ல்ட","ல்ண","ல்த","ல்ந","ல்ம","ல்ர","ல்ள","ல்ழ","ல்ற","ல்ன"]#Invalid combinations for ல்
    set22=["ல்ங்","ல்ஞ்","ல்ட்","ல்ண்","ல்த்","ல்ந்","ல்ம்","ல்ர்","ல்ள்","ல்ழ்","ல்ற்","ல்ன்"]

    set23=["ள்ங","ள்ஞ","ள்ட","ள்ண","ள்த","ள்ந","ள்ம","ள்ர","ள்ழ","ள்ல","ள்ற","ள்ன"]#Invalid combinations for ள்
    set24=["ள்ங்","ள்ஞ்","ள்ட்","ள்ண்","ள்த்","ள்ந்","ள்ம்","ள்ர்","ள்ழ்","ள்ல்","ள்ற்","ள்ன்"]

    set25=["க்ங","க்ச","க்ஞ","க்ட","க்ண","க்த","க்ந","க்ப","க்ம","க்ய","க்ர","க்ள","க்வ","க்ழ","க்ல","க்ற","க்ன"]#Invalid combinations for க்
    set26=["க்ங்","க்ச்","க்ஞ்","க்ட்","க்ண்","க்த்","க்ந்","க்ப்","க்ம்","க்ய்","க்ர்","க்ள்","க்வ்","க்ழ்","க்ல்","க்ற்","க்ன்"]

    set27=["ச்க","ச்ங","ச்ஞ","ச்ட","ச்ண","ச்த","ச்ந","ச்ப","ச்ம","ச்ய","ச்ர","ச்ள","ச்வ","ச்ழ","ச்ல","ச்ற","ச்ன"] #Invalid combinations for ச்
    set28=["ச்க்","ச்ங்","ச்ஞ்","ச்ட்","ச்ண்","ச்த்","ச்ந்","ச்ப்","ச்ம்","ச்ய்","ச்ர்","ச்ள்","ச்வ்","ச்ழ்","ச்ல்","ச்ற்","ச்ன்"]    

    set29=["த்க","த்ங","த்ச","த்ஞ","த்ட","த்ண","த்ந","த்ப","த்ம","த்ய","த்ர","த்ள","த்வ","த்ழ","த்ல","த்ற","த்ன"] #Invalid combinations for த்
    set30=["த்க்","த்ங்","த்ச்","த்ஞ்","த்ட்","த்ண்","த்ந்","த்ப்","த்ம்","த்ய்","த்ர்","த்ள்","த்வ்","த்ழ்","த்ல்","த்ற்","த்ன்"]

    set31=["ப்க","ப்ங","ப்ச","ப்ஞ","ப்ட","ப்ண","ப்த","ப்ந","ப்ம","ப்ய","ப்ர","ப்ள","ப்வ","ப்ழ","ப்ல","ப்ற","ப்ன"] #Invalid combinations for ப்
    set32=["ப்க்","ப்ங்","ப்ச்","ப்ஞ்","ப்ட்","ப்ண்","ப்த்","ப்ந்","ப்ம்","ப்ய்","ப்ர்","ப்ள்","ப்வ்","ப்ழ்","ப்ல்","ப்ற்","ப்ன்"]

    set33=["ர்ர"] #Invalid combinations for ர்
    set34=["ர்ர்"]

    set35=["ழ்ழ"] #Invalid combinations for ழ்
    set36=["ழ்ழ்"]

    letters=set1
    letters[len(letters):]=set2  #Lists are merged separatly purposly
    letters[len(letters):]=set3
    letters[len(letters):]=set4
    letters[len(letters):]=set5
    letters[len(letters):]=set6
    letters[len(letters):]=set7
    letters[len(letters):]=set8
    letters[len(letters):]=set9
    letters[len(letters):]=set10
    letters[len(letters):]=set11
    letters[len(letters):]=set12
    letters[len(letters):]=set13
    letters[len(letters):]=set14
    letters[len(letters):]=set15
    letters[len(letters):]=set16
    letters[len(letters):]=set17
    letters[len(letters):]=set18
    letters[len(letters):]=set19
    letters[len(letters):]=set20
    letters[len(letters):]=set21
    letters[len(letters):]=set22
    letters[len(letters):]=set23
    letters[len(letters):]=set24
    letters[len(letters):]=set25
    letters[len(letters):]=set26
    letters[len(letters):]=set27
    letters[len(letters):]=set28
    letters[len(letters):]=set29
    letters[len(letters):]=set30
    letters[len(letters):]=set31
    letters[len(letters):]=set32
    letters[len(letters):]=set33
    letters[len(letters):]=set34
    letters[len(letters):]=set35
    letters[len(letters):]=set36
    correct_word=0
    for x in letters: 
        p=re.compile(x)
        if p.search(word):
            correct_word=1
            break
    if correct_word==1:
        correct_word="Wrong Meimmayakkam!"
    return correct_word

def CheckOreluthuOrumozhi(word):
    found=0
    #129  42 one letter words are declared in nannool
    letters=["ஆ","ஈ","ஊ","ஏ","ஐ","ஓ","மா","மீ","மூ","மே","மை","மோ","தா","தீ","தூ","தே","தை","பா","பூ","பே","பை","போ","நா","நீ","நே","நை","நோ","கா","கூ","கை","கோ","வா","வீ","வை","வௌ","சா","சீ","சே","சோ","யா","நொ","து"]
    for x in letters: 
        if word==x:
            found=1
    return found


def TamilNormalizer(word) :
	#print (word)
	confusion_set={'ோ':'ோ','ொ':'ொ','ா்':'ர்','ெள':'ௌ'} #Invalid code sequences
	for key, value in confusion_set.items():
		word=word.replace(key,value)
	return word

def SandhiRemover(word) :
	word=word.strip() #this is to strip off extra while spaces
	#print (word)
	sandhi_letters={'க்','த்','ப்','ச்'} 
	for x in sandhi_letters: #if it is not oreluthu orumozhi
            		p=re.compile(x+"$")
            		if p.search(word):
                	   word=word[:-2] #remove last two letters / code points
	return word


def ValidateTamilWord(word):
	if CheckOreluthuOrumozhi(word)==1:
		return "A valid Oreluthu orumozhi"
	else:
		if CheckStartingLetter(word)==1:
			if CheckEndingLetter(word)==1:
				if CheckMeimmayakkam(word)==0:
					return 1
				else :
					return "Invalid Meimmayakkam"
			else:
				return "Invalid ending letter"
		else :
			return "Invalid starting letter"



#Todo:
#doesnt valid two letter words like தௌ


