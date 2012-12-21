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

// Samples
vector<TFile*> Files;
vector<TString> Labels;
vector<TString> Names;

// Histograms
vector<TString> Histograms;
vector<TString> XLabels;
vector<unsigned int> FirstValues;
vector<unsigned int> LastValues;

// Selections
vector<TString> Selections;
vector<TString> SelectionLabels;

// Bins
vector<unsigned int> FirstBins;
vector<unsigned int> LastBins;
vector<TString> BinLabels;
vector<unsigned int> BinColors;
vector<unsigned int> MarkerStyles;

// add sample
void addSample(TFile* sample, TString label, TString name)
{
  Files.push_back(sample);
  Labels.push_back(label);
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
int TtGenEventAnalyzer_nJetsProjectionX()
{

  //---------------------------------------------------------------------------------
  // Sample
  //---------------------------------------------------------------------------------

  TFile* SemiLep = new TFile("SemiLep.root", "READ");
  TFile* DiLep   = new TFile("DiLep.root", "READ");
  TFile* SingleTop = new TFile("SingleTop.root", "READ");
  TFile* WJetsHT   = new TFile("WJetsHT.root", "READ");

  //---------------------------------------------------------------------------------
  // addSample(TFile* sample, TString label)
  //---------------------------------------------------------------------------------
  
  //addSample(SemiLep, "SemiLep t#bar{t}", "SemiLep");
  addSample(DiLep,   "DiLep t#bar{t}",  "DiLep");
  //addSample(SingleTop, "Single Top", "SingleTop");
  //addSample(WJetsHT,   "W+Jets",     "WJets");

  //---------------------------------------------------------------------------------
  // addHistogram(TString name, TString xLabel, int firstValue, int lastValue)
  //---------------------------------------------------------------------------------

  addHistogram("YMET_nJets",    "YMET [GeV^{1/2}]", 0, 25);
  //addHistogram("mT_nJets",      "m_{T} [GeV]",          0, 300);
  //addHistogram("mlv_nJets_gen", "m_{l#nu}^{gen} [GeV]", 0, 300);
  //addHistogram("mlb_nJets",     "mlb [GeV]",        0, 300);
  //addHistogram("mLepTop_nJets", "mLepTop [GeV]",    0, 400);

  //---------------------------------------------------------------------------------
  // addSelectionStep(TString step, TString selectionLabel)
  //---------------------------------------------------------------------------------

  addSelectionStep("analyzeCorrelation1l", "lepton selection");
  //addSelectionStep("analyzeCorrelation1l_HT400ToInf_MET100ToInf", "lepton selection");
  //addSelectionStep("analyzeCorrelation1l_HT600ToInf_MET150ToInf", "lepton selection");

//   addSelectionStep("analyzeCorrelation1l_YMET10To15", "lepton selection");
//   addSelectionStep("analyzeCorrelation1l_YMET15To20", "lepton selection");
//   addSelectionStep("analyzeCorrelation1l_YMET20To25", "lepton selection");
//   addSelectionStep("analyzeCorrelation1l_YMET25To30", "lepton selection");
//   addSelectionStep("analyzeCorrelation1l_YMET30To35", "lepton selection");
//   addSelectionStep("analyzeCorrelation1l_YMET35To40", "lepton selection");

  //---------------------------------------------------------------------------------
  // addBin(int firstBin, int lastBin, TString binLabel, int binColor, int marker)
  //---------------------------------------------------------------------------------

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

  for(int fdx=0; fdx<(int)Files.size(); ++fdx)
    {
      std::cout << "\n" << Files[fdx] << std::endl;
      
      for(int hdx=0; hdx<(int)Histograms.size(); ++hdx)
	{ 
	  std::cout << "\n" << Histograms[hdx] << std::endl;
	  std::cout << "-----------------------" << std::endl;
	  
	  for(int sdx=0; sdx<(int)Selections.size(); ++sdx)
	    {
	      std::cout << Selections[sdx] << "_" << Histograms[hdx] << std::endl;
	      
	      TCanvas *canvas = new TCanvas(Selections[sdx]+"_"+Histograms[hdx]+"_"+Labels[fdx],Selections[sdx]+"_"+Histograms[hdx]+"_"+Labels[fdx], 1);
	      
	      // legend
	      TLegend *leg = new TLegend(.56,.67,.90,.91);
	      leg->SetTextFont(42);
	      leg->SetTextSize(0.055);
	      leg->SetFillColor(0);
	      leg->SetLineColor(1);
	      leg->SetShadowColor(0);
	      leg->SetLineColor(0);
	      leg->AddEntry((TObject*)0, Labels[fdx], "");
	      
	      // label
	      TPaveText *label = new TPaveText(0.14,0.94,0.99,1.,"NDC");
	      label->SetFillColor(0);
	      label->SetTextFont(42);
	      label->SetTextSize(0.043);
	      label->SetBorderSize(0);
	      label->SetTextAlign(12);
	      TText *text=label->AddText("Simulation, #sqrt{s} = 7 TeV");
	      
	      TH2F* Hist = (TH2F*)Files[fdx]->Get(Selections[sdx]+"/"+Histograms[hdx]);
	      
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
		  
		  Projection->Scale(1/Projection->Integral(4,-1));

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
	      canvas->SaveAs(Selections[sdx]+"_"+Histograms[hdx]+"_"+Names[fdx]+"_ProjectionX_log.pdf");
	    }
	}
    }	  
}
