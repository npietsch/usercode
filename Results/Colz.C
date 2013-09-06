#include <vector>
#include <iostream>
#include <bitset>
#include <vector>
#include <fstream>
#include "TFile.h"
#include "TH1.h"
#include "TCanvas.h"
#include "TDRStyle.h"
#include "TLegend.h"

vector<TFile*> Files;

int Colz()
{

  Files.push_back (new TFile("SemiLepElMuTTJets_Correlation.root", "READ"));

  TH1F* Hist1=(TH1F*)Files[0]->Get("analyzeCorrelation1m_jetSelection/NuPt_fakeMET");
  TH1F* Hist2=(TH1F*)Files[0]->Get("analyzeCorrelation1e_jetSelection/NuPt_fakeMET");

  Hist1->Add(Hist2);

  TCanvas *c1 =new TCanvas("Test", "Test", 1);

  setTDRStyle();

  tdrStyle->SetPalette(1);

  Hist1->GetXaxis()->SetRangeUser(0,500);
  Hist1->GetYaxis()->SetRangeUser(0,500);

  Hist1->Draw("colz");

  c1->SaveAs("MET.pdf"); 
}
