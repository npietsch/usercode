# Auto generated configuration file
# using: 
# Revision: 1.341.2.2 
# Source: /local/reps/CMSSW.admin/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: QCD_Pt_30_7TeV_herwigpp_cff.py -s GEN,FASTSIM,HLT --pileup=NoPileUp --conditions auto:mc --datatier GEN-SIM-DIGI-RECO --eventcontent AODSIM -n 10 --no_exec
import FWCore.ParameterSet.Config as cms

process = cms.Process('HLT')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('FastSimulation.Configuration.EventContent_cff')
process.load('FastSimulation.PileUpProducer.PileUpSimulator_NoPileUp_cff')
process.load('FastSimulation.Configuration.Geometries_MC_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('FastSimulation.Configuration.FamosSequences_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedParameters_cfi')
process.load('FastSimulation.Configuration.HLT_GRun_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.4 $'),
    annotation = cms.untracked.string('QCD_Pt_30_7TeV_herwigpp_cff.py nevts:10'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition

process.AODSIMoutput = cms.OutputModule("PoolOutputModule",
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    outputCommands = process.AODSIMEventContent.outputCommands,
    fileName = cms.untracked.string('PointA3.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RECO')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Additional output definition

# Other statements
process.famosSimHits.SimulateCalorimetry = True
process.famosSimHits.SimulateTracking = True
process.simulation = cms.Sequence(process.simulationWithFamos)
process.HLTEndSequence = cms.Sequence(process.reconstructionWithFamos)
process.Realistic7TeV2011CollisionVtxSmearingParameters.type = cms.string("BetaFunc")
process.famosSimHits.VertexGenerator = process.Realistic7TeV2011CollisionVtxSmearingParameters
process.famosPileUp.VertexGenerator = process.Realistic7TeV2011CollisionVtxSmearingParameters
process.GlobalTag.globaltag = 'MC_44_V7::All'

process.generator = cms.EDFilter("ThePEGGeneratorFilter",
    ue_2_3 = cms.vstring('cd /Herwig/UnderlyingEvent', 
        'set KtCut:MinKT 4.0', 
        'set UECuts:MHatMin 8.0', 
        'set MPIHandler:InvRadius 1.5', 
        'cd /'),
    pdfMRST2001 = cms.vstring('cd /Herwig/Partons', 
        'create Herwig::MRST MRST2001 HwMRST.so', 
        'setup MRST2001 ${HERWIGPATH}/PDF/mrst/2001/lo2002.dat', 
        'set MRST2001:RemnantHandler HadronRemnants', 
        'cp MRST2001 cmsPDFSet', 
        'cd /'),
    ue_2_4 = cms.vstring('cd /Herwig/UnderlyingEvent', 
        'set KtCut:MinKT 4.3', 
        'set UECuts:MHatMin 8.6', 
        'set MPIHandler:InvRadius 1.2', 
        'cd /'),
    cm7TeV = cms.vstring('set /Herwig/Generators/LHCGenerator:EventHandler:LuminosityFunction:Energy 7000.0', 
        'set /Herwig/Shower/Evolver:IntrinsicPtGaussian 2.0*GeV'),
    powhegDefaults = cms.vstring('cp /Herwig/Partons/MRST-NLO /cmsPDFSet', 
        'set /Herwig/Particles/p+:PDF    /Herwig/Partons/MRST-NLO', 
        'set /Herwig/Particles/pbar-:PDF /Herwig/Partons/MRST-NLO', 
        'create Herwig::O2AlphaS O2AlphaS', 
        'set /Herwig/Generators/LHCGenerator:StandardModelParameters:QCD/RunningAlphaS O2AlphaS', 
        'cd /Herwig/Shower', 
        'set KinematicsReconstructor:ReconstructionOption General', 
        'create Herwig::PowhegEvolver PowhegEvolver HwPowhegShower.so', 
        'set ShowerHandler:Evolver PowhegEvolver', 
        'set PowhegEvolver:ShowerModel ShowerModel', 
        'set PowhegEvolver:SplittingGenerator SplittingGenerator', 
        'set PowhegEvolver:MECorrMode 0', 
        'create Herwig::DrellYanHardGenerator DrellYanHardGenerator', 
        'set DrellYanHardGenerator:ShowerAlpha AlphaQCD', 
        'insert PowhegEvolver:HardGenerator 0 DrellYanHardGenerator', 
        'create Herwig::GGtoHHardGenerator GGtoHHardGenerator', 
        'set GGtoHHardGenerator:ShowerAlpha AlphaQCD', 
        'insert PowhegEvolver:HardGenerator 0 GGtoHHardGenerator'),
    reweightConstant = cms.vstring('mkdir /Herwig/Weights', 
        'cd /Herwig/Weights', 
        'create ThePEG::ReweightConstant reweightConstant ReweightConstant.so', 
        'cd /', 
        'set /Herwig/Weights/reweightConstant:C 1', 
        'insert SimpleQCD:Reweights[0] /Herwig/Weights/reweightConstant'),
    lheDefaultPDFs = cms.vstring('cd /Herwig/EventHandlers', 
        'set LHEReader:PDFA /cmsPDFSet', 
        'set LHEReader:PDFB /cmsPDFSet', 
        'cd /'),
    lheDefaults = cms.vstring('cd /Herwig/Cuts', 
        'create ThePEG::Cuts NoCuts', 
        'cd /Herwig/EventHandlers', 
        'create ThePEG::LesHouchesInterface LHEReader', 
        'set LHEReader:Cuts /Herwig/Cuts/NoCuts', 
        'create ThePEG::LesHouchesEventHandler LHEHandler', 
        'set LHEHandler:WeightOption VarWeight', 
        'set LHEHandler:PartonExtractor /Herwig/Partons/QCDExtractor', 
        'set LHEHandler:CascadeHandler /Herwig/Shower/ShowerHandler', 
        'set LHEHandler:HadronizationHandler /Herwig/Hadronization/ClusterHadHandler', 
        'set LHEHandler:DecayHandler /Herwig/Decays/DecayHandler', 
        'insert LHEHandler:LesHouchesReaders 0 LHEReader', 
        'cd /Herwig/Generators', 
        'set LHCGenerator:EventHandler /Herwig/EventHandlers/LHEHandler', 
        'cd /Herwig/Shower', 
        'set Evolver:HardVetoScaleSource Read', 
        'set Evolver:MECorrMode No', 
        'cd /'),
    cmsDefaults = cms.vstring('+pdfMRST2001', 
        '+cm14TeV', 
        '+ue_2_3', 
        '+basicSetup', 
        '+setParticlesStableForDetector'),
    pdfMRST2008LOss = cms.vstring('cp /Herwig/Partons/MRST /Herwig/Partons/cmsPDFSet'),
    generatorModule = cms.string('/Herwig/Generators/LHCGenerator'),
    basicSetup = cms.vstring('cd /Herwig/Generators', 
        'create ThePEG::RandomEngineGlue /Herwig/RandomGlue', 
        'set LHCGenerator:RandomNumberGenerator /Herwig/RandomGlue', 
        'set LHCGenerator:NumberOfEvents 10', 
        'set LHCGenerator:DebugLevel 1', 
        #'set LHCGenerator:PrintEvent 0', 
        'set LHCGenerator:MaxErrors 10000'

	#-----------
        'set LHCGenerator:RandomNumberGenerator:Seed 28181231241245125140',
	'set LHCGenerator:PrintEvent 10',

	'insert LHCGenerator:AnalysisHandlers 0 /Herwig/Analysis/HepMCFile',
	'set /Herwig/Analysis/HepMCFile:PrintEvent 250000',
	'set /Herwig/Analysis/HepMCFile:Format GenEvent',
	'set /Herwig/Analysis/HepMCFile:Units GeV_mm',

	'cd /Herwig/Analysis',
	'set Basics:CheckQuark 0',		     
	#-----------
			     
        'cd /Herwig/Particles', 
        'set p+:PDF /Herwig/Partons/cmsPDFSet', 
        'set pbar-:PDF /Herwig/Partons/cmsPDFSet', 
        'set K0:Width 1e300*GeV', 
        'set Kbar0:Width 1e300*GeV', 
        'cd /'),
    run = cms.string('LHC'),
    repository = cms.string('HerwigDefaults.rpo'),
    cm14TeV = cms.vstring('set /Herwig/Generators/LHCGenerator:EventHandler:LuminosityFunction:Energy 14000.0', 
        'set /Herwig/Shower/Evolver:IntrinsicPtGaussian 2.2*GeV',
	#-----------		  
	'set /Herwig/Shower/ShowerHandler:MPIHandler NULL'),
	#-----------
    dataLocation = cms.string('${HERWIGPATH}'),
    pdfCTEQ5L = cms.vstring('cd /Herwig/Partons', 
        'create ThePEG::LHAPDF CTEQ5L ThePEGLHAPDF.so', 
        'set CTEQ5L:PDFName cteq5l.LHgrid', 
        'set CTEQ5L:RemnantHandler HadronRemnants', 
        'cp CTEQ5L cmsPDFSet', 
        'cd /'),
    setParticlesStableForDetector = cms.vstring('cd /Herwig/Particles', 
        'set mu-:Stable Stable', 
        'set mu+:Stable Stable', 
        'set Sigma-:Stable Stable', 
        'set Sigmabar+:Stable Stable', 
        'set Lambda0:Stable Stable', 
        'set Lambdabar0:Stable Stable', 
        'set Sigma+:Stable Stable', 
        'set Sigmabar-:Stable Stable', 
        'set Xi-:Stable Stable', 
        'set Xibar+:Stable Stable', 
        'set Xi0:Stable Stable', 
        'set Xibar0:Stable Stable', 
        'set Omega-:Stable Stable', 
        'set Omegabar+:Stable Stable', 
        'set pi+:Stable Stable', 
        'set pi-:Stable Stable', 
        'set K+:Stable Stable', 
        'set K-:Stable Stable', 
        'set K_S0:Stable Stable', 
        'set K_L0:Stable Stable', 
        'cd /'),
    reweightPthat = cms.vstring('mkdir /Herwig/Weights', 
        'cd /Herwig/Weights', 
        'create ThePEG::ReweightMinPT reweightMinPT ReweightMinPT.so', 
        'cd /', 
        'set /Herwig/Weights/reweightMinPT:Power 4.5', 
        'set /Herwig/Weights/reweightMinPT:Scale 15*GeV', 
        'insert SimpleQCD:Reweights[0] /Herwig/Weights/reweightMinPT'),
    cm10TeV = cms.vstring('set /Herwig/Generators/LHCGenerator:EventHandler:LuminosityFunction:Energy 10000.0', 
        'set /Herwig/Shower/Evolver:IntrinsicPtGaussian 2.1*GeV'),
    cm8TeV = cms.vstring('set /Herwig/Generators/LHCGenerator:EventHandler:LuminosityFunction:Energy 8000.0', 
        'set /Herwig/Shower/Evolver:IntrinsicPtGaussian 2.0*GeV'),
    pdfCTEQ6L1 = cms.vstring('cd /Herwig/Partons', 
        'create ThePEG::LHAPDF CTEQ6L1 ThePEGLHAPDF.so', 
        'set CTEQ6L1:PDFName cteq6ll.LHpdf', 
        'set CTEQ6L1:RemnantHandler HadronRemnants', 
        'cp CTEQ6L1 cmsPDFSet', 
        'cd /'),
    eventHandlers = cms.string('/Herwig/EventHandlers'),
    configFiles = cms.vstring(),
    crossSection = cms.untracked.double(0.36),
    parameterSets = cms.vstring('cm14TeV', 
        'pdfMRST2001', 
        'Summer09QCDParameters', 
        'basicSetup', 
        'setParticlesStableForDetector'),
    filterEfficiency = cms.untracked.double(1.0),
    Summer09QCDParameters = cms.vstring(
	#-----------
	'read MSSM.model',
	'cd /Herwig/NewPhysics',

	'set HPConstructor:IncludeEW Yes',

	'insert HPConstructor:Incoming 0 /Herwig/Particles/g',
	'insert HPConstructor:Incoming 1 /Herwig/Particles/u',
	'insert HPConstructor:Incoming 2 /Herwig/Particles/ubar',
	'insert HPConstructor:Incoming 3 /Herwig/Particles/d',
	'insert HPConstructor:Incoming 4 /Herwig/Particles/dbar',
	'insert HPConstructor:Incoming 5 /Herwig/Particles/s',
	'insert HPConstructor:Incoming 6 /Herwig/Particles/sbar',
	'insert HPConstructor:Incoming 7 /Herwig/Particles/c',
	'insert HPConstructor:Incoming 8 /Herwig/Particles/cbar',
	
	'insert HPConstructor:Outgoing 0 /Herwig/Particles/~g',
	'insert HPConstructor:Outgoing 1 /Herwig/Particles/~d_R',
	'insert HPConstructor:Outgoing 2 /Herwig/Particles/~u_L',
	'insert HPConstructor:Outgoing 3 /Herwig/Particles/~d_R',
	'insert HPConstructor:Outgoing 4 /Herwig/Particles/~u_R',
	'insert HPConstructor:Outgoing 5 /Herwig/Particles/~s_L',
	'insert HPConstructor:Outgoing 6 /Herwig/Particles/~c_L',
	'insert HPConstructor:Outgoing 7 /Herwig/Particles/~s_R',
	'insert HPConstructor:Outgoing 8 /Herwig/Particles/~c_R',

	'setup MSSM/Model PointA3.slha',
	#-----------

## 	'cd /Herwig/MatrixElements/', 
##         'insert SimpleQCD:MatrixElements[0] MEQCD2to2', 
##         'cd /', 
##         'set /Herwig/Cuts/JetKtCut:MinKT 30*GeV', 
##         'set /Herwig/Cuts/QCDCuts:MHatMin 0.0*GeV', 
##         'set /Herwig/UnderlyingEvent/MPIHandler:IdenticalToUE 0'

	'cd /')
)


process.ProductionFilterSequence = cms.Sequence(process.generator)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen_genonly)
process.reconstruction = cms.Path(process.reconstructionWithFamos)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.AODSIMoutput_step = cms.EndPath(process.AODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.reconstruction,process.AODSIMoutput_step])
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq 

