from SUSYPAT_MODELSCAN_cfg import *

#Set the SMS parameters XINT, MGLUINO, MLSP#
####################################
MGLUINO = 700
MLSP = 100

#Use command line
import sys
for iArg in sys.argv:
    if (len(iArg) > 3):
        if (iArg[0:3]=='MG='):
            MGLUINO = int(iArg[3:])
        elif (iArg[:3]=='ML='):
            MLSP = int(iArg[3:])

print "Using SMS MGLUINO: " + str(MGLUINO)
print "Using SMS MLSP: " + str(MLSP)
####################################


#-----------------------------------------
#Load modules required to access the SMS parameters and filter on them
#-----------------------------------------

process.load('SUSYAnalysis.ScanAnalyzer.sms2ParamExtract_cfi')
process.sms2ParamExtract.debug = False

process.load('SUSYAnalysis.ScanAnalyzer.sms2ParamFilter_cfi')
process.sms2ParamFilter.mGluino  = float(MGLUINO)
process.sms2ParamFilter.mLSP     = float(MLSP)
process.sms2ParamFilter.paramSrc = "sms2ParamExtract"
process.sms2ParamFilter.debug    = False

process.maxEvents.input = -1

#Define TFileService
rootOutName = 'SMSANALYSIS_' + str(MGLUINO) + '_' + str(MLSP) + '.root'

process.TFileService = cms.Service("TFileService",
                                       fileName = cms.string(rootOutName)
                                   )

##############################
#Insert modules into the paths
##############################

process.PATTuple.replace(process.susyPatDefaultSequence,
                         process.sms2ParamExtract*       #extract susyPars
                         process.sms2ParamFilter*        #filter susyPars                            
                         process.susyPatDefaultSequence #produce PAT sequence
                         )


#---------------------------------------------
#Load all files for the appropriate SMS point
#---------------------------------------------

fileList = []
fileCat = open('fileCat.txt', 'r')

for line in fileCat :
    line = line.rstrip()
    lineList = line.split(' ')

    #Check to see if point is the one desired
    if ( (int(lineList[1]) != MGLUINO) or (int(lineList[2]) != MLSP) ):
        continue

    #Check that point has 10000 events
    if ( len(lineList) < 5 ) :
        break #break since point is found, but there are no files
    #if ( lineList[2] == '10000' ) :

    for fileName in lineList[4:] :
        fileList.append(fileName)

    #If here, point was found, so breal
    break

fileCat.close()

print "Running over files:  "
print fileList

process.source.fileNames = fileList