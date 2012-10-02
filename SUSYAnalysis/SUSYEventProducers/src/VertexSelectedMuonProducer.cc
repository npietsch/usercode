#include "SUSYAnalysis/SUSYEventProducers/interface/VertexSelectedMuonProducer.h"

#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"

VertexSelectedMuonProducer::VertexSelectedMuonProducer(const edm::ParameterSet& cfg):
  src_          (cfg.getParameter<edm::InputTag>("src")),
  primaryVertex_(cfg.getParameter<edm::InputTag>("primaryVertex")),
  cutValue_     (cfg.getParameter<double>       ("cutValue")),
  dxy_cut_      (cfg.getParameter<bool>         ("dxy_cut")),
  dxy_          (cfg.getParameter<double>       ("dxy"))

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

//  for(reco::VertexCollection::const_iterator vtx=primaryVertex->begin(); vtx!=primaryVertex->end(); ++vtx) {
//    std::cout << "vtx->isFake:ndof:z:rho : "
//	      << vtx->isFake() << ":"
//	      << vtx->ndof() << ":"
//	      << vtx->z() << ":"
//	      << vtx->position().Rho() << std::endl;
//  }

  std::auto_ptr<std::vector<pat::Muon> > selectedMuons(new std::vector<pat::Muon>());
  for(std::vector<pat::Muon>::const_iterator muon=src->begin(); muon!=src->end(); ++muon)
    {
      if(std::abs(muon->vertex().z() - primaryVertex->begin()->z()) < cutValue_)
	{
	  if(dxy_cut_ == true)
	    {
	      double dx  = muon->vertex().x() - primaryVertex->begin()->x();
	      double dy  = muon->vertex().y() - primaryVertex->begin()->y();
	      double dxy = sqrt(dx*dx+dy*dy);

	      if(dxy < dxy_) selectedMuons->push_back(*muon);
	    }
	  else selectedMuons->push_back(*muon);
	}
  }
  evt.put(selectedMuons);
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(VertexSelectedMuonProducer);
