from BjetsPAT_cfg import *

from SUSYAnalysis.SUSYFilter.sequences.Preselection_cff import *
process.preselection = preselectionMuHTMC
process.preselection2 = preselectionElHTMC

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
'/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_10_2_vSs.root',
'/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_11_2_hIa.root',
'/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_12_2_vxu.root',
'/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_13_2_KuO.root',
'/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_14_2_ueG.root',
'/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_15_1_f0D.root',
'/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_16_2_PwI.root',
'/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_17_2_H0p.root',
'/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_18_1_83t.root',
'/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_1_4_PQY.root',
'/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_20_1_GxY.root',
'/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_21_1_OKh.root',
'/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_22_3_DWk.root',
'/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_2_2_Nlw.root',
'/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_3_2_xqm.root',
'/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_4_1_Ntn.root',
'/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_5_1_gMK.root',
'/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_6_1_alS.root',
'/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_7_1_HJo.root',
'/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_8_1_vqj.root',
'/store/user/npietsch/LM9_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_9_2_wZR.root'
)
 )
