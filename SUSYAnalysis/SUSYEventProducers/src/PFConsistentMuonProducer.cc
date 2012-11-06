#include "SUSYAnalysis/SUSYEventProducers/interface/PFConsistentMuonProducer.h"

#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "TMath.h"
#include "DataFormats/TrackReco/interface/Track.h"

PFConsistentMuonProducer::PFConsistentMuonProducer(const edm::ParameterSet& cfg):
  muons_    (cfg.getParameter<edm::InputTag>("muons")),
  pfMuons_  (cfg.getParameter<edm::InputTag>("pfMuons"))

{
  produces<std::vector<pat::Muon> >();
}  

void
PFConsistentMuonProducer::produce(edm::Event& evt, const edm::EventSetup& setup)
{
  edm::Handle<std::vector<pat::Muon> > muons;
  event.getByLabel(muons_, muons);
  
  edm::Handle<std::vector<pat::Muon> > pfMuons;
  event.getByLabel(pfMuons_, pfMuons);

  std::auto_ptr<std::vector<pat::Muon> > PFConsitentMuons(new std::vector<pat::Muon>());

  for(std::vector<pat::Muon>::const_iterator muon=src->begin(); muon!=src->end(); ++muon)
    {
      double dRmin  = 10;
      double PtPF = 0;            

      for(int pdx=0; pdx<(int)pfMuons->size(); ++pdx)
	{
	  double dR=abs(deltaR(muon->eta(),muon->phi(),(*pfMuons)[pdx].eta(),(*pfMuons)[pdx].phi()));
	  if(dR < dRmin)
	    {
	      dR=dRmin;
	      PtPf=(*pfMuons)[pdx].pt();
	    }
	}
      if(PtPF > 0 && ( ((muon->pt() - PtPF) / muon->pt()) < 0.2)
	  PFConsistentMuons->push_back(*muon);
	 }
    }
}
