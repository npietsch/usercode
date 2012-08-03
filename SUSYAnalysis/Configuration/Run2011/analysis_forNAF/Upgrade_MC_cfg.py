
import FWCore.ParameterSet.Config as cms

process = cms.Process("RA4b") 

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.MessageLogger.categories.append('ParticleListDrawer')

process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = cms.string('')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100),
    skipEvents = cms.untracked.uint32(0)
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('Upgrade.root')
                                   )

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring( "")
                            )

# load and configure modules for event weighting
process.load("SUSYAnalysis.SUSYEventProducers.WeightProducer_cfi")

## load and configure module for PU re-weighting
#process.load("TopAnalysis.TopUtils.EventWeightPU_cfi")
#process.eventWeightPU.DataFile = "SUSYAnalysis/SUSYUtils/data/PU_Fall11_TTJets.root"

# load modules for preselection
process.load("SUSYAnalysis.SUSYFilter.sequences.Preselection_cff")

# load modules to create objects and filter events on reco level
process.load("SUSYAnalysis.SUSYFilter.sequences.BjetsSelection_cff")

# load and configure module to smear jet energy
from SUSYAnalysis.Uncertainties.JetEnergy_cfi import *
process.scaledJetEnergy = scaledJetEnergy.clone()
process.scaledJetEnergy.inputJets = "selectedPatJetsAK5PF" ######### <---------------
process.scaledJetEnergy.inputMETs = "patMETsPF"
process.scaledJetEnergy.doJetSmearing = True

# define source for goodJets producer
process.goodJets.src = "scaledJetEnergy:selectedPatJetsAK5PF"######### <---------------
process.goodMETs.src = "scaledJetEnergy:patMETsPF"

######### CALO <---------------

process.scaledCaloJetEnergy = scaledJetEnergy.clone()
process.scaledCaloJetEnergy.inputJets = "cleanPatJetsAK5Calo" 
process.scaledCaloJetEnergy.inputMETs = "patMETsAK5Calo"
process.scaledCaloJetEnergy.doJetSmearing = True

# define source for goodJets producer
process.goodCaloJets.src = "scaledCaloJetEnergy:cleanPatJetsAK5Calo"
process.goodCaloMETs.src = "scaledCaloJetEnergy:patMETsAK5Calo"

#------------------------------------------------------------
# load and configure modules for b-tag efficiency weighting
#------------------------------------------------------------

process.load("RecoBTag.PerformanceDB.PoolBTagPerformanceDB1107")
process.load("RecoBTag.PerformanceDB.BTagPerformanceDB1107")
process.load("Btagging.BtagWeightProducer.BtagEventWeight_cfi")
#process.load("SUSYAnalysis.SUSYAnalyzer.HCalUpgrade_cfi")

### common default settings (similar for muon and electron channel)
process.btagEventWeight.bTagAlgo  = "TCHEM"
process.btagEventWeight.filename  = "../../../../SUSYAnalysis/SUSYUtils/data/BtagEff_TTJets.root"
process.btagEventWeight.jets      = "goodJets"

process.btagEventWeightMu         = process.btagEventWeight.clone( rootDir = "RA4bMuTCHEM3" )
process.btagEventWeightEl         = process.btagEventWeight.clone( rootDir = "RA4bElTCHEM3" )


#--------------------------
# selection paths
#--------------------------

process.createObjects = cms.Path(process.scaledJetEnergy *
                                 #process.scaledCaloJetEnergy *
                                 process.makeObjects #*
                                 #process.eventWeightPU *
                                 #process.weightProducer
                                 )

#--------------------------
# muon + PF Jets paths
#--------------------------

from SUSYAnalysis.SUSYAnalyzer.SUSYAnalyzer_cfi import *

analyzeSUSY.jets = "goodJets"
analyzeSUSY.bjets = "mediumCSVBjets"
analyzeSUSY.muons = "goodMuons"
analyzeSUSY.electrons = "goodElectrons"
analyzeSUSY.met = "scaledJetEnergy:patMETsPF"

process.analyzeSUSY1m_noCuts = analyzeSUSY.clone()
process.analyzeSUSY1m_noCuts.muons = "goodNotIsoMuons"
process.analyzeSUSY1m_lepton = analyzeSUSY.clone()
process.analyzeSUSY1m_jet    = analyzeSUSY.clone()
process.analyzeSUSY1m_HT     = analyzeSUSY.clone()
process.analyzeSUSY1m_met    = analyzeSUSY.clone()
process.analyzeSUSY1m_1b     = analyzeSUSY.clone()
process.analyzeSUSY1m_2b     = analyzeSUSY.clone()
process.analyzeSUSY1m_3b     = analyzeSUSY.clone()
process.analyzeSUSY1m_mt     = analyzeSUSY.clone()
'''
process.analyzeSUSY1b1m_0 = analyzeSUSY.clone()
process.analyzeSUSY1b1m_1 = analyzeSUSY.clone()
process.analyzeSUSY1b1m_2 = analyzeSUSY.clone()
process.analyzeSUSY1b1m_3 = analyzeSUSY.clone()
process.analyzeSUSY1b1m_4 = analyzeSUSY.clone()
process.analyzeSUSY1b1m_5 = analyzeSUSY.clone()
process.analyzeSUSY1b1m_6 = analyzeSUSY.clone()
process.analyzeSUSY1b1m_mtSelection = analyzeSUSY.clone()
'''
from SUSYAnalysis.SUSYAnalyzer.HCalUpgrade_cfi import *

analyzeHCal_PF   = analyzeHCal.clone()
analyzeHCal_PF.jets = "goodJets"
analyzeHCal_PF.muons = "goodMuons"
analyzeHCal_PF.electrons = "goodElectrons"

process.analyzeHCal1m_PF_noCuts = analyzeHCal_PF.clone()
process.analyzeHCal1m_PF_noCuts.muons = "goodNotIsoMuons"
process.analyzeHCal1m_PF_lepton = analyzeHCal_PF.clone()
process.analyzeHCal1m_PF_jet    = analyzeHCal_PF.clone()
process.analyzeHCal1m_PF_HT     = analyzeHCal_PF.clone()
process.analyzeHCal1m_PF_met    = analyzeHCal_PF.clone()
process.analyzeHCal1m_PF_1b     = analyzeHCal_PF.clone()
process.analyzeHCal1m_PF_2b     = analyzeHCal_PF.clone()
process.analyzeHCal1m_PF_3b     = analyzeHCal_PF.clone()
process.analyzeHCal1m_PF_mt     = analyzeHCal_PF.clone()
'''

process.analyzeHCal1m_PF_noCuts = process.analyzeHCal_PF.clone()
process.analyzeHCal1m_PF_noCuts.muons = "goodNotIsoMuons"
process.analyzeHCal1m_PF_0      = process.analyzeHCal_PF.clone()
process.analyzeHCal1m_PF_1      = process.analyzeHCal_PF.clone()
process.analyzeHCal1m_PF_2      = process.analyzeHCal_PF.clone()
process.analyzeHCal1m_PF_3      = process.analyzeHCal_PF.clone()
process.analyzeHCal1m_PF_4      = process.analyzeHCal_PF.clone()
process.analyzeHCal1m_PF_5      = process.analyzeHCal_PF.clone()
process.analyzeHCal1m_PF_6      = process.analyzeHCal_PF.clone()
process.analyzeHCal1m_PF_mtSelection = process.analyzeHCal_PF.clone()
'''
#--------------------------
# muon + Calo Jets paths
#--------------------------

from SUSYAnalysis.SUSYAnalyzer.SUSYAnalyzer_cfi import *

analyzeSUSY.jets = "goodJets"
analyzeSUSY.muons = "goodMuons"
analyzeSUSY.bjets = "mediumCSVBjets"
analyzeSUSY.electrons = "goodElectrons"
analyzeSUSY.met = "scaledCaloJetEnergy:patMETsAK5Calo"

process.analyzeSUSY1b1mCalo_noCuts = analyzeSUSY.clone()
process.analyzeSUSY1b1mCalo_noCuts.muons = "goodNotIsoMuons"
process.analyzeSUSY1b1mCalo_0 = analyzeSUSY.clone()
process.analyzeSUSY1b1mCalo_1 = analyzeSUSY.clone()
process.analyzeSUSY1b1mCalo_2 = analyzeSUSY.clone()
process.analyzeSUSY1b1mCalo_3 = analyzeSUSY.clone()
process.analyzeSUSY1b1mCalo_4 = analyzeSUSY.clone()
process.analyzeSUSY1b1mCalo_5 = analyzeSUSY.clone()
process.analyzeSUSY1b1mCalo_6 = analyzeSUSY.clone()
process.analyzeSUSY1b1mCalo_mtSelection = analyzeSUSY.clone()

from SUSYAnalysis.SUSYAnalyzer.HCalUpgrade_cfi import *

process.analyzeHCal_Calo = analyzeHCal.clone()
process.analyzeHCal_Calo.jets = "goodJets"
process.analyzeHCal_Calo.muons = "goodMuons"
process.analyzeHCal_Calo.electrons = "goodElectrons"
process.analyzeHCal_Calo.met = "scaledCaloJetEnergy:patMETsAK5Calo"


process.analyzeHCal1m_Calo_noCuts = process.analyzeHCal_Calo.clone()
process.analyzeHCal1m_Calo_noCuts.muons = "goodNotIsoMuons"
process.analyzeHCal1m_Calo_0      = process.analyzeHCal_Calo.clone()
process.analyzeHCal1m_Calo_1      = process.analyzeHCal_Calo.clone()
process.analyzeHCal1m_Calo_2      = process.analyzeHCal_Calo.clone()
process.analyzeHCal1m_Calo_3      = process.analyzeHCal_Calo.clone()
process.analyzeHCal1m_Calo_4      = process.analyzeHCal_Calo.clone()
process.analyzeHCal1m_Calo_5      = process.analyzeHCal_Calo.clone()
process.analyzeHCal1m_Calo_6      = process.analyzeHCal_Calo.clone()
process.analyzeHCal1m_Calo_mtSelection = process.analyzeHCal_Calo.clone()

'''process.analyzeHCal1b1m_PF_noCuts = process.analyzeHCal_PF.clone()
process.analyzeHCal1b1m_PF_noCuts.muons = "goodNotIsoMuons"
process.analyzeHCal1b1m_PF_1      = process.analyzeHCal_PF.clone()
process.analyzeHCal1b1m_PF_2      = process.analyzeHCal_PF.clone()
process.analyzeHCal1b1m_PF_3      = process.analyzeHCal_PF.clone()
process.analyzeHCal1b1m_PF_4      = process.analyzeHCal_PF.clone()
process.analyzeHCal1b1m_PF_5      = process.analyzeHCal_PF.clone()
process.analyzeHCal1b1m_PF_6      = process.analyzeHCal_PF.clone()
process.analyzeHCal1b1m_PF_mtSelection = process.analyzeHCal_PF.clone()

process.analyzeHCal1b1m_Calo_noCuts = process.analyzeHCal_Calo.clone()
process.analyzeHCal1b1m_Calo_noCuts.muons = "goodNotIsoMuons"
process.analyzeHCal1b1m_Calo_1      = process.analyzeHCal_Calo.clone()
process.analyzeHCal1b1m_Calo_2      = process.analyzeHCal_Calo.clone()
process.analyzeHCal1b1m_Calo_3      = process.analyzeHCal_Calo.clone()
process.analyzeHCal1b1m_Calo_4      = process.analyzeHCal_Calo.clone()
process.analyzeHCal1b1m_Calo_5      = process.analyzeHCal_Calo.clone()
process.analyzeHCal1b1m_Calo_6      = process.analyzeHCal_Calo.clone()
process.analyzeHCal1b1m_Calo_mtSelection = process.analyzeHCal_Calo.clone()
'''
process.cutFlow1bMuPF = cms.Path(process.analyzeSUSY1m_noCuts *
                                 process.analyzeHCal1m_PF_noCuts *
                                 
                                 process.preselectionMuHTMC2 *
                                 #process.analyzeSUSY1b1m_1 *
                                 #process.analyzeHCal1m_PF_1 *
                                 
                                 process.MuHadSelection *
                                 process.muonSelection*
                                 process.analyzeSUSY1m_lepton *
                                 process.analyzeHCal1m_PF_lepton *
                                 
                                 process.jetSelection *
                                 process.analyzeSUSY1m_jet *
                                 process.analyzeHCal1m_PF_jet *
                               
                                 process.HTSelection *
                                 process.analyzeSUSY1m_HT *
                                 process.analyzeHCal1m_PF_HT *
                                 
                                 process.metSelection *
                                 process.analyzeSUSY1m_met *
                                 process.analyzeHCal1m_PF_met *

                                 process.oneMediumCSVBjet *
                                 process.analyzeSUSY1m_1b *
                                 process.analyzeHCal1m_PF_1b *
                                 
                                 process.twoMediumCSVBjet *
                                 process.analyzeSUSY1m_2b *
                                 process.analyzeHCal1m_PF_2b *
                                 
                                 process.threeMediumCSVBjet *
                                 process.analyzeSUSY1m_3b *
                                 process.analyzeHCal1m_PF_3b *
                                                                
                                 process.mTSelection *
                                 process.analyzeSUSY1m_mt *
                                 process.analyzeHCal1m_PF_mt
                                 )

'''
process.cutFlow1bMuCalo = cms.Path(process.analyzeSUSY1b1mCalo_noCuts *
                                   process.analyzeHCal1m_Calo_noCuts *
                                   
                                   process.preselectionMuHTMC2 *
                                   #process.analyzeSUSY1b1mCalo_1 *
                                   #process.analyzeHCal1m_Calo_1 *
                                   
                                   process.MuHadSelectionCalo *
                                   process.muonSelection*
                                   #process.analyzeSUSY1b1mCalo_2 *
                                   #process.analyzeHCal1m_Calo_2 *
                                 
                                   process.calojetSelection *
                                   #process.analyzeSUSY1b1mCalo_3 *
                                   #process.analyzeHCal1m_Calo_3 *
                               
                                   process.HTSelectionCalo *
                                   #process.analyzeSUSY1b1mCalo_4 *
                                   #process.analyzeHCal1m_Calo_4 *
                                 
                                   process.caloMetSelection *
                                   process.analyzeSUSY1b1mCalo_0*
                                   process.analyzeHCal1m_Calo_0 *
                                 
                                   process.oneMediumCSVCaloBjet *
                                   process.analyzeSUSY1b1mCalo_1 *
                                   process.analyzeHCal1m_Calo_1 *

                                   process.twoMediumCSVCaloBjet *
                                   process.analyzeSUSY1b1mCalo_2 *
                                   process.analyzeHCal1m_Calo_2 *
                                   
                                   process.threeMediumCSVCaloBjet *
                                   process.analyzeSUSY1b1mCalo_3 *
                                   process.analyzeHCal1m_Calo_3 *
                                   
                                   process.mTSelection *
                                   process.analyzeSUSY1b1mCalo_mtSelection *
                                   process.analyzeHCal1m_Calo_mtSelection
                                 )

'''
'''
process.cutFlowMu = cms.Path(process.analyzeSUSY1b1m_noCuts *
                             process.preselectionMuHTMC2 *
                             process.analyzeSUSY1b1m_1 *
                             process.MuHadSelection *
                             process.muonSelection*
                             process.analyzeSUSY1b1m_2 *
                             process.jetSelection *
                             #process.analyzeHCal *
                             process.analyzeSUSY1b1m_3 *
                             process.HTSelection *
                             process.analyzeSUSY1b1m_4 *
                             process.metSelection *
                             process.analyzeSUSY1b1m_5 *
                             process.mTSelection *
                             process.analyzeSUSY1b1m_mtSelection
                             )

process.selection1m = cms.Sequence(process.preselectionMuHTMC2 *
                                   process.MuHadSelection *
                                   process.muonSelection *
                                   process.jetSelection
                                   #process.btagEventWeightMu
                                   )

process.analysis1b1m = cms.Path(process.selection1m
                                #process.analyzeSUSY1b1m_6
                                )

'''

#----------------------------
# electron + PF Jets paths
#----------------------------

from SUSYAnalysis.SUSYAnalyzer.SUSYAnalyzer_cfi import *

analyzeSUSY.jets = "goodJets"
analyzeSUSY.muons = "goodMuons"
analyzeSUSY.bjets = "mediumCSVBjets"
analyzeSUSY.electrons = "goodElectrons"
analyzeSUSY.met = "scaledJetEnergy:patMETsPF"

process.analyzeSUSY1e_noCuts = analyzeSUSY.clone()
process.analyzeSUSY1e_noCuts.muons = "goodNotIsoMuons"
process.analyzeSUSY1e_lepton = analyzeSUSY.clone()
process.analyzeSUSY1e_jet    = analyzeSUSY.clone()
process.analyzeSUSY1e_HT     = analyzeSUSY.clone()
process.analyzeSUSY1e_met    = analyzeSUSY.clone()
process.analyzeSUSY1e_1b     = analyzeSUSY.clone()
process.analyzeSUSY1e_2b     = analyzeSUSY.clone()
process.analyzeSUSY1e_3b     = analyzeSUSY.clone()
process.analyzeSUSY1e_mt     = analyzeSUSY.clone()

'''
process.analyzeSUSY1b1e_noCuts = analyzeSUSY.clone()
process.analyzeSUSY1b1e_noCuts.muons = "goodNotIsoMuons"
process.analyzeSUSY1b1e_0 = analyzeSUSY.clone()
process.analyzeSUSY1b1e_1 = analyzeSUSY.clone()
process.analyzeSUSY1b1e_2 = analyzeSUSY.clone()
process.analyzeSUSY1b1e_3 = analyzeSUSY.clone()
process.analyzeSUSY1b1e_4 = analyzeSUSY.clone()
process.analyzeSUSY1b1e_5 = analyzeSUSY.clone()
process.analyzeSUSY1b1e_6 = analyzeSUSY.clone()
process.analyzeSUSY1b1e_mtSelection = analyzeSUSY.clone()
'''
from SUSYAnalysis.SUSYAnalyzer.HCalUpgrade_cfi import *

analyzeHCal_PF   = analyzeHCal.clone()
analyzeHCal_PF.jets = "goodJets"
analyzeHCal_PF.muons = "goodMuons"
analyzeHCal_PF.electrons = "goodElectrons"

process.analyzeHCal1e_PF_noCuts = analyzeHCal_PF.clone()
process.analyzeHCal1e_PF_noCuts.muons = "goodNotIsoMuons"
process.analyzeHCal1e_PF_lepton = analyzeHCal_PF.clone()
process.analyzeHCal1e_PF_jet    = analyzeHCal_PF.clone()
process.analyzeHCal1e_PF_HT     = analyzeHCal_PF.clone()
process.analyzeHCal1e_PF_met    = analyzeHCal_PF.clone()
process.analyzeHCal1e_PF_1b     = analyzeHCal_PF.clone()
process.analyzeHCal1e_PF_2b     = analyzeHCal_PF.clone()
process.analyzeHCal1e_PF_3b     = analyzeHCal_PF.clone()
process.analyzeHCal1e_PF_mt     = analyzeHCal_PF.clone()
'''
process.analyzeHCal1e_PF_noCuts = process.analyzeHCal_PF.clone()
process.analyzeHCal1e_PF_noCuts.muons = "goodNotIsoMuons"
process.analyzeHCal1e_PF_0      = process.analyzeHCal_PF.clone()
process.analyzeHCal1e_PF_1      = process.analyzeHCal_PF.clone()
process.analyzeHCal1e_PF_2      = process.analyzeHCal_PF.clone()
process.analyzeHCal1e_PF_3      = process.analyzeHCal_PF.clone()
process.analyzeHCal1e_PF_4      = process.analyzeHCal_PF.clone()
process.analyzeHCal1e_PF_5      = process.analyzeHCal_PF.clone()
process.analyzeHCal1e_PF_6      = process.analyzeHCal_PF.clone()
process.analyzeHCal1e_PF_mtSelection = process.analyzeHCal_PF.clone()
'''
#-----------------------------
# electron + Calo Jets paths
#-----------------------------

from SUSYAnalysis.SUSYAnalyzer.SUSYAnalyzer_cfi import *

analyzeSUSY.jets = "goodCaloJets"
analyzeSUSY.muons = "goodMuons"
analyzeSUSY.bjets = "mediumCSVBjets"
analyzeSUSY.electrons = "goodElectrons"
analyzeSUSY.met = "scaledCaloJetEnergy:patMETsAK5Calo"

process.analyzeSUSY1b1eCalo_noCuts = analyzeSUSY.clone()
process.analyzeSUSY1b1eCalo_noCuts.muons = "goodNotIsoMuons"
process.analyzeSUSY1b1eCalo_0 = analyzeSUSY.clone()
process.analyzeSUSY1b1eCalo_1 = analyzeSUSY.clone()
process.analyzeSUSY1b1eCalo_2 = analyzeSUSY.clone()
process.analyzeSUSY1b1eCalo_3 = analyzeSUSY.clone()
process.analyzeSUSY1b1eCalo_4 = analyzeSUSY.clone()
process.analyzeSUSY1b1eCalo_5 = analyzeSUSY.clone()
process.analyzeSUSY1b1eCalo_6 = analyzeSUSY.clone()
process.analyzeSUSY1b1eCalo_mtSelection = analyzeSUSY.clone()

from SUSYAnalysis.SUSYAnalyzer.HCalUpgrade_cfi import *

process.analyzeHCal_Calo = analyzeHCal.clone()
process.analyzeHCal_Calo.jets = "goodJets"
process.analyzeHCal_Calo.muons = "goodMuons"
process.analyzeHCal_Calo.electrons = "goodElectrons"
process.analyzeHCal_Calo.met = "scaledCaloJetEnergy:patMETsAK5Calo"


process.analyzeHCal1e_Calo_noCuts = process.analyzeHCal_Calo.clone()
process.analyzeHCal1e_Calo_noCuts.muons = "goodNotIsoMuons"
process.analyzeHCal1e_Calo_0      = process.analyzeHCal_Calo.clone()
process.analyzeHCal1e_Calo_1      = process.analyzeHCal_Calo.clone()
process.analyzeHCal1e_Calo_2      = process.analyzeHCal_Calo.clone()
process.analyzeHCal1e_Calo_3      = process.analyzeHCal_Calo.clone()
process.analyzeHCal1e_Calo_4      = process.analyzeHCal_Calo.clone()
process.analyzeHCal1e_Calo_5      = process.analyzeHCal_Calo.clone()
process.analyzeHCal1e_Calo_6      = process.analyzeHCal_Calo.clone()
process.analyzeHCal1e_Calo_mtSelection = process.analyzeHCal_Calo.clone()

'''process.analyzeHCal1b1e_PF_noCuts = process.analyzeHCal_PF.clone()
process.analyzeHCal1b1e_PF_noCuts.muons = "goodNotIsoMuons"
process.analyzeHCal1b1e_PF_1      = process.analyzeHCal_PF.clone()
process.analyzeHCal1b1e_PF_2      = process.analyzeHCal_PF.clone()
process.analyzeHCal1b1e_PF_3      = process.analyzeHCal_PF.clone()
process.analyzeHCal1b1e_PF_4      = process.analyzeHCal_PF.clone()
process.analyzeHCal1b1e_PF_5      = process.analyzeHCal_PF.clone()
process.analyzeHCal1b1e_PF_6      = process.analyzeHCal_PF.clone()
process.analyzeHCal1b1e_PF_mtSelection = process.analyzeHCal_PF.clone()

process.analyzeHCal1b1e_Calo_noCuts = process.analyzeHCal_Calo.clone()
process.analyzeHCal1b1e_Calo_noCuts.muons = "goodNotIsoMuons"
process.analyzeHCal1b1e_Calo_1      = process.analyzeHCal_Calo.clone()
process.analyzeHCal1b1e_Calo_2      = process.analyzeHCal_Calo.clone()
process.analyzeHCal1b1e_Calo_3      = process.analyzeHCal_Calo.clone()
process.analyzeHCal1b1e_Calo_4      = process.analyzeHCal_Calo.clone()
process.analyzeHCal1b1e_Calo_5      = process.analyzeHCal_Calo.clone()
process.analyzeHCal1b1e_Calo_6      = process.analyzeHCal_Calo.clone()
process.analyzeHCal1b1e_Calo_mtSelection = process.analyzeHCal_Calo.clone()
'''
process.cutFlow1bElPF = cms.Path(process.analyzeSUSY1e_noCuts *
                                 process.analyzeHCal1e_PF_noCuts *
                                 
                                 process.preselectionElHTMC2 *
                                 #process.analyzeSUSY1b1e_1 *
                                 #process.analyzeHCal1e_PF_1 *
                                 
                                 process.ElHadSelection *
                                 process.electronSelection*
                                 process.analyzeSUSY1e_lepton *
                                 process.analyzeHCal1e_PF_lepton *
                                 
                                 process.jetSelection *
                                 process.analyzeSUSY1e_jet *
                                 process.analyzeHCal1e_PF_jet *
                               
                                 process.HTSelection *
                                 process.analyzeSUSY1e_HT *
                                 process.analyzeHCal1e_PF_HT *

                                 process.metSelection *
                                 process.analyzeSUSY1e_met *
                                 process.analyzeHCal1e_PF_met *

                                 process.oneMediumCSVBjet *
                                 process.analyzeSUSY1e_1b *
                                 process.analyzeHCal1e_PF_1b *
                                 
                                 process.twoMediumCSVBjet *
                                 process.analyzeSUSY1e_2b *
                                 process.analyzeHCal1e_PF_2b *
                                 
                                 process.threeMediumCSVBjet *
                                 process.analyzeSUSY1e_3b *
                                 process.analyzeHCal1e_PF_3b *
                                 
                                 process.mTSelection *
                                 process.analyzeSUSY1e_mt *
                                 process.analyzeHCal1e_PF_mt
                                 )

'''
process.cutFlow1bElCalo = cms.Path(process.analyzeSUSY1b1eCalo_noCuts *
                                   process.analyzeHCal1e_Calo_noCuts *
                                   
                                   process.preselectionElHTMC2 *
                                   #process.analyzeSUSY1b1eCalo_1 *
                                   #process.analyzeHCal1e_Calo_1 *
                                   
                                   process.ElHadSelectionCalo *
                                   process.electronSelection*
                                   #process.analyzeSUSY1b1eCalo_2 *
                                   #process.analyzeHCal1e_Calo_2 *
                                 
                                   process.calojetSelection *
                                   #process.analyzeSUSY1b1eCalo_3 *
                                   #process.analyzeHCal1e_Calo_3 *
                               
                                   process.HTSelectionCalo *
                                   #process.analyzeSUSY1b1eCalo_4 *
                                   #process.analyzeHCal1e_Calo_4 *
                                 
                                   process.caloMetSelection *
                                   process.analyzeSUSY1b1eCalo_0 *
                                   process.analyzeHCal1e_Calo_0 *
                                 
                                   process.oneMediumCSVCaloBjet *
                                   process.analyzeSUSY1b1eCalo_1 *
                                   process.analyzeHCal1e_Calo_1 *

                                   process.twoMediumCSVCaloBjet *
                                   process.analyzeSUSY1b1eCalo_2 *
                                   process.analyzeHCal1e_Calo_2 *
                                   
                                   process.threeMediumCSVCaloBjet *
                                   process.analyzeSUSY1b1eCalo_3 *
                                   process.analyzeHCal1e_Calo_3 *
                                 
                                   process.mTSelection *
                                   process.analyzeSUSY1b1mCalo_mtSelection *
                                   process.analyzeHCal1m_Calo_mtSelection
                                 )
'''
'''
process.cutFlowEle = cms.Path(#process.analyzeSUSY1b1e_noCuts *
                              process.preselectionElHTMC2 *
                              #process.analyzeSUSY1b1e_1 *
                              process.ElHadSelection *
                              process.electronSelection*
                              #process.analyzeSUSY1b1e_2 *
                              process.jetSelection *
                              #process.analyzeSUSY1b1e_3 *
                              process.HTSelection *
                              #process.analyzeSUSY1b1e_4 *
                              process.metSelection *
                              #process.analyzeSUSY1b1e_5 *
                              process.mTSelection
                              #process.analyzeSUSY1b1e_mtSelection
                              )

process.selection1e = cms.Sequence(process.preselectionElHTMC2 *
                                   process.ElHadSelection *
                                   process.electronSelection*
                                   process.jetSelection #*
                                   #process.btagEventWeightEl
                                   )


process.analysis1b1e = cms.Path(process.selection1e
                                #process.analyzeSUSY1b1e_6
                                )
'''
