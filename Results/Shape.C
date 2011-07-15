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
  Files.push_back (new TFile("TTJets.root", "READ"));
  Files.push_back (new TFile("LM3.root", "READ"));
  Files.push_back (new TFile("LM8.root", "READ"));
  Files.push_back (new TFile("LM9.root", "READ"));

//   TH1F* hist1=(TH1F*)Files[0]->Get("analyzeSUSY1l_jetSelection/nJets");
//   TH1F* hist2=(TH1F*)Files[1]->Get("analyzeSUSY1l_jetSelection/nJets");
//   TH1F* hist3=(TH1F*)Files[2]->Get("analyzeSUSY1l_jetSelection/nJets");
//   TH1F* hist4=(TH1F*)Files[3]->Get("analyzeSUSY1l_jetSelection/nJets");

  TH1F* hist1=(TH1F*)Files[0]->Get("analyzeSUSY1l_HTSelection/nJets");
  TH1F* hist2=(TH1F*)Files[1]->Get("analyzeSUSY1l_HTSelection/nJets");
  TH1F* hist3=(TH1F*)Files[2]->Get("analyzeSUSY1l_HTSelection/nJets");
  TH1F* hist4=(TH1F*)Files[3]->Get("analyzeSUSY1l_HTSelection/nJets");

//   TH1F* hist1=(TH1F*)Files[0]->Get("analyzeSUSY3b1l_1/nJets");
//   TH1F* hist2=(TH1F*)Files[1]->Get("analyzeSUSY3b1l_1/nJets");
//   TH1F* hist3=(TH1F*)Files[2]->Get("analyzeSUSY3b1l_1/nJets");
//   TH1F* hist4=(TH1F*)Files[3]->Get("analyzeSUSY3b1l_1/nJets");


  double hist1Int=hist1->Integral(1,hist1->GetNbinsX());
  double hist2Int=hist2->Integral(1,hist2->GetNbinsX());
  double hist3Int=hist3->Integral(1,hist3->GetNbinsX());
  double hist4Int=hist4->Integral(1,hist4->GetNbinsX());
  //double hist5Int=hist5->Integral(1,hist5->GetNbinsX());
  //double hist6Int=hist6->Integral(1,hist6->GetNbinsX());
  //double hist7Int=hist7->Integral(1,hist7->GetNbinsX());

  hist1->Scale(1/hist1Int);
  hist2->Scale(1/hist2Int);
  hist3->Scale(1/hist3Int);
  hist4->Scale(1/hist4Int);
  //hist5->Scale(1/hist5Int);
  //hist6->Scale(1/hist6Int);
  //hist7->Scale(1/hist7Int);

  hist1->SetLineColor(7);
  hist2->SetLineColor(2);
  hist3->SetLineColor(4);
  hist4->SetLineColor(1);
  //hist5->SetLineColor(6);
  //hist6->SetLineColor(8);
  //hist7->SetLineColor(46);

  hist1->SetFillColor(7);
  hist2->SetLineWidth(3);
  hist3->SetLineWidth(3);
  hist4->SetLineWidth(3);

  hist1->SetMaximum(0.6);
  hist1->SetMinimum(0.001);

  TCanvas *c1 =new TCanvas( "nJets" , "nJets" ,1);
  hist1->Draw("");
  hist2->Draw("same");
  hist3->Draw("same");
  hist4->Draw("same");
  //hist5->Draw("same");
  //hist6->Draw("same");
  //hist7->Draw("same");
  gPad->SetLogy();

  TLegend *leg = new TLegend(.58,.55,.99,.99);
  leg->SetTextFont(42);
  leg->SetFillColor(0);
  leg->SetLineColor(0);

  leg->AddEntry(hist1,"Ttbar" ,"l");
  leg->AddEntry(hist2,"LM3" ,"l");
  leg->AddEntry(hist3,"LM8" ,"l");
  leg->AddEntry(hist4,"LM9" ,"l");
  //leg->AddEntry(hist5," " ,"l");
  //leg->AddEntry(hist6," " ,"l");
  //leg->AddEntry(hist7, " ,"l");

  leg->SetFillColor(10);
  leg->Draw("box");

  c1->SaveAs("nJets_0btags.pdf");

  return 0;
  
}
