import FWCore.ParameterSet.Config as cms

process = cms.Process("Daniel") 

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.MessageLogger.categories.append('ParticleListDrawer')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000),
    skipEvents = cms.untracked.uint32(0)
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('Bjets.root')
                                   )

process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = cms.string('START42_V13::All')

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_10_2_DWR.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_11_2_bZK.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_12_2_33F.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_13_2_WxO.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_14_2_Vnk.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_15_2_UoD.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_16_2_MKR.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_17_2_GHI.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_18_2_x61.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_19_2_bKs.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_1_2_pMS.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_20_2_2NX.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_21_2_cRh.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_22_2_Tcn.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_23_2_unu.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_24_2_ihv.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_25_2_29N.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_26_2_umf.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_27_2_kIn.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_28_2_zqm.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_29_2_fEJ.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_2_2_KZW.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_30_2_i0C.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_31_2_0ux.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_3_2_275.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_4_2_yOX.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_5_2_nQr.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_6_2_qVT.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_7_2_wxo.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_8_2_omT.root',
    '/store/user/fcostanz/LM9_SUSY_sftsht_7TeV-pythia6/LM9_Summer2011/7775abddf4cecee1ba70f412bba59ece/Summer11_9_2_UPY.root'
    )
 )

#------------------------------------------------------------------------------------------------------------------------
# Load modules to create SUSY Gen Event and TtGenEvent
#
# Note: To create the TtGenEvent for non-SM samples, a small modification in the TQAF is needed:
# - Checkout TopQuarkAnalysis/TopEventProducers  (for CMSSW_4_1_4: cvs co -r V06-07-11 TopQuarkAnalysis/TopEventProducers)
# - replace in the constructor of TopQuarkAnalysis/TopEventProducers/src/TopDecaySubset.cc "kStart" by "kPythia"
#-----------------------------------------------------------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYEventProducers.sequences.SUSYGenEvent_cff")

#------------------------------------------------------
# Import modules to filter events on generator level 
#------------------------------------------------------

from SUSYAnalysis.SUSYEventProducers.producers.SUSYGenEvtFilter_cfi import *

process.GluinoGluinoFilter = SUSYGenEventFilter.clone(cut='GluinoGluinoDecay()')
process.GluinoGluinoVeto   = SUSYGenEventFilter.clone(cut='!GluinoGluinoDecay()')

process.GluinoGluino0TopFilter = SUSYGenEventFilter.clone(cut='GluinoGluinoDecay() &&  numberOfTops()==0')
process.GluinoGluino1TopFilter = SUSYGenEventFilter.clone(cut='GluinoGluinoDecay() &&  numberOfTops()==1')
process.GluinoGluino2TopFilter = SUSYGenEventFilter.clone(cut='GluinoGluinoDecay() &&  numberOfTops()>1' )

process.GluinoGluino0LepFilter = SUSYGenEventFilter.clone(cut='GluinoGluinoDecay() &&  numberOfLeptons()==0')
process.GluinoGluino1LepFilter = SUSYGenEventFilter.clone(cut='GluinoGluinoDecay() &&  numberOfLeptons()==1')
process.GluinoGluino2LepFilter = SUSYGenEventFilter.clone(cut='GluinoGluinoDecay() &&  numberOfLeptons()>1' )

#-----------------------------------------------------------------
# Load modules for preselection
#-----------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.Preselection_cff")

#-----------------------------------------------------------------
# Load modules to create objects and filter events on reco level
#-----------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.BjetsSelection_cff")

#----------------------------------------------------------------------------------------
# Load modules for analysis on generator level, level of matched objects and reco-level
#-----------------------------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYAnalyzer.GluinoAnalyzer_cfi")

process.analyzeAll              = process.analyzeGluino.clone()
process.analyzeGluinoGluino     = process.analyzeGluino.clone()
process.analyzeGluinoGluinoVeto = process.analyzeGluino.clone()

process.analyzeGluinoGluino0Top = process.analyzeGluino.clone()
process.analyzeGluinoGluino1Top = process.analyzeGluino.clone()
process.analyzeGluinoGluino2Top = process.analyzeGluino.clone()

process.analyzeGluinoGluino0Lep = process.analyzeGluino.clone()
process.analyzeGluinoGluino1Lep = process.analyzeGluino.clone()
process.analyzeGluinoGluino2Lep = process.analyzeGluino.clone()

#-------------------------------------------------
# Load and configure module for event weighting
#-------------------------------------------------

process.load("TopAnalysis.TopUtils.EventWeightPU_cfi")
process.eventWeightPU.DataFile = "TopAnalysis/TopUtils/data/Data_PUDist_160404-163869_7TeV_May10ReReco_Collisions11_v2_and_165088-167913_7TeV_PromptReco_Collisions11.root"

process.load("SUSYAnalysis.SUSYEventProducers.WeightProducer_cfi")

#-------------------------------------------------
# Temporary
#-------------------------------------------------

## produce printout of particle listings (for debugging)
process.load("TopQuarkAnalysis.TopEventProducers.sequences.printGenParticles_cff")

#--------------------------
# selection paths
#--------------------------

process.all = cms.Path(process.makeObjects *
                       process.makeSUSYGenEvt *
                       process.eventWeightPU *
                       process.weightProducer *
                       process.jetSelection *
                       process.analyzeAll
                       )

process.GluinoGluino = cms.Path(process.makeObjects *
                                process.makeSUSYGenEvt *
                                process.eventWeightPU *
                                process.weightProducer *
                                process.jetSelection *
                                process.GluinoGluinoFilter *
                                #process.printGenParticles *
                                process.analyzeGluinoGluino
                                )

process.Other = cms.Path(process.makeObjects *
                         process.makeSUSYGenEvt *
                         process.eventWeightPU *
                         process.weightProducer *
                         process.jetSelection *
                         process.GluinoGluinoVeto *
                         process.analyzeGluinoGluinoVeto
                         )

process.GluinoGluino0Top = cms.Path(process.makeObjects *
                                    process.makeSUSYGenEvt *
                                    process.eventWeightPU *
                                    process.weightProducer *
                                    process.jetSelection *
                                    process.GluinoGluino0TopFilter *
                                    process.analyzeGluinoGluino0Top
                                    )

process.GluinoGluino1Top = cms.Path(process.makeObjects *
                                    process.makeSUSYGenEvt *
                                    process.eventWeightPU *
                                    process.weightProducer *
                                    process.jetSelection *
                                    process.GluinoGluino1TopFilter *
                                    process.analyzeGluinoGluino1Top
                                    )

process.GluinoGluino2Top = cms.Path(process.makeObjects *
                                    process.makeSUSYGenEvt *
                                    process.eventWeightPU *
                                    process.weightProducer *
                                    process.jetSelection *
                                    process.GluinoGluino2TopFilter *
                                    process.analyzeGluinoGluino2Top
                                    )


process.GluinoGluino0Lep = cms.Path(process.makeObjects *
                                    process.makeSUSYGenEvt *
                                    process.eventWeightPU *
                                    process.weightProducer *
                                    process.jetSelection *
                                    process.GluinoGluino0LepFilter *
                                    process.analyzeGluinoGluino0Lep
                                    )

process.GluinoGluino1Lep = cms.Path(process.makeObjects *
                                    process.makeSUSYGenEvt *
                                    process.eventWeightPU *
                                    process.weightProducer *
                                    process.jetSelection *
                                    process.GluinoGluino1LepFilter *
                                    process.analyzeGluinoGluino1Lep
                                    )

process.GluinoGluino2Lep = cms.Path(process.makeObjects *
                                    process.makeSUSYGenEvt *
                                    process.eventWeightPU *
                                    process.weightProducer *
                                    process.jetSelection *
                                    process.GluinoGluino2LepFilter *
                                    process.analyzeGluinoGluino2Lep
                                    )
