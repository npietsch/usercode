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
    version = cms.untracked.string('$Revision: 1.3 $'),
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


#-------------------------------------------------
# Load and configure module for event weighting
#-------------------------------------------------

process.load("TopAnalysis.TopUtils.EventWeightPU_cfi")
process.load("SUSYAnalysis.SUSYEventProducers.WeightProducer_cfi")
#process.eventWeightPU.DataFile = "TopAnalysis/TopUtils/data/Data_PUDist_160404-163869_7TeV_May10ReReco_Collisions11_v2_and_165088-167913_7TeV_PromptReco_Collisions11.root"
#process.eventWeightPU.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_TTJets_TuneZ2_7TeV_madgraph_tauola.root"

#------------------------------------------------------------
# load and configure modules for b-tag efficiency weighting
#------------------------------------------------------------

process.load ("RecoBTag.PerformanceDB.PoolBTagPerformanceDB1107")
process.load ("RecoBTag.PerformanceDB.BTagPerformanceDB1107")
process.load("Btagging.BtagWeightProducer.BtagEventWeight_cfi")

## common default settings (similar for muon and electron channel)
process.btagEventWeight           = process.btagEventWeight.clone()
process.btagEventWeight.bTagAlgo  = "TCHEM"
process.btagEventWeight.filename  = "./BtagEff_TTJets.root"

## muon channel default settings
process.btagEventWeightMu                    = process.btagEventWeight.clone()
process.btagEventWeightMu.rootDir            = "RA4bMuTCHEM3"

## create weights for muon selection
process.btagEventWeightMuJER                 = process.btagEventWeightMu.clone()
process.btagEventWeightMuJER.jets            = "smearedGoodJets"

process.btagEventWeightMuBtagSFUp            = process.btagEventWeightMuJER.clone()
process.btagEventWeightMuBtagSFUp.sysVar     = "bTagSFUp"

process.btagEventWeightMuBtagSFDown          = process.btagEventWeightMuJER.clone()
process.btagEventWeightMuBtagSFDown.sysVar   = "bTagSFDown"

process.btagEventWeightMuMistagSFUp          = process.btagEventWeightMuJER.clone()
process.btagEventWeightMuBtagSFUp.sysVar     = "MisTagSFUp"

process.btagEventWeightMuMistagSFDown        = process.btagEventWeightMuJER.clone()
process.btagEventWeightMuMistagSFDown.sysVar = "MisTagSFDown"

## electron channel default settings
process.btagEventWeightEl                    = process.btagEventWeight.clone()
process.btagEventWeightEl.rootDir            = "RA4bElTCHEM3"

## create weights for electron selection
process.btagEventWeightElJER                 = process.btagEventWeightEl.clone()
process.btagEventWeightElJER.jets            = "smearedGoodJets"

process.btagEventWeightElBtagSFUp            = process.btagEventWeightElJER.clone()
process.btagEventWeightElBtagSFUp.sysVar     = "bTagSFUp"

process.btagEventWeightElBtagSFDown          = process.btagEventWeightElJER.clone()
process.btagEventWeightElBtagSFDown.sysVar   = "bTagSFDown"

process.btagEventWeightElMistagSFUp          = process.btagEventWeightElJER.clone()
process.btagEventWeightElBtagSFUp.sysVar     = "MisTagSFUp"

process.btagEventWeightElMistagSFDown        = process.btagEventWeightElJER.clone()
process.btagEventWeightElMistagSFDown.sysVar = "MisTagSFDown"


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
process.scaledJetEnergy.maxJetEtaForMET = 4.7      ## proposed on Nov 15 in RA4 meeting

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


#-----------------------------------------------------------------
# Load and configure module to scale lepton energy
#-----------------------------------------------------------------

process.load("SUSYAnalysis.Uncertainties.LeptonEnergy_cfi")

process.scaledLeptonEnergy.inputMuons = "goodMuons"
process.scaledLeptonEnergy.inputElectrons = "goodElectrons"
process.scaledLeptonEnergy.inputMETs = "scaledJetEnergy:patMETsPF"

process.scaledLeptonEnergyUp = process.scaledLeptonEnergy.clone()
process.scaledLeptonEnergyUp.scaleFactorMu = 1.01     ## proposed on Nov 15 in RA4 meeting
process.scaledLeptonEnergyUp.scaleFactorEl = 1.025    ## proposed on Nov 15 in RA4 meeting

process.scaledLeptonEnergyDown = process.scaledLeptonEnergy.clone()
process.scaledLeptonEnergyDown.scaleFactorMu = 0.99   ## proposed on Nov 15 in RA4 meeting
process.scaledLeptonEnergyDown.scaleFactorEl = 0.975  ## proposed on Nov 15 in RA4 meeting

#-----------------------------------------------------------------
# Load and configure module to scale unclustered energy
#-----------------------------------------------------------------

process.load("SUSYAnalysis.Uncertainties.UnclusteredEnergy_cfi")

process.scaledUnclusteredEnergyUp = process.unclusteredEnergy.clone()
process.scaledUnclusteredEnergyUp.scaleFactor = 1.1
process.scaledUnclusteredEnergyUp.inputMETs = "scaledJetEnergy:patMETsPF"

process.scaledUnclusteredEnergyDown = process.unclusteredEnergy.clone()
process.scaledUnclusteredEnergyDown.scaleFactor = 0.9
process.scaledUnclusteredEnergyDown.inputMETs = "scaledJetEnergy:patMETsPF"

#-----------------------------------------------------------------------------------------
# Load modules for analysis on generator level, level of matched objects and reco level
#-----------------------------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYAnalyzer.sequences.SystematicsAnalyzerMu_cff")
process.load("SUSYAnalysis.SUSYAnalyzer.sequences.SystematicsAnalyzerEl_cff")

#----------------------------------------------------------------------------------------
# Load modules for analysis on generator level, level of matched objects and reco-level
#-----------------------------------------------------------------------------------------

#process.load("SUSYAnalysis.SUSYAnalyzer.sequences.SUSYBjetsAnalysis_cff")




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

#process.createAllObjects = cms.Sequence(process.PATTuple*
#                                        process.scaledJetEnergy *
#                                        process.scaledJetEnergyJECUp *
#                                        process.scaledJetEnergyJECDown *
#                                        process.scaledJetEnergyJERUp *
#                                        process.scaledJetEnergyJERDown *
#                                        process.createGoodObjects *
#                                        process.makeSUSYGenEvt *
#                                        process.eventWeightPU *
#                                        process.weightProducer 
#                                        )
 
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

#Create a set of analysers to perform pre-cut checks
process.analyzeSystematicsNoCuts0b = process.analyzeSystematicsMu0b.clone()
process.analyzeSystematicsNoCuts1b = process.analyzeSystematicsMu1b.clone()
process.analyzeSystematicsNoCuts2b = process.analyzeSystematicsMu2b.clone()
process.analyzeSystematicsNoCuts3b = process.analyzeSystematicsMu3b.clone()

#--------------------------
# Muon selection paths
#--------------------------

##  muon selection w/o smeared jet energy
process.RA4bMuonSelection = cms.Path(process.PATTuple * ## Object Producer sequences
                                     process.createGoodLeptons *
                                     process.createGoodJets *
                                     process.createGoodMETs *
                                     process.makeSUSYGenEvt *
                                     ## Weight producer sequences
                                     process.eventWeightPU *
                                     process.weightProducer *
                                     process.btagEventWeightMu *
                                     ## Analyzer Sequences
                                     process.analyzeSystematicsNoCuts0b *
                                     process.analyzeSystematicsNoCuts1b *
                                     process.analyzeSystematicsNoCuts2b *
                                     process.analyzeSystematicsNoCuts3b *                                  
                                     ## Selection sequences
                                     process.preselectionMuHTMC2 * process.preselectionMC2PAT *  
                                     process.MuHadSelection *
                                     process.muonSelection *
                                     process.jetSelection *
                                     ## Analyzer Sequences
                                     process.analyzeSystematicsMu0b *
                                     process.analyzeSystematicsMu1b *
                                     process.analyzeSystematicsMu2b *
                                     process.analyzeSystematicsMu3b
                                     )

## muon selection with smeared jet energy
process.RA4bMuonSelectionJER = cms.Path(process.PATTuple * ## Object Producer sequences
                                        process.scaledJetEnergy *
                                        process.createGoodLeptons *
                                        process.createSmearedGoodJets *
                                        process.createSmearedGoodMETs *
                                        process.makeSUSYGenEvt *
                                        ## Weight producer sequences
                                        process.eventWeightPU *
                                        process.weightProducer *
                                        process.btagEventWeightMuJER *
                                        process.btagEventWeightMuBtagSFUp *
                                        process.btagEventWeightMuBtagSFDown *
                                        process.btagEventWeightMuMistagSFUp *
                                        process.btagEventWeightMuMistagSFDown *
                                        ## Selection sequences
                                        process.preselectionMuHTMC2 * process.preselectionMC2PAT *  
                                        process.MuHadSelectionJER *
                                        process.muonSelection *
                                        process.jetSelectionJER *
                                        ## Analyzer Sequences for Mu 0 btags
                                        process.analyzeSystematicsMu0bJER *
                                        process.analyzeSystematicsMu0bBtagSFUp *
                                        process.analyzeSystematicsMu0bBtagSFDown *
                                        process.analyzeSystematicsMu0bMistagSFUp *
                                        process.analyzeSystematicsMu0bMistagSFDown *
                                        process.analyzeSystematicsMu0bPUUp *
                                        process.analyzeSystematicsMu0bPUDown *
                                        process.analyzeSystematicsMu0bWUp *
                                        process.analyzeSystematicsMu0bWDown *
                                        ## Analyzer Sequences for Mu 1 btags
                                        process.analyzeSystematicsMu1bJER *
                                        process.analyzeSystematicsMu1bBtagSFUp *
                                        process.analyzeSystematicsMu1bBtagSFDown *
                                        process.analyzeSystematicsMu1bMistagSFUp *
                                        process.analyzeSystematicsMu1bMistagSFDown *
                                        process.analyzeSystematicsMu1bPUUp *
                                        process.analyzeSystematicsMu1bPUDown *
                                        process.analyzeSystematicsMu1bWUp *
                                        process.analyzeSystematicsMu1bWDown *
                                        ## Analyzer Sequences for Mu 2 btags
                                        process.analyzeSystematicsMu2bJER *
                                        process.analyzeSystematicsMu2bBtagSFUp *
                                        process.analyzeSystematicsMu2bBtagSFDown *
                                        process.analyzeSystematicsMu2bMistagSFUp *
                                        process.analyzeSystematicsMu2bMistagSFDown *
                                        process.analyzeSystematicsMu2bPUUp *
                                        process.analyzeSystematicsMu2bPUDown *
                                        process.analyzeSystematicsMu2bWUp *
                                        process.analyzeSystematicsMu2bWDown *
                                        ## Analyzer Sequences for Mu 3 btags
                                        process.analyzeSystematicsMu3bJER *
                                        process.analyzeSystematicsMu3bBtagSFUp *
                                        process.analyzeSystematicsMu3bBtagSFDown *
                                        process.analyzeSystematicsMu3bMistagSFUp *
                                        process.analyzeSystematicsMu3bMistagSFDown *
                                        process.analyzeSystematicsMu3bPUUp *
                                        process.analyzeSystematicsMu3bPUDown *
                                        process.analyzeSystematicsMu3bWUp *
                                        process.analyzeSystematicsMu3bWDown
                                        )

##  muon selection with smeared jet energy and scaled up lepton energy
process.RA4bMuonSelectionLepUp = cms.Path(process.PATTuple * ## Object Producer sequences
                                          process.scaledJetEnergy *
                                          process.createGoodLeptonsUp *
                                          process.createSmearedGoodJets *
                                          process.scaledLeptonEnergyUp *
                                          process.createGoodMETsLepUp *
                                          process.makeSUSYGenEvt *
                                          ## Weight producer sequences
                                          process.eventWeightPU *
                                          process.weightProducer *
                                          process.btagEventWeightMuJER *
                                          ## Selection sequences
                                          process.preselectionMuHTMC2 * process.preselectionMC2PAT *  
                                          process.MuHadSelectionLepUp *
                                          process.muonSelectionUp *
                                          process.jetSelectionJER *
                                          ## Analyzer Sequences
                                          process.analyzeSystematicsMu0bLepUp *
                                          process.analyzeSystematicsMu1bLepUp *
                                          process.analyzeSystematicsMu2bLepUp *
                                          process.analyzeSystematicsMu3bLepUp
                                          )

##  muon selection with smeared jet energy and scaled down lepton energy
process.RA4bMuonSelectionLepDown = cms.Path(process.PATTuple * ## Object Producer sequences
                                            process.scaledJetEnergy *
                                            process.createGoodLeptonsDown *
                                            process.createSmearedGoodJets *
                                            process.scaledLeptonEnergyDown *
                                            process.createGoodMETsLepDown *
                                            process.makeSUSYGenEvt *
                                            ## Weight producer sequences
                                            process.eventWeightPU *
                                            process.weightProducer *
                                            process.btagEventWeightMuJER *
                                            ## Selection sequences
                                            process.preselectionMuHTMC2 * process.preselectionMC2PAT *  
                                            process.MuHadSelectionLepDown *
                                            process.muonSelectionDown *
                                            process.jetSelectionJER *
                                            ## Analyzer Sequences
                                            process.analyzeSystematicsMu0bLepDown *
                                            process.analyzeSystematicsMu1bLepDown *
                                            process.analyzeSystematicsMu2bLepDown *
                                            process.analyzeSystematicsMu3bLepDown
                                            )

##  muon selection with smeared jet energy and scaled up unclustered energy
process.RA4bMuonSelectionMETUp = cms.Path(process.PATTuple * ## Object Producer sequences
                                          process.scaledJetEnergy *
                                          process.createGoodLeptons *
                                          process.createSmearedGoodJets *
                                          process.scaledUnclusteredEnergyUp *
                                          process.createGoodMETsMETUp *
                                          process.makeSUSYGenEvt *
                                          ## Weight producer sequences
                                          process.eventWeightPU *
                                          process.weightProducer *
                                          process.btagEventWeightMuJER *
                                          ## Selection sequences
                                          process.preselectionMuHTMC2 * process.preselectionMC2PAT *  
                                          process.MuHadSelectionMETUp *
                                          process.muonSelection *
                                          process.jetSelectionJER *
                                          ## Analyzer Sequences
                                          process.analyzeSystematicsMu0bMETUp *
                                          process.analyzeSystematicsMu1bMETUp *
                                          process.analyzeSystematicsMu2bMETUp *
                                          process.analyzeSystematicsMu3bMETUp
                                          )

##  muon selection with smeared jet energy and scaled down unclustered energy
process.RA4bMuonSelectionMETDown = cms.Path(process.PATTuple * ## Object Producer sequences
                                          process.scaledJetEnergy *
                                          process.createGoodLeptons *
                                          process.createSmearedGoodJets *
                                          process.scaledUnclusteredEnergyDown *
                                          process.createGoodMETsMETDown *
                                          process.makeSUSYGenEvt *
                                          ## Weight producer sequences
                                          process.eventWeightPU *
                                          process.weightProducer *
                                          process.btagEventWeightMuJER *
                                          ## Selection sequences
                                          process.preselectionMuHTMC2 * process.preselectionMC2PAT *  
                                          process.MuHadSelectionMETDown *
                                          process.muonSelection *
                                          process.jetSelectionJER *
                                          ## Analyzer Sequences
                                          process.analyzeSystematicsMu0bMETDown *
                                          process.analyzeSystematicsMu1bMETDown *
                                          process.analyzeSystematicsMu2bMETDown *
                                          process.analyzeSystematicsMu3bMETDown
                                          )

##  muon selection with smeared and scaled up jet energy corrections
process.RA4bMuonSelectionJECUp = cms.Path(process.PATTuple * ## Producer sequences
                                          process.scaledJetEnergyJECUp *
                                          process.createGoodLeptons *
                                          process.createGoodJetsJECUp *
                                          process.createGoodMETsJECUp *
                                          process.makeSUSYGenEvt *
                                          ## Weight producer sequences
                                          process.eventWeightPU *
                                          process.weightProducer *
                                          process.btagEventWeightMuJER *
                                          ## Selection sequences
                                          process.preselectionMuHTMC2 * process.preselectionMC2PAT *  
                                          process.MuHadSelectionJECUp *
                                          process.muonSelection *
                                          process.jetSelectionJECUp *
                                          ## Analyzer Sequences
                                          process.analyzeSystematicsMu0bJECUp *
                                          process.analyzeSystematicsMu1bJECUp *
                                          process.analyzeSystematicsMu2bJECUp *
                                          process.analyzeSystematicsMu3bJECUp
                                          )

##  muon selection with smeared and scaled down jet energy corrections
process.RA4bMuonSelectionJECDown = cms.Path(process.PATTuple * ## Producer sequences
                                          process.scaledJetEnergyJECDown *
                                          process.createGoodLeptons *
                                          process.createGoodJetsJECDown *
                                          process.createGoodMETsJECDown *
                                          process.makeSUSYGenEvt *
                                          ## Weight producer sequences
                                          process.eventWeightPU *
                                          process.weightProducer *
                                          process.btagEventWeightMuJER *
                                          ## Selection sequences
                                          process.preselectionMuHTMC2 * process.preselectionMC2PAT *  
                                          process.MuHadSelectionJECDown *
                                          process.muonSelection *
                                          process.jetSelectionJECDown *
                                          ## Analyzer Sequences
                                          process.analyzeSystematicsMu0bJECDown *
                                          process.analyzeSystematicsMu1bJECDown *
                                          process.analyzeSystematicsMu2bJECDown *
                                          process.analyzeSystematicsMu3bJECDown
                                          )

##  muon selection with smeared and scaled up jet energy resolution
process.RA4bMuonSelectionJERUp = cms.Path(process.PATTuple * ## Producer sequences
                                          process.scaledJetEnergyJERUp *
                                          process.createGoodLeptons *
                                          process.createGoodJetsJERUp *
                                          process.createGoodMETsJERUp *
                                          process.makeSUSYGenEvt *
                                          ## Weight producer sequences
                                          process.eventWeightPU *
                                          process.weightProducer *
                                          process.btagEventWeightMuJER *
                                          ## Selection sequences
                                          process.preselectionMuHTMC2 * process.preselectionMC2PAT *  
                                          process.MuHadSelectionJERUp *
                                          process.muonSelection *
                                          process.jetSelectionJERUp *
                                          ## Analyzer Sequences
                                          process.analyzeSystematicsMu0bJERUp *
                                          process.analyzeSystematicsMu1bJERUp *
                                          process.analyzeSystematicsMu2bJERUp *
                                          process.analyzeSystematicsMu3bJERUp
                                          )

##  muon selection with smeared and scaled down jet energy resolution
process.RA4bMuonSelectionJERDown = cms.Path(process.PATTuple * ## Producer sequences
                                          process.scaledJetEnergyJERDown *
                                          process.createGoodLeptons *
                                          process.createGoodJetsJERDown *
                                          process.createGoodMETsJERDown *
                                          process.makeSUSYGenEvt *
                                          ## Weight producer sequences
                                          process.eventWeightPU *
                                          process.weightProducer *
                                          process.btagEventWeightMuJER *
                                          ## Selection sequences
                                          process.preselectionMuHTMC2 * process.preselectionMC2PAT *  
                                          process.MuHadSelectionJERDown *
                                          process.muonSelection *
                                          process.jetSelectionJERDown *
                                          ## Analyzer Sequences
                                          process.analyzeSystematicsMu0bJERDown *
                                          process.analyzeSystematicsMu1bJERDown *
                                          process.analyzeSystematicsMu2bJERDown *
                                          process.analyzeSystematicsMu3bJERDown 
                                          )


#--------------------------
# Electron selection paths
#--------------------------

##  electron selection w/o smeared jet energy
process.RA4bElectronSelection = cms.Path(process.PATTuple * ## Object Producer sequences
                                     process.createGoodLeptons *
                                     process.createGoodJets *
                                     process.createGoodMETs *
                                     process.makeSUSYGenEvt *
                                     ## Weight producer sequences
                                     process.eventWeightPU *
                                     process.weightProducer *
                                     process.btagEventWeightEl *
                                     ## Selection sequences
                                     process.preselectionElHTMC2 * process.preselectionMC2PAT *  
                                     process.ElHadSelection *
                                     process.electronSelection *
                                     process.jetSelection *
                                     ## Analyzer Sequences
                                     process.analyzeSystematicsEl0b *
                                     process.analyzeSystematicsEl1b *
                                     process.analyzeSystematicsEl2b *
                                     process.analyzeSystematicsEl3b
                                     )

## electron selection with smeared jet energy
process.RA4bElectronSelectionJER = cms.Path(process.PATTuple * ## Object Producer sequences
                                        process.scaledJetEnergy *
                                        process.createGoodLeptons *
                                        process.createSmearedGoodJets *
                                        process.createSmearedGoodMETs *
                                        process.makeSUSYGenEvt *
                                        ## Weight producer sequences
                                        process.eventWeightPU *
                                        process.weightProducer *
                                        process.btagEventWeightElJER *
                                        process.btagEventWeightElBtagSFUp *
                                        process.btagEventWeightElBtagSFDown *
                                        process.btagEventWeightElMistagSFUp *
                                        process.btagEventWeightElMistagSFDown *
                                        ## Selection sequences
                                        process.preselectionElHTMC2 * process.preselectionMC2PAT *  
                                        process.ElHadSelectionJER *
                                        process.electronSelection *
                                        process.jetSelectionJER *
                                        ## Analyzer Sequences for El 0 btags
                                        process.analyzeSystematicsEl0bJER *
                                        process.analyzeSystematicsEl0bBtagSFUp *
                                        process.analyzeSystematicsEl0bBtagSFDown *
                                        process.analyzeSystematicsEl0bMistagSFUp *
                                        process.analyzeSystematicsEl0bMistagSFDown *
                                        process.analyzeSystematicsEl0bPUUp *
                                        process.analyzeSystematicsEl0bPUDown *
                                        process.analyzeSystematicsEl0bWUp *
                                        process.analyzeSystematicsEl0bWDown *
                                        ## Analyzer Sequences for El 1 btags
                                        process.analyzeSystematicsEl1bJER *
                                        process.analyzeSystematicsEl1bBtagSFUp *
                                        process.analyzeSystematicsEl1bBtagSFDown *
                                        process.analyzeSystematicsEl1bMistagSFUp *
                                        process.analyzeSystematicsEl1bMistagSFDown *
                                        process.analyzeSystematicsEl1bPUUp *
                                        process.analyzeSystematicsEl1bPUDown *
                                        process.analyzeSystematicsEl1bWUp *
                                        process.analyzeSystematicsEl1bWDown *
                                        ## Analyzer Sequences for El 2 btags
                                        process.analyzeSystematicsEl2bJER *
                                        process.analyzeSystematicsEl2bBtagSFUp *
                                        process.analyzeSystematicsEl2bBtagSFDown *
                                        process.analyzeSystematicsEl2bMistagSFUp *
                                        process.analyzeSystematicsEl2bMistagSFDown *
                                        process.analyzeSystematicsEl2bPUUp *
                                        process.analyzeSystematicsEl2bPUDown *
                                        process.analyzeSystematicsEl2bWUp *
                                        process.analyzeSystematicsEl2bWDown *
                                        ## Analyzer Sequences for El 3 btags
                                        process.analyzeSystematicsEl3bJER *
                                        process.analyzeSystematicsEl3bBtagSFUp *
                                        process.analyzeSystematicsEl3bBtagSFDown *
                                        process.analyzeSystematicsEl3bMistagSFUp *
                                        process.analyzeSystematicsEl3bMistagSFDown *
                                        process.analyzeSystematicsEl3bPUUp *
                                        process.analyzeSystematicsEl3bPUDown *
                                        process.analyzeSystematicsEl3bWUp *
                                        process.analyzeSystematicsEl3bWDown
                                        )

##  electron selection with smeared jet energy and scaled up lepton energy
process.RA4bElectronSelectionLepUp = cms.Path(process.PATTuple * ## Object Producer sequences
                                          process.scaledJetEnergy *
                                          process.createGoodLeptonsUp *
                                          process.createSmearedGoodJets *
                                          process.scaledLeptonEnergyUp *
                                          process.createGoodMETsLepUp *
                                          process.makeSUSYGenEvt *
                                          ## Weight producer sequences
                                          process.eventWeightPU *
                                          process.weightProducer *
                                          process.btagEventWeightElJER *
                                          ## Selection sequences
                                          process.preselectionElHTMC2 * process.preselectionMC2PAT *  
                                          process.ElHadSelectionLepUp *
                                          process.electronSelectionUp *
                                          process.jetSelectionJER *
                                          ## Analyzer Sequences
                                          process.analyzeSystematicsEl0bLepUp *
                                          process.analyzeSystematicsEl1bLepUp *
                                          process.analyzeSystematicsEl2bLepUp *
                                          process.analyzeSystematicsEl3bLepUp
                                          )

##  electron selection with smeared jet energy and scaled down lepton energy
process.RA4bElectronSelectionLepDown = cms.Path(process.PATTuple * ## Object Producer sequences
                                            process.scaledJetEnergy *
                                            process.createGoodLeptonsDown *
                                            process.createSmearedGoodJets *
                                            process.scaledLeptonEnergyDown *
                                            process.createGoodMETsLepDown *
                                            process.makeSUSYGenEvt *
                                            ## Weight producer sequences
                                            process.eventWeightPU *
                                            process.weightProducer *
                                            process.btagEventWeightElJER *
                                            ## Selection sequences
                                            process.preselectionElHTMC2 * process.preselectionMC2PAT *  
                                            process.ElHadSelectionLepDown *
                                            process.electronSelectionDown *
                                            process.jetSelectionJER *
                                            ## Analyzer Sequences
                                            process.analyzeSystematicsEl0bLepDown *
                                            process.analyzeSystematicsEl1bLepDown *
                                            process.analyzeSystematicsEl2bLepDown *
                                            process.analyzeSystematicsEl3bLepDown
                                            )

##  electron selection with smeared jet energy and scaled up unclustered energy
process.RA4bElectronSelectionMETUp = cms.Path(process.PATTuple * ## Object Producer sequences
                                          process.scaledJetEnergy *
                                          process.createGoodLeptons *
                                          process.createSmearedGoodJets *
                                          process.scaledUnclusteredEnergyUp *
                                          process.createGoodMETsMETUp *
                                          process.makeSUSYGenEvt *
                                          ## Weight producer sequences
                                          process.eventWeightPU *
                                          process.weightProducer *
                                          process.btagEventWeightElJER *
                                          ## Selection sequences
                                          process.preselectionElHTMC2 * process.preselectionMC2PAT *  
                                          process.ElHadSelectionMETUp *
                                          process.electronSelection *
                                          process.jetSelectionJER *
                                          ## Analyzer Sequences
                                          process.analyzeSystematicsEl0bMETUp *
                                          process.analyzeSystematicsEl1bMETUp *
                                          process.analyzeSystematicsEl2bMETUp *
                                          process.analyzeSystematicsEl3bMETUp
                                          )

##  electron selection with smeared jet energy and scaled down unclustered energy
process.RA4bElectronSelectionMETDown = cms.Path(process.PATTuple * ## Object Producer sequences
                                          process.scaledJetEnergy *
                                          process.createGoodLeptons *
                                          process.createSmearedGoodJets *
                                          process.scaledUnclusteredEnergyDown *
                                          process.createGoodMETsMETDown *
                                          process.makeSUSYGenEvt *
                                          ## Weight producer sequences
                                          process.eventWeightPU *
                                          process.weightProducer *
                                          process.btagEventWeightElJER *
                                          ## Selection sequences
                                          process.preselectionElHTMC2 * process.preselectionMC2PAT *  
                                          process.ElHadSelectionMETDown *
                                          process.electronSelection *
                                          process.jetSelectionJER *
                                          ## Analyzer Sequences
                                          process.analyzeSystematicsEl0bMETDown *
                                          process.analyzeSystematicsEl1bMETDown *
                                          process.analyzeSystematicsEl2bMETDown *
                                          process.analyzeSystematicsEl3bMETDown
                                          )

##  electron selection with smeared and scaled up jet energy corrections
process.RA4bElectronSelectionJECUp = cms.Path(process.PATTuple * ## Producer sequences
                                          process.scaledJetEnergyJECUp *
                                          process.createGoodLeptons *
                                          process.createGoodJetsJECUp *
                                          process.createGoodMETsJECUp *
                                          process.makeSUSYGenEvt *
                                          ## Weight producer sequences
                                          process.eventWeightPU *
                                          process.weightProducer *
                                          process.btagEventWeightElJER *
                                          ## Selection sequences
                                          process.preselectionElHTMC2 * process.preselectionMC2PAT *  
                                          process.ElHadSelectionJECUp *
                                          process.electronSelection *
                                          process.jetSelectionJECUp *
                                          ## Analyzer Sequences
                                          process.analyzeSystematicsEl0bJECUp *
                                          process.analyzeSystematicsEl1bJECUp *
                                          process.analyzeSystematicsEl2bJECUp *
                                          process.analyzeSystematicsEl3bJECUp
                                          )

##  electron selection with smeared and scaled down jet energy corrections
process.RA4bElectronSelectionJECDown = cms.Path(process.PATTuple * ## Producer sequences
                                          process.scaledJetEnergyJECDown *
                                          process.createGoodLeptons *
                                          process.createGoodJetsJECDown *
                                          process.createGoodMETsJECDown *
                                          process.makeSUSYGenEvt *
                                          ## Weight producer sequences
                                          process.eventWeightPU *
                                          process.weightProducer *
                                          process.btagEventWeightElJER *
                                          ## Selection sequences
                                          process.preselectionElHTMC2 * process.preselectionMC2PAT *  
                                          process.ElHadSelectionJECDown *
                                          process.electronSelection *
                                          process.jetSelectionJECDown *
                                          ## Analyzer Sequences
                                          process.analyzeSystematicsEl0bJECDown *
                                          process.analyzeSystematicsEl1bJECDown *
                                          process.analyzeSystematicsEl2bJECDown *
                                          process.analyzeSystematicsEl3bJECDown
                                          )

##  electron selection with smeared and scaled up jet energy resolution
process.RA4bElectronSelectionJERUp = cms.Path(process.PATTuple * ## Producer sequences
                                          process.scaledJetEnergyJERUp *
                                          process.createGoodLeptons *
                                          process.createGoodJetsJERUp *
                                          process.createGoodMETsJERUp *
                                          process.makeSUSYGenEvt *
                                          ## Weight producer sequences
                                          process.eventWeightPU *
                                          process.weightProducer *
                                          process.btagEventWeightElJER *
                                          ## Selection sequences
                                          process.preselectionElHTMC2 * process.preselectionMC2PAT *  
                                          process.ElHadSelectionJERUp *
                                          process.electronSelection *
                                          process.jetSelectionJERUp *
                                          ## Analyzer Sequences
                                          process.analyzeSystematicsEl0bJERUp *
                                          process.analyzeSystematicsEl1bJERUp *
                                          process.analyzeSystematicsEl2bJERUp *
                                          process.analyzeSystematicsEl3bJERUp
                                          )

##  electron selection with smeared and scaled down jet energy resolution
process.RA4bElectronSelectionJERDown = cms.Path(process.PATTuple * ## Producer sequences
                                          process.scaledJetEnergyJERDown *
                                          process.createGoodLeptons *
                                          process.createGoodJetsJERDown *
                                          process.createGoodMETsJERDown *
                                          process.makeSUSYGenEvt *
                                          ## Weight producer sequences
                                          process.eventWeightPU *
                                          process.weightProducer *
                                          process.btagEventWeightElJER *
                                          ## Selection sequences
                                          process.preselectionElHTMC2 * process.preselectionMC2PAT *  
                                          process.ElHadSelectionJERDown *
                                          process.electronSelection *
                                          process.jetSelectionJERDown *
                                          ## Analyzer Sequences
                                          process.analyzeSystematicsEl0bJERDown *
                                          process.analyzeSystematicsEl1bJERDown *
                                          process.analyzeSystematicsEl2bJERDown *
                                          process.analyzeSystematicsEl3bJERDown 
                                          )








## muon selection w/o scaled jet energy
#rocess.RA4bMuonSelection = cms.Path(## Producer sequences
#                                    process.createAllObjects *
#                                    process.btagEventWeightMu *
#                                    process.btagEventWeightMuBtagSFUp *
#                                    process.btagEventWeightMuBtagSFDown *
#                                    process.btagEventWeightMuMistagSFUp *
#                                    process.btagEventWeightMuMistagSFDown *
#                                    ## Selection sequences
#                                    process.preselectionMC2PAT*
#                                    process.preselectionMuHTMC2 *
#                                    process.MuHadSelection *
#                                    process.muonSelection*
#                                    process.jetSelection *
#                                    ## Analyzer Sequences for Mu 0 btags
#                                    process.analyzeSystematicsMu0b *
#                                    process.analyzeSystematicsMu0bMETUp *
#                                    process.analyzeSystematicsMu0bMETDown *
#                                    process.analyzeSystematicsMu0bBtagSFUp *
#                                    process.analyzeSystematicsMu0bBtagSFDown *
#                                    process.analyzeSystematicsMu0bMistagSFUp *
#                                    process.analyzeSystematicsMu0bMistagSFDown *
#                                    process.analyzeSystematicsMu0bPUUp *
#                                    process.analyzeSystematicsMu0bPUDown *
#                                    ## Analyzer Sequences for Mu 1 btags
#                                    process.analyzeSystematicsMu1b *
#                                    process.analyzeSystematicsMu1bMETUp *
#                                    process.analyzeSystematicsMu1bMETDown *
#                                    process.analyzeSystematicsMu1bBtagSFUp *
#                                    process.analyzeSystematicsMu1bBtagSFDown *
#                                    process.analyzeSystematicsMu1bMistagSFUp *
#                                    process.analyzeSystematicsMu1bMistagSFDown *
#                                    process.analyzeSystematicsMu1bPUUp *
#                                    process.analyzeSystematicsMu1bPUDown *
#                                    ## Analyzer Sequences for Mu 2 btags
#                                    process.analyzeSystematicsMu2b *
#                                    process.analyzeSystematicsMu2bMETUp *
#                                    process.analyzeSystematicsMu2bMETDown *
#                                    process.analyzeSystematicsMu2bBtagSFUp *
#                                    process.analyzeSystematicsMu2bBtagSFDown *
#                                    process.analyzeSystematicsMu2bMistagSFUp *
#                                    process.analyzeSystematicsMu2bMistagSFDown *
#                                    process.analyzeSystematicsMu2bPUUp *
#                                    process.analyzeSystematicsMu2bPUDown *
#                                    ## Analyzer Sequences for Mu 3 btags
#                                    process.analyzeSystematicsMu3b *
#                                    process.analyzeSystematicsMu3bMETUp *
#                                    process.analyzeSystematicsMu3bMETDown *
#                                    process.analyzeSystematicsMu3bBtagSFUp *
#                                    process.analyzeSystematicsMu3bBtagSFDown *
#                                    process.analyzeSystematicsMu3bMistagSFUp *
#                                    process.analyzeSystematicsMu3bMistagSFDown *
#                                    process.analyzeSystematicsMu3bPUUp *
#                                    process.analyzeSystematicsMu3bPUDown
#                                    )
#
##  muon selection w/o with scaled up jet energy corrections
#rocess.RA4bMuonSelectionJECUp = cms.Path(## Producer sequences
#                                         process.createAllObjects *
#                                         process.btagEventWeightMu *
#                                         ## Selection sequences
#                                         process.preselectionMC2PAT*
#                                         process.preselectionMuHTMC2 *
#                                         process.MuHadSelectionJECUp *
#                                         process.muonSelection*
#                                         process.jetSelectionJECUp*
#                                         ## Analyzer Sequence
#                                         process.analyzeSystematicsMu0bJECUp *
#                                         process.analyzeSystematicsMu1bJECUp *
#                                         process.analyzeSystematicsMu2bJECUp *
#                                         process.analyzeSystematicsMu3bJECUp
#                                         )
#
##  muon selection w/o with scaled down jet energy corrections
#rocess.RA4bMuonSelectionJECDown = cms.Path(## Producer sequences
#                                           process.createAllObjects *
#                                           process.btagEventWeightMu *
#                                           ## Selection sequences
#                                           process.preselectionMC2PAT *
#                                           process.preselectionMuHTMC2 *
#                                           process.MuHadSelectionJECDown *
#                                           process.muonSelection*
#                                           process.jetSelectionJECDown*
#                                           ## Analyzer Sequence
#                                           process.analyzeSystematicsMu0bJECDown *
#                                           process.analyzeSystematicsMu1bJECDown *
#                                           process.analyzeSystematicsMu2bJECDown *
#                                           process.analyzeSystematicsMu3bJECDown
#                                           )
#
##  muon selection w/o with scaled up jet energy resolution
#rocess.RA4bMuonSelectionJERUp = cms.Path(## Producer sequences
#                                         process.createAllObjects * 
#                                         process.btagEventWeightMu *
#                                         ## Selection sequences
#                                         process.preselectionMC2PAT* 
#                                         process.preselectionMuHTMC2 *
#                                         process.MuHadSelectionJERUp *
#                                         process.muonSelection*
#                                         process.jetSelectionJERUp*
#                                         ## Analyzer Sequence
#                                         process.analyzeSystematicsMu0bJERUp *
#                                         process.analyzeSystematicsMu1bJERUp *
#                                         process.analyzeSystematicsMu2bJERUp *
#                                         process.analyzeSystematicsMu3bJERUp
#                                         )
#
##  muon selection w/o with scaled down jet energy resolution
#rocess.RA4bMuonSelectionJERDown = cms.Path(## Producer sequences
#                                           process.createAllObjects *
#                                           process.btagEventWeightMu *
#                                           ## Selection sequences
#                                           process.preselectionMC2PAT* 
#                                           process.preselectionMuHTMC2 *
#                                           process.MuHadSelectionJERDown *
#                                           process.muonSelection*
#                                           process.jetSelectionJERDown*
#                                           ## Analyzer Sequence
#                                           process.analyzeSystematicsMu0bJERDown *
#                                           process.analyzeSystematicsMu1bJERDown *
#                                           process.analyzeSystematicsMu2bJERDown *
#                                           process.analyzeSystematicsMu3bJERDown
#                                           )
#
#
