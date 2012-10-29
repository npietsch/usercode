from Ruediger_cfg import *

process.weightProducer.Method = "PtHat"
process.weightProducer.XS = 10.62E+10 #2317000000
process.weightProducer.NumberEvts = 38550000
process.weightProducer.Lumi = 300000  ## Lumi in 1/pb

# Choose input files
process.source = cms.Source("PoolSource",
                            duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
                            fileNames = cms.untracked.vstring(
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_401.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_402.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_403.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_404.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_405.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_406.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_407.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_408.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_409.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_410.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_411.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_412.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_413.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_414.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_415.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_416.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_417.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_418.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_419.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_420.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_421.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_422.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_423.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_424.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_425.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_426.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_427.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_428.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_429.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_430.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_431.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_432.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_433.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_434.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_435.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_436.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_437.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_438.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_439.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_440.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_441.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_442.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_443.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_444.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_445.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_446.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_447.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_448.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_449.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_450.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_451.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_452.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_453.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_454.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_455.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_456.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_457.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_458.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_459.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_460.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_461.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_462.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_463.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_464.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_465.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_466.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_467.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_468.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_469.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_470.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_471.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_472.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_473.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_474.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_475.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_476.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_477.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_478.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_479.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_480.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_481.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_482.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_483.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_484.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_485.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_486.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_487.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_488.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_489.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_490.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_491.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_492.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_493.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_494.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_495.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_496.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_497.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_498.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_499.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_500.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_501.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_502.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_503.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_504.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_505.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_506.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_507.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_508.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_509.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_510.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_511.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_512.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_513.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_514.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_515.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_516.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_517.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_518.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_519.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_520.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_521.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_522.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_523.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_524.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_525.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_526.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_527.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_528.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_529.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_530.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_531.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_532.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_533.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_534.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_535.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_536.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_537.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_538.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_539.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_540.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_541.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_542.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_543.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_544.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_545.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_546.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_547.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_548.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_549.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_550.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_551.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_552.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_553.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_554.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_555.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_556.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_557.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_558.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_559.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_560.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_561.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_562.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_563.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_564.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_565.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_566.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_567.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_568.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_569.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_570.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_571.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_572.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_573.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_574.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_575.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_576.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_577.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_578.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_579.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_580.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_581.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_582.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_583.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_584.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_585.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_586.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_587.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_588.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_589.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_590.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_591.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_592.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_593.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_594.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_595.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_596.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_597.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_598.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_599.root',
    'file:../../../../../../Storage/QCD_Pt15to3000_Pythia_PAT_600.root'
    )
)
