from BjetsPAT_cfg import *

from SUSYAnalysis.SUSYFilter.sequences.Preselection_cff import *
process.preselection = preselectionMuHTMC
process.preselection2 = preselectionElHTMC

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
