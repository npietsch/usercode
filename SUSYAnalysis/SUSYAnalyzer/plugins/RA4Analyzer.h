#ifndef RA4Analyzer_h  
#define RA4Analyzer_h

#include "TH1.h"
#include "TH2.h"

#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/Math/interface/angle.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Electron.h"

class RA4Analyzer : public edm::EDAnalyzer {

 public:
  
  explicit RA4Analyzer(const edm::ParameterSet&);
  ~RA4Analyzer();

 private:

  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
           	

  TH1F* JetsEt_;
  TH1F* JetsEta_;
  TH1F* nJets_;

  TH1F* MuonsPt_;
  TH1F* MuonsEta_;
  TH1F* nMuons_;

  TH1F* ElectronsPt_;
  TH1F* ElectronsEta_;
  TH1F* nElectrons_;

  TH1F* nLeptons_;

  TH1F* dRMuonJet_;
  TH1F* dRElectronJet_;

  edm::InputTag met_;
  edm::InputTag jets_;
  edm::InputTag muons_;
  edm::InputTag electrons_;
/*   edm::InputTag pfMuons_; */

  std::vector<TH1F*> Jet_Et_;
  std::vector<TH1F*> Muon_pt_;
  std::vector<TH1F*> Electron_pt_;

  std::vector<TH1F*> Jet_eta_;
  std::vector<TH1F*> Muon_eta_;
  std::vector<TH1F*> Electron_eta_;

/*   std::vector<TH1F*> dRBadMuonJet_; */
/*   std::vector<TH1F*> BadMuonNrJets_; */
};  

#endif  
