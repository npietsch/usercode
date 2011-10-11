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
  met_              (cfg.getParameter<edm::InputTag>("met")),
  jets_             (cfg.getParameter<edm::InputTag>("jets")),
  bjets_            (cfg.getParameter<edm::InputTag>("bjets")), 
  matchedLightJets_ (cfg.getParameter<edm::InputTag>("matchedLightJets")),
  matchedBjets_     (cfg.getParameter<edm::InputTag>("matchedBjets")),
  muons_            (cfg.getParameter<edm::InputTag>("muons")),
  electrons_        (cfg.getParameter<edm::InputTag>("electrons")),
  pvSrc_            (cfg.getParameter<edm::InputTag>("pvSrc") ),
  weight_           (cfg.getParameter<edm::InputTag>("weight") ),
  PUSource_         (cfg.getParameter<edm::InputTag>("PUInfo") ),
  RA2weight_        (cfg.getParameter<edm::InputTag>("RA2weight") ),
  useEvtWgt_        (cfg.getParameter<bool>("useEventWeight") )

{ 
  edm::Service<TFileService> fs;

  Dummy_=fs->make<TH1F>();
  Dummy2_=fs->make<TH2F>();

  //Dummy_->SetDefaultSumw2(true);
  //Dummy2_->SetDefaultSumw2(true);
  
  // Jets
  JetsPt_ = fs->make<TH1F>("JetsPt","JetsPt", 50, 0.,500.);
  JetsEta_ = fs->make<TH1F>("JetsEta","JetsEta", 70, -3.5 , 3.5);
  JetsBdisc_ = fs->make<TH1F>("JetsBdisc","JetsBdisc", 160, -20., 20.);
  NrJets_ = fs->make<TH1F>("NrJets","NrJets", 13, -0.5, 12.5);

  HighPtJetsEta_ = fs->make<TH1F>("HighPtJetsEta","HighPtJetsEta", 70, -3.5 , 3.5);
  HighPtJetsBdisc_ = fs->make<TH1F>("HighPtJetsBdisc","HighPtJetsBdisc", 160, -20., 20.);
  NrHighPtJets_ = fs->make<TH1F>("NrHighPtJets","NrHighPtJets", 7, -0.5, 6.5);

  LowPtJetsEta_ = fs->make<TH1F>("LowPtJetsEta","LowPtJetsEta", 70, -3.5 , 3.5);
  LowPtJetsBdisc_ = fs->make<TH1F>("LowPtJetsBdisc","LowPtJetsBdisc", 160, -20., 20.);
  NrLowPtJets_ = fs->make<TH1F>("NrLowPtJets","NrLowPtJets", 7, -0.5, 6.5);

  dRJetMET_=fs->make<TH1F>("dRJetMET","dR(Jet,MET)", 16, 0., 3.2);

  // Bjets
  BjetsPt_ = fs->make<TH1F>("BjetsPt","BjetsPt", 50, 0.,500.);
  BjetsEta_ = fs->make<TH1F>("BjetsEta","BjetsEta", 70, -3.5 , 3.5);
  BjetsBdisc_ = fs->make<TH1F>("BjetsBdisc","BjetsBdisc", 160, -20., 20.);
  NrBjets_ = fs->make<TH1F>("NrBjets","NrBjets", 7, -0.5, 6.5);

  HighPtBjetsEta_ = fs->make<TH1F>("HighPtBjetsEta","HighPtBjetsEta", 70, -3.5 , 3.5);
  HighPtBjetsBdisc_ = fs->make<TH1F>("HighPtBjetsBdisc","HighPtBjetsBdisc", 160, -20., 20.);
  NrHighPtBjets_ = fs->make<TH1F>("NrHighPtBjets","NrHighPtBjets", 7, -0.5, 6.5);

  LowPtBjetsEta_ = fs->make<TH1F>("LowPtBjetsEta","LowPtBjetsEta", 70, -3.5 , 3.5);
  LowPtBjetsBdisc_ = fs->make<TH1F>("LowPtBjetsBdisc","LowPtBjetsBdisc", 160, -20., 20.);
  NrLowPtBjets_ = fs->make<TH1F>("NrLowPtBjets","NrLowPtBjets", 7, -0.5, 6.5);

  dRBjetMET_=fs->make<TH1F>("dRBjetMET","dR(Bjet,MET)", 16, 0., 3.2);

  // Btags
  BtagsPt_ = fs->make<TH1F>("BtagsPt","BtagsPt", 50, 0.,500.);
  BtagsEta_ = fs->make<TH1F>("BtagsEta","BtagsEta", 70, -3.5 , 3.5);
  NrBtags_ = fs->make<TH1F>("NrBtags","NrBtags", 7, -0.5, 6.5);

  HighPtBtagsEta_ = fs->make<TH1F>("HighPtBtagsEta","HighPtBtagsEta", 70, -3.5 , 3.5);
  NrHighPtBtags_ = fs->make<TH1F>("NrHighPtBtags","NrHighPtBtags", 7, -0.5, 6.5);

  LowPtBtagsEta_ = fs->make<TH1F>("LowPtBtagsEta","LowPtBtagsEta", 70, -3.5 , 3.5);
  NrLowPtBtags_ = fs->make<TH1F>("NrLowPtBtags","NrLowPtBtags", 7, -0.5, 6.5);

  dRBtagMET_=fs->make<TH1F>("dRBtagMET","dR(Btag,MET)", 16, 0., 3.2);

  // Btags for >= 1 btag
  BtagsPt_1b_ = fs->make<TH1F>("BtagsPt_1b","BtagsPt_1b", 50, 0.,500.);
  BtagsEta_1b_ = fs->make<TH1F>("BtagsEta_1b","BtagsEta_1b", 70, -3.5 , 3.5);
  
  HighPtBtagsEta_1b_ = fs->make<TH1F>("HighPtBtagsEta_1b","HighPtBtagsEta_1b", 70, -3.5 , 3.5);
  
  LowPtBtagsEta_1b_ = fs->make<TH1F>("LowPtBtagsEta_1b","LowPtBtagsEta_1b", 70, -3.5 , 3.5);
  
  dRBtagMET_1b_ =fs->make<TH1F>("dRBtagMET_1b","dR(Btag,MET)", 16, 0., 3.2);

  // Btags for >= 2 btags
  BtagsPt_2b_ = fs->make<TH1F>("BtagsPt_2b","BtagsPt_2b", 50, 0.,500.);
  BtagsEta_2b_ = fs->make<TH1F>("BtagsEta_2b","BtagsEta_2b", 70, -3.5 , 3.5);
  
  HighPtBtagsEta_2b_ = fs->make<TH1F>("HighPtBtagsEta_2b","HighPtBtagsEta_2b", 70, -3.5 , 3.5);
  
  LowPtBtagsEta_2b_ = fs->make<TH1F>("LowPtBtagsEta_2b","LowPtBtagsEta_2b", 70, -3.5 , 3.5);
  
  dRBtagMET_2b_=fs->make<TH1F>("dRBtagMET_2b","dR(Btag,MET)", 16, 0., 3.2);

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
  // Handles
  //-------------------------------------------------
  
  edm::Handle<std::vector<pat::MET> > met;
  evt.getByLabel(met_, met);

  edm::Handle<std::vector<pat::Jet> > jets;
  evt.getByLabel(jets_, jets);

  edm::Handle<std::vector<pat::Jet> > bjets;
  evt.getByLabel(bjets_, bjets);

  edm::Handle<std::vector<pat::Jet> > matchedLightJets;
  evt.getByLabel(matchedLightJets_, matchedLightJets);

  edm::Handle<std::vector<pat::Jet> > matchedBjets;
  evt.getByLabel(matchedBjets_, matchedBjets);

  edm::Handle<std::vector<pat::Muon> > muons;
  evt.getByLabel(muons_, muons);

  edm::Handle<std::vector<pat::Electron> > electrons;
  evt.getByLabel(electrons_, electrons);

  edm::Handle<std::vector<reco::Vertex> > pvSrc;
  evt.getByLabel(pvSrc_, pvSrc);


  //-------------------------------------------------
  // Weighting
  //-------------------------------------------------

  double weight=1;
  double weightPU=1;
  double weightRA2=1;

  if(useEvtWgt_)
    {
      edm::Handle<double> weightHandle;
      evt.getByLabel(weight_, weightHandle);
      weightPU=*weightHandle;

      edm::Handle<edm::View<PileupSummaryInfo> > PUInfo;
      evt.getByLabel(PUSource_, PUInfo);

      edm::View<PileupSummaryInfo>::const_iterator iterPU;
      
      double nvtx=-1;
      
      for(iterPU = PUInfo->begin(); iterPU != PUInfo->end(); ++iterPU)  // vector size is 3
	{ 
	  if (iterPU->getBunchCrossing()==0) // -1: previous BX, 0: current BX,  1: next BX
	    {
	      nvtx = iterPU->getPU_NumInteractions();
	    }
	}

      edm::Handle<double> RA2weightHandle;
      evt.getByLabel(RA2weight_, RA2weightHandle);
      weightRA2=*RA2weightHandle;

      weight=weightPU*weightRA2;
    }

  //------------------------------------------------------
  // Kinematics of jets
  //------------------------------------------------------
  
  reco::Particle::LorentzVector MET=(*met)[0].p4();

  int HighPtJets=0;
  int LowPtJets=0;
  double dRMin=10;
  
  //Loop over jets
  for(int idx=0; idx < (int)jets->size(); ++idx)
    {
      JetsPt_->Fill((*jets)[idx].pt(),weight);
      JetsEta_->Fill((*jets)[idx].eta(),weight);
      JetsBdisc_->Fill((*jets)[idx].bDiscriminator("trackCountingHighEffBJetTags"),weight);
      
      double dR=abs(deltaR((*jets)[idx].eta(),(*jets)[idx].phi(),(*met)[0].eta(),(*met)[0].phi()));
      if(dR<dRMin) dRMin=dR;
      
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

  dRJetMET_->Fill(dRMin,weight);

  //------------------------------------------------------
  // Kinematics of jets that can be matched to b-quarks
  //------------------------------------------------------
  
  int HighPtBjets=0;
  int LowPtBjets=0;
  double dRMinBjet=10;
  
  //Loop over jets that can be natched to b-quarks
  for(int idx=0; idx < (int)matchedBjets->size(); ++idx)
    {
      BjetsPt_->Fill((*matchedBjets)[idx].pt(),weight);
      BjetsEta_->Fill((*matchedBjets)[idx].eta(),weight);
      BjetsBdisc_->Fill((*matchedBjets)[idx].bDiscriminator("trackCountingHighEffBJetTags"),weight);
      
      double dR=abs(deltaR((*matchedBjets)[idx].eta(),(*matchedBjets)[idx].phi(),(*met)[0].eta(),(*met)[0].phi()));
      if(dR<dRMinBjet) dRMinBjet=dR;
      
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

  dRBjetMET_->Fill(dRMinBjet,weight);

  //------------------------------------------------------
  // Kinematics of B-tagged jets ("btags")
  //------------------------------------------------------
  
  int HighPtBtags=0;
  int LowPtBtags=0;
  double dRMinBtag=10;
  
  //Loop over b-tagged jets ("btags")
  for(int idx=0; idx < (int)bjets->size(); ++idx)
    {
      BtagsPt_->Fill((*bjets)[idx].pt(),weight);
      BtagsEta_->Fill((*bjets)[idx].eta(),weight);
            
      double dR=abs(deltaR((*bjets)[idx].eta(),(*bjets)[idx].phi(),(*met)[0].eta(),(*met)[0].phi()));
      if(dR<dRMinBtag) dRMinBtag=dR;
      
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

  dRBtagMET_->Fill(dRMinBtag,weight);

  //------------------------------------------------------
  // Kinematics of B-tagged jets - events with >= 1 btags
  //------------------------------------------------------

  if(bjets->size()>0)
    {
      double dRMinBtag_1b=10;
      
      // Loop over b-tagged jets ("btags")
      for(int idx=0; idx < (int)bjets->size(); ++idx)
	{
	  BtagsPt_1b_->Fill((*bjets)[idx].pt(),weight);
	  BtagsEta_1b_->Fill((*bjets)[idx].eta(),weight);
	  	  
	  double dR=abs(deltaR((*bjets)[idx].eta(),(*bjets)[idx].phi(),(*met)[0].eta(),(*met)[0].phi()));
	  if(dR<dRMinBtag_1b) dRMinBtag_1b=dR;
	  
	  if((*bjets)[idx].pt()>240)
	    {
	      HighPtBtagsEta_1b_->Fill((*bjets)[idx].eta(),weight);
	    }
	  else
	    {
	      LowPtBtagsEta_1b_->Fill((*bjets)[idx].eta(),weight);
	    }      
	}
      
      dRBtagMET_1b_->Fill(dRMinBtag_1b,weight);
    }
  
  //------------------------------------------------------
  // Kinematics of B-tagged jets - events with >= 2 btags
  //------------------------------------------------------
  
  if(bjets->size()>1)
    {
      double dRMinBtag_2b=10;
      
      // Loop over b-tagged jets ("btags")
      for(int idx=0; idx < (int)bjets->size(); ++idx)
	{
	  BtagsPt_2b_->Fill((*bjets)[idx].pt(),weight);
	  BtagsEta_2b_->Fill((*bjets)[idx].eta(),weight);
	  
	  double dR=abs(deltaR((*bjets)[idx].eta(),(*bjets)[idx].phi(),(*met)[0].eta(),(*met)[0].phi()));
	  if(dR<dRMinBtag_2b) dRMinBtag_2b=dR;
	  
	  if((*bjets)[idx].pt()>240)
	    {
	      HighPtBtagsEta_2b_->Fill((*bjets)[idx].eta(),weight);
	    }
	  else
	    {
	      LowPtBtagsEta_2b_->Fill((*bjets)[idx].eta(),weight);
	    }      
	}
      
      dRBtagMET_2b_->Fill(dRMinBtag_2b,weight);
    }
}

void BtagAnalyzer::endJob()
{
}