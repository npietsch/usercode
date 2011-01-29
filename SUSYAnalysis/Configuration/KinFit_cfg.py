import FWCore.ParameterSet.Config as cms

process = cms.Process("Bjets")

## configure message logger
process.load("FWCore.MessageLogger.MessageLogger_cfi")
#process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.MessageLogger.categories.append('ParticleListDrawer')

# Choose input files
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(

    #'file:/afs/naf.desy.de/user/n/npietsch/CMSSW_3_8_7/src/testfile.root'

    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/0496C14C-9BE4-DF11-8C37-0030485A3C51.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/0815F007-F2E4-DF11-AA69-A4BADB3CE8FE.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/083AC44F-A2E4-DF11-97C8-00D0680BF90E.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/0CA389A7-58E5-DF11-84D6-485B39800BF0.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/18813034-73E4-DF11-9834-00145E552567.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/20F923B1-91E4-DF11-B3A0-00D0680BF898.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/28AFECEC-A1E4-DF11-9CC3-003048D47677.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/321C5A90-8DE4-DF11-8BC6-00304879D32A.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/3610FFEC-9DE4-DF11-951B-00D0680BF88E.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/3E9594AB-99E4-DF11-AAAE-00D0680BF8EE.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/4C8991CD-82E4-DF11-AA8F-003048D4114A.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/58B0F662-C3E4-DF11-87E8-0015172C03DF.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/5CEF23B3-99E4-DF11-B75B-003048CDCCDA.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/5E37586A-82E4-DF11-AC86-00D0680BF9B6.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/62AE2877-7FE4-DF11-B15B-0022191F51AF.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/66826EB9-CEE4-DF11-8943-00221983E092.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/6A1E9722-7AE4-DF11-B50C-00145E5514B4.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/742838F3-25E5-DF11-AA83-A4BADB3CF208.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/74A8633D-E0E4-DF11-913C-A4BADB3D0073.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/84AC6991-B3E4-DF11-9929-00D0680BF95C.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/864CB3E0-7DE4-DF11-8E29-001D0967517A.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/86FFADED-AEE4-DF11-A9BD-0022192050A7.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/88755089-58E4-DF11-B0EC-001517255EB3.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/8AA4394F-CDE4-DF11-837B-003048CECB02.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/9A6D3BC8-C9E4-DF11-BB6F-003048F8E8B0.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/A2A2D9CB-95E4-DF11-84BB-00D0680BF968.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/A6E03BCF-FCE4-DF11-9E0F-A4BADB3CF509.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/B46F139B-99E4-DF11-BFE2-00D0680BF87C.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/BC8A8D35-B2E4-DF11-A925-003048C5D91E.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/BCF11959-F0E4-DF11-9885-001F29658458.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/C0876495-7AE4-DF11-B7D5-001EC9EB9223.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/C4EA2571-A8E4-DF11-9A2C-0022191F5E57.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/C8627527-77E4-DF11-B83F-0015172C03DF.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/CE3E5F2E-63E4-DF11-95CA-00145E5518E5.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/D4C2A8BE-6DE4-DF11-BDDF-003048D4EEAB.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/DA02468E-B0E4-DF11-9788-0015172C051D.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/DAA81DBC-7DE4-DF11-A178-00D0680B8824.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/E66A3DEA-8EE4-DF11-A414-001D096766B0.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/E8E8F872-8EE4-DF11-97C4-003048D4EEBE.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/EEA5EC66-61E4-DF11-B24E-003048D4766A.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/F4C4DBEA-A0E4-DF11-A7FC-00145E551E68.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/F8116D96-A4E4-DF11-9AF0-0030487CAB52.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/FA42A46A-5CE4-DF11-949F-00D0680BF87C.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0006/FA9178C2-95E4-DF11-BC72-003048D4762A.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/0AEEA039-57E5-DF11-93FD-E0CB4E29C4E4.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/1672DB82-5CE5-DF11-989F-485B39800B9F.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/18675F46-41E5-DF11-96E3-A4BADB3CF8F5.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/1A03E45A-73E5-DF11-8981-003048C5D19A.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/1C59AB17-BBE4-DF11-8534-00D0680BF8B8.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/1C6A891D-34E5-DF11-9DDF-0030487CAA50.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/1E98F377-35E5-DF11-A8C2-003048F9888E.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/200D7E78-F2E4-DF11-A028-0030487DA36C.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/2067E02E-D0E4-DF11-A65F-00D0680BF954.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/22C71F95-59E5-DF11-8D31-E0CB4E55365A.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/30F3F91B-00E5-DF11-8CFD-00145E551A9B.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/3CB60495-2AE5-DF11-9638-003048792C0E.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/3EE1C1E4-09E5-DF11-B215-00248CB320C3.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/3EEA150C-30E5-DF11-AF17-003048F9857A.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/3EF12C3E-E0E4-DF11-8367-003048D4113B.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/4064F457-E4E4-DF11-91BD-003048F9888C.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/40C7A7F7-6EE5-DF11-B88A-003048CAA6B0.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/44818A6A-C5E4-DF11-9C3A-00D0680BF8F0.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/46F6C34C-63E6-DF11-BC58-00261834B65A.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/4E8C76F6-E7E4-DF11-90D5-0015172C66D6.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/4EF968F6-BFE4-DF11-9750-00D0680BF8B8.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/5E041610-3DE5-DF11-BAF6-001F29659BB2.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/5EF968C9-4AE5-DF11-9FCD-A4BADB3CF208.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/680ED6A6-C3E4-DF11-82A0-00144F45F56E.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/681FE665-47E5-DF11-9A18-A4BADB3CEC68.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/6EFEC75C-EEE4-DF11-90B5-001D096763B3.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/70D04A96-4EE5-DF11-AF8C-003048D4EF1D.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/720C38E5-E3E4-DF11-A3BC-00145E5519C0.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/7C746AF8-B3E4-DF11-9CDE-001D09675139.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/828C09A9-09E5-DF11-8CE2-003048D47673.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/863C65C3-DAE4-DF11-BD27-00D0680BF9E4.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/86DD3818-20E5-DF11-BACC-00248C855FE4.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/8A505727-58E5-DF11-85A2-E0CB4E19F9A9.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/8E0BB58A-D3E4-DF11-88FC-00D0680BF97C.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/8E861B6E-40E5-DF11-837C-001F29656386.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/AE72E0BF-CDE4-DF11-9862-00145E55304D.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/B0200D27-D5E4-DF11-A771-00145E5570C7.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/B6E0C503-42E5-DF11-8FD0-A4BADB3CF509.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/BCB92602-40E5-DF11-ACF5-A4BADB3D0073.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/CC1536C8-3FE5-DF11-9ACC-A4BADB3CF8F5.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/D6C3133A-C5E4-DF11-A19D-001D09675143.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/DC839AF2-5AE5-DF11-B008-E0CB4E29C4DD.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/E48C994A-F8E4-DF11-90DB-00145E5522B5.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/EC9962B2-FDE4-DF11-9360-0015172C08F5.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/EE7D6DD7-CEE4-DF11-AF24-00151725603F.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/F4259099-04E5-DF11-A66A-00238B172271.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/F4BFF942-70E5-DF11-99EF-003048CAA6B0.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0007/FCAF0D20-19E5-DF11-82CA-003048F98864.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0008/02126537-ABE5-DF11-8A96-001F2965744C.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0008/34907473-AAE5-DF11-BDF1-00144F4525AE.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0008/48FB6208-44E5-DF11-95B0-A4BADB3D004C.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0008/5A2B37DE-6BE5-DF11-A5D5-00145E551CD6.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0008/62E98801-AEE5-DF11-95A6-003048F9888E.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0008/788BCB6C-ACE5-DF11-A13C-90E6BA442F1F.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0008/9C7AD216-ACE5-DF11-BE50-001517255D36.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0008/B28EE7AE-48E5-DF11-9F45-001F29651428.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0008/B2D39D4C-63E6-DF11-8CFA-003048CEB070.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0008/D8F33E3F-58E5-DF11-9FCC-0026B9548CB5.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0008/DC4963A1-E0E5-DF11-807E-00D0680BF898.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0009/6EE559BE-11E7-DF11-B575-00145E5513C1.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0009/E847D402-12E7-DF11-97C5-003048D4EF1D.root',
    '/store/mc/Fall10/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/START38_V12-v2/0009/E8B2CA4D-42E7-DF11-988C-90E6BA442F16.root'
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000),
    skipEvents = cms.untracked.uint32(0)
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('Bjets.root')
                                   )

process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = cms.string('GR_R_38X_V14::All')


#-------------------------------------------------
# PAT configuration
#-------------------------------------------------

## std sequence for pat
process.load("PhysicsTools.PatAlgos.patSequences_cff")

from PhysicsTools.PatAlgos.tools.cmsswVersionTools import run36xOn35xInput

## remove MC matching, photons, taus and cleaning from PAT default sequence
from PhysicsTools.PatAlgos.tools.coreTools import *
## removeMCMatching(process, ['All'])

#removeSpecificPATObjects(process,
#                         ['Photons'],  # 'Tau' has currently been taken out due to problems with tau discriminators
#                         outputInProcess=False)

#removeCleaning(process,
#               outputInProcess=False)

process.patJetCorrFactors.payload = 'AK5Calo'
# For data:
#process.patJetCorrFactors.levels = ['L2Relative', 'L3Absolute', 'L2L3Residual', 'L5Flavor', 'L7Parton']
# For MC:
process.patJetCorrFactors.levels = ['L2Relative', 'L3Absolute']
#process.patJetCorrFactors.flavorType = "T"

# embed IsoDeposits
process.patMuons.isoDeposits = cms.PSet(
    tracker = cms.InputTag("muIsoDepositTk"),
    ecal    = cms.InputTag("muIsoDepositCalByAssociatorTowers","ecal"),
    hcal    = cms.InputTag("muIsoDepositCalByAssociatorTowers","hcal"),
    user    = cms.VInputTag(
                            cms.InputTag("muIsoDepositCalByAssociatorTowers","ho"),
                            cms.InputTag("muIsoDepositJets")
                            ),
    )
process.patMuons.usePV = False

## add PF MET
from PhysicsTools.PatAlgos.tools.metTools import addPfMET
addPfMET(process, 'PF')

## Add particle flow jets
from PhysicsTools.PatAlgos.tools.jetTools import *

addJetCollection(process,cms.InputTag('ak5PFJets'),'AK5','PF',
                 doJTA        = True,
                 doBTagging   = True,
                 jetCorrLabel = ('AK5PF', ['L2Relative', 'L3Absolute']),
                 doType1MET   = False,
                 doL1Cleaning = False,
                 doL1Counters = False,
                 genJetCollection=None,
                 doJetID      = True,
                 )

## remove TagInfos from jets to run on AOD
process.patJets.addTagInfos = False

## produce cut based electron IDs
process.load("SUSYAnalysis.SUSYAnalyzer.simpleEleIdSequence_cff")

process.patElectronIDs = cms.Sequence(process.simpleEleIdSequence)
process.makePatElectrons = cms.Sequence(process.electronMatch*process.patElectronIDs*process.patElectronIsolation*process.patElectrons)

process.patElectrons.addElectronID = cms.bool(True)
process.patElectrons.electronIDSources = cms.PSet(
    simpleEleId95relIso= cms.InputTag("simpleEleId95relIso"),
    simpleEleId90relIso= cms.InputTag("simpleEleId90relIso"),
    simpleEleId85relIso= cms.InputTag("simpleEleId85relIso"),
    simpleEleId80relIso= cms.InputTag("simpleEleId80relIso"),
    simpleEleId70relIso= cms.InputTag("simpleEleId70relIso"),
    simpleEleId60relIso= cms.InputTag("simpleEleId60relIso"),
    simpleEleId95cIso= cms.InputTag("simpleEleId95cIso"),
    simpleEleId90cIso= cms.InputTag("simpleEleId90cIso"),
    simpleEleId85cIso= cms.InputTag("simpleEleId85cIso"),
    simpleEleId80cIso= cms.InputTag("simpleEleId80cIso"),
    simpleEleId70cIso= cms.InputTag("simpleEleId70cIso"),
    simpleEleId60cIso= cms.InputTag("simpleEleId60cIso"),
)

#------------------------------------------------
# Create Gen Events 
#------------------------------------------------

process.load("SUSYAnalysis.SUSYEventProducers.sequences.SUSYGenEvent_cff")
# set to 2,3,4,5
process.SUSYGenEvt.Generation = 3
process.load("TopQuarkAnalysis.TopEventProducers.sequences.ttGenEvent_cff")

#------------------------------------------------
# Gen Event Selection 
#------------------------------------------------

from SUSYAnalysis.SUSYEventProducers.producers.SUSYGenEvtFilter_cfi import *
process.SUSYGenEventFilter = SUSYGenEventFilter.clone(cut="GluinoGluinoDecay")

from TopQuarkAnalysis.TopEventProducers.producers.TtGenEvtFilter_cfi import *
process.ttGenEventFilter = ttGenEventFilter.clone(cut="isSemiLeptonic")

#------------------------------------------------
# Example Event Selection
#------------------------------------------------

# Trigger + Noise cleaning sequence
process.load("SUSYAnalysis.SUSYFilter.sequences.RAPreselection_cff")
process.scrapingVeto.thresh = 0.15 ## <-- for MC

# Object Selection
process.load("SUSYAnalysis.SUSYFilter.sequences.BjetsSelection_cff")

process.leptonSelection.electronSource = "goodElectrons"
process.leptonSelection.muonSource = "goodMuons"                           
process.leptonSelection.minNumber = 1

process.leptonVeto.electronSource = "vetoElectrons"
process.leptonVeto.muonSource = "vetoMuons"                           
process.leptonVeto.maxNumber = 1

#------------------------------------------------
# Sequence for analysis of single objects
#------------------------------------------------

process.load("SUSYAnalysis.SUSYAnalyzer.sequences.singleObjectsAnalysis_cff")

# Example how to change input tags:
process.analyzeMuonKinematics.src = "goodMuons"
process.analyzeElectronKinematics.src = "goodElectrons"
process.analyzeJetKinematics.src = "goodJets"

#------------------------------------------------
# Modules for analysis on generator level
#------------------------------------------------

from SUSYAnalysis.SUSYAnalyzer.SUSYGenEventAnalyzer_cfi import analyzeSUSYGenEvt

# change input tags to consider only selected Jets
analyzeSUSYGenEvt.jets = "goodJets"
analyzeSUSYGenEvt.bjets = "mediumBJets"
analyzeSUSYGenEvt.matchedbjets = "matchedBJets"
analyzeSUSYGenEvt.matchedqjets = "matchedLightJets"
analyzeSUSYGenEvt.matchedmuons = "goodMuons"
analyzeSUSYGenEvt.matchedelectrons = "goodElectrons"

process.analyzeSUSYGenEvt1 = analyzeSUSYGenEvt.clone()
process.analyzeSUSYGenEvt2 = analyzeSUSYGenEvt.clone()
process.analyzeSUSYGenEvt3 = analyzeSUSYGenEvt.clone()
process.analyzeSUSYGenEvt4 = analyzeSUSYGenEvt.clone()
process.analyzeSUSYGenEvt5 = analyzeSUSYGenEvt.clone()

from SUSYAnalysis.SUSYAnalyzer.SUSYAnalyzer_cfi import analyzeSUSY
analyzeSUSY.jets = "goodJets"
analyzeSUSY.muons = "goodMuons"
analyzeSUSY.electrons = "goodElectrons"

process.analyzeSUSY1 = analyzeSUSY.clone()
process.analyzeSUSY2 = analyzeSUSY.clone()
process.analyzeSUSY3 = analyzeSUSY.clone()
process.analyzeSUSY4 = analyzeSUSY.clone()
process.analyzeSUSY5 = analyzeSUSY.clone()

from SUSYAnalysis.SUSYAnalyzer.BjetsAnalyzer_cfi import analyzeBjets
analyzeBjets.jets = "goodJets"
analyzeBjets.muons = "goodMuons"
analyzeBjets.electrons = "goodElectrons"
analyzeBjets.bjets = "mediumBJets"

process.analyzeBjets1 = analyzeBjets.clone()
process.analyzeBjets2 = analyzeBjets.clone()
process.analyzeBjets3 = analyzeBjets.clone()
process.analyzeBjets4 = analyzeBjets.clone()
process.analyzeBjets5 = analyzeBjets.clone()

#-------------------------------------------------
# Additional tools
#-------------------------------------------------

## #process.load("TopQuarkAnalysis.TopEventProducers.sequences.ttSemiLepEvtBuilder_cff")

## from TopQuarkAnalysis.TopEventProducers.sequences.ttSemiLepEvtBuilder_cff import *

## addTtSemiLepHypotheses(process,
##                        ["kGeom", "kWMassDeltaTopMass", "kWMassMaxSumPt", "kMaxSumPtWMass", "kMVADisc", "kKinFit"]
##                        )

## addTtSemiLepHypotheses(process,
##                        ["kKinFit"]
##                        )

#removeTtSemiLepHypGenMatch(process)

process.load("SUSYAnalysis.SUSYEventProducers.sequences.makeTtSemiLepMuonEvent_cff")
process.load("SUSYAnalysis.SUSYEventProducers.sequences.makeTtSemiLepElectronEvent_cff")

from TopAnalysis.TopAnalyzer.HypothesisKinFit_cfi import *

process.analyzeMuonHypothesisKinFit = analyzeHypothesisKinFit.clone()
process.analyzeMuonHypothesisKinFit.src = "ttSemiLepMuonEvent"

process.analyzeElectronHypothesisKinFit = analyzeHypothesisKinFit.clone()
process.analyzeElectronHypothesisKinFit.src = "ttSemiLepElectronEvent"

#-------------------------------------------------
# Temp
#-------------------------------------------------

## produce printout of particle listings (for debugging)
#process.load("TopQuarkAnalysis.TopEventProducers.sequences.printGenParticles_cff")


#-------------------------------------------------
# Selection paths
#-------------------------------------------------

process.RA4Selection = cms.Path(#process.printGenParticles *
                                process.patDefaultSequence *
                                process.goodObjects *
                                process.matchedGoodObjects *
                                #process.makeGenEvt *
                                process.makeSUSYGenEvt *
                                #process.makeTtSemiLepMuonEvent *
                                #process.makeTtSemiLepElectronEvent *
                                #process.SUSYGenEventFilter *
                                process.preselection *
                                process.threeGoodJets *
                                process.analyzeSUSYGenEvt1 *
                                process.analyzeSUSY1 *
                                process.analyzeBjets1 *
                                process.singleObjectsAnalysis1 *
                                process.fourGoodJets *
                                process.analyzeSUSYGenEvt2 *
                                process.analyzeSUSY2 *
                                process.analyzeBjets2 *
                                process.singleObjectsAnalysis2*
                                
                                process.metSelection *
                                process.analyzeSUSYGenEvt3 *
                                process.analyzeSUSY3 *
                                process.analyzeBjets3 *
                                process.singleObjectsAnalysis3 *
                                
                                process.fourMediumBJets *
                                process.analyzeSUSYGenEvt4 *
                                process.analyzeSUSY4 *
                                process.analyzeBjets4 *
                                process.singleObjectsAnalysis4 *

                                process.leptonSelection *
                                #process.analyzeMuonHypothesisKinFit *
                                #process.analyzeElectronHypothesisKinFit *
                                process.analyzeSUSYGenEvt5 *
                                process.analyzeSUSY5 *
                                process.analyzeBjets5 *
                                process.singleObjectsAnalysis5
                                )

