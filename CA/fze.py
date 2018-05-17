##CYberAnima

#bot generateur de morceau transe créer a partir de ressource prise sur le net
#ensuite le couplet avec le bot companion (style de musique celon l'humeur)

import sys
import os
import glob
import configparser as ConfigParser#lecture de fichier syntaxique utiliser pour configurer des script
import struct#bibli mani bit
import wave#bibli manip wave

#ParamSong={"bpm":120,"nbpattern":[],"rate":44100}

RessourcePath ="""C:\Users\poste\Archives\Projet\projets en cour\cyberanimisme\CA\samples"""#chemin des banque de sample
OutputPath = "creations"#chemin de sortie des fichier audio créer
samples = {}#list sample utiliser
patterns = {}#list pattern

#ressource=#fichier qui stock les pattern et music déjà existante
#patternBankOk #quand un pattern est approuvé on le stock la dedans pour que le programme s'en inspire
#patternBankNop #""  ""  ""  ""  ""  désapprouvé "" "" "" "" "" "" "" "  " " " " " " " " " " " " " ""

print("   lancement création de morceau")

listDir = glob.glob(RessourcePath)

for file in listDir:

	print(os.path.splitext(file))

#print("je selectionne le sample :")

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



#def rythmValue

#def noteHeight

#def soundManip #speed/length

#def piste

#def score

#def pitch
