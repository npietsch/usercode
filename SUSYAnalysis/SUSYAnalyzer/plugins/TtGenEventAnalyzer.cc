#include "AnalysisDataFormats/TopObjects/interface/TtGenEvent.h"
#include "SUSYAnalysis/SUSYAnalyzer/plugins/TtGenEventAnalyzer.h"
 
TtGenEventAnalyzer::TtGenEventAnalyzer(const edm::ParameterSet& cfg):
  inputGenEvent_    (cfg.getParameter<edm::InputTag>("genEvent")),
  genEvtInfoHandle_ (cfg.getParameter<edm::InputTag>("genEvtInfoHandle")),
  genParticles_     (cfg.getParameter<edm::InputTag>("genParticles" ))

{ 
  edm::Service<TFileService> fs;

  // Dummy histograms
  Dummy_ =fs->make<TH1F>();
  Dummy2_=fs->make<TH2F>();

  Dummy_->SetDefaultSumw2(true);
  Dummy2_->SetDefaultSumw2(true);

  // fill for all events
  DecayChannel_ = fs->make<TH1F>("DecayChannel", "decay",        14,   0.,   14.);
  nLep_         = fs->make<TH1F>("nLep",         "N(Lepton)",     5,   0.,    5.);
  topPt_        = fs->make<TH1F>("topPt",        "pt (top)",    100,   0.,  500.);
  topEta_       = fs->make<TH1F>("topEta",       "eta(top)",     40,  -5.,    5.);
  topPhi_       = fs->make<TH1F>("topPhi",       "phi(top)",     60, -3.5,   3.5);
  topBarPt_     = fs->make<TH1F>("topBarPt",     "pt (topBar)", 100,   0.,  500.);
  topBarEta_    = fs->make<TH1F>("topBarEta",    "eta(topBar)",  40,  -5.,    5.);
  topBarPhi_    = fs->make<TH1F>("topBarPhi",    "phi(topBar)",  60, -3.5,   3.5);
  ttbarPt_      = fs->make<TH1F>("ttbarPt",      "pt (ttbar)",  100,   0.,  500.);
  ttbarEta_     = fs->make<TH1F>("ttbarEta",     "eta(ttbar)",   40,  -5.,    5.);
  ttbarPhi_     = fs->make<TH1F>("ttbarPhi",     "phi(ttbar)",   60, -3.5,   3.5);
  ttbarMass_    = fs->make<TH1F>("ttbarMass",    "m(ttbar)",    100,    0., 1000);

  // fill only in the case of semileptonic ttbar decays with muon or electron
  NuPt_  = fs->make<TH1F>("NuPt",  "neutrino pt", 50, 0., 1000.);
  LepPt_ = fs->make<TH1F>("LepPt", "lepton pt",   50, 0., 1000.);
  mT_    = fs->make<TH1F>("mT",    "mT",          40, 0,   200.);
  mlb_   = fs->make<TH1F>("mlb",   "mlb",         40, 0,   200.);

  qScale_MET_    = fs->make<TH2F>("qScale_MET",   "qScale vs. MET",    50, 0., 2000., 50, 0.,  1000.);
  qScale_HT_     = fs->make<TH2F>("qScale_HT",    "qScale vs. HT",     50, 0., 2000., 50, 0.,  2000.);
  PDFScale_MET_  = fs->make<TH2F>("PDFScale_MET", "PDFScale vs. MET",  50, 0., 2000., 50, 0.,  1000.);
  PDFScale_HT_   = fs->make<TH2F>("PDFScale_HT",  "PDFScale vs. HT",   50, 0., 2000., 50, 0.,  2000.);
  ttbarMass_MET_ = fs->make<TH2F>("ttbarMass_MET","m(ttbar)vs. MET",   50, 0., 2000., 50, 0.,  1000.);
  ttbarMass_HT_  = fs->make<TH2F>("ttbarMass_HT", "m(ttbar)vs. HT",    50, 0., 2000., 50, 0.,  2000.);

  HT_MET_      = fs->make<TH2F>("HT_MET",      "HT vs. MET",           50, 0., 2000., 50, 0.,  1000.);
  HT_LepPt_    = fs->make<TH2F>("HT_LepPt",    "HT vs. lepton pt",     50, 0., 2000., 50, 0.,  1000.);
  HT_YMET_     = fs->make<TH2F>("HT_YMET",     "HT vs. YMET",          50, 0., 2000., 50, 0.,    25.);
  HT_LepPtSig_ = fs->make<TH2F>("HT_LepPtSig", "HT vs. lepton pt sig", 50, 0., 2000., 50, 0.,    25.);
  HT_mT_       = fs->make<TH2F>("HT_mT",       "HT vs. mT",            50, 0., 2000., 80, 0.,   400.);

  HT_MET_acceptance_      = fs->make<TH2F>("HT_MET_acceptance",     "HT vs. MET",          50, 0., 2000., 50, 0.,  1000.);
  HT_LepPt_acceptance_    = fs->make<TH2F>("HT_LepPt_acceptance",   "HT vs. lepton pt",    50, 0., 2000., 50, 0.,  1000.);
  HT_YMET_acceptance_     = fs->make<TH2F>("HT_YMET_acceptance",    "HT vs. YMET",          50, 0., 2000., 50, 0.,   25.);
  HT_LepPtSig_acceptance_ = fs->make<TH2F>("HT_LepPtSig_acceptance","HT vs. lepton pt sig", 50, 0., 2000., 50, 0.,   25.);
  HT_mT_acceptance_       = fs->make<TH2F>("HT_mT_acceptance", "     HT vs. mT",            50, 0., 2000., 40, 0.,  200.);

}

TtGenEventAnalyzer::~TtGenEventAnalyzer()
{
}

void
TtGenEventAnalyzer::analyze(const edm::Event& evt, const edm::EventSetup& setup)
{
  edm::Handle<TtGenEvent> genEvent;
  evt.getByLabel(inputGenEvent_, genEvent);

  edm::Handle<GenEventInfoProduct> genEvtInfoHandle;
  evt.getByLabel(genEvtInfoHandle_, genEvtInfoHandle);
  
  edm::Handle<reco::GenParticleCollection> genParticles;
  evt.getByLabel(genParticles_, genParticles);

  if(!genEvent->isTtBar()) return;

  // Fill decay channels
  if(genEvent->isFullHadronic())
    DecayChannel_ ->Fill(0);
  if(genEvent->isSemiLeptonic(WDecay::kMuon) ||  genEvent->isSemiLeptonic(WDecay::kElec))
    DecayChannel_ ->Fill(1);
  else if(genEvent->isSemiLeptonic(WDecay::kTau))
    {
      DecayChannel_ ->Fill(2);
      bool LeptonicDecay = false;
      reco::GenParticleCollection::const_iterator Tau;
      for(reco::GenParticleCollection::const_iterator t=genParticles->begin(); t!=genParticles->end(); ++t)
	{
	  if(abs(t->pdgId())==15)
	    {
	      if(t->pdgId()==15 && genEvent->lepton())
		{	
		  if(t->pt()==genEvent->lepton()->pt()) Tau=t;
		}
	      
	      if(t->pdgId()==-15 && genEvent->leptonBar())
		{	
		  if(t->pt()==genEvent->leptonBar()->pt()) Tau=t;
		}
	    }
	}
      for(reco::GenParticle::const_iterator tdx=Tau->begin(); tdx!=Tau->end(); ++tdx)
	{
	  for(reco::GenParticle::const_iterator daughter=tdx->begin(); daughter!=tdx->end(); ++daughter)
	    {
	      //std::cout << "daughter->pdgId(): " << daughter->pdgId() << std::endl;
	      if(abs(daughter->pdgId())==11 || abs(daughter->pdgId())==13) LeptonicDecay = true;
	      if(abs(daughter->pdgId())==24)
		{
		  for(reco::GenParticle::const_iterator Wdaughter=daughter->begin(); Wdaughter!=daughter->end(); ++Wdaughter)
		    {
		      if(abs(Wdaughter->pdgId())==11 || abs(Wdaughter->pdgId())==13) LeptonicDecay = true;
		    }
		}
	    }
	}
      if(LeptonicDecay == true)
	DecayChannel_ ->Fill(3);
      else
	DecayChannel_ ->Fill(4);
    }
  else if(genEvent->isFullLeptonic(WDecay::kMuon,WDecay::kMuon) || genEvent->isFullLeptonic(WDecay::kMuon,WDecay::kElec) ||
	  genEvent->isFullLeptonic(WDecay::kElec,WDecay::kElec) )
    DecayChannel_ ->Fill(5);
  else if(genEvent->isFullLeptonic(WDecay::kTau,WDecay::kMuon) || genEvent->isFullLeptonic(WDecay::kTau,WDecay::kElec))
    {
      DecayChannel_ ->Fill(6);
      bool LeptonicDecay = false;
      reco::GenParticleCollection::const_iterator Tau;
      for(reco::GenParticleCollection::const_iterator t=genParticles->begin(); t!=genParticles->end(); ++t)
	{
	  if(abs(t->pdgId())==15)
	    {
	      if(t->pdgId()==15 && genEvent->lepton())
		{	
		  if(t->pt()==genEvent->lepton()->pt()) Tau=t;
		}
	      
	      if(t->pdgId()==-15 && genEvent->leptonBar())
		{	
		  if(t->pt()==genEvent->leptonBar()->pt()) Tau=t;
		}
	    }
	}
      for(reco::GenParticle::const_iterator tdx=Tau->begin(); tdx!=Tau->end(); ++tdx)
	{
	  for(reco::GenParticle::const_iterator daughter=tdx->begin(); daughter!=tdx->end(); ++daughter)
	    {
	      //std::cout << "daughter->pdgId(): " << daughter->pdgId() << std::endl;
	      if(abs(daughter->pdgId())==11 || abs(daughter->pdgId())==13) LeptonicDecay = true;
	      if(abs(daughter->pdgId())==24)
		{
		  for(reco::GenParticle::const_iterator Wdaughter=daughter->begin(); Wdaughter!=daughter->end(); ++Wdaughter)
		    {
		      if(abs(daughter->pdgId())==11 || abs(daughter->pdgId())==13) LeptonicDecay = true; 
		    }
		}
	    }
	}
      if(LeptonicDecay == true)
	DecayChannel_ ->Fill(7);
      else
	DecayChannel_ ->Fill(8);
    }
  else if(genEvent->isFullLeptonic(WDecay::kTau,WDecay::kTau))
    {
      DecayChannel_ ->Fill(9);
      bool LeptonicDecay    = false;
      bool LeptonicDecayBar = false;
      reco::GenParticleCollection::const_iterator Tau;
      reco::GenParticleCollection::const_iterator TauBar;
      for(reco::GenParticleCollection::const_iterator t=genParticles->begin(); t!=genParticles->end(); ++t)
	{
	  if(abs(t->pdgId())==15)
	    {
	      if(t->pdgId()==15 && genEvent->lepton())
		{	
		  if(t->pt()==genEvent->lepton()->pt()) Tau=t;
		}
	      
	      if(t->pdgId()==-15 && genEvent->leptonBar())
		{	
		  if(t->pt()==genEvent->leptonBar()->pt()) TauBar=t;
		}
	    }
	}
      for(reco::GenParticle::const_iterator tdx=Tau->begin(); tdx!=Tau->end(); ++tdx)
	{
	  for(reco::GenParticle::const_iterator daughter=tdx->begin(); daughter!=tdx->end(); ++daughter)
	    {
	      //std::cout << "daughter->pdgId(): " << daughter->pdgId() << std::endl;
	      if(abs(daughter->pdgId())==11 || abs(daughter->pdgId())==13) LeptonicDecay = true;
	      if(abs(daughter->pdgId())==24)
		{
		  for(reco::GenParticle::const_iterator Wdaughter=daughter->begin(); Wdaughter!=daughter->end(); ++Wdaughter)
		    {
		      if(abs(daughter->pdgId())==11 || abs(daughter->pdgId())==13) LeptonicDecay = true; 
		    }
		}
	    }
	}
      for(reco::GenParticle::const_iterator tdx=TauBar->begin(); tdx!=TauBar->end(); ++tdx)
	{
	  for(reco::GenParticle::const_iterator daughter=tdx->begin(); daughter!=tdx->end(); ++daughter)
	    {
	      //std::cout << "daughter->pdgId(): " << daughter->pdgId() << std::endl;
	      if(abs(daughter->pdgId())==11 || abs(daughter->pdgId())==13) LeptonicDecayBar = true;
	      if(abs(daughter->pdgId())==24)
		{
		  for(reco::GenParticle::const_iterator Wdaughter=daughter->begin(); Wdaughter!=daughter->end(); ++Wdaughter)
		    {
		      if(abs(daughter->pdgId())==11 || abs(daughter->pdgId())==13) LeptonicDecayBar = true; 
		    }
		}
	    }
	}
      if(LeptonicDecay == true && LeptonicDecayBar == true)
	DecayChannel_ ->Fill(10);
      else if ( (LeptonicDecay == true && LeptonicDecayBar == false) || (LeptonicDecay == false && LeptonicDecayBar == true) )
	DecayChannel_ ->Fill(11);
      else
	DecayChannel_ ->Fill(12);	  
    }
  else
    DecayChannel_ ->Fill(13);

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
  double mttbar=sqrt(p4.Dot(p4));

  ttbarPt_  ->Fill(p4.pt());
  ttbarEta_ ->Fill(p4.eta());
  ttbarPhi_ ->Fill(p4.phi());
  ttbarMass_->Fill(mttbar);

  // fill histograms only in th case of semi leptonic ttbar decays with muon or electron
  if(genEvent->isSemiLeptonic(WDecay::kMuon) ||  genEvent->isSemiLeptonic(WDecay::kElec))
    {
      double NuPt = genEvent->singleNeutrino()->pt();
      double NuPx = genEvent->singleNeutrino()->px();
      double NuPy = genEvent->singleNeutrino()->py();

      double LepPt = genEvent->singleLepton()->pt();
      double LepPx = genEvent->singleLepton()->px();
      double LepPy = genEvent->singleLepton()->py();
      
      double LepBQuarkPt = genEvent->leptonicDecayB()->pt();
      double LepBQuarkPx = genEvent->leptonicDecayB()->px();
      double LepBQuarkPy = genEvent->leptonicDecayB()->py();

      double mT  = sqrt(2*(NuPt*LepPt-NuPx*LepPx-NuPy*LepPy));
      double mlb = sqrt(2*(LepPt*LepBQuarkPt-LepPx*LepBQuarkPx-LepPy*LepBQuarkPy));

      NuPt_ ->Fill(NuPt);
      LepPt_->Fill(LepPt);
      mT_->Fill(mT);
      mlb_->Fill(mlb);

      // correlations histograms
      double HT=genEvent->hadronicDecayB()->pt()+genEvent->leptonicDecayB()->pt();
      
      for(int ddx=0; ddx<(int)genEvent->hadronicDecayW()->numberOfDaughters(); ++ddx)
	{  
	  HT=HT+genEvent->hadronicDecayW()->daughter(ddx)->pt();
	}

      qScale_MET_->Fill(genEvtInfoHandle->qScale(), NuPt);
      qScale_HT_ ->Fill(genEvtInfoHandle->qScale(),   HT);

      PDFScale_MET_->Fill(genEvtInfoHandle->pdf()->scalePDF, NuPt);
      PDFScale_HT_ ->Fill(genEvtInfoHandle->pdf()->scalePDF,   HT);

      ttbarMass_MET_->Fill(mttbar, NuPt);
      ttbarMass_HT_ ->Fill(mttbar, HT  );

      HT_MET_   ->Fill(HT, NuPt );
      HT_LepPt_ ->Fill(HT, LepPt);

      HT_YMET_ ->Fill(HT, NuPt/(sqrt(HT)));
      HT_LepPtSig_->Fill(HT, LepPt/(sqrt(HT)));
      HT_mT_   ->Fill(HT, mT);

      // correlations histograms for finit detector acceptance
      if(abs(genEvent->hadronicDecayB()->eta())<2.4 && genEvent->hadronicDecayB()->pt()>20 &&
	 abs(genEvent->leptonicDecayB()->eta())<2.4 && genEvent->leptonicDecayB()->pt()>20 &&
	 abs(genEvent->singleLepton()->eta())<2.5 && genEvent->singleLepton()->pt()>10)
	{
	  double HT_acceptance=genEvent->hadronicDecayB()->pt()+genEvent->leptonicDecayB()->pt();
	  
	  for(int ddx=0; ddx<(int)genEvent->hadronicDecayW()->numberOfDaughters(); ++ddx)
	    {
	      if(abs(genEvent->hadronicDecayW()->daughter(ddx)->eta())>2.4 ||
		 genEvent->hadronicDecayW()->daughter(ddx)->pt()<10 ) return;
	      HT_acceptance=HT_acceptance+genEvent->hadronicDecayW()->daughter(ddx)->pt();
	    }
	  HT_MET_acceptance_   ->Fill(HT, NuPt );
	  HT_LepPt_acceptance_ ->Fill(HT, LepPt);

	  HT_YMET_acceptance_     ->Fill(HT_acceptance, NuPt/(sqrt(HT_acceptance)) );
	  HT_LepPtSig_acceptance_ ->Fill(HT_acceptance, LepPt/(sqrt(HT_acceptance)));
	  HT_mT_acceptance_       ->Fill(HT_acceptance, mT                         );
	}     
    }
}

void TtGenEventAnalyzer::beginJob()
{  
} 

void TtGenEventAnalyzer::endJob()
{
}
