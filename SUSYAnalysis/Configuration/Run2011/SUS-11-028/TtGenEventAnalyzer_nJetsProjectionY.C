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
#include <TDRStyle_TtGenEventAnalyzer.h>

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
void addHistogram(TString name, TString xLabel, int firstValue, int lastValue);

void addHistogram(TString name, TString xLabel, int firstValue, int lastValue)
{
  Histograms.push_back(name);
  XLabels.push_back(xLabel);
  FirstValues.push_back(firstValue);
  LastValues.push_back(lastValue);
}

// add selection step
void addSelectionStep(TString step, TString selectionLabel);

void addSelectionStep(TString step, TString selectionLabel)
{
  Selections.push_back(step);
  SelectionLabels.push_back(selectionLabel);
}

// add bin
void addBin(int firstBin, int lastBin, TString binLabel, int binColor, int marker);

void addBin(int firstBin, int lastBin, TString binLabel, int binColor, int marker)
{
  FirstBins.push_back(firstBin);
  LastBins.push_back(lastBin);
  BinLabels.push_back(binLabel);
  BinColors.push_back(binColor);
  MarkerStyles.push_back(marker);
}

// main function
int TtGenEventAnalyzer_nJetsProjectionY()
{

  //--------------------------------------------------------------
  // Sample
  //--------------------------------------------------------------

  TFile* TTJets = new TFile("TTJetsFall11.root", "READ");
  //TFile* TTJets = new TFile("TTJetsFall11_back.root", "READ");

  //--------------------------------------------------------------
  // addHistogram
  //--------------------------------------------------------------

  //addHistogram("HT_MET",      "HT [GeV]",  "<MET> [GeV]");
  //addHistogram("HT_LepPt",    "HT [GeV]",  "<Lepton p_{T}> [GeV]");

  //addHistogram("HT_YMET",     "HT [GeV]",         "<YMET> [GeV^{1/2}]");
  //addHistogram("HT_LepPtSig", "HT [GeV]",         "<Lepton p_{T} sig> [GeV^{1/2}]");
  //addHistogram("HT_mT",       "HT [GeV]",         "<m_{T}> [GeV]");
  //addHistogram(ls
  //addHistogram("HT_mlb",        "HT [GeV]",       "mlb [GeV]");
  //addHistogram("HT_mLepTop",    "HT [GeV]",       "mLepTop [GeV]");
  //addHistogram("HT_minj3",        "HT [GeV]",  "minj3 [GeV]");

  //addHistogram("YMET_nJets",    "nJets", 0, 12);

  addHistogram("mT_nJets",       "nJets", 0, 12 );
  //addHistogram("pv_nJets",       "nJets", 0, 12 );
  //addHistogram("mlv_nJets_gen",  "nJets", 0, 12 );
  //addHistogram("mlv_nJets_reco", "nJets", 0, 12 );

  //--------------------------------------------------------------
  // addSelectionStep
  //--------------------------------------------------------------

  addSelectionStep("analyzeSUSY1l_leptonSelection_TTJets", "lepton selection");
  //addSelectionStep("analyzeSUSY1l_jetSelection_TTJets",    "jet selection");
  addSelectionStep("analyzeSUSY1l_HTSelection_TTJets",     "HT selection");
  addSelectionStep("analyzeSUSY1l_METSelection_TTJets",    "MET selection");

  //--------------------------------------------------------------
  // addBin
  //--------------------------------------------------------------

//   addBin(7, 10,  "3 <= Y_{MET} < 5",  4, 22);
//   addBin(11, 20, "5 <= Y_{MET} < 10", 1, 23);
//   addBin(21, -1, "Y_{MET} > 10",      2, 20);

  addBin(1,  5,  "m_{T} < 50 GeV",       2, 22);
  addBin(6, 10,  "50 < m_{T} < 100 GeV", 4, 23);
  addBin(11, -1, "m_{T} > 100",          1, 20);
  
//   addBin(1,  5,  "m_{lv} < 50 GeV",       2, 22);
//   addBin(6, 10,  "50 < m_{lv} < 100 GeV", 4, 23);
//   addBin(11, -1, "m_{lv} > 100",          1, 20);
  
//   addBin(1,  5,  "m_{lv} < 50 GeV",       2, 22);
//   addBin(6, 10,  "50 < m_{lv} < 100 GeV", 4, 23);
//   addBin(11, -1, "m_{lv} > 100",          1, 20);

//   addBin(1,  5,  "p_{v} < 50 GeV",       2, 22);
//   addBin(6, 10,  "50 < p_{v} < 100 GeV", 4, 23);
//   addBin(11, -1, "p_{v} > 100",          1, 20);
  
//   addBin(1,  8, "m_{l,b} < 80 GeV",       2, 22);
//   addBin(9, 16, "80 < m_{l,b} < 160 GeV",  4, 23);
//   addBin(17, -1, "m_{l,b} > 160",          1, 20);

//   addBin(1,  12, "m_{3,lep} < 120 GeV",        2, 22);
//   addBin(13, 20, "120 < m_{3,lep} < 200 GeV",  4, 23);
//   addBin(21, -1, "m_{3,lep} > 200",            1, 20);

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
 
	  TLegend *leg = new TLegend(.64,.62,.91,.89);
	  leg->SetTextFont(42);
	  leg->SetFillColor(0);
	  leg->SetLineColor(1);
	  leg->SetShadowColor(0);

	  TH2F* Hist = (TH2F*)TTJets->Get(Selections[sdx]+"/"+Histograms[hdx]);

	  for(int bin=0; bin<(int)FirstBins.size(); ++bin)
	    {
	      std::cout << "bins " << FirstBins[bin] << " - " << LastBins[bin] << std::endl;

	      // create projection
	      TH1F* Projection = (TH1F*)Hist->ProjectionY(Histograms[hdx], FirstBins[bin], LastBins[bin],"");
	      
	      // edit projection
	      Projection->SetTitle("");
	      Projection->GetXaxis()->SetTitle(XLabels[hdx]);
	      Projection->GetXaxis()->SetTitleOffset(1.4);
	      Projection->GetXaxis()->SetRangeUser(FirstValues[hdx],LastValues[hdx]);
	      Projection->GetYaxis()->SetTitle("# events");
	      Projection->SetLineColor(BinColors[bin]);
	      Projection->SetLineWidth(2);
	      Projection->Scale(1/Projection->Integral(4,-1));
	      Projection->SetMarkerStyle(MarkerStyles[bin]);
	      Projection->SetMarkerColor(BinColors[bin]);
	      leg->AddEntry(Projection->Clone(),BinLabels[bin],"l P");

	      if(bin == 0)
		{
		  Projection->SetMaximum(1.2*(Projection->GetMaximum()));
		  Projection->DrawCopy("");
		}
	      else Projection->DrawCopy("same");
	    }
	  leg->Draw();
	  canvas->SetLogy();

	  canvas->SaveAs(Selections[sdx]+"_"+Histograms[hdx]+"_ProjectionY.pdf");
	}
    }

// 	  TCanvas *canvas = new TCanvas(Histograms[hdx],Histograms[hdx],1);

	  
// 	  for(int bin=0; bin<(int)bins.size(); ++bin)
// 	    {
// 	      std::cout << "bin " << bin << std::cout;
	      
// 	      // create projection
// 	      TH2F* Hist = (TH2F*)TTJets->Get(Selections[sdx]+"/"+Histograms[hdx]);
// 	      TH1F* Projection = (TH1F*)Hist->ProjectionX("", bins[bin], bins[bin],"");
	      
// 	      // edit projection
// 	      Projection->SetTitle("");
// 	      Projection->GetXaxis()->SetTitle(XLabels[hdx]);
// 	      Projection->GetXaxis()->SetTitleOffset(1.4);
// 	      Projection->GetXaxis()->SetRangeUser(0,400);
// 	      Projection->GetYaxis()->SetTitle("# events");
// 	      Projection->SetLineColor(LineColors[sdx]);
// 	      Projection->SetLineWidth(2);
// 	      leg->AddEntry(Projection->Clone(),Labels[sdx],"l P");
	      
// 	      if(bin == 0) Projection->DrawCopy();
// 	      else Projection->DrawCopy("same");
	      // }
	  //leg->Draw();
	  // 	  canvas->SetLogy();
	  
	  // 	  canvas->SaveAs(Histograms[hdx]+"_reco.pdf");
	  
}
