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
  //addHistogram("HT_mlb",        "HT [GeV]",       "mlb [GeV]");
  //addHistogram("HT_mLepTop",    "HT [GeV]",       "mLepTop [GeV]");
  //addHistogram("HT_minj3",        "HT [GeV]",  "minj3 [GeV]");

  addHistogram("YMET_nJets",    "nJets", 0, 12);
  //addHistogram("mT_nJets",        "nJets",      0, 12);
  //addHistogram("mlb_nJets",     "nJets",        0, 12);
  //addHistogram("mLepTop_nJets", "nJets",    0, 400);

  //addHistogram("minj3_nJets",   "minj3 [GeV]");

  //addHistogram("HT_MET_acceptance",      "HT [GeV]",  "<MET> [GeV]");
  //addHistogram("HT_LepPt_acceptance",    "HT [GeV]",  "<Lepton p_{T}> [GeV]");
  //addHistogram("HT_YMET_acceptance",     "HT [GeV]",  "<YMET> [GeV^{1/2}]");
  //addHistogram("HT_LepPtSig_acceptance", "HT [GeV]",  "<Lepton p_{T} sig> [GeV^{1/2}]");
  //addHistogram("HT_mT_acceptance",       "HT [GeV]",  "<m_{T}> [GeV]");

//    addHistogram("qScale_MET", "genEvtInfoHandle->qScale()",  "<MET> [GeV]");
//    addHistogram("qScale_HT", "genEvtInfoHandle->qScale()",  "<HT> [GeV]");

//    addHistogram("PDFScale_MET", "genEvtInfoHandle->pdf()->scalePDF",  "<MET> [GeV]");
//    addHistogram("PDFScale_HT", "genEvtInfoHandle->pdf()->scalePDF",  "<HT> [GeV]");

//    addHistogram("ttbarMass_MET", "m_{t#bar{t}} [GeV]",  "<MET> [GeV]");
//    addHistogram("ttbarMass_HT",  "m_{t#bar{t}} [GeV]",  "<HT> [GeV]");

  //--------------------------------------------------------------
  // addSelectionStep
  //--------------------------------------------------------------

//   addSelectionStep("analyzeTtGenEvent_noCuts_1l",          "no Cuts",           1);
//   addSelectionStep("analyzeTtGenEvent_leptonSelection_1l", "lepton selection",  4);
//   addSelectionStep("analyzeTtGenEvent_jetSelection_1l",    "jet selection",     8);
//   addSelectionStep("analyzeTtGenEvent_HTSelection_1l",    "HT selection",      2);
//   addSelectionStep("analyzeTtGenEvent_metSelection_1l",     "MET selection",     kRed+2);
  
  //addSelectionStep("analyzeSUSY_noCuts_1l",          "no Cuts");
  addSelectionStep("analyzeSUSY_leptonSelection_1l", "lepton selection");
  //addSelectionStep("analyzeSUSY_jetSelection_1l",    "jet selection");
  addSelectionStep("analyzeSUSY_HTSelection_1l",     "HT selection");
  addSelectionStep("analyzeSUSY_metSelection_1l",    "MET selection");
  addSelectionStep("analyzeSUSY_metSelection_1l_noHT","MET selection");
 
//   addSelectionStep("analyzeSUSY_noCuts_1l_match2",          "no Cuts",           1);
//   addSelectionStep("analyzeSUSY_leptonSelection_1l_match2", "lepton selection",  4);
//   addSelectionStep("analyzeSUSY_jetSelection_1l_match2",    "jet selection",     8);
//   addSelectionStep("analyzeSUSY_HTSelection_1l_match2",    "HT selection",      2);
//   addSelectionStep("analyzeSUSY_metSelection_1l_match2",     "MET selection",     kRed+2);

  //--------------------------------------------------------------
  // addBin
  //--------------------------------------------------------------

  addBin(7, 10,  "3 <= Y_{MET} < 5",  4, 22);
  addBin(11, 20, "5 <= Y_{MET} < 10", 1, 23);
  addBin(21, -1, "Y_{MET} > 10",      2, 20);

//   addBin(1,  5, "m_{T} < 50 GeV",       2, 22);
//   addBin(6, 10, "50 < m_{T} < 100 GeV", 4, 23);
//   addBin(11, -1, "m_{T} > 100",          1, 20);

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
	  //canvas->SetLogy();

	  canvas->SaveAs(Selections[sdx]+"_"+Histograms[hdx]+"_Y.pdf");
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
