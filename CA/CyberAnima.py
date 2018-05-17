##CYberAnima

#bot generateur de morceau transe créer a partir de ressource prise sur le net
#ensuite le couplet avec le bot companion (style de musique celon l'humeur)

import sys
import os
import glob
import configparser as ConfigParser#lecture de fichier syntaxique utiliser pour configurer des script
import struct#bibli mani bit
import wave#bibli manip wave
import random
#import numpy as np#manipulation de tableau de donnée utile pour modifier le son (a voir plus tard )

ParamSong={"bpm":120,"nbpattern":[],"rate":44100}
FramesperBeat = (ParamSong["rate"]*60)/ParamSong["bpm"]

RessourcePath ="I:\\cyberanimisme\\CA\\samples"#chemin des banque de sample
outputfile = "creations2.wav"#chemin de sortie des fichier audio créer
samples = {}#list sample utiliser
patterns = {}#list pattern

#ressource=#fichier qui stock les pattern et music déjà existante
#patternBankOk #quand un pattern est approuvé on le stock la dedans pour que le programme s'en inspire
#patternBankNop #""  ""  ""  ""  ""  désapprouvé "" "" "" "" "" "" "" "  " " " " " " " " " " " " " ""


print("   lancement création de morceau")

listDir = os.listdir(RessourcePath)#recupere la liste des son ressources


choosenOne=random.choice(listDir) #on choisi un sample aux hasard dans ceux proposé
choosenTwo=random.choice(listDir)

print("je choisis ce sample : "+choosenOne)
print("et celui ci : "+choosenTwo)

sample = wave.open(os.path.join(RessourcePath, choosenOne), "r")
sample2 = wave.open(os.path.join(RessourcePath, choosenTwo), "r")

nbframes = sample.getnframes()#recupere le nmbre de frame du son
nbframesii = sample2.getnframes()#recupere le nmbre de frame du son
print(sample.getparams())
print("%dh"%nbframes)

print(sample2.getparams())
print("%dh"%nbframesii)

bi="%dh"%(nbframes*sample.getparams()[0])#on multipli le nombre de frames (= au nb de bytes) par le nombre de channel
bii="%dh"%(nbframesii*sample2.getparams()[0])

echant = struct.unpack(bi, sample.readframes(nbframes))#on echantillonne en bit le sample
echant2 = struct.unpack(bii, sample2.readframes(nbframesii))

sample.close()
sample2.close()

print( "ce sample dure " + str(nbframes) +" frames. Il y a "+str(int(FramesperBeat)) +" frames par battement")
print( "ce sample dure " + str(nbframesii) +" frames. Il y a "+str(int(FramesperBeat)) +" frames par battement")

i=0
time=0
track=[]


def add_sample(timecode,sampleadd):
        global track

        if len(track) < (timecode + len(sampleadd)):#si il ya eu des silence entre le sample precedent et celuici...
        	#print((timecode + len(sampleadd)) - len(track))
        	track += [0] * (int(timecode + len(sampleadd)) - len(track))
        for i in range(len(sampleadd)):

        	#print(str(i)+" "+str(timecode))

        	track[int(timecode) + i] += sampleadd[i]##pour chaque frames du sample on ajoute chaque frame dans le bon ordre
        	#on a juste a ajouté au même time code les bytes de chaque son pour les jouer en meme temps




while i<8:

	print("sa roule")
	add_sample(time,echant)
	add_sample(time/2,echant2)
	time+=FramesperBeat
	i+=1

trackstr=b"".join(([struct.pack("h", min(32767, max(v, -32768))) for v in track]))

output = wave.open(outputfile, "w")#on creer une instance d'un fichier wave

output.setparams((1, 2,ParamSong["rate"], 0, "NONE", "not compressed"))#on configure le fichier
output.writeframes(trackstr)#on ecrit les bit du fichier

output.close()#on le ferme

print("Musique crée !!!")

##on genre un son de 8 battement, a chaque battement on met le sample
#def generateSong():


#def beat

#def apprentissage

#def basse

#def melody

#def patternorder/structure

#def harmony

#def rules

#save song

#def evolution generation / mix

#def pattern

#def cover generator


#sample to signal

#cutomatic

#def rythmValue

#def noteHeight

#def soundManip #speed/length

#def piste

#def score

#def pitch
