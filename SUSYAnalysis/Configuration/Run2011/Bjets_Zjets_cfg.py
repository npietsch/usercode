from BjetsPAT_cfg import *

from SUSYAnalysis.SUSYFilter.sequences.Preselection_cff import *
process.preselection = preselectionMuHTMC
process.preselection2 = preselectionElHTMC

# Choose input files
process.source = cms.Source("PoolSource",
     fileNames = cms.untracked.vstring(
'/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_10_1_VV1.root',
'/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_11_1_neU.root',
'/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_12_1_QVI.root',
'/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_13_1_yfA.root',
'/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_14_1_lpB.root',
'/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_15_1_bHQ.root',
'/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_16_1_GhR.root',
'/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_17_1_jXT.root',
'/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_18_1_obz.root',
'/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_19_1_aIS.root',
'/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_1_1_GF2.root',
'/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_20_1_jkp.root',
'/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_21_1_Rty.root',
'/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_22_1_lf3.root',
'/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_23_1_kM1.root',
'/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_24_1_Pv7.root',
'/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_25_1_7aU.root',
'/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_26_1_QP6.root',
'/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_27_1_eud.root',
'/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_2_1_uTu.root',
'/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_3_1_CJZ.root',
'/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_4_1_iIe.root',
'/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_5_1_FkW.root',
'/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_6_1_Ges.root',
'/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_7_1_Y4k.root',
'/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_8_1_O9A.root',
'/store/user/npietsch/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_9_1_nkN.root'
)
)
