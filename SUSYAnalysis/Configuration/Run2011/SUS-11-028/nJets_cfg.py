import FWCore.ParameterSet.Config as cms

process = cms.Process("nJets") 

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
                                   fileName = cms.string('nJets.root')
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
# Load and configure modules to create SUSYGenEvent and SUSYEvent
#------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYEventProducers.sequences.SUSYGenEvent_cff")
process.load("SUSYAnalysis.SUSYEventProducers.producers.SUSYEventProducer_cfi")

process.SUSYEvt.muons     = "goodMuons"
process.SUSYEvt.electrons = "goodElectrons"
process.SUSYEvt.jets      = "goodJets"
process.SUSYEvt.mets      = "scaledJetEnergy:patMETsPF"

#---------------------------------------------------------------------------
# load and configure module to create TtGenEvent
#---------------------------------------------------------------------------

process.load("TopQuarkAnalysis.TopEventProducers.sequences.ttGenEvent_cff")
process.decaySubset.fillMode = "kME"

#------------------------------------------------------------------
# Load and configure modules for event weighting
#------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYEventProducers.WeightProducer_cfi")

process.load("TopAnalysis.TopUtils.EventWeightPU_cfi")

process.eventWeightPU.DataFile = "SUSYAnalysis/SUSYUtils/data/PU_Data_73500.root"

process.eventWeightPUUp = process.eventWeightPU.clone()
process.eventWeightPUUp.DataFile = "SUSYAnalysis/SUSYUtils/data/PU_Data_79380.root"

process.eventWeightPUDown = process.eventWeightPU.clone()
process.eventWeightPUDown.DataFile = "SUSYAnalysis/SUSYUtils/data/PU_Data_67620.root"

#------------------------------------------------------------------
# Load modules for preselection
#------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.Preselection_cff")

#------------------------------------------------------------------
# Load analyzer modules
#------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYAnalyzer.sequences.Correlation_cff")

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

## lepton selection path for all TTJets
process.LeptonSelection_TTJets = cms.Path(# execute producer and preselection modules
                                          process.makeGenEvt *
                                          process.makeSUSYGenEvt *
                                          process.scaledJetEnergy *
                                          process.preselectionLepHTMC2 *
                                          process.makeObjects *
                                          process.SUSYEvt *
                                          process.eventWeightPU *
                                          process.weightProducer *
                                          process.btagEventWeightMuJER *
                                          
                                          # execute filter and analyzer modules
                                          process.oneGoodLepton *
                                          
##                                           process.DiLeptonFilter *
##                                           process.filterLeptonPair *
                                          
                                          process.analyzeTtGenEvent1l_leptonSelection_TTJets *
                                          
                                          process.threeGoodJets *
                                          process.analyzeTtGenEvent1l_jetSelection_TTJets *

                                          process.analyzeCorrelation1l *

                                          process.filterMT *
                                          process.analyzeTtGenEvent1l_mTSelection_TTJets *
                                          
##                                           # execute analyzer modules for inclusive nJets cuts 
##                                           process.analyzeCorrelation1l_nJets3To4 *
##                                           process.analyzeCorrelation1l_nJets5To6 *
##                                           process.analyzeCorrelation1l_nJets7ToInf *

                                          # execute analyzer modules for inclusive HT cuts
                                          process.analyzeCorrelation1l_HT200ToInf *
                                          process.analyzeCorrelation1l_HT300ToInf *
                                          process.analyzeCorrelation1l_HT400ToInf *
                                          process.analyzeCorrelation1l_HT500ToInf *
                                          process.analyzeCorrelation1l_HT600ToInf *
                                          process.analyzeCorrelation1l_HT700ToInf *
                                          
##                                           # execute analyzer modules for exclusive HT cuts
##                                           process.analyzeCorrelation1l_HT200To300 *
                                          process.analyzeCorrelation1l_HT300To400 *
                                          process.analyzeCorrelation1l_HT400To500 *
                                          process.analyzeCorrelation1l_HT500To600 *
                                          process.analyzeCorrelation1l_HT600To700 *
                                          
                                          # execute analyzer modules for inclusive MET cuts
                                          process.analyzeCorrelation1l_MET0ToInf *
                                          process.analyzeCorrelation1l_MET50ToInf *
                                          process.analyzeCorrelation1l_MET100ToInf *
                                          process.analyzeCorrelation1l_MET150ToInf *
                                          process.analyzeCorrelation1l_MET200ToInf *
                                          process.analyzeCorrelation1l_MET250ToInf *

##                                           # execute analyzer modules for exclusive MET cuts
                                          process.analyzeCorrelation1l_MET0To50 *
                                          process.analyzeCorrelation1l_MET50To100 *
                                          process.analyzeCorrelation1l_MET100To150 *
                                          process.analyzeCorrelation1l_MET150To200 *
                                          process.analyzeCorrelation1l_MET200To250 *
                                          
                                          # execute analyzer modules for exclusive YMET cuts
                                          process.analyzeCorrelation1l_YMET10To15 *
                                          process.analyzeCorrelation1l_YMET15To20 *
                                          process.analyzeCorrelation1l_YMET20To25 *
                                          process.analyzeCorrelation1l_YMET25To30 *
                                          process.analyzeCorrelation1l_YMET30To35 *
                                          process.analyzeCorrelation1l_YMET35To40 *

                                          # execute analyzer modules for HT > 400 and inclusive MET cuts
 ##                                          process.analyzeCorrelation1l_HT400ToInf_MET0ToInf *
##                                           process.analyzeCorrelation1l_HT400ToInf_MET50ToInf *
##                                           process.analyzeCorrelation1l_HT400ToInf_MET100ToInf *
##                                           process.analyzeCorrelation1l_HT400ToInf_MET150ToInf *
##                                           process.analyzeCorrelation1l_HT400ToInf_MET200ToInf *
##                                           process.analyzeCorrelation1l_HT400ToInf_MET250ToInf *

##                                           # execute analyzer modules for HT > 400 and exclusive MET cuts
##                                           process.analyzeCorrelation1l_HT400ToInf_MET0To50 *
##                                           process.analyzeCorrelation1l_HT400ToInf_MET50To100 *
##                                           process.analyzeCorrelation1l_HT400ToInf_MET100To150 *
##                                           process.analyzeCorrelation1l_HT400ToInf_MET150To200 *
##                                           process.analyzeCorrelation1l_HT400ToInf_MET200To250 *
##                                           process.analyzeCorrelation1l_HT400ToInf_MET150ToInf *

                                          # execute analyzer modules for HT > 500 and inclusive MET cuts
##                                           process.analyzeCorrelation1l_HT500ToInf_MET0ToInf *
##                                           process.analyzeCorrelation1l_HT500ToInf_MET50ToInf *
##                                           process.analyzeCorrelation1l_HT500ToInf_MET100ToInf *
##                                           process.analyzeCorrelation1l_HT500ToInf_MET150ToInf *
##                                           process.analyzeCorrelation1l_HT500ToInf_MET200ToInf *
##                                           process.analyzeCorrelation1l_HT500ToInf_MET250ToInf *

##                                           # execute analyzer modules for HT > 500 and exclusive MET cuts
##                                           process.analyzeCorrelation1l_HT500ToInf_MET0To50 *
##                                           process.analyzeCorrelation1l_HT500ToInf_MET50To100 *
##                                           process.analyzeCorrelation1l_HT500ToInf_MET100To150 *
##                                           process.analyzeCorrelation1l_HT500ToInf_MET150To200 *
##                                           process.analyzeCorrelation1l_HT500ToInf_MET200To250 *

                                          # execute analyzer modules for HT > 600 and inclusive MET cuts
 ##                                          process.analyzeCorrelation1l_HT600ToInf_MET0ToInf *
##                                           process.analyzeCorrelation1l_HT600ToInf_MET50ToInf *
##                                           process.analyzeCorrelation1l_HT600ToInf_MET100ToInf *
##                                           process.analyzeCorrelation1l_HT600ToInf_MET150ToInf *
##                                           process.analyzeCorrelation1l_HT600ToInf_MET200ToInf *
##                                           process.analyzeCorrelation1l_HT600ToInf_MET250ToInf *

##                                           # execute analyzer modules for HT > 600 and exclusive MET cuts
##                                           process.analyzeCorrelation1l_HT600ToInf_MET0To50 *
##                                           process.analyzeCorrelation1l_HT600ToInf_MET50To100 *
##                                           process.analyzeCorrelation1l_HT600ToInf_MET100To150 *
##                                           process.analyzeCorrelation1l_HT600ToInf_MET150To200 *
##                                           process.analyzeCorrelation1l_HT600ToInf_MET200To250 *
                                          
##                                           # execute analyzer modules for exclusive HT and exclusive MET cuts
##                                           process.analyzeCorrelation1l_HT300To400_MET0To50 *
##                                           process.analyzeCorrelation1l_HT300To400_MET50To100 *
##                                           process.analyzeCorrelation1l_HT300To400_MET100To150 *

##                                           process.analyzeCorrelation1l_HT400To500_MET0To50 *
##                                           process.analyzeCorrelation1l_HT400To500_MET50To100 *
##                                           process.analyzeCorrelation1l_HT400To500_MET100To150 *

##                                           process.analyzeCorrelation1l_HT500To600_MET0To50 *
##                                           process.analyzeCorrelation1l_HT500To600_MET50To100 *
##                                           process.analyzeCorrelation1l_HT500To600_MET100To150 *

                                          # execute analyzer modules for inclusive nJets cuts
 ##                                          process.filterTightHT *
##                                           process.analyzeTtGenEvent1l_HTSelection_TTJets *
                                                                                    
                                          process.oneTightMET *
                                          process.analyzeTtGenEvent1l_METSelection_TTJets *

                                          process.analyzeCorrelation1l_HT600ToInf_MET150ToInf_nJets3ToInf *
                                          process.analyzeCorrelation1l_HT600ToInf_MET150ToInf_nJets4ToInf 
                                          )

## ## path for dilep control sample
## process.DiLepSelection_TTJets = cms.Path(# execute producer and preselection modules
##                                          process.makeGenEvt *
##                                          process.makeSUSYGenEvt *
##                                          process.scaledJetEnergy *
##                                          process.preselectionLepHTMC2 *
##                                          process.makeObjects *
##                                          process.SUSYEvt *
##                                          process.eventWeightPU *
##                                          process.weightProducer *
##                                          process.btagEventWeightMuJER *

##                                          process.threeGoodJets *
##                                          process.oneTightMET *

##                                          process.filterLeptonPair *
##                                          process.filterMT
##                                          )
                                         
## ## process.load("TopQuarkAnalysis.TopEventProducers.sequences.ttSemiLepEvtBuilder_cff")

## ## addTtSemiLepHypotheses(process,
## ##                        ["kKinFit"]
## ##                        )
## ## removeTtSemiLepHypGenMatch(process)

## #------------------------------------------------------------------
## # Import all modules to to create ttSemiLepEvent
## #------------------------------------------------------------------

## from TopQuarkAnalysis.TopEventProducers.sequences.ttSemiLepEvtBuilder_cff import *

## #------------------------------------------------------------------
## # clone and configure modules to fit hadronically decaying W
## #------------------------------------------------------------------

## process.kinFitTtSemiLepEventHypothesisHadWMass      =  kinFitTtSemiLepEventHypothesis.clone()
## process.kinFitTtSemiLepEventHypothesisHadWMass.mets = "scaledJetEnergy:patMETsPF"
## process.kinFitTtSemiLepEventHypothesisHadWMass.jets = "goodJets"
## process.kinFitTtSemiLepEventHypothesisHadWMass.leps = "goodMuons"
## process.kinFitTtSemiLepEventHypothesisHadWMass.maxNJets = 8
## process.kinFitTtSemiLepEventHypothesisHadWMass.constraints = 1,

## process.ttSemiLepHypKinFitHadWMass      = ttSemiLepHypKinFit.clone()
## process.ttSemiLepHypKinFitHadWMass.mets = "scaledJetEnergy:patMETsPF"
## process.ttSemiLepHypKinFitHadWMass.jets = "goodJets"
## process.ttSemiLepHypKinFitHadWMass.leps = "goodMuons"
        
## process.ttSemiLepHypKinFitHadWMass.match       = "kinFitTtSemiLepEventHypothesisHadWMass"
## process.ttSemiLepHypKinFitHadWMass.status      = "kinFitTtSemiLepEventHypothesisHadWMass:Status"
## process.ttSemiLepHypKinFitHadWMass.leptons     = "kinFitTtSemiLepEventHypothesisHadWMass:Leptons"
## process.ttSemiLepHypKinFitHadWMass.neutrinos   = "kinFitTtSemiLepEventHypothesisHadWMass:Neutrinos"
## process.ttSemiLepHypKinFitHadWMass.partonsHadP = "kinFitTtSemiLepEventHypothesisHadWMass:PartonsHadP"
## process.ttSemiLepHypKinFitHadWMass.partonsHadQ = "kinFitTtSemiLepEventHypothesisHadWMass:PartonsHadQ"
## process.ttSemiLepHypKinFitHadWMass.partonsHadB = "kinFitTtSemiLepEventHypothesisHadWMass:PartonsHadB"
## process.ttSemiLepHypKinFitHadWMass.partonsLepB = "kinFitTtSemiLepEventHypothesisHadWMass:PartonsLepB"
## #process.ttSemiLepHypKinFitHadWMass.nJetsConsidered = "kinFitTtSemiLepEventHypothesisHadWMass:NumberOfConsideredJets"

## process.ttSemiLepEventHadWMass             = ttSemiLepEvent.clone()
## process.ttSemiLepEventHadWMass.hypotheses = ["ttSemiLepHypKinFitHadWMass"]

## ## add extra information on kinFit
## process.ttSemiLepEventHadWMass.kinFit.chi2 = "kinFitTtSemiLepEventHypothesisHadWMass:Chi2"
## process.ttSemiLepEventHadWMass.kinFit.prob = "kinFitTtSemiLepEventHypothesisHadWMass:Prob"


## ## selection path to test kin fit of had W mass
## process.testKinFitHadWMass_TTJets = cms.Path(# execute producer and preselection modules
##                                              process.makeGenEvt *
##                                              process.makeSUSYGenEvt *
##                                              process.scaledJetEnergy *
##                                              process.preselectionLepHTMC2 *
##                                              process.makeObjects *
##                                              process.SUSYEvt *
##                                              process.eventWeightPU *
##                                              process.weightProducer *
##                                              process.btagEventWeightMuJER *
                                             
##                                              # execute filter and analyzer modules
##                                              process.muonSelection *
                                             
##                                              process.fourGoodJets *
                                             
##                                              #process.makeTtSemiLepEventHadWMass *
##                                              process.kinFitTtSemiLepEventHypothesisHadWMass *
##                                              process.ttSemiLepHypKinFitHadWMass *
##                                              process.ttSemiLepEventHadWMass *
                                             
##                                              process.analyzeCorrelation1m_KinFitHadWMass *
##                                              process.analyzeCorrelation1m_KinFitHadWMass_nJets4 *
##                                              process.analyzeCorrelation1m_KinFitHadWMass_nJets5 *
##                                              process.analyzeCorrelation1m_KinFitHadWMass_nJets6
                                             
##                                              #process.filterTightHT *
                                             
##                                              #process.oneTightMET *
##                                              )





#------------------------------------------------------------------
# stuff for gen matching
#------------------------------------------------------------------

## process.ttSemiLepHypGenMatch.jets = 'goodJets'
## process.ttSemiLepHypGenMatch.leps = 'goodMuons'
## process.ttSemiLepHypGenMatch.mets = 'scaledJetEnergy:patMETsPF'
## process.ttSemiLepHypGenMatch.jetCorrectionLevel="L3Absolute"

## #process.ttSemiLepJetPartonMatch.algorithm = "unambiguousOnly"
## #process.ttSemiLepJetPartonMatch.algorithm = "totalMinDist"
## #process.ttSemiLepJetPartonMatch.useMaxDist = True
## ## set number of jets considered in jet-parton matching
## process.ttSemiLepJetPartonMatch.maxNJets=8
## ## choose jet collection considered in jet-parton matching
## process.ttSemiLepJetPartonMatch.jets='goodJets'

## process.load("TopAnalysis.TopAnalyzer.HypothesisKinFit_cfi")
## process.analyzeHypothesisKinFit.analyze.maxNJets = 8
