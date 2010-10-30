import FWCore.ParameterSet.Config as cms

#
# produce SUSYGenEvent with all necessary ingredients
#
from SUSYAnalysis.SUSYEventProducers.producers.SUSYInitSubset_cfi import *
from SUSYAnalysis.SUSYEventProducers.producers.SUSYGenEvtProducer_cfi import *

makeSUSYGenEvt = cms.Sequence(SUSYInitSubset*SUSYGenEvt)
