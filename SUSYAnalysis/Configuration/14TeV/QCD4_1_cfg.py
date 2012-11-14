from Ruediger_cfg import *

process.weightProducer.Method = "PtHat"
process.weightProducer.XS = 10.62E+10 #2317000000
process.weightProducer.NumberEvts = 146200000
process.weightProducer.Lumi = 300000  ## Lumi in 1/pb

# Choose input files
process.source = cms.Source("PoolSource",
                            duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
                            fileNames = cms.untracked.vstring(
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1201.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1202.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1203.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1204.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1205.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1206.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1207.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1208.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1209.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1210.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1211.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1212.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1213.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1214.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1215.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1216.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1217.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1218.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1219.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1220.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1221.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1222.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1223.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1224.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1225.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1226.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1227.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1228.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1229.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1230.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1231.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1232.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1233.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1234.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1235.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1236.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1237.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1238.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1239.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1240.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1241.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1242.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1243.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1244.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1245.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1246.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1247.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1248.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1249.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1250.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1251.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1252.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1253.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1254.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1255.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1256.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1257.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1258.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1259.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1260.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1261.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1262.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1263.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1264.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1265.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1266.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1267.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1268.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1269.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1270.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1271.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1272.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1273.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1274.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1275.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1276.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1277.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1278.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1279.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1280.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1281.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1282.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1283.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1284.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1285.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1286.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1287.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1288.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1289.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1290.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1291.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1292.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1293.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1294.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1295.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1296.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1297.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1298.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1299.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1300.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1301.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1302.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1303.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1304.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1305.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1306.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1307.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1308.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1309.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1310.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1311.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1312.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1313.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1314.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1315.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1316.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1317.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1318.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1319.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1320.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1321.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1322.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1323.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1324.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1325.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1326.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1327.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1328.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1329.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1330.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1331.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1332.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1333.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1334.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1335.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1336.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1337.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1338.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1339.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1340.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1341.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1342.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1343.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1344.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1345.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1346.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1347.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1348.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1349.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples4/QCD_Pt15to3000_Pythia_PAT_1350.root'
    )
)
