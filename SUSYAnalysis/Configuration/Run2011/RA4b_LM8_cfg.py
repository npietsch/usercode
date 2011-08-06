from BjetsPAT_cfg import *

from SUSYAnalysis.SUSYFilter.sequences.Preselection_cff import *
process.preselection = preselectionMuHTMC
process.preselection2 = preselectionElHTMC

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
        '/store/user/npietsch/LM13_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_9_1_GnE.root',
        '/store/user/npietsch/LM13_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_8_1_USg.root',
        '/store/user/npietsch/LM13_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_7_1_mGF.root',
        '/store/user/npietsch/LM13_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_6_1_vNU.root',
        '/store/user/npietsch/LM13_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_5_1_htI.root',
        '/store/user/npietsch/LM13_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_4_1_M1k.root',
        '/store/user/npietsch/LM13_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_3_1_WxM.root',
        '/store/user/npietsch/LM13_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_2_1_nv8.root',
        '/store/user/npietsch/LM13_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_22_1_as7.root',
        '/store/user/npietsch/LM13_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_21_1_5D1.root',
        '/store/user/npietsch/LM13_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_20_1_GKK.root',
        '/store/user/npietsch/LM13_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_1_1_6Cy.root',
        '/store/user/npietsch/LM13_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_19_1_xM9.root',
        '/store/user/npietsch/LM13_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_18_1_Yfn.root',
        '/store/user/npietsch/LM13_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_17_1_2aB.root',
        '/store/user/npietsch/LM13_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_16_1_3wa.root',
        '/store/user/npietsch/LM13_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_15_1_6rT.root',
        '/store/user/npietsch/LM13_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_14_1_879.root',
        '/store/user/npietsch/LM13_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_13_1_DNy.root',
        '/store/user/npietsch/LM13_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_12_1_FTX.root',
        '/store/user/npietsch/LM13_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_11_1_FJv.root',
        '/store/user/npietsch/LM13_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_10_1_ekM.root'
)
)
