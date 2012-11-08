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
int TtGenEventAnalyzer_nJetsProjectionX()
{

  //--------------------------------------------------------------
  // Sample
  //--------------------------------------------------------------

  TFile* TTJets = new TFile("TTJetsFall11.root", "READ");

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

  //addHistogram("YMET_nJets",    "YMET [GeV^{1/2}]", 0, 25);
  //addHistogram("mT_nJets",      "m_{T} [GeV]",      0, 300);
  //addHistogram("mlb_nJets",     "mlb [GeV]",        0, 300);
  //addHistogram("mLepTop_nJets", "mLepTop [GeV]",    0, 400);

  //addHistogram("pv_nJets",        "p_{#nu}  [GeV]",      0, 600);
  addHistogram("mlv_nJets_gen",   "m_{l#nu} [GeV]",      0, 200);
  //addHistogram("mlv_nJets_reco",  "p_{l#nu} [GeV]",      0, 200);

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

  addSelectionStep("analyzeSUSY1l_leptonSelection_TTJets", "lepton selection");
  //addSelectionStep("analyzeSUSY1l_jetSelection_TTJets",    "jet selection");
  addSelectionStep("analyzeSUSY1l_HTSelection_TTJets",     "HT selection");
  addSelectionStep("analyzeSUSY1l_METSelection_TTJets",    "MET selection");

  //--------------------------------------------------------------
  // addBin
  //--------------------------------------------------------------

  //addBin(4, 5,  "3-4 Jets", 2, 22);
  //addBin(6, 7,  "5-6 Jets", 4, 23);
  //addBin(8, -1, "> 7 Jets", 1, 20);

  addBin(4, 4,  "3 Jets", 2, 22);
  addBin(7, 7,  "6 Jets", 4, 23);
  addBin(9, 9,  "8 Jets", 1, 20);

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
	      TH1F* Projection = (TH1F*)Hist->ProjectionX(Histograms[hdx], FirstBins[bin], LastBins[bin],"");
	      
	      // edit projection
	      Projection->SetTitle("");
	      Projection->GetXaxis()->SetTitle(XLabels[hdx]);
	      Projection->GetXaxis()->SetTitleOffset(1.4);
	      Projection->GetXaxis()->SetRangeUser(FirstValues[hdx],LastValues[hdx]);
	      Projection->GetYaxis()->SetTitle("# events");
	      Projection->SetLineColor(BinColors[bin]);
	      Projection->SetLineWidth(2);
	      Projection->Scale(1/Projection->Integral(1,-1));
	      Projection->SetMarkerStyle(MarkerStyles[bin]);
	      Projection->SetMarkerColor(BinColors[bin]);
	      leg->AddEntry(Projection->Clone(),BinLabels[bin],"l P");

	      if(bin == 0) Projection->DrawCopy();
	      else Projection->DrawCopy("same");
	    }
	  leg->Draw();
	  //canvas->SetLogy();
	  canvas->SaveAs(Selections[sdx]+"_"+Histograms[hdx]+"_ProjectionX_368.pdf");
	}
    }

// 	  TCanvas *canvas = new TCanvas(Histograms[hdx],Histograms[hdx],1);
	  
// 	  TLegend *leg = new TLegend(.64,.18,.91,.45);
// 	  leg->SetTextFont(42);
// 	  leg->SetFillColor(0);
// 	  leg->SetLineColor(1);
// 	  leg->SetShadowColor(0);
	  
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
