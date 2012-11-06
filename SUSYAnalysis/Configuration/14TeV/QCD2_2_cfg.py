from Ruediger_cfg import *

process.weightProducer.Method = "PtHat"
process.weightProducer.XS = 10.62E+10 #2317000000
process.weightProducer.NumberEvts = 66200000
process.weightProducer.Lumi = 300000  ## Lumi in 1/pb

# Choose input files
process.source = cms.Source("PoolSource",
                            duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
                            fileNames = cms.untracked.vstring(
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_601.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_602.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_603.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_604.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_605.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_606.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_607.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_608.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_609.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_610.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_611.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_612.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_613.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_614.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_615.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_616.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_617.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_618.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_619.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_620.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_621.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_622.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_623.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_624.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_625.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_626.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_627.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_628.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_629.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_630.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_631.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_632.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_633.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_634.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_635.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_636.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_637.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_638.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_639.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_640.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_641.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_642.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_643.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_644.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_645.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_646.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_647.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_648.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_649.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_650.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_651.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_652.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_653.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_654.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_655.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_656.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_657.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_658.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_659.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_660.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_661.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_662.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_663.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_664.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_665.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_666.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_667.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_668.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_669.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_670.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_671.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_672.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_673.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_674.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_675.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_676.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_677.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_678.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_679.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_680.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_681.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_682.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_683.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_684.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_685.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_686.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_687.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_688.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_689.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_690.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_691.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_692.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_693.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_694.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_695.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_696.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_697.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_698.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_699.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_700.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_701.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_702.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_703.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_704.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_705.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_706.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_707.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_708.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_709.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_710.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_711.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_712.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_713.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_714.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_715.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_716.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_717.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_718.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_719.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_720.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_721.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_722.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_723.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_724.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_725.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_726.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_727.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_728.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_729.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_730.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_731.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_732.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_733.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_734.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_735.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_736.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_737.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_738.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_739.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_740.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_741.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_742.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_743.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_744.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_745.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_746.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_747.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_748.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_749.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_750.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_751.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_752.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_753.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_754.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_755.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_756.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_757.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_758.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_759.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_761.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_763.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_767.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_780.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_783.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_784.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_785.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_786.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_787.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_788.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_789.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_790.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_791.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_794.root',
    'file:/scratch/hh/dust/naf/cms/user/npietsch/QCDSamples2/QCD_Pt15to3000_Pythia_PAT_800.root'
    )
)
