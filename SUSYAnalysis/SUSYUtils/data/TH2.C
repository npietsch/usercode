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
#include <TDRStyle.h>
//#include <TDRStyle_Projection.h>

vector<TFile*> Files;
vector<TString> Samples;
vector<TString> Names;

vector<TString> Histograms;
vector<TString> XLabels;
vector<TString> YLabels;
vector<double> LowerValuesX;
vector<double> HigherValuesX;
vector<double> LowerValuesY;
vector<double> HigherValuesY;
vector<TString> HistogramLabels;

vector<TString> Modules;
vector<TString> Selections;
vector<TString> Channels;
vector<TString> SelectionLabels;
vector<TString> ChannelLabels;

vector<unsigned int> FirstBins;
vector<unsigned int> LastBins;
vector<TString> BinLabels;
vector<unsigned int> BinColors;
vector<unsigned int> MarkerStyles;

// addSample
void addSample(TFile* file, TString sample, TString name)
{
  Files.push_back(file);
  Samples.push_back(sample);
  Names.push_back(name);
}

// main function
int TH2()
{

  TFile* TTJets = new TFile("Btag_TTJetsFall11.root",      "READ");
 
  //--------------------------------------------------------------------------------------------------
  // add addSample(TFile* file, TString sample, TString name)
  //--------------------------------------------------------------------------------------------------

  addSample(TTJets, "TTJets", "t#bar{t}+Jets");
  
  //--------------------------------------------------------------------------------------------------
  // Set style 
  //--------------------------------------------------------------------------------------------------

  setTDRStyle();
  tdrStyle->SetPadLeftMargin(0.09);
  tdrStyle->SetPadRightMargin(0.15);
  tdrStyle->SetPadTopMargin(0.1);
  tdrStyle->SetPadBottomMargin(0.18);
  tdrStyle->SetPalette(1);
  tdrStyle->SetCanvasDefH(400);
  tdrStyle->SetCanvasDefW(800);

  //--------------------------------------------------------------------------------------------------
  // Plot
  //--------------------------------------------------------------------------------------------------

  for(int fdx=0; fdx<(int)Files.size(); ++fdx)
    {
      std::cout << Samples[fdx] << std::endl;

      TCanvas *canvas = new TCanvas(Samples[fdx],Samples[fdx], 1);
      
      //canvas->SetLogz();

      TH2F* MuTag_ = (TH2F*)Files[fdx]->Get("bTagEffRA4bMuTCHEM/NumBJetsTaggedPtEta");
      TH2F* ElTag_ = (TH2F*)Files[fdx]->Get("bTagEffRA4bElTCHEM/NumBJetsTaggedPtEta");

      MuTag_->Add(ElTag_);

      TH2F* MuAll_ = (TH2F*)Files[fdx]->Get("bTagEffRA4bMuTCHEM/NumBJetsPtEta");
      TH2F* ElAll_ = (TH2F*)Files[fdx]->Get("bTagEffRA4bElTCHEM/NumBJetsPtEta");

      MuAll_->Add(ElAll_);

      MuTag_->Divide(MuAll_);

      MuTag_->SetTitle("");

      // Axes
      MuTag_->GetXaxis()->SetTitle("b-jet p_{T} [GeV]");
      MuTag_->GetXaxis()->SetTitleSize(0.07);
      MuTag_->GetXaxis()->SetTitleFont(42);
      MuTag_->GetXaxis()->SetTitleOffset(1.2);
      
      MuTag_->GetYaxis()->SetTitle("b-jet |#eta|");
      MuTag_->GetYaxis()->SetTitleOffset(0.6);
      MuTag_->GetYaxis()->SetTitleSize(0.07);
      MuTag_->GetYaxis()->SetTitleFont(42);
      MuTag_->GetYaxis()->SetRangeUser(0,2.4);
      
      MuTag_->GetZaxis()->SetTitle("b-tag efficiency");
      MuTag_->GetZaxis()->SetTitleOffset(0.7);
      MuTag_->GetZaxis()->SetTitleSize(0.07);
      MuTag_->GetZaxis()->SetTitleFont(42);
  
      MuTag_->SetMinimum(0.5);
      MuTag_->SetMaximum(0.8);
      
      // Labels
      MuTag_->SetLabelColor(1, "XYZ");
      MuTag_->SetLabelFont(62, "XYZ");
      MuTag_->SetLabelOffset(0.007, "XYZ");
      MuTag_->SetLabelSize(0.05, "XYZ");

      // label
      TPaveText *label = new TPaveText(0.06,0.94,0.99,1.,"NDC");
      label->SetFillColor(0);
      label->SetTextFont(42);
      label->SetTextSize(0.07);
      label->SetBorderSize(0);
      label->SetTextAlign(12);
      TText *text=label->AddText(Names[fdx]+" Simulation, #sqrt{s} = 7 TeV");
      
      MuTag_->Draw("colz");
      label->Draw("same");

      canvas->SaveAs("BtagEfficiency.pdf");
    }
}

