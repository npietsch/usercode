from Ruediger_cfg import *

process.weightProducer.Method = "PtHat"
process.weightProducer.XS = 10.62E+10 #2317000000
process.weightProducer.NumberEvts = 146200000
process.weightProducer.Lumi = 300000  ## Lumi in 1/pb

# Choose input files
process.source = cms.Source("PoolSource",
                            duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
                            fileNames = cms.untracked.vstring(
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3031.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3032.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3033.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3034.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3035.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3036.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3037.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3038.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3039.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3040.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3041.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3042.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3043.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3044.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3045.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3046.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3047.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3049.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3050.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3051.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3052.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3053.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3054.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3055.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3056.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3057.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3058.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3059.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3060.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3062.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3063.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3064.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3065.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3066.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3067.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3069.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3070.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3071.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3072.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3073.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3074.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3076.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3077.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3078.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3080.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3081.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3082.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3083.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3084.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3085.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3086.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3087.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3088.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3089.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3090.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3091.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3092.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3093.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3094.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3095.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3096.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3098.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3099.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3100.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3101.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3102.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3103.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3104.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3105.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3106.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3107.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3108.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3109.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3110.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3111.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3112.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3113.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3114.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3117.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3119.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3121.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3123.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3124.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3126.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3128.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3129.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3130.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3132.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3133.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3135.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3136.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3139.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3140.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3141.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3144.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3145.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3148.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3149.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3151.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3152.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3154.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3155.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3157.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3158.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3160.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3161.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3162.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3164.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3165.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3166.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3167.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3168.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3169.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3170.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3171.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3172.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3173.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3174.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3175.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3177.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3180.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3182.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3184.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3185.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3187.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3189.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3192.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3193.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3194.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3196.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3197.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3198.root',
'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples8/QCD_Pt15to3000_Pythia_PAT_3200.root'
)
)