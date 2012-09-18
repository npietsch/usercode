# -*- coding: utf-8 -*-
import FWCore.ParameterSet.Config as cms

process = cms.Process("Trigger")

## configure message logger
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.MessageLogger.categories.append('ParticleListDrawer')

# Choose input files
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/197/770/7EF0FF77-77C3-E111-941A-5404A63886EE.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/197/772/8E02C4D0-79C3-E111-9773-001D09F28EA3.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/197/774/3C5FCCD6-79C3-E111-8249-001D09F25479.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/197/885/30C899F9-2BC4-E111-B4C9-001D09F248F8.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/197/889/DAF8E779-2DC4-E111-B741-003048F118AA.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/197/891/42B538CE-2CC4-E111-8797-001D09F291D2.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/197/903/74A7E651-EAC4-E111-A28F-003048678098.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/197/931/B2B2A382-D1C4-E111-B3BD-001D09F290CE.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/011/9ACC3B1C-6BC5-E111-9D75-001D09F27067.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/022/820CDDD1-DCC5-E111-8D21-5404A63886AF.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/023/C483D7C0-D5C5-E111-8E93-001D09F23C73.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/031/EE111B5F-96C5-E111-AE9F-001D09F2B30B.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/041/E07EDEFE-ECC5-E111-80F1-003048D2C020.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/044/C4E7447F-E6C5-E111-BDC2-001D09F29597.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/045/9A8C703D-FFC5-E111-B12A-001D09F25109.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/045/D68225DF-F8C5-E111-9B8A-002481E0D790.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/045/FCDFCE72-F7C5-E111-95A3-BCAEC5329708.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/047/BC78EE43-B3C5-E111-A2F7-0025901D627C.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/048/1E111932-04C6-E111-8055-003048D374F2.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/049/AAB9323B-F2C6-E111-8308-BCAEC5364C93.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/050/50ADC9A7-00C6-E111-BC6E-001D09F2527B.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/050/86ABEFBF-1AC6-E111-A000-001D09F24353.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/063/328F8859-12C6-E111-AB6E-001D09F25460.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/063/6619F339-04C6-E111-8100-001D09F2960F.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/063/DA036DB3-07C6-E111-A8BE-001D09F2462D.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/111/9E70EB51-FBC5-E111-805D-0025901D6268.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/116/0A7930F8-77C6-E111-8C16-001D09F29169.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/116/10E3831B-69C6-E111-803C-003048F1BF66.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/116/74CDE1E9-6BC6-E111-AAEA-BCAEC5329727.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/116/B8CBCD49-7EC6-E111-B16E-001D09F2A690.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/130/2E8AE38E-30C6-E111-AB70-003048D2BB90.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/136/C689DE46-3BC6-E111-9FF7-001D09F252DA.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/150/EA29C8E7-69C6-E111-AADD-003048F11C5C.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/151/4C968938-6BC6-E111-9EBE-BCAEC518FF6B.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/152/BADA9270-6DC6-E111-8E4A-001D09F2A49C.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/160/52E0F634-7AC6-E111-AF79-001D09F24D8A.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/163/1E3FACB8-7FC6-E111-88DD-BCAEC518FF5F.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/166/E8C4AF04-86C6-E111-9AA3-001D09F2905B.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/167/0C9A3F73-89C6-E111-B72A-001D09F24D4E.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/169/3035A833-88C6-E111-84AE-001D09F23C73.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/171/AC3BEAE8-8BC6-E111-B149-BCAEC518FF62.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/176/0862F3C4-92C6-E111-B6D8-001D09F23F2A.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/185/AED4B237-A7C6-E111-8530-001D09F25267.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/192/2A8DEA34-BBC6-E111-9954-001D09F28D4A.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/197/C85D09CB-BFC6-E111-B5C7-003048678098.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/200/AEE7C958-D4C6-E111-9C32-001D09F29524.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/202/CA8D8E53-E4C6-E111-9652-001D09F24763.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/207/5CAA3D73-1BC7-E111-B669-003048F11DE2.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/207/6C63F57D-35C7-E111-9DEA-003048D2BC62.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/207/A01087B6-3EC7-E111-93DF-001D09F252E9.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/208/20D21C5E-33C7-E111-8C80-003048F1C832.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/208/A42901D7-4AC7-E111-8161-001D09F25267.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/208/BAB34C13-32C7-E111-8098-003048F1C836.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/208/C643B813-34C7-E111-84E7-001D09F2841C.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/208/D225CC63-4BC7-E111-9B0D-001D09F29524.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/208/F8321213-32C7-E111-BD57-003048F024DA.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/210/02CF26BA-3EC7-E111-8A12-003048D2BED6.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/210/1AAFD96F-2EC7-E111-9C9D-001D09F2525D.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/210/7C219595-46C7-E111-8569-001D09F29619.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/210/9EDC4BAC-32C7-E111-9917-0025B32036D2.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/211/447AC762-08C7-E111-94F6-5404A6388694.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/212/4CA6E3B8-3EC7-E111-8808-BCAEC518FF7C.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/212/763531DD-4AC7-E111-A27D-5404A638868F.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/212/7C56A476-3AC7-E111-9873-002481E0D7D8.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/212/7E15B482-3FC7-E111-8294-0025901D5E10.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/212/82B84E4D-3DC7-E111-B63D-0030486733B4.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/212/E88950DE-4AC7-E111-ACC6-0019B9F72F97.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/212/F898ED01-3EC7-E111-A1B7-001D09F297EF.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/213/50FB66A0-4DC7-E111-89CE-001D09F27067.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/214/9890069B-2BC7-E111-A2D8-001D09F2441B.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/215/7CEF8987-46C7-E111-B7CE-003048D37694.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/229/345BD8BB-45C7-E111-91F7-001D09F28E80.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/230/02E5284A-CDC7-E111-AD69-001D09F253C0.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/230/04528B2F-C1C7-E111-BBE2-001D09F241F0.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/230/08342341-B9C7-E111-9B49-5404A63886C3.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/230/085451ED-CDC7-E111-AFEA-001D09F2910A.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/230/0E4C6C71-AEC7-E111-9218-003048F1C424.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/230/1ED16F75-BCC7-E111-8BA8-00237DDC5CB0.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/230/247BAB70-BCC7-E111-9D63-003048CF94A8.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/230/2A899871-B0C7-E111-8CA1-0025B3203898.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/230/2AF7715B-D4C7-E111-9505-001D09F24399.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/230/321F6BE1-B1C7-E111-A36F-5404A63886CE.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/230/3C4DF62F-B9C7-E111-B615-485B3977172C.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/230/541BEBBD-E1C7-E111-B40C-003048D2BE12.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/230/54E5955B-D4C7-E111-B88C-001D09F29619.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/230/5AE67471-19C8-E111-A8E5-001D09F2441B.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/230/5C68BABF-ACC7-E111-BD02-003048D37694.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/230/70E97807-D0C7-E111-BC61-001D09F25460.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/230/74F75D90-B9C7-E111-93DA-5404A640A643.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/230/7EA5C834-DEC7-E111-B5EE-001D09F2462D.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/230/8050483D-B3C7-E111-BCE7-BCAEC518FF63.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/230/84ED582D-C1C7-E111-AEB2-001D09F248F8.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/230/98F0A9E2-C1C7-E111-9899-003048D37694.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/230/98FA3BDB-D7C7-E111-A2A7-003048D2C01A.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/230/A09208A8-DAC7-E111-89F2-003048673374.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/230/A0CAF42F-DEC7-E111-A85F-BCAEC518FF63.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/230/A69C4DC4-B4C7-E111-9523-001D09F24763.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/230/AE7582E8-DEC7-E111-9ACE-001D09F2AF96.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/230/D65F18A3-BDC7-E111-B80C-003048CF94A8.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/230/E49867A3-BDC7-E111-B0B9-003048F118C4.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/230/E4A6CE70-CBC7-E111-B9B6-5404A63886A0.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/230/F6CEFEA5-BDC7-E111-8D7E-003048D2BC5C.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/230/FCA62996-CEC7-E111-A4F6-003048F118C2.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/249/0475AA78-D1C7-E111-A2CA-003048F117F6.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/259/C47CF432-BFC7-E111-AA34-001D09F290BF.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/268/C0F20F0C-2BC8-E111-B4CE-003048F117F6.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/269/129DE34D-1EC8-E111-8A7B-001D09F2906A.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/269/28629A9D-19C8-E111-B7F4-0019B9F581C9.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/269/5EA6B2B2-1CC8-E111-9FEA-BCAEC518FF80.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/269/6055F305-2DC8-E111-8297-001D09F23D1D.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/269/720E4291-19C8-E111-B497-003048D2BF1C.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/269/9A1B3E23-1FC8-E111-98CE-BCAEC518FF74.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/269/9ECEDE69-30C8-E111-9D78-5404A63886EF.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/269/B44CAF69-30C8-E111-B19F-5404A63886AE.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/269/B49BC362-29C8-E111-9445-5404A63886CB.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/269/C0B585F4-2CC8-E111-B536-001D09F25460.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/269/C4961763-29C8-E111-AEEB-002481E0D646.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/269/DA71A850-41C8-E111-9978-5404A63886B4.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/269/F2C47232-2AC8-E111-8910-003048F117F6.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/270/566F91D9-C9C7-E111-AF1C-5404A63886CC.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/271/04E69AEC-46C8-E111-BE79-003048D2BCA2.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/271/502F0473-53C8-E111-A600-003048D2C0F4.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/271/56FC8D9E-57C8-E111-8E64-5404A63886D2.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/271/5A4579D5-60C8-E111-8105-003048D2BC4C.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/271/5CFC0F70-53C8-E111-AF3A-003048D3733E.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/271/5E474AFA-4BC8-E111-86D9-BCAEC518FF62.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/271/60C5B79A-59C8-E111-A426-001D09F2A465.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/271/629C547F-45C8-E111-A22C-003048F1C424.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/271/6C862362-59C8-E111-B8C7-001D09F24763.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/271/74B93B01-67C8-E111-8AE8-0025901D5D90.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/271/74BCE6A4-4CC8-E111-97F7-003048F24A04.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/271/74D7BB4C-50C8-E111-A0FB-003048F118AA.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/271/7ED19214-49C8-E111-9990-003048D2C092.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/271/828E7719-5DC8-E111-948C-003048CFB40C.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/271/82AD60C6-5CC8-E111-91F9-001D09F29146.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/271/8A25FAD5-60C8-E111-B9DC-001D09F24DA8.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/271/8E190160-55C8-E111-926A-003048D2BC4C.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/271/8E4B308C-4AC8-E111-8010-003048678110.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/271/94277FFD-6BC8-E111-A453-002481E94050.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/271/94926102-51C8-E111-ACC4-003048D2BEAA.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/271/94DACE18-49C8-E111-963F-003048D2C0F2.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/271/A8F6A04F-5BC8-E111-BFF8-003048F1182E.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/271/B8F5D2F4-51C8-E111-8A44-001D09F290CE.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/271/E07D454C-50C8-E111-983F-00237DDBE49C.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/271/E0B9AC00-6CC8-E111-9241-001D09F28D4A.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/271/E272CCB4-7DC8-E111-9A4F-BCAEC5329720.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/271/F89105ED-59C8-E111-A293-001D09F24EE3.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/271/FA7490F4-4BC8-E111-B2C0-BCAEC518FF76.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/272/1800D5D5-59C8-E111-811A-002481E0D524.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/272/3CB76867-59C8-E111-9561-0030486780E6.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/272/70405EAC-5CC8-E111-85F7-001D09F2B2CF.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/272/7226D5E6-86C8-E111-87A9-5404A63886EF.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/272/76CAA5BA-5DC8-E111-BA57-002481E0CC00.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/272/7CC7A34D-5BC8-E111-87B2-5404A6388698.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/272/905FF3B0-5BC8-E111-BAFE-003048D2C108.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/272/C2EFED2C-6EC8-E111-B899-003048D2BB58.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/272/DC6974EE-5FC8-E111-956D-003048F11C5C.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/272/E4DF6BC1-62C8-E111-A2DF-003048F117F6.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/272/FCEEB5D6-59C8-E111-B189-003048D37524.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/300/D470EDFB-57C8-E111-8A18-485B3962633D.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/310/3E425F8B-57C8-E111-BC27-5404A63886A2.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/311/F46AB0A3-5AC8-E111-811E-0025901D5C88.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/314/9A3605B3-57C8-E111-B70C-E0CB4E55365C.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/345/762D36E8-69C8-E111-BE74-0025901D6272.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/346/9AF542B2-A6C8-E111-91BF-003048F118C2.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/362/B22B35F1-90C8-E111-90A3-001D09F24353.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/363/1E0D0495-94C8-E111-8AC7-001D09F241B9.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/372/964E28C9-E1C8-E111-9FF7-003048673374.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/372/AA4423CF-FEC8-E111-9727-001D09F29619.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/372/BAF82C6B-E5C8-E111-8F98-BCAEC532971C.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/483/3C8CFB2E-DDC9-E111-BFE2-5404A63886A0.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/485/365BEDB7-25CA-E111-8CAB-003048D2C01E.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/485/5A43ADD8-2ECA-E111-9EBF-001D09F28EA3.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/485/5C616B1F-AACA-E111-B1DB-BCAEC518FF80.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/485/5EFF1FE7-29CA-E111-B73C-001D09F276CF.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/485/6296F0DA-2ECA-E111-9C6B-001D09F292D1.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/485/74A0CEB7-25CA-E111-B0FD-BCAEC5364C93.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/485/7C900D0A-33CA-E111-B42C-001D09F241F0.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/485/88450335-29CA-E111-AC4C-001D09F2AD4D.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/485/BED36EB8-25CA-E111-8C61-5404A63886BB.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/485/E44910B7-25CA-E111-9279-BCAEC518FF30.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/486/D620880D-F3C9-E111-9494-001D09F29321.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/487/086CA5B2-ADCA-E111-9091-003048F11942.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/487/08FD66E1-68CA-E111-B3B2-BCAEC532971D.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/487/18574F85-77CA-E111-A738-001D09F29533.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/487/18E7FE47-C5CA-E111-A6DC-001D09F2906A.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/487/1A461D3C-CACA-E111-8E63-001D09F2A690.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/487/1C08BDE8-A5CA-E111-AEF6-003048D3C982.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/487/20998863-7ACA-E111-85CA-001D09F2983F.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/487/221E4054-B9CA-E111-BD66-BCAEC5329702.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/487/2E28FB3C-78CA-E111-BABC-001D09F2512C.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/487/3E8CC88A-9DCA-E111-824E-003048F1C420.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/487/42C4D023-8ECA-E111-8BE0-5404A6388698.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/487/46356A53-B9CA-E111-9669-BCAEC5364C62.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/487/5E5FB822-C8CA-E111-82EE-001D09F2915A.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/487/5E7FC8A1-D7CA-E111-8D4B-001D09F2A49C.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/487/683D6B3F-7FCA-E111-8994-5404A63886CE.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/487/6886CD5C-C0CA-E111-ACD0-0019B9F581C9.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/487/6C226660-98CA-E111-B2C5-002481E0CC00.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/487/70417AC9-75CA-E111-8A9B-001D09F34488.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/487/760A8218-A5CA-E111-8CD4-5404A6388697.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/487/76A19930-ACCA-E111-907A-5404A638869C.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/487/7813213F-A7CA-E111-B1F5-BCAEC532971E.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/487/78D9B43F-FCCA-E111-BD05-BCAEC518FF89.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/487/7A7B1404-7BCA-E111-8EE9-5404A63886CB.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/487/8210C04B-D1CA-E111-8B01-0019B9F70468.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/487/860EB652-B4CA-E111-A579-001D09F25041.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/487/8CDA38C9-D4CA-E111-BA8C-001D09F29597.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/487/A437EC3F-A9CA-E111-8B4C-BCAEC518FF30.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/487/B467989A-A3CA-E111-9E85-0025901D5DF4.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/487/B6D953E1-C3CA-E111-9FF8-001D09F25109.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/487/B8E79AF4-90CA-E111-9FA4-003048F118AA.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/487/C88F8823-B7CA-E111-BB43-001D09F28D54.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/487/CC1B685C-B4CA-E111-ADD1-001D09F252E9.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/487/CEACA990-C9CA-E111-9ECB-001D09F290CE.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/487/CEADEE02-7BCA-E111-8E29-BCAEC518FF7A.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/487/D85DC333-ACCA-E111-B172-002481E0D90C.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/487/E26EAF91-C9CA-E111-B74D-001D09F251FE.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/487/EA59E146-90CA-E111-99BD-5404A63886BE.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/487/ECE3E895-D0CA-E111-8D63-0019B9F70468.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/514/52C135D0-B0CA-E111-A8EA-001D09F23F2A.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/516/66F490CB-B3CA-E111-92C6-001D09F24763.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/520/E609C729-B7CA-E111-A1EE-003048F11C5C.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/522/063D59AA-23CB-E111-9C64-001D09F29524.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/522/1E365961-24CB-E111-AF08-0019B9F72CE5.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/522/8AE0B0F8-82CB-E111-91E4-001D09F2B2CF.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/522/AC754A8C-21CB-E111-8DDE-001D09F29524.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/522/CEABBB58-1DCB-E111-983F-5404A63886EF.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/522/E09F95D2-2CCB-E111-897D-001D09F24399.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/522/F2CFC41A-19CB-E111-AAD3-BCAEC5329703.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/522/F8B55067-18CB-E111-8B0F-5404A63886CB.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/523/74EA08C6-F1CA-E111-9F0E-0025901D62A6.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/713/8AC498CC-BECC-E111-B7BD-E0CB4E55365D.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/719/7C404937-C7CC-E111-A8DB-0025B32445E0.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/720/FE26045A-C7CC-E111-B23B-BCAEC5329701.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/722/1CD3F30B-CFCC-E111-9DEC-00215AEDFD98.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/744/9CACFB71-D0CC-E111-B46B-001D09F25460.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/748/22995DAE-E2CC-E111-A7FD-003048F024FA.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/765/A85BA9D8-E7CC-E111-8BBF-003048F118AC.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/791/DEE01822-0ACD-E111-BA47-5404A63886AF.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/846/14562693-67CD-E111-BAFA-001D09F29597.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/856/F614FF6D-8BCD-E111-B8C6-003048678098.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/859/1290E575-92CD-E111-82E4-0025901D5D80.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/860/80768E31-93CD-E111-9DD2-0025B320384C.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/898/BC85F1ED-D7CD-E111-8D80-BCAEC5329700.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/910/243301B0-63CE-E111-BEBB-001D09F2437B.root',
    '/store/data/Run2012C/DoubleMu/AOD/PromptReco-v1/000/198/913/C0EB7FD1-78CE-E111-BB63-003048D37580.root'   
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100),
    skipEvents = cms.untracked.uint32(1)
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('Trigger.root')
                                   )

process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")

## dummy output module
process.out = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring('drop *'),
    dropMetaData = cms.untracked.string("DROPPED"),                                     
    fileName = cms.untracked.string('Summer12.root')
)

#------------------------------------------------------------------------------
# Import modules for preselection (trigger, vertex selection, event cleaning)
#------------------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.Preselection_cff")

#------------------------------------------------------------------------------
# Import modules and sequences for selection of objects and events
#------------------------------------------------------------------------------

process.load("SUSYAnalysis.SUSYFilter.sequences.BjetsSelection_cff")

#------------------------------------------------------------------------------
# Import and configure modules for trigger study 
#------------------------------------------------------------------------------

# import and configure trigger layer 1 modules
#------------------------------------------------------------------------------
process.load("PhysicsTools.PatAlgos.triggerLayer1.triggerProducer_cff")

# example given at http://cmssw.cvs.cern.ch/cgi-bin/cmssw.cgi/UserCode/npietsch/SUSYAnalysis/Configuration/Run2011/Trigger_cfg.py?hideattic=0&revision=1.3&view=markup


# import and configure test analyzer
#------------------------------------------------------------------------------
from SUSYAnalysis.SUSYAnalyzer.TestAnalyzer_cfi import *

# clone analyzer module named testAnalysis
process.test = testAnalysis.clone()

# configure module test, e.g.
process.test.jets = "goodJets"

#------------------------------------------------------------------------------
# From PhysicsTools/Configuration/test/SUSY_pattuple_cfg.py
#------------------------------------------------------------------------------

## NP: Disregard this for the moment

#-- VarParsing ----------------------------------------------------------------
import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing ('standard')

#  for SusyPAT configuration
options.register('GlobalTag', "GR_P_V41_AN1::All", VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string, "GlobalTag to use (if empty default Pat GT is used)")
options.register('mcInfo', False, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.int, "process MonteCarlo data")
options.register('jetCorrections', 'L1FastJet', VarParsing.VarParsing.multiplicity.list, VarParsing.VarParsing.varType.string, "Level of jet corrections to use: Note the factors are read from DB via GlobalTag")
options.jetCorrections.append('L2Relative')
options.jetCorrections.append('L3Absolute')
options.jetCorrections.append('L2L3Residual')
options.register('hltName', 'HLT', VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string, "HLT menu to use for trigger matching")
options.register('mcVersion', '', VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string, "Currently not needed and supported")
options.register('jetTypes', 'AK5PF', VarParsing.VarParsing.multiplicity.list, VarParsing.VarParsing.varType.string, "Additional jet types that will be produced (AK5Calo and AK5PF, cross cleaned in PF2PAT, are included anyway)")
options.register('hltSelection', '', VarParsing.VarParsing.multiplicity.list, VarParsing.VarParsing.varType.string, "hlTriggers (OR) used to filter events")
options.register('doValidation', False, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.int, "Include the validation histograms from SusyDQM (needs extra tags)")
options.register('doExtensiveMatching', False, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.int, "Matching to simtracks (needs extra tags)")
options.register('doSusyTopProjection', False, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.int, "Apply Susy selection in PF2PAT to obtain lepton cleaned jets (needs validation)")
options.register('addKeep', '', VarParsing.VarParsing.multiplicity.list, VarParsing.VarParsing.varType.string, "Additional keep and drop statements to trim the event content")


#-- Calibration tag -----------------------------------------------------------
if options.GlobalTag:
    process.GlobalTag.globaltag = options.GlobalTag


#-- import SUSY PAT sequence --------------------------------------------------
from PhysicsTools.Configuration.SUSY_pattuple_cff import addDefaultSUSYPAT, getSUSY_pattuple_outputCommands

addDefaultSUSYPAT(process,options.mcInfo,options.hltName,options.jetCorrections,options.mcVersion,options.jetTypes,options.doValidation,options.doExtensiveMatching,options.doSusyTopProjection)

#------------------------------------------------------------------------------
# Type-1 MET corrections
#------------------------------------------------------------------------------

process.load("JetMETCorrections.Type1MET.pfMETCorrections_cff")
process.load("JetMETCorrections.Type1MET.pfMETsysShiftCorrections_cfi")
## if isMC:
##   process.pfJetMETcorr.jetCorrLabel = "ak5PFL1FastL2L3"
##   process.pfMEtSysShiftCorr.parameter = process.pfMEtSysShiftCorrParameters_2012runAvsNvtx_mc
## else:
process.pfJetMETcorr.jetCorrLabel = "ak5PFL1FastL2L3Residual"
process.pfMEtSysShiftCorr.parameter = process.pfMEtSysShiftCorrParameters_2012runAvsNvtx_data

process.patPFMETs = process.patMETs.clone(
             metSource = cms.InputTag('pfMet'),
             addMuonCorrections = cms.bool(False),
             #genMETSource = cms.InputTag('genMetTrue'),
             #addGenMET = cms.bool(True)
             )
process.pfType1CorrectedMet.applyType0Corrections = cms.bool(False)
process.pfType1CorrectedMet.srcType1Corrections = cms.VInputTag(
    cms.InputTag('pfJetMETcorr', 'type1') ,
    cms.InputTag('pfMEtSysShiftCorr')  
)
process.patPFMETsTypeIcorrected = process.patPFMETs.clone(
             metSource = cms.InputTag('pfType1CorrectedMet'),
             )

## process.p += process.pfMEtSysShiftCorrSequence
## process.p += process.producePFMETCorrections
## process.p += process.patPFMETsTypeIcorrected


#------------------------------------------------------------------------------
# Execution path
#------------------------------------------------------------------------------

process.p = cms.Path(# execute producer modules
                     process.susyPatDefaultSequence *

                     process.pfMEtSysShiftCorrSequence *
                     process.producePFMETCorrections *
                     process.patPFMETsTypeIcorrected *
                     
                     process.createObjects *
                     # execute analyzer and filter modules
                     process.preselection *
                     process.test *
                     process.muonSelection *
                     process.jetSelection *
                     process.HTSelection *
                     process.metSelection
                     )
