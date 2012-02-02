#At the moment should import from AnalyzeSystematics_cfg
#A script copies the AnalyzeSystematics_cfg and renames it SUSYPAT_MODELSCAN_cfg
from SUSYPAT_MODELSCAN_cfg import *

#Set the SUSY parameters M0 and M12#
####################################
M0 = 380
M12 = 220

#Use command line
import sys
for iArg in sys.argv:
    if (len(iArg) > 3):
        if (iArg[0:3]=='M0='):
            M0 = int(iArg[3:])
        elif (iArg[:4]=='M12='):
            M12 = int(iArg[4:])

print "Using SUSY M0: " + str(M0)
print "Using SUSY M12: " + str(M12)
####################################


#-----------------------------------------
#Load modules required to access the SUSY parameters and filter on them
#-----------------------------------------

#Add module to get the susyPars
process.load('SUSYAnalysis.ScanAnalyzer.susyParamExtract_cfi')
process.susyParamExtract.debug = False

#Add module to filter the susyPars
process.load('SUSYAnalysis.ScanAnalyzer.susyParamFilter_cfi')
process.susyParamFilter.m0 = M0
process.susyParamFilter.m12 = M12
process.susyParamFilter.paramSrc = "susyParamExtract"
process.susyParamFilter.debug = False

#Add module for counting points in m12 vs m0 plane
from SUSYAnalysis.ScanAnalyzer.pointcount_cfi import *
process.prePatCount = pointCounter.clone(paramSrc = "susyParamExtract")
process.postPatCount = pointCounter.clone(paramSrc = "susyParamExtract")

process.maxEvents.input = -1

#Define TFileService
rootOutName = 'SUSYANALYSIS_' + str(M0) + '_' + str(M12) + '.root'
process.TFileService = cms.Service("TFileService",
                                       fileName = cms.string(rootOutName)
                                   )


##############################
#Insert modules into the paths
##############################

#Use this if doing combined PAT-tuple - analysis
#print "MODE: Creating pat-tuples..... "
#process.PATTuple.replace(process.susyPatDefaultSequence,
#                         process.susyParamExtract*       #extract susyPars
#                         process.prePatCount*            #fill a Hist
#                         process.susyParamFilter*        #filter susyPars                            
#                         process.susyPatDefaultSequence* #produce PAT sequence
#                         process.postPatCount
#                         )


#Use this if just running analysis of pat-tuples
print "MODE: Running over pat-tuples..... "

#Create a set of analysers to perform pre-cut checks
#Needed to obtain the total number of each subproc
process.analyzeSystematicsNoCuts0b = process.analyzeSystematicsMu0b.clone()
process.analyzeSystematicsNoCuts1b = process.analyzeSystematicsMu1b.clone()
process.analyzeSystematicsNoCuts2b = process.analyzeSystematicsMu2b.clone()
process.analyzeSystematicsNoCuts3b = process.analyzeSystematicsMu3b.clone()

process.RA4bMuonSelection.replace(process.btagEventWeightMu,
                                  process.btagEventWeightMu *
                                  process.analyzeSystematicsNoCuts0b *
                                  process.analyzeSystematicsNoCuts1b *
                                  process.analyzeSystematicsNoCuts2b *
                                  process.analyzeSystematicsNoCuts3b
                                  )

#Insert the filter in the makeSUSYGenEvt, since this is always present in each path
process.globalReplace(process.makeSUSYGenEvt,
                      process.susyParamExtract*       #extract susyPars
                      process.prePatCount*            #fill a Hist
                      process.susyParamFilter*        #filter susyPars                            
                      process.postPatCount*
                      process.makeSUSYGenEvt
                      )

#---------------------------------------------
#Load all files for the appropriate SUSY point
#---------------------------------------------

#Only load files if the number of events is 10000
FILEPREFIX='dcap://dcache-cms-dcap.desy.de:22125/pnfs/desy.de/cms/tier2'
fileList = []
fileCat = open('fileCat.txt', 'r')

for line in fileCat:
    line = line.rstrip()
    lineList = line.split(' ')

    #Check to see if point is the one desired
    if not ( (int(lineList[0]) == M0 ) and ( int(lineList[1]) == M12 ) ):
        continue

    #If there are no files listed in the catalogue, quit
    if ( len(lineList) < 4 ) :
        break

    #Check that point has (almost) 10000 events
    numEvents = int(lineList[2])
    if ( numEvents <  11000 and numEvents > 9000 ) :
        for fileName in lineList[3:] :
            fileList.append(fileName[len(FILEPREFIX):])
    break

fileCat.close()

print "Running over files:  "
print fileList

process.source.fileNames = fileList
