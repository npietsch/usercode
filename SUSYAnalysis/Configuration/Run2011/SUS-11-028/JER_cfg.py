import FWCore.ParameterSet.Config as cms

process = cms.Process("RA4b") 

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.MessageLogger.categories.append('ParticleListDrawer')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100000),
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


#------------------------------------------------------------------
# Load and configure module to smear jet energy on reco level
#------------------------------------------------------------------

from SUSYAnalysis.Uncertainties.JetEnergy_cfi import *
process.scaledJetEnergy = scaledJetEnergy.clone()
process.scaledJetEnergy.inputJets = "selectedPatJetsAK5PF"
process.scaledJetEnergy.inputMETs = "patMETsPF"
process.scaledJetEnergy.doJetSmearing = True

#------------------------------------------------------------------
# Load modules to create objects and filter events on reco level
#------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.BjetsSelection_cff")

# define source for goodJets producer
process.goodJets.src = "scaledJetEnergy:selectedPatJetsAK5PF"
process.goodMETs.src = "scaledJetEnergy:patMETsPF"

#------------------------------------------------------------------
# Load modules to create SUSYGenEvent
#------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYEventProducers.sequences.SUSYGenEvent_cff")

#---------------------------------------------------------------------------
# load and configure module to create TtGenEvent
#---------------------------------------------------------------------------

process.load("TopQuarkAnalysis.TopEventProducers.sequences.ttGenEvent_cff")
process.decaySubset.fillMode = "kME"

#---------------------------------------------------------------------------
# load and configure modules to filter on member functions of TtGenEvent
#---------------------------------------------------------------------------

process.load("TopQuarkAnalysis.TopEventProducers.producers.TtGenEvtFilter_cfi")

process.SemiLepTtGenEventFilter = process.ttGenEventFilter.clone(cut="semiLeptonicChannel()=1 || semiLeptonicChannel()=2")
process.DiLepTtGenEventFilter   = process.ttGenEventFilter.clone(cut="isFullLeptonic() && fullLeptonicChannel.first!=3 && fullLeptonicChannel.second!=3 ")
process.FullHadTtGenEventFilter = process.ttGenEventFilter.clone(cut="isFullHadronic()")
process.TauTtGenEventFilter     = process.ttGenEventFilter.clone(cut="semiLeptonicChannel()=3 || fullLeptonicChannel.first=3 || fullLeptonicChannel.second=3")

#------------------------------------------------------------------
# Load and configure modules for event weighting
#------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYEventProducers.WeightProducer_cfi")

process.load("TopAnalysis.TopUtils.EventWeightPU_cfi")

process.eventWeightPU.DataFile = "SUSYAnalysis/SUSYUtils/data/PU_Data_68000.root"

process.eventWeightPUUp = process.eventWeightPU.clone()
process.eventWeightPUUp.DataFile = "SUSYAnalysis/SUSYUtils/data/PU_Data_64600.root"

process.eventWeightPUDown = process.eventWeightPU.clone()
process.eventWeightPUDown.DataFile = "SUSYAnalysis/SUSYUtils/data/PU_Data_71400.root"

#------------------------------------------------------------------
# Load modules for preselection
#------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.Preselection_cff")

#------------------------------------------------------------------
# Load analyzer modules
#------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYAnalyzer.sequences.SUSYBjetsAnalysis_cff")

# clone and configure modules to monitor b-tag efficiency weighting
process.monitorBtagWeightingMu                    = process.analyzeSUSY.clone()
process.monitorBtagWeightingMu.useBtagEventWeight = True
process.monitorBtagWeightingMu.BtagEventWeights   = "btagEventWeightMuJER:RA4bEventWeights"
process.monitorBtagWeightingMu.BtagJetWeights     = "btagEventWeightMuJER:RA4bJetWeights"

process.monitorBtagWeightingMu_2 = process.monitorBtagWeightingMu.clone()
process.monitorBtagWeightingMu_3 = process.monitorBtagWeightingMu.clone()

process.monitorBtagWeightingEl                    = process.analyzeSUSY.clone()
process.monitorBtagWeightingEl.useBtagEventWeight = True
process.monitorBtagWeightingEl.BtagEventWeights   = "btagEventWeightElJER:RA4bEventWeights"
process.monitorBtagWeightingEl.BtagJetWeights     = "btagEventWeightElJER:RA4bJetWeights"

process.monitorBtagWeightingEl_2 = process.monitorBtagWeightingEl.clone()
process.monitorBtagWeightingEl_3 = process.monitorBtagWeightingEl.clone()

process.load("SUSYAnalysis.SUSYAnalyzer.RA4MuonAnalyzer_cfi")

process.analyzeRA4Muons.jets           = "goodJets"
process.analyzeRA4Muons.muons          = "looseMuons"
process.analyzeRA4Muons.electrons      = "goodElectrons"
process.analyzeRA4Muons.met            = "scaledJetEnergy:patMETsPF"
process.analyzeRA4Muons.PVSrc          = "goodVertices"
process.analyzeRA4Muons.useEventWeight = True

process.load("SUSYAnalysis.SUSYAnalyzer.RA4ElectronAnalyzer_cfi")

process.analyzeRA4Electrons.jets           = "goodJets"
process.analyzeRA4Electrons.muons          = "goodMuons"
process.analyzeRA4Electrons.electrons      = "looseElectrons"
process.analyzeRA4Electrons.met            = "scaledJetEnergy:patMETsPF"
process.analyzeRA4Electrons.PVSrc          = "goodVertices"
process.analyzeRA4Electrons.useEventWeight = True

#------------------------------------------------------------------
# Load and configure modules for b-tag efficiency weighting
#------------------------------------------------------------------

process.load("RecoBTag.PerformanceDB.PoolBTagPerformanceDB1107")
process.load("RecoBTag.PerformanceDB.BTagPerformanceDB1107")
process.load("Btagging.BtagWeightProducer.BtagEventWeight_cfi")

## common default settings (similar for muon and electron channel)
process.btagEventWeight           = process.btagEventWeight.clone()
process.btagEventWeight.bTagAlgo  = "TCHEM"
process.btagEventWeight.filename  = "../../../../SUSYAnalysis/SUSYUtils/data/TTJetsSummer11.root"

## create weights for muon selection
process.btagEventWeightMuJER                 = process.btagEventWeight.clone()
process.btagEventWeightMuJER.rootDir         = "RA4bMuTCHEM"
process.btagEventWeightMuJER.jets            = "goodJets"

## create weights for electron selection
process.btagEventWeightElJER                 = process.btagEventWeight.clone()
process.btagEventWeightElJER.rootDir         = "RA4bElTCHEM"
process.btagEventWeightElJER.jets            = "goodJets"

#--------------------------
# Selection paths
#--------------------------

## muon selection path
process.MuonSelection = cms.Path(# execute producer and preselection modules
                                 process.makeSUSYGenEvt *
                                 process.scaledJetEnergy *
                                 process.preselectionMuHTMC2 *
                                 process.makeObjects *
                                 process.eventWeightPU *
                                 process.weightProducer *
                                 
                                 # execute filter and analyzer modules
                                 process.analyzeSUSYBjets1m_noCuts *
                                 
                                 process.MuHadSelection *
                                 process.analyzeSUSYBjets1m_preselection *
                                 #process.analyzeRA4uons *
                                 
                                 process.muonSelection*
                                 process.analyzeSUSYBjets1m_leptonSelection *
                                 
                                 process.jetSelection*
                                 process.analyzeSUSYBjets1m_jetSelection *
                                 
                                 # execute b-tag producer modules and analyzer modules
                                 process.btagEventWeightMuJER *
                                 
                                 process.monitorBtagWeightingMu *
                                 process.analyzeSUSYBjets1b1m_1 *
                                 process.analyzeSUSYBjets2b1m_1 *
                                 process.analyzeSUSYBjets3b1m_1 *
                                 process.analyzeSUSYBjets0b1m_2 *
                                 process.analyzeSUSYBjets1b1m_2 *
                                 process.analyzeSUSYBjets2b1m_2                                   
                                 )

## electron selection path
process.ElectronSelection = cms.Path(# execute producer and preselection modules
                                     process.makeSUSYGenEvt *
                                     process.scaledJetEnergy *
                                     process.preselectionElHTMC2 *
                                     process.makeObjects *
                                     process.eventWeightPU *
                                     process.weightProducer *
                                     
                                     # execute filter and analyzer modules
                                     process.analyzeSUSYBjets1e_noCuts *
                                     
                                     process.ElHadSelection *
                                     process.analyzeSUSYBjets1e_preselection *
                                     process.analyzeRA4Electrons *
                                     
                                     process.electronSelection*
                                     process.analyzeSUSYBjets1e_leptonSelection *
                                     
                                     process.jetSelection*
                                     process.analyzeSUSYBjets1e_jetSelection *
                                     
                                     # execute b-tag producer modules and analyzer modules
                                     process.btagEventWeightElJER *
                                     
                                     process.monitorBtagWeightingEl *
                                     process.analyzeSUSYBjets1b1e_1 *
                                     process.analyzeSUSYBjets2b1e_1 *
                                     process.analyzeSUSYBjets3b1e_1 *
                                     process.analyzeSUSYBjets0b1e_2 *
                                     process.analyzeSUSYBjets1b1e_2 *
                                     process.analyzeSUSYBjets2b1e_2                                   
                                     )

## muon selection path for SemiLep TTJets
process.MuonSelection_SemiLep = cms.Path(# execute producer and preselection modules
                                         process.makeGenEvt *
                                         process.makeSUSYGenEvt *
                                         process.SemiLepTtGenEventFilter *
                                         process.scaledJetEnergy *
                                         process.preselectionMuHTMC2 *
                                         process.makeObjects *
                                         process.eventWeightPU *
                                         process.weightProducer *
                                         
                                         # execute filter and analyzer modules
                                         process.analyzeSUSY1m_noCuts_SemiLep *
                                 
                                         #process.MuHadSelection *
                                         process.analyzeSUSY1m_preselection_SemiLep *
                                         #process.analyzeRA4Muons *
                                         
                                         process.muonSelection*
                                         process.analyzeSUSY1m_leptonSelection_SemiLep *
                                         
                                         process.threeGoodJets*
                                         process.analyzeSUSY1m_jetSelection_SemiLep *
                                         
                                         process.filterMediumHT *
                                         process.analyzeSUSY1m_HTSelection_SemiLep *
                                                                                   
                                         process.oneMediumMET *
                                         process.analyzeSUSY1m_METSelection_SemiLep
                                         )

## electron selection path for SemiLep TTJets
process.ElectronSelection_SemiLep = cms.Path(# execute producer and preselection modules
                                             process.makeGenEvt *
                                             process.makeSUSYGenEvt *
                                             process.SemiLepTtGenEventFilter *
                                             process.scaledJetEnergy *
                                             process.preselectionElHTMC2 *
                                             process.makeObjects *
                                             process.eventWeightPU *
                                             process.weightProducer *
                                             
                                             # execute filter and analyzer modules
                                             process.analyzeSUSY1e_noCuts_SemiLep *
                                             
                                             #process.ElHadSelection *
                                             process.analyzeSUSY1e_preselection_SemiLep *
                                             process.analyzeRA4Electrons *
                                             
                                             process.electronSelection*
                                             process.analyzeSUSY1e_leptonSelection_SemiLep *
                                             
                                             process.threeGoodJets*
                                             process.analyzeSUSY1e_jetSelection_SemiLep *
                                             
                                             process.filterMediumHT *
                                             process.analyzeSUSY1e_HTSelection_SemiLep *
                                             
                                             process.oneMediumMET *
                                             process.analyzeSUSY1e_METSelection_SemiLep
                                             )


## muon selection path for DiLep TTJets
process.MuonSelection_DiLep = cms.Path(# execute producer and preselection modules
                                       process.makeGenEvt *
                                       process.makeSUSYGenEvt *
                                       process.DiLepTtGenEventFilter *
                                       process.scaledJetEnergy *
                                       process.preselectionMuHTMC2 *
                                       process.makeObjects *
                                       process.eventWeightPU *
                                       process.weightProducer *
                                       
                                       # execute filter and analyzer modules
                                       process.analyzeSUSY1m_noCuts_DiLep *
                                       
                                       #process.MuHadSelection *
                                       process.analyzeSUSY1m_preselection_DiLep *
                                       #process.analyzeRA4Muons *
                                       
                                       process.muonSelection*
                                       process.analyzeSUSY1m_leptonSelection_DiLep *
                                       
                                       process.threeGoodJets*
                                       process.analyzeSUSY1m_jetSelection_DiLep *
                                          
                                       process.filterMediumHT *
                                       process.analyzeSUSY1m_HTSelection_DiLep *
                                       
                                       process.oneMediumMET *
                                       process.analyzeSUSY1m_METSelection_DiLep
                                       )

## electron selection path for DiLep TTJets
process.ElectronSelection_DiLep = cms.Path(# execute producer and preselection modules
                                           process.makeGenEvt *
                                           process.makeSUSYGenEvt *
                                           process.DiLepTtGenEventFilter *
                                           process.scaledJetEnergy *
                                           process.preselectionElHTMC2 *
                                           process.makeObjects *
                                           process.eventWeightPU *
                                           process.weightProducer *
                                           
                                           # execute filter and analyzer modules
                                           process.analyzeSUSY1e_noCuts_DiLep *
                                           
                                           #process.ElHadSelection *
                                           process.analyzeSUSY1e_preselection_DiLep *
                                           process.analyzeRA4Electrons *
                                           
                                           process.electronSelection*
                                           process.analyzeSUSY1e_leptonSelection_DiLep *
                                           
                                           process.threeGoodJets*
                                           process.analyzeSUSY1e_jetSelection_DiLep *
                                          
                                           process.filterMediumHT *
                                           process.analyzeSUSY1e_HTSelection_DiLep *
                                           
                                           process.oneMediumMET *
                                           process.analyzeSUSY1e_METSelection_DiLep
                                           )


## muon selection path for FullHad TTJets
process.MuonSelection_FullHad = cms.Path(# execute producer and preselection modules
                                         process.makeGenEvt *
                                         process.makeSUSYGenEvt *
                                         process.FullHadTtGenEventFilter *
                                         process.scaledJetEnergy *
                                         process.preselectionMuHTMC2 *
                                         process.makeObjects *
                                         process.eventWeightPU *
                                         process.weightProducer *
                                         
                                         # execute filter and analyzer modules
                                         process.analyzeSUSY1m_noCuts_FullHad *
                                 
                                         #process.MuHadSelection *
                                         process.analyzeSUSY1m_preselection_FullHad *
                                         #process.analyzeRA4uons *
                                         
                                         process.muonSelection*
                                         process.analyzeSUSY1m_leptonSelection_FullHad *
                                         
                                         process.threeGoodJets*
                                         process.analyzeSUSY1m_jetSelection_FullHad *
                                         
                                         process.filterMediumHT *
                                         process.analyzeSUSY1m_HTSelection_FullHad *
                                         
                                         process.oneMediumMET *
                                         process.analyzeSUSY1m_METSelection_FullHad
                                         )

## electron selection path for FullHad TTJets
process.ElectronSelection_FullHad = cms.Path(# execute producer and preselection modules
                                             process.makeGenEvt *
                                             process.makeSUSYGenEvt *
                                             process.FullHadTtGenEventFilter *
                                             process.scaledJetEnergy *
                                             process.preselectionElHTMC2 *
                                             process.makeObjects *
                                             process.eventWeightPU *
                                             process.weightProducer *
                                             
                                             # execute filter and analyzer modules
                                             process.analyzeSUSY1e_noCuts_FullHad *
                                             
                                             #process.ElHadSelection *
                                             process.analyzeSUSY1e_preselection_FullHad *
                                             process.analyzeRA4Electrons *
                                             
                                             process.electronSelection*
                                             process.analyzeSUSY1e_leptonSelection_FullHad *
                                             
                                             process.threeGoodJets*
                                             process.analyzeSUSY1e_jetSelection_FullHad *
                                          
                                             process.filterMediumHT *
                                             process.analyzeSUSY1e_HTSelection_FullHad *
                                             
                                             process.oneMediumMET *
                                             process.analyzeSUSY1e_METSelection_FullHad
                                             )


## muon selection path for Tau TTJets
process.MuonSelection_Tau = cms.Path(# execute producer and preselection modules
                                     process.makeGenEvt *
                                     process.makeSUSYGenEvt *
                                     process.TauTtGenEventFilter *
                                     process.scaledJetEnergy *
                                     process.preselectionMuHTMC2 *
                                     process.makeObjects *
                                     process.eventWeightPU *
                                     process.weightProducer *
                                     
                                     # execute filter and analyzer modules
                                     process.analyzeSUSY1m_noCuts_Tau *
                                     
                                     #process.MuHadSelection *
                                     process.analyzeSUSY1m_preselection_Tau *
                                     #process.analyzeRA4uons *
                                     
                                     process.muonSelection*
                                     process.analyzeSUSY1m_leptonSelection_Tau *
                                     
                                     process.threeGoodJets*
                                     process.analyzeSUSY1m_jetSelection_Tau *
                                     
                                     process.filterMediumHT *
                                     process.analyzeSUSY1m_HTSelection_Tau *
                                     
                                     process.oneMediumMET *
                                     process.analyzeSUSY1m_METSelection_Tau
                                     )

## electron selection path for Tau TTJets
process.ElectronSelection_Tau = cms.Path(# execute producer and preselection modules
                                         process.makeGenEvt *
                                         process.makeSUSYGenEvt *
                                         process.TauTtGenEventFilter *
                                         process.scaledJetEnergy *
                                         process.preselectionElHTMC2 *
                                         process.makeObjects *
                                         process.eventWeightPU *
                                         process.weightProducer *
                                         
                                         # execute filter and analyzer modules
                                         process.analyzeSUSY1e_noCuts_Tau *
                                         
                                         #process.ElHadSelection *
                                         process.analyzeSUSY1e_preselection_Tau *
                                         process.analyzeRA4Electrons *
                                         
                                         process.electronSelection*
                                         process.analyzeSUSY1e_leptonSelection_Tau *
                                         
                                         process.threeGoodJets*
                                         process.analyzeSUSY1e_jetSelection_Tau *
                                          
                                         process.filterMediumHT *
                                         process.analyzeSUSY1e_HTSelection_Tau *
                                         
                                         process.oneMediumMET *
                                         process.analyzeSUSY1e_METSelection_Tau
                                         )

## lepton selection path for all SemiLep TTJets
process.LeptonSelection_SemiLep = cms.Path(# execute producer and preselection modules
                                          process.makeGenEvt *
                                          process.makeSUSYGenEvt *
                                          process.SemiLepTtGenEventFilter *
                                          process.scaledJetEnergy *
                                          process.preselectionLepHTMC2 *
                                          process.makeObjects *
                                          process.eventWeightPU *
                                          process.weightProducer *
                                          
                                          # execute filter and analyzer modules
                                          process.analyzeSUSY1l_noCuts_SemiLep *
                                          process.analyzeTtGenEvent1l_noCuts_SemiLep *

                                          ##process.LepHadSelection *
                                          process.analyzeSUSY1l_preselection_SemiLep *
                                          process.analyzeTtGenEvent1l_preselection_SemiLep *
                                                                                    
                                          process.leptonSelection *
                                          process.analyzeSUSY1l_leptonSelection_SemiLep *
                                          process.analyzeTtGenEvent1l_leptonSelection_SemiLep *
                                          
                                          process.threeGoodJets *
                                          process.analyzeSUSY1l_jetSelection_SemiLep *
                                          process.analyzeTtGenEvent1l_jetSelection_SemiLep *
                                          
                                          process.filterMediumHT *
                                          process.analyzeSUSY1l_HTSelection_SemiLep *
                                          process.analyzeTtGenEvent1l_HTSelection_SemiLep *
                                          
                                          process.oneMediumMET *
                                          process.analyzeSUSY1l_METSelection_SemiLep *
                                          process.analyzeTtGenEvent1l_METSelection_SemiLep
                                          )

## lepton selection path for all TTJets
process.LeptonSelection_TTJets = cms.Path(# execute producer and preselection modules
                                          process.makeGenEvt *
                                          process.makeSUSYGenEvt *
                                          process.scaledJetEnergy *
                                          process.preselectionLepHTMC2 *
                                          process.makeObjects *
                                          process.eventWeightPU *
                                          process.weightProducer *
                                                                                    
                                          # execute filter and analyzer modules
                                          process.analyzeSUSY1l_noCuts_TTJets *
                                          #process.analyzeTtGenEvent1l_noCuts_TTJets *

                                          ##process.LepHadSelection *
                                          process.analyzeSUSY1l_preselection_TTJets *
                                          #process.analyzeTtGenEvent1l_preselection_TTJets *
                                                                                    
                                          process.leptonSelection *
                                          process.analyzeSUSY1l_leptonSelection_TTJets *
                                          process.analyzeTtGenEvent1l_leptonSelection_TTJets *
                                          
                                          process.threeGoodJets *
                                          process.analyzeSUSY1l_jetSelection_TTJets *
                                          #process.analyzeTtGenEvent1l_jetSelection_TTJets *
                                          
                                          process.filterMediumHT *
                                          process.analyzeSUSY1l_HTSelection_TTJets *
                                          #process.analyzeTtGenEvent1l_HTSelection_TTJets *
                                          
                                          process.oneMediumMET *
                                          process.analyzeSUSY1l_METSelection_TTJets #*
                                          #process.analyzeTtGenEvent1l_METSelection_TTJets
                                          )


#--------------------------
# TEMP
#--------------------------

process.scaledJetEnergy00 = process.scaledJetEnergy.clone()
process.scaledJetEnergy10 = process.scaledJetEnergy.clone()
process.scaledJetEnergy20 = process.scaledJetEnergy.clone()
process.scaledJetEnergy30 = process.scaledJetEnergy.clone()
process.scaledJetEnergy40 = process.scaledJetEnergy.clone()
process.scaledJetEnergy50 = process.scaledJetEnergy.clone()

process.scaledJetEnergy00.resolutionFactors = 1.0,  1.0,  1.0
process.scaledJetEnergy10.resolutionFactors = 1.25, 1.25, 1.25
process.scaledJetEnergy20.resolutionFactors = 1.5,  1.5,  1.5
process.scaledJetEnergy30.resolutionFactors = 1.75, 1.75, 1.75
process.scaledJetEnergy40.resolutionFactors = 2.0,  2.0,  2.0
process.scaledJetEnergy50.resolutionFactors = 2.25, 2.25, 2.25

process.goodJets00   = process.goodJets.clone(src = "scaledJetEnergy00:selectedPatJetsAK5PF")
process.goodJets10   = process.goodJets.clone(src = "scaledJetEnergy10:selectedPatJetsAK5PF")
process.goodJets20   = process.goodJets.clone(src = "scaledJetEnergy20:selectedPatJetsAK5PF")
process.goodJets30   = process.goodJets.clone(src = "scaledJetEnergy30:selectedPatJetsAK5PF")
process.goodJets40   = process.goodJets.clone(src = "scaledJetEnergy40:selectedPatJetsAK5PF")
process.goodJets50   = process.goodJets.clone(src = "scaledJetEnergy50:selectedPatJetsAK5PF")

process.analyzeSUSY1l_leptonSelection_JER00 = process.analyzeSUSY1l_leptonSelection_TTJets.clone()
process.analyzeSUSY1l_leptonSelection_JER10 = process.analyzeSUSY1l_leptonSelection_TTJets.clone()
process.analyzeSUSY1l_leptonSelection_JER20 = process.analyzeSUSY1l_leptonSelection_TTJets.clone()
process.analyzeSUSY1l_leptonSelection_JER30 = process.analyzeSUSY1l_leptonSelection_TTJets.clone()
process.analyzeSUSY1l_leptonSelection_JER40 = process.analyzeSUSY1l_leptonSelection_TTJets.clone()
process.analyzeSUSY1l_leptonSelection_JER50 = process.analyzeSUSY1l_leptonSelection_TTJets.clone()

process.analyzeSUSY1l_leptonSelection_JER00.jets = "goodJets00"
process.analyzeSUSY1l_leptonSelection_JER00.met  = "scaledJetEnergy00:patMETsPF"

process.analyzeSUSY1l_leptonSelection_JER10.jets = "goodJets10"
process.analyzeSUSY1l_leptonSelection_JER10.met  = "scaledJetEnergy10:patMETsPF"

process.analyzeSUSY1l_leptonSelection_JER20.jets = "goodJets20"
process.analyzeSUSY1l_leptonSelection_JER20.met  = "scaledJetEnergy20:patMETsPF"

process.analyzeSUSY1l_leptonSelection_JER30.jets = "goodJets30"
process.analyzeSUSY1l_leptonSelection_JER30.met  = "scaledJetEnergy30:patMETsPF"

process.analyzeSUSY1l_leptonSelection_JER40.jets = "goodJets40"
process.analyzeSUSY1l_leptonSelection_JER40.met  = "scaledJetEnergy40:patMETsPF"

process.analyzeSUSY1l_leptonSelection_JER50.jets = "goodJets50"
process.analyzeSUSY1l_leptonSelection_JER50.met  = "scaledJetEnergy50:patMETsPF"


process.analyzeSUSY1l_HTSelection_JER00 = process.analyzeSUSY1l_leptonSelection_JER00.clone()
process.analyzeSUSY1l_HTSelection_JER10 = process.analyzeSUSY1l_leptonSelection_JER10.clone()
process.analyzeSUSY1l_HTSelection_JER20 = process.analyzeSUSY1l_leptonSelection_JER20.clone()
process.analyzeSUSY1l_HTSelection_JER30 = process.analyzeSUSY1l_leptonSelection_JER30.clone()
process.analyzeSUSY1l_HTSelection_JER40 = process.analyzeSUSY1l_leptonSelection_JER40.clone()
process.analyzeSUSY1l_HTSelection_JER50 = process.analyzeSUSY1l_leptonSelection_JER50.clone()

process.analyzeSUSY1l_METSelection_JER00 = process.analyzeSUSY1l_leptonSelection_JER00.clone()
process.analyzeSUSY1l_METSelection_JER10 = process.analyzeSUSY1l_leptonSelection_JER10.clone()
process.analyzeSUSY1l_METSelection_JER20 = process.analyzeSUSY1l_leptonSelection_JER20.clone()
process.analyzeSUSY1l_METSelection_JER30 = process.analyzeSUSY1l_leptonSelection_JER30.clone()
process.analyzeSUSY1l_METSelection_JER40 = process.analyzeSUSY1l_leptonSelection_JER40.clone()
process.analyzeSUSY1l_METSelection_JER50 = process.analyzeSUSY1l_leptonSelection_JER50.clone()

## lepton selection path with JER smeared by different amounts
process.LeptonSelection_JER = cms.Path(# execute producer and preselection modules
                                       process.makeGenEvt *
                                       process.makeSUSYGenEvt *
                                       process.scaledJetEnergy *
                                       process.preselectionLepHTMC2 *
                                       process.makeObjects *
                                       process.eventWeightPU *
                                       process.weightProducer *

                                       process.scaledJetEnergy00 *
                                       process.scaledJetEnergy10 *
                                       process.scaledJetEnergy20 *
                                       process.scaledJetEnergy30 *
                                       process.scaledJetEnergy40 *
                                       process.scaledJetEnergy50 *

                                       process.goodJets00 *
                                       process.goodJets10 *
                                       process.goodJets20 *
                                       process.goodJets30 *
                                       process.goodJets40 *
                                       process.goodJets50 *
                                       
                                       # execute filter and analyzer modules
                                       process.leptonSelection *
                                       
                                       process.analyzeSUSY1l_leptonSelection_JER00 *
                                       process.analyzeSUSY1l_leptonSelection_JER10 *
                                       process.analyzeSUSY1l_leptonSelection_JER20 *
                                       process.analyzeSUSY1l_leptonSelection_JER30 *
                                       process.analyzeSUSY1l_leptonSelection_JER40 *
                                       process.analyzeSUSY1l_leptonSelection_JER50 *
                                       
                                       process.threeGoodJets *
                                                                                                                     
                                       process.filterMediumHT *
                                       
                                       process.analyzeSUSY1l_HTSelection_JER00 *
                                       process.analyzeSUSY1l_HTSelection_JER10 *
                                       process.analyzeSUSY1l_HTSelection_JER20 *
                                       process.analyzeSUSY1l_HTSelection_JER30 *
                                       process.analyzeSUSY1l_HTSelection_JER40 *
                                       process.analyzeSUSY1l_HTSelection_JER50 *
                                       
                                       process.oneMediumMET *
                                       
                                       process.analyzeSUSY1l_METSelection_JER00 *
                                       process.analyzeSUSY1l_METSelection_JER10 *
                                       process.analyzeSUSY1l_METSelection_JER20 *
                                       process.analyzeSUSY1l_METSelection_JER30 *
                                       process.analyzeSUSY1l_METSelection_JER40 *
                                       process.analyzeSUSY1l_METSelection_JER50 
                                       )
