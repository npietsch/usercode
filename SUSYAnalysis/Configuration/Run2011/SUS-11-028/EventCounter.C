#include <vector>
#include <iostream>
#include <bitset>
#include <fstream>
#include "TFile.h"
#include "TH1.h"
#include "TH2.h"
#include "TProfile2D.h"
#include "TF1.h"
#include "TCanvas.h"
#include "TStyle.h"
#include "TLegend.h"
#include "TPaveText.h"
#include <TDRStyle_TtGenEventAnalyzer.h>

std::vector<TString> Selections;

// main function
int EventCounter()
{
  TFile* TTJets = new TFile("TTJetsFall11.root", "READ");

  Selections.push_back("leptonSelection_SemiLep");
//   Selections.push_back("jetSelection_SemiLep");
//   Selections.push_back("HTSelection_SemiLep");
//   Selections.push_back("METSelection_SemiLep");
  
  Selections.push_back("leptonSelection_DiLep");
//   Selections.push_back("jetSelection_DiLep");
//   Selections.push_back("HTSelection_DiLep");
//   Selections.push_back("METSelection_DiLep");

  Selections.push_back("leptonSelection_FullHad");
//   Selections.push_back("jetSelection_FullHad");
//   Selections.push_back("HTSelection_FullHad");
//   Selections.push_back("METSelection_FullHad");

  Selections.push_back("leptonSelection_Tau");
//   Selections.push_back("jetSelection_Tau");
//   Selections.push_back("HTSelection_Tau");
//   Selections.push_back("METSelection_Tau");

  for(int sel=0; sel<(int)Selections.size(); ++sel)
    { 
      
      TH1F* MuonHist     = (TH1F*)TTJets->Get("analyzeSUSY1m_"+Selections[sel]+"/nJets");
      TH1F* ElectronHist = (TH1F*)TTJets->Get("analyzeSUSY1e_"+Selections[sel]+"/nJets");

      std::cout << Selections[sel] << ": " << ElectronHist->Integral(1,-1)+MuonHist->Integral(4,-1)  <<std::endl;
    }
}
