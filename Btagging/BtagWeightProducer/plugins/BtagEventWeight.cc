#include "FWCore/Utilities/interface/EDMException.h"
#include "Btagging/BtagWeightProducer/plugins/BtagEventWeight.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/Common/interface/View.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"


BtagEventWeight::BtagEventWeight(const edm::ParameterSet& cfg):
  jets_               ( cfg.getParameter<edm::InputTag> ( "jets"   ) ),
  bTagAlgo_           ( cfg.getParameter<std::string>   ("bTagAlgo") ),
  sysVar_             ( cfg.getParameter<std::string>   ("sysVar"  ) ),
  verbose_            ( cfg.getParameter<int>           ("verbose" ) ),
  filename_           ( cfg.getParameter<std::string>   ("filename") ),
  rootDir_            ( cfg.getParameter<std::string>   ("rootDir" ) ),
  shift_              ( cfg.getParameter<double>        ("shift"   ) ),
  scaleJetEffSF_      ( cfg.getParameter<bool>          ("scaleJetEffSF"     ) ),
  scaleEventEffSF_    ( cfg.getParameter<bool>          ("scaleEventEffSF"   ) ),
  scaleEventMistagSF_ ( cfg.getParameter<bool>          ("scaleEventMistagSF") )
{
  // collections of weights that will be produced
  produces< std::vector<double> > ("RA4bJetWeights");
  produces< std::vector<double> > ("RA4bSFJetWeights");
  produces< std::vector<double> > ("RA4bEventWeights");
  produces< std::vector<double> > ("RA4bSFEventWeights");
  produces< std::vector<double> > ("effBTagEventGrid");

  produces< std::vector<std::vector<double> > > ("RA4bJetWeightsGrid");
  produces< std::vector<std::vector<double> > > ("RA4bEventWeightsGrid");
  produces< std::vector<std::vector<double> > > ("RA4bEventWeightsGridMistag");

  // set the edges of the last histo bin
  maxPt_ = 670.;
  maxEta_= 2.4;
  
  // load TFile Service
  edm::Service<TFileService> fs;
  if( !fs ){
    throw edm::Exception( edm::errors::Configuration,
			  "TFile Service is not registered in cfg file" );
  }
 
  std::cout << "bTagAlgo_: " << bTagAlgo_ << std::endl;

  // getting efficiency histos from input files
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
      
      // re-calculation of b tag efficiencies as input might be corrupted due to hadd
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
  
  // load map from database
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
  // setup measurement from database
  setup.get<BTagPerformanceRecord>().get( "BTAG"+bTagAlgo_, perfHBTag);
  setup.get<BTagPerformanceRecord>().get( "MISTAG"+bTagAlgo_, perfHMisTag);
  
  edm::Handle<edm::View< pat::Jet > > jets;
  evt.getByLabel(jets_, jets);

  double pt, eta;
  std::vector<double> BEffies(0) , BEffies_scaled(0);
  std::vector<double> oneMinusBEffies(0) , oneMinusBEffies_scaled(0);
  std::vector<double> oneMinusBMistags(0), oneMinusBMistags_scaled(0);
  
  // loop over jets
  for(edm::View<pat::Jet>::const_iterator jet = jets->begin();jet != jets->end(); ++jet)
    {
      pt  = jet->pt();
      eta = std::abs(jet->eta());

      if(jet->partonFlavour() == 5 || jet->partonFlavour() == -5)
	{	
	  BEffies.push_back(effBTag(pt, eta));
	  BEffies_scaled.push_back(effBTag(pt, eta)*(effBTagSF(pt, eta,1)+shift_) );
	  oneMinusBEffies.push_back(1.- effBTag(pt, eta));
	  oneMinusBEffies_scaled.push_back(1.- effBTag(pt, eta) * (effBTagSF(pt, eta,1)+shift_) );
	}     
      else if(jet->partonFlavour() == 4 || jet->partonFlavour() == -4)
	{
	  BEffies.push_back(effBTagCjet(pt, eta));
	  BEffies_scaled.push_back(effBTagCjet(pt, eta)*(effBTagSF(pt, eta,2)) );
	  oneMinusBMistags.push_back(1.- effBTagCjet(pt, eta));
	  oneMinusBMistags_scaled.push_back(1.-effBTagCjet(pt, eta)*(effBTagSF(pt, eta,2)) );
	}
      else
	{ 
	  BEffies.push_back(effMisTag(pt, eta));
	  BEffies_scaled.push_back(effMisTag(pt, eta)*effMisTagSF(pt, eta));
	  oneMinusBMistags               .push_back(1.- effMisTag(pt, eta));
	  oneMinusBMistags_scaled        .push_back(1.-(effMisTag(pt, eta) * effMisTagSF(pt, eta)));
	}

    }

  // collection of jet weights
  std::auto_ptr<std::vector<double> > RA4bJetWeights( new std::vector<double> );
  *RA4bJetWeights = BEffies; 
  evt.put(RA4bJetWeights,"RA4bJetWeights");

  // collection of jet weights with scale factors applied
  std::auto_ptr<std::vector<double> > RA4bSFJetWeights( new std::vector<double> );
  *RA4bSFJetWeights = BEffies_scaled; 
  evt.put(RA4bSFJetWeights,"RA4bSFJetWeights");

  // collection of event weights
  std::auto_ptr<std::vector<double> > RA4bEventWeights( new std::vector<double> );
  *RA4bEventWeights = effBTagEvent0123(oneMinusBEffies, oneMinusBMistags, 1, 1); 
  evt.put(RA4bEventWeights,"RA4bEventWeights");

  // collection of event weights with scale factors applied
  std::auto_ptr<std::vector<double> > RA4bSFEventWeights( new std::vector<double> );
  *RA4bSFEventWeights = effBTagEvent0123(oneMinusBEffies_scaled, oneMinusBMistags_scaled, 1, 1); 
  evt.put(RA4bSFEventWeights,"RA4bSFEventWeights");

  //=======================================================================================
  //=================================== BAUSTELLE =========================================
  //=======================================================================================

  if(scaleJetEffSF_==true)
    {
      std::vector<std::vector<double> > BtagEffSFShiftGrid(0);
      
      for(int sdx=-10; sdx <= 10; ++sdx)
	{
	  double SFShift=sdx*0.05;
	  std::vector<double> BtagEffSFShiftVec(0);
	  
	  for(edm::View<pat::Jet>::const_iterator jet = jets->begin();jet != jets->end(); ++jet)
	    {
	      pt  = jet->pt();
	      eta = std::abs(jet->eta());
	      
	      if(jet->partonFlavour() == 5 || jet->partonFlavour() == -5)
		{
		  BtagEffSFShiftVec.push_back(effBTag(pt, eta)*(effBTagSF(pt, eta,1)+SFShift) );
		}
	      else if(jet->partonFlavour() == 4 || jet->partonFlavour() == -4)
		{
		  BtagEffSFShiftVec.push_back(effBTagCjet(pt, eta)*(effBTagSF(pt, eta,2)) );
		}
	      else
		{
		  BtagEffSFShiftVec.push_back(effMisTag(pt, eta)*effMisTagSF(pt, eta));
		}
	    }
	  BtagEffSFShiftGrid.push_back(BtagEffSFShiftVec);
	}
      
      // grid of jet weights with scale factors applied
      std::auto_ptr<std::vector<std::vector<double> > >  RA4bJetWeightsGrid( new std::vector<std::vector<double> >);
      *RA4bJetWeightsGrid = BtagEffSFShiftGrid ; 
      evt.put(RA4bJetWeightsGrid,"RA4bJetWeightsGrid");
    }

  //=======================================================================================
  //=================================== BAUSTELLE =========================================
  //=======================================================================================

  if(scaleEventEffSF_==true)
    {
      std::vector<std::vector<double> > BtagEffSFShiftGrid(0);
      
      for(int sdx=-10; sdx <= 10 ; ++sdx)
	{
	  double SFShift=sdx*0.05;;
	  
	  double JetPt, JetEta;
	  std::vector<double> oneMinusBEff_scaled(0);
	  std::vector<double> oneMinusBMis_scaled(0);

	  for(edm::View<pat::Jet>::const_iterator jet = jets->begin();jet != jets->end(); ++jet)
	    {
	      JetPt  = jet->pt();
	      JetEta = std::abs(jet->eta());
	      if(jet->partonFlavour() == 5 || jet->partonFlavour() == -5)
		{	
		  oneMinusBEff_scaled.push_back(1.- effBTag(JetPt, JetEta)*(effBTagSF(JetPt, JetEta,1)+SFShift));
		}
	      else if(jet->partonFlavour() == 4 || jet->partonFlavour() == -4)
		{
		  oneMinusBMis_scaled.push_back(1.-effBTagCjet(JetPt, JetEta)*(effBTagSF(JetPt, JetEta,2)));
		}
	      else
		{
		  oneMinusBMis_scaled.push_back(1.-(effMisTag(JetPt, JetEta)*effMisTagSF(JetPt, JetEta)));
		}
	    }
	  BtagEffSFShiftGrid.push_back(effBTagEvent0123(oneMinusBEff_scaled, oneMinusBMis_scaled, 1, 1) );
	}
       
      // grid of event weights with scale factors applied
      std::auto_ptr<std::vector<std::vector<double> > >  RA4bEventWeightsGrid( new std::vector<std::vector<double> >);
      *RA4bEventWeightsGrid = BtagEffSFShiftGrid; 
      evt.put(RA4bEventWeightsGrid,"RA4bEventWeightsGrid");
    }
  
  if(scaleEventMistagSF_==true)
    {
      std::vector<std::vector<double> > MistagSFShiftGrid(0);
      
      for(int sdx=-10; sdx <= 10 ; ++sdx)
	{
	  double SFShift=sdx*0.01;;
	  
	  double JetPt, JetEta;
	  std::vector<double> oneMinusBEff_scaled(0);
	  std::vector<double> oneMinusBMis_scaled(0);

	  for(edm::View<pat::Jet>::const_iterator jet = jets->begin();jet != jets->end(); ++jet)
	    {
	      JetPt  = jet->pt();
	      JetEta = std::abs(jet->eta());
	      if(jet->partonFlavour() == 5 || jet->partonFlavour() == -5)
		{	
		  oneMinusBEff_scaled.push_back(1.- effBTag(JetPt, JetEta)*effBTagSF(JetPt, JetEta,1));
		}
	      else if(jet->partonFlavour() == 4 || jet->partonFlavour() == -4)
		{
		  oneMinusBMis_scaled.push_back(1.-(effBTagCjet(JetPt, JetEta)*(effBTagSF(JetPt, JetEta,2)+SFShift)));
		}
	      else
		{
		  oneMinusBMis_scaled.push_back(1.-(effMisTag(JetPt, JetEta)*(effMisTagSF(JetPt, JetEta)+SFShift)));
		}
	    }
	  MistagSFShiftGrid.push_back(effBTagEvent0123(oneMinusBEff_scaled, oneMinusBMis_scaled, 1, 1) );
	}
       
      // grid of event weights with scale factors applied
      std::auto_ptr<std::vector<std::vector<double> > > RA4bEventWeightsGridMistag( new std::vector<std::vector<double> >);
      *RA4bEventWeightsGridMistag = MistagSFShiftGrid; 
      evt.put(RA4bEventWeightsGridMistag,"RA4bEventWeightsGridMistag");
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

// b tag eff. SF as a function of jet pt, eta - kept for reference and later use with updated db
double BtagEventWeight::effBTagSF_old(double jetPt, double jetEta)
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
  // std::cout<< "effBTagSF old ("<<jetPt<<")="<<result<<" +/- "<<error<<std::endl;
  return result;
}
// b tag eff. SF as a function of jet pt, eta - see https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagPOG#Recommendation_for_b_c_tagging_a
double BtagEventWeight::effBTagSF(double jetPt, double jetEta, double blowUp)
{

  double result = 0.932251*((1.+(0.00335634*jetPt))/(1.+(0.00305994*jetPt)));

  //Find the correct pt bin
  //Works for 16 different pt bins. 
  //This must be changed by hand, if the payload changes.
  int ptBinNum = 15; //Initialise to last bin. 
  
  //Loop through each of the bins, iBin, in order of pt. 
  //When one finds a ptmin[iBin] value greater than jetPt, set ptBinNum to iBin-1 and escape.
  //This works except for jets in the last bin, which is taken into account by the initialisation.
  if ( jetPt < SFb_ptmin[15] ) {
    for (int iPtBin = 0 ; iPtBin < 16 ; iPtBin++ ) {
      if (SFb_ptmin[iPtBin] > jetPt) {
	ptBinNum = iPtBin - 1;
	break;
      }
    }
  }
  //Protect against negative values. Should not be needed.
  if (ptBinNum < 0) ptBinNum = 0;

  if (ptBinNum == 0)  result = 0.939843589813758817; //0.932251*((1.+(0.00335634*30))/(1.+(0.00305994*30)));
  if (ptBinNum == 15) result = 0.992947446654368848; // 0.932251*((1.+(0.00335634*670))/(1.+(0.00305994*670)));
  double   error = SFb_err[ptBinNum];

  if(sysVar_ == "bTagSFUp")   result += error*blowUp;
  if(sysVar_ == "bTagSFDown") result -= error*blowUp;
  if(verbose_>=2) std::cout<< "effBTagSF= "<<result<<" +/- "<<error<<std::endl;
  // std::cout<< "effBTagSF new ("<<jetPt<<")= "<<result<<" +/- "<<error<<std::endl;

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
double BtagEventWeight::effMisTagSF_old(double jetPt, double jetEta)
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

  //if(sysVar_ == "misTagSFUp" || sysVar_ == "misTagSFDown")
  //{
  //  std::cout << "result: " << result << std::endl;
  //  std::cout << "error: " << error << std::endl;
  //}
  
  if(sysVar_ == "misTagSFUp")   result += error;
  if(sysVar_ == "misTagSFDown") result -= error;

  //if(sysVar_ == "misTagSFUp") std::cout << "effMisTagSFUp: "<< result << std::endl;
  //if(sysVar_ == "misTagSFDown") std::cout << "effMisTagDown: "<< result << std::endl;

  if(verbose_>=2) std::cout<< "effMisTagSF= "<<result<<" +/- "<<error<<std::endl;
  //std::cout<< "effMisTagSF old (pt="<<jetPt<<", eta="<<jetEta<<") = "<<result<<" +/- "<<error<<std::endl;
  return result;
}

// mistag eff. SF as a function of jet pt, eta - see https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagPOG#Recommendation_for_b_c_tagging_a
double BtagEventWeight::effMisTagSF(double jetPt, double jetEta)
{
  double result,max,min;

  if(fabs(jetEta)>2.4) { // to keep it running as in the old code
  		result =   1;
  		max    = 0.1;
  		min    = 0.1;
  } else if(jetPt<=670) {
  	if(fabs(jetEta)<=0.8) {
  		result  = SFL_0008_mean(jetPt);
  		max     = SFL_0008_max(jetPt);
  		min     = SFL_0008_min(jetPt);
  	} else if(fabs(jetEta)<=1.6) {
  		result  = SFL_0816_mean(jetPt);
  		max     = SFL_0816_max(jetPt);
  		min     = SFL_0816_min(jetPt);
  	} else { // <=2.4
  		result  = SFL_1624_mean(jetPt);
  		max     = SFL_1624_max(jetPt);
  		min     = SFL_1624_min(jetPt);
  	} 
  } else { // pt>670
    //Following BTAG POG recommendation, use the SF for eta integrated, with twice the uncertainty.
  		result  = SFL_0024_mean(670);
  		max     = SFL_0024_mean(670) + 2.*( SFL_0024_max(670) - SFL_0024_mean(670) );
  		min     = SFL_0024_mean(670) + 2.*( SFL_0024_min(670) - SFL_0024_mean(670) );
  } 
  
  if(sysVar_ == "misTagSFUp")   result = max;
  if(sysVar_ == "misTagSFDown") result = min;

  if(verbose_>=2) std::cout<< "effMisTagSF= "<<result<<" (max="<<max<<", min="<<min<<std::endl;
  // std::cout<< "effMisTagSF new (pt="<<jetPt<<", eta="<<jetEta<<") = "<<result<<" (max="<<max<<", min="<<min<<std::endl;
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
// numbers from https://twiki.cern.ch/twiki/pub/CMS/BtagPOG/SFb-mujet_payload.txt
float BtagEventWeight::SFb_err[] = {0.12, 0.0311456, 0.0303825, 0.0209488, 0.0216987, 0.0227149, 0.0260294, 0.0205766, 0.0227065, 0.0260481, 0.0278001, 0.0295361, 0.0306555, 0.0367805, 0.0527368 , 0.1054736};
float BtagEventWeight::SFb_ptmin[] = {0, 30, 40, 50, 60, 70, 80, 100, 120, 160, 210, 260, 320, 400, 500, 670};


double BtagEventWeight::SFL_0008_mean(double x){
	return (1.2875*((1+(-0.000356371*x))+(1.08081e-07*(x*x))))+(-6.89998e-11*(x*(x*(x/(1+(-0.0012139*x))))));
}
double BtagEventWeight::SFL_0008_max(double x){
	return (1.47515*((1+(-0.000484868*x))+(2.36817e-07*(x*x))))+(-2.05073e-11*(x*(x*(x/(1+(-0.00142819*x))))));
}
double BtagEventWeight::SFL_0008_min(double x){
	return (1.11418*((1+(-0.000442274*x))+(1.53463e-06*(x*x))))+(-4.93683e-09*(x*(x*(x/(1+(0.00152436*x))))));
}
double BtagEventWeight::SFL_0816_mean(double x){
	return (1.24986*((1+(-0.00039734*x))+(5.37486e-07*(x*x))))+(-1.74023e-10*(x*(x*(x/(1+(-0.00112954*x))))));
}
double BtagEventWeight::SFL_0816_max(double x){
	return (1.41211*((1+(-0.000559603*x))+(9.50754e-07*(x*x))))+(-5.81148e-10*(x*(x*(x/(1+(-0.000787359*x))))));
}
double BtagEventWeight::SFL_0816_min(double x){
	return (1.08828*((1+(-0.000208737*x))+(1.50487e-07*(x*x))))+(-2.54249e-11*(x*(x*(x/(1+(-0.00141477*x))))));
}
double BtagEventWeight::SFL_1624_mean(double x){
	return (1.10763*((1+(-0.000105805*x))+(7.11718e-07*(x*x))))+(-5.3001e-10*(x*(x*(x/(1+(-0.000821215*x))))));
}
double BtagEventWeight::SFL_1624_min(double x){
	return (0.958079*((1+(0.000327804*x))+(-4.09511e-07*(x*x))))+(-1.95933e-11*(x*(x*(x/(1+(-0.00143323*x))))));
}
double BtagEventWeight::SFL_1624_max(double x){
	return (1.26236*((1+(-0.000524055*x))+(2.08863e-06*(x*x))))+(-2.29473e-09*(x*(x*(x/(1+(-0.000276268*x))))));
}
double BtagEventWeight::SFL_0024_mean(double x){
	return (1.06268*((1+(0.00390509*x))+(-5.85405e-05*(x*x))))+(7.87135e-07*(x*(x*(x/(1+(0.01259*x))))));
}
double BtagEventWeight::SFL_0024_min(double x){
	return (0.967092*((1+(0.00201431*x))+(-1.49359e-05*(x*x))))+(6.94324e-08*(x*(x*(x/(1+(0.00459787*x))))));
}
double BtagEventWeight::SFL_0024_max(double x){
	return (1.22691*((1+(0.00211682*x))+(-2.07959e-05*(x*x))))+(1.72938e-07*(x*(x*(x/(1+(0.00658853*x))))));
}


#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE( BtagEventWeight );

