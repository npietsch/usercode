#include <vector>
#include "TFile.h"
#include "TH1.h"
#include "TH2.h"
#include "TProfile2D.h"
#include "TCanvas.h"
#include "TStyle.h"
#include "TLegend.h"
#include "TPaveText.h"

int Correlation()
{
  // Define file
  TFile* TTJets    = new TFile("Bjets.root" , "READ");

  // Read from file
  TH2F* HT_MET=(TH2F*)TTJets->Get("analyzeTtGenEvent_noCuts_1m/HT_MET");

  TCanvas *canvas =new TCanvas("c1","c1",1);

  TProfile2D* HT=(TProfile2D*)HT_MET->ProfileX();

  HT->Draw("");

}
