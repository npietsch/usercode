#
#  SUSY-PAT configuration file
#
#  PAT configuration for the SUSY group - 42X series
#  More information here:
#  https://twiki.cern.ch/twiki/bin/view/CMS/SusyPatLayer1DefV10
#

#Set the SUSY parameters M0 and M12#
####################################
M0 = 360
M12 = 700

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

# Starting with a skeleton process which gets imported with the following line
from PhysicsTools.PatAlgos.patTemplate_cfg import *

#-- Meta data to be logged in DBS ---------------------------------------------
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.1 $'),
    name = cms.untracked.string('$Source: /cvs_server/repositories/CMSSW/UserCode/npietsch/SUSYAnalysis/Configuration/Run2011/SUSYPAT_SUSYMC_cfg.py,v $'),
    annotation = cms.untracked.string('SUSY pattuple definition')
)


#-- Message Logger ------------------------------------------------------------
process.MessageLogger.categories.append('PATSummaryTables')
process.MessageLogger.cerr.PATSummaryTables = cms.untracked.PSet(
    limit = cms.untracked.int32(-1),
    reportEvery = cms.untracked.int32(1)
    )
process.MessageLogger.cerr.FwkReport.reportEvery = 100


#---------------------------------------------------------------------------------
# Load modules to create SUSY Gen Event and TtGenEvent
#
# Note: To create the TtGenEvent for non-SM samples, a small modification in the TQAF is needed:
# - Checkout TopQuarkAnalysis/TopEventProducers  (for CMSSW_4_1_4: cvs co -r V06-07-11 TopQuarkAnalysis/TopEventProducers)
# - replace in the constructor of TopQuarkAnalysis/TopEventProducers/src/TopDecaySubset.cc "kStart" by "kPythia"
#-----------------------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYEventProducers.sequences.SUSYGenEvent_cff")
## process.load("TopQuarkAnalysis.TopEventProducers.sequences.ttGenEvent_cff")

#-----------------------------------------------------------------
# Load modules for preselection
#-----------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.Preselection_cff")

#-----------------------------------------------------------------
# Load modules to create objects and filter events on reco level
#-----------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.BjetsSelection_cff")
process.load("SUSYAnalysis.SUSYFilter.sequences.MuonID_cff")

#----------------------------------------------------------------------------------------
# Load modules for analysis on generator level, level of matched objects and reco-level
#-----------------------------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYAnalyzer.sequences.SUSYBjetsAnalysis_cff")

#-------------------------------------------------
# Load and configure module for event weighting
#-------------------------------------------------

process.load("TopAnalysis.TopUtils.EventWeightPU_cfi")
process.eventWeightPU.DataFile = "TopAnalysis/TopUtils/data/Data_PUDist_160404-163869_7TeV_May10ReReco_Collisions11_v2_and_165088-167913_7TeV_PromptReco_Collisions11.root"

process.load("SUSYAnalysis.SUSYEventProducers.WeightProducer_cfi")


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


## dummy output module
#process.out = cms.OutputModule("PoolOutputModule",
#    outputCommands = cms.untracked.vstring('drop *'),
#    dropMetaData = cms.untracked.string("DROPPED"),                                     
#    fileName = cms.untracked.string('Summer11.root')
#)

#-----------------------------------------------------------------
# From PhysicsTools/Configuration/test/SUSY_pattuple_cfg.py
#-----------------------------------------------------------------

#-- VarParsing ----------------------------------------------------------------
import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing ('standard')

process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
options.maxEvents = -1

#  for SusyPAT configuration
options.register('GlobalTag', 'START42_V13::All', VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string, "GlobalTag to use (if empty default Pat GT is used)")
options.register('mcInfo', True, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.int, "process MonteCarlo data")
options.register('jetCorrections', 'L1FastJet', VarParsing.VarParsing.multiplicity.list, VarParsing.VarParsing.varType.string, "Level of jet corrections to use: Note the factors are read from DB via GlobalTag")
options.jetCorrections.append('L2Relative')
options.jetCorrections.append('L3Absolute')
options.register('hltName', 'HLT', VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string, "HLT menu to use for trigger matching")
options.register('mcVersion', '', VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string, "Currently not needed and supported")
options.register('jetTypes', 'AK5PF', VarParsing.VarParsing.multiplicity.list, VarParsing.VarParsing.varType.string, "Additional jet types that will be produced (AK5Calo and AK5PF, cross cleaned in PF2PAT, are included anyway)")
options.register('hltSelection', '', VarParsing.VarParsing.multiplicity.list, VarParsing.VarParsing.varType.string, "hlTriggers (OR) used to filter events")
options.register('doValidation', False, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.int, "Include the validation histograms from SusyDQM (needs extra tags)")
options.register('doExtensiveMatching', False, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.int, "Matching to simtracks (needs extra tags)")
options.register('doSusyTopProjection', False, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.int, "Apply Susy selection in PF2PAT to obtain lepton cleaned jets (needs validation)")
options.register('addKeep', '', VarParsing.VarParsing.multiplicity.list, VarParsing.VarParsing.varType.string, "Additional keep and drop statements to trim the event content")


process.maxEvents.input = options.maxEvents
# Due to problem in production of LM samples: same event number appears multiple times
process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')

#-- Calibration tag -----------------------------------------------------------
if options.GlobalTag:
    process.GlobalTag.globaltag = options.GlobalTag

############################# START SUSYPAT specifics ####################################
from PhysicsTools.Configuration.SUSY_pattuple_cff import addDefaultSUSYPAT, getSUSY_pattuple_outputCommands
#Apply SUSYPAT
addDefaultSUSYPAT(process,options.mcInfo,options.hltName,options.jetCorrections,options.mcVersion,options.jetTypes,options.doValidation,options.doExtensiveMatching,options.doSusyTopProjection)
SUSY_pattuple_outputCommands = getSUSY_pattuple_outputCommands( process )
############################## END SUSYPAT specifics ####################################

## #-- TFileService --------------------------------------------------------------
## process.load ("PhysicsTools.UtilAlgos.TFileService_cfi")
## process.TFileService = cms.Service("TFileService",
##   fileName = cms.string('histo.root')
## )

#-- HLT selection ------------------------------------------------------------
import HLTrigger.HLTfilters.hltHighLevel_cfi as hlt
if options.hltSelection:
    process.hltFilter = hlt.hltHighLevel.clone(
        HLTPaths = cms.vstring(options.hltSelection),
        TriggerResultsTag = cms.InputTag("TriggerResults","",options.hltName),
        throw = False
    )
    process.susyPatDefaultSequence.replace(process.eventCountProducer, process.eventCountProducer * process.hltFilter)

## Note: L1FastJet propagation is working only with reco jets and can therefore not be applied here 
process.metJESCorAK5PFTypeI.corrector = cms.string('ak5PFL2L3')

#process.p = cms.Path( process.susyPatDefaultSequence )


#-------------------------------------------------
# Create patTuple
#-------------------------------------------------

#Remove the outputModule from the EndPath outpath
process.outpath.remove(process.out)

##process.EventSelection = cms.PSet(
#    SelectEvents = cms.untracked.PSet(
#    SelectEvents = cms.vstring('PATTuple'
#                               )
#    )
#    )
#
##process.out = cms.OutputModule("PoolOutputModule",
#                               process.EventSelection,
#                               outputCommands = cms.untracked.vstring('drop *'),
#                               dropMetaData = cms.untracked.string('DROPPED'),
#                               fileName = cms.untracked.string('Summer11.root')
#                               )
#
## Specify what to keep in the event content
#from PhysicsTools.PatAlgos.patEventContent_cff import *
#process.out.outputCommands += patEventContentNoCleaning
#process.out.outputCommands += patExtraAodEventContent
#process.out.outputCommands += cms.untracked.vstring('keep *_addPileupInfo_*_*')
#process.out.outputCommands += cms.untracked.vstring('keep *_patMETsTypeIPF_*_*')
#process.out.outputCommands += cms.untracked.vstring('keep *_*ElectronsPF_*_*')
#process.out.outputCommands += cms.untracked.vstring('keep *_*MuonsPF_*_*')

#Keep the susy pars in output file
#process.out.outputCommands += cms.untracked.vstring('keep *_susyParamExtract_*_*') 
#Keep the LHEEventProduct, might be required to extract the subprocess
#process.out.outputCommands += cms.untracked.vstring('keep *_source_*_*') 

#from SUSYAnalysis.SUSYEventProducers.SUSYEventContent_cff import *
#process.out.outputCommands += SUSYEventContent
#from TopQuarkAnalysis.TopEventProducers.tqafEventContent_cff import *
#process.out.outputCommands += tqafEventContent

#process.outpath = cms.EndPath(process.out)

#Add modules for getting the susy parameters and adding them to the file
process.maxEvents.input = -1
#process.maxEvents.skipEvents = 1

#Define TFileService
rootOutName = 'SUSYANALYSIS_' + str(M0) + '_' + str(M12) + '.root'
process.TFileService = cms.Service("TFileService",
                                       fileName = cms.string(rootOutName)
                                   )

##############################
#Insert modules into the paths
##############################

#process.p = cms.Path(process.susyParamExtract #extract susyPars
#                     *process.prePatCount
#                     *process.susyParamFilter  #filter susyPars                            
#                     *process.susyPatDefaultSequence##  *
#                     *process.postPatCount
#                     )

#Setup some basic sequences
process.PATTuple = cms.Sequence(process.susyParamExtract*       #extract susyPars
                                process.prePatCount*            #fill a Hist
                                process.susyParamFilter*        #filter susyPars                            
                                process.susyPatDefaultSequence* #produce PAT sequence
                                process.postPatCount
                                )

process.createAllObjects = cms.Sequence(process.PATTuple*
                                        process.makeObjects*
                                        process.makeSUSYGenEvt*
                                        process.eventWeightPU*
                                        process.weightProducer
                                        )

#Remove the HBHENoiseFilter, since hcalnoise not present in SUSY AOD
process.preselectionMC2PAT.remove(process.HBHENoiseFilter)
process.basicMuonSelections = cms.Sequence(process.preselectionMC2PAT*
                                           process.preselectionMuHTMC2*
                                           process.MuHadSelection*
                                           process.muonSelection*
                                           process.jetSelection
                                           )
process.basicElectronSelections = cms.Sequence(process.preselectionMC2PAT*
                                               process.preselectionElHTMC2*
                                               process.ElHadSelection*
                                               process.electronSelection*
                                               process.jetSelection
                                               )


#--------------------------
# muon selection paths
#--------------------------

## no btag
process.Selection1m = cms.Path(process.PATTuple*    
                               process.makeObjects *
                               process.makeSUSYGenEvt *
                               process.eventWeightPU *
                               process.weightProducer *
                               process.analyzeSUSYBjets1m_noCuts * #This is important. Will find the no of subprocs.
                               process.preselectionMC2PAT*
                               process.preselectionMuHTMC2 *
                               process.MuHadSelection *
                               process.analyzeSUSYBjets1m_preselection *
                               process.RA4MuonCollections *
                               process.RA4MuonSelection *
                               process.muonSelection*
                               process.analyzeSUSYBjets1m_leptonSelection *
                               process.jetSelection*
                               process.analyzeSUSYBjets1m_jetSelection *
                               process.HTSelection *
                               process.analyzeSUSYBjets1m_HTSelection *
                               process.metSelection *
                               process.analyzeSUSYBjets1m_metSelection *
                               process.mTSelection *
                               process.analyzeSUSYBjets1m_mTSelection
                               )
## exactly 1 btag
process.Selection1b1m_2 = cms.Path(process.createAllObjects*
                                   process.basicMuonSelections*
                                   process.exactlyOneMediumTrackHighEffBjet *
                                   process.analyzeSUSYBjets1b1m_4 *
                                   process.HTSelection *
                                   process.analyzeSUSYBjets1b1m_5 *
                                   process.metSelection *
                                   process.analyzeSUSYBjets1b1m_6 *
                                   process.mTSelection *
                                   process.analyzeSUSYBjets1b1m_1
                                   )
## exactly 2 btags
process.Selection2b1m_2 = cms.Path(process.createAllObjects*
                                   process.basicMuonSelections*
                                   process.exactlyTwoMediumTrackHighEffBjets *
                                   process.analyzeSUSYBjets2b1m_4 *
                                   process.HTSelection *
                                   process.analyzeSUSYBjets2b1m_5 *
                                   process.metSelection *
                                   process.analyzeSUSYBjets2b1m_6 *
                                   process.mTSelection *
                                   process.analyzeSUSYBjets2b1m_1
                                   )
## at least 3 btags
process.Selection3b1m_1 = cms.Path(process.createAllObjects*
                                   process.basicMuonSelections*
                                   process.threeMediumTrackHighEffBjets *
                                   process.analyzeSUSYBjets3b1m_4 *
                                   process.HTSelection *
                                   process.analyzeSUSYBjets3b1m_5 *
                                   process.metSelection *
                                   process.analyzeSUSYBjets3b1m_6 *
                                   process.mTSelection *
                                   process.analyzeSUSYBjets3b1m_1
                                   )

#--------------------------
# electron selection paths
#--------------------------

## no btag
process.Selection1e = cms.Path(process.PATTuple*
                               process.makeObjects *
                               process.makeSUSYGenEvt *
                               process.eventWeightPU *
                               process.weightProducer *
                               process.analyzeSUSYBjets1e_noCuts * #Also important. But should give the same as 1m!
                               process.preselectionMC2PAT*
                               process.preselectionElHTMC2 *
                               process.ElHadSelection *
                               process.analyzeSUSYBjets1e_preselection *
                               process.electronSelection*
                               process.analyzeSUSYBjets1e_leptonSelection *
                               process.jetSelection*
                               process.analyzeSUSYBjets1e_jetSelection *
                               process.HTSelection *
                               process.analyzeSUSYBjets1e_HTSelection *
                               process.metSelection *
                               process.analyzeSUSYBjets1e_metSelection *
                               process.mTSelection *
                               process.analyzeSUSYBjets1e_mTSelection
                               )

## exactly 1 btag
process.Selection1b1e_2 = cms.Path(process.createAllObjects*
                                   process.basicElectronSelections*
                                   process.exactlyOneMediumTrackHighEffBjet *
                                   process.analyzeSUSYBjets1b1e_4 *
                                   process.HTSelection *
                                   process.analyzeSUSYBjets1b1e_5 *
                                   process.metSelection *
                                   process.analyzeSUSYBjets1b1e_6 *
                                   process.mTSelection *
                                   process.analyzeSUSYBjets1b1e_1
                                   )

## exactly 2 btags
process.Selection2b1e_2 = cms.Path(process.createAllObjects*
                                   process.basicElectronSelections*
                                   process.exactlyTwoMediumTrackHighEffBjets *
                                   process.analyzeSUSYBjets2b1e_4 *
                                   process.HTSelection *
                                   process.analyzeSUSYBjets2b1e_5 *
                                   process.metSelection *
                                   process.analyzeSUSYBjets2b1e_6 *
                                   process.mTSelection *
                                   process.analyzeSUSYBjets2b1e_1
                                   )

## at least 3 btags
process.Selection3b1e_1 = cms.Path(process.createAllObjects*
                                   process.basicElectronSelections*
                                   process.threeMediumTrackHighEffBjets *
                                   process.analyzeSUSYBjets3b1e_4 *
                                   process.HTSelection *
                                   process.analyzeSUSYBjets3b1e_5 *
                                   process.metSelection *
                                   process.analyzeSUSYBjets3b1e_6 *
                                   process.mTSelection *
                                   process.analyzeSUSYBjets3b1e_1
                                   )

#---------------------------------------------
#Load all files for the appropriate SUSY point
#---------------------------------------------

#Only load files if the number of events is 10000
FILEPREFIX='dcap://dcache-cms-dcap.desy.de:22125/pnfs/desy.de/cms/tier2'
fileList = []
fileCat = open('fileCat_SUSYMC.txt')

for line in fileCat:
    line = line.rstrip()
    lineList = line.split(' ')

    #Check to see if point is the one desired
    if not ( (lineList[0] == str(M0)) and (lineList[1] == str(M12)) ):
        continue

    #Check that point has 10000 events
    if ( len(lineList) < 4 ) :
        break
    if ( lineList[2] == '10000' ) :
        for fileName in lineList[3:] :
            fileList.append(fileName[len(FILEPREFIX):])
    break

fileCat.close()

print "Running over files:  "
print fileList

process.source.fileNames = fileList
