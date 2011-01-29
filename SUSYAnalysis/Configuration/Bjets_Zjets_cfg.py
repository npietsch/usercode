from BjetsPat_cfg import *

# Choose input files
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    '/store/user/mgoerner/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/PAT_FALL10HH/148435cd71339b79cc0025730c13472a/fall10MC_9_1_rxl.root',
    '/store/user/mgoerner/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/PAT_FALL10HH/148435cd71339b79cc0025730c13472a/fall10MC_8_1_Ecw.root',
    '/store/user/mgoerner/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/PAT_FALL10HH/148435cd71339b79cc0025730c13472a/fall10MC_7_2_R2z.root',
    '/store/user/mgoerner/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/PAT_FALL10HH/148435cd71339b79cc0025730c13472a/fall10MC_6_1_GwN.root',
    '/store/user/mgoerner/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/PAT_FALL10HH/148435cd71339b79cc0025730c13472a/fall10MC_5_2_lWn.root',
    '/store/user/mgoerner/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/PAT_FALL10HH/148435cd71339b79cc0025730c13472a/fall10MC_4_2_k7Q.root',
    '/store/user/mgoerner/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/PAT_FALL10HH/148435cd71339b79cc0025730c13472a/fall10MC_3_1_nZm.root',
    '/store/user/mgoerner/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/PAT_FALL10HH/148435cd71339b79cc0025730c13472a/fall10MC_31_1_lh4.root',
    '/store/user/mgoerner/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/PAT_FALL10HH/148435cd71339b79cc0025730c13472a/fall10MC_30_1_gwx.root',
    '/store/user/mgoerner/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/PAT_FALL10HH/148435cd71339b79cc0025730c13472a/fall10MC_2_1_8O7.root',
    '/store/user/mgoerner/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/PAT_FALL10HH/148435cd71339b79cc0025730c13472a/fall10MC_29_1_2J8.root',
    '/store/user/mgoerner/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/PAT_FALL10HH/148435cd71339b79cc0025730c13472a/fall10MC_28_1_UrP.root',
    '/store/user/mgoerner/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/PAT_FALL10HH/148435cd71339b79cc0025730c13472a/fall10MC_27_1_vJ6.root',
    '/store/user/mgoerner/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/PAT_FALL10HH/148435cd71339b79cc0025730c13472a/fall10MC_26_2_ZN3.root',
    '/store/user/mgoerner/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/PAT_FALL10HH/148435cd71339b79cc0025730c13472a/fall10MC_25_2_bZD.root',
    '/store/user/mgoerner/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/PAT_FALL10HH/148435cd71339b79cc0025730c13472a/fall10MC_24_2_AmF.root',
    '/store/user/mgoerner/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/PAT_FALL10HH/148435cd71339b79cc0025730c13472a/fall10MC_23_1_tBi.root',
    '/store/user/mgoerner/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/PAT_FALL10HH/148435cd71339b79cc0025730c13472a/fall10MC_22_2_WUn.root',
    '/store/user/mgoerner/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/PAT_FALL10HH/148435cd71339b79cc0025730c13472a/fall10MC_21_1_K9T.root',
    '/store/user/mgoerner/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/PAT_FALL10HH/148435cd71339b79cc0025730c13472a/fall10MC_20_1_jM3.root',
    '/store/user/mgoerner/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/PAT_FALL10HH/148435cd71339b79cc0025730c13472a/fall10MC_1_1_LCp.root',
    '/store/user/mgoerner/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/PAT_FALL10HH/148435cd71339b79cc0025730c13472a/fall10MC_19_1_2po.root',
    '/store/user/mgoerner/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/PAT_FALL10HH/148435cd71339b79cc0025730c13472a/fall10MC_18_1_dgw.root',
    '/store/user/mgoerner/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/PAT_FALL10HH/148435cd71339b79cc0025730c13472a/fall10MC_17_1_bbe.root',
    '/store/user/mgoerner/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/PAT_FALL10HH/148435cd71339b79cc0025730c13472a/fall10MC_16_2_XCr.root',
    '/store/user/mgoerner/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/PAT_FALL10HH/148435cd71339b79cc0025730c13472a/fall10MC_15_1_8y3.root',
    '/store/user/mgoerner/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/PAT_FALL10HH/148435cd71339b79cc0025730c13472a/fall10MC_14_1_Uz1.root',
    '/store/user/mgoerner/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/PAT_FALL10HH/148435cd71339b79cc0025730c13472a/fall10MC_13_1_FtY.root',
    '/store/user/mgoerner/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/PAT_FALL10HH/148435cd71339b79cc0025730c13472a/fall10MC_12_1_Yep.root',
    '/store/user/mgoerner/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/PAT_FALL10HH/148435cd71339b79cc0025730c13472a/fall10MC_11_2_Tdu.root',
    '/store/user/mgoerner/DYJetsToLL_TuneD6T_M-50_7TeV-madgraph-tauola/PAT_FALL10HH/148435cd71339b79cc0025730c13472a/fall10MC_10_1_mae.root'
    )
)
