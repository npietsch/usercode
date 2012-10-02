#include "SUSYAnalysis/SUSYEventProducers/interface/VertexSelectedElectronProducer.h"

#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "TMath.h"
#include "DataFormats/TrackReco/interface/Track.h"

VertexSelectedElectronProducer::VertexSelectedElectronProducer(const edm::ParameterSet& cfg):
  src_          (cfg.getParameter<edm::InputTag>("src")),
  primaryVertex_(cfg.getParameter<edm::InputTag>("primaryVertex")),
  dxyCut_       (cfg.getParameter<bool>         ("dxyCut")),
  dzCut_        (cfg.getParameter<bool>         ("dzCut")),
  dxyCutValue_  (cfg.getParameter<double>       ("dxyCutValue")),
  dzCutValue_   (cfg.getParameter<double>       ("dzCutValue"))

{
  produces<std::vector<pat::Electron> >();
}

void
VertexSelectedElectronProducer::produce(edm::Event& evt, const edm::EventSetup& setup)
{
  edm::Handle<std::vector<pat::Electron> > src; 
  evt.getByLabel(src_, src);

  edm::Handle<reco::VertexCollection> primaryVertex;
  evt.getByLabel(primaryVertex_, primaryVertex);

  bool dxy = false;
  bool dz = false;


  std::auto_ptr<std::vector<pat::Electron> > selectedElectrons(new std::vector<pat::Electron>());
  for(std::vector<pat::Electron>::const_iterator electron=src->begin(); electron!=src->end(); ++electron)
    {
      if(std::abs(electron->gsfTrack()->dxy(primaryVertex->begin()->position())) < dxyCutValue_)
	{
	  dxy = true;
	  
	}
      if(std::abs(electron->gsfTrack()->dz(primaryVertex->begin()->position())) < dzCutValue_)
	{
	  dz = true;
	}
      
      if(dxy == true && dz == true) selectedElectrons->push_back(*electron);  
    }
  evt.put(selectedElectrons);
}
