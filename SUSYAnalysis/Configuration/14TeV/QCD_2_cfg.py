from Ruediger_cfg import *

process.weightProducer.Method = "PtHat"
process.weightProducer.XS = 10.62E+10 #2317000000
process.weightProducer.NumberEvts = 38550000
process.weightProducer.Lumi = 300000  ## Lumi in 1/pb

# Choose input files
process.source = cms.Source("PoolSource",
                            duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
                            fileNames = cms.untracked.vstring(
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_201.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_202.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_203.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_204.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_205.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_206.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_207.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_208.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_209.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_210.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_211.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_212.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_213.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_214.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_215.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_216.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_217.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_218.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_219.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_220.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_221.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_222.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_223.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_224.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_225.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_226.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_227.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_228.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_229.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_230.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_231.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_232.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_233.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_234.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_235.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_236.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_237.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_238.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_239.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_240.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_241.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_242.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_243.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_244.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_245.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_246.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_247.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_248.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_249.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_250.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_251.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_252.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_253.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_254.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_255.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_256.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_257.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_258.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_259.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_260.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_261.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_262.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_263.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_264.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_265.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_266.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_267.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_268.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_269.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_270.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_271.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_272.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_273.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_274.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_275.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_276.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_277.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_278.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_279.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_280.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_281.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_282.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_283.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_284.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_285.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_286.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_287.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_288.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_289.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_290.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_291.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_292.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_293.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_294.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_295.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_296.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_297.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_298.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_299.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_300.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_301.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_302.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_303.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_304.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_305.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_306.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_307.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_308.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_309.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_310.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_311.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_312.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_313.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_314.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_315.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_316.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_317.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_318.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_319.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_320.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_321.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_322.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_323.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_324.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_325.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_326.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_327.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_328.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_329.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_330.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_331.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_332.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_333.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_334.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_335.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_336.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_337.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_338.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_339.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_340.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_341.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_342.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_343.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_344.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_345.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_346.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_347.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_348.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_349.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_350.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_351.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_352.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_353.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_354.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_355.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_356.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_357.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_358.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_359.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_360.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_361.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_362.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_363.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_364.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_365.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_366.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_367.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_368.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_369.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_370.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_371.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_372.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_373.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_374.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_375.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_376.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_377.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_378.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_379.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_380.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_381.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_382.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_383.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_384.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_385.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_386.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_387.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_388.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_389.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_390.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_391.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_392.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_393.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_394.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_395.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_396.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_397.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_398.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_399.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_400.root'
    )
)
