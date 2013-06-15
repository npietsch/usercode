#include "TopAnalysis/TopAnalyzer/interface/PUEventWeight.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "AnalysisDataFormats/TopObjects/interface/TtGenEvent.h"
#include "SUSYAnalysis/SUSYAnalyzer/plugins/HerwigGenEventAnalyzer.h"
#include "AnalysisDataFormats/TopObjects/interface/TtSemiLeptonicEvent.h"
#include  <stdio.h>
#include "DataFormats/METReco/interface/CaloMETCollection.h"
#include "DataFormats/METReco/interface/CaloMET.h"
#include "DataFormats/METReco/interface/GenMET.h"
#include "DataFormats/METReco/interface/GenMETCollection.h"
#include "DataFormats/Common/interface/View.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"
#include "PhysicsTools/Utilities/interface/LumiReWeighting.h"
#include "SUSYAnalysis/SUSYObjects/interface/SUSYGenEvent.h"
#include "SUSYAnalysis/SUSYObjects/interface/HerwigGenEvent.h"
#include <Math/RotationZ.h>
#include "TVector3.h"
#include "TRandom.h"

using namespace std;
 
HerwigGenEventAnalyzer::HerwigGenEventAnalyzer(const edm::ParameterSet& cfg):
  jets_           (cfg.getParameter<edm::InputTag>("jets")),
  looseJets_      (cfg.getParameter<edm::InputTag>("looseJets")),
  bjets_          (cfg.getParameter<edm::InputTag>("bjets")),
  muons_          (cfg.getParameter<edm::InputTag>("muons")),
  electrons_      (cfg.getParameter<edm::InputTag>("electrons")),
  vetoMuons_      (cfg.getParameter<edm::InputTag>("vetoMuons")),
  vetoElectrons_  (cfg.getParameter<edm::InputTag>("vetoElectrons")),
  met_            (cfg.getParameter<edm::InputTag>("met")),
  inputGenEvent_  (cfg.getParameter<edm::InputTag>("susyGenEvent")),
  PVSrc_          (cfg.getParameter<edm::InputTag>("PVSrc")),
  PUInfo_         (cfg.getParameter<edm::InputTag>("PUInfo")),
  RA2Weight_      (cfg.getParameter<edm::InputTag>("RA2Weight") ),
  genParticles_   (cfg.getParameter<edm::InputTag>("genParticles" ) ),
  HerwigGenEvent_ (cfg.getParameter<edm::InputTag>("HerwigGenEvent" ) )


{ 
  edm::Service<TFileService> fs;

  //-------------------------------------------------
  // Dummy histograms
  //-------------------------------------------------

  Dummy_ =fs->make<TH1F>();
  Dummy2_=fs->make<TH2F>();

  Dummy_->SetDefaultSumw2(true);
  Dummy2_->SetDefaultSumw2(true);

  //-------------------------------------------------
  // Event weighting and Pile-up
  //-------------------------------------------------

  nPV_     = fs->make<TH1F>("nPV",     "nPV",      50,   0,  50);
  nPU_     = fs->make<TH1F>("nPU",     "nPU",      50, 0.5,  50.5);

  weights_ = fs->make<TH1F>("weights", "weights", 100,   1,  100);

  //-------------------------------------------------
  // GenEvent plots
  //-------------------------------------------------

  qqbarBino_ = fs->make<TH1F>("qqbarBino",    "m_{qqbar}",          40, 0.,  2000.);
  qqbarWino_ = fs->make<TH1F>("qqbarWino",    "m_{qqbar}",          40, 0.,  2000.);

  //-------------------------------------------------
  // Histograms for mjj variables
  //-------------------------------------------------

  minj3_          = fs->make<TH1F>("minj3",         "minj3",          40, 0.,  2000.);
  min123_         = fs->make<TH1F>("min123",        "min123",         40, 0.,  2000.);
  min234_         = fs->make<TH1F>("min234",        "min234",         40, 0.,  2000.);

  //-------------------------------------------------
  // Basic kinematics
  //-------------------------------------------------

  for(int idx=0; idx<8; ++idx)
    {
      char histname[20];
      sprintf(histname,"Jet%i_Pt",idx);
      Jet_Pt_.push_back(fs->make<TH1F>(histname,histname,    80, 0., 2000.));

      char histname2[20];
      sprintf(histname2,"Jet%i_Eta",idx);
      Jet_Eta_.push_back(fs->make<TH1F>(histname2,histname2, 60, -3, 3));

      char histname3[20];
      sprintf(histname3,"DeltaPhi_MHT_Jet%i",idx);
      DeltaPhi_MHT_Jet_.push_back(fs->make<TH1F>(histname3,histname3, 66, -3.3, 3.3));

      char histname4[20];
      sprintf(histname4,"Delta_Pt_%i",idx);
      Delta_Pt_.push_back(fs->make<TH1F>(histname4,histname4, 400, -200, 200 ));

      char histname5[20];
      sprintf(histname5,"Delta_Pt_MHT_%i",idx);
      Delta_Pt_MHT_.push_back(fs->make<TH2F>(histname5,histname5, 400, -200, 200, 50, 0, 500));

      char histname6[20];
      sprintf(histname6,"RecoJetPt_MHT_%i",idx);
      RecoJetPt_MHT_.push_back(fs->make<TH2F>(histname6,histname6, 200, 0, 2000, 90, 0, 900));

      char histname7[20];
      sprintf(histname7,"GenJetPt_MHT_%i",idx);
      GenJetPt_MHT_.push_back(fs->make<TH2F>(histname7,histname6, 200, 0, 2000, 90, 0, 900));

      char histname8[20];
      sprintf(histname8,"DeltaPhi_MET_Jet%i",idx);
      DeltaPhi_MET_Jet_.push_back(fs->make<TH1F>(histname8,histname8, 66, -3.3, 3.3));
    }

  Jets_Pt_         = fs->make<TH1F>("Jets_Pt",         "Jets_Pt",          80,   0.,  2000.);
  Jets_Eta_        = fs->make<TH1F>("Jets_Eta",        "Jets_Eta",         60,  -3.,    3. );
  Jets_Phi_        = fs->make<TH1F>("Jets_Phi",        "Jets_Phi",         68,  -3.4,   3.4);
  Jets_Theta_      = fs->make<TH1F>("Jets_Theta",      "Jets_Theta",       34,   0.,    3.4);
  GluonJets_Pt_    = fs->make<TH1F>("GluonJets_Pt",    "GluonJets_Pt",     90,   0.,  900. );

  MET_      = fs->make<TH1F>("MET",      "MET",      50,   0.,  2000.);
  MHT_      = fs->make<TH1F>("MHT",      "MHT",      50,   0.,  2000.);
  HT_       = fs->make<TH1F>("HT",       "HT",      100,   0.,  5000.);
  mT_       = fs->make<TH1F>("mT",       "mT",       60,   0.,   600.);
  YMET_     = fs->make<TH1F>("YMET",     "YMET",     50,   0.,    50.);
  METSig_   = fs->make<TH1F>("METSig",   "METSig",  100,   0.,    50.);
  nJets_    = fs->make<TH1F>("nJets",    "nJets",    16 , -0.5,  15.5);
  DeltaPtSum_     = fs->make<TH1F>("DeltaPtSum", "DeltaPtSum", 50,   0.,  500.);

  nJets70_   = fs->make<TH1F>("nJets70",  "nJets70",    16, -0.5,  15.5);
  nJets80_   = fs->make<TH1F>("nJets80",  "nJets80",    16, -0.5,  15.5);
  nJets100_  = fs->make<TH1F>("nJets100", "nJets100",   16, -0.5,  15.5);
  nJets120_  = fs->make<TH1F>("nJets120", "nJets120",   16, -0.5,  15.5);
  nJets150_  = fs->make<TH1F>("nJets150", "nJets150",   16, -0.5,  15.5);
  nJets200_  = fs->make<TH1F>("nJets200", "nJets200",   16, -0.5,  15.5);

  TCHE_  = fs->make<TH1F>("TCHE",  "TCHE",   80, -20, 20);
  TCHP_  = fs->make<TH1F>("TCHP",  "TCHP",   80, -20, 20);
  SSVHE_ = fs->make<TH1F>("SSVHE", "SSVHE", 120,  -2, 10);
  SSVHP_ = fs->make<TH1F>("SSVHP", "SSVHP", 120,  -2, 10);

  nBjets_noWgt_    = fs->make<TH1F>("nBjets_noWgt",   "nBjets_noWgt",   4, 0, 4);
  nBjets_noWgt_2_  = fs->make<TH1F>("nBjets_noWgt_2", "nBjets_noWgt_2", 8, 0, 8);
  nBjets_          = fs->make<TH1F>("nBjets_",        "nBjets_",        4, 0, 4);
  nBjets_2_        = fs->make<TH1F>("nBjets_2",       "nBjets_2",       8, 0, 8);

  DeltaPtSum_MHT_ = fs->make<TH2F>("DeltaPtSum_MHT", "DeltaPtSum_MHT",  50, 0.,  500., 50, 0,  500);
  HT_MHT_         = fs->make<TH2F>("HT_MHT",         "HT_MHT",         100, 0., 5000., 50, 0, 2000);

  for(int idx=0; idx<2; ++idx)
    {
      char histname[20];
      sprintf(histname,"Muon%i_Pt",idx);
      Muon_Pt_.push_back(fs->make<TH1F>(histname,histname, 60, 0., 600.));

      char histname2[20];
      sprintf(histname2,"Muon%i_Eta",idx);
      Muon_Eta_.push_back(fs->make<TH1F>(histname2,histname2, 60, -3, 3));
    }
  for(int idx=0; idx<2; ++idx)
    {
      char histname[20];
      sprintf(histname,"Electron%i_Pt",idx);
      Electron_Pt_.push_back(fs->make<TH1F>(histname,histname, 60, 0., 600.));

      char histname2[20];
      sprintf(histname2,"Electron%i_Eta",idx);
      Electron_Eta_.push_back(fs->make<TH1F>(histname2,histname2, 60, -3, 3));
    }

  nMuons_      = fs->make<TH1F>("nMuons",     "nMuons",      7, -0.5,  6.5);
  nElectrons_  = fs->make<TH1F>("nElectrons", "nElectrons",  7, -0.5,  6.5);
  nLeptons_    = fs->make<TH1F>("nLeptons",   "nLeptons",   13, -0.5, 12.5);
  
  nVetoMuons_      = fs->make<TH1F>("nVetoMuons",     "nVetoMuons",      7, -0.5,  6.5);
  nVetoElectrons_  = fs->make<TH1F>("nVetoElectrons", "nVetoElectrons",  7, -0.5,  6.5);
  nVetoLeptons_    = fs->make<TH1F>("nVetoLeptons",   "nVetoLeptons",   13, -0.5, 12.5);

  MT_          = fs->make<TH1F>("MT","MT", 80, 0., 4000.);

  //-------------------------------------------------
  // Correlation
  //-------------------------------------------------
  
  MHT_nJets_ = fs->make<TH2F>("MHT_nJets", "MHT vs. nJets", 16, -0.5, 15.5, 50, 0, 2000);

}

HerwigGenEventAnalyzer::~HerwigGenEventAnalyzer()
{
}

void
HerwigGenEventAnalyzer::analyze(const edm::Event& evt, const edm::EventSetup& setup){

  //-------------------------------------------------
  // Fetch input collection from the event content
  //-------------------------------------------------

  edm::Handle<std::vector<pat::Jet> > jets;
  evt.getByLabel(jets_, jets);
  edm::Handle<std::vector<pat::Jet> > looseJets;
  evt.getByLabel(looseJets_, looseJets);
  edm::Handle<std::vector<pat::Jet> > bjets;
  evt.getByLabel(bjets_, bjets);
  edm::Handle<std::vector<pat::Muon> > muons;
  evt.getByLabel(muons_, muons);
  edm::Handle<std::vector<pat::Electron> > electrons;
  evt.getByLabel(electrons_, electrons);
  edm::Handle<std::vector<pat::Muon> > vetoMuons;
  evt.getByLabel(vetoMuons_, vetoMuons);
  edm::Handle<std::vector<pat::Electron> > vetoElectrons;
  evt.getByLabel(vetoElectrons_, vetoElectrons);
  edm::Handle<std::vector<pat::MET> > met;
  evt.getByLabel(met_, met);
  edm::Handle<SUSYGenEvent> susyGenEvent;
  evt.getByLabel(inputGenEvent_, susyGenEvent);
  edm::Handle<std::vector<reco::Vertex> > PVSrc;
  evt.getByLabel(PVSrc_, PVSrc);
  edm::Handle<edm::View<PileupSummaryInfo> > PUInfoHandle;
  evt.getByLabel(PUInfo_, PUInfoHandle);

  //-------------------------------------------------
  // Event weighting and Pile-up
  //-------------------------------------------------

  double weight=1;  

  edm::Handle<double> RA2WeightHandle;
  evt.getByLabel(RA2Weight_, RA2WeightHandle);
  weight=*RA2WeightHandle;

  edm::View<PileupSummaryInfo>::const_iterator iterPU;      
  double nvtx=-1;
  for(iterPU = PUInfoHandle->begin(); iterPU != PUInfoHandle->end(); ++iterPU)
    { 
      if (iterPU->getBunchCrossing()==0)
	{
	  nvtx = iterPU->getPU_NumInteractions();
	}
    }
  
  nPV_->Fill(PVSrc->size(), weight);
  nPU_->Fill(nvtx,          weight);

  weights_ ->Fill(weight);

  //-------------------------------------------------
  // HerwigGenEvent Analysis
  //-------------------------------------------------

  edm::Handle<HerwigGenEvent> GenEvent;
  evt.getByLabel(HerwigGenEvent_, GenEvent);

  if(GenEvent->DecayA()=="Bino") qqbarBino_->Fill(GenEvent->qqbarA());
  if(GenEvent->DecayA()=="Wino") qqbarWino_->Fill(GenEvent->qqbarA());

  if(GenEvent->DecayB()=="Bino") qqbarBino_->Fill(GenEvent->qqbarB());
  if(GenEvent->DecayB()=="Wino") qqbarWino_->Fill(GenEvent->qqbarB());

  //-------------------------------------------------
  // Temp
  //-------------------------------------------------

  edm::Handle<reco::GenParticleCollection> genParticles;
  evt.getByLabel(genParticles_, genParticles);

//   for(reco::GenParticleCollection::const_iterator t=genParticles->begin(); t!=genParticles->end(); ++t)
//     {
//       if(abs(t->pdgId())==6)
// 	{
// 	  std::cout << "-----------------------" << std::endl;
// 	  std::cout << t->mother()->pdgId() << std::endl;
// 	  std::cout << "-----------------------" << std::endl;
// 	}      
//       //std::cout << "Test" << std::endl;
//       if(abs(t->pdgId())==1000005 ||
// 	 abs(t->pdgId())==2000006 ||
// 	 abs(t->pdgId())==1000006 ||
// 	 abs(t->pdgId())==2000006 )
// 	{
// 	  std::cout << t->pdgId() << std::endl;
// 	}
//     }
  
  //loop over genParticles
//   for(reco::GenParticleCollection::const_iterator t=genParticles->begin(); t!=genParticles->end(); ++t)
//      {
//        if(t->pdgId()== 1000021 && t->numberOfDaughters() == 3)
// 	 {
// 	   std::cout << t->daughter(0)->pdgId() << std::endl;
// 	   std::cout << t->daughter(1)->pdgId() << std::endl;
// 	   std::cout << t->daughter(2)->pdgId() << std::endl;
// 	 }
//      }

  //-------------------------------------------------
  // mjj variabels
  //-------------------------------------------------

  // Example how to use member function of SUSYGenEvent
  //if(susyGenEvent->decayCascadeA()=="gluino->neutralino1" && susyGenEvent->decayCascadeB()=="gluino->neutralino1")

  //TF1 *f1 = new TF1("f1","",-3.1,3.1);
 
  if(jets->size() >= 3)
    {
      // define four-vectors
      reco::Particle::LorentzVector Jet1 = (*jets)[0].p4();
      reco::Particle::LorentzVector Jet2 = (*jets)[1].p4();
      reco::Particle::LorentzVector Jet3 = (*jets)[2].p4();

      // define invariant dijet masses
      double m12 = sqrt((Jet1+Jet2).Dot(Jet1+Jet2));   
      double m13 = sqrt((Jet1+Jet3).Dot(Jet1+Jet3));
      double m23 = sqrt((Jet2+Jet3).Dot(Jet2+Jet3));

      double minj3  = min(m13,m23);
      double min123 = min(minj3,m12);

      minj3_  -> Fill(minj3,  weight);
      min123_ -> Fill(min123, weight);


      if(jets->size() >= 4)
	{
	  reco::Particle::LorentzVector Jet4=(*jets)[3].p4();

	  double m24 = sqrt((Jet2+Jet4).Dot(Jet2+Jet4));
	  double m34 = sqrt((Jet3+Jet4).Dot(Jet3+Jet4));

	  double min234 = min(m23,min(m24,m34));

	  min234_ -> Fill(min234, weight);
	}
    }

  //-------------------------------------------------
  // Basic kinematics
  //-------------------------------------------------

  //std::cout << "Test2" << std::endl;

  if(met->size()==0) return;

  double MHT=0;
  double HT=0;
  double DeltaPtSum=0;

  int nJets70=0;
  int nJets80=0;
  int nJets100=0;
  int nJets120=0;
  int nJets150=0;
  int nJets200=0;

  //std::cout << "HerwigGenEventAnalyzer: nJets=" << jets->size() << std::endl;

  if(jets->size()>0)
    {
      reco::Particle::LorentzVector P4=(*jets)[0].p4();
      
      // loop over all loose jets
      for(int i=1; i< (int)jets->size(); ++i)
	{
	  //
	  P4=P4+(*jets)[i].p4();
  	}
      reco::Particle::LorentzVector MHTP4(-P4.X(),-P4.Y(),-P4.Z(),P4.E());

      MHT=MHTP4.pt();

      //std::cout << "HerwigGenEventAnalyzer: " << MHT << std::endl;

      for(int i=0; i<(int)jets->size(); ++i)
	{
	  //std::cout << (*jets)[i].partonFlavour() << std::endl;
	  if(i<8)
	    {
	      Jet_Pt_[i]           ->Fill((*jets)[i].pt(),  weight);
	      Jet_Eta_[i]          ->Fill((*jets)[i].eta(), weight);

	      DeltaPhi_MHT_Jet_[i] ->Fill(deltaPhi(MHTP4.phi(),     (*jets)[i].phi()), weight);
	      //if(i==0)std::cout << "deltaPhi((*met)[0].phi(), (*jets)[i].phi()): " << deltaPhi((*met)[0].phi(), (*jets)[i].phi()) << std::endl;
	      DeltaPhi_MET_Jet_[i] ->Fill(deltaPhi((*met)[0].phi(), (*jets)[i].phi()), weight);
	      RecoJetPt_MHT_[i]    ->Fill((*jets)[i].pt(),           MHT,              weight);

	      if((*jets)[i].genJet())
		{
		  Delta_Pt_[i]     ->Fill((*jets)[i].pt()-(*jets)[i].genJet()->pt(),      weight);
		  Delta_Pt_MHT_[i] ->Fill((*jets)[i].pt()-(*jets)[i].genJet()->pt(), MHT, weight);
		  GenJetPt_MHT_[i]  ->Fill((*jets)[i].genJet()->pt(),                MHT, weight);

		  DeltaPtSum=DeltaPtSum+abs((*jets)[i].pt()-(*jets)[i].genJet()->pt());
		}
	    }
	  Jets_Pt_    ->Fill((*jets)[i].pt(),  weight);
	  Jets_Eta_   ->Fill((*jets)[i].eta(), weight);
	  Jets_Phi_   ->Fill((*jets)[i].phi(), weight);
	  Jets_Theta_ ->Fill((*jets)[i].theta(), weight);
	  HT=HT+(*jets)[i].pt();
	  if((*jets)[i].partonFlavour() == 21) GluonJets_Pt_->Fill((*jets)[i].pt(),  weight);
	  
	  if((*jets)[i].pt()>70) nJets70=nJets70+1;
	  if((*jets)[i].pt()>80) nJets80=nJets70+1;
	  if((*jets)[i].pt()>100) nJets100=nJets70+1;
	  if((*jets)[i].pt()>120) nJets120=nJets70+1;
	  if((*jets)[i].pt()>150) nJets150=nJets70+1;
	  if((*jets)[i].pt()>200) nJets150=nJets70+1;

	  TCHE_  ->Fill((*jets)[i].bDiscriminator("trackCountingHighEffBJetTags"), weight);
	  TCHP_  ->Fill((*jets)[i].bDiscriminator("trackCountingHighPurBJetTags"), weight);
	  SSVHE_ ->Fill((*jets)[i].bDiscriminator("simpleSecondaryVertexHighEffBJetTags"), weight);
	  SSVHP_ ->Fill((*jets)[i].bDiscriminator("simpleSecondaryVertexHighPurBJetTags"), weight);
	}
    }
  
  double sigmaX2 = (*met)[0].getSignificanceMatrix()(0,0);
  double sigmaY2 = (*met)[0].getSignificanceMatrix()(1,1);
  double METSig  = 0;
  if(sigmaX2<1.e10 && sigmaY2<1.e10) METSig = (*met)[0].significance();
  // Use the sqrt of the significance
  if (METSig > 0.) METSig = sqrt(METSig);

  MET_->Fill((*met)[0].et(), weight);
  MHT_->Fill(MHT, weight);
  HT_->Fill(HT, weight);
  YMET_->Fill((*met)[0].et()/sqrt(HT),weight);
  METSig_->Fill(METSig, weight);
  nJets_->Fill(jets->size(), weight);
  DeltaPtSum_->Fill(DeltaPtSum, weight);
  DeltaPtSum_MHT_->Fill(DeltaPtSum, MHT, weight);
  HT_MHT_->Fill(HT, MHT, weight);

  nJets70_->Fill(nJets70, weight);
  nJets80_->Fill(nJets80, weight);
  nJets100_->Fill(nJets100, weight);
  nJets120_->Fill(nJets120, weight);
  nJets150_->Fill(nJets150, weight);
  nJets200_->Fill(nJets200, weight);

  int nBjets=bjets->size();
  if(bjets->size()>3) nBjets=3;
  nBjets_noWgt_   ->Fill(nBjets);
  nBjets_noWgt_2_ ->Fill(bjets->size());
  nBjets_         ->Fill(nBjets, weight);
  nBjets_2_       ->Fill(bjets->size(),weight);

  int nLeptons=0;
  int nMuons=0;
  int nElectrons=0;
  double LepHT=0;

  //std::cout << "Test3" << std::endl;

  // loop over muons
  for(int i=0; i<(int)muons->size(); ++i)
    {
      if(i<2)
	{
	  Muon_Pt_[i] ->Fill((*muons)[i].pt(),  weight);
	  Muon_Eta_[i]->Fill((*muons)[i].eta(), weight);
	}
      nMuons=nMuons+1;
      nLeptons=nLeptons+1;
      LepHT=LepHT+(*muons)[i].pt();
    }

  //std::cout << "Test4" << std::endl;

  // loop over electrons
  for(int i=0; i<(int)electrons->size(); ++i)
    {
      if(i<2)
	{
	  Electron_Pt_[i] ->Fill((*electrons)[i].pt(),  weight);
	  Electron_Eta_[i]->Fill((*electrons)[i].eta(), weight);
	}
      nElectrons=nElectrons+1;
      nLeptons=nLeptons+1;
      LepHT=LepHT+(*electrons)[i].pt();
    }

  nMuons_    ->Fill(nMuons,     weight);
  nElectrons_->Fill(nElectrons, weight);
  nLeptons_  ->Fill(nLeptons,   weight);

  nVetoMuons_    ->Fill(vetoMuons->size(),                       weight);
  nVetoElectrons_->Fill(vetoElectrons->size(),                   weight);
  nVetoLeptons_  ->Fill(vetoMuons->size()+vetoElectrons->size(), weight);

  //std::cout << "Test5" << std::endl;

  // MT
  double MT=LepHT+HT+(*met)[0].et();
  MT_->Fill(MT, weight);
  
  // mT
  double mT;

  const reco::LeafCandidate * singleLepton = 0;
  if(muons->size()==1) singleLepton = &(*muons)[0];
  else if(electrons->size()==1) singleLepton = &(*electrons)[0];

  if(singleLepton != 0)
    {
      mT=sqrt(2*( (*met)[0].et()*singleLepton->et() - (*met)[0].px()*singleLepton->px() - (*met)[0].py()*singleLepton->py()));
      mT_ ->Fill(mT, weight); 
    }  

  //-------------------------------------------------
  // Correlation
  //-------------------------------------------------

  MHT_nJets_->Fill(MHT, jets->size(), weight);

}


void HerwigGenEventAnalyzer::beginJob()
{  
} 

void HerwigGenEventAnalyzer::endJob()
{
}
