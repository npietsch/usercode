from BjetsPAT_cfg import *

from SUSYAnalysis.SUSYFilter.sequences.Preselection_cff import *
process.preselection = preselectionMuHTMC
process.preselection2 = preselectionElHTMC

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
    '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_9_1_Cf1.root',
        '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_8_1_LMG.root',
        '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_7_1_lXv.root',
        '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_6_1_nPJ.root',
        '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_5_1_2mS.root',
        '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_4_1_qFZ.root',
        '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_3_1_eKP.root',
        '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_2_1_g42.root',
        '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_22_1_yB6.root',
        '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_21_1_B2d.root',
        '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_20_1_MHb.root',
        '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_1_1_Ykq.root',
        '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_19_1_YmO.root',
        '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_18_1_TTZ.root',
        '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_17_1_THk.root',
        '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_16_1_w0A.root',
        '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_15_1_0HM.root',
        '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_14_1_pb7.root',
        '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_13_1_WrT.root',
        '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_12_1_L6V.root',
        '/store/user/npietsch/LM3_SUSY_sftsht_7TeV-pythia6/L1/2c6d1e1ec308dbfacf6dd66fd816c59c/Spring11_11_1_jVs.root'

    )
)
