#include <TROOT.h>
#include "TFile.h"
#include "TH1.h"
#include "TH2.h"
#include "TTree.h"
#include "TKey.h"
#include "TF1.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <Plot.h>

vector<TFile*> Files;
vector<TString> Names;
vector<double> Weights;
vector<unsigned int> LineColors;
vector<unsigned int> FillColors;
vector<unsigned int> FillStyles;

vector<TString> Selections;
vector<TString> Histograms;

// add  sample
void addSample(TFile* sample, TString name, double weight, int lc, int fc, int fs);

void addSample(TFile* sample, TString name, double weight, int lc, int fc, int fs)
{
  Files.push_back(sample);
  Names.push_back(name);
  Weights.push_back(weight);
  LineColors.push_back(lc);
  FillColors.push_back(fc);
  FillStyles.push_back(fs);
}

// add  histogram
void addHistogram(TString name);

void addHistogram(TString name)
{
  Histograms.push_back(name);
}

// main function
int BtagEff()
{

  //--------------------------------------------------------------
  // Samples
  //--------------------------------------------------------------

  TFile* TTJetsSummer11 = new TFile("TTJetsSummer11.root", "READ");
  //TFile* TTJetsFall11   = new TFile("TTJetsFall11.root",   "READ");
  TFile* SingleTop      = new TFile("SingleTop.root",      "READ");
  //TFile* ZJets          = new TFile("ZJets.root",          "READ");
  //TFile* WJets          = new TFile("WJets.root",          "READ");
  //TFile* WJetsHT        = new TFile("WJetsHT.root",        "READ");
  TFile* QCD            = new TFile("QCD.root",            "READ");
  
  TFile* LM3            = new TFile("LM3.root",            "READ");
  TFile* LM8            = new TFile("LM8.root",            "READ");
  TFile* LM13           = new TFile("LM13.root",           "READ");

  //-------------------------------------------------------------------------------------------------------------------
  // addSample(TFile* sample, TString name, double weight, int lc, int fc, int fs)
  //-------------------------------------------------------------------------------------------------------------------

  addSample(TTJetsSummer11, "TTJetsSummer11", 1, kRed,     0, 0);
  //addSample(TTJetsFall11,   "TTJetsFall11",   1, kRed,     0, 0);
  addSample(SingleTop,      "SingleTop",      1, kRed+2,   0, 0);
  //addSample(ZJets,          "ZJets",          1, kGreen+2, 0, 0);
  //addSample(WJets,          "WJets",          1, kYellow,  0, 0);
  //addSample(WJetsHT,        "WJetsHT",        1, kYellow,  0, 0);
  addSample(QCD,            "QCD",            1, kBlue-7,  0, 0);
					    
  addSample(LM3,       "LM3",         1, kRed+2,   0, 0);
  addSample(LM8,       "LM8",         1, 1,        0, 0);
  addSample(LM13,      "LM13",        1, kBlue,    0, 0);


  //-------------------------------------------------------------------------------------------------
  // push back selection step to vector<TString> Selections and DataSelection;
  //-------------------------------------------------------------------------------------------------

  std::cout << "Test1" << std::endl;

  //Selections.push_back("analyzeSUSY1b1m_6");
  //Selections.push_back("analyzeSUSY2b1m_6");
  //Selections.push_back("analyzeSUSY3b1m_6");
  //Selections.push_back("analyzeSUSY1b1e_6");
  //Selections.push_back("analyzeSUSY2b1e_6");
  //Selections.push_back("analyzeSUSY3b1e_6");

  Selections.push_back("monitorBtagWeightingMu");
  Selections.push_back("monitorBtagWeightingEl");

  //-------------------------------------------------------------------------------------------------
  // push back histogram to vector<int> Histograms and DataHistograms;
  //-------------------------------------------------------------------------------------------------

  std::cout << "Test2" << std::endl;

  addHistogram("nBjets_noWgt");
  addHistogram("btagWeights_noWgt");

  //------------
  // set style 
  //------------ 

  gStyle->SetCanvasColor(10);
  gStyle->SetOptStat(0);
  gStyle->SetPalette(1);
  gStyle->SetTitleFillColor(0);

  //--------
  // Plot
  //--------

  // loop over samples
   for(int ndx=0; ndx<(int)Files.size(); ++ndx)
     {

       // loop over selections
       for(int sdx=0; sdx<(int)Selections.size(); ++sdx)
	 {
	   TCanvas *c1=new TCanvas(Selections[sdx]+"_"+Histograms[0]+"_"+Names[ndx],Selections[sdx]+"_"+Histograms[0]+"_"+Names[ndx], 1);
	   
	   TLegend *leg = new TLegend(.65,.75,.98,.98);
	   leg->SetTextFont(42);
	   leg->SetFillColor(0);
	   leg->SetLineColor(0);
	   
	   // draw first histogram
	   TH1F* Temp1=(TH1F*)Files[ndx]->Get(Selections[sdx]+"/"+Histograms[0]);
	   Temp1->Draw();
	   Temp1->SetTitle(Names[ndx]);
	   Temp1->GetXaxis()->SetTitle("Number of bjets");
	   Temp1->GetXaxis()->CenterTitle();
	   Temp1->GetYaxis()->SetTitle("# events after basline selection");
	   Temp1->GetYaxis()->CenterTitle();
	   Temp1->GetYaxis()->SetTitleOffset(1.3);
	   Temp1->SetLineColor(LineColors[ndx]);
	   Temp1->SetLineStyle(1);
	   Temp1->SetMarkerStyle(20);
	   Temp1->SetMarkerColor(LineColors[ndx]);
	   Temp1->SetMarkerSize(0.7);
	   leg->AddEntry(Temp1,"w/ cut","l P");
	   
	   // loop over different histograms
	   for(int hdx=1; hdx<(int)Histograms.size(); ++hdx)
	     {
	       TH1F* Temp2=(TH1F*)Files[ndx]->Get(Selections[sdx]+"/"+Histograms[hdx]);
	       Temp2->Draw("same");
	       Temp2->SetLineColor(LineColors[ndx]);
	       Temp2->SetLineStyle(2);
	       Temp2->SetMarkerStyle(25);
	       Temp2->SetMarkerColor(LineColors[ndx]);
	       Temp2->SetMarkerSize(0.9);
	       leg->AddEntry(Temp2,"w/ weights","l P");
	       
	     }
	   leg->Draw("box");
	   c1->SaveAs(Selections[sdx]+"_"+Histograms[0]+"_"+Names[ndx]+".pdf");
	 }
     }
}
