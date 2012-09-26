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

// add  histogram
void addHistogram(TString name, TString xLabel);

void addHistogram(TString name, TString xLabel)
{
  Histograms.push_back(name);
  XLabels.push_back(xLabel);
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
int Variables()
{

  //--------------------------------------------------------------
  // Sample
  //--------------------------------------------------------------

  //TFile* TTJets = new TFile("TTJetsFall11.root", "READ");
  TFile* TTJets = new TFile("temp.root", "READ");

  //--------------------------------------------------------------
  // addHistogram
  //--------------------------------------------------------------

  addHistogram("YMET",    "Y_{MET} [GeV^{1/2}]");
  //addHistogram("mT",      "m_{T} [GeV]");
  //addHistogram("mlb",     "m_{l,b} [GeV]");
  //addHistogram("mLepTop", "m_{3,lep} [GeV]");
  //addHistogram("minj3",   "minj3 [GeV]");

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
      
      TLegend *leg = new TLegend(.64,.62,.91,.89);
      leg->SetTextFont(42);
      leg->SetFillColor(0);
      leg->SetLineColor(1);
      leg->SetShadowColor(0);
      
      double max=0;

      for(int sdx=0; sdx<(int)Selections.size(); ++sdx)
	{
	  std::cout << "Draw " << Selections[sdx]+"/"+Histograms[hdx] << std::endl;
	  
	  // create histogram
	  TH1F* Hist = (TH1F*)TTJets->Get(Selections[sdx]+"/"+Histograms[hdx]);
	  
	  // edit histogram
	  Hist->SetTitle("");
	  Hist->GetXaxis()->SetTitle(XLabels[hdx]);
	  Hist->GetXaxis()->SetTitleOffset(1.4);
	  Hist->GetXaxis()->SetRangeUser(0,25.);
	  Hist->GetYaxis()->SetTitle("# events");
	  Hist->GetYaxis()->SetTitleOffset(1.4);
	  //Hist->SetMinimum(0);
	  //Hist->SetMaximum(50);
	  Hist->SetLineColor(LineColors[sdx]);
	  Hist->SetLineWidth(2);
	    leg->AddEntry(Hist->Clone(),Labels[sdx],"l P");
	  
	  if(sdx == 0)
	    {
	      Hist->DrawCopy();
	      max=Hist->GetMaximum();
	    }
	  else Hist->DrawCopy("same");
	}
      
      // TLine
      TLine * line = new TLine(173, 0, 173, 1.05*max);
      line->SetLineWidth(1);
      line->SetLineStyle(7);
      line->SetLineColor(1);
      //line->Draw("same");


      leg->Draw();
      canvas->SetLogy();
      
      canvas->SaveAs(Histograms[hdx]+"_reco_log.pdf");
      
    }  
}
