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

  edm::Service<TFileService> fs;

  PFConsistency_  = fs->make<TH1F>("PFConsistency", "PFConsistency", 40, 0., 2.);
}  

void
PFConsistentMuonProducer::produce(edm::Event& evt, const edm::EventSetup& setup)
{
  edm::Handle<std::vector<pat::Muon> > muons;
  evt.getByLabel(muons_, muons);
  
  edm::Handle<std::vector<pat::Muon> > pfMuons;
  evt.getByLabel(pfMuons_, pfMuons);

  std::auto_ptr<std::vector<pat::Muon> > PFConsistentMuons(new std::vector<pat::Muon>());

  for(std::vector<pat::Muon>::const_iterator muon=muons->begin(); muon!=muons->end(); ++muon)
    {
      double dRmin  = 10;
      double PtPF = 0;            
      
      for(int pdx=0; pdx<(int)pfMuons->size(); ++pdx)
	{
	  double dR=abs(deltaR(muon->eta(),muon->phi(),(*pfMuons)[pdx].eta(),(*pfMuons)[pdx].phi()));
	  if(dR < dRmin)
	    {
	      dR=dRmin;
	      PtPF=(*pfMuons)[pdx].pt();
	    }
	  PFConsistency_ ->Fill((muon->pt() - PtPF) / muon->pt());
	}
      if(PtPF > 0 && ( ((muon->pt() - PtPF) / muon->pt()) < 0.2)) PFConsistentMuons->push_back(*muon);
    }
}
