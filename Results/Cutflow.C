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

vector<TFile*> MCFiles;
vector<TString> MCLabels;
vector<TString> MCNames;
vector<double> MCWeights;
vector<unsigned int> MCLineColors;
vector<unsigned int> MCFillColors;
vector<unsigned int> MCFillStyles;

vector<TString> Selections;

void addSampleMC(TFile* MCSample, TString MCName, TString MCLabel, double MCWeight, int MCLc, int MCfc, int MCfs)
{
  MCFiles.push_back(MCSample);
  MCNames.push_back(MCName);
  MCLabels.push_back(MCLabel);
  MCWeights.push_back(MCWeight);
  MCLineColors.push_back(MCLc);
  MCFillColors.push_back(MCFc);
  MCFillStyles.push_back(MCFs);
}

// main function
int Cutflow()
{
  //--------------------------------------------------------------
  // Samples
  //--------------------------------------------------------------

  TFile* TTJetsFall11  = new TFile("TTJetsFall11_new.root", "READ");
  TFile* SingleTop     = new TFile("SingleTop_new.root",    "READ");
  //TFile* ZJets         = new TFile("ZJets_new.root",       "READ");
  TFile* WJetsHT       = new TFile("WJetsHT_new.root",      "READ");
  TFile* QCD           = new TFile("QCD_new.root",          "READ");
  
  //TFile* LM6           = new TFile("LM6_new.root",         "READ");
  //TFile* LM8           = new TFile("LM8_new.root",         "READ");
  //TFile* LM9           = new TFile("LM9_new.root",         "READ");
  
  TFile* MuHad         = new TFile("MuHad_new.root",         "READ");
  TFile* ElHad         = new TFile("ElHad)new.root",         "READ");

  //-------------------------------------------------------------------------------------------------------------------
  // addMCSample(TFile* sample, TString name, double weight, int lc, int fc, int fs)
  //-------------------------------------------------------------------------------------------------------------------

  addSample(TTJetsFall11, "TTJets",    "t#bar{t}+Jets",   1, kRed,      0, 0);
  addSample(SingleTop,    "SingleTop", "Single Top",      1, kGreen-3,  0, 0);
  //addSample(ZJets,        "ZJets",     "Z/#gamma*+Jets",  1, kBlue-7,   0, 0);
  addSample(WJetsHT,      "WJets",     "W+Jets",          1, kYellow-4, 0, 0);
  addSample(QCD,          "QCD",       "QCD",             1, kRed+2,    0, 0);
  
  //addSample(LM6,          "LM6",       "LM6",             1, kBlack,    0, 0);
  //addSample(LM8,          "LM8",       "LM8",             1, kBlue,     0, 0);
  //addSample(LM9,          "LM9",       "LM9",             1, kRed,      0, 0);
  
  //-------------------------------------------------------------------------------------------------
  // push back selection step to vector<TString> Selections and DataSelection;
  //-------------------------------------------------------------------------------------------------

  Selections.push_back("analyzeSUSY1m_noCuts");
  
  //------------
  // set style 
  //------------ 

  setTDRStyle();
  gStyle->SetPadLeftMargin(0.16);
  gStyle->SetPadRightMargin(0.05);
  gStyle->SetPadTopMargin(0.08);
  gStyle->SetPadBottomMargin(0.14);

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
	   
	   TLegend *leg = new TLegend(.34,.7,.95,.92);
	   leg->SetTextFont(62);
	   leg->SetTextSize(0.04);
	   leg->SetFillColor(0);
	   leg->SetLineColor(1);
	   leg->SetShadowColor(0);
	   leg->SetLineColor(1);
	   
	   // label
	   TPaveText *label = new TPaveText(0.12,0.94,0.99,1.,"NDC");
	   label->SetFillColor(0);
	   label->SetTextFont(62);
	   label->SetTextSize(0.045);
	   label->SetBorderSize(0);
	   label->SetTextAlign(12);
	   TText *text=label->AddText("Simulation, #sqrt{s} = 7 TeV");

	   // Draw first histogram
	   TH1F* Temp1=(TH1F*)Files[ndx]->Get(Selections[sdx]+"/"+Histograms[0]);

	   //std::cout << "Integral after weighting: " << Temp1->Integral() << std::endl;

	   // Normalization and ranges
	   Temp1->Scale(1/(Temp1->Integral()));

	   // Title
	   Temp1->SetTitle("");

	   // Line color, style, and width
	   Temp1->SetLineColor(LineColors[ndx]);
	   Temp1->SetLineStyle(7);
	   Temp1->SetLineWidth(3);

	   // Axes
	   Temp1->GetXaxis()->SetTitle("Number of PU interactions");
	   Temp1->GetXaxis()->SetTitleSize(0.05);
	   Temp1->GetXaxis()->SetTitleFont(62);
	   Temp1->GetXaxis()->SetTitleOffset(1.4);

	   Temp1->GetYaxis()->SetTitle("a.u.");
	   Temp1->GetYaxis()->SetTitleOffset(1.7);
	   Temp1->GetYaxis()->SetTitleSize(0.05);
	   Temp1->GetYaxis()->SetTitleFont(62);

	   // Labels
	   Temp1->SetLabelColor(1, "XYZ");
	   Temp1->SetLabelFont(62, "XYZ");
	   Temp1->SetLabelOffset(0.007, "XYZ");
	   Temp1->SetLabelSize(0.04, "XYZ");

	   Temp1->Draw("Hist");

	   // Draw second histogram
	   TH1F* Temp2=(TH1F*)Files[ndx]->Get(Selections[sdx]+"/"+Histograms[1]);

	   //std::cout << "Integral before weighting: " << Temp2->Integral() << std::endl;

	   // Normalization
	   Temp2->Scale(1/(Temp2->Integral()));

	   // Line color, style, and width
	   Temp2->SetLineColor(LineColors[ndx]);
	   Temp2->SetLineStyle(1);
	   Temp2->SetLineWidth(2);

	   Temp2->Draw("same Hist");

	   // Draw third histogram
	   TH1F* Temp3=(TH1F*)Data->Get("pileup");

	   // Normalization
	   Temp3->Scale(1/(Temp3->Integral()));

	   // Line color, style, and width
	   Temp3->SetLineColor(1);
	   Temp3->SetLineWidth(1);

	   // Marker style, colors, and size
	   Temp3->SetMarkerStyle(20);
	   Temp3->SetMarkerColor(1);
	   Temp3->SetMarkerSize(0.9);

	   Temp3->Draw("same E");

	   // Add entries to legend
	   leg->AddEntry(Temp2,Labels[ndx]+" w/o reweighting","l P");
	   leg->AddEntry(Temp1,Labels[ndx]+" w reweighting","l P");
	   leg->AddEntry(Temp3,"Run 2011","l P");
	   	 
	   // Draw legend and labels
	   leg->Draw();
	   label->Draw("same");

	   // Save canvas
	   c1->SaveAs("PU_"+Names[ndx]+".pdf");
	 }
     }
}
