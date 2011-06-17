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

int PU()
{

  Files.push_back (new TFile("Electron.root", "READ"));

  TH1F* hist1=(TH1F*)Files[0]->Get("analyzeBjets1e_HTSelection/nMediumBjetsTrackHighEff1pv");
  TH1F* hist2=(TH1F*)Files[0]->Get("analyzeBjets1e_HTSelection/nMediumBjetsTrackHighEff2pv");
  TH1F* hist3=(TH1F*)Files[0]->Get("analyzeBjets1e_HTSelection/nMediumBjetsTrackHighEff3pv");
  TH1F* hist4=(TH1F*)Files[0]->Get("analyzeBjets1e_HTSelection/nMediumBjetsTrackHighEff4pv");
  TH1F* hist5=(TH1F*)Files[0]->Get("analyzeBjets1e_HTSelection/nMediumBjetsTrackHighEff5pv");

  double hist1Int=hist1->Integral(1,hist1->GetNbinsX());
  double hist2Int=hist2->Integral(1,hist2->GetNbinsX());
  double hist3Int=hist3->Integral(1,hist3->GetNbinsX());
  double hist4Int=hist4->Integral(1,hist4->GetNbinsX());
  double hist5Int=hist5->Integral(1,hist5->GetNbinsX());

  hist1->GetXaxis()->SetRangeUser(0,4);

  hist1->Scale(1/hist1Int);
  hist2->Scale(1/hist2Int);
  hist3->Scale(1/hist3Int);
  hist4->Scale(1/hist4Int);
  hist5->Scale(1/hist5Int);

  hist1->SetLineColor(1);
  hist2->SetLineColor(7);
  hist3->SetLineColor(2);
  hist4->SetLineColor(4);
  hist5->SetLineColor(6);

  hist1->SetMaximum(0.6);

  TCanvas *c1 =new TCanvas( "PU" , "PU" ,1);
  hist1->Draw("");
  hist2->Draw("same");
  hist3->Draw("same");
  hist4->Draw("same");
  hist5->Draw("same");
  gPad->SetLogz();

  TLegend *leg = new TLegend(.58,.45,.99,.99);
  leg->SetTextFont(42);
  leg->SetFillColor(0);
  leg->SetLineColor(0);

  leg->AddEntry(hist1,"1 pv" ,"l");
  leg->AddEntry(hist2,"2-3 pv" ,"l");
  leg->AddEntry(hist3,"4-6 pv" ,"l");
  leg->AddEntry(hist4,"7-9 pv" ,"l");
  leg->AddEntry(hist5,">10 pv" ,"l");

  leg->SetFillColor(10);
  leg->Draw("box");

  c1->SaveAs("nBjets_MediumTCHE_PU.pdf");

  return 0;
  
}
