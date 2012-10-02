#include "SUSYAnalysis/SUSYEventProducers/interface/VertexSelectedMuonProducer.h"

#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "TMath.h"
#include "DataFormats/TrackReco/interface/Track.h"

VertexSelectedMuonProducer::VertexSelectedMuonProducer(const edm::ParameterSet& cfg):
  src_          (cfg.getParameter<edm::InputTag>("src")),
  primaryVertex_(cfg.getParameter<edm::InputTag>("primaryVertex")),
  dxyCut_       (cfg.getParameter<bool>         ("dxyCut")),
  dzCut_        (cfg.getParameter<bool>         ("dzCut")),
  dxyCutValue_  (cfg.getParameter<double>       ("dxyCutValue")),
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

  bool dxy = false;
  bool dz = false;


  std::auto_ptr<std::vector<pat::Muon> > selectedMuons(new std::vector<pat::Muon>());
  for(std::vector<pat::Muon>::const_iterator muon=src->begin(); muon!=src->end(); ++muon)
    {
      if(std::abs(muon->innerTrack()->dxy(primaryVertex->begin()->position())) < dxyCutValue_)
	{
	  dxy = true;
	  
	}
      if(std::abs(muon->innerTrack()->dz(primaryVertex->begin()->position())) < dzCutValue_)
	{
	  dz = true;
	}
      
      if(dxy == true && dz == true) selectedMuons->push_back(*muon);  
    }
  evt.put(selectedMuons);
}
