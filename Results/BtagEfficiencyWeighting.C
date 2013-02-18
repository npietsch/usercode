#include <vector>
#include <iostream>
#include <bitset>
#include <vector>
#include <fstream>
#include "TFile.h"
#include "TH1.h"
#include "TH2.h"
#include "TF1.h"
#include "TCanvas.h"
#include "TStyle.h"
#include "TLegend.h"
#include "TPaveText.h"
#include "TDRStyle.h"

vector<TFile*> Files;
vector<TString> Labels;
vector<unsigned int> SampleColors;
vector<unsigned int> MarkerStyles;
vector<double> MarkerSizes;
vector<unsigned int> FitStyles;
vector<TString> Names;

vector<TString> Steps;
vector<unsigned int> LineColors;
vector<TString> SelectionNames;

vector<TH1F*> Histograms;

// function addSample
void addSample(TFile* sample, TString label, int lc, int ms, double msize, int fs, TString Name);

void addSample(TFile* sample, TString label, int lc, int ms, double msize, int fs, TString Name)
{
  Files.push_back(sample);
  Labels.push_back(label);
  SampleColors.push_back(lc);
  MarkerStyles.push_back(ms);
  MarkerSizes.push_back(msize);
  FitStyles.push_back(fs);
  Names.push_back(Name);
}

int BtagEfficiencyWeighting()
{
  //-----------------------------------------------------
  // Define samples
  //-----------------------------------------------------

  TFile* TTJets    = new TFile("TTJetsFall11.root",   "READ");
  TFile* WJetsHT   = new TFile("WJetsHT.root",        "READ");
  TFile* SingleTop = new TFile("SingleTop.root",      "READ");

  TFile* ZJets     = new TFile("ZJets.root",          "READ");
  TFile* QCD       = new TFile("QCD.root",            "READ");

  //TFile* LM3       = new TFile("LM3.root",            "READ");
  //TFile* LM8       = new TFile("LM8.root",            "READ");
  //TFile* LM13      = new TFile("LM13.root",           "READ");

  //----------------------------------------------------------------------------------
  // addSample(TFile* sample, TString label, int lc, int ms, double msize, int fs);
  //----------------------------------------------------------------------------------

  addSample(TTJets,    "t#bar{t}+Jets", kRed+2,   21, 1.1, 7, "TTJets");
  addSample(SingleTop, "Single Top",    kRed,     22, 1.4, 7, "SingleTop");
  addSample(WJetsHT,   "W+Jets",        1,        23, 1.4, 7, "WJetsHT");

  addSample(ZJets,     "Z+Jets",        kGreen+2, 21, 0.9, 7, "ZJets");
  addSample(QCD,       "QCD",           kBlue,    21, 0.9, 7, "QCD");

//   addSample(LM3,  "LM3",  kRed,     20, 1.1, 7);
//   addSample(LM8,  "LM8",  kBlue,    21, 0.9, 7);
//   addSample(LM13, "LM13", kGreen+2, 22, 1.2, 7);

  //-----------------------------------------------------
  // set Style
  //-----------------------------------------------------

  setTDRStyle();
 
  //-----------------------------------------------------
  // Make plots
  //-----------------------------------------------------

  // loop over files
  for(int f=0; f<(int)Files.size(); ++f)
    {
      std::cout << "File: " << Labels[f] <<  std::endl;
      
      // Define canvas, legend and labels
      TCanvas *canvas =new TCanvas(Labels[f],Labels[f],1);
      
      TLegend *leg = new TLegend(.57,.66,.92,.90);
      leg->SetTextFont(42);
      leg->SetTextSize(0.06);
      leg->SetFillColor(0);
      leg->SetLineColor(1);
      leg->SetShadowColor(0);
      leg->SetLineColor(1);
      leg->AddEntry((TObject*)0, Labels[f], "");

      TPaveText *label = new TPaveText(0.22,0.94,0.99,1.,"NDC");
      label->SetFillColor(0);
      label->SetTextFont(42);
      label->SetTextSize(0.043);
      label->SetBorderSize(0);
      label->SetTextAlign(12);
      TText *text=label->AddText("Simulation, #sqrt{s} = 7 TeV, muon channel");
      
      //--------------------------------------
      // Define and draw b-tags histogram
      //--------------------------------------

      TH1F* cuts_=(TH1F*)Files[f]->Get("monitorBtagWeightingMu/nBjets_noWgt");

      // Title
      cuts_->SetTitle("");

      // Line color, style, and width
      cuts_->SetLineColor(4);
      //cuts_->SetLineColor(SampleColors[f]);
      cuts_->SetLineStyle(1);
      cuts_->SetLineWidth(1);

      // Axes
      cuts_->GetXaxis()->SetTitle("Number of b-jets");
      cuts_->SetNdivisions(5, "X");
      cuts_->GetXaxis()->SetTitleSize(0.05);
      cuts_->GetXaxis()->SetTitleFont(42);
      cuts_->GetXaxis()->SetTitleOffset(1.2);
      
      cuts_->GetYaxis()->SetTitle("events");
      cuts_->SetNdivisions(505, "Y");
      cuts_->GetYaxis()->SetTitleOffset(1.4);
      cuts_->GetYaxis()->SetTitleSize(0.05);
      cuts_->GetYaxis()->SetTitleFont(42);

      // Labels
      cuts_->SetLabelColor(1, "XYZ");
      cuts_->SetLabelFont(42, "XYZ");
      cuts_->SetLabelOffset(0.007, "XYZ");
      cuts_->SetLabelSize(0.04, "XYZ");

      // Define marker
      cuts_->SetMarkerStyle(22);
      cuts_->SetMarkerColor(4);
      //cuts_->SetMarkerColor(SampleColors[f]);
      cuts_->SetMarkerSize(1.4);
      leg->AddEntry(cuts_, "w/ cuts" ,"l P");    

      // draw histogram
      cuts_->Draw("l P");

      //--------------------------------------
      // Define and weights histogram
      //--------------------------------------
      
      TH1F* weights_=(TH1F*)Files[f]->Get("monitorBtagWeightingMu/btagWeights_noWgt");
      
      // define shifts of markers in x direction
      double shift_=0.12;
      
      // define int nBins and array xbins and xbins2
      Int_t nBins=weights_->GetNbinsX();
      double xbins[5];
      double xbins2[5];

      // fill arrays xbins and xbins2
      double xbin0=weights_->GetBinLowEdge(1);
      xbins[0] =xbin0;
      xbins2[0]=xbin0;

      double ibinX=0;
      for(int xbin=1; xbin<weights_->GetNbinsX(); ++xbin)
	{
	  ibinX=ibinX+1;
	  
	  xbins[xbin] =ibinX-0.5;
	  xbins2[xbin]=ibinX-0.5+shift_;
	}

      xbins[4]=4;
      xbins2[4]=4;

      // define new histograms Tmp_ and Tmp2_
      char Tmp [70];
      char Tmp2 [70];
      sprintf(Tmp,"%i",    f);
      sprintf(Tmp2,"%i_2", f);
      TH1F* Tmp_ =new TH1F(Tmp,  Tmp,  nBins, xbins );
      TH1F* Tmp2_=new TH1F(Tmp2, Tmp2, nBins, xbins2);

      // fill histogramw Tmp_ and Tmp2_
      for(int xbin=0; xbin<Tmp_->GetNbinsX()+1; ++xbin)
	{	  
	  Tmp_->SetBinContent(xbin,weights_->GetBinContent(xbin));
	  Tmp_->SetBinError(xbin,0.0000001);

	  Tmp2_->SetBinContent(xbin,weights_->GetBinContent(xbin));
	  Tmp2_->SetBinError(xbin,weights_->GetBinError(xbin));
	}
      
      // Draw x-errors
      Tmp_->SetLineColor(2);
      //Tmp_->SetLineColor(SampleColors[f]);
      Tmp_->SetLineWidth(2);
      Tmp_->SetLineStyle(7);
      Tmp_->Draw("same");
      
      // Draw markers
      Tmp2_->SetLineColor(2);
      //Tmp2_->SetLineColor(SampleColors[f]);
      Tmp2_->SetLineWidth(2);
      Tmp2_->SetLineStyle(7);
      Tmp2_->SetMarkerStyle(21);
      Tmp2_->SetMarkerColor(2);
      //Tmp2_->SetMarkerColor(SampleColors[f]);
      Tmp2_->SetMarkerSize(1.1);
      Tmp2_->Draw("same E x0");
      leg->AddEntry(Tmp2_, "w/ weights" ,"l P");

      leg->Draw();
      label->Draw();
  
      canvas->SaveAs("BtagEfficiencyWeighting_"+Names[f]+"_Mu.pdf");
    }


  return 0;
}
