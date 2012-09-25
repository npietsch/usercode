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

vector<TString> Selections;
vector<TString> Labels;
vector<unsigned int> LineColors;
vector<TString> Histograms;
vector<TString> XLabels;
vector<TString> YLabels;

// add  histogram
void addHistogram(TString name, TString xLabel, TString yLabel);

void addHistogram(TString name, TString xLabel, TString yLabel)
{
  Histograms.push_back(name);
  XLabels.push_back(xLabel);
  YLabels.push_back(yLabel);
}

// add  selection step
void addSelectionStep(TString step, TString label, int lc);

void addSelectionStep(TString step, TString label, int lc)
{
  Selections.push_back(step);
  Labels.push_back(label);
  LineColors.push_back(lc);
}

// main function
int TtGenEventAnalyzer()
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
  addHistogram("HT_YMET",     "HT [GeV]",         "<YMET> [GeV^{1/2}]");
  //addHistogram("HT_LepPtSig", "HT [GeV]",         "<Lepton p_{T} sig> [GeV^{1/2}]");
  //addHistogram("HT_mT",       "HT [GeV]",         "<m_{T}> [GeV]");
  //addHistogram("YMET_nJets",  "YMET [GeV^{1/2}]", "<nJets>");
  //addHistogram("mT_nJets",   "m_{T} [GeV]",     "<nJets>");
  //addHistogram("minj3_nJets",   "minj3 [GeV]",     "<nJets>");
  //addHistogram("mlb_nJets",     "mlb [GeV]",       "<nJets>");
  //addHistogram("HT_mlb",        "HT [GeV]",       "mlb [GeV]");
  //addHistogram("HT_mLepTop",    "HT [GeV]",       "mLepTop [GeV]");
  //addHistogram("HT_minj3",        "HT [GeV]",  "minj3 [GeV]");

  //addHistogram("mlb_nJets",        "mlb [GeV]",      "<nJets>");
  //addHistogram("mLepTop_nJets",    "mLepTop [GeV]",  "<nJets>");

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
  
  addSelectionStep("analyzeSUSY_noCuts_1l",          "no Cuts",           1);
  addSelectionStep("analyzeSUSY_leptonSelection_1l", "lepton selection",  4);
  addSelectionStep("analyzeSUSY_jetSelection_1l",    "jet selection",     8);
  addSelectionStep("analyzeSUSY_HTSelection_1l",     "HT selection",      2);
  addSelectionStep("analyzeSUSY_metSelection_1l",    "MET selection",     kRed+2);

//   addSelectionStep("analyzeSUSY_noCuts_1l_match2",          "no Cuts",           1);
//   addSelectionStep("analyzeSUSY_leptonSelection_1l_match2", "lepton selection",  4);
//   addSelectionStep("analyzeSUSY_jetSelection_1l_match2",    "jet selection",     8);
//   addSelectionStep("analyzeSUSY_HTSelection_1l_match2",    "HT selection",      2);
//   addSelectionStep("analyzeSUSY_metSelection_1l_match2",     "MET selection",     kRed+2);

  //------------
  // set style 
  //------------ 

  setTDRStyle();

  for(int hdx=0; hdx<(int)Histograms.size(); ++hdx)
    {
      std::cout << "\nDraw " << Histograms[hdx] << std::endl;
      std::cout << "--------------------------" << std::endl;

      TCanvas *canvas = new TCanvas(Histograms[hdx],Histograms[hdx],1);

      TLegend *leg = new TLegend(.64,.18,.91,.45);
      leg->SetTextFont(42);
      leg->SetFillColor(0);
      leg->SetLineColor(1);
      leg->SetShadowColor(0);
      
      for(int sdx=0; sdx<(int)Selections.size(); ++sdx)
	{
	  std::cout << "Draw " << Selections[sdx]+"/"+Histograms[hdx] << std::endl;
 
	  // create profile
	  TH2F* Hist = (TH2F*)TTJets->Get(Selections[sdx]+"/"+Histograms[hdx]);
	  TProfile2D* Profile = (TProfile2D*)Hist->ProfileX();

	  // edit profile
	  Profile->SetTitle("");
	  Profile->GetXaxis()->SetTitle(XLabels[hdx]);
	  Profile->GetXaxis()->SetTitleOffset(1.4);
	  Profile->GetXaxis()->SetRangeUser(0,1000.);
	  Profile->GetYaxis()->SetTitle(YLabels[hdx]);
	  Profile->SetMinimum(0);
	  Profile->SetMaximum(9);
	  Profile->SetLineColor(LineColors[sdx]);
	  Profile->SetLineWidth(2);
	  leg->AddEntry(Profile->Clone(),Labels[sdx],"l P");

	  if(sdx == 0) Profile->DrawCopy();
	  else Profile->DrawCopy("same");
	}

      leg->Draw();

      canvas->SaveAs(Histograms[hdx]+"_reco.pdf");
      
    }  
}
