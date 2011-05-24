from BjetsPAT_cfg import *

from SUSYAnalysis.SUSYFilter.sequences.Preselection_cff import *
process.preselection = preselectionMuHTMC
process.preselection2 = preselectionElHTMC

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
    '/store/user/npietsch/LM8_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_10_1_zlb.root',
    '/store/user/npietsch/LM8_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_11_1_fJg.root',
    '/store/user/npietsch/LM8_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_12_1_jWl.root',
    '/store/user/npietsch/LM8_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_13_1_gcz.root',
    '/store/user/npietsch/LM8_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_14_1_Vgd.root',
    '/store/user/npietsch/LM8_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_15_1_TTt.root',
    '/store/user/npietsch/LM8_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_16_1_BZ6.root',
    '/store/user/npietsch/LM8_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_17_1_Ary.root',
    '/store/user/npietsch/LM8_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_18_1_GeA.root',
    '/store/user/npietsch/LM8_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_19_1_IJI.root',
    '/store/user/npietsch/LM8_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_1_1_tgU.root',
    '/store/user/npietsch/LM8_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_20_1_BQa.root',
    '/store/user/npietsch/LM8_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_21_1_PEC.root',
    '/store/user/npietsch/LM8_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_22_1_96f.root',
    '/store/user/npietsch/LM8_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_2_1_v0I.root',
    '/store/user/npietsch/LM8_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_3_1_zAt.root',
    '/store/user/npietsch/LM8_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_4_1_Ub3.root',
    '/store/user/npietsch/LM8_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_5_1_yAa.root',
    '/store/user/npietsch/LM8_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_6_1_JMG.root',
    '/store/user/npietsch/LM8_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_7_1_FA4.root',
    '/store/user/npietsch/LM8_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_8_1_9rS.root',
    '/store/user/npietsch/LM8_SUSY_sftsht_7TeV-pythia6/Spring11PAT/89614fbe8472c25559618ceb16e3da73/Spring11_9_1_4yc.root'
)
)
