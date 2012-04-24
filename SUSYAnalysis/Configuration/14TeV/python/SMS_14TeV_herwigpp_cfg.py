import FWCore.ParameterSet.Config as cms

from Configuration.Generator.SMSHerwigppDefaults_cfi import *

source = cms.Source("EmptySource")
generator = cms.EDFilter("ThePEGGeneratorFilter",
	herwigDefaultsBlock,

	configFiles = cms.vstring(),
	parameterSets = cms.vstring(
		'cm14TeV',
		'pdfMRST2001',
		'productionParameters',
		'basicSetup',
		'setParticlesStableForDetector',
	),

	productionParameters = cms.vstring(
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
	'cd /'
	),
                         
	crossSection = cms.untracked.double(0.36),
	filterEfficiency = cms.untracked.double(1.0),
)

ProductionFilterSequence = cms.Sequence(generator)
