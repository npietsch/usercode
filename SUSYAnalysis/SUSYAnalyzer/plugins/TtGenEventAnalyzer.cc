#include "AnalysisDataFormats/TopObjects/interface/TtGenEvent.h"
#include "SUSYAnalysis/SUSYAnalyzer/plugins/TtGenEventAnalyzer.h"
 
TtGenEventAnalyzer::TtGenEventAnalyzer(const edm::ParameterSet& cfg):
  inputGenEvent_(cfg.getParameter<edm::InputTag>("genEvent"))
{ 
  edm::Service<TFileService> fs;
  nLep_      = fs->make<TH1F>("nLep",      "N(Lepton)",     5,   0.,   5.);
  topPt_     = fs->make<TH1F>("topPt",     "pt (top)",    100,   0., 500.);
  topEta_    = fs->make<TH1F>("topEta",    "eta(top)",     40,  -5.,   5.);
  topPhi_    = fs->make<TH1F>("topPhi",    "phi(top)",     60, -3.5,  3.5);
  topBarPt_  = fs->make<TH1F>("topBarPt",  "pt (topBar)", 100,   0., 500.);
  topBarEta_ = fs->make<TH1F>("topBarEta", "eta(topBar)",  40,  -5.,   5.);
  topBarPhi_ = fs->make<TH1F>("topBarPhi", "phi(topBar)",  60, -3.5,  3.5);
  ttbarPt_   = fs->make<TH1F>("ttbarPt",   "pt (ttbar)",  100,   0., 500.);
  ttbarEta_  = fs->make<TH1F>("ttbarEta",  "eta(ttbar)",   40,  -5.,   5.);
  ttbarPhi_  = fs->make<TH1F>("ttbarPhi",  "phi(ttbar)",   60, -3.5,  3.5);

  HT_Ymet_=fs-> make<TH2F>("mW_MET","MET vs. mW", 80, 0., 2000., 80, 0., 20.);

}

TtGenEventAnalyzer::~TtGenEventAnalyzer()
{
}

void
TtGenEventAnalyzer::analyze(const edm::Event& evt, const edm::EventSetup& setup)
{
  edm::Handle<TtGenEvent> genEvent;
  evt.getByLabel(inputGenEvent_, genEvent);

  // fill BR's
  nLep_  ->Fill(genEvent->numberOfLeptons());

  //fill top kinematic
  topPt_    ->Fill(genEvent->top   ()->pt ());
  topEta_   ->Fill(genEvent->top   ()->eta());
  topPhi_   ->Fill(genEvent->top   ()->phi());
  topBarPt_ ->Fill(genEvent->topBar()->pt ());
  topBarEta_->Fill(genEvent->topBar()->eta());
  topBarPhi_->Fill(genEvent->topBar()->phi());

  //fill ttbar kinematics
  reco::Particle::LorentzVector p4 = genEvent->top()->p4()+genEvent->topBar()->p4();
  ttbarPt_ ->Fill(p4.pt() );
  ttbarEta_->Fill(p4.eta());
  ttbarPhi_->Fill(p4.phi());

  if( genEvent->isSemiLeptonic(WDecay::kMuon) ||  genEvent->isSemiLeptonic(WDecay::kElec))
    {
      //transverse W mass
      double NuPt=genEvent->singleNeutrino()->pt();
      double LepPt=genEvent->singleLepton()->pt();

      double NuPx=genEvent->singleNeutrino()->px();
      double LepPx=genEvent->singleLepton()->px();

      double NuPy=genEvent->singleNeutrino()->py();
      double LepPy=genEvent->singleLepton()->py();

      double mW=sqrt(2*(NuPt*LepPt-NuPx*LepPx-NuPy*LepPy));

       //Ymet
      double HT=genEvent->hadronicDecayB()->pt()+genEvent->leptonicDecayB()->pt();
      
      for(int ddx=0; ddx<(int)genEvent->hadronicDecayW()->numberOfDaughters(); ++ddx)
	{
	  //std::cout << genEvent->hadronicDecayW()->daughter(ddx)->pdgId() <<std::endl;
	  HT=HT+genEvent->hadronicDecayW()->daughter(ddx)->pt();
	}
      HT_Ymet_->Fill(HT,NuPt/(sqrt(HT)));
    }
}

void TtGenEventAnalyzer::beginJob()
{  
} 

void TtGenEventAnalyzer::endJob()
{
}
