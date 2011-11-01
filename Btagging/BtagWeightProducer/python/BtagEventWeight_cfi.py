import FWCore.ParameterSet.Config as cms

btagEventWeight = cms.EDProducer("BtagEventWeight",
                                 jets          = cms.InputTag("selectedPatJetsAK5PF"), ## jet collection
                                 bTagAlgo      = cms.string("TCHEM"),               ## name of b tag algorithm
                                 sysVar        = cms.string(""),   ## bTagSFUp, bTagSFDown, misTagSFUp, misTagSFDown
                                 verbose       = cms.int32(0),     ## set to 1 if terminal text output is desired
                                 filename      = cms.string(""),   ## if filename != "", efficiencies are read from file
                                 rootDir       = cms.string(""),   ## root dir where histos are located
                                 shift         = cms.double(0.),   ## shift b-tag scale factor up or down
                                 scaleJetEffSF = cms.bool(False),  ## scale all jet tag efficiency scale factors
                                 scaleEventEffSF = cms.bool(False) ## scale all event tag efficiency scale factors
                                 )
