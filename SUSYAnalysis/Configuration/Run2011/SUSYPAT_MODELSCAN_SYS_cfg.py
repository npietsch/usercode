#
#  SUSY-PAT configuration file
#
#  PAT configuration for the SUSY group - 42X series
#  More information here:
#  https://twiki.cern.ch/twiki/bin/view/CMS/SusyPatLayer1DefV10
#

# Starting with a skeleton process which gets imported with the following line



from PhysicsTools.PatAlgos.patTemplate_cfg import *

#-- Meta data to be logged in DBS ---------------------------------------------
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.1 $'),
    name = cms.untracked.string('$Source: /cvs_server/repositories/CMSSW/UserCode/npietsch/SUSYAnalysis/Configuration/Run2011/SUSYPAT_MODELSCAN_SYS_cfg.py,v $'),
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
# process.load("TopQuarkAnalysis.TopEventProducers.sequences.ttGenEvent_cff")

#-----------------------------------------------------------------
# Load modules for preselection
#-----------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.Preselection_cff")


#-----------------------------------------------------------------
# Load modules to create objects and filter events on reco level
#-----------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.Systematics_cff")

#process.load("SUSYAnalysis.SUSYFilter.sequences.BjetsSelection_cff")
#process.load("SUSYAnalysis.SUSYFilter.sequences.MuonID_cff")

#-----------------------------------------------------------------
# Load and configure module for to scale jet energy
#-----------------------------------------------------------------

process.load("SUSYAnalysis.Uncertainties.JetEnergy_cfi")

## define default settings
process.scaledJetEnergy.inputJets = "selectedPatJetsAK5PF"
process.scaledJetEnergy.inputMETs = "patMETsPF"

process.scaledJetEnergy.resolutionEtaRanges  = cms.vdouble(0, 1.5, 1.5, 2.0, 2.0, -1)
process.scaledJetEnergy.resolutionFactors    = cms.vdouble(1.1, 1.1, 1.1)

process.scaledJetEnergy.jetPTThresholdForMET = 10. ## proposed on Nov 15 in RA4 meeting

## create collections of selectedPatJetsAK5PF and patMETsPF with scaled up jet energy corrections
process.scaledJetEnergyJECUp = process.scaledJetEnergy.clone()
process.scaledJetEnergyJECUp.scaleType   = "jes:up"

## create collections of selectedPatJetsAK5PF and patMETsPF with scaled down jet energy resolution
process.scaledJetEnergyJECDown = process.scaledJetEnergy.clone()
process.scaledJetEnergyJECDown.scaleType   = "jes:down"

## create collections of selectedPatJetsAK5PF and patMETsPF with scaled up jet energy corrections
process.scaledJetEnergyJERUp = process.scaledJetEnergy.clone()
process.scaledJetEnergyJERUp.resolutionFactors    = cms.vdouble(1.2, 1.25, 1.3)

## create collections of selectedPatJetsAK5PF and patMETsPF with scaled down jet energy corrections
process.scaledJetEnergyJERDown = process.scaledJetEnergy.clone()
process.scaledJetEnergyJERDown.resolutionFactors    = cms.vdouble(1., 0.95, 0.9)

#-----------------------------------------------------------------------------------------
# Load modules for analysis on generator level, level of matched objects and reco level
#-----------------------------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYAnalyzer.sequences.SystematicsAnalyzerMu_cff")
process.load("SUSYAnalysis.SUSYAnalyzer.sequences.SystematicsAnalyzerEl_cff")

#----------------------------------------------------------------------------------------
# Load modules for analysis on generator level, level of matched objects and reco-level
#-----------------------------------------------------------------------------------------

#process.load("SUSYAnalysis.SUSYAnalyzer.sequences.SUSYBjetsAnalysis_cff")

#-------------------------------------------------
# Load and configure module for event weighting
#-------------------------------------------------

process.load("TopAnalysis.TopUtils.EventWeightPU_cfi")
process.load("SUSYAnalysis.SUSYEventProducers.WeightProducer_cfi")
#process.eventWeightPU.DataFile = "TopAnalysis/TopUtils/data/Data_PUDist_160404-163869_7TeV_May10ReReco_Collisions11_v2_and_165088-167913_7TeV_PromptReco_Collisions11.root"
process.eventWeightPU.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_TTJets_TuneZ2_7TeV_madgraph_tauola.root"


#------------------------------------------------------------
# load and configure modules for b-tag efficiency weighting
#------------------------------------------------------------

process.load ("RecoBTag.PerformanceDB.PoolBTagPerformanceDB1107")
process.load ("RecoBTag.PerformanceDB.BTagPerformanceDB1107")
process.load("Btagging.BtagWeightProducer.BtagEventWeight_cfi")

## define default settings
process.btagEventWeight.bTagAlgo= "TCHEM"

## create weights for muon selection
process.btagEventWeightMu                    = process.btagEventWeight.clone()
process.btagEventWeightMu.filename           = "../../../SUSYAnalysis/SUSYUtils/data/BtagEff_TTJets.root"
process.btagEventWeightMu.rootDir            = "RA4bMuTCHEM3"

process.btagEventWeightMuBtagSFUp            = process.btagEventWeightMu.clone()
process.btagEventWeightMuBtagSFUp.sysVar     = "bTagSFUp"

process.btagEventWeightMuBtagSFDown          = process.btagEventWeightMu.clone()
process.btagEventWeightMuBtagSFDown.sysVar   = "bTagSFDown"

process.btagEventWeightMuMistagSFUp          = process.btagEventWeightMu.clone()
process.btagEventWeightMuBtagSFUp.sysVar     = "MisTagSFUp"

process.btagEventWeightMuMistagSFDown        = process.btagEventWeightMu.clone()
process.btagEventWeightMuMistagSFDown.sysVar = "MisTagSFDown"

## create weights for electron selection
process.btagEventWeightEl                    = process.btagEventWeight.clone()
process.btagEventWeightEl.filename           = "../../../SUSYAnalysis/SUSYUtils/data/BtagEff_TTJets.root"
process.btagEventWeightEl.rootDir            = "RA4bElTCHEM3"

process.btagEventWeightElBtagSFUp            = process.btagEventWeightEl.clone()
process.btagEventWeightElBtagSFUp.sysVar     = "bTagSFUp"

process.btagEventWeightElBtagSFDown          = process.btagEventWeightEl.clone()
process.btagEventWeightElBtagSFDown.sysVar   = "bTagSFDown"

process.btagEventWeightElMistagSFUp          = process.btagEventWeightEl.clone()
process.btagEventWeightElBtagSFUp.sysVar     = "MisTagSFUp"

process.btagEventWeightElMistagSFDown        = process.btagEventWeightEl.clone()
process.btagEventWeightElMistagSFDown.sysVar = "MisTagSFDown"



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
process.PATTuple = cms.Sequence(process.susyPatDefaultSequence #produce PAT sequence
                                )

process.createAllObjects = cms.Sequence(process.PATTuple*
                                        process.scaledJetEnergy *
                                        process.scaledJetEnergyJECUp *
                                        process.scaledJetEnergyJECDown *
                                        process.scaledJetEnergyJERUp *
                                        process.scaledJetEnergyJERDown *
                                        process.createGoodObjects *
                                        process.makeSUSYGenEvt *
                                        process.eventWeightPU *
                                        process.weightProducer 
                                        )

#Remove the HBHENoiseFilter, since hcalnoise not present in SUSY AOD
process.preselectionMC2PAT.remove(process.HBHENoiseFilter)

#process.basicMuonSelections = cms.Sequence(process.preselectionMC2PAT*
#                                           process.preselectionMuHTMC2*
#                                           process.MuHadSelection*
#                                           process.muonSelection*
#                                           process.jetSelection
#                                           )
#process.basicElectronSelections = cms.Sequence(process.preselectionMC2PAT*
#                                               process.preselectionElHTMC2*
#                                               process.ElHadSelection*
#                                               process.electronSelection*
#                                               process.jetSelection
#                                               )
  

#-------------------------
# Muon selection paths
#--------------------------

## muon selection w/o scaled jet energy
process.RA4bMuonSelection = cms.Path(## Producer sequences
                                     process.createAllObjects *
                                     process.btagEventWeightMu *
                                     process.btagEventWeightMuBtagSFUp *
                                     process.btagEventWeightMuBtagSFDown *
                                     process.btagEventWeightMuMistagSFUp *
                                     process.btagEventWeightMuMistagSFDown *
                                     ## Selection sequences
                                     process.preselectionMC2PAT*
                                     process.preselectionMuHTMC2 *
                                     process.MuHadSelection *
                                     process.muonSelection*
                                     process.jetSelection *
                                     ## Analyzer Sequences for Mu 0 btags
                                     process.analyzeSystematicsMu0b *
                                     process.analyzeSystematicsMu0bMETUp *
                                     process.analyzeSystematicsMu0bMETDown *
                                     process.analyzeSystematicsMu0bBtagSFUp *
                                     process.analyzeSystematicsMu0bBtagSFDown *
                                     process.analyzeSystematicsMu0bMistagSFUp *
                                     process.analyzeSystematicsMu0bMistagSFDown *
                                     process.analyzeSystematicsMu0bPUUp *
                                     process.analyzeSystematicsMu0bPUDown *
                                     ## Analyzer Sequences for Mu 1 btags
                                     process.analyzeSystematicsMu1b *
                                     process.analyzeSystematicsMu1bMETUp *
                                     process.analyzeSystematicsMu1bMETDown *
                                     process.analyzeSystematicsMu1bBtagSFUp *
                                     process.analyzeSystematicsMu1bBtagSFDown *
                                     process.analyzeSystematicsMu1bMistagSFUp *
                                     process.analyzeSystematicsMu1bMistagSFDown *
                                     process.analyzeSystematicsMu1bPUUp *
                                     process.analyzeSystematicsMu1bPUDown *
                                     ## Analyzer Sequences for Mu 2 btags
                                     process.analyzeSystematicsMu2b *
                                     process.analyzeSystematicsMu2bMETUp *
                                     process.analyzeSystematicsMu2bMETDown *
                                     process.analyzeSystematicsMu2bBtagSFUp *
                                     process.analyzeSystematicsMu2bBtagSFDown *
                                     process.analyzeSystematicsMu2bMistagSFUp *
                                     process.analyzeSystematicsMu2bMistagSFDown *
                                     process.analyzeSystematicsMu2bPUUp *
                                     process.analyzeSystematicsMu2bPUDown *
                                     ## Analyzer Sequences for Mu 3 btags
                                     process.analyzeSystematicsMu3b *
                                     process.analyzeSystematicsMu3bMETUp *
                                     process.analyzeSystematicsMu3bMETDown *
                                     process.analyzeSystematicsMu3bBtagSFUp *
                                     process.analyzeSystematicsMu3bBtagSFDown *
                                     process.analyzeSystematicsMu3bMistagSFUp *
                                     process.analyzeSystematicsMu3bMistagSFDown *
                                     process.analyzeSystematicsMu3bPUUp *
                                     process.analyzeSystematicsMu3bPUDown
                                     )

##  muon selection w/o with scaled up jet energy corrections
process.RA4bMuonSelectionJECUp = cms.Path(## Producer sequences
                                          process.createAllObjects *
                                          process.btagEventWeightMu *
                                          ## Selection sequences
                                          process.preselectionMC2PAT*
                                          process.preselectionMuHTMC2 *
                                          process.MuHadSelectionJECUp *
                                          process.muonSelection*
                                          process.jetSelectionJECUp*
                                          ## Analyzer Sequence
                                          process.analyzeSystematicsMu0bJECUp *
                                          process.analyzeSystematicsMu1bJECUp *
                                          process.analyzeSystematicsMu2bJECUp *
                                          process.analyzeSystematicsMu3bJECUp
                                          )

##  muon selection w/o with scaled down jet energy corrections
process.RA4bMuonSelectionJECDown = cms.Path(## Producer sequences
                                            process.createAllObjects *
                                            process.btagEventWeightMu *
                                            ## Selection sequences
                                            process.preselectionMC2PAT *
                                            process.preselectionMuHTMC2 *
                                            process.MuHadSelectionJECDown *
                                            process.muonSelection*
                                            process.jetSelectionJECDown*
                                            ## Analyzer Sequence
                                            process.analyzeSystematicsMu0bJECDown *
                                            process.analyzeSystematicsMu1bJECDown *
                                            process.analyzeSystematicsMu2bJECDown *
                                            process.analyzeSystematicsMu3bJECDown
                                            )

##  muon selection w/o with scaled up jet energy resolution
process.RA4bMuonSelectionJERUp = cms.Path(## Producer sequences
                                          process.createAllObjects * 
                                          process.btagEventWeightMu *
                                          ## Selection sequences
                                          process.preselectionMC2PAT* 
                                          process.preselectionMuHTMC2 *
                                          process.MuHadSelectionJERUp *
                                          process.muonSelection*
                                          process.jetSelectionJERUp*
                                          ## Analyzer Sequence
                                          process.analyzeSystematicsMu0bJERUp *
                                          process.analyzeSystematicsMu1bJERUp *
                                          process.analyzeSystematicsMu2bJERUp *
                                          process.analyzeSystematicsMu3bJERUp
                                          )

##  muon selection w/o with scaled down jet energy resolution
process.RA4bMuonSelectionJERDown = cms.Path(## Producer sequences
                                            process.createAllObjects *
                                            process.btagEventWeightMu *
                                            ## Selection sequences
                                            process.preselectionMC2PAT* 
                                            process.preselectionMuHTMC2 *
                                            process.MuHadSelectionJERDown *
                                            process.muonSelection*
                                            process.jetSelectionJERDown*
                                            ## Analyzer Sequence
                                            process.analyzeSystematicsMu0bJERDown *
                                            process.analyzeSystematicsMu1bJERDown *
                                            process.analyzeSystematicsMu2bJERDown *
                                            process.analyzeSystematicsMu3bJERDown
                                            )

#----------------------------
# Electron selection paths
#----------------------------

## electron selection w/o scaled jet energy
process.RA4bElectronSelection = cms.Path(## Producer sequences
                                     process.createAllObjects *
                                     process.btagEventWeightEl *
                                     process.btagEventWeightElBtagSFUp *
                                     process.btagEventWeightElBtagSFDown *
                                     process.btagEventWeightElMistagSFUp *
                                     process.btagEventWeightElMistagSFDown *
                                     ## Selection sequences
                                     process.preselectionMC2PAT* 
                                     process.preselectionElHTMC2 *
                                     process.ElHadSelection *
                                     process.electronSelection*
                                     process.jetSelection *
                                     ## Analyzer Sequences for El 0 btags
                                     process.analyzeSystematicsEl0b *
                                     process.analyzeSystematicsEl0bMETUp *
                                     process.analyzeSystematicsEl0bMETDown *
                                     process.analyzeSystematicsEl0bBtagSFUp *
                                     process.analyzeSystematicsEl0bBtagSFDown *
                                     process.analyzeSystematicsEl0bMistagSFUp *
                                     process.analyzeSystematicsEl0bMistagSFDown *
                                     process.analyzeSystematicsEl0bPUUp *
                                     process.analyzeSystematicsEl0bPUDown *
                                     ## Analyzer Sequences for El 1 btags
                                     process.analyzeSystematicsEl1b *
                                     process.analyzeSystematicsEl1bMETUp *
                                     process.analyzeSystematicsEl1bMETDown *
                                     process.analyzeSystematicsEl1bBtagSFUp *
                                     process.analyzeSystematicsEl1bBtagSFDown *
                                     process.analyzeSystematicsEl1bMistagSFUp *
                                     process.analyzeSystematicsEl1bMistagSFDown *
                                     process.analyzeSystematicsEl1bPUUp *
                                     process.analyzeSystematicsEl1bPUDown *
                                     ## Analyzer Sequences for El 2 btags
                                     process.analyzeSystematicsEl2b *
                                     process.analyzeSystematicsEl2bMETUp *
                                     process.analyzeSystematicsEl2bMETDown *
                                     process.analyzeSystematicsEl2bBtagSFUp *
                                     process.analyzeSystematicsEl2bBtagSFDown *
                                     process.analyzeSystematicsEl2bMistagSFUp *
                                     process.analyzeSystematicsEl2bMistagSFDown *
                                     process.analyzeSystematicsEl2bPUUp *
                                     process.analyzeSystematicsEl2bPUDown *
                                     ## Analyzer Sequences for El 3 btags
                                     process.analyzeSystematicsEl3b *
                                     process.analyzeSystematicsEl3bMETUp *
                                     process.analyzeSystematicsEl3bMETDown *
                                     process.analyzeSystematicsEl3bBtagSFUp *
                                     process.analyzeSystematicsEl3bBtagSFDown *
                                     process.analyzeSystematicsEl3bMistagSFUp *
                                     process.analyzeSystematicsEl3bMistagSFDown *
                                     process.analyzeSystematicsEl3bPUUp *
                                     process.analyzeSystematicsEl3bPUDown
                                     )

##  electron selection w/o with scaled up jet energy corrections
process.RA4bElectronSelectionJECUp = cms.Path(## Producer sequences
                                          process.createAllObjects *
                                          process.btagEventWeightEl *
                                          ## Selection sequences
                                          process.preselectionMC2PAT* 
                                          process.preselectionElHTMC2 *
                                          process.ElHadSelectionJECUp *
                                          process.electronSelection*
                                          process.jetSelectionJECUp*
                                          ## Analyzer Sequence
                                          process.analyzeSystematicsEl0bJECUp *
                                          process.analyzeSystematicsEl1bJECUp *
                                          process.analyzeSystematicsEl2bJECUp *
                                          process.analyzeSystematicsEl3bJECUp
                                          )

##  electron selection w/o with scaled down jet energy corrections
process.RA4bElectronSelectionJECDown = cms.Path(## Producer sequences
                                            process.createAllObjects *
                                            process.btagEventWeightEl *
                                            ## Selection sequences
                                            process.preselectionMC2PAT* 
                                            process.preselectionElHTMC2 *
                                            process.ElHadSelectionJECDown *
                                            process.electronSelection*
                                            process.jetSelectionJECDown*
                                            ## Analyzer Sequence
                                            process.analyzeSystematicsEl0bJECDown *
                                            process.analyzeSystematicsEl1bJECDown *
                                            process.analyzeSystematicsEl2bJECDown *
                                            process.analyzeSystematicsEl3bJECDown
                                            )

##  electron selection w/o with scaled up jet energy resolution
process.RA4bElectronSelectionJERUp = cms.Path(## Producer sequences
                                          process.createAllObjects *
                                          process.btagEventWeightEl *
                                          ## Selection sequences
                                          process.preselectionMC2PAT* 
                                          process.preselectionElHTMC2 *
                                          process.ElHadSelectionJERUp *
                                          process.electronSelection*
                                          process.jetSelectionJERUp*
                                          ## Analyzer Sequence
                                          process.analyzeSystematicsEl0bJERUp *
                                          process.analyzeSystematicsEl1bJERUp *
                                          process.analyzeSystematicsEl2bJERUp *
                                          process.analyzeSystematicsEl3bJERUp
                                          )

##  electron selection w/o with scaled down jet energy resolution
process.RA4bElectronSelectionJERDown = cms.Path(## Producer sequences
                                            process.createAllObjects *
                                            process.btagEventWeightEl *
                                            ## Selection sequences
                                            process.preselectionMC2PAT* 
                                            process.preselectionElHTMC2 *
                                            process.ElHadSelectionJERDown *
                                            process.electronSelection*
                                            process.jetSelectionJERDown*
                                            ## Analyzer Sequence
                                            process.analyzeSystematicsEl0bJERDown *
                                            process.analyzeSystematicsEl1bJERDown *
                                            process.analyzeSystematicsEl2bJERDown *
                                            process.analyzeSystematicsEl3bJERDown
                                            )



#--------------------------
# muon selection paths
#--------------------------
#
## no btag
#rocess.Selection1m = cms.Path(process.PATTuple*    
#                              process.makeObjects *
#                              process.makeSUSYGenEvt *
#                              process.eventWeightPU *
#                              process.weightProducer *
#                              process.analyzeSUSYBjets1m_noCuts * #This is important. Will find the no of subprocs.
#                              process.preselectionMC2PAT*
#                              process.preselectionMuHTMC2 *
#                              process.MuHadSelection *
#                              process.analyzeSUSYBjets1m_preselection *
#                              process.RA4MuonCollections *
#                              process.RA4MuonSelection *
#                              process.muonSelection*
#                              process.analyzeSUSYBjets1m_leptonSelection *
#                              process.jetSelection*
#                              process.analyzeSUSYBjets1m_jetSelection *
#                              process.HTSelection *
#                              process.analyzeSUSYBjets1m_HTSelection *
#                              process.metSelection *
#                              process.analyzeSUSYBjets1m_metSelection *
#                              process.mTSelection *
#                              process.analyzeSUSYBjets1m_mTSelection
#                              )
## exactly 1 btag
#rocess.Selection1b1m_2 = cms.Path(process.createAllObjects*
#                                  process.basicMuonSelections*
#                                  process.exactlyOneMediumTrackHighEffBjet *
#                                  process.analyzeSUSYBjets1b1m_4 *
#                                  process.HTSelection *
#                                  process.analyzeSUSYBjets1b1m_5 *
#                                  process.metSelection *
#                                  process.analyzeSUSYBjets1b1m_6 *
#                                  process.mTSelection *
#                                  process.analyzeSUSYBjets1b1m_1
#                                  )
## exactly 2 btags
#rocess.Selection2b1m_2 = cms.Path(process.createAllObjects*
#                                  process.basicMuonSelections*
#                                  process.exactlyTwoMediumTrackHighEffBjets *
#                                  process.analyzeSUSYBjets2b1m_4 *
#                                  process.HTSelection *
#                                  process.analyzeSUSYBjets2b1m_5 *
#                                  process.metSelection *
#                                  process.analyzeSUSYBjets2b1m_6 *
#                                  process.mTSelection *
#                                  process.analyzeSUSYBjets2b1m_1
#                                  )
## at least 3 btags
#rocess.Selection3b1m_1 = cms.Path(process.createAllObjects*
#                                  process.basicMuonSelections*
#                                  process.threeMediumTrackHighEffBjets *
#                                  process.analyzeSUSYBjets3b1m_4 *
#                                  process.HTSelection *
#                                  process.analyzeSUSYBjets3b1m_5 *
#                                  process.metSelection *
#                                  process.analyzeSUSYBjets3b1m_6 *
#                                  process.mTSelection *
#                                  process.analyzeSUSYBjets3b1m_1
#                                  )
#
#--------------------------
# electron selection paths
#--------------------------
#
## no btag
#rocess.Selection1e = cms.Path(process.PATTuple*
#                              process.makeObjects *
#                              process.makeSUSYGenEvt *
#                              process.eventWeightPU *
#                              process.weightProducer *
#                              process.analyzeSUSYBjets1e_noCuts * #Also important. But should give the same as 1m!
#                              process.preselectionMC2PAT*
#                              process.preselectionElHTMC2 *
#                              process.ElHadSelection *
#                              process.analyzeSUSYBjets1e_preselection *
#                              process.electronSelection*
#                              process.analyzeSUSYBjets1e_leptonSelection *
#                              process.jetSelection*
#                              process.analyzeSUSYBjets1e_jetSelection *
#                              process.HTSelection *
#                              process.analyzeSUSYBjets1e_HTSelection *
#                              process.metSelection *
#                              process.analyzeSUSYBjets1e_metSelection *
#                              process.mTSelection *
#                              process.analyzeSUSYBjets1e_mTSelection
#                              )
#
## exactly 1 btag
#rocess.Selection1b1e_2 = cms.Path(process.createAllObjects*
#                                  process.basicElectronSelections*
#                                  process.exactlyOneMediumTrackHighEffBjet *
#                                  process.analyzeSUSYBjets1b1e_4 *
#                                  process.HTSelection *
#                                  process.analyzeSUSYBjets1b1e_5 *
#                                  process.metSelection *
#                                  process.analyzeSUSYBjets1b1e_6 *
#                                  process.mTSelection *
#                                  process.analyzeSUSYBjets1b1e_1
#                                  )
#
## exactly 2 btags
#rocess.Selection2b1e_2 = cms.Path(process.createAllObjects*
#                                  process.basicElectronSelections*
#                                  process.exactlyTwoMediumTrackHighEffBjets *
#                                  process.analyzeSUSYBjets2b1e_4 *
#                                  process.HTSelection *
#                                  process.analyzeSUSYBjets2b1e_5 *
#                                  process.metSelection *
#                                  process.analyzeSUSYBjets2b1e_6 *
#                                  process.mTSelection *
#                                  process.analyzeSUSYBjets2b1e_1
#                                  )
#
## at least 3 btags
#rocess.Selection3b1e_1 = cms.Path(process.createAllObjects*
#                                  process.basicElectronSelections*
#                                  process.threeMediumTrackHighEffBjets *
#                                  process.analyzeSUSYBjets3b1e_4 *
#                                  process.HTSelection *
#                                  process.analyzeSUSYBjets3b1e_5 *
#                                  process.metSelection *
#                                  process.analyzeSUSYBjets3b1e_6 *
#                                  process.mTSelection *
#                                  process.analyzeSUSYBjets3b1e_1
#                                  )
#
#
