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

vector<TString> Histograms;
vector<TString> XLabels;
vector<unsigned int> FirstValues;
vector<unsigned int> LastValues;

vector<TString> Selections;
vector<TString> SelectionLabels;

vector<unsigned int> FirstBins;
vector<unsigned int> LastBins;
vector<TString> BinLabels;
vector<unsigned int> BinColors;
vector<unsigned int> MarkerStyles;

// add histogram
void addHistogram(TString name, TString xLabel, int firstValue, int lastValue)
{
  Histograms.push_back(name);
  XLabels.push_back(xLabel);
  FirstValues.push_back(firstValue);
  LastValues.push_back(lastValue);
}

// add selection step
void addSelectionStep(TString step, TString selectionLabel)
{
  Selections.push_back(step);
  SelectionLabels.push_back(selectionLabel);
}

// add bin
void addBin(int firstBin, int lastBin, TString binLabel, int binColor, int marker)
{
  FirstBins.push_back(firstBin);
  LastBins.push_back(lastBin);
  BinLabels.push_back(binLabel);
  BinColors.push_back(binColor);
  MarkerStyles.push_back(marker);
}

// main function
int TtGenEventAnalyzer_nJetsProjectionX()
{

  //--------------------------------------------------------------
  // Sample
  //--------------------------------------------------------------

  //TFile* TTJets = new TFile("SemiLepElMu.root", "READ");
  TFile* TTJets = new TFile("SingleTop.root", "READ");
  // TFile* TTJets = new TFile("DiLep.root", "READ");

  //--------------------------------------------------------------
  // addHistogram
  //--------------------------------------------------------------

  //addHistogram("YMET_nJets",    "YMET [GeV^{1/2}]", 0, 25);
  addHistogram("mT_nJets",      "m_{T} [GeV]",      0, 300);
  //addHistogram("mlv_nJets_gen", "m_{l#nu}^{gen} [GeV]",      0, 300);
  //addHistogram("mlb_nJets",     "mlb [GeV]",        0, 300);
  //addHistogram("mLepTop_nJets", "mLepTop [GeV]",    0, 400);

  //--------------------------------------------------------------
  // addSelectionStep
  //--------------------------------------------------------------
  
  addSelectionStep("analyzeCorrelation1l", "lepton selection");

//   addSelectionStep("analyzeCorrelation1l_YMET0To1", "lepton selection");
//   addSelectionStep("analyzeCorrelation1l_YMET1To2", "lepton selection");
//   addSelectionStep("analyzeCorrelation1l_YMET2To3", "lepton selection");
//   addSelectionStep("analyzeCorrelation1l_YMET3To4", "lepton selection");
//   addSelectionStep("analyzeCorrelation1l_YMET4To5", "lepton selection");
//   addSelectionStep("analyzeCorrelation1l_YMET5To6", "lepton selection");

  //--------------------------------------------------------------
  // addBin
  //--------------------------------------------------------------

  //addBin(4, 5,  "3-4 Jets", 2, 22);
  //addBin(6, 7,  "5-6 Jets", 4, 23);
  //addBin(8, -1, "> 7 Jets", 1, 20);

  addBin(4,  5, "3-4 Jets", 2, 22);
  addBin(6,  7, "5-6 Jets", 4, 23);
  addBin(8, -1, ">7 Jets", 1, 20);

  //------------
  // set style 
  //------------ 

  setTDRStyle();

  for(int hdx=0; hdx<(int)Histograms.size(); ++hdx)
    { 
      std::cout << "\n" << Histograms[hdx] << std::endl;
      std::cout << "-----------------------" << std::endl;

      for(int sdx=0; sdx<(int)Selections.size(); ++sdx)
	{
	  std::cout << Selections[sdx] << "_" << Histograms[hdx] << std::endl;
	  
	  TCanvas *canvas = new TCanvas(Selections[sdx]+"_"+Histograms[hdx],Selections[sdx]+"_"+Histograms[hdx], 1);

	  // legend
	  TLegend *leg = new TLegend(.56,.67,.90,.91);
	  leg->SetTextFont(42);
	  leg->SetTextSize(0.055);
	  leg->SetFillColor(0);
	  leg->SetLineColor(1);
	  leg->SetShadowColor(0);
	  leg->SetLineColor(0);
	  leg->AddEntry((TObject*)0, "Semilep. t#bar{t}", "");

	  // label
	  TPaveText *label = new TPaveText(0.14,0.94,0.99,1.,"NDC");
	  label->SetFillColor(0);
	  label->SetTextFont(42);
	  label->SetTextSize(0.043);
	  label->SetBorderSize(0);
	  label->SetTextAlign(12);
	  TText *text=label->AddText("Simulation, #sqrt{s} = 7 TeV");
      
	  TH2F* Hist = (TH2F*)TTJets->Get(Selections[sdx]+"/"+Histograms[hdx]);

	  for(int bin=0; bin<(int)FirstBins.size(); ++bin)
	    {
	      std::cout << "bins " << FirstBins[bin] << " - " << LastBins[bin] << std::endl;

	      // create projection
	      TH1F* Projection = (TH1F*)Hist->ProjectionX(Histograms[hdx], FirstBins[bin], LastBins[bin],"");
	      
	      // titles, scales and ranges
	      Projection->SetTitle("");

	      Projection->GetXaxis()->SetTitle(XLabels[hdx]);
	      Projection->GetXaxis()->SetTitleSize(0.05);
	      Projection->GetYaxis()->SetTitleOffset(1.4);
	      Projection->GetXaxis()->SetRangeUser(FirstValues[hdx],LastValues[hdx]);
	      
	      Projection->GetYaxis()->SetTitle("a.u.");
	      Projection->GetYaxis()->SetTitleSize(0.05);
	      Projection->GetYaxis()->SetTitleSize(0.05);

	      Projection->Scale(1/Projection->Integral(1,-1));

	      // lines
	      Projection->SetLineColor(BinColors[bin]);
	      Projection->SetLineWidth(2);

	      // markers
	      Projection->SetMarkerStyle(MarkerStyles[bin]);
	      Projection->SetMarkerColor(BinColors[bin]);

	      // add entry to legend
	      leg->AddEntry(Projection->Clone(),BinLabels[bin],"l P");

	      if(bin == 0) Projection->DrawCopy();
	      else Projection->DrawCopy("same");
	    }

	  TPaveText *label2 = new TPaveText(0.45,0.38,0.75,0.54,"NDC");
	  label2->SetFillColor(0);
	  label2->SetTextFont(62);
	  label2->SetTextSize(0.07);
	  label2->SetBorderSize(0);
	  label2->SetTextAlign(12);
	  TText *text2=label2->AddText("Own work");
	  TText *text3=label2->AddText("in progress");
	  
	  label->Draw("same");
	  //label2->Draw("same");
	  leg->Draw();

	  canvas->SetLogy();
	  canvas->SaveAs(Selections[sdx]+"_"+Histograms[hdx]+"_ProjectionX_log.pdf");
	}
    }	  
}
