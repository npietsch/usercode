#include "FWCore/Utilities/interface/EDMException.h"
#include "Btagging/BtagWeightProducer/plugins/BtagEventWeight.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/Common/interface/View.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"


BtagEventWeight::BtagEventWeight(const edm::ParameterSet& cfg):
  jets_           ( cfg.getParameter<edm::InputTag> ( "jets"   ) ),
  bTagAlgo_       ( cfg.getParameter<std::string>   ("bTagAlgo") ),
  sysVar_         ( cfg.getParameter<std::string>   ("sysVar"  ) ),
  verbose_        ( cfg.getParameter<int>           ("verbose" ) ),
  filename_       ( cfg.getParameter<std::string>   ("filename") ),
  rootDir_        ( cfg.getParameter<std::string>   ("rootDir" ) ),
  shift_          ( cfg.getParameter<double>        ("shift"   ) ),
  scaleJetEffSF_  ( cfg.getParameter<bool>          ("scaleJetEffSF") )
{

  produces< std::vector<double> > ("RA4bJetWeights");
  produces< std::vector<double> > ("RA4bSFJetWeights");
  produces< std::vector<double> > ("RA4bEventWeights");
  produces< std::vector<double> > ("RA4bSFEventWeights");
  produces< std::vector<double> > ("effBTagEventGrid");

  produces< std::vector<std::vector<double> > > ("RA4bJetWeightsGrid");

  // set the edges of the last histo bin
  maxPt_ = 500.;
  maxEta_= 3.;
  
  // laod TFile Service
  edm::Service<TFileService> fs;
  if( !fs ){
    throw edm::Exception( edm::errors::Configuration,
			  "TFile Service is not registered in cfg file" );
  }
 
  std::cout << "bTagAlgo_: " << bTagAlgo_ << std::endl;

  /// getting efficiency histos from input files
  if(filename_!=""){
    file_ = new TFile((TString)filename_);
    dir_ = (TString)rootDir_;

    std::cout << "filename_ "  << filename_ << std::endl;
    std::cout << "dir_: " << dir_  <<std::endl;

    if(!(file_->IsZombie())){
      if(verbose_>=1) std::cout<<filename_<<" opened"<<std::endl;
      effHists_["NumBJetsPtEta"]       = (TH2F*) file_->Get("bTagEff"+dir_+"/NumBJetsPtEta")->Clone();
      effHists_["NumBJetsTaggedPtEta"] = (TH2F*) file_->Get("bTagEff"+dir_+"/NumBJetsTaggedPtEta")->Clone();
      effHists_["EffBJetsTaggedPtEta"] = (TH2F*) file_->Get("bTagEff"+dir_+"/EffBJetsTaggedPtEta")->Clone();
      effHists_["NumCJetsPtEta"]       = (TH2F*) file_->Get("bTagEff"+dir_+"/NumCJetsPtEta")->Clone();
      effHists_["NumCJetsTaggedPtEta"] = (TH2F*) file_->Get("bTagEff"+dir_+"/NumCJetsTaggedPtEta")->Clone();
      effHists_["EffCJetsTaggedPtEta"] = (TH2F*) file_->Get("bTagEff"+dir_+"/EffCJetsTaggedPtEta")->Clone();
      effHists_["NumLJetsPtEta"]       = (TH2F*) file_->Get("bTagEff"+dir_+"/NumLJetsPtEta")->Clone();
      effHists_["NumLJetsTaggedPtEta"] = (TH2F*) file_->Get("bTagEff"+dir_+"/NumLJetsTaggedPtEta")->Clone();
      effHists_["EffLJetsTaggedPtEta"] = (TH2F*) file_->Get("bTagEff"+dir_+"/EffLJetsTaggedPtEta")->Clone();
      
      /// re-calculation of b tag efficiencies as input might be corrupted due to hadd
      if(effHists_.count("NumBJetsPtEta") && effHists_.count("NumBJetsTaggedPtEta") && effHists_.count("EffBJetsTaggedPtEta") &&
	 effHists_.count("NumCJetsPtEta") && effHists_.count("NumCJetsTaggedPtEta") && effHists_.count("EffCJetsTaggedPtEta") &&
	 effHists_.count("NumBJetsPtEta") && effHists_.count("NumBJetsTaggedPtEta") && effHists_.count("EffBJetsTaggedPtEta"))
	{
	
	  effHists_.find("EffBJetsTaggedPtEta")->second->Reset();
	  effHists_.find("EffCJetsTaggedPtEta")->second->Reset();
	  effHists_.find("EffLJetsTaggedPtEta")->second->Reset();
	  
	  effHists_.find("EffBJetsTaggedPtEta")->second->Divide(effHists_.find("NumBJetsTaggedPtEta")->second, 
								effHists_.find("NumBJetsPtEta")->second,1,1,"B");
	  effHists_.find("EffCJetsTaggedPtEta")->second->Divide(effHists_.find("NumCJetsTaggedPtEta")->second, 
								effHists_.find("NumCJetsPtEta")->second,1,1,"B");
	  effHists_.find("EffLJetsTaggedPtEta")->second->Divide(effHists_.find("NumLJetsTaggedPtEta")->second, 
								effHists_.find("NumLJetsPtEta")->second,1,1,"B");
	}
      else{
	std::cout<<"Eff.Histos not found!!!!! Efficiencies cannot be taken from this file!!! Default taken!"<<std::endl;
	filename_ = "";
      }
    }
    else{
      std::cout<<filename_<<" not found!!!!! Efficiencies cannot be taken from this file!!! Default taken!"<<std::endl;
      filename_ = "";
    }
  }
  
  /// load map from database
  measureMap_["BTAGBEFF"]=PerformanceResult::BTAGBEFF;
  measureMap_["BTAGBERR"]=PerformanceResult::BTAGBERR;
  measureMap_["BTAGCEFF"]=PerformanceResult::BTAGCEFF;
  measureMap_["BTAGCERR"]=PerformanceResult::BTAGCERR;
  measureMap_["BTAGLEFF"]=PerformanceResult::BTAGLEFF;
  measureMap_["BTAGLERR"]=PerformanceResult::BTAGLERR;

  measureMap_["BTAGNBEFF"]=PerformanceResult::BTAGNBEFF;
  measureMap_["BTAGNBERR"]=PerformanceResult::BTAGNBERR;

  measureMap_["BTAGBEFFCORR"]=PerformanceResult::BTAGBEFFCORR;
  measureMap_["BTAGBERRCORR"]=PerformanceResult::BTAGBERRCORR;
  measureMap_["BTAGCEFFCORR"]=PerformanceResult::BTAGCEFFCORR;
  measureMap_["BTAGCERRCORR"]=PerformanceResult::BTAGCERRCORR;
  measureMap_["BTAGLEFFCORR"]=PerformanceResult::BTAGLEFFCORR;
  measureMap_["BTAGLERRCORR"]=PerformanceResult::BTAGLERRCORR;
  
  measureMap_["BTAGNBEFFCORR"]=PerformanceResult::BTAGNBEFFCORR;
  measureMap_["BTAGNBERRCORR"]=PerformanceResult::BTAGNBERRCORR;
}

BtagEventWeight::~BtagEventWeight()
{
  if(filename_!="") {if(!(file_->IsZombie())) file_->Close();}
}

void
BtagEventWeight::produce(edm::Event& evt, const edm::EventSetup& setup)
{  
  //Setup measurement from database
  setup.get<BTagPerformanceRecord>().get( "BTAG"+bTagAlgo_, perfHBTag);
  setup.get<BTagPerformanceRecord>().get( "MISTAG"+bTagAlgo_, perfHMisTag);
  
  edm::Handle<edm::View< pat::Jet > > jets;
  evt.getByLabel(jets_, jets);

  double pt, eta;
  std::vector<double> BEffies(0) , BEffies_scaled(0);
  std::vector<double> oneMinusBEffies(0) , oneMinusBEffies_scaled(0);
  std::vector<double> oneMinusBMistags(0), oneMinusBMistags_scaled(0);
  
  for(edm::View<pat::Jet>::const_iterator jet = jets->begin();jet != jets->end(); ++jet)
    {
      pt  = jet->pt();
      eta = std::abs(jet->eta());
      if(jet->partonFlavour() == 5 || jet->partonFlavour() == -5)
	{	
	  //std::cout << "effBTag(pt, eta): " << (effBTag (pt, eta)) << std::endl;
	  //std::cout << effBTag(pt, eta)*effBTagSF(pt, eta) << std::endl;
	  //if(pt>=240)
	  //{
	  //  std::cout << "pt, eta: " << pt << ", "<< eta << std::endl;
	  //  std::cout << "effBTagSF(pt, eta): " << (effBTagSF(pt, eta)) << std::endl;
	  //}
	  BEffies.push_back(effBTag(pt, eta));
	  BEffies_scaled.push_back(effBTag(pt, eta)*(effBTagSF(pt, eta)+shift_) );
	  
	  oneMinusBEffies.push_back(1.- effBTag(pt, eta));
	  oneMinusBEffies_scaled.push_back(1.- effBTag(pt, eta) * (effBTagSF(pt, eta)+shift_) );
	}
      
      else if(jet->partonFlavour() == 4 || jet->partonFlavour() == -4)
	{
	  //std::cout << "effBTagCjet(pt, eta): " << (effBTagCjet (pt, eta)) << std::endl;
	  //std::cout << effBTagCjet(pt, eta)*effBTagSF(pt, eta) << std::endl;
	  
	  BEffies.push_back(effBTagCjet(pt, eta));
	  BEffies_scaled.push_back(effBTagCjet(pt, eta)*(effBTagSF(pt, eta)+shift_) );
	  
	  oneMinusBMistags.push_back(1.- effBTagCjet(pt, eta));
	  oneMinusBMistags_scaled.push_back(1.-effBTagCjet(pt, eta)*(effBTagSF(pt, eta)+shift_) );
	}
      
      else
	{
	  //std::cout << "effMisTag(pt, eta): " << (effMisTag (pt, eta)) << std::endl;
	  //std::cout << effMisTag(pt, eta)*effMisTagSF(pt, eta) << std::endl;
	  //if(pt>=300)
	  //{
	  //  std::cout << "pt, eta: " << pt << ", "<< eta << std::endl;
	  //  std::cout << "effMisTagSF(pt, eta): " << (effMisTagSF (pt, eta)) << std::endl;
	  //}
	  
	  BEffies.push_back(effMisTag(pt, eta));
	  BEffies_scaled.push_back(effMisTag(pt, eta)*effMisTagSF(pt, eta));
	  
	  oneMinusBMistags               .push_back(1.- effMisTag(pt, eta));
	  oneMinusBMistags_scaled        .push_back(1.-(effMisTag(pt, eta) * effMisTagSF(pt, eta)));
	}
    }

  // collection jet weights
  std::vector<double> jetWeights = BEffies; 
  std::auto_ptr<std::vector<double> > RA4bJetWeights( new std::vector<double> );
  *RA4bJetWeights = jetWeights; 
  evt.put(RA4bJetWeights,"RA4bJetWeights");

  // collection jet weights scale factors applied
  std::vector<double> jetWeightsSF = BEffies_scaled; 
  std::auto_ptr<std::vector<double> > RA4bSFJetWeights( new std::vector<double> );
  *RA4bSFJetWeights = jetWeightsSF; 
  evt.put(RA4bSFJetWeights,"RA4bSFJetWeights");

  // collection  event weights
  std::vector<double> eventWeights = effBTagEvent0123(oneMinusBEffies, oneMinusBMistags, 1, 1);
  std::auto_ptr<std::vector<double> > RA4bEventWeights( new std::vector<double> );
  *RA4bEventWeights = eventWeights; 
  evt.put(RA4bEventWeights,"RA4bEventWeights");

  // collection of event weights with scale factors applied
  std::vector<double> eventWeightsSF = effBTagEvent0123(oneMinusBEffies_scaled, oneMinusBMistags_scaled, 1, 1);
  std::auto_ptr<std::vector<double> > RA4bSFEventWeights( new std::vector<double> );
  *RA4bSFEventWeights = eventWeightsSF; 
  evt.put(RA4bSFEventWeights,"RA4bSFEventWeights");


  //=======================================================================================
  //=================================== BAUSTELLE =========================================
  //=======================================================================================

  if(scaleJetEffSF_==true)
    {
      std::vector<std::vector<double> > BtagEffSFShiftGrid(0);
      
      for(int sdx=-10; sdx <= 10 ; ++sdx)
	{
	  double SFShift=sdx*0.05;
	  std::vector<double> BtagEffSFShiftVec(0);
	  
	  for(edm::View<pat::Jet>::const_iterator jet = jets->begin();jet != jets->end(); ++jet)
	    {
	      pt  = jet->pt();
	      eta = std::abs(jet->eta());
	      
	      if(jet->partonFlavour() == 5 || jet->partonFlavour() == -5)
		{
		  //std::cout << "effBTag(pt, eta): " << effBTag(pt, eta) << std::endl;
		  //std::cout << "effBTagSF(pt, eta): " << effBTagSF(pt, eta) << std::endl;
		  //std::cout << "effBTagSF(pt, eta)+SFShift: " << (effBTagSF(pt, eta)+SFShift) << std::endl;
		  //std::cout << "-------------------------------------------" << std::endl;
		  //std::cout << "effBTag(pt, eta)*(effBTagSF(pt, eta)+SFShift): " << effBTag(pt, eta)*(effBTagSF(pt, eta)+SFShift) << std::endl;
		  //std::cout << "-------------------------------------------" << std::endl;

		  BtagEffSFShiftVec.push_back(effBTag(pt, eta)*(effBTagSF(pt, eta)+SFShift) );
		}
	      else if(jet->partonFlavour() == 4 || jet->partonFlavour() == -4)
		{
		  BtagEffSFShiftVec.push_back(effBTagCjet(pt, eta)*(effBTagSF(pt, eta)+SFShift) );
		}
	      else
		{
		  BtagEffSFShiftVec.push_back(effMisTag(pt, eta)*effMisTagSF(pt, eta));
		}
	    }
	  BtagEffSFShiftGrid.push_back(BtagEffSFShiftVec);
	}
      
      // grid of jet weights with scale factors applied
      std::vector<std::vector<double> > testSF = BtagEffSFShiftGrid;
      std::auto_ptr<std::vector<std::vector<double> > >  RA4bJetWeightsGrid( new std::vector<std::vector<double> >);
      *RA4bJetWeightsGrid =  testSF; 
      evt.put(RA4bJetWeightsGrid,"RA4bJetWeightsGrid");
    }

  //=======================================================================================
  //=================================== BAUSTELLE =========================================
  //=======================================================================================


  // systematic study on the influence of different eff and mis 
  double points[]={0.8, 0.9, 0.95, 1, 1.05, 1.1, 1.2};
  unsigned N=sizeof(points)/sizeof(double);
  std::auto_ptr< std::vector<double>  >effBTagEventGrid( new std::vector<double>  );

  unsigned M=0;
  for(unsigned i=0;i<N;i++) for(unsigned j=0;j<N;j++){
  	std::vector<double> weights = effBTagEvent0123(oneMinusBEffies, oneMinusBMistags, points[i], points[j]) ;
  	M=weights.size();
  	for(unsigned k=0;k<M;k++) effBTagEventGrid->push_back( weights[k] );
  }
  if(verbose_>=2)
    {
      for(unsigned i=0;i<N;i++)
	for(unsigned j=0;j<N;j++){
	  std::cout<<"(fac_eff="<<points[i]<<", fac_mis="<<points[j]<<") : ";
	  for(unsigned k=0;k<M;k++)
	    std::cout<<(*effBTagEventGrid)[k+j*M+i*N*M]<<" ";
	  std::cout<<std::endl;
	}
    }
  evt.put( effBTagEventGrid ,"effBTagEventGrid");
}

//--------------------------------------------------------------------------

// Default Eff. and SF values taken from PAS BTV-11-001 (pTrel method),
// or from user-defined histo as a function of pt (in the future also eta?).
// In the future take SF directly from file provided by BTV.

// b tag eff. from MC as a function of jet pt, eta
double BtagEventWeight::effBTag(double jetPt, double jetEta)
{
  double result = -1111.;
  // if histo file exists, take value from there; else return a default value
  if(filename_!="") {
    TH2F* his = effHists_.find("EffBJetsTaggedPtEta")->second;
    if(jetPt >= maxPt_)       result = his->GetBinContent(his->FindBin(maxPt_-0.1, jetEta));
    else if(jetEta >= maxEta_)result = his->GetBinContent(his->FindBin(jetPt, maxEta_-0.01));
    else                      result = his->GetBinContent( his->FindBin(jetPt, jetEta) );
  }
  else if(bTagAlgo_ == "SSVHEM") { result = 0.564/0.854;}
  if(verbose_>=2) std::cout<< "effBTag= "<<result<<std::endl;
  
  return result;
}

// b tag eff. SF as a function of jet pt, eta
double BtagEventWeight::effBTagSF(double jetPt, double jetEta)
{
  double result = -1111., error = -1111.;
  const BtagPerformance & perf = *(perfHBTag.product());
    BinningPointByMap measurePoint;
    if(jetPt>=240) jetPt=200;
    measurePoint.insert(BinningVariables::JetEt, jetPt);
    measurePoint.insert(BinningVariables::JetAbsEta, jetEta);
    if(perf.isResultOk( measureMap_[ "BTAGBEFFCORR" ], measurePoint))
         result = perf.getResult( measureMap_[ "BTAGBEFFCORR" ], measurePoint);
    else result = 1.;
    if(perf.isResultOk( measureMap_[ "BTAGBERRCORR" ], measurePoint))
         error = perf.getResult( measureMap_[ "BTAGBERRCORR" ], measurePoint);
    else error = 0.1;
  if(sysVar_ == "bTagSFUp")   result += error;
  if(sysVar_ == "bTagSFDown") result -= error;
  if(verbose_>=2) std::cout<< "effBTagSF= "<<result<<" +/- "<<error<<std::endl;
  return result;
}

// b tag eff. from MC for c jets as a function of jet pt, eta;
// as first step: take average of b and mis eff.
double BtagEventWeight::effBTagCjet(double jetPt, double jetEta)
{
  double result = -1111.;
  // if histo file exists, take value from there; else return a default value
  if(filename_!="") {
    TH2F* his = effHists_.find("EffCJetsTaggedPtEta")->second;
    if(jetPt >= maxPt_)       result = his->GetBinContent(his->FindBin(maxPt_-0.1, jetEta));
    else if(jetEta >= maxEta_)result = his->GetBinContent(his->FindBin(jetPt, maxEta_-0.01));
    else                      result = his->GetBinContent(his->FindBin(jetPt, jetEta));
  }
  else if(bTagAlgo_ == "SSVHEM") { result = (0.564/0.854 + 0.0195)/2;}
  if(verbose_>=2) std::cout<< "effBTagCjet= "<<result<<std::endl;
  return result;
}

// mistag eff. from MC as a function of jet pt, eta
double BtagEventWeight::effMisTag(double jetPt, double jetEta)
{
  double result = -1111.;
  // if histo file exists, take value from there; else return a default value
  if(filename_!="") {
    TH2F* his = effHists_.find("EffLJetsTaggedPtEta")->second;
    if(jetPt >= maxPt_)       result = his->GetBinContent(his->FindBin(maxPt_-0.1, jetEta));
    else if(jetEta >= maxEta_)result = his->GetBinContent(his->FindBin(jetPt, maxEta_-0.01));
    else                      result = his->GetBinContent(his->FindBin(jetPt, jetEta) );
  }
  else if(bTagAlgo_ == "SSVHEM") { result = 0.0195/0.97;}
  if(verbose_>=2) std::cout<< "effMisTag= "<<result<<std::endl;

  return result;
}

// mistag eff. SF as a function of jet pt, eta
double BtagEventWeight::effMisTagSF(double jetPt, double jetEta)
{
  double result = -1111., error = -1111.;
  const BtagPerformance & perf = *(perfHMisTag.product());
  BinningPointByMap measurePoint;
  measurePoint.insert(BinningVariables::JetEt, jetPt);
  measurePoint.insert(BinningVariables::JetAbsEta, jetEta);
  if(perf.isResultOk( measureMap_[ "BTAGLEFFCORR" ], measurePoint))
       result = perf.getResult( measureMap_[ "BTAGLEFFCORR" ], measurePoint);
  else result = 1.;
  if(perf.isResultOk( measureMap_[ "BTAGLERRCORR" ], measurePoint))
       error = perf.getResult( measureMap_[ "BTAGLERRCORR" ], measurePoint);
  else error = 0.1;
  if(sysVar_ == "misTagSFUp")   result += error;
  if(sysVar_ == "misTagSFDown") result -= error;
  if(verbose_>=2) std::cout<< "effMisTagSF= "<<result<<" +/- "<<error<<std::endl;
  return result;
}

// we produce a vector of weights 
std::vector<double> BtagEventWeight::effBTagEvent0123(std::vector<double> oneMinusBEffies, 
						      std::vector<double> oneMinusBMistags,
						      double scl_eff, double scl_mis){
 
 	// include scaling for grid - oneMinusBEffies and oneMinusBMistags are local copies
	for(unsigned i=0;i<oneMinusBEffies.size();i++)  oneMinusBEffies[i] =1-(1-oneMinusBEffies[i]) *scl_eff;
	for(unsigned i=0;i<oneMinusBMistags.size();i++) oneMinusBMistags[i]=1-(1-oneMinusBMistags[i])*scl_mis;

	std::vector<double> weights;

	double E0 = 1;
	double E1 = 0;
	for(unsigned i=0;i<oneMinusBEffies.size();i++){
		E0*=oneMinusBEffies[i];//E=\prod_{i=1}^b \eps(b-quark)_i
		E1+=(1-oneMinusBEffies[i])/oneMinusBEffies[i];// E2=\sum_{i=1}^b \eps(b-quark)_i / (1-\eps(b-quark)_i)
	}

	double M0 = 1;
	double M1 = 0;
	for(unsigned i=0;i<oneMinusBMistags.size();i++){
		M0*=oneMinusBMistags[i];//M=\prod_{i=1}^l \eps(light)_i
		M1+=(1-oneMinusBMistags[i])/oneMinusBMistags[i];// M2=\sum_{i=1}^l \eps(light)_i / (1-\eps(light)_i)
	}

	double E2 = 0;
	if(oneMinusBEffies.size()>=2)
		for(unsigned i=0;i<oneMinusBEffies.size()-1;i++)
			for(unsigned j=i+1;j<oneMinusBEffies.size();j++){
				E2+=(1-oneMinusBEffies[i])*(1-oneMinusBEffies[j])/oneMinusBEffies[i]/oneMinusBEffies[j];
	}
	double M2 = 0;
	if(oneMinusBMistags.size()>=2)
		for(unsigned i=0;i<oneMinusBMistags.size()-1;i++)
			for(unsigned j=i+1;j<oneMinusBMistags.size();j++){
				M2+=(1-oneMinusBMistags[i])*(1-oneMinusBMistags[j])/oneMinusBMistags[i]/oneMinusBMistags[j];
	}

	weights.push_back(E0*M0);
	weights.push_back(M0*E0*(E1+M1));
	weights.push_back(E0*M0*(E2+M2+E1*M1));
	weights.push_back(1-weights[0]-weights[1]-weights[2]);
	return weights;
}


// executed at the end after looping over all events
void
    BtagEventWeight::endJob() 
{
}


#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE( BtagEventWeight );

