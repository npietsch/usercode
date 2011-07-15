#include "TopAnalysis/TopAnalyzer/interface/PUEventWeight.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "AnalysisDataFormats/TopObjects/interface/TtGenEvent.h"
#include "SUSYAnalysis/SUSYAnalyzer/plugins/BjetsAnalyzer.h"
#include "AnalysisDataFormats/TopObjects/interface/TtSemiLeptonicEvent.h"
#include  <stdio.h>
#include "DataFormats/METReco/interface/CaloMETCollection.h"
#include "DataFormats/METReco/interface/CaloMET.h"
#include "DataFormats/METReco/interface/GenMET.h"
#include "DataFormats/METReco/interface/GenMETCollection.h"
#include "SUSYAnalysis/SUSYObjects/interface/SUSYGenEvent.h"

using namespace std;

BjetsAnalyzer::BjetsAnalyzer(const edm::ParameterSet& cfg):
  src_          (cfg.getParameter<edm::InputTag>("source")),
  met_          (cfg.getParameter<edm::InputTag>("met")),
  jets_         (cfg.getParameter<edm::InputTag>("jets")),
  muons_        (cfg.getParameter<edm::InputTag>("muons")),
  electrons_    (cfg.getParameter<edm::InputTag>("electrons")),
  looseTrackHighPurBjets_(cfg.getParameter<edm::InputTag>("looseTrackHighPurBjets")),
  mediumTrackHighPurBjets_(cfg.getParameter<edm::InputTag>("mediumTrackHighPurBjets")),
  tightTrackHighPurBjets_(cfg.getParameter<edm::InputTag>("tightTrackHighPurBjets")),
  looseTrackHighEffBjets_(cfg.getParameter<edm::InputTag>("looseTrackHighEffBjets")),
  mediumTrackHighEffBjets_(cfg.getParameter<edm::InputTag>("mediumTrackHighEffBjets")),
  tightTrackHighEffBjets_(cfg.getParameter<edm::InputTag>("tightTrackHighEffBjets")),
  pvSrc_        (cfg.getParameter<edm::InputTag>("pvSrc") ),
  weight_       (cfg.getParameter<edm::InputTag>("weight") ),
  useEvtWgt_    (cfg.getParameter<bool>("useEventWeight") )
{ 
  edm::Service<TFileService> fs;
  
  for(int i=0; i<4; ++i)
    {
      for(int j=0; j < 5; ++j)
	{
	  char histname[20];
	  sprintf(histname,"nbjets_%i_%i",i, j);
	  nbjets_[i][j]=fs->make<TH1F>(histname,"# of Bjets",10 , -0.5, 9.5);
	}
    }
  for(int i2=0; i2<2; ++i2)
    {
      for(int j2=0; j2 < 6; ++j2)
	{
	  char histname[20];
	  sprintf(histname,"Bdisc_%i_%i",i2, j2);
	  Bdisc_[i2][j2]=fs->make<TH1F>(histname,"bDiscriminator",160, -20., 20.);
	}
    }
  for(int i3=2; i3<4; ++i3)
    {
      for(int j3=0; j3 < 6; ++j3)
	{
	  char histname3[20];
	  sprintf(histname3,"Bdisc_%i_%i",i3, j3);
	  Bdisc_[i3][j3]=fs->make<TH1F>(histname3,"bDiscriminator",22 , -1, 10.);
	}
    }
  for(int i4=0; i4<4; ++i4)
    {
      for(int j4=0; j4 < 6; ++j4)
	{
	  char histname4[20];
	  sprintf(histname4,"BtagEt_%i_%i",i4, j4);
	  BtagEt_[i4][j4]=fs->make<TH1F>(histname4,"Et Btag",90 , 0., 900.);
	}
    }

  nLooseBjetsTrackHighPur_=fs->make<TH1F>("nLooseBjetsTrackHighPur","# loose bjets TrackHighPur",10 , -0.5, 9.5);
  nMediumBjetsTrackHighPur_=fs->make<TH1F>("nMediumBjetsTrackHighPur","# medium bjets TrackHighPur",10 , -0.5, 9.5);
  nTightBjetsTrackHighPur_=fs->make<TH1F>("nTightBjetsTrackHighPur","# tight bjets TrackHighPur",10 , -0.5, 9.5);
  nLooseBjetsTrackHighEff_=fs->make<TH1F>("nLooseBjetsTrackHighEff","# loose bjets TrackHighEff",10 , -0.5, 9.5);
  nMediumBjetsTrackHighEff_=fs->make<TH1F>("nMediumBjetsTrackHighEff","# medium bjets TrackHighEff",10 , -0.5, 9.5);
  nTightBjetsTrackHighEff_=fs->make<TH1F>("nTightBjetsTrackHighEff","# tight bjets TrackHighEff",10 , -0.5, 9.5);

  nLooseBjetsTrackHighPur1pv_=fs->make<TH1F>("nLooseBjetsTrackHighPur1pv","# loose bjets TrackHighPur 1pv",10 , -0.5, 9.5);
  nMediumBjetsTrackHighPur1pv_=fs->make<TH1F>("nMediumBjetsTrackHighPur1pv","# medium bjets TrackHighPur 1pv",10 , -0.5, 9.5);
  nTightBjetsTrackHighPur1pv_=fs->make<TH1F>("nTightBjetsTrackHighPur1pv","# tight bjets TrackHighPur 1pv",10 , -0.5, 9.5);
  nLooseBjetsTrackHighEff1pv_=fs->make<TH1F>("nLooseBjetsTrackHighEff1pv","# loose bjets TrackHighEff 1pv",10 , -0.5, 9.5);
  nMediumBjetsTrackHighEff1pv_=fs->make<TH1F>("nMediumBjetsTrackHighEff1pv","# medium bjets TrackHighEff 1pv",10 , -0.5, 9.5);
  nTightBjetsTrackHighEff1pv_=fs->make<TH1F>("nTightBjetsTrackHighEff1pv","# tight bjets TrackHighEff 1pv",10 , -0.5, 9.5);

  nLooseBjetsTrackHighPur2pv_=fs->make<TH1F>("nLooseBjetsTrackHighPur2pv","# loose bjets TrackHighPur 2pv",10 , -0.5, 9.5);
  nMediumBjetsTrackHighPur2pv_=fs->make<TH1F>("nMediumBjetsTrackHighPur2pv","# medium bjets TrackHighPur 2pv",10 , -0.5, 9.5);
  nTightBjetsTrackHighPur2pv_=fs->make<TH1F>("nTightBjetsTrackHighPur2pv","# tight bjets TrackHighPur 2pv",10 , -0.5, 9.5);
  nLooseBjetsTrackHighEff2pv_=fs->make<TH1F>("nLooseBjetsTrackHighEff2pv","# loose bjets TrackHighEff 2pv",10 , -0.5, 9.5);
  nMediumBjetsTrackHighEff2pv_=fs->make<TH1F>("nMediumBjetsTrackHighEff2pv","# medium bjets TrackHighEff 2pv",10 , -0.5, 9.5);
  nTightBjetsTrackHighEff2pv_=fs->make<TH1F>("nTightBjetsTrackHighEff2pv","# tight bjets TrackHighEff 2pv",10 , -0.5, 9.5);

  nLooseBjetsTrackHighPur3pv_=fs->make<TH1F>("nLooseBjetsTrackHighPur3pv","# loose bjets TrackHighPur 3pv",10 , -0.5, 9.5);
  nMediumBjetsTrackHighPur3pv_=fs->make<TH1F>("nMediumBjetsTrackHighPur3pv","# medium bjets TrackHighPur 3pv",10 , -0.5, 9.5);
  nTightBjetsTrackHighPur3pv_=fs->make<TH1F>("nTightBjetsTrackHighPur3pv","# tight bjets TrackHighPur 3pv",10 , -0.5, 9.5);
  nLooseBjetsTrackHighEff3pv_=fs->make<TH1F>("nLooseBjetsTrackHighEff3pv","# loose bjets TrackHighEff 3pv",10 , -0.5, 9.5);
  nMediumBjetsTrackHighEff3pv_=fs->make<TH1F>("nMediumBjetsTrackHighEff3pv","# medium bjets TrackHighEff 3pv",10 , -0.5, 9.5);
  nTightBjetsTrackHighEff3pv_=fs->make<TH1F>("nTightBjetsTrackHighEff3pv","# tight bjets TrackHighEff 3pv",10 , -0.5, 9.5);

  nLooseBjetsTrackHighPur4pv_=fs->make<TH1F>("nLooseBjetsTrackHighPur4pv","# loose bjets TrackHighPur 4pv",10 , -0.5, 9.5);
  nMediumBjetsTrackHighPur4pv_=fs->make<TH1F>("nMediumBjetsTrackHighPur4pv","# medium bjets TrackHighPur 4pv",10 , -0.5, 9.5);
  nTightBjetsTrackHighPur4pv_=fs->make<TH1F>("nTightBjetsTrackHighPur4pv","# tight bjets TrackHighPur 4pv",10 , -0.5, 9.5);
  nLooseBjetsTrackHighEff4pv_=fs->make<TH1F>("nLooseBjetsTrackHighEff4pv","# loose bjets TrackHighEff 4pv",10 , -0.5, 9.5);
  nMediumBjetsTrackHighEff4pv_=fs->make<TH1F>("nMediumBjetsTrackHighEff4pv","# medium bjets TrackHighEff 4pv",10 , -0.5, 9.5);
  nTightBjetsTrackHighEff4pv_=fs->make<TH1F>("nTightBjetsTrackHighEff4pv","# tight bjets TrackHighEff 4pv",10 , -0.5, 9.5);
  
  nLooseBjetsTrackHighPur5pv_=fs->make<TH1F>("nLooseBjetsTrackHighPur5pv","# loose bjets TrackHighPur 5pv",10 , -0.5, 9.5);
  nMediumBjetsTrackHighPur5pv_=fs->make<TH1F>("nMediumBjetsTrackHighPur5pv","# medium bjets TrackHighPur 5pv",10 , -0.5, 9.5);
  nTightBjetsTrackHighPur5pv_=fs->make<TH1F>("nTightBjetsTrackHighPur5pv","# tight bjets TrackHighPur 5pv",10 , -0.5, 9.5);
  nLooseBjetsTrackHighEff5pv_=fs->make<TH1F>("nLooseBjetsTrackHighEff5pv","# loose bjets TrackHighEff 5pv",10 , -0.5, 9.5);
  nMediumBjetsTrackHighEff5pv_=fs->make<TH1F>("nMediumBjetsTrackHighEff5pv","# medium bjets TrackHighEff 5pv",10 , -0.5, 9.5);
  nTightBjetsTrackHighEff5pv_=fs->make<TH1F>("nTightBjetsTrackHighEff5pv","# tight bjets TrackHighEff 1pv",10 , -0.5, 9.5);

  bdiscTrackHighEff_=fs->make<TH1F>("bdiscTrackHighEff","bdiscTrackHighEff",200, -25., 25.);
  bdiscTrackHighPur_=fs->make<TH1F>("bdiscTrackHighPur","bdiscTrackHighPur",200, -25., 25.);

  bdiscTrackHighEff1pv_=fs->make<TH1F>("bdiscTrackHighEff1pv","bdiscTrackHighEff1pv",200, -25., 25.);
  bdiscTrackHighPur1pv_=fs->make<TH1F>("bdiscTrackHighPur1pv","bdiscTrackHighPur1pv",200, -25., 25.);

  bdiscTrackHighEff2pv_=fs->make<TH1F>("bdiscTrackHighEff2pv","bdiscTrackHighEff2pv",200, -25., 25.);
  bdiscTrackHighPur2pv_=fs->make<TH1F>("bdiscTrackHighPur2pv","bdiscTrackHighPur2pv",200, -25., 25.);

  bdiscTrackHighEff3pv_=fs->make<TH1F>("bdiscTrackHighEff3pv","bdiscTrackHighEff3pv",200, -25., 25.);
  bdiscTrackHighPur3pv_=fs->make<TH1F>("bdiscTrackHighPur3pv","bdiscTrackHighPur3pv",200, -25., 25.);

  bdiscTrackHighEff4pv_=fs->make<TH1F>("bdiscTrackHighEff4pv","bdiscTrackHighEff4pv",200, -25., 25.);
  bdiscTrackHighPur4pv_=fs->make<TH1F>("bdiscTrackHighPur4pv","bdiscTrackHighPur4pv",200, -25., 25.);

  bdiscTrackHighEff5pv_=fs->make<TH1F>("bdiscTrackHighEff5pv","bdiscTrackHighEff5pv",200, -25., 25.);
  bdiscTrackHighPur5pv_=fs->make<TH1F>("bdiscTrackHighPur5pv","bdiscTrackHighPur5pv",200, -25., 25.);

  for(int j5=0; j5<6; ++j5)
    {
      char histnamej5_1[20];
      char histnamej5_2[20];
      char histnamej5_3[20];
      char histnamej5_4[20];
      char histnamej5_5[20];
      char histnamej5_6[20];
      char histnamej5_7[20];
      char histnamej5_8[20];
      
      sprintf(histnamej5_1,"angleb1b2_%i",j5);
      sprintf(histnamej5_2,"mbb_%i",j5);
      sprintf(histnamej5_3,"DeltaPhi_%i",j5);
      sprintf(histnamej5_4,"Jet1_Et_2Bjets_%i",j5);
      sprintf(histnamej5_5,"Bjet1_Et_%i",j5);
      sprintf(histnamej5_6,"Bjet2_Et_%i",j5);
      sprintf(histnamej5_7,"Bjet2_Et_%i",j5);
      sprintf(histnamej5_8,"HT_2Bjets_1LightJet_%i",j5);
      
      angleb1b2_.push_back( fs->make<TH1F>(histnamej5_1,"angle (bjet1,bjet2)", 31, 0.,  3.1));
      mbb_.push_back( fs->make<TH1F>(histnamej5_2,"invariant bb mass", 90, 0.,  900));
      deltaPhi_.push_back( fs->make<TH1F>(histnamej5_3,"delta Phi(b,b)", 31 , 0., 3.1));
      Jet1_Et_2Bjets_.push_back( fs->make<TH1F>(histnamej5_4,"Et Jet1 2Bjets", 90 , 0, 900));
      Bjet1_Et_.push_back( fs->make<TH1F>(histnamej5_5,"Et Bjet1", 90 , 0, 900));
      Bjet2_Et_.push_back( fs->make<TH1F>(histnamej5_6,"Et Bjet2", 90 , 0, 900));
      HT_2Bjets_.push_back( fs->make<TH1F>(histnamej5_7,    "HT (2bjets)", 40, 0., 2000.));
      HT_2Bjets_1LightJet_.push_back( fs->make<TH1F>(histnamej5_8,    "HT (2bjets+1lightjet)", 40, 0., 2000.));
    }
}

BjetsAnalyzer::~BjetsAnalyzer()
{
}

void
BjetsAnalyzer::analyze(const edm::Event& evt, const edm::EventSetup& setup)
{  
  //--------------------------------------------------
  // Handles
  //-------------------------------------------------
  
  edm::Handle<reco::GenParticleCollection> src;
  evt.getByLabel(src_, src);
  edm::Handle<std::vector<pat::MET> > met;
  evt.getByLabel(met_, met);
  edm::Handle<std::vector<pat::Jet> > jets;
  evt.getByLabel(jets_, jets);
  edm::Handle<std::vector<pat::Muon> > muons;
  evt.getByLabel(muons_, muons);
  edm::Handle<std::vector<pat::Electron> > electrons;
  evt.getByLabel(electrons_, electrons);
  edm::Handle<std::vector<pat::Jet> > looseTrackHighPurBjets;
  evt.getByLabel(looseTrackHighPurBjets_, looseTrackHighPurBjets);
  edm::Handle<std::vector<pat::Jet> > mediumTrackHighPurBjets;
  evt.getByLabel(mediumTrackHighPurBjets_, mediumTrackHighPurBjets);
  edm::Handle<std::vector<pat::Jet> > tightTrackHighPurBjets;
  evt.getByLabel(tightTrackHighPurBjets_, tightTrackHighPurBjets);
  edm::Handle<std::vector<pat::Jet> > looseTrackHighEffBjets;
  evt.getByLabel(looseTrackHighEffBjets_, looseTrackHighEffBjets);
  edm::Handle<std::vector<pat::Jet> > mediumTrackHighEffBjets;
  evt.getByLabel(mediumTrackHighEffBjets_, mediumTrackHighEffBjets);
  edm::Handle<std::vector<pat::Jet> > tightTrackHighEffBjets;
  evt.getByLabel(tightTrackHighEffBjets_, tightTrackHighEffBjets);
  edm::Handle<std::vector<reco::Vertex> > pvSrc;
  evt.getByLabel(pvSrc_, pvSrc);

  double weight=1;
  if(useEvtWgt_)
    {
      //std::cout << "use event weight" << std::endl;
      edm::Handle<double> weightHandle;
      evt.getByLabel(weight_, weightHandle);
      weight=*weightHandle;
    }

  //-------------------------------------------------
  // BJets
  //-------------------------------------------------

  int nbjets[4][5];
  std::vector<double> values[4][10];
  std::vector<double> sortedValues[4][10];
  for(int k=0; k<4; ++k)
    {
      for(int l=0; l < 5; ++l) nbjets[k][l]=0;
      for(int m=0; m < 10; ++m)
	{
	  values[k][m].push_back(-100);
	  sortedValues[k][m].push_back(-100);
      	  values[k][m].push_back(0);
	  sortedValues[k][m].push_back(0);
	}
    }

  int looseBjetsTrackHighPur=0;
  int mediumBjetsTrackHighPur=0;
  int tightBjetsTrackHighPur=0;

  int looseBjetsTrackHighEff=0;
  int mediumBjetsTrackHighEff=0;
  int tightBjetsTrackHighEff=0;

  //std::cout << "Test1" << std::endl;

  for(int i=0; i<(int)jets->size(); ++i)
    {
      // nbjets
      if((*jets)[i].bDiscriminator("trackCountingHighEffBJetTags") > 1.) ++nbjets[0][0];
      if((*jets)[i].bDiscriminator("trackCountingHighEffBJetTags") > 2.) ++nbjets[0][1];
      if((*jets)[i].bDiscriminator("trackCountingHighEffBJetTags") > 3.) ++nbjets[0][2];
      if((*jets)[i].bDiscriminator("trackCountingHighEffBJetTags") > 4.) ++nbjets[0][3];
      if((*jets)[i].bDiscriminator("trackCountingHighEffBJetTags") > 5.) ++nbjets[0][4];
      
      if((*jets)[i].bDiscriminator("trackCountingHighPurBJetTags") > 1.) ++nbjets[1][0];
      if((*jets)[i].bDiscriminator("trackCountingHighPurBJetTags") > 2.) ++nbjets[1][1];
      if((*jets)[i].bDiscriminator("trackCountingHighPurBJetTags") > 3.) ++nbjets[1][2];
      if((*jets)[i].bDiscriminator("trackCountingHighPurBJetTags") > 4.) ++nbjets[1][3];
      if((*jets)[i].bDiscriminator("trackCountingHighPurBJetTags") > 5.) ++nbjets[1][4];
      
      if((*jets)[i].bDiscriminator("simpleSecondaryVertexHighEffBJetTags") > 0) ++nbjets[2][0];
      if((*jets)[i].bDiscriminator("simpleSecondaryVertexHighEffBJetTags") > 1) ++nbjets[2][1];
      if((*jets)[i].bDiscriminator("simpleSecondaryVertexHighEffBJetTags") > 2) ++nbjets[2][2];
      if((*jets)[i].bDiscriminator("simpleSecondaryVertexHighEffBJetTags") > 3) ++nbjets[2][3];
      if((*jets)[i].bDiscriminator("simpleSecondaryVertexHighEffBJetTags") > 4) ++nbjets[2][4];
      
      if((*jets)[i].bDiscriminator("simpleSecondaryVertexHighPurBJetTags") > 0) ++nbjets[3][0];
      if((*jets)[i].bDiscriminator("simpleSecondaryVertexHighPurBJetTags") > 1) ++nbjets[3][1];
      if((*jets)[i].bDiscriminator("simpleSecondaryVertexHighPurBJetTags") > 2) ++nbjets[3][2];
      if((*jets)[i].bDiscriminator("simpleSecondaryVertexHighPurBJetTags") > 3) ++nbjets[3][3];
      if((*jets)[i].bDiscriminator("simpleSecondaryVertexHighPurBJetTags") > 4) ++nbjets[3][4];

      if((*jets)[i].bDiscriminator("trackCountingHighPurBJetTags") > 1.19) ++looseBjetsTrackHighPur;
      if((*jets)[i].bDiscriminator("trackCountingHighPurBJetTags") > 1.93) ++mediumBjetsTrackHighPur;
      if((*jets)[i].bDiscriminator("trackCountingHighPurBJetTags") > 3.41) ++tightBjetsTrackHighPur;

      if((*jets)[i].bDiscriminator("trackCountingHighEffBJetTags") > 1.7) ++looseBjetsTrackHighEff;
      if((*jets)[i].bDiscriminator("trackCountingHighEffBJetTags") > 3.3) ++mediumBjetsTrackHighEff;
      if((*jets)[i].bDiscriminator("trackCountingHighEffBJetTags") > 10.2) ++tightBjetsTrackHighEff;
 
      bdiscTrackHighEff_->Fill((*jets)[i].bDiscriminator("trackCountingHighEffBJetTags"), weight);
      bdiscTrackHighPur_->Fill((*jets)[i].bDiscriminator("trackCountingHighPurBJetTags"), weight);

      if(pvSrc->size()==1)
	{
	  bdiscTrackHighEff1pv_->Fill((*jets)[i].bDiscriminator("trackCountingHighEffBJetTags"), weight);
	  bdiscTrackHighPur1pv_->Fill((*jets)[i].bDiscriminator("trackCountingHighPurBJetTags"), weight);
	}
      if(pvSrc->size()==2 || pvSrc->size()==3)
	{
	  bdiscTrackHighEff2pv_->Fill((*jets)[i].bDiscriminator("trackCountingHighEffBJetTags"), weight);
	  bdiscTrackHighPur2pv_->Fill((*jets)[i].bDiscriminator("trackCountingHighPurBJetTags"), weight);
	}
      if(pvSrc->size()==4 || pvSrc->size()==5 || pvSrc->size()==6)
	{
	  bdiscTrackHighEff3pv_->Fill((*jets)[i].bDiscriminator("trackCountingHighEffBJetTags"), weight);
	  bdiscTrackHighPur3pv_->Fill((*jets)[i].bDiscriminator("trackCountingHighPurBJetTags"), weight);
	}
      if(pvSrc->size()==7 || pvSrc->size()==8 || pvSrc->size()==9 )
	{
	  bdiscTrackHighEff4pv_->Fill((*jets)[i].bDiscriminator("trackCountingHighEffBJetTags"), weight);
	  bdiscTrackHighPur4pv_->Fill((*jets)[i].bDiscriminator("trackCountingHighPurBJetTags"), weight);
	}
      if(pvSrc->size()>=10)
	{
	  bdiscTrackHighEff5pv_->Fill((*jets)[i].bDiscriminator("trackCountingHighEffBJetTags"), weight);
	  bdiscTrackHighPur5pv_->Fill((*jets)[i].bDiscriminator("trackCountingHighPurBJetTags"), weight);
	}

      if(i<10)
	{
	  //std::cout << "Jet " << i << " bdisc:" << (*jets)[i].bDiscriminator("trackCountingHighPurBJetTags") << std::endl;
	  values[0][i][0]=((*jets)[i].bDiscriminator("trackCountingHighEffBJetTags"));
	  values[1][i][0]=((*jets)[i].bDiscriminator("trackCountingHighPurBJetTags"));
	  values[2][i][0]=((*jets)[i].bDiscriminator("simpleSecondaryVertexHighEffBJetTags"));
	  values[3][i][0]=((*jets)[i].bDiscriminator("simpleSecondaryVertexHighPurBJetTags"));

	  values[0][i][1]=((*jets)[i].et());
	  values[1][i][1]=((*jets)[i].et());
	  values[2][i][1]=((*jets)[i].et());
	  values[3][i][1]=((*jets)[i].et());
	}
    }
  //std::cout << "Test2" << std::endl;
  for(int n=0; n<4; ++n)
    {
      for(int o=0; o < 5; ++o) nbjets_[n][o]->Fill(nbjets[n][o]);
    }
  
  nLooseBjetsTrackHighPur_->Fill(looseBjetsTrackHighPur, weight);
  nMediumBjetsTrackHighPur_->Fill(mediumBjetsTrackHighPur, weight);
  nTightBjetsTrackHighPur_->Fill(tightBjetsTrackHighPur, weight);
  nLooseBjetsTrackHighEff_->Fill(looseBjetsTrackHighEff, weight);
  nMediumBjetsTrackHighEff_->Fill(mediumBjetsTrackHighEff, weight);
  nTightBjetsTrackHighEff_->Fill(tightBjetsTrackHighEff, weight);

 if(pvSrc->size()==1)
    {
      nLooseBjetsTrackHighPur1pv_->Fill(looseBjetsTrackHighPur, weight);
      nMediumBjetsTrackHighPur1pv_->Fill(mediumBjetsTrackHighPur, weight);
      nTightBjetsTrackHighPur1pv_->Fill(tightBjetsTrackHighPur, weight);
      nLooseBjetsTrackHighEff1pv_->Fill(looseBjetsTrackHighEff, weight);
      nMediumBjetsTrackHighEff1pv_->Fill(mediumBjetsTrackHighEff, weight);
      nTightBjetsTrackHighEff1pv_->Fill(tightBjetsTrackHighEff, weight);
    }

  if(pvSrc->size()==2 || pvSrc->size()==3)
    {
      nLooseBjetsTrackHighPur2pv_->Fill(looseBjetsTrackHighPur, weight);
      nMediumBjetsTrackHighPur2pv_->Fill(mediumBjetsTrackHighPur, weight);
      nTightBjetsTrackHighPur2pv_->Fill(tightBjetsTrackHighPur, weight);
      nLooseBjetsTrackHighEff2pv_->Fill(looseBjetsTrackHighEff, weight);
      nMediumBjetsTrackHighEff2pv_->Fill(mediumBjetsTrackHighEff, weight);
      nTightBjetsTrackHighEff2pv_->Fill(tightBjetsTrackHighEff, weight);
    }

  if(pvSrc->size()==4 || pvSrc->size()==5 || pvSrc->size()==6)
    {
      nLooseBjetsTrackHighPur3pv_->Fill(looseBjetsTrackHighPur, weight);
      nMediumBjetsTrackHighPur3pv_->Fill(mediumBjetsTrackHighPur, weight);
      nTightBjetsTrackHighPur3pv_->Fill(tightBjetsTrackHighPur, weight);
      nLooseBjetsTrackHighEff3pv_->Fill(looseBjetsTrackHighEff, weight);
      nMediumBjetsTrackHighEff3pv_->Fill(mediumBjetsTrackHighEff, weight);
      nTightBjetsTrackHighEff3pv_->Fill(tightBjetsTrackHighEff, weight);
    }
  
  if(pvSrc->size()==7 || pvSrc->size()==8 || pvSrc->size()==9)
    {
      nLooseBjetsTrackHighPur4pv_->Fill(looseBjetsTrackHighPur, weight);
      nMediumBjetsTrackHighPur4pv_->Fill(mediumBjetsTrackHighPur, weight);
      nTightBjetsTrackHighPur4pv_->Fill(tightBjetsTrackHighPur, weight);
      nLooseBjetsTrackHighEff4pv_->Fill(looseBjetsTrackHighEff, weight);
      nMediumBjetsTrackHighEff4pv_->Fill(mediumBjetsTrackHighEff, weight);
      nTightBjetsTrackHighEff4pv_->Fill(tightBjetsTrackHighEff, weight);
    }

  if(pvSrc->size()>=10)
    {
      nLooseBjetsTrackHighPur5pv_->Fill(looseBjetsTrackHighPur, weight);
      nMediumBjetsTrackHighPur5pv_->Fill(mediumBjetsTrackHighPur, weight);
      nTightBjetsTrackHighPur5pv_->Fill(tightBjetsTrackHighPur, weight);
      nLooseBjetsTrackHighEff5pv_->Fill(looseBjetsTrackHighEff, weight);
      nMediumBjetsTrackHighEff5pv_->Fill(mediumBjetsTrackHighEff, weight);
      nTightBjetsTrackHighEff5pv_->Fill(tightBjetsTrackHighEff, weight);
    }
  //------------------------------------------------------------------------------
  //  for events containing exactly two ...
  //------------------------------------------------------------------------------
  

  //std::cout << "Test0" << std::endl;
  // ... looseTrackHighEffBjets
  if(looseTrackHighEffBjets->size()==2)
    {
      reco::Particle::LorentzVector bjet1=(*looseTrackHighEffBjets)[0].p4();
      reco::Particle::LorentzVector bjet2=(*looseTrackHighEffBjets)[1].p4();
      double mbb=0;
      double dPhi=abs(deltaPhi((*looseTrackHighEffBjets)[0].phi(),(*looseTrackHighEffBjets)[1].phi()));
      mbb=sqrt(bjet1.Dot(bjet2));
      mbb_[0]->Fill(mbb);
      angleb1b2_[0]->Fill(abs(angle(bjet1,bjet2)), weight);
      deltaPhi_[0]->Fill(dPhi, weight);
      Bjet1_Et_[0]->Fill((*looseTrackHighEffBjets)[0].et(), weight);
      Bjet2_Et_[0]->Fill((*looseTrackHighEffBjets)[1].et(), weight);
      HT_2Bjets_[0]->Fill((*looseTrackHighEffBjets)[0].et()+(*looseTrackHighEffBjets)[1].et(), weight);
      for(int jdx=0; jdx<(int)jets->size(); ++jdx)
	{  
	  if((*jets)[jdx].bDiscriminator("trackCountingHighEffBJetTags") <= 1.7)
	    {
	      Jet1_Et_2Bjets_[0]->Fill((*jets)[jdx].et(), weight);
	      HT_2Bjets_1LightJet_[0]->Fill((*looseTrackHighEffBjets)[0].et()+(*looseTrackHighEffBjets)[1].et()+(*jets)[jdx].et(), weight);
	      break;
	    }
	}
    }
  //std::cout << "Test1" << std::endl;
  // ... mediumTrackHighEffBjets
  if(mediumTrackHighEffBjets->size()==2)
    {
      reco::Particle::LorentzVector bjet1=(*mediumTrackHighEffBjets)[0].p4();
      reco::Particle::LorentzVector bjet2=(*mediumTrackHighEffBjets)[1].p4();
      double mbb=0;
      double dPhi=abs(deltaPhi((*mediumTrackHighEffBjets)[0].phi(),(*mediumTrackHighEffBjets)[1].phi()));
      mbb=sqrt(bjet1.Dot(bjet2));
      mbb_[1]->Fill(mbb, weight);
      angleb1b2_[1]->Fill(abs(angle(bjet1,bjet2)), weight);
      deltaPhi_[1]->Fill(dPhi, weight);
      Bjet1_Et_[1]->Fill((*mediumTrackHighEffBjets)[0].et(), weight);
      Bjet2_Et_[1]->Fill((*mediumTrackHighEffBjets)[1].et(), weight);
      HT_2Bjets_[1]->Fill((*mediumTrackHighEffBjets)[0].et()+(*mediumTrackHighEffBjets)[1].et(), weight);
      for(int jdx=0; jdx<(int)jets->size(); ++jdx)
	{  
	  if((*jets)[jdx].bDiscriminator("trackCountingHighEffBJetTags") <= 3.3)
	    {
	      Jet1_Et_2Bjets_[1]->Fill((*jets)[jdx].et(), weight);
	      HT_2Bjets_1LightJet_[1]->Fill((*mediumTrackHighEffBjets)[0].et()+(*mediumTrackHighEffBjets)[1].et()+(*jets)[jdx].et(), weight);
	      break;
	    }
	}  
    }

  //std::cout << "Test2" << std::endl;
  // ... tightTrackHighEffBjets
  if(tightTrackHighEffBjets->size()==2)
    {
      reco::Particle::LorentzVector bjet1=(*tightTrackHighEffBjets)[0].p4();
      reco::Particle::LorentzVector bjet2=(*tightTrackHighEffBjets)[1].p4();
      double mbb=0;
      double dPhi=abs(deltaPhi((*tightTrackHighEffBjets)[0].phi(),(*tightTrackHighEffBjets)[1].phi()));
      mbb=sqrt(bjet1.Dot(bjet2));
      mbb_[2]->Fill(mbb, weight);
      angleb1b2_[2]->Fill(abs(angle(bjet1,bjet2)), weight);
      deltaPhi_[2]->Fill(dPhi, weight);
      Bjet1_Et_[2]->Fill((*tightTrackHighEffBjets)[0].et(), weight);
      Bjet2_Et_[2]->Fill((*tightTrackHighEffBjets)[1].et(), weight);
      HT_2Bjets_[2]->Fill((*tightTrackHighEffBjets)[0].et()+(*tightTrackHighEffBjets)[1].et(), weight);
      for(int jdx=0; jdx<(int)jets->size(); ++jdx)
	{  
	  if((*jets)[jdx].bDiscriminator("trackCountingHighEffBJetTags") <= 10.2)
	    {
	      Jet1_Et_2Bjets_[2]->Fill((*jets)[jdx].et(), weight);
	      HT_2Bjets_1LightJet_[2]->Fill((*tightTrackHighEffBjets)[0].et()+(*tightTrackHighEffBjets)[1].et()+(*jets)[jdx].et(), weight);
	      break;
	    }
	}  
    }
  //std::cout << "Test3" << std::endl;
  // ... looseTrackHighPurBjets
  if(looseTrackHighPurBjets->size()==2)
    {
      reco::Particle::LorentzVector bjet1=(*looseTrackHighPurBjets)[0].p4();
      reco::Particle::LorentzVector bjet2=(*looseTrackHighPurBjets)[1].p4();
      double mbb=0;
      double dPhi=abs(deltaPhi((*looseTrackHighPurBjets)[0].phi(),(*looseTrackHighPurBjets)[1].phi()));
      mbb=sqrt(bjet1.Dot(bjet2));
      mbb_[3]->Fill(mbb, weight);
      angleb1b2_[3]->Fill(abs(angle(bjet1,bjet2)), weight);
      deltaPhi_[3]->Fill(dPhi, weight);
      Bjet1_Et_[3]->Fill((*looseTrackHighPurBjets)[0].et(), weight);
      Bjet2_Et_[3]->Fill((*looseTrackHighPurBjets)[1].et(), weight);
      HT_2Bjets_[3]->Fill((*looseTrackHighPurBjets)[0].et()+(*looseTrackHighPurBjets)[1].et(), weight);
      for(int jdx=0; jdx<(int)jets->size(); ++jdx)
	{  
	  if((*jets)[jdx].bDiscriminator("trackCountingHighPurBJetTags") <= 1.19)
	    {
	      Jet1_Et_2Bjets_[3]->Fill((*jets)[jdx].et(), weight);
	      HT_2Bjets_1LightJet_[3]->Fill((*looseTrackHighPurBjets)[0].et()+(*looseTrackHighPurBjets)[1].et()+(*jets)[jdx].et(), weight);
	      break;
	    }
	}  
    }
  //std::cout << "Test4" << std::endl;
  // ... mediumTrackHighPurBjets
  if(mediumTrackHighPurBjets->size()==2)
    {
      reco::Particle::LorentzVector bjet1=(*mediumTrackHighPurBjets)[0].p4();
      reco::Particle::LorentzVector bjet2=(*mediumTrackHighPurBjets)[1].p4();
      double mbb=0;
      double dPhi=abs(deltaPhi((*mediumTrackHighPurBjets)[0].phi(),(*mediumTrackHighPurBjets)[1].phi()));
      mbb=sqrt(bjet1.Dot(bjet2));
      mbb_[4]->Fill(mbb, weight);
      angleb1b2_[4]->Fill(abs(angle(bjet1,bjet2)), weight);
      deltaPhi_[4]->Fill(dPhi, weight);
      Bjet1_Et_[4]->Fill((*mediumTrackHighPurBjets)[0].et(), weight);
      Bjet2_Et_[4]->Fill((*mediumTrackHighPurBjets)[1].et(), weight);
      HT_2Bjets_[4]->Fill((*mediumTrackHighPurBjets)[0].et()+(*mediumTrackHighPurBjets)[1].et(), weight);
      for(int jdx=0; jdx<(int)jets->size(); ++jdx)
	{  
	  if((*jets)[jdx].bDiscriminator("trackCountingHighPurBJetTags") <= 1.93)
	    {
	      Jet1_Et_2Bjets_[4]->Fill((*jets)[jdx].et(), weight);
	      HT_2Bjets_1LightJet_[4]->Fill((*mediumTrackHighPurBjets)[0].et()+(*mediumTrackHighPurBjets)[1].et()+(*jets)[jdx].et(), weight);
	      break;
	    }
	}  
    }
  //std::cout << "Test5" << std::endl;
  // ... tightTrackHighPurBjets
  if(tightTrackHighPurBjets->size()==2)
    {
      reco::Particle::LorentzVector bjet1=(*tightTrackHighPurBjets)[0].p4();
      reco::Particle::LorentzVector bjet2=(*tightTrackHighPurBjets)[1].p4();
      double mbb=0;
      double dPhi=abs(deltaPhi((*tightTrackHighPurBjets)[0].phi(),(*tightTrackHighPurBjets)[1].phi()));
      mbb=sqrt(bjet1.Dot(bjet2));
      mbb_[5]->Fill(mbb, weight);
      angleb1b2_[5]->Fill(abs(angle(bjet1,bjet2)), weight);
      deltaPhi_[5]->Fill(dPhi, weight);
      Bjet1_Et_[5]->Fill((*tightTrackHighPurBjets)[0].et(), weight);
      Bjet2_Et_[5]->Fill((*tightTrackHighPurBjets)[1].et(), weight);
      HT_2Bjets_[5]->Fill((*tightTrackHighPurBjets)[0].et()+(*tightTrackHighPurBjets)[1].et(), weight);
      for(int jdx=0; jdx<(int)jets->size(); ++jdx)
	{  
	  if((*jets)[jdx].bDiscriminator("trackCountingHighPurBJetTags") <= 3.41)
	    {
	      Jet1_Et_2Bjets_[5]->Fill((*jets)[jdx].et(), weight);
	      HT_2Bjets_1LightJet_[5]->Fill((*tightTrackHighPurBjets)[0].et()+(*tightTrackHighPurBjets)[1].et()+(*jets)[jdx].et(), weight);
	      break;
	    }
	}  
    }
  //std::cout << "Test6" << std::endl;
  for(int p=0; p<4; ++p)
    {
      for(int q=0; q < 10; ++q)
	{
	  if(values[p][q][0]>sortedValues[p][0][0])
	    {
	      sortedValues[p][5]=sortedValues[p][4];
	      sortedValues[p][4]=sortedValues[p][3];
	      sortedValues[p][3]=sortedValues[p][2];
	      sortedValues[p][2]=sortedValues[p][1];
	      sortedValues[p][1]=sortedValues[p][0];
	      sortedValues[p][0]=values[p][q];
	    }
	  else if(values[p][q][0]>sortedValues[p][1][0])
	    {
	      sortedValues[p][5]=sortedValues[p][4];
	      sortedValues[p][4]=sortedValues[p][3];
	      sortedValues[p][3]=sortedValues[p][2];
	      sortedValues[p][2]=sortedValues[p][1];
	      sortedValues[p][1]=values[p][q];
	    }
	  else if(values[p][q][0]>sortedValues[p][2][0])
	    {
	      sortedValues[p][5]=sortedValues[p][4];
	      sortedValues[p][4]=sortedValues[p][3];
	      sortedValues[p][3]=sortedValues[p][2];
	      sortedValues[p][2]=values[p][q];
	    }
	  else if(values[p][q][0]>sortedValues[p][3][0])
	    {
	      sortedValues[p][5]=sortedValues[p][4];
	      sortedValues[p][4]=sortedValues[p][3];
	      sortedValues[p][3]=values[p][q];
	    }
	  else if(values[p][q][0]>sortedValues[p][4][0])
	    {
	      sortedValues[p][5]=sortedValues[p][4];
	      sortedValues[p][4]=values[p][q];
	    }
	  else if(values[p][q][0]>sortedValues[p][5][0])
	    {
	      sortedValues[p][5]=values[p][q];
	    }	
	}
    }
  
  //std::cout << "jets->size(): " << jets->size() << std::endl;

  // Comment in for debugging

//   std::cout << "===============" << std::endl;
//   std::cout << "Values:" << std::endl;
//   std::cout << "---------------" << std::endl;
//   std::cout << values[0][0][0] << std::endl;
//   std::cout << values[0][1][0] << std::endl;
//   std::cout << values[0][2][0] << std::endl;
//   std::cout << values[0][3][0] << std::endl;
//   std::cout << values[0][4][0] << std::endl;
//   std::cout << values[0][5][0] << std::endl;
//   std::cout << "SortedValues:" << std::endl;
//   std::cout << "---------------" << std::endl;
//   std::cout << sortedValues[0][0][0] << std::endl;
//   std::cout << sortedValues[0][1][0] << std::endl;
//   std::cout << sortedValues[0][2][0] << std::endl;
//   std::cout << sortedValues[0][3][0] << std::endl;
//   std::cout << sortedValues[0][4][0] << std::endl;
//   std::cout << sortedValues[0][5][0] << std::endl;
//   std::cout << "===============" << std::endl;
  
//       std::cout << "Values:" << std::endl;
//       std::cout << "---------------" << std::endl;
//       std::cout << values[0][0][1] << std::endl;
//       std::cout << values[0][1][1] << std::endl;
//       std::cout << values[0][2][1] << std::endl;
//       std::cout << values[0][3][1] << std::endl;
//       std::cout << values[0][4][1] << std::endl;
//       std::cout << values[0][5][1] << std::endl;
//       std::cout << "SortedValues:" << std::endl;
//       std::cout << "---------------" << std::endl;
//       std::cout << sortedValues[0][0][1] << std::endl;
//       std::cout << sortedValues[0][1][1] << std::endl;
//       std::cout << sortedValues[0][2][1] << std::endl;
//       std::cout << sortedValues[0][3][1] << std::endl;
//       std::cout << sortedValues[0][4][1] << std::endl;
//       std::cout << sortedValues[0][5][1] << std::endl;
//       std::cout << "===============" << std::endl;

  for(int r=0; r<4; ++r)
    {
      for(int s=0; s<6; ++s)
	{
	  if(sortedValues[r][s][0] > -100.)
	    {
	      //if(r==0) std::cout << "sortedValues[r][s][0]" << sortedValues[r][s][0] << std::endl;
	      Bdisc_[r][s]->Fill(sortedValues[r][s][0], weight);
	      BtagEt_[r][s]->Fill(sortedValues[r][s][1], weight);
	    }
	}
    }
}

void BjetsAnalyzer::beginJob()
{  
} 

void BjetsAnalyzer::endJob()
{
}
