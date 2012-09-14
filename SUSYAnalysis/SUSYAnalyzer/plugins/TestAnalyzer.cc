#include "FWCore/Framework/interface/MakerMacros.h"
#include "StopAnalysis/Analyzer/plugins/TestAnalyzer.h"

using namespace std;
 
TestAnalyzer::TestAnalyzer(const edm::ParameterSet& cfg):
  muons_        (cfg.getParameter<edm::InputTag>("muons")),
  electrons_    (cfg.getParameter<edm::InputTag>("electrons")),
  jets_         (cfg.getParameter<edm::InputTag>("jets"))

  
{ 
  edm::Service<TFileService> fs;

  JetsEt_ = fs->make<TH1F>("JetsEt" ,"JetsEt",  90, 0., 900.);
  JetsEta_= fs->make<TH1F>("JetsEta","JetsEta",    60, -3, 3);
  nJets_  = fs->make<TH1F>("nJets"  ,"nJets",   16, -0.5, 15);
}

TestAnalyzer::~TestAnalyzer()
{
}

void
TestAnalyzer::analyze(const edm::Event& evt, const edm::EventSetup& setup){

  //-------------------------------------------------
  // Handles
  //-------------------------------------------------
  
  edm::Handle<std::vector<pat::Jet> > jets;
  evt.getByLabel(jets_, jets);

  edm::Handle<std::vector<pat::Muon> > muons;
  evt.getByLabel(muons_, muons);

  edm::Handle<std::vector<pat::Electron> > electrons;
  evt.getByLabel(electrons_, electrons);

  //-------------------------------------------------
  // event weight
  //-------------------------------------------------

  double weight=1;

  //-------------------------------------------------
  // Basic kinematics
  //-------------------------------------------------

  // Jets
  for(int idx=0; idx<(int)jets->size(); ++idx)
    {
      JetsEt_->Fill((*jets)[idx].et(),weight);
      JetsEta_->Fill((*jets)[idx].eta());
    }
	
  nJets_->Fill(jets->size(),weight);

}

void TestAnalyzer::beginJob()
{  
} 

void TestAnalyzer::endJob()
{
}

DEFINE_FWK_MODULE(TestAnalyzer);
