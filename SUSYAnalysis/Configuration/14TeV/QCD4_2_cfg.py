from Ruediger_cfg import *

process.weightProducer.Method = "PtHat"
process.weightProducer.XS = 10.62E+10 #2317000000
process.weightProducer.NumberEvts = 66200000
process.weightProducer.Lumi = 300000  ## Lumi in 1/pb

# Choose input files
process.source = cms.Source("PoolSource",
                            duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
                            fileNames = cms.untracked.vstring(
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1351.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1352.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1353.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1354.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1355.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1356.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1357.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1358.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1359.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1360.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1361.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1362.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1363.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1364.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1365.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1366.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1367.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1368.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1369.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1370.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1371.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1372.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1373.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1374.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1375.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1376.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1377.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1378.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1379.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1380.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1381.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1382.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1383.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1384.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1385.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1386.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1387.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1388.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1389.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1390.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1391.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1392.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1393.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1394.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1395.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1396.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1397.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1398.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1399.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1400.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1401.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1402.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1403.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1404.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1405.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1406.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1407.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1408.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1409.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1410.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1411.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1412.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1413.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1414.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1415.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1416.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1417.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1418.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1419.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1420.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1421.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1422.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1423.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1424.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1425.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1426.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1427.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1428.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1429.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1430.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1431.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1432.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1433.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1434.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1435.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1436.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1437.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1438.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1439.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1440.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1441.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1442.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1443.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1444.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1445.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1446.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1447.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1448.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1449.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1450.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1451.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1452.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1453.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1454.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1455.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1456.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1457.root'
    )
)
