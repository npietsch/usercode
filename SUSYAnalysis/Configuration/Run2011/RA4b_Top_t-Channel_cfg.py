from BjetsPAT_cfg import *

from SUSYAnalysis.SUSYFilter.sequences.Preselection_cff import *
process.preselectionMuHTMC = preselectionMuHTMC2
process.preselectionElHTMC = preselectionElHTMC2
process.preselectionLepHTMC = preselectionLepHTMC2

process.weightProducer.Method = "Constant"
process.weightProducer.XS = 41.92
process.weightProducer.NumberEvts = 
process.weightProducer.Lumi = 1000  ## Lumi in 1/pb

process.eventWeightPU.MCSampleFile = "TopAnalysis/TopUtils/data/MC_PUDist_Summer11_SingleTop_TuneZ2_t_channel_7TeV_powheg_tauola.root"

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
    
)
)
