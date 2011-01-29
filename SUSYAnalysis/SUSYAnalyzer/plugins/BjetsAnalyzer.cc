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
  bjets_        (cfg.getParameter<edm::InputTag>("bjets"))
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
	  sprintf(histname,"bdisc_%i_%i",i2, j2);
	  bdisc_[i2][j2]=fs->make<TH1F>(histname,"bDiscriminator",160, -20., 20.);
	}
    }
  for(int i3=2; i3<4; ++i3)
    {
      for(int j3=0; j3 < 6; ++j3)
	{
	  char histname3[20];
	  sprintf(histname3,"bdisc_%i_%i",i3, j3);
	  bdisc_[i3][j3]=fs->make<TH1F>(histname3,"bDiscriminator",22 , -1, 10.);
	}
    }
  for(int i4=0; i4<4; ++i4)
    {
      for(int j4=0; j4 < 6; ++j4)
	{
	  char histname4[20];
	  sprintf(histname4,"EtBtag_%i_%i",i4, j4);
	  EtBtag_[i4][j4]=fs->make<TH1F>(histname4,"Et Btag",30 , 0., 900.);
	}
    }
  nLooseBjetsTrackHighPur_=fs->make<TH1F>("nLooseBjetsTrackHighPur","# loose bjets TrackHighPur",10 , -0.5, 9.5);
  nMediumBjetsTrackHighPur_=fs->make<TH1F>("nMediumBjetsTrackHighPur","# medium bjets TrackHighPur",10 , -0.5, 9.5);
  nTightBjetsTrackHighPur_=fs->make<TH1F>("nTightBjetsTrackHighPur","# tight bjets TrackHighPur",10 , -0.5, 9.5);

  nLooseBjetsTrackHighEff_=fs->make<TH1F>("nLooseBjetsTrackHighEff","# loose bjets TrackHighEff",10 , -0.5, 9.5);
  nMediumBjetsTrackHighEff_=fs->make<TH1F>("nMediumBjetsTrackHighEff","# medium bjets TrackHighEff",10 , -0.5, 9.5);
  nTightBjetsTrackHighEff_=fs->make<TH1F>("nTightBjetsTrackHighEff","# tight bjets TrackHighEff",10 , -0.5, 9.5);
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
  edm::Handle<std::vector<pat::Jet> > bjets;
  evt.getByLabel(bjets_, bjets);

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
      if((*jets)[i].bDiscriminator("trackCountingHighEffBJetTags") > 10.21) ++tightBjetsTrackHighEff;

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
  
  for(int n=0; n<4; ++n)
    {
      for(int o=0; o < 5; ++o) nbjets_[n][o]->Fill(nbjets[n][o]);
    }
  
  nLooseBjetsTrackHighPur_->Fill(looseBjetsTrackHighPur);
  nMediumBjetsTrackHighPur_->Fill(looseBjetsTrackHighPur);
  nTightBjetsTrackHighPur_->Fill(looseBjetsTrackHighPur);

  nLooseBjetsTrackHighEff_->Fill(looseBjetsTrackHighEff);
  nMediumBjetsTrackHighEff_->Fill(looseBjetsTrackHighEff);
  nTightBjetsTrackHighEff_->Fill(looseBjetsTrackHighEff);

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
	      bdisc_[r][s]->Fill(sortedValues[r][s][0]);
	      EtBtag_[r][s]->Fill(sortedValues[r][s][1]);
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
