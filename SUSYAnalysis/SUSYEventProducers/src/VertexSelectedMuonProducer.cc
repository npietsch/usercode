#include "SUSYAnalysis/SUSYEventProducers/interface/VertexSelectedMuonProducer.h"

#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"

VertexSelectedMuonProducer::VertexSelectedMuonProducer(const edm::ParameterSet& cfg):
  src_          (cfg.getParameter<edm::InputTag>("src")),
  primaryVertex_(cfg.getParameter<edm::InputTag>("primaryVertex")),
  dxyCut_       (cfg.getParameter<bool>         ("dxyCut")),
  dzCut_        (cfg.getParameter<double>       ("dzCut")),
  dxyCutValue_  (cfg.getParameter<bool>         ("dxyCutValue")),
  dzCutValue_   (cfg.getParameter<double>       ("dzCutValue"))

{
  produces<std::vector<pat::Muon> >();
}

void
VertexSelectedMuonProducer::produce(edm::Event& evt, const edm::EventSetup& setup)
{
  edm::Handle<std::vector<pat::Muon> > src; 
  evt.getByLabel(src_, src);

  edm::Handle<reco::VertexCollection> primaryVertex;
  evt.getByLabel(primaryVertex_, primaryVertex);

  std::auto_ptr<std::vector<pat::Muon> > selectedMuons(new std::vector<pat::Muon>());
  for(std::vector<pat::Muon>::const_iterator muon=src->begin(); muon!=src->end(); ++muon)
    {
      if(std::abs(muon->vertex().z() - primaryVertex->begin()->z()) < dzCutValue_)
	{
	  if(dxyCut_ == true)
	    {
	      double dx  = muon->vertex().x() - primaryVertex->begin()->x();
	      double dy  = muon->vertex().y() - primaryVertex->begin()->y();
	      double dxy = sqrt(dx*dx+dy*dy);

	      if(dxy < dxyCutValue_) selectedMuons->push_back(*muon);
	    }
	  else selectedMuons->push_back(*muon);
	}
  }
  evt.put(selectedMuons);
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(VertexSelectedMuonProducer);
