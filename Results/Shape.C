#include <vector>
#include <iostream>
#include <bitset>
#include <vector>
#include <fstream>
#include "TFile.h"
#include "TH1.h"
#include "TCanvas.h"
#include "TStyle.h"
#include "TLegend.h"


vector<TFile*> Files;
vector<string> Names;
vector<double> Scales;
vector<unsigned int> Colors;
vector<unsigned int> FillColors;
vector<unsigned int> Styles;

int Shape()
{
  Files.push_back (new TFile("Bjets.root", "READ"));
  Files.push_back (new TFile("Data_PUDist_160404-163869_7TeV_May10ReReco_Collisions11.root", "READ"));

  TH1F* hist1=(TH1F*)Files[0]->Get("analyzeSUSY1m_noCuts/nPU");
  //TH1F* hist2=(TH1F*)Files[0]->Get("analyzeSUSY1m_noCuts/nPVweighted");
  TH1F* hist2=(TH1F*)Files[1]->Get("pileup");

  double hist1Int=hist1->Integral(1,hist1->GetNbinsX());
  double hist2Int=hist2->Integral(1,hist2->GetNbinsX());
 
  hist1->Scale(1/hist1Int);
  hist2->Scale(1/hist2Int);

  hist1->SetLineColor(2);
  hist2->SetLineColor(4);;

  TCanvas *c1 =new TCanvas( "nJets" , "nJets" ,1);
  hist1->Draw("");
  hist2->Draw("same");
  gPad->SetLogy();

  TLegend *leg = new TLegend(.58,.55,.99,.99);
  leg->SetTextFont(42);
  leg->SetFillColor(0);
  leg->SetLineColor(0);

  leg->AddEntry(hist1,"Ttbar weighted" ,"l");
  leg->AddEntry(hist2,"May10 ReReco" ,"l");

  leg->SetFillColor(10);
  leg->Draw("box");

  c1->SaveAs("PU.pdf");

  return 0;
  
}
