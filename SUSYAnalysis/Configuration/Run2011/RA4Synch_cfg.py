import FWCore.ParameterSet.Config as cms

process = cms.Process("RA4Synch")

## configure message logger
process.load("FWCore.MessageLogger.MessageLogger_cfi")
#process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.MessageLogger.categories.append('ParticleListDrawer')

# Choose input files
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    '/store/user/npietsch/LM1_SUSY_sftsht_7TeV-pythia6/PAT/89614fbe8472c25559618ceb16e3da73/Spring11_10_1_BhC.root',
    '/store/user/npietsch/LM1_SUSY_sftsht_7TeV-pythia6/PAT/89614fbe8472c25559618ceb16e3da73/Spring11_11_1_Le5.root',
    '/store/user/npietsch/LM1_SUSY_sftsht_7TeV-pythia6/PAT/89614fbe8472c25559618ceb16e3da73/Spring11_12_1_KZa.root',
    '/store/user/npietsch/LM1_SUSY_sftsht_7TeV-pythia6/PAT/89614fbe8472c25559618ceb16e3da73/Spring11_13_1_3uv.root',
    '/store/user/npietsch/LM1_SUSY_sftsht_7TeV-pythia6/PAT/89614fbe8472c25559618ceb16e3da73/Spring11_14_1_viA.root',
    '/store/user/npietsch/LM1_SUSY_sftsht_7TeV-pythia6/PAT/89614fbe8472c25559618ceb16e3da73/Spring11_15_1_4k1.root',
    '/store/user/npietsch/LM1_SUSY_sftsht_7TeV-pythia6/PAT/89614fbe8472c25559618ceb16e3da73/Spring11_16_1_9x4.root',
    '/store/user/npietsch/LM1_SUSY_sftsht_7TeV-pythia6/PAT/89614fbe8472c25559618ceb16e3da73/Spring11_17_1_9eE.root',
    '/store/user/npietsch/LM1_SUSY_sftsht_7TeV-pythia6/PAT/89614fbe8472c25559618ceb16e3da73/Spring11_18_1_75D.root',
    '/store/user/npietsch/LM1_SUSY_sftsht_7TeV-pythia6/PAT/89614fbe8472c25559618ceb16e3da73/Spring11_19_1_jk5.root',
    '/store/user/npietsch/LM1_SUSY_sftsht_7TeV-pythia6/PAT/89614fbe8472c25559618ceb16e3da73/Spring11_1_1_aVA.root',
    '/store/user/npietsch/LM1_SUSY_sftsht_7TeV-pythia6/PAT/89614fbe8472c25559618ceb16e3da73/Spring11_20_1_ucC.root',
    '/store/user/npietsch/LM1_SUSY_sftsht_7TeV-pythia6/PAT/89614fbe8472c25559618ceb16e3da73/Spring11_21_1_tz2.root',
    '/store/user/npietsch/LM1_SUSY_sftsht_7TeV-pythia6/PAT/89614fbe8472c25559618ceb16e3da73/Spring11_22_1_wGO.root',
    '/store/user/npietsch/LM1_SUSY_sftsht_7TeV-pythia6/PAT/89614fbe8472c25559618ceb16e3da73/Spring11_2_1_LNw.root',
    '/store/user/npietsch/LM1_SUSY_sftsht_7TeV-pythia6/PAT/89614fbe8472c25559618ceb16e3da73/Spring11_3_1_Evm.root',
    '/store/user/npietsch/LM1_SUSY_sftsht_7TeV-pythia6/PAT/89614fbe8472c25559618ceb16e3da73/Spring11_4_1_4cW.root',
    '/store/user/npietsch/LM1_SUSY_sftsht_7TeV-pythia6/PAT/89614fbe8472c25559618ceb16e3da73/Spring11_5_1_NoR.root',
    '/store/user/npietsch/LM1_SUSY_sftsht_7TeV-pythia6/PAT/89614fbe8472c25559618ceb16e3da73/Spring11_6_1_szm.root',
    '/store/user/npietsch/LM1_SUSY_sftsht_7TeV-pythia6/PAT/89614fbe8472c25559618ceb16e3da73/Spring11_7_1_0vR.root',
    '/store/user/npietsch/LM1_SUSY_sftsht_7TeV-pythia6/PAT/89614fbe8472c25559618ceb16e3da73/Spring11_8_1_uS1.root',
    '/store/user/npietsch/LM1_SUSY_sftsht_7TeV-pythia6/PAT/89614fbe8472c25559618ceb16e3da73/Spring11_9_1_KMj.root'
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(22000),
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
process.GlobalTag.globaltag = cms.string('START311_V2A::All')

#-----------------------------------------------------------------
# Load modules for preselection
#-----------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.Preselection_cff")

#-----------------------------------------------------------------
# Load modules to create objects and filter events on reco level
#-----------------------------------------------------------------

# Object Selection
process.load("SUSYAnalysis.SUSYFilter.sequences.BjetsSelection_cff")
#process.load("SUSYAnalysis.SUSYFilter.sequences.RA4_Selection_cff")
#process.load("SUSYAnalysis.SUSYFilter.sequences.MuonID_cff")

#--------------------------------------------------------
# Load modules for analysis on generator and reco-level
#--------------------------------------------------------

## process.load("SUSYAnalysis.SUSYAnalyzer.sequences.SUSYBjetsAnalysis_cff")

#------------------
# Selection paths
#-------------------

## Muon selection
process.MuonSelection = cms.Path(process.preselectionMuSynch *
                                 process.goodObjects *
                                 process.oneVertexMuon *
                                 process.oneGoodMuon *
                                 process.exactlyOneGoodMuon *
                                 process.noGoodElectron *
                                 process.oneLooseJet*
                                 process.twoLooseJets *
                                 process.threeLooseJets *
                                 process.fourLooseJets *
                                 process.oneGoodMET *
                                 process.oneTightMET
                                 )
## Electron selection
process.ElecSelection = cms.Path(process.preselectionElSynch *
                                 process.goodObjects *
                                 process.oneIsolatedElectron *
                                 process.oneGoodElectron *
                                 process.exactlyOneGoodElectron *
                                 process.noGoodMuon *
                                 process.oneLooseJet*
                                 process.twoLooseJets *
                                 process.threeLooseJets *
                                 process.fourLooseJets *
                                 process.oneGoodMET *
                                 process.oneTightMET
                                 )
