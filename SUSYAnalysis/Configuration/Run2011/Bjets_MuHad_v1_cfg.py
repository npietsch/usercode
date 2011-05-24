from BjetsData_cfg import *


from SUSYAnalysis.SUSYFilter.sequences.Preselection_cff import *
process.preselection = preselectionMuHTData
process.preselection2 = preselectionElHTData

# Choose input files
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
    '/store/user/cakir/MuHad/PAT_Data2011_MuHadv1_GJSON/d006f2bc492c2b853732556b211d6e87/Data2011_GJSON_10_1_vcC.root',
    '/store/user/cakir/MuHad/PAT_Data2011_MuHadv1_GJSON/d006f2bc492c2b853732556b211d6e87/Data2011_GJSON_11_1_AYD.root',
    '/store/user/cakir/MuHad/PAT_Data2011_MuHadv1_GJSON/d006f2bc492c2b853732556b211d6e87/Data2011_GJSON_12_1_uRR.root',
    '/store/user/cakir/MuHad/PAT_Data2011_MuHadv1_GJSON/d006f2bc492c2b853732556b211d6e87/Data2011_GJSON_13_1_4no.root',
    '/store/user/cakir/MuHad/PAT_Data2011_MuHadv1_GJSON/d006f2bc492c2b853732556b211d6e87/Data2011_GJSON_14_1_EiR.root',
    '/store/user/cakir/MuHad/PAT_Data2011_MuHadv1_GJSON/d006f2bc492c2b853732556b211d6e87/Data2011_GJSON_15_1_n77.root',
    '/store/user/cakir/MuHad/PAT_Data2011_MuHadv1_GJSON/d006f2bc492c2b853732556b211d6e87/Data2011_GJSON_16_1_Aku.root',
    '/store/user/cakir/MuHad/PAT_Data2011_MuHadv1_GJSON/d006f2bc492c2b853732556b211d6e87/Data2011_GJSON_17_1_aN7.root',
    '/store/user/cakir/MuHad/PAT_Data2011_MuHadv1_GJSON/d006f2bc492c2b853732556b211d6e87/Data2011_GJSON_18_1_9AK.root',
    '/store/user/cakir/MuHad/PAT_Data2011_MuHadv1_GJSON/d006f2bc492c2b853732556b211d6e87/Data2011_GJSON_19_1_8bj.root',
    '/store/user/cakir/MuHad/PAT_Data2011_MuHadv1_GJSON/d006f2bc492c2b853732556b211d6e87/Data2011_GJSON_1_1_Qkx.root',
    '/store/user/cakir/MuHad/PAT_Data2011_MuHadv1_GJSON/d006f2bc492c2b853732556b211d6e87/Data2011_GJSON_20_1_J7a.root',
    '/store/user/cakir/MuHad/PAT_Data2011_MuHadv1_GJSON/d006f2bc492c2b853732556b211d6e87/Data2011_GJSON_21_1_Y35.root',
    '/store/user/cakir/MuHad/PAT_Data2011_MuHadv1_GJSON/d006f2bc492c2b853732556b211d6e87/Data2011_GJSON_22_1_cH9.root',
    '/store/user/cakir/MuHad/PAT_Data2011_MuHadv1_GJSON/d006f2bc492c2b853732556b211d6e87/Data2011_GJSON_23_1_UD0.root',
    '/store/user/cakir/MuHad/PAT_Data2011_MuHadv1_GJSON/d006f2bc492c2b853732556b211d6e87/Data2011_GJSON_24_1_dI7.root',
    '/store/user/cakir/MuHad/PAT_Data2011_MuHadv1_GJSON/d006f2bc492c2b853732556b211d6e87/Data2011_GJSON_25_1_MyP.root',
    '/store/user/cakir/MuHad/PAT_Data2011_MuHadv1_GJSON/d006f2bc492c2b853732556b211d6e87/Data2011_GJSON_2_1_UIe.root',
    '/store/user/cakir/MuHad/PAT_Data2011_MuHadv1_GJSON/d006f2bc492c2b853732556b211d6e87/Data2011_GJSON_3_1_qTG.root',
    '/store/user/cakir/MuHad/PAT_Data2011_MuHadv1_GJSON/d006f2bc492c2b853732556b211d6e87/Data2011_GJSON_4_1_4s0.root',
    '/store/user/cakir/MuHad/PAT_Data2011_MuHadv1_GJSON/d006f2bc492c2b853732556b211d6e87/Data2011_GJSON_5_1_zwe.root',
    '/store/user/cakir/MuHad/PAT_Data2011_MuHadv1_GJSON/d006f2bc492c2b853732556b211d6e87/Data2011_GJSON_6_1_pDa.root',
    '/store/user/cakir/MuHad/PAT_Data2011_MuHadv1_GJSON/d006f2bc492c2b853732556b211d6e87/Data2011_GJSON_7_1_Isj.root',
    '/store/user/cakir/MuHad/PAT_Data2011_MuHadv1_GJSON/d006f2bc492c2b853732556b211d6e87/Data2011_GJSON_8_1_5yL.root',
    '/store/user/cakir/MuHad/PAT_Data2011_MuHadv1_GJSON/d006f2bc492c2b853732556b211d6e87/Data2011_GJSON_9_1_cgj.root'
    )
 )
