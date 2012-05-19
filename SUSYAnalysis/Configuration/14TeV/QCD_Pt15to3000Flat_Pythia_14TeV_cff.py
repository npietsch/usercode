import FWCore.ParameterSet.Config as cms

from Configuration.Generator.PythiaUEZ2Settings_cfi import *
generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(0),
    comEnergy = cms.double(14000.0),
    filterEfficiency = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(0),
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
        processParameters = cms.vstring(
            'MSEL=1                ! QCD hight pT processes', 
            'CKIN(3)=15.           ! minimum pt hat for hard interactions', 
            'CKIN(4)=3000.         ! maximum pt hat for hard interactions',
            'MSTP(142)=2           ! Turns on the PYWEVT Pt reweighting routine'
            
        ),
        CSAParameters = cms.vstring(
            'CSAMODE = 7     ! towards a "flat" QCD spectrum',
            'PTPOWER = 4.5   ! reweighting of the pt spectrum'
        ),
        parameterSets = cms.vstring(
            'pythiaUESettings', 
            'processParameters', 
            'CSAParameters'
        )
    )
)

## import FWCore.ParameterSet.Config as cms

## from Configuration.Generator.PythiaUED6TSettings_cfi import *


## generator = cms.EDFilter('Pythia6GeneratorFilter',
## 	comEnergy = cms.double(14000.0),
## 	crossSection = cms.untracked.double(1),
## 	filterEfficiency = cms.untracked.double(1),
## 	maxEventsToPrint = cms.untracked.int32(0),
## 	pythiaHepMCVerbosity = cms.untracked.bool(False),
## 	pythiaPylistVerbosity = cms.untracked.int32(0),

## 	PythiaParameters = cms.PSet(
## 		pythiaUESettingsBlock,
## 		processParameters = cms.vstring(
## 			'MSEL = 1        ! QCD hight pT processes',
## 			'CKIN(3) = 200   ! minimum pt hat for hard interactions',
## 			'CKIN(4) = 4000  ! maximum pt hat for hard interactions',
## 			'MSTP(142) = 2   ! Turns on the PYWEVT Pt reweighting routine',
## 		),
## 		CSAParameters = cms.vstring(
## 			'CSAMODE = 7     ! towards a flat QCD spectrum',
## 			'PTPOWER = 4.5   ! reweighting of the pt spectrum',
## 		),
## 		parameterSets = cms.vstring(
## 			'pythiaUESettings',
## 			'processParameters',
## 			'CSAParameters',
## 		)
## 	)
## )

## configurationMetadata = cms.untracked.PSet(
## 	version = cms.untracked.string('\$Revision: 1.2 $'),
## 	name = cms.untracked.string('\$Source: /afs/cern.ch/project/cvs/reps/CMSSW/CMSSW/Configuration/GenProduction/python/EightTeV/QCD_Pt_15to3000_TuneD6T_Flat_8TeV_pythia6_cff.py,v $'),
## 	annotation = cms.untracked.string('Summer2012-Z2star sample with PYTHIA6: QCD dijet production, pThat = 15 .. 3000 GeV, weighted, TuneD6T')
## )



## import FWCore.ParameterSet.Config as cms

## from Configuration.Generator.PythiaUEZ2Settings_cfi import *


## generator = cms.EDFilter('Pythia6GeneratorFilter',
## 	comEnergy = cms.double(14000.0),
## 	crossSection = cms.untracked.double(33.80),
## 	filterEfficiency = cms.untracked.double(1),
## 	maxEventsToPrint = cms.untracked.int32(0),
## 	pythiaHepMCVerbosity = cms.untracked.bool(False),
## 	pythiaPylistVerbosity = cms.untracked.int32(0),

## 	PythiaParameters = cms.PSet(
## 		pythiaUESettingsBlock,
## 		processParameters = cms.vstring(
## 			'MSEL = 1        ! QCD hight pT processes',
## 			'CKIN(3) = 180   ! minimum pt hat for hard interactions',
## 			'CKIN(4) = 200   ! maximum pt hat for hard interactions',
## 		),
## 		parameterSets = cms.vstring(
## 			'pythiaUESettings',
## 			'processParameters',
## 		)
## 	)
## )

## configurationMetadata = cms.untracked.PSet(
## 	version = cms.untracked.string('\$Revision: 1.1 $'),
## 	name = cms.untracked.string('\$Source: /afs/cern.ch/project/cvs/reps/CMSSW/CMSSW/Configuration/GenProduction/python/FourteenTeV/QCD_Pt_800to1000_TuneZ2star_14TeV_pythia6_cff.py,v $'),
## 	annotation = cms.untracked.string('Summer2012-Z2star sample with PYTHIA6: QCD dijet production, pThat = 800 .. 1000 GeV, TuneZ2star')
## )
