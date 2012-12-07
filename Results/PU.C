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
#include <TDRStyle.h>

vector<TFile*> Files;
vector<TString> Labels;
vector<TString> Names;
vector<double> Weights;
vector<unsigned int> LineColors;
vector<unsigned int> FillColors;
vector<unsigned int> FillStyles;

vector<TString> Selections;
vector<TString> Histograms;

// add  sample
void addSample(TFile* sample, TString name, TString label, double weight, int lc, int fc, int fs);

void addSample(TFile* sample, TString name, TString label, double weight, int lc, int fc, int fs)
{
  Files.push_back(sample);
  Names.push_back(name);
  Labels.push_back(label);
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
int PU()
{

  //--------------------------------------------------------------
  // Samples
  //--------------------------------------------------------------

  //TFile* TTJetsSummer11 = new TFile("TTJetsSummer11.root", "READ");
  TFile* TTJetsFall11   = new TFile("TTJetsFall11.root",   "READ");
  TFile* SingleTop      = new TFile("SingleTop.root",      "READ");
  TFile* ZJets          = new TFile("ZJets.root",          "READ");
  //TFile* WJets          = new TFile("WJets.root",          "READ");
  TFile* WJetsHT        = new TFile("WJetsHT.root",        "READ");
  TFile* QCD            = new TFile("QCD.root",            "READ");
  
  TFile* LM3            = new TFile("LM3.root",            "READ");
  TFile* LM8            = new TFile("LM8.root",            "READ");
  TFile* LM13           = new TFile("LM13.root",           "READ");

  TFile* Data = new TFile("PU_Data_68000.root", "Read"); 

  //-------------------------------------------------------------------------------------------------------------------
  // addSample(TFile* sample, TString name, double weight, int lc, int fc, int fs)
  //-------------------------------------------------------------------------------------------------------------------

  addSample(TTJetsFall11, "TTJets",    "t#bar{t}+Jets",    1, kRed+2,   0, 0);
  addSample(SingleTop,    "SingleTop", "Single Top",       1, kRed,     0, 0);
  addSample(ZJets,        "ZJets",     "Z/#gamma*+Jets",   1, kGreen+2, 0, 0);
  addSample(WJetsHT,      "WJets",     "W+Jets",           1, 1,        0, 0);
  addSample(QCD,          "QCD",       "QCD",              1, kBlue,    0, 0);
				    
//   addSample(LM3,       "LM3",         1, kRed+2,   0, 0);
//   addSample(LM8,       "LM8",         1, 1,        0, 0);
//   addSample(LM13,      "LM13",        1, kBlue,    0, 0);

  //-------------------------------------------------------------------------------------------------
  // push back selection step to vector<TString> Selections and DataSelection;
  //-------------------------------------------------------------------------------------------------

  Selections.push_back("analyzeSUSY1m_noCuts");
  
  //-------------------------------------------------------------------------------------------------
  // push back histogram to vector<int> Histograms and DataHistograms;
  //-------------------------------------------------------------------------------------------------

  addHistogram("nPU");
  addHistogram("nPU_noWgt");

  //------------
  // set style 
  //------------ 

  setTDRStyle();

//   gStyle->SetCanvasColor(10);
//   gStyle->SetOptStat(0);
//   gStyle->SetPalette(1);
//   gStyle->SetTitleFillColor(0);

  //--------
  // Plot
  //--------

  // loop over samples
   for(int ndx=0; ndx<(int)Files.size(); ++ndx)
     {

       std::cout << "\n"<< Names[ndx] << std::endl;
       std::cout << "---------------" << std::endl;

       // loop over selections
       for(int sdx=0; sdx<(int)Selections.size(); ++sdx)
	 {
	   TCanvas *c1=new TCanvas(Selections[sdx]+"_"+Histograms[0]+"_"+Labels[ndx],Selections[sdx]+"_"+Histograms[0]+"_"+Labels[ndx], 1);
	   
	   TLegend *leg = new TLegend(.33,.70,.91,.91);
	   leg->SetTextFont(42);
	   leg->SetFillColor(0);
	   leg->SetLineColor(1);
	   leg->SetShadowColor(0);
	   leg->SetTextSize(0.045);
	   leg->SetFillColor(0);
	   leg->SetLineColor(1);
	   leg->SetShadowColor(0);
	   leg->SetLineColor(0);

	   TPaveText *label = new TPaveText(0.14,0.94,0.99,1.,"NDC");
	   label->SetFillColor(0);
	   label->SetTextFont(42);
	   label->SetTextSize(0.043);
	   label->SetBorderSize(0);
	   label->SetTextAlign(12);
	   TText *text=label->AddText("Simulation, #sqrt{s} = 7 TeV");

	   // Draw first histogram
	   TH1F* Temp1=(TH1F*)Files[ndx]->Get(Selections[sdx]+"/"+Histograms[0]);

	   std::cout << "Integral after weighting: " << Temp1->Integral() << std::endl;

	   Temp1->Scale(1/(Temp1->Integral()));
	   Temp1->SetTitle("");
	   //Temp1->SetMaximum(0.11);
	   //if(Labels[ndx]=="Single Top") Temp1->SetMaximum(0.11);
	   Temp1->GetXaxis()->SetTitle("Number of PU interactions");
	   //Temp1->GetXaxis()->CenterTitle();
	   Temp1->GetXaxis()->SetTitleOffset(1.2);
	   //Temp1->GetXaxis()->SetRangeUser(-0.5,50.5);
	   Temp1->GetYaxis()->SetTitle("a.u.");
	   //Temp1->GetYaxis()->CenterTitle();
	   Temp1->GetYaxis()->SetTitleOffset(1.4);
	   Temp1->SetLineColor(LineColors[ndx]);
	   Temp1->SetLineStyle(3);
	   Temp1->SetLineWidth(3);
	   //Temp1->SetMarkerStyle(24);
	   //Temp1->SetMarkerColor(LineColors[ndx]);
	   //Temp1->SetMarkerSize(1.0);
	   Temp1->Draw("Hist");

	   // Draw first histogram
	   TH1F* Temp2=(TH1F*)Files[ndx]->Get(Selections[sdx]+"/"+Histograms[1]);

	   std::cout << "Integral before weighting: " << Temp2->Integral() << std::endl;

	   Temp2->Scale(1/(Temp2->Integral()));
	   Temp2->SetLineColor(LineColors[ndx]);
	   Temp2->SetLineStyle(1);
	   Temp2->SetLineWidth(2);
	   //Temp2->SetMarkerStyle(21);
	   //Temp2->SetMarkerColor(LineColors[ndx]);
	   //Temp2->SetMarkerSize(1.0);
	   Temp2->Draw("same Hist");

	   TH1F* Temp3=(TH1F*)Data->Get("pileup");
	   Temp3->Scale(1/(Temp3->Integral()));
	   Temp3->SetLineColor(1);
	   Temp3->SetLineWidth(1);
	   Temp3->SetMarkerStyle(20);
	   Temp3->SetMarkerColor(1);
	   Temp3->SetMarkerSize(0.9);
	   Temp3->Draw("same E");

	   leg->AddEntry(Temp2,Labels[ndx]+" w/o reweighting","l P");
	   leg->AddEntry(Temp1,Labels[ndx]+" w reweighting","l P");
	   leg->AddEntry(Temp3,"Run 2011","l P");
	   	 
	   leg->Draw();
	   label->Draw("same");
	   c1->SaveAs("PU_"+Names[ndx]+".pdf");
	 }
     }
}
