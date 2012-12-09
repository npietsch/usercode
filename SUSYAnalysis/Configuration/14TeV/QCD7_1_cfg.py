from Ruediger_cfg import *

process.weightProducer.Method = "PtHat"
process.weightProducer.XS = 10.62E+10 #2317000000
process.weightProducer.NumberEvts = 146200000
process.weightProducer.Lumi = 300000  ## Lumi in 1/pb

# Choose input files
process.source = cms.Source("PoolSource",
                            duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
                            fileNames = cms.untracked.vstring(
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2401.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2402.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2404.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2405.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2406.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2407.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2408.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2410.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2412.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2413.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2414.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2415.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2417.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2420.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2421.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2422.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2423.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2424.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2425.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2426.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2427.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2428.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2429.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2430.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2431.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2432.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2434.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2435.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2436.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2438.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2439.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2440.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2441.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2442.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2444.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2446.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2447.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2449.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2450.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2451.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2452.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2453.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2454.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2455.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2456.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2457.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2459.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2460.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2461.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2462.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2463.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2464.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2465.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2467.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2469.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2470.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2471.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2472.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2473.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2475.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2476.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2477.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2478.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2479.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2480.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2481.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2482.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2483.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2484.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2486.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2487.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2488.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2489.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2490.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2493.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2494.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2495.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2496.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2497.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2498.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2499.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2500.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2502.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2503.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2504.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2505.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2506.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2507.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2508.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2509.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2510.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2511.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2512.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2513.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2514.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2516.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2517.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2518.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2519.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2521.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2522.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2523.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2524.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2525.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2526.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2527.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2528.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2529.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2530.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2531.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2532.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2533.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2534.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2535.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2536.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2537.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2538.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2539.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2540.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2541.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2542.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2543.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2544.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2547.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2548.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2549.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2550.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2552.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2553.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2554.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2555.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2556.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2557.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2558.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2559.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2560.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2561.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2562.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2563.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2564.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2565.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2566.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2567.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2568.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2569.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2570.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2571.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2572.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2573.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2574.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2575.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2576.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2577.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2578.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2579.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2580.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2581.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2582.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2583.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2584.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2585.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2586.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2587.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2588.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2589.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2590.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2591.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2592.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2593.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2597.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2598.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2599.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2601.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2602.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2603.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2604.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2605.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2606.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2607.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2608.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2609.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2610.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2613.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2614.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2615.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2616.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2617.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2618.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2619.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2620.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2622.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2623.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2624.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2625.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2626.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2627.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2628.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2631.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2632.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples7/QCD_Pt15to3000_Pythia_PAT_2633.root'
)
)
