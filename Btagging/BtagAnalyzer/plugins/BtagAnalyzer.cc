#include "TopAnalysis/TopAnalyzer/interface/PUEventWeight.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "AnalysisDataFormats/TopObjects/interface/TtGenEvent.h"
#include "Btagging/BtagAnalyzer/plugins/BtagAnalyzer.h"
#include "AnalysisDataFormats/TopObjects/interface/TtSemiLeptonicEvent.h"
#include  <stdio.h>
#include "DataFormats/METReco/interface/CaloMETCollection.h"
#include "DataFormats/METReco/interface/CaloMET.h"
#include "DataFormats/METReco/interface/GenMET.h"
#include "DataFormats/METReco/interface/GenMETCollection.h"
#include "DataFormats/Common/interface/View.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"
#include "PhysicsTools/Utilities/interface/LumiReWeighting.h"

using namespace std;
 
BtagAnalyzer::BtagAnalyzer(const edm::ParameterSet& cfg):
  // collections of R44b objects
  jets_         (cfg.getParameter<edm::InputTag>("jets") ),
  bjets_        (cfg.getParameter<edm::InputTag>("bjets" )),
  muons_        (cfg.getParameter<edm::InputTag>("muons" )),
  electrons_    (cfg.getParameter<edm::InputTag>("electrons") ),
  met_          (cfg.getParameter<edm::InputTag>("met") ),
  // collections of matched objects
  matchedLightJets_ (cfg.getParameter<edm::InputTag>("matchedLightJets") ),
  matchedBjets_     (cfg.getParameter<edm::InputTag>("matchedBjets" ) ),
  // for event weighting
  PVSrc_          (cfg.getParameter<edm::InputTag>("PVSrc") ),
  PUInfo_         (cfg.getParameter<edm::InputTag>("PUInfo") ),
  PUWeight_       (cfg.getParameter<edm::InputTag>("PUWeight") ),
  RA2Weight_      (cfg.getParameter<edm::InputTag>("RA2Weight") ),
  BtagEffWeights_ (cfg.getParameter<edm::InputTag>("BtagEffWeights") ),
  BtagEffGrid_    (cfg.getParameter<edm::InputTag>("BtagEffGrid") ),
  // bool
  useEvtWgt_        (cfg.getParameter<bool>("useEventWeight") ),
  useBtagEffEvtWgt_ (cfg.getParameter<bool>("useBtagEffEventWeight") ),
  // int
  btagBin_          (cfg.getParameter<int>("btagBin") )

{ 
  edm::Service<TFileService> fs;

  //Dummy_=fs->make<TH1F>();
  //Dummy_->SetDefaultSumw2(true);

  //Dummy2_=fs->make<TH2F>();
  //Dummy2_->SetDefaultSumw2(true);

  // control plots
  nPV_noWgt_ = fs->make<TH1F>("nPV_noWgt","nPV_noWgt", 50, 0.,  50  );
  nPV_ = fs->make<TH1F>("nPV","nPV", 50, 0.,  50  );
  nPU_noWgt_ = fs->make<TH1F>("nPU_noWgt","nPU_noWgt", 50, 0.5, 50.5);
  nPU_ = fs->make<TH1F>("nPU","nPU", 50, 0.5, 50.5);

  btagWeights_noWgt_ = fs->make<TH1F>("btagWeights_noWgt","btagWeights_noWgt", 4, 0., 4.);
  btagWeights_PUWgt_ = fs->make<TH1F>("btagWeights_PUWgt","btagWeights_PUWgt", 4, 0., 4.);
  nBtags_noWgt_ = fs->make<TH1F>("nBtags_noWgt","nBtags_noWgt", 4, 0., 4.); 
  nBtags_PUWgt_ = fs->make<TH1F>("nBtags_PUWgt","nBtags_PUWgt", 4, 0., 4.);
  nBtags_ = fs->make<TH1F>("nBtags","nBtags", 4, 0., 4.);

  TCHE_= fs->make<TH1F>("TCHE","TCHE", 80, -20., 20.);
  TCHP_= fs->make<TH1F>("TCHP","TCHP", 80, -20., 20.);
  SSVHE_= fs->make<TH1F>("SSVHE","SSVHE", 120, -2, 10.);
  SSVHP_= fs->make<TH1F>("SSVHP","SSVHP", 120, -2, 10.);

  MET_ = fs->make<TH1F>("MET","MET", 40, 0.,  1000.);
  HT_  = fs->make<TH1F>("HT","HT",   40, 0.,  2000.);
  MHT_ = fs->make<TH1F>("MHT","MHT", 50, 0.,  1000.);

  // Jets
  JetsPt_ = fs->make<TH1F>("JetsPt","JetsPt", 70, 0.,700.);
  JetsEta_ = fs->make<TH1F>("JetsEta","JetsEta", 30, -3. , 3.);
  JetsBdisc_ = fs->make<TH1F>("JetsBdisc","JetsBdisc", 80, -10., 30.);
  NrJets_ = fs->make<TH1F>("NrJets","NrJets", 13, -0.5, 12.5);

  HighPtJetsEta_ = fs->make<TH1F>("HighPtJetsEta","HighPtJetsEta", 30, -3. , 3.);
  HighPtJetsBdisc_ = fs->make<TH1F>("HighPtJetsBdisc","HighPtJetsBdisc", 80, -10., 30.);
  NrHighPtJets_ = fs->make<TH1F>("NrHighPtJets","NrHighPtJets", 7, -0.5, 6.5);

  LowPtJetsEta_ = fs->make<TH1F>("LowPtJetsEta","LowPtJetsEta", 30, -3. , 3.);
  LowPtJetsBdisc_ = fs->make<TH1F>("LowPtJetsBdisc","LowPtJetsBdisc", 80, -10., 30.);
  NrLowPtJets_ = fs->make<TH1F>("NrLowPtJets","NrLowPtJets", 7, -0.5, 6.5);

  dPhiJetMET_=fs->make<TH1F>("dPhiJetMET","dPhi(Jet,MET)", 31, 0., 3.1);

  // Bjets
  BjetsPt_ = fs->make<TH1F>("BjetsPt","BjetsPt", 70, 0.,700.);
  BjetsEta_ = fs->make<TH1F>("BjetsEta","BjetsEta", 30, -3. , 3.);
  BjetsBdisc_ = fs->make<TH1F>("BjetsBdisc","BjetsBdisc", 80, -10., 30.);
  NrBjets_ = fs->make<TH1F>("NrBjets","NrBjets", 7, -0.5, 6.5);

  HighPtBjetsEta_ = fs->make<TH1F>("HighPtBjetsEta","HighPtBjetsEta", 30, -3. , 3.);
  HighPtBjetsBdisc_ = fs->make<TH1F>("HighPtBjetsBdisc","HighPtBjetsBdisc", 80, -10., 30.);
  NrHighPtBjets_ = fs->make<TH1F>("NrHighPtBjets","NrHighPtBjets", 7, -0.5, 6.5);

  LowPtBjetsEta_ = fs->make<TH1F>("LowPtBjetsEta","LowPtBjetsEta", 30, -3. , 3.);
  LowPtBjetsBdisc_ = fs->make<TH1F>("LowPtBjetsBdisc","LowPtBjetsBdisc", 80, -10., 30.);
  NrLowPtBjets_ = fs->make<TH1F>("NrLowPtBjets","NrLowPtBjets", 7, -0.5, 6.5);

  dPhiBjetMET_=fs->make<TH1F>("dPhiBjetMET","dPhi(Bjet,MET)", 31, 0., 3.1);

  // Btags
  BtagsPt_ = fs->make<TH1F>("BtagsPt","BtagsPt", 70, 0.,700.);
  BtagsEta_ = fs->make<TH1F>("BtagsEta","BtagsEta", 30, -3. , 3.);
  NrBtags_ = fs->make<TH1F>("NrBtags","NrBtags", 7, -0.5, 6.5);

  HighPtBtagsEta_ = fs->make<TH1F>("HighPtBtagsEta","HighPtBtagsEta", 30, -3. , 3.);
  NrHighPtBtags_ = fs->make<TH1F>("NrHighPtBtags","NrHighPtBtags", 7, -0.5, 6.5);

  LowPtBtagsEta_ = fs->make<TH1F>("LowPtBtagsEta","LowPtBtagsEta", 30, -3. , 3.);
  NrLowPtBtags_ = fs->make<TH1F>("NrLowPtBtags","NrLowPtBtags", 7, -0.5, 6.5);

  dPhiBtagMET_=fs->make<TH1F>("dPhiBtagMET","dPhi(Btag,MET)", 31, 0., 3.1);

  // Btags for >= 1 btag
  BtagsPt_1b_ = fs->make<TH1F>("BtagsPt_1b","BtagsPt_1b", 70, 0.,700.);
  BtagsEta_1b_ = fs->make<TH1F>("BtagsEta_1b","BtagsEta_1b", 30, -3. , 3.);
  
  HighPtBtagsEta_1b_ = fs->make<TH1F>("HighPtBtagsEta_1b","HighPtBtagsEta_1b", 30, -3. , 3.);
  
  LowPtBtagsEta_1b_ = fs->make<TH1F>("LowPtBtagsEta_1b","LowPtBtagsEta_1b", 30, -3. , 3.);
  
  dPhiBtagMET_1b_ =fs->make<TH1F>("dPhiBtagMET_1b","dPhi(Btag,MET)", 31, 0., 3.1);

  // Btags for >= 2 btags
  BtagsPt_2b_ = fs->make<TH1F>("BtagsPt_2b","BtagsPt_2b", 70, 0.,700.);
  BtagsEta_2b_ = fs->make<TH1F>("BtagsEta_2b","BtagsEta_2b", 30, -3. , 3.);
  
  HighPtBtagsEta_2b_ = fs->make<TH1F>("HighPtBtagsEta_2b","HighPtBtagsEta_2b", 30, -3. , 3.);
  
  LowPtBtagsEta_2b_ = fs->make<TH1F>("LowPtBtagsEta_2b","LowPtBtagsEta_2b", 30, -3. , 3.);
  
  dPhiBtagMET_2b_=fs->make<TH1F>("dPhiBtagMET_2b","dPhi(Btag,MET)", 31, 0., 3.1);

  // Btags for >= 3 btags
  BtagsPt_3b_ = fs->make<TH1F>("BtagsPt_3b","BtagsPt_3b", 70, 0.,700.);
  BtagsEta_3b_ = fs->make<TH1F>("BtagsEta_3b","BtagsEta_3b", 30, -3. , 3.);
  
  HighPtBtagsEta_3b_ = fs->make<TH1F>("HighPtBtagsEta_3b","HighPtBtagsEta_3b", 30, -3. , 3.);
  
  LowPtBtagsEta_3b_ = fs->make<TH1F>("LowPtBtagsEta_3b","LowPtBtagsEta_3b", 30, -3. , 3.);
  
  dPhiBtagMET_3b_=fs->make<TH1F>("dPhiBtagMET_3b","dPhi(Btag,MET)", 31, 0., 3.1);

}

BtagAnalyzer::~BtagAnalyzer()
{
}


void BtagAnalyzer::beginJob()
{  
} 

void
BtagAnalyzer::analyze(const edm::Event& evt, const edm::EventSetup& setup){

  //-------------------------------------------------
  // Fetch input collection from the event content
  //-------------------------------------------------

  // collections of RA4b objects
  edm::Handle<std::vector<pat::Jet> > jets;
  evt.getByLabel(jets_, jets);
  edm::Handle<std::vector<pat::Jet> > bjets;
  evt.getByLabel(bjets_, bjets);
  edm::Handle<std::vector<pat::Muon> > muons;
  evt.getByLabel(muons_, muons);
  edm::Handle<std::vector<pat::Electron> > electrons;
  evt.getByLabel(electrons_, electrons);
  edm::Handle<std::vector<pat::MET> > met;
  evt.getByLabel(met_, met);

  // collections of matched objects
  edm::Handle<std::vector<pat::Jet> > matchedLightJets;
  evt.getByLabel(matchedLightJets_, matchedLightJets);
  edm::Handle<std::vector<pat::Jet> > matchedBjets;
  evt.getByLabel(matchedBjets_, matchedBjets);

  // collection of PV vertices
  edm::Handle<std::vector<reco::Vertex> > PVSrc;
  evt.getByLabel(PVSrc_, PVSrc);


  //-------------------------------------------------
  // Event weighting
  //-------------------------------------------------

  double weight=1;

  // declare and initialize different weights
  double weightPU=1;
  double weightRA2=1;
  double weightBtagEff=1;

  // if events should be weighted
  if(useEvtWgt_)
    {
      // RA2 weight
      edm::Handle<double> RA2WeightHandle;
      evt.getByLabel(RA2Weight_, RA2WeightHandle);
      weightRA2=*RA2WeightHandle;

      weight=weightRA2;

      // PU weight
      edm::Handle<double> PUWeightHandle;
      evt.getByLabel(PUWeight_, PUWeightHandle);
      weightPU=(*PUWeightHandle);

      weight=weightRA2*weightPU;

      // number of b-tagged jets
      unsigned int nBtags = bjets->size();
      if(bjets->size() > 2) nBtags=3;
      nBtags_PUWgt_->Fill(nBtags, weight);
      
      if(useBtagEffEvtWgt_)
	{
	  // Btag weight
	  edm::Handle<std::vector<double> > BtagEffWeightsHandle;
	  evt.getByLabel(BtagEffWeights_, BtagEffWeightsHandle);
	  weightBtagEff=(*BtagEffWeightsHandle)[btagBin_];
	
	  btagWeights_noWgt_->Fill(0.,(*BtagEffWeightsHandle)[0]);
	  btagWeights_noWgt_->Fill(1, (*BtagEffWeightsHandle)[1]);
	  btagWeights_noWgt_->Fill(2, (*BtagEffWeightsHandle)[2]);
	  btagWeights_noWgt_->Fill(3, (*BtagEffWeightsHandle)[3]);

	  btagWeights_PUWgt_->Fill(0.,(*BtagEffWeightsHandle)[0]*weight);
	  btagWeights_PUWgt_->Fill(1, (*BtagEffWeightsHandle)[1]*weight);
	  btagWeights_PUWgt_->Fill(2, (*BtagEffWeightsHandle)[2]*weight);
	  btagWeights_PUWgt_->Fill(3, (*BtagEffWeightsHandle)[3]*weight);

// 	  std::cout << "SystematicsAnalyzer: " << (*BtagEffWeightsHandle).size() << std::endl;
// 	  std::cout << "SystematicsAnalyzer: " << (*BtagEffWeightsHandle)[0] << std::endl;
// 	  std::cout << "SystematicsAnalyzer: " << (*BtagEffWeightsHandle)[1] << std::endl;
// 	  std::cout << "SystematicsAnalyzer: " << (*BtagEffWeightsHandle)[2] << std::endl;
// 	  std::cout << "SystematicsAnalyzer: " << (*BtagEffWeightsHandle)[3] << std::endl;
	  
	  double summBtagWgt=(*BtagEffWeightsHandle)[0]+(*BtagEffWeightsHandle)[1]+(*BtagEffWeightsHandle)[2]+(*BtagEffWeightsHandle)[3];
	  //std::cout << "SystematicsAnalyzer: " << summBtagWgt << std::endl;
	}
      
      weight=weightRA2*weightPU*weightBtagEff;

//       std::cout << "--------------------------------" << std::endl;
//       std::cout << "weightPU: "      << weightPU      << std::endl;
//       std::cout << "weightRA2: "     << weightRA2     << std::endl;
//       std::cout << "weightBtagEff: " << weightBtagEff << std::endl << std::endl;
//       std::cout << "weight: " << weight << std::endl;
//       std::cout << "--------------------------------" << std::endl;
  
      
      // -----------------------------------------------------------------------

      // number of PU interactions only in MC available, therefore filled in this loop
      edm::Handle<edm::View<PileupSummaryInfo> > PUInfoHandle;
      evt.getByLabel(PUInfo_, PUInfoHandle);

      edm::View<PileupSummaryInfo>::const_iterator iterPU;
      
      double nvtx=-1;
      for(iterPU = PUInfoHandle->begin(); iterPU != PUInfoHandle->end(); ++iterPU)  // vector size is 3
	{ 
	  if (iterPU->getBunchCrossing()==0) // -1: previous BX, 0: current BX,  1: next BX
	    {
	      nvtx = iterPU->getPU_NumInteractions();
	    }
	}

      nPU_noWgt_->Fill(nvtx);
      nPU_->Fill(nvtx,weight);
    }

  //------------------------------------------------------
  // control plots
  //------------------------------------------------------
  
  // number of primary vertices
  nPV_noWgt_->Fill(PVSrc->size());
  nPV_->Fill(PVSrc->size(), weight);

  // number of b-tagged jets
  unsigned int nBtags = bjets->size();
  if(bjets->size() > 2) nBtags=3;
  nBtags_->Fill(nBtags,weight);
  nBtags_noWgt_->Fill(nBtags);


  // bdisc
  for(int i=0; i<(int)bjets->size();++i)
    {
      TCHE_->Fill((*bjets)[i].bDiscriminator("trackCountingHighEffBJetTags"), weight);
      TCHP_->Fill((*bjets)[i].bDiscriminator("trackCountingHighPurBJetTags"), weight);
      SSVHE_->Fill((*bjets)[i].bDiscriminator("simpleSecondaryVertexHighEffBJetTags"), weight);
      SSVHP_->Fill((*bjets)[i].bDiscriminator("simpleSecondaryVertexHighPurBJetTags"), weight);
    }

  // MET, HT, MHT
  double MET=(*met)[0].et();
  double HT=0;
  double MHT=0;

  if(jets->size()>0)
    {
      reco::Particle::LorentzVector P4=(*jets)[0].p4();
      for(int i=1; i< (int)jets->size(); ++i)
	{
	  P4=P4+(*jets)[i].p4();
  	}   
      MHT=P4.Et();
    }
  // keep HT saparate from MHT calculation
  for(int i=0; i<(int)jets->size();++i)
    {
      HT=HT+(*jets)[i].et();
    }

  MET_->Fill(MET,weight);
  HT_->Fill(HT,weight);
  MHT_->Fill(MHT,weight);

  //------------------------------------------------------
  // Kinematics of jets
  //------------------------------------------------------

  reco::Particle::LorentzVector METP4=(*met)[0].p4();

  int HighPtJets=0;
  int LowPtJets=0;
  double dPhiMin=10;
  
  //Loop over jets
  for(int idx=0; idx < (int)jets->size(); ++idx)
    {
      JetsPt_->Fill((*jets)[idx].pt(),weight);
      JetsEta_->Fill((*jets)[idx].eta(),weight);
      JetsBdisc_->Fill((*jets)[idx].bDiscriminator("trackCountingHighEffBJetTags"),weight);
      
      double dPhi=abs(deltaPhi((*jets)[idx].phi(),(*met)[0].phi()));
      if(dPhi<dPhiMin) dPhiMin=dPhi;
      
      if((*jets)[idx].pt()>240)
	{
	  HighPtJetsEta_->Fill((*jets)[idx].eta(),weight);
	  HighPtJetsBdisc_->Fill((*jets)[idx].bDiscriminator("trackCountingHighEffBJetTags"),weight);
	  HighPtJets=HighPtJets+1;
	}
      else
	{
	  LowPtJetsEta_->Fill((*jets)[idx].eta(),weight);
	  LowPtJetsBdisc_->Fill((*jets)[idx].bDiscriminator("trackCountingHighEffBJetTags"),weight);
	  LowPtJets=LowPtJets+1;
	}      
    }
  
  NrJets_->Fill(jets->size(),weight);
  NrHighPtJets_->Fill(HighPtJets,weight);
  NrLowPtJets_->Fill(LowPtJets,weight);

  dPhiJetMET_->Fill(dPhiMin,weight);

  //------------------------------------------------------
  // Kinematics of jets that can be matched to b-quarks
  //------------------------------------------------------
  
  int HighPtBjets=0;
  int LowPtBjets=0;
  double dPhiMinBjet=10;
  
  //Loop over jets that can be natched to b-quarks
  for(int idx=0; idx < (int)matchedBjets->size(); ++idx)
    {
      BjetsPt_->Fill((*matchedBjets)[idx].pt(),weight);
      BjetsEta_->Fill((*matchedBjets)[idx].eta(),weight);
      BjetsBdisc_->Fill((*matchedBjets)[idx].bDiscriminator("trackCountingHighEffBJetTags"),weight);
      
      double dPhi=abs(deltaPhi((*matchedBjets)[idx].phi(),(*met)[0].phi()));
      if(dPhi<dPhiMinBjet) dPhiMinBjet=dPhi;
      
      if((*matchedBjets)[idx].pt()>240)
	{
	  HighPtBjetsEta_->Fill((*matchedBjets)[idx].eta(),weight);
	  HighPtBjetsBdisc_->Fill((*matchedBjets)[idx].bDiscriminator("trackCountingHighEffBJetTags"),weight);
	  HighPtBjets=HighPtBjets+1;
	}
      else
	{
	  LowPtBjetsEta_->Fill((*matchedBjets)[idx].eta(),weight);
	  LowPtBjetsBdisc_->Fill((*matchedBjets)[idx].bDiscriminator("trackCountingHighEffBJetTags"),weight);
	  LowPtBjets=LowPtBjets+1;
	}      
    }
  
  NrBjets_->Fill(matchedBjets->size(),weight);
  NrHighPtBjets_->Fill(HighPtBjets,weight);
  NrLowPtBjets_->Fill(LowPtBjets,weight);

  dPhiBjetMET_->Fill(dPhiMinBjet,weight);

  //------------------------------------------------------
  // Kinematics of B-tagged jets ("btags")
  //------------------------------------------------------
  
  int HighPtBtags=0;
  int LowPtBtags=0;
  double dPhiMinBtag=10;
  
  //Loop over b-tagged jets ("btags")
  for(int idx=0; idx < (int)bjets->size(); ++idx)
    {
      BtagsPt_->Fill((*bjets)[idx].pt(),weight);
      BtagsEta_->Fill((*bjets)[idx].eta(),weight);
            
      double dPhi=abs(deltaPhi((*bjets)[idx].phi(),(*met)[0].phi()));
      if(dPhi<dPhiMinBtag) dPhiMinBtag=dPhi;
      
      if((*bjets)[idx].pt()>240)
	{
	  HighPtBtagsEta_->Fill((*bjets)[idx].eta(),weight);
	  HighPtBtags=HighPtBtags+1;
	}
      else
	{
	  LowPtBtagsEta_->Fill((*bjets)[idx].eta(),weight);
	  LowPtBtags=LowPtBtags+1;
	}      
    }
  
  NrBtags_->Fill(bjets->size(),weight);
  NrHighPtBtags_->Fill(HighPtBtags,weight);
  NrLowPtBtags_->Fill(LowPtBtags,weight);

  dPhiBtagMET_->Fill(dPhiMinBtag,weight);

  //------------------------------------------------------
  // Kinematics of B-tagged jets - events with >= 1 btags
  //------------------------------------------------------

  if(bjets->size()>0)
    {
      double dPhiMinBtag_1b=10;
      
      // Loop over b-tagged jets ("btags")
      for(int idx=0; idx < (int)bjets->size(); ++idx)
	{
	  BtagsPt_1b_->Fill((*bjets)[idx].pt(),weight);
	  BtagsEta_1b_->Fill((*bjets)[idx].eta(),weight);
	  	  
	  double dPhi=abs(deltaPhi((*bjets)[idx].phi(),(*met)[0].phi()));
	  if(dPhi<dPhiMinBtag_1b) dPhiMinBtag_1b=dPhi;
	  
	  if((*bjets)[idx].pt()>240)
	    {
	      HighPtBtagsEta_1b_->Fill((*bjets)[idx].eta(),weight);
	    }
	  else
	    {
	      LowPtBtagsEta_1b_->Fill((*bjets)[idx].eta(),weight);
	    }      
	}
      
      dPhiBtagMET_1b_->Fill(dPhiMinBtag_1b,weight);
    }
  
  //------------------------------------------------------
  // Kinematics of B-tagged jets - events with >= 2 btags
  //------------------------------------------------------
  
  if(bjets->size()>1)
    {
      double dPhiMinBtag_2b=10;
      
      // Loop over b-tagged jets ("btags")
      for(int idx=0; idx < (int)bjets->size(); ++idx)
	{
	  BtagsPt_2b_->Fill((*bjets)[idx].pt(),weight);
	  BtagsEta_2b_->Fill((*bjets)[idx].eta(),weight);
	  
	  double dPhi=abs(deltaPhi((*bjets)[idx].phi(),(*met)[0].phi()));
	  if(dPhi<dPhiMinBtag_2b) dPhiMinBtag_2b=dPhi;
	  
	  if((*bjets)[idx].pt()>240)
	    {
	      HighPtBtagsEta_2b_->Fill((*bjets)[idx].eta(),weight);
	    }
	  else
	    {
	      LowPtBtagsEta_2b_->Fill((*bjets)[idx].eta(),weight);
	    }      
	}
      
      dPhiBtagMET_2b_->Fill(dPhiMinBtag_2b,weight);
    }

  //------------------------------------------------------
  // Kinematics of B-tagged jets - events with >= 3 btags
  //------------------------------------------------------
  
  if(bjets->size()>2)
    {
      double dPhiMinBtag_3b=10;
      
      // Loop over b-tagged jets ("btags")
      for(int idx=0; idx < (int)bjets->size(); ++idx)
	{
	  BtagsPt_3b_->Fill((*bjets)[idx].pt(),weight);
	  BtagsEta_3b_->Fill((*bjets)[idx].eta(),weight);
	  
	  double dPhi=abs(deltaPhi((*bjets)[idx].phi(),(*met)[0].phi()));
	  if(dPhi<dPhiMinBtag_3b) dPhiMinBtag_3b=dPhi;
	  
	  if((*bjets)[idx].pt()>240)
	    {
	      HighPtBtagsEta_3b_->Fill((*bjets)[idx].eta(),weight);
	    }
	  else
	    {
	      LowPtBtagsEta_3b_->Fill((*bjets)[idx].eta(),weight);
	    }      
	}
      
      dPhiBtagMET_3b_->Fill(dPhiMinBtag_3b,weight);
    }
}

void BtagAnalyzer::endJob()
{
}
