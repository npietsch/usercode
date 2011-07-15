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

int Shape2()
{

  //Files.push_back (new TFile("LM9.root", "READ"));
  Files.push_back (new TFile("Bjets.root", "READ"));

//   TH1F* hist1=(TH1F*)Files[0]->Get("analyzeEventTopology1l_mediumTCHE_3/Jets3_dPhiLepMETMin");
//   TH1F* hist2=(TH1F*)Files[0]->Get("analyzeEventTopology1l_mediumTCHE_3/Jets4_dPhiLepMETMin");
//   TH1F* hist3=(TH1F*)Files[0]->Get("analyzeEventTopology1l_mediumTCHE_3/Jets5_dPhiLepMETMin");
//   TH1F* hist4=(TH1F*)Files[0]->Get("analyzeEventTopology1l_mediumTCHE_3/Jets6_dPhiLepMETMin");
//   TH1F* hist5=(TH1F*)Files[0]->Get("analyzeEventTopology1l_mediumTCHE_3/Jets78_dPhiLepMETMin");
//   TH1F* hist6=(TH1F*)Files[0]->Get("analyzeEventTopology1l_mediumTCHE_3/Jets9_dPhiLepMETMin");

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


//   TH1F* hist1=(TH1F*)Files[0]->Get("analyzeSUSY1l_jetSelection/mW_MET0");
//   TH1F* hist2=(TH1F*)Files[0]->Get("analyzeSUSY1l_jetSelection/mW_MET50");
//   TH1F* hist3=(TH1F*)Files[0]->Get("analyzeSUSY1l_jetSelection/mW_MET100");
//   TH1F* hist4=(TH1F*)Files[0]->Get("analyzeSUSY1l_jetSelection/mW_MET150");
//   TH1F* hist5=(TH1F*)Files[0]->Get("analyzeSUSY1l_jetSelection/mW_MET200");
//   TH1F* hist6=(TH1F*)Files[0]->Get("analyzeSUSY1l_jetSelection/mW_MET250");
//   TH1F* hist7=(TH1F*)Files[0]->Get("analyzeSUSY1l_jetSelection/mW_MET300");

  TH1F* hist1=(TH1F*)Files[0]->Get("analyzeSUSY1l_noCuts/mW_HT300");
  TH1F* hist2=(TH1F*)Files[0]->Get("analyzeSUSY1l_noCuts/mW_HT400");
  TH1F* hist3=(TH1F*)Files[0]->Get("analyzeSUSY1l_noCuts/mW_HT500");
  TH1F* hist4=(TH1F*)Files[0]->Get("analyzeSUSY1l_noCuts/mW_HT600");
  TH1F* hist5=(TH1F*)Files[0]->Get("analyzeSUSY1l_noCuts/mW_HT700");
  TH1F* hist6=(TH1F*)Files[0]->Get("analyzeSUSY1l_noCuts/mW_HT800");
    
  //hist1->SetDefaultSumw2(kTRUE);

//   TH1F* hist1=(TH1F*)Files[0]->Get("analyzeSUSY1l_metSelection/mW_4Jets");
//   TH1F* hist2=(TH1F*)Files[0]->Get("analyzeSUSY1l_metSelection/mW_5Jets");
//   TH1F* hist3=(TH1F*)Files[0]->Get("analyzeSUSY1l_metSelection/mW_6Jets");
//   TH1F* hist4=(TH1F*)Files[0]->Get("analyzeSUSY1l_metSelection/mW_7Jets");
//   TH1F* hist5=(TH1F*)Files[0]->Get("analyzeSUSY1l_metSelection/mW_8Jets");
//   TH1F* hist6=(TH1F*)Files[0]->Get("analyzeSUSY1l_metSelection/mW_9Jets");

  //TH1F* hist1=(TH1F*)Files[0]->Get("analyzeSUSY1l_jetSelection/mW_SigMET0");
  //TH1F* hist2=(TH1F*)Files[0]->Get("analyzeSUSY1l_jetSelection/mW_SigMET2");
  //TH1F* hist3=(TH1F*)Files[0]->Get("analyzeSUSY1l_jetSelection/mW_SigMET4");
  //TH1F* hist4=(TH1F*)Files[0]->Get("analyzeSUSY1l_jetSelection/mW_SigMET6");
  //TH1F* hist5=(TH1F*)Files[0]->Get("analyzeSUSY1l_jetSelection/mW_SigMET9");
  //TH1F* hist6=(TH1F*)Files[0]->Get("analyzeSUSY1l_jetSelection/mW_SigMET12");
  //TH1F* hist7=(TH1F*)Files[0]->Get("analyzeSUSY1l_jetSelection/mW_MET300");

//   TH1F* hist1=(TH1F*)Files[0]->Get("analyzeSUSY2b1l_3/mW_eta05");
//   TH1F* hist2=(TH1F*)Files[0]->Get("analyzeSUSY2b1l_3/mW_eta10");
//   TH1F* hist3=(TH1F*)Files[0]->Get("analyzeSUSY2b1l_3/mW_eta15");
//   TH1F* hist4=(TH1F*)Files[0]->Get("analyzeSUSY2b1l_3/mW_eta20");
//   TH1F* hist5=(TH1F*)Files[0]->Get("analyzeSUSY2b1l_3/mW_eta25");
 
//   TH1F* hist1=(TH1F*)Files[0]->Get("analyzeSUSY1l_leptonSelection/mW_4Jets");
//   TH1F* hist2=(TH1F*)Files[0]->Get("analyzeSUSY1l_leptonSelection/mW_5Jets");
//   TH1F* hist3=(TH1F*)Files[0]->Get("analyzeSUSY1l_leptonSelection/mW_6Jets");
//   TH1F* hist4=(TH1F*)Files[0]->Get("analyzeSUSY1l_leptonSelection/mW_7Jets");
//   TH1F* hist5=(TH1F*)Files[0]->Get("analyzeSUSY1l_leptonSelection/mW_8Jets");
//   TH1F* hist6=(TH1F*)Files[0]->Get("analyzeSUSY1l_leptonSelection/mW_9Jets");

  double hist1Int=hist1->Integral(1,hist1->GetNbinsX());
  double hist2Int=hist2->Integral(1,hist2->GetNbinsX());
  double hist3Int=hist3->Integral(1,hist3->GetNbinsX());
  double hist4Int=hist4->Integral(1,hist4->GetNbinsX());
  double hist5Int=hist5->Integral(1,hist5->GetNbinsX());
  
  hist1->Scale(1/hist1Int);
  hist2->Scale(1/hist2Int);
  hist3->Scale(1/hist3Int);
  hist4->Scale(1/hist4Int);
  hist5->Scale(1/hist5Int);
  
  hist1->SetLineColor(7);
  hist2->SetLineColor(2);
  hist3->SetLineColor(4);
  hist4->SetLineColor(1);
  hist5->SetLineColor(6);
  
  hist1->SetFillColor(7);
  hist2->SetLineWidth(2);
  hist3->SetLineWidth(2);
  hist4->SetLineWidth(2);
  hist5->SetLineWidth(2);

  hist1->SetMaximum(0.1);
  hist1->SetMinimum(0);

  TCanvas *c1 =new TCanvas( "LM9" , "LM9" ,1);
  hist1->Draw("");
  hist2->Draw("same");
  hist3->Draw("same");
  hist4->Draw("same");
  hist5->Draw("same");
  gPad->SetLogz();

  TLegend *leg = new TLegend(.58,.55,.99,.99);
  leg->SetTextFont(42);
  leg->SetFillColor(0);
  leg->SetLineColor(0);

  leg->AddEntry(hist1,"|#eta| < 0.5","l");
  leg->AddEntry(hist2,"0.5 < |#eta| < 1.0 ","l");
  leg->AddEntry(hist3,"1.0 < |#eta| < 1.5 ","l");
  leg->AddEntry(hist4,"1.5 < |#eta| < 2.0 ","l");
  leg->AddEntry(hist5,"2.0 < |#eta| < 2.5 ","l");

  leg->SetFillColor(10);
  leg->Draw("box");

  c1->SaveAs("LM9.pdf");

  return 0;
  
}
