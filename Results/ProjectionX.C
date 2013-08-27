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
vector<unsigned int> FirstValues;
vector<unsigned int> LastValues;

vector<TString> Selections;
vector<TString> SelectionLabels;

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
int ProjectionX()
{
  TFile* WJetsHT = new TFile("WJetsHT.root",      "READ");
  //TFile* TTJets  = new TFile("TTJetsFall11.root", "READ");
  TFile* TTJets  = new TFile("Test.root", "READ");

  //-------------------------------------------------------------------------------------------------------------------
  // addSample(TFile* file, TString sample, TString name)
  //-------------------------------------------------------------------------------------------------------------------

  addSample(WJetsHT, "WJetsHT", "W+Jets");
  addSample(TTJets,  "TTJets",  "t#bar{t}+Jets");

  //-------------------------------------------------------------------------------
  // addHistogram
  //-------------------------------------------------------------------------------

  addHistogram("HT_YMET", "H_{T} [GeV]", 360, 1000);
  
  //-------------------------------------------------------------------------------
  // addSelectionStep(TString step, TString selectionLabel)
  //-------------------------------------------------------------------------------
 
  addSelectionStep("analyzeSUSY1e_leptonSelection", "lepton selection");
  addSelectionStep("analyzeSUSY1e_jetSelection",    "jet selection");

  //-------------------------------------------------------------------------------
  // addBin(int firstBin, int lastBin, TString binLabel, int binColor, int marker
  //-------------------------------------------------------------------------------

  addBin(8,  12,  "#kern[0]{3.5} < Y_{MET} < 6",   2, 22);
  addBin(13, 20,  "#kern[1]{6} < Y_{MET} < 10",    4, 23);
  addBin(21, -1,  "10 < Y_{MET}",                  1, 20);

  //-------------------------------------------------------------------------------
  // Set style 
  //-------------------------------------------------------------------------------

  setTDRStyle();
  
  //-------------------------------------------------------------------------------
  // Plot
  //-------------------------------------------------------------------------------

  for(int fdx=0; fdx<(int)Files.size(); ++fdx)
    {
      for(int hdx=0; hdx<(int)Histograms.size(); ++hdx)
	{ 
	  std::cout << "\n" << Histograms[hdx] << std::endl;
	  std::cout << "-----------------------" << std::endl;
	  
	  for(int sdx=0; sdx<(int)Selections.size(); ++sdx)
	    {
	      std::cout << Selections[sdx] << "_" << Histograms[hdx] << std::endl;
	      
	      TCanvas *canvas = new TCanvas(Selections[sdx]+"_"+Histograms[hdx]+"_"+Samples[fdx],Selections[sdx]+"_"+Histograms[hdx]+"_"+Samples[fdx], 1);
	      
	      TLegend *leg = new TLegend(.55,.62,.95,.93);
	      leg->SetTextFont(42);
	      leg->SetTextSize(0.05);
	      leg->SetFillColor(0);
	      leg->SetLineColor(1);
	      leg->SetShadowColor(0);
	      
	      TPaveText *label = new TPaveText(0.14,0.94,0.99,1.,"NDC");
	      label->SetFillColor(0);
	      label->SetTextFont(42);
	      label->SetTextSize(0.043);
	      label->SetBorderSize(0);
	      label->SetTextAlign(12);
	      TText *text=label->AddText("Simulation, #sqrt{s} = 7 TeV, muon channel");
	      
	      TH2F* Hist = (TH2F*)Files[fdx]->Get(Selections[sdx]+"/"+Histograms[hdx]);
	      
	      for(int bin=0; bin<(int)FirstBins.size(); ++bin)
		{
		  std::cout << "bins " << FirstBins[bin] << " - " << LastBins[bin] << std::endl;
		  
		  // create projection
		  TH1F* Projection = (TH1F*)Hist->ProjectionX(Histograms[hdx], FirstBins[bin], LastBins[bin],"");
		  
		  // edit projection
		  Projection->SetTitle("");
		  Projection->GetXaxis()->SetTitle(XLabels[hdx]);
		  Projection->GetXaxis()->SetTitleOffset(1.2);
		  Projection->GetXaxis()->SetTitleSize(0.05);
		  Projection->GetXaxis()->SetTitleFont(42);
		  Projection->GetYaxis()->SetTitleSize(0.05);
		  Projection->GetYaxis()->SetTitleFont(42);
		  
		  Projection->GetYaxis()->SetTitleOffset(1.4);
		  Projection->GetXaxis()->SetRangeUser(FirstValues[hdx],LastValues[hdx]);
		  Projection->GetYaxis()->SetTitle("a.u.");
		  Projection->SetLineColor(BinColors[bin]);
		  Projection->SetLineWidth(2);
		  Projection->GetYaxis()->SetLabelFont(42);
		  Projection->GetXaxis()->SetLabelFont(42);
		  Projection->Scale(1/Projection->Integral(9,24));
		  Projection->SetMarkerStyle(MarkerStyles[bin]);
		  Projection->SetMarkerColor(BinColors[bin]);
		  leg->AddEntry(Projection->Clone(),BinLabels[bin],"l P");
		  
		  if(bin == 0) Projection->DrawCopy();
		  else Projection->DrawCopy("same");
		}
	      leg->Draw();
	      label->Draw();
	      //canvas->SetLogy();
	      canvas->SaveAs(Selections[sdx]+"_"+Histograms[hdx]+"_ProjectionX_"+Samples[fdx]+".pdf");
	    }
	}
    }
}
