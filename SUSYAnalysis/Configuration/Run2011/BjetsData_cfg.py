import FWCore.ParameterSet.Config as cms

process = cms.Process("RA4b")

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000
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
process.GlobalTag.globaltag = cms.string('GR_R_42_V19::All')

## load modules for preselection
process.load("SUSYAnalysis.SUSYFilter.sequences.Preselection_cff")

## load modules to create objects and filter events on reco level
process.load("SUSYAnalysis.SUSYFilter.sequences.BjetsSelection_cff")
process.load("SUSYAnalysis.SUSYFilter.sequences.MuonID_cff")

## load modules for analysis on reco-level
process.load("SUSYAnalysis.SUSYAnalyzer.sequences.SUSYBjetsAnalysis_Data_cff")

#--------------------------
# muon selection paths
#--------------------------

## no btag
process.Selection1m = cms.Path(process.makeObjects *
                               process.analyzeSUSYBjets1m_noCuts *
                               process.preselectionMuHTAllData *
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
process.Selection1b1m_2 = cms.Path(process.makeObjects *
                                   process.preselectionMuHTAllData *
                                   process.MuHadSelection *
                                   process.muonSelection*
                                   process.jetSelection *
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
process.Selection2b1m_2 = cms.Path(process.makeObjects *
                                   process.preselectionMuHTAllData *
                                   process.MuHadSelection *
                                   process.muonSelection*
                                   process.jetSelection *
                                   process.exactlyTwoMediumTrackHighEffBjets *
                                   process.analyzeSUSYBjets2b1m_4 *
                                   process.HTSelection *
                                   process.analyzeSUSYBjets2b1m_5 *
                                   process.metSelection *
                                   process.analyzeSUSYBjets2b1m_6 *
                                   process.mTSelection *
                                   process.analyzeSUSYBjets3b1m_1
                                   )
## at least 3 btags
process.Selection3b1m_1 = cms.Path(process.makeObjects *
                                   process.preselectionMuHTAllData *
                                   process.MuHadSelection *
                                   process.muonSelection*
                                   process.jetSelection *
                                   process.threeMediumTrackHighEffBjets *
                                   process.analyzeSUSYBjets3b1m_4 *
                                   process.HTSelection *
                                   process.analyzeSUSYBjets3b1m_5 *
                                   process.metSelection *
                                   process.analyzeSUSYBjets3b1m_6 *
                                   process.mTSelection *
                                   process.analyzeSUSYBjets1b1m_1
                                   )
#--------------------------
# electron selection paths
#--------------------------

## no btag
process.Selection1e = cms.Path(process.makeObjects *
                               process.analyzeSUSYBjets1e_noCuts *
                               process.preselectionElHTAllData *
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
process.Selection1b1e_2 = cms.Path(process.makeObjects *
                                   process.preselectionElHTAllData *
                                   process.ElHadSelection *
                                   process.electronSelection*
                                   process.jetSelection *
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
process.Selection2b1e_2 = cms.Path(process.makeObjects *
                                   process.preselectionElHTAllData *
                                   process.ElHadSelection *
                                   process.electronSelection*
                                   process.jetSelection *
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
process.Selection3b1e_1 = cms.Path(process.makeObjects *
                                   process.preselectionElHTAllData *
                                   process.ElHadSelection *
                                   process.electronSelection *
                                   process.jetSelection *
                                   process.threeMediumTrackHighEffBjets *
                                   process.analyzeSUSYBjets3b1e_4 *
                                   process.HTSelection *
                                   process.analyzeSUSYBjets3b1e_5 *
                                   process.metSelection *
                                   process.analyzeSUSYBjets3b1e_6 *
                                   process.mTSelection *
                                   process.analyzeSUSYBjets3b1e_1
                                   )
