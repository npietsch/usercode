#
#  SUSY-PAT configuration file
#
#  PAT configuration for the SUSY group - 42X series
#  More information here:
#  https://twiki.cern.ch/twiki/bin/view/CMS/SusyPatLayer1DefV10
#

# Starting with a skeleton process which gets imported with the following line
from PhysicsTools.PatAlgos.patTemplate_cfg import *

#-- Meta data to be logged in DBS ---------------------------------------------
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.1.2.6 $'),
    name = cms.untracked.string('$Source: /local/reps/CMSSW/UserCode/npietsch/SUSYAnalysis/Configuration/Run2011/Attic/SUSY_pattuple_Upgrade_cfg.py,v $'),
    annotation = cms.untracked.string('SUSY pattuple definition')
)
#-- Message Logger ------------------------------------------------------------
process.MessageLogger.categories.append('PATSummaryTables')
process.MessageLogger.cerr.PATSummaryTables = cms.untracked.PSet(
    limit = cms.untracked.int32(-1),
    reportEvery = cms.untracked.int32(1)
    )
process.MessageLogger.cerr.FwkReport.reportEvery = 1

#-- VarParsing ----------------------------------------------------------------
import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing ('standard')


#  for SusyPAT configuration
options.register('GlobalTag', "START42_V17::All", VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string, "GlobalTag to use (if empty default Pat GT is used)")
options.register('mcInfo', True, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.int, "process MonteCarlo data")
options.register('jetCorrections', 'L1FastJet', VarParsing.VarParsing.multiplicity.list, VarParsing.VarParsing.varType.string, "Level of jet corrections to use: Note the factors are read from DB via GlobalTag")
options.jetCorrections.append('L2Relative')
options.jetCorrections.append('L3Absolute')
options.register('hltName', 'HLT', VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string, "HLT menu to use for trigger matching")
options.register('mcVersion', '', VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string, "Currently not needed and supported")
options.register('jetTypes', 'AK5PF', VarParsing.VarParsing.multiplicity.list, VarParsing.VarParsing.varType.string, "Additional jet types that will be produced (AK5Calo and AK5PF, cross cleaned in PF2PAT, are included anyway)")
options.register('hltSelection', '', VarParsing.VarParsing.multiplicity.list, VarParsing.VarParsing.varType.string, "hlTriggers (OR) used to filter events")
options.register('doValidation', False, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.int, "Include the validation histograms from SusyDQM (needs extra tags)")
options.register('doExtensiveMatching', False, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.int, "Matching to simtracks (needs extra tags)")
options.register('doSusyTopProjection', False, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.int, "Apply Susy selection in PF2PAT to obtain lepton cleaned jets (needs validation)")
options.register('addKeep', '', VarParsing.VarParsing.multiplicity.list, VarParsing.VarParsing.varType.string, "Additional keep and drop statements to trim the event content")

#---parse user input
options.parseArguments()
options._tagOrder =[]

process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )


# Due to problem in production of LM samples: same event number appears multiple times
process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')


############################# START SUSYPAT specifics ####################################
from PhysicsTools.Configuration.SUSY_pattuple_cff import addDefaultSUSYPAT, getSUSY_pattuple_outputCommands
#Apply SUSYPAT
addDefaultSUSYPAT(process,options.mcInfo,options.hltName,options.jetCorrections,options.mcVersion,options.jetTypes,options.doValidation,options.doExtensiveMatching,options.doSusyTopProjection)
SUSY_pattuple_outputCommands = getSUSY_pattuple_outputCommands( process )

## Note: L1FastJet propagation is working only with reco jets and can therefore not be applied here 
process.metJESCorAK5PFTypeI.corrector = cms.string('ak5PFL2L3')

############################## END SUSYPAT specifics ####################################

#-- HLT selection ------------------------------------------------------------
import HLTrigger.HLTfilters.hltHighLevel_cfi as hlt
if options.hltSelection:
    process.hltFilter = hlt.hltHighLevel.clone(
        HLTPaths = cms.vstring(options.hltSelection),
        TriggerResultsTag = cms.InputTag("TriggerResults","",options.hltName),
        throw = False
    )
    process.susyPatDefaultSequence.replace(process.eventCountProducer, process.eventCountProducer * process.hltFilter)

#-- Output module configuration -----------------------------------------------
process.out.fileName = options.output
# Custom settings
#process.out.splitLevel = cms.untracked.int32(99)  # Turn on split level (smaller files???)
#process.out.overrideInputFileSplitLevels = cms.untracked.bool(True)
process.out.dropMetaData = cms.untracked.string('DROPPED')   # Get rid of metadata related to dropped collections
process.out.outputCommands = cms.untracked.vstring('drop *')
if options.hltSelection:
    process.out.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring("p"))
if options.addKeep:
    process.out.outputCommands.extend(options.addKeep)

############################## some Custome options for the Upgrade  ####################################

# Choose input files
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    'root://eoscms.cern.ch//eos/cms/store/mc/Summer12/PYTHIA6_Tauola_TTbar_TuneZ2star_14TeV/GEN-SIM-DIGI-RECO/UpgradeHCAL_PixelPhase1_DR428_R2-PU50-DESIGN42_V17S-v1/00002/EEE6A5C2-61D7-E111-98E9-003048678A6A.root',
    'root://eoscms.cern.ch//eos/cms/store/mc/Summer12/PYTHIA6_Tauola_TTbar_TuneZ2star_14TeV/GEN-SIM-DIGI-RECO/UpgradeHCAL_PixelPhase1_DR428_R2-PU50-DESIGN42_V17S-v1/00001/4E56B10B-F8D6-E111-8D9A-0026189438CF.root',
    'root://eoscms.cern.ch//eos/cms/store/mc/Summer12/PYTHIA6_Tauola_TTbar_TuneZ2star_14TeV/GEN-SIM-DIGI-RECO/UpgradeHCAL_PixelPhase1_DR428_R2-PU50-DESIGN42_V17S-v1/00000/BC71F154-FED6-E111-A93F-003048679162.root',
    'root://eoscms.cern.ch//eos/cms/store/mc/Summer12/PYTHIA6_Tauola_TTbar_TuneZ2star_14TeV/GEN-SIM-DIGI-RECO/UpgradeHCAL_PixelPhase1_DR428_R2-PU50-DESIGN42_V17S-v1/00002/E6BFAEB3-46D7-E111-888D-0018F3D096CE.root',
    'root://eoscms.cern.ch//eos/cms/store/mc/Summer12/PYTHIA6_Tauola_TTbar_TuneZ2star_14TeV/GEN-SIM-DIGI-RECO/UpgradeHCAL_PixelPhase1_DR428_R2-PU50-DESIGN42_V17S-v1/00000/AA14DC8F-F2D6-E111-A0FA-00261894384F.root',
    'root://eoscms.cern.ch//eos/cms/store/mc/Summer12/PYTHIA6_Tauola_TTbar_TuneZ2star_14TeV/GEN-SIM-DIGI-RECO/UpgradeHCAL_PixelPhase1_DR428_R2-PU50-DESIGN42_V17S-v1/00001/9E85F027-22D7-E111-BA18-001A928116E8.root', 
    #"/store/mc/Summer12/PYTHIA6_Tauola_TTbar_TuneZ2star_14TeV/GEN-SIM-DIGI-RECO/UpgradeHCAL_PixelPhase1_DR428-PU50-DESIGN42_V17S-v2/0002/FED1A35B-97C9-E111-A11D-002618943939.root"
    #"root://eoscms.cern.ch//eos/cms/store/mc/Summer12/DYToMuMu_M_20_TuneZ2star_14TeV_pythia6/GEN-SIM-DIGI-RECO/UpgradeHCAL_PixelPhase1_DR428-PU50-DESIGN42_V17S-v1/0002/FE6A3DDB-A3C9-E111-8DB9-003048678B86.root"
    #"root://eoscms.cern.ch//eos/cms/store/mc/Summer12/PYTHIA6_Tauola_TTbar_TuneZ2star_14TeV/GEN-SIM-DIGI-RECO/UpgradeStdGeom2_DR428-PU50-DESIGN42_V17S-v1/0000/A6A3B8DE-A9AA-E111-936F-003048D3C880.root"
    #"/store/mc/Summer11/TTJets_TuneZ2_7TeV-madgraph-tauola/AODSIM/PU_S4_START42_V11-v1/0000/FEEE3638-F297-E011-AAF8-00304867BEC0.root"
    )
                            )

#-- Calibration tag -----------------------------------------------------------
#options.GlobalTag = "START42_V17::All"
options.GlobalTag = "DESIGN42_V17S::All"
if options.GlobalTag:
    process.GlobalTag.globaltag = options.GlobalTag

# Output
process.maxEvents.input = -1

from SUSYAnalysis.SUSYEventProducers.RA4bEventContent_cff import *
process.out.outputCommands += RA4bEventContent
process.out.fileName="Upgrade.root"

process.load("Configuration.StandardSequences.Generator_cff")# import genJetMET
#process.load("RecoJets.JetProducers.ak5JetID_cfi")# load ak5JetID
#process.load("RecoJets.JetProducers.ak5CaloJets_cfi")
#process.calonew=process.ak5CaloJets.clone()
#process.ak5JetID.useRecHits = cms.bool(False)
#process.ak5JetID.src="ak5CaloJetsnew"
process.TrackerDigiGeometryESModule.applyAlignment = cms.bool(False)
process.patJetsAK5PF.jetIDMap="ak5JetID"
#process.patJetsAK5PF.jetSource = cms.InputTag("ak5CaloJets")
process.patJetsAK5PF.addJetID = cms.bool(True)
#process.patJets.jetSource = cms.InputTag("ak5CaloJets")
process.patJets.addJetID = cms.bool(True)
process.load("SLHCUpgradeSimulations.Geometry.Phase1_cmsSimIdealGeometryXML_cfi")
'''
process.ak5JetID = cms.EDProducer("JetIDProducer",
    eeRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    hbheRecHitsColl = cms.InputTag("hbhereco"),
    rpcRecHits = cms.InputTag("rpcRecHits"),
    hoRecHitsColl = cms.InputTag("horeco"),
    ebRecHitsColl = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    hfRecHitsColl = cms.InputTag("hfreco"),
    useRecHits = cms.bool(True),
    src = cms.InputTag("ak5CaloJets")
)
'''



# load the PU JetID sequence
from CMGTools.External.pujetidsequence_cff import *

process.puJetIdPF=puJetId.clone(jets = cms.InputTag("selectedPatJetsPF"))
process.puJetMvaPF=puJetMva.clone(jets = cms.InputTag("selectedPatJetsPF"),
                                  jetids = cms.InputTag("puJetIdPF"))
    
process.puJetIdAK5PF=puJetId.clone(jets = cms.InputTag("selectedPatJetsAK5PF"))
process.puJetMvaAK5PF=puJetMva.clone(jets = cms.InputTag("selectedPatJetsAK5PF"),
                                     jetids = cms.InputTag("puJetIdAK5PF"))

process.puJetIdSequence=cms.Sequence(process.puJetIdPF*process.puJetMvaPF*process.puJetIdAK5PF*process.puJetMvaAK5PF)

'''
process.puJetIdSqeuencePF=puJetIdSqeuence.clone(
    puJetId.PSet(),
    )
'''
#process.load("CMGTools.External.pujetidsequence_cff")

#process.puJetId.jets = cms.InputTag("selectedPatJetsPF")
#process.puJetMva.jets = cms.InputTag("selectedPatJetsPF")

# run the PU JetID sequence
#process.p = cms.Path(process.patSequence * process.puJetIdSqeuence)

# keep the PU JetID products
#process.out.outputCommands +=["keep *_puJetId_*_*", # input variables
#"keep *_puJetMva_*_*" # final MVAs and working point flags
#]


process.outpath = cms.EndPath(process.out)

############################## end of Custome options for the Upgrade  ####################################

#-- Execution path ------------------------------------------------------------
# Full path
#process.p = cms.Path( process.genJetMET*process.susyPatDefaultSequence * process.puJetIdSqeuence)
process.p = cms.Path( process.genJetMET*process.ak5JetID*process.susyPatDefaultSequence * process.puJetIdSequence)
process.p.remove(process.daVertices)
#-- Dump config ------------------------------------------------------------
file = open('SusyPAT_cfg.py','w')
file.write(str(process.dumpPython()))
file.close()
