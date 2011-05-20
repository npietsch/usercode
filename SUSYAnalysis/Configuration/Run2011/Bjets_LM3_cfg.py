from BjetsPAT_cfg import *

from SUSYAnalysis.SUSYFilter.sequences.Preselection_cff import *
process.preselection = preselectionElHTMC

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
    '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_10_1_ewx.root',
    '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_11_1_bHP.root',
    '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_12_1_iZb.root',
    '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_13_1_i5B.root',
    '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_14_1_rkt.root',
    '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_15_1_kV6.root',
    '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_16_1_9wR.root',
    '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_17_1_6vt.root',
    '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_18_1_2kn.root',
    '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_19_1_FSf.root',
    '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_1_1_5Vb.root',
    '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_20_1_79O.root',
    '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_21_1_Tm8.root',
    '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_22_1_9CL.root',
    '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_2_1_kAG.root',
    '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_3_1_Oa0.root',
    '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_4_1_hYU.root',
    '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_5_1_UX9.root',
    '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_6_1_Iqr.root',
    '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_7_1_Mtt.root',
    '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_8_1_Pnb.root',
    '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_9_1_toP.root'
    )
)
