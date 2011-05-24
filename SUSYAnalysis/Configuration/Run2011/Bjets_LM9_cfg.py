from BjetsPAT_cfg import *

from SUSYAnalysis.SUSYFilter.sequences.Preselection_cff import *
process.preselection = preselectionMuHTMC
process.preselection2 = preselectionElHTMC

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
    '/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_10_1_usV.root',
    '/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_11_1_Y6s.root',
    '/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_13_1_ey9.root',
    '/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_14_1_O8J.root',
    '/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_15_1_mha.root',
    '/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_16_1_v0e.root',
    '/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_17_1_fy7.root',
    '/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_18_1_GWY.root',
    '/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_19_1_v44.root',
    '/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_1_1_yqm.root',
    '/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_20_1_9Fk.root',
    '/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_21_1_xqW.root',
    '/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_22_1_N51.root',
    '/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_2_1_ijG.root',
    '/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_3_1_GvV.root',
    '/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_4_1_cLQ.root',
    '/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_5_1_qEY.root',
    '/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_6_1_gkS.root',
    '/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_7_1_5NN.root',
    '/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_8_1_s4K.root',
    '/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_9_1_FxO.root'
    )
 )
