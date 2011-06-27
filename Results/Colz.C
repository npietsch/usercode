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

int Colz()
{

  Files.push_back (new TFile("TTJets.root", "READ"));

  TH1F* hist1=(TH1F*)Files[0]->Get("analyzeEventTopology1l_mediumTCHE_3/Jets3_dPhiLepMETMin");
  TH1F* hist2=(TH1F*)Files[0]->Get("analyzeEventTopology1l_mediumTCHE_3/Jets4_dPhiLepMETMin");
  TH1F* hist3=(TH1F*)Files[0]->Get("analyzeEventTopology1l_mediumTCHE_3/Jets5_dPhiLepMETMin");
  TH1F* hist4=(TH1F*)Files[0]->Get("analyzeEventTopology1l_mediumTCHE_3/Jets6_dPhiLepMETMin");
  TH1F* hist5=(TH1F*)Files[0]->Get("analyzeEventTopology1l_mediumTCHE_3/Jets78_dPhiLepMETMin");
  TH1F* hist6=(TH1F*)Files[0]->Get("analyzeEventTopology1l_mediumTCHE_3/Jets9_dPhiLepMETMin");

//   TH1F* hist1=(TH1F*)Files[0]->Get("analyzeEventTopology1l_mediumTCHE_3/MET50_dPhiLepMETMin");
//   TH1F* hist2=(TH1F*)Files[0]->Get("analyzeEventTopology1l_mediumTCHE_3/MET100_dPhiLepMETMin");
//   TH1F* hist3=(TH1F*)Files[0]->Get("analyzeEventTopology1l_mediumTCHE_3/MET150_dPhiLepMETMin");
//   TH1F* hist4=(TH1F*)Files[0]->Get("analyzeEventTopology1l_mediumTCHE_3/MET200_dPhiLepMETMin");
//   TH1F* hist5=(TH1F*)Files[0]->Get("analyzeEventTopology1l_mediumTCHE_3/MET250_dPhiLepMETMin");
//   TH1F* hist6=(TH1F*)Files[0]->Get("analyzeEventTopology1l_mediumTCHE_3/MET300_dPhiLepMETMin");

//   TH1F* hist1=(TH1F*)Files[0]->Get("analyzeEventTopology1l_mediumTCHE_3/HT200_dPhiLepMETMin");
//   TH1F* hist2=(TH1F*)Files[0]->Get("analyzeEventTopology1l_mediumTCHE_3/HT300_dPhiLepMETMin");
//   TH1F* hist3=(TH1F*)Files[0]->Get("analyzeEventTopology1l_mediumTCHE_3/HT400_dPhiLepMETMin");
//   TH1F* hist4=(TH1F*)Files[0]->Get("analyzeEventTopology1l_mediumTCHE_3/HT500_dPhiLepMETMin");
//   TH1F* hist5=(TH1F*)Files[0]->Get("analyzeEventTopology1l_mediumTCHE_3/HT600_dPhiLepMETMin");
//   TH1F* hist6=(TH1F*)Files[0]->Get("analyzeEventTopology1l_mediumTCHE_3/HT700_dPhiLepMETMin");

  double hist1Int=hist1->Integral(1,hist1->GetNbinsX());
  double hist2Int=hist2->Integral(1,hist2->GetNbinsX());
  double hist3Int=hist3->Integral(1,hist3->GetNbinsX());
  double hist4Int=hist4->Integral(1,hist4->GetNbinsX());
  double hist5Int=hist5->Integral(1,hist5->GetNbinsX());
  double hist6Int=hist6->Integral(1,hist6->GetNbinsX());

  hist1->Scale(1/hist1Int);
  hist2->Scale(1/hist2Int);
  hist3->Scale(1/hist3Int);
  hist4->Scale(1/hist4Int);
  hist5->Scale(1/hist5Int);
  hist6->Scale(1/hist6Int);

  hist1->SetLineColor(1);
  hist2->SetLineColor(7);
  hist3->SetLineColor(2);
  hist4->SetLineColor(4);
  hist5->SetLineColor(6);
  hist6->SetLineColor(8);

  hist2->SetMaximum(0.15);
  hist2->SetMinimum(0);

  TCanvas *c1 =new TCanvas( "LM3" , "LM3" ,1);
  //hist1->Draw("");
  hist2->Draw("");
  //hist3->Draw("same");
  hist4->Draw("same");
  //hist5->Draw("same");
  hist6->Draw("same");
  gPad->SetLogz();

  TLegend *leg = new TLegend(.58,.55,.99,.99);
  leg->SetTextFont(42);
  leg->SetFillColor(0);
  leg->SetLineColor(0);

  //leg->AddEntry(hist1,"3 Jets" ,"l");
  leg->AddEntry(hist2,"4 Jets" ,"l");
  //leg->AddEntry(hist3,"5 Jets" ,"l");
  leg->AddEntry(hist4,"6 Jets" ,"l");
  //leg->AddEntry(hist5,"7-8 Jets" ,"l");
  leg->AddEntry(hist6,">9 Jets" ,"l");

  leg->SetFillColor(10);
  leg->Draw("box");

  c1->SaveAs("LM3.pdf");

  return 0;
  
}
