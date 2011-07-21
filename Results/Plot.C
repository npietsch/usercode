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

int Plot()
{
  Files.push_back (new TFile("ElectronHad.root", "READ"));
  Files.push_back (new TFile("MuHad.root", "READ")); 
  TH1F* hist1=(TH1F*)Files[0]->Get("analyzeSUSY3b1e_3/JetsEt_TightA");
  TH1F* hist2=(TH1F*)Files[0]->Get("analyzeSUSY3b1e_3/JetsEt_TightB");
  TH1F* hist3=(TH1F*)Files[0]->Get("analyzeSUSY3b1e_3/JetsEt_TightC");
  TH1F* hist4=(TH1F*)Files[0]->Get("analyzeSUSY3b1e_3/JetsEt_TightD");

  TH1F* hist1a=(TH1F*)Files[1]->Get("analyzeSUSY3b1m_3/JetsEt_TightA");
  TH1F* hist2a=(TH1F*)Files[1]->Get("analyzeSUSY3b1m_3/JetsEt_TightB");
  TH1F* hist3a=(TH1F*)Files[1]->Get("analyzeSUSY3b1m_3/JetsEt_TightC");
  TH1F* hist4a=(TH1F*)Files[1]->Get("analyzeSUSY3b1m_3/JetsEt_TightD");

//   TH1F* hist1=(TH1F*)Files[0]->Get("analyzeSUSY1e_metSelection/JetsEt_TightA");
//   TH1F* hist2=(TH1F*)Files[0]->Get("analyzeSUSY1e_metSelection/JetsEt_TightB");
//   TH1F* hist3=(TH1F*)Files[0]->Get("analyzeSUSY1e_metSelection/JetsEt_TightC");
//   TH1F* hist4=(TH1F*)Files[0]->Get("analyzeSUSY1e_metSelection/JetsEt_TightD");

//   TH1F* hist1a=(TH1F*)Files[1]->Get("analyzeSUSY1m_metSelection/JetsEt_TightA");
//   TH1F* hist2a=(TH1F*)Files[1]->Get("analyzeSUSY1m_metSelection/JetsEt_TightB");
//   TH1F* hist3a=(TH1F*)Files[1]->Get("analyzeSUSY1m_metSelection/JetsEt_TightC");
//   TH1F* hist4a=(TH1F*)Files[1]->Get("analyzeSUSY1m_metSelection/JetsEt_TightD");


  TCanvas *c1 =new TCanvas("1" , "1" ,1);
  hist1->Draw();
  gPad->SetLogy();
  hist1->SetTitle("Electron Had 3 btags A");
  hist1->GetXaxis()->SetTitle("E_{T} jets [GeV]");
  hist1->GetXaxis()->CenterTitle();
  hist1->GetYaxis()->SetTitle("# events");
  hist1->GetYaxis()->CenterTitle();
  hist1->GetXaxis()->SetRangeUser(0, 500);
  c1->SaveAs("Electron_3btagsA.pdf");
  TCanvas *c2 =new TCanvas("2" , "2" ,1);
  hist2->Draw();
  gPad->SetLogy();
  hist2->SetTitle("Electron Had 3 btags B");
  hist2->GetXaxis()->SetTitle("E_{T} jets [GeV]");
  hist2->GetXaxis()->CenterTitle();
  hist2->GetYaxis()->SetTitle("# events");
  hist2->GetYaxis()->CenterTitle();
  hist2->GetXaxis()->SetRangeUser(0, 500);
  c2->SaveAs("Electron_3btagsB.pdf");
  TCanvas *c3 =new TCanvas("3" , "3" ,1);
  hist3->Draw();
  gPad->SetLogy();
  hist3->SetTitle("Electron Had 3 btags C");
  hist3->GetXaxis()->SetTitle("E_{T} jets [GeV]");
  hist3->GetXaxis()->CenterTitle();
  hist3->GetYaxis()->SetTitle("# events");
  hist3->GetYaxis()->CenterTitle();
  hist3->GetXaxis()->SetRangeUser(0, 500);
  c3->SaveAs("Electron_3btagsC.pdf");
  TCanvas *c4 =new TCanvas("4" , "4" ,1);
  hist4->Draw();
  gPad->SetLogy();
  hist4->SetTitle("Electron Had 2 btag D");
  hist4->GetXaxis()->SetTitle("E_{T} jets [GeV]");
  hist4->GetXaxis()->CenterTitle();
  hist4->GetYaxis()->SetTitle("# events");
  hist4->GetYaxis()->CenterTitle();
  hist4->GetXaxis()->SetRangeUser(0, 500);
  c4->SaveAs("Electron_3btagsD.pdf");

  TCanvas *c1a =new TCanvas("5" , "5" ,1);
  hist1->Draw();
  gPad->SetLogy();
  hist1a->SetTitle("Muon Had 3 btags A");
  hist1a->GetXaxis()->SetTitle("E_{T} jets [GeV]");
  hist1a->GetXaxis()->CenterTitle();
  hist1a->GetYaxis()->SetTitle("# events");
  hist1a->GetYaxis()->CenterTitle();
  hist1a->GetXaxis()->SetRangeUser(0, 500);
  c1a->SaveAs("Muon_3btagsA.pdf");
  TCanvas *c2a =new TCanvas("6" , "6" ,1);
  hist2a->Draw();
  gPad->SetLogy();
  hist2a->SetTitle("Muon Had 3 btags B");
  hist2a->GetXaxis()->SetTitle("E_{T} jets [GeV]");
  hist2a->GetXaxis()->CenterTitle();
  hist2a->GetYaxis()->SetTitle("# events");
  hist2a->GetYaxis()->CenterTitle();
  hist2a->GetXaxis()->SetRangeUser(0, 500);
  c2a->SaveAs("Muon_3btagsB.pdf");
  TCanvas *c3a =new TCanvas("7" , "7" ,1);
  hist3a->Draw();
  gPad->SetLogy();
  hist3a->SetTitle("Muon Had 3 btags C");
  hist3a->GetXaxis()->SetTitle("E_{T} jets [GeV]");
  hist3a->GetXaxis()->CenterTitle();
  hist3a->GetYaxis()->SetTitle("# events");
  hist3a->GetYaxis()->CenterTitle();
  hist3a->GetXaxis()->SetRangeUser(0, 500);
  c3a->SaveAs("Muon_3btagsC.pdf");
  TCanvas *c4a =new TCanvas("8" , "8" ,1);
  hist4a->Draw();
  gPad->SetLogy();
  hist4a->SetTitle("Muon Had 3 btags D");
  hist4a->GetXaxis()->SetTitle("E_{T} jets [GeV]");
  hist4a->GetXaxis()->CenterTitle();
  hist4a->GetYaxis()->SetTitle("# events");
  hist4a->GetYaxis()->CenterTitle();
  hist4a->GetXaxis()->SetRangeUser(0, 500);
  c4a->SaveAs("Muon_3btagsD.pdf");

  return 0;
  
}
