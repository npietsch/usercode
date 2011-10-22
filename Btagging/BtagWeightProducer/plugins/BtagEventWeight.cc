#include "FWCore/Utilities/interface/EDMException.h"
#include "Btagging/BtagWeightProducer/plugins/BtagEventWeight.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/Common/interface/View.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"


BtagEventWeight::BtagEventWeight(const edm::ParameterSet& cfg):
  jets_    ( cfg.getParameter<edm::InputTag>    ( "jets"   ) ),
  bTagAlgo_( cfg.getParameter<std::string>      ("bTagAlgo") ),
  sysVar_  ( cfg.getParameter<std::string>      ("sysVar"  ) ),
  verbose_ ( cfg.getParameter<int>              ("verbose" ) ),
  filename_( cfg.getParameter<std::string>      ("filename"  ) )
{
  produces<double>();

  produces< std::vector<double>  > ("effBTagEventGrid");  
  // set the edges of the last histo bin
  maxPt_ = 250.;
  maxEta_= 3.;
  
  // laod TFile Service
  edm::Service<TFileService> fs;
  if( !fs ){
    throw edm::Exception( edm::errors::Configuration,
			  "TFile Service is not registered in cfg file" );
  }
  /// booking of histogram for b tag eff SF
  hists_["effBTagEventSF"]     = fs->make<TH1F>( "effBTagEventSF", "effBTagEventSF", 100, 0, 1 );
  hists_["effBTagEventSFMean"] = fs->make<TH1F>( "effBTagEventSFMean", "effBTagEventSFMean", 1, 0, 1 );
  
  /// getting efficiency histos from input files
  if(filename_!=""){
    file_ = new TFile((TString)filename_);
    if(!(file_->IsZombie())){
      if(verbose_>=1) std::cout<<filename_<<" opened"<<std::endl;
//       effHists_["NumBJetsPt"]       = (TH1F*) file_->Get("bTagEff/NumBJetsPt")->Clone();
//       effHists_["NumBJetsTaggedPt"] = (TH1F*) file_->Get("bTagEff/NumBJetsTaggedPt")->Clone();
//       effHists_["EffBJetsTaggedPt"] = (TH1F*) file_->Get("bTagEff/EffBJetsTaggedPt")->Clone();
//       effHists_["NumCJetsPt"]       = (TH1F*) file_->Get("bTagEff/NumCJetsPt")->Clone();
//       effHists_["NumCJetsTaggedPt"] = (TH1F*) file_->Get("bTagEff/NumCJetsTaggedPt")->Clone();
//       effHists_["EffCJetsTaggedPt"] = (TH1F*) file_->Get("bTagEff/EffCJetsTaggedPt")->Clone();
//       effHists_["NumLJetsPt"]       = (TH1F*) file_->Get("bTagEff/NumLJetsPt")->Clone();
//       effHists_["NumLJetsTaggedPt"] = (TH1F*) file_->Get("bTagEff/NumLJetsTaggedPt")->Clone();
//       effHists_["EffLJetsTaggedPt"] = (TH1F*) file_->Get("bTagEff/EffLJetsTaggedPt")->Clone();
//       
//       /// re-calculation of b tag efficiencies as input might be corrupted due to hadd
//       if(effHists_.count("NumBJetsPt") && effHists_.count("NumBJetsTaggedPt") && effHists_.count("EffBJetsTaggedPt") &&
// 	 effHists_.count("NumCJetsPt") && effHists_.count("NumCJetsTaggedPt") && effHists_.count("EffCJetsTaggedPt") &&
// 	 effHists_.count("NumBJetsPt") && effHists_.count("NumBJetsTaggedPt") && effHists_.count("EffBJetsTaggedPt")) {
// 	
// 	effHists_.find("EffBJetsTaggedPt")->second->Reset();
//         effHists_.find("EffCJetsTaggedPt")->second->Reset();
//         effHists_.find("EffLJetsTaggedPt")->second->Reset();
//       
//         effHists_.find("EffBJetsTaggedPt")->second->Divide(effHists_.find("NumBJetsTaggedPt")->second, 
//             effHists_.find("NumBJetsPt")->second,1,1,"B");
//         effHists_.find("EffCJetsTaggedPt")->second->Divide(effHists_.find("NumCJetsTaggedPt")->second, 
//             effHists_.find("NumCJetsPt")->second,1,1,"B");
//         effHists_.find("EffLJetsTaggedPt")->second->Divide(effHists_.find("NumLJetsTaggedPt")->second, 
//             effHists_.find("NumLJetsPt")->second,1,1,"B");
      
	effHists_["NumBJetsPtEta"]       = (TH2F*) file_->Get("bTagEff/NumBJetsPtEta")->Clone();
	effHists_["NumBJetsTaggedPtEta"] = (TH2F*) file_->Get("bTagEff/NumBJetsTaggedPtEta")->Clone();
	effHists_["EffBJetsTaggedPtEta"] = (TH2F*) file_->Get("bTagEff/EffBJetsTaggedPtEta")->Clone();
	effHists_["NumCJetsPtEta"]       = (TH2F*) file_->Get("bTagEff/NumCJetsPtEta")->Clone();
	effHists_["NumCJetsTaggedPtEta"] = (TH2F*) file_->Get("bTagEff/NumCJetsTaggedPtEta")->Clone();
	effHists_["EffCJetsTaggedPtEta"] = (TH2F*) file_->Get("bTagEff/EffCJetsTaggedPtEta")->Clone();
	effHists_["NumLJetsPtEta"]       = (TH2F*) file_->Get("bTagEff/NumLJetsPtEta")->Clone();
	effHists_["NumLJetsTaggedPtEta"] = (TH2F*) file_->Get("bTagEff/NumLJetsTaggedPtEta")->Clone();
	effHists_["EffLJetsTaggedPtEta"] = (TH2F*) file_->Get("bTagEff/EffLJetsTaggedPtEta")->Clone();
	
	/// re-calculation of b tag efficiencies as input might be corrupted due to hadd
	if(effHists_.count("NumBJetsPtEta") && effHists_.count("NumBJetsTaggedPtEta") && effHists_.count("EffBJetsTaggedPtEta") &&
	  effHists_.count("NumCJetsPtEta") && effHists_.count("NumCJetsTaggedPtEta") && effHists_.count("EffCJetsTaggedPtEta") &&
	  effHists_.count("NumBJetsPtEta") && effHists_.count("NumBJetsTaggedPtEta") && effHists_.count("EffBJetsTaggedPtEta")) {
	  
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
  measureMap_["BTAGBEFFCORR"]=PerformanceResult::BTAGBEFFCORR;
  measureMap_["BTAGBERRCORR"]=PerformanceResult::BTAGBERRCORR;
  measureMap_["BTAGLEFFCORR"]=PerformanceResult::BTAGLEFFCORR;
  measureMap_["BTAGLERRCORR"]=PerformanceResult::BTAGLERRCORR;
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
  std::vector<double> oneMinusBEffies(0) , oneMinusBEffies_scaled(0);
  std::vector<double> oneMinusBMistags(0), oneMinusBMistags_scaled(0);
  
    for(edm::View<pat::Jet>::const_iterator jet = jets->begin();jet != jets->end(); ++jet) {
      pt  = jet->pt();
      eta = std::abs(jet->eta());
      if(jet->partonFlavour() == 5 || jet->partonFlavour() == -5){
	oneMinusBEffies               .push_back(1.- effBTag(pt, eta));
	oneMinusBEffies_scaled        .push_back(1.- (effBTag(pt, eta) * effBTagSF(pt, eta)));
      }
  
      else if(jet->partonFlavour() == 4 || jet->partonFlavour() == -4){
	oneMinusBMistags               .push_back(1.- effBTagCjet(pt, eta));
	oneMinusBMistags_scaled        .push_back(1.-(effBTagCjet(pt, eta) * effBTagSF(pt, eta)));
      }
  
      else{
	oneMinusBMistags               .push_back(1.- effMisTag(pt, eta));
	oneMinusBMistags_scaled        .push_back(1.-(effMisTag(pt, eta) * effMisTagSF(pt, eta)));
      }
   }
     
   double effBTagEvent_unscaled = effBTagEvent( oneMinusBEffies, oneMinusBMistags );
   double effBTagEvent_scaled   = effBTagEvent( oneMinusBEffies_scaled, oneMinusBMistags_scaled );
   double effBTagEventSF = effBTagEvent_scaled / effBTagEvent_unscaled;
  
   if(verbose_>=1) std::cout<<"effBTagEvent_unscaled= "<<effBTagEvent_unscaled
	                    <<" effBTagEvent_scaled = " <<effBTagEvent_scaled
	                    <<" effBTagEventSF ="       <<effBTagEventSF << std::endl;
   
   hists_.find("effBTagEventSF" )->second->Fill( effBTagEventSF );

  std::auto_ptr<double> bTagSFEventWeight(new double);
  *bTagSFEventWeight = effBTagEventSF;    
  evt.put(bTagSFEventWeight);  

//dk
//  std::vector<double> blah = effBTagEvent0123(oneMinusBEffies, oneMinusBMistags, 1.,1.);
//	std::cout<<"DK "<<blah[0]<<" "<<blah[1]<<" "<<blah[2]<<" "<<blah[3]<<std::endl;
//	std::cout<<"   "<<blah[2]+blah[3]<<" =?= "<<effBTagEvent_unscaled<<std::endl;

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

  // test printout
  for(unsigned i=0;i<N;i++)
  for(unsigned j=0;j<N;j++){
	std::cout<<"(fac_eff="<<points[i]<<", fac_mis="<<points[j]<<") : ";
	for(unsigned k=0;k<M;k++)
		std::cout<<(*effBTagEventGrid)[k+j*M+i*N*M]<<" ";
	std::cout<<std::endl;
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
    else                      result = his->GetBinContent( his->FindBin(jetPt, jetEta) );
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
    else                      result = his->GetBinContent( his->FindBin(jetPt, jetEta) );
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

//--------------------------------------------------------------------------

// calculate event b tag efficiency for >=2 b tags
double BtagEventWeight::effBTagEvent(std::vector<double> &oneMinusBEffies,
				       std::vector<double> &oneMinusBMistags)
{
  double bTaggingEfficiency = 1.;
  double tmp = 1.;

  if(verbose_) std::cout << oneMinusBEffies.size() << ": " << std::flush;

  for(std::vector<double>::const_iterator eff = oneMinusBEffies.begin();
eff != oneMinusBEffies.end(); ++eff){
    tmp *= (*eff);
    if(verbose_) std::cout << 1.-(*eff) << ", ";
  }
  if(verbose_) std::cout << oneMinusBMistags.size() << ": " << std::flush;
  for(std::vector<double>::const_iterator mis =
oneMinusBMistags.begin(); mis != oneMinusBMistags.end(); ++mis){
    tmp *= (*mis);
    if(verbose_) std::cout << 1.-(*mis) << ", ";
  }
  bTaggingEfficiency -= tmp;
  for(std::vector<double>::const_iterator eff = oneMinusBEffies.begin();
eff != oneMinusBEffies.end(); ++eff){
    tmp = 1.-(*eff);
    for(std::vector<double>::const_iterator eff2 =
oneMinusBEffies.begin(); eff2 != oneMinusBEffies.end(); ++eff2){
      if(eff != eff2) tmp *= (*eff2);
    }
    for(std::vector<double>::const_iterator mis =
oneMinusBMistags.begin(); mis != oneMinusBMistags.end(); ++mis){
      tmp *= (*mis);
    }
    bTaggingEfficiency -= tmp;
  }
  for(std::vector<double>::const_iterator mis =
oneMinusBMistags.begin(); mis != oneMinusBMistags.end(); ++mis){
    tmp = 1.-(*mis);
    for(std::vector<double>::const_iterator eff =
oneMinusBEffies.begin(); eff != oneMinusBEffies.end(); ++eff){
      tmp *= (*eff);
    }
    for(std::vector<double>::const_iterator mis2 =
oneMinusBMistags.begin(); mis2 != oneMinusBMistags.end(); ++mis2){
      if(mis != mis2) tmp *= (*mis2);
    }
    bTaggingEfficiency -= tmp;
  }
  if(verbose_) std::cout << " -> " << bTaggingEfficiency << std::endl;
  return bTaggingEfficiency;

}

//dk
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
  double effBTagEventSFMean = hists_.find("effBTagEventSF" )->second->GetMean();
  hists_.find("effBTagEventSFMean" )->second->Fill(0.5, effBTagEventSFMean );
  if(verbose_>=1) std::cout<<"Mean effBTagEventSF = "<<effBTagEventSFMean<<std::endl;
}


#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE( BtagEventWeight );

