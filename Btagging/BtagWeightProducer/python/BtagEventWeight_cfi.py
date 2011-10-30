import FWCore.ParameterSet.Config as cms

btagEventWeight = cms.EDProducer("BtagEventWeight",
                                 jets  = cms.InputTag("selectedPatJetsAK5PF"), ## jet collection
                                 bTagAlgo = cms.string("TCHEM"),               ## name of b tag algorithm
                                 sysVar   = cms.string(""),      ## bTagSFUp, bTagSFDown, misTagSFUp, misTagSFDown
                                 verbose  = cms.int32(0),        ## set to 1 if terminal text output is desired
                                 filename = cms.string(""),      ## if filename != "", efficiencies are read from file
                                 rootDir = cms.string(""),       ## root dir where histos are located
                                 applySF = cms.bool(False)
                                 )
