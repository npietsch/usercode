#include <cmath>
#include <memory>
#include <string>
#include <iostream>
#include <vector>

#include "TFile.h"
#include "TH1.h"

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ParameterSet/interface/FileInPath.h"

#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h" 

//
// class decleration
//

class WeightProducer: public edm::EDProducer {
   public:
      explicit WeightProducer(const edm::ParameterSet&);
      ~WeightProducer();

   private:
      //  virtual void beginJob() ;
      virtual void produce(edm::Event&, const edm::EventSetup&);
      virtual void endJob();

      const std::string _weightingMethod;
      const double _expo;
      const double _startWeight;
      const double _LumiScale;
      const double _xs;
      const double _NumberEvents;
      const double _lumi;

      edm::InputTag _weightName;
      std::vector<double> _puWeigths;
      double _weightFactor;
      bool _applyPUWeights;

      std::vector<double> generate_flat10_weights(const TH1* data_npu_estimated) const;
      double getPUWeight(int npu) const;
};

WeightProducer::WeightProducer(const edm::ParameterSet& iConfig) :
   _weightingMethod(iConfig.getParameter<std::string> ("Method")), _expo(iConfig.getParameter<double> ("Exponent")),
         _startWeight(iConfig.getParameter<double> ("weight")), _LumiScale(iConfig.getParameter<double> ("LumiScale")),
         _xs(iConfig.getParameter<double> ("XS")), _NumberEvents(iConfig.getParameter<double> ("NumberEvts")), _lumi(
               iConfig.getParameter<double> ("Lumi")), _weightName(iConfig.getParameter<edm::InputTag> ("weightName")) {

   // Option 1: weight constant, as defined in cfg file
   if (_startWeight >= 0) {
      std::cout << "WeightProducer: Using constant event weight of " << _startWeight << std::endl;
   }

   // Option 2: weight from event
   else if (_weightingMethod == "FromEvent") {
      std::cout << "WeightProducer: Using weight from event" << std::endl;
   }

   // Option 3: compute new weight
   else if (_weightingMethod == "Constant") {
      _weightFactor = _lumi * _xs / _NumberEvents;
      std::cout << "WeightProducer: Using constant event weight of " << _weightFactor << std::endl;
      std::cout << "  Target luminosity (1/pb) : " << _lumi << std::endl;
      std::cout << "        Cross section (pb) : " << _xs << std::endl;
      std::cout << "          Number of events : " << _NumberEvents << std::endl;
   }

   else if (_weightingMethod == "PtHat") {
      _weightFactor = _lumi * _xs / (_NumberEvents * pow(15., _expo));
      std::cout << "WeightProducer: Using ptHat dependent event weight" << std::endl;
   }

   // No option specified
   else {
      std::cerr << "WARNING: WeightProducer: No weighting option specified. Using event weights of 1" << std::endl;
   }

   ///This is to consider the lumi-uncertainty, i.e. to scale the weights up- or down by 1sigma of the lumi-scale
   ///uncertainty. In general the scale is 1.0!
   _weightFactor *= _LumiScale;

   if (_LumiScale != 1.) {
      std::cout << "WeightProducer: Scaling event weights by factor " << _LumiScale << std::endl;
   }

   // Optionally, compute multiplicative weight factors for PU reweighting
   // The weights are a function of the generated PU interactions and the
   // expected data distribution is given as a histogram from a ROOT file.
   // See https://twiki.cern.ch/twiki/bin/viewauth/CMS/PileupReweighting
   std::string fileNamePU = iConfig.getParameter<std::string> ("FileNamePUDataDistribution");
   if (fileNamePU.length() != 0 && fileNamePU != "NONE") {
      _applyPUWeights = true;
      edm::FileInPath filePUDataDistr(fileNamePU);

      std::cout << "WeightProducer: Applying multiplicative PU weights" << std::endl;
      std::cout << "  Reading PU scenario from '" << filePUDataDistr.fullPath() << "'" << std::endl;
      TFile file(filePUDataDistr.fullPath().c_str(), "READ");
      TH1 *h = 0;
      file.GetObject("pileup", h);
      if (h) {
         h->SetDirectory(0);
      } else {
         std::cerr << "ERROR in WeightProducer: Histogram 'pileup' does not exist in file '"
               << filePUDataDistr.fullPath() << "'\n.";
         std::cerr
               << "See https://twiki.cern.ch/twiki/bin/view/CMS/HamburgWikiAnalysisCalibration#Pile_Up_Reweighting for available input distributions."
               << std::endl;
         exit(1);
      }
      file.Close();

      std::cout << "  Computing weights" << std::endl;
      _puWeigths = generate_flat10_weights(h);

      delete h;
   } else {
      _applyPUWeights = false;
   }

   //register your products
   produces<double> ("weight");
}

WeightProducer::~WeightProducer() {
}

// ------------ method called to produce the data  ------------
void WeightProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup) {

   double resultWeight = 1.;

   //Option 1: constant start weight from config file
   if (_startWeight >= 0) {
     resultWeight = _startWeight;
     resultWeight *= _LumiScale;  //could not be done in constructor as _startWeight is read only
   }

   //Option 2: existing weight variable in the event named as in _weightName
   else if (_weightingMethod == "FromEvent") {
     //std::cout << "Option2" << std::endl;
      edm::Handle<double> event_weight;
      iEvent.getByLabel(_weightName, event_weight);
      resultWeight = (event_weight.isValid() ? (*event_weight) : 1.0);

      ///This is to consider the lumi-uncertainty, i.e. to scale the weights up- or down by 1sigma of the lumi-scale
      ///uncertainty. In general the scale is 1.0!
      resultWeight *= _LumiScale;
   }

   //Option 3: weighting from lumi, xs, and num evts
   else if (_weightingMethod == "Constant") {
     //std::cout << "Option3a" << std::endl;
      resultWeight = _weightFactor;
   } else if (_weightingMethod == "PtHat") {
      // Get pthat
     double ptHat = 0.;
     edm::Handle<GenEventInfoProduct> genEvtInfoHandle;
     iEvent.getByLabel("generator", genEvtInfoHandle);
     if (genEvtInfoHandle.isValid()) {
       ptHat = genEvtInfoHandle->binningValues()[0];
       resultWeight = _weightFactor * pow(ptHat, _expo);
     } else {
       std::cout << "WARNING:: PtHat information needed but not available: set weight to 1!" << std::endl;
       resultWeight = 1.;
     }
   }
   
   // Optionally, multiply PU weight
   edm::Handle<std::vector<PileupSummaryInfo> > puInfo;
   iEvent.getByLabel("addPileupInfo", puInfo);
   int npu = 0;
   if (_applyPUWeights) {
      if (puInfo.isValid()) {
         std::vector<PileupSummaryInfo>::const_iterator puIt;
         int n = 0;
         for (puIt = puInfo->begin(); puIt != puInfo->end(); ++puIt, ++n) {
            //std::cout << " Pileup Information: bunchXing, nvtx: " << puIt->getBunchCrossing() << " " << puIt->getPU_NumInteractions() << std::endl;
            if (puIt->getBunchCrossing() == 0) { // Select in-time bunch crossing
               npu = puIt->getPU_NumInteractions();
               break;
            }
         }
         resultWeight *= getPUWeight(npu);
      } else
         std::cout << "No Valid PileupSummaryInfo Object! PU reweighing not applied!" << std::endl;
   }

   ///Also, here one could define look-up tables for all used samples.
   ///An identifying 'string' for the currently used sample could be read
   ///from the config file. Perhaps this can be obtained dirtectly from crab?
   //---------------------------------------------------------------------------

   // put weight into the Event
   std::auto_ptr<double> pOut(new double(resultWeight));
   iEvent.put(pOut, "weight");
}

// ------------ method called once each job just before starting event loop  ------------
//void
//WeightProducer::beginJob()
//{
//}

// ------------ method called once each job just after ending the event loop  ------------
void WeightProducer::endJob() {
}

// Get weight factor dependent on number of 
// added PU interactions
// --------------------------------------------------
double WeightProducer::getPUWeight(int npu) const {
   double w = 1.;
   if (npu < static_cast<int> (_puWeigths.size())) {
      w = _puWeigths.at(npu);
   } else {
      std::cerr << "WARNING in WeightProcessor::getPUWeight: Number of PU vertices = " << npu
            << " out of histogram binning." << std::endl;
   }

   return w;
}

// Generate weights for given data PU distribution
// Code from: https://twiki.cern.ch/twiki/bin/viewauth/CMS/PileupReweighting
// --------------------------------------------------
std::vector<double> WeightProducer::generate_flat10_weights(const TH1* data_npu_estimated) const {
   // see SimGeneral/MixingModule/python/mix_E7TeV_FlatDist10_2011EarlyData_inTimeOnly_cfi.py; copy and paste from there:
   const double npu_probs[25] = { 0.0698146584, 0.0698146584, 0.0698146584, 0.0698146584, 0.0698146584, 0.0698146584,
         0.0698146584, 0.0698146584, 0.0698146584, 0.0698146584, 0.0698146584 /* <-- 10*/, 0.0630151648, 0.0526654164,
         0.0402754482, 0.0292988928, 0.0194384503, 0.0122016783, 0.007207042, 0.004003637, 0.0020278322, 0.0010739954,
         0.0004595759, 0.0002229748, 0.0001028162, 4.58337152809607E-05 /* <-- 24 */};
   std::vector<double> result(25);
   double s = 0.0;
   for (int npu = 0; npu < 25; ++npu) {
      double npu_estimated = data_npu_estimated->GetBinContent(data_npu_estimated->GetXaxis()->FindBin(npu));
      result[npu] = npu_estimated / npu_probs[npu];
      s += npu_estimated;
   }
   // normalize weights such that the total sum of weights over thw whole sample is 1.0, i.e., sum_i  result[i] * npu_probs[i] should be 1.0 (!)
   for (int npu = 0; npu < 25; ++npu) {
      result[npu] /= s;
   }
   return result;
}

//define this as a plug-in
DEFINE_FWK_MODULE( WeightProducer);
