import FWCore.ParameterSet.Config as cms

from Configuration.Generator.PythiaUEZ2Settings_cfi import *


generator = cms.EDFilter('Pythia6GeneratorFilter',
	comEnergy = cms.double(14000.0),
	crossSection = cms.untracked.double(10.62e+10),
	filterEfficiency = cms.untracked.double(1),
	maxEventsToPrint = cms.untracked.int32(0),
	pythiaHepMCVerbosity = cms.untracked.bool(False),
	pythiaPylistVerbosity = cms.untracked.int32(0),

	PythiaParameters = cms.PSet(
		pythiaUESettingsBlock,
		processParameters = cms.vstring(
			'MSEL = 1        ! QCD hight pT processes',
			'CKIN(3) = 15    ! minimum pt hat for hard interactions',
			'CKIN(4) = 3000  ! maximum pt hat for hard interactions',
			'MSTP(142) = 2   ! Turns on the PYWEVT Pt reweighting routine',
		),
		CSAParameters = cms.vstring(
			'CSAMODE = 7     ! towards a flat QCD spectrum',
			'PTPOWER = 4.5   ! reweighting of the pt spectrum',
		),
		parameterSets = cms.vstring(
			'pythiaUESettings',
			'processParameters',
			'CSAParameters',
		)
	)
)

configurationMetadata = cms.untracked.PSet(
	version = cms.untracked.string('\$Revision: 1.2 $'),
	name = cms.untracked.string('\$Source: /local/reps/CMSSW/UserCode/npietsch/SUSYAnalysis/Configuration/14TeV/QCD_Pt15to3000Flat_Pythia_14TeV_cff.py,v $'),
	annotation = cms.untracked.string('14TeV sample with PYTHIA6: QCD dijet production, pThat = 15 .. 3000 GeV, weighted, TuneZ2')
)
