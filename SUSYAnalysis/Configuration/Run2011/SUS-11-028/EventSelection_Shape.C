#include <TROOT.h>
#include "TCanvas.h"
#include "TFile.h"
#include "TH1.h"
#include "TH2.h"
#include "TTree.h"
#include "TKey.h"
#include "TF1.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include "TLegend.h"
#include "TPaveText.h"
#include <TDRStyle.h>

// Samples
vector<TFile*> Files;
vector<TString> Labels;
vector<unsigned int> LineColors;
vector<unsigned int> LineStyles;
vector<unsigned int> LineWidths;
vector<unsigned int> FillColors;
vector<unsigned int> FillStyles;
vector<unsigned int> MarkerStyles;
vector<unsigned int> MarkerSizes;
vector<double> Weights;

// Selections
vector<TString> SelectionSteps;
vector<TString> SelectionLabels;
vector<unsigned int> SelectionColors;

// Histograms
vector<TString> Histograms;
vector<TString> XLabels;
vector<double> XMin;
vector<double> XMax;
vector<TString> DrawStyles;
vector<bool> DrawLegend;

// add selection
void addSelection(TString selectionStep, TString selectionLabel, int selectionColor)
{
  SelectionSteps.push_back(selectionStep);
  SelectionLabels.push_back(selectionLabel);
  SelectionColors.push_back(selectionColor);
}

// add sample
void addSample(TFile* sample, TString label, int lc, int ls, int lw, int fc, int fs, int markerStyle, double markerSize, double weight)
{
  Files.push_back(sample);
  Labels.push_back(label);
  LineColors.push_back(lc);
  LineStyles.push_back(ls);
  LineWidths.push_back(lw);
  FillColors.push_back(fc);
  FillStyles.push_back(fs);
  MarkerStyles.push_back(markerStyle);
  MarkerSizes.push_back(markerSize);
  Weights.push_back(weight);
}

void addHistogram(TString hist, TString xlabel, double xMin, double xMax, TString drawStyle, bool drawLegend)
{
  Histograms.push_back(hist);
  XLabels.push_back(xlabel);
  XMin.push_back(xMin);
  XMax.push_back(xMax);
  DrawStyles.push_back(drawStyle);
  DrawLegend.push_back(drawLegend);
}

// main function
int EventSelection_Shape()
{
  // make thes settings as command line option available later
  bool normalize = false;
  bool setLogY = true;

  //--------------------------------------------------------------
  // Samples and luminosity
  //--------------------------------------------------------------

  TFile* SemiLep     = new TFile("SemiLep.root", "READ");
  //TFile* SemiLepElMu = new TFile("SemiLepElMu.root", "READ");
  //TFile* SemiLepTau  = new TFile("SemiLepTau.root",  "READ");
  TFile* DiLep       = new TFile("temp.root",       "READ");
  TFile* DiLepElMu   = new TFile("DiLepElMu.root",   "READ");
  TFile* DiLepTau    = new TFile("DiLepTau.root",    "READ");

  TFile* SingleTop   = new TFile("SingleTop.root",   "READ");

  TFile* SingleTops  = new TFile("SingleTop_sChannel.root",   "READ");
  TFile* SingleTopt  = new TFile("SingleTop_tChannel.root",   "READ");
  TFile* SingleToptW = new TFile("SingleTop_tW.root",         "READ");

  TFile* WJetsHT     = new TFile("WJetsHT.root",     "READ");
  //TFile* ZJets       = new TFile("ZJets.root",       "READ");
  //TFile* QCD         = new TFile("QCD.root",         "READ");
  
  TFile* LM6         = new TFile("LM6.root",          "READ");
  //TFile* LM8         = new TFile("LM8.root",          "READ");
  //TFile* LM6StopPair = new TFile("LM6StopPair.root",  "READ");
  TFile* LM8StopPair = new TFile("LM8StopPair.root",  "READ");

  //--------------------------------------------------------------
  // Weights
  //--------------------------------------------------------------

  // cross-sections
  double xsecQCD       = 0.001;
  double xsecZJets     = 3048;
  double xsecWJets     = 0.001;
  double xsecSingleTop = 0.001;
  double xsecTTJets    = 157.5;

  double xsecLM3       = 3.438;
  double xsecLM6       = 0.3105;
  double xsecLM8       = 0.730;
  double xsecLM13      = 6.899;

  // number of events
  double nQCD       = 1;
  double nZJets     = 36058014;
  double nWJets     = 1;
  double nSingleTop = 1;
  double nTTJets    = 59517528;

  double nLM3       = 440000;
  double nLM6       = 427625;
  double nLM8       = 421190;
  double nLM13      = 437225;

  // weights
  double sQCD       = xsecQCD/(nQCD);
  double sZJets     = xsecZJets/(nZJets);
  double sWJets     = xsecWJets/(nWJets);
  double sSingleTop = xsecSingleTop/(nSingleTop);
  double sTTJets    = xsecTTJets/(nTTJets);

  double sLM3       = xsecLM3/(nLM3);
  double sLM6       = xsecLM6/(nLM6);
  double sLM8       = xsecLM8/(nLM8);
  double sLM13      = xsecLM13/(nLM13);

  //------------------------------------------------------------------------------------------------------------------------------------
  // addSample(TFile* sample, TString label, int lc, int ls, int lw, int fc, int fs, int markerStyle, double markerSize, double weight)
  //------------------------------------------------------------------------------------------------------------------------------------
  
  //addSample(SemiLep,       "t#bar{t} Semilep",         kRed+2,    1,   2,   0,   0,  21,   1.1,   sTTJets);
  //addSample(SemiLepElMu,   "t#bar{t} Semilep e/#mu",   kRed+2,    1,   2,   0,   0,  21,   1.1,   sTTJets);
  //addSample(SemiLepTau,    "t#bar{t} Semilep #tau",    kOrange+7, 1,   2,   0,   0,  22,   1.5,   sTTJets);
  //addSample(DiLep,         "t#bar{t} Dilep",           kPink+5,   1,   2,   0,   0,  23,   1.5,   sTTJets);
  addSample(DiLepElMu,     "t#bar{t} Dilep e/#mu",      kRed,      1,   2,   0,   0,  21,   1.1,   sTTJets);
  //addSample(DiLepTau,      "t#bar{t} Dilep #tau",       kBlue,     1,   2,   0,   0,  23,   1.5,   sTTJets);

  //addSample(SingleTop,     "Single Top",               kRed,      1,   2,   0,   0,  22,   1.5,   sSingleTop);
  //addSample(SingleTops,    "Single Top s",             kRed,      1,   2,   0,   0,  21,   1.1,   sSingleTop);
  //addSample(SingleTopt,    "Single Top t",             kBlue,     1,   2,   0,   0,  22,   1.5,   sSingleTop);
  //addSample(SingleToptW,   "Single Top tW",            kPink+5,   1,   2,   0,   0,  23,   1.5,   sSingleTop);


  //addSample(WJetsHT,       "W+Jets",                   1,         1,   2,   0,   0,  23,   1.5,   sWJets);

  //addSample(LM8,           "LM8",                      kBlue,     1,   2,   0,   0,  20,   1.2,    sLM8);
  //addSample(LM6,           "LM6",                      kBlue+2,   1,   2,   0,   0,  20,   1.2,    sLM6);
  //addSample(LM8StopPair,   "LM8 #tilde{t}#tilde{t}*",  kBlue,     1,   2,   0,   0,  24,   1.2,    sLM8);
  //addSample(LM6StopPair,   "LM6 #tilde{t}#tilde{t}*",  kBlue+2,   1,   2,   0,   0,  24,   1.2,    sLM6);

  //-------------------------------------------------------------------------------------------------
  // push back selection steps to vector<TString> Selections;
  //-------------------------------------------------------------------------------------------------

  addSelection("analyzeCorrelation1l_DiLep",  "Single lepton selection", 2);
  addSelection("analyzeCorrelation1l_DiLep2", "Dilepton selection", 4);

  //--------------------------------------------------------------------------------------------------------------
  // void addHistogram(TString hist, TString xlabel, double xMin, double xMax, TString drawStyle, bool drawLegend)
  //---------------------------------------------------------------------------------------------------------------

  //addHistogram("chi2",   "#chi^{2}_{W fit}",      0,    1, "Hist",   true);
  //addHistogram("nJets",   "Number of Jets",  -0.5, 15.5, "Marker",   true);
  //addHistogram("nJets50", "Number of Jets",  -0.5, 15.5, "Marker",   false);
  addHistogram("mT",       "m_{T} [GeV]",         0,  400, "Marker", true);
  //addHistogram("YMET",    "Y_{MET} [GeV]",      0,   25, "Marker", false);
  //addHistogram("minj3",    "minj3 [GeV]",         0,  300, "Marker", true);
  //addHistogram("hadWMass", "m_{Whad} [GeV]",     60,  100, "Marker", true);
  //addHistogram("MET",      "E_{T}^{miss} [GeV]",  0,  900, "Marker", true);
  //addHistogram("HT",       "H_{T} [GeV]",         0, 2500, "Marker", true);
  //addHistogram("Jets_Et","E_{T} [GeV]",        0, 700,  "Marker", true);
  //addHistogram("Jet0_Et","E_{T} [GeV]",        0, 1000, "Marker", true);
  //addHistogram("Jet1_Et","E_{T} [GeV]",        0, 700,  "Marker", true);
  //addHistogram("Jet2_Et","E_{T} [GeV]",        0, 400,  "Marker", true);
  //addHistogram("Jet3_Et","E_{T} [GeV]",        0, 400,  "Marker", true);
//   addHistogram("Jet4_Et","E_{T} [GeV]",        0, 400);
//   addHistogram("Jet5_Et","E_{T} [GeV]",        0, 400);

  //-------------------------------------------------------------------------------------------------
  // create histograms
  //-------------------------------------------------------------------------------------------------

  setTDRStyle();

  for(int fdx=0; fdx<(int)Files.size(); ++fdx)
    {
      std::cout << "\n" << Labels[fdx] << std::endl;
      std::cout << "---------------------------------------------" << std::endl;

      for(int hdx=0; hdx<(int)Histograms.size(); ++hdx)
	{
	  std::cout << Histograms[hdx] << std::endl;
	  
	  // canvas
	  TCanvas *canvas =new TCanvas(Labels[fdx]+"_"+Histograms[hdx],Labels[fdx]+"_"+Histograms[hdx],1);
	  if(setLogY == true) canvas->SetLogy();

	  // legend
	  TLegend *leg = new TLegend(.48,.8,.90,.91);
	  leg->SetTextFont(42);
	  leg->SetTextSize(0.04);
	  leg->SetFillColor(0);
	  leg->SetLineColor(1);
	  leg->SetShadowColor(0);
	  leg->SetLineColor(0);

	  // label
	  TPaveText *label = new TPaveText(0.14,0.94,0.99,1.,"NDC");
	  label->SetFillColor(0);
	  label->SetTextFont(42);
	  label->SetTextSize(0.043);
	  label->SetBorderSize(0);
	  label->SetTextAlign(12);
	  TText *text=label->AddText("Simulation, #sqrt{s} = 7 TeV");
	  
	  // loop over selection steps
	  for(int sdx=0; sdx<(int)SelectionSteps.size(); ++sdx)
	    {
	      TH1F* temp=(TH1F*)Files[fdx]->Get(SelectionSteps[sdx]+"/"+Histograms[hdx]);
	      
	      // titles, scales and ranges
	      temp->SetTitle("");

	      temp->GetXaxis()->SetTitle(XLabels[hdx]);
	      temp->GetXaxis()->SetRangeUser(XMin[hdx], XMax[hdx]);
	      temp->GetXaxis()->SetTitleOffset(1.2);
	      temp->GetXaxis()->SetTitleSize(0.05);

	      if(normalize == true)
		{
		  temp->GetYaxis()->SetTitle("a.u.");
		  temp->Scale(1/temp->Integral(1,temp->GetNbinsX()+1));
		  temp->SetMinimum(0.001);
		}
	      else
		{
		  temp->GetYaxis()->SetTitle("events");
		  temp->Scale(20000*Weights[fdx]);
		  temp->SetMinimum(0.1);
		}

	      std::cout << temp->Integral(13,temp->GetNbinsX()+1) << std::endl;

	      temp->GetYaxis()->SetTitleOffset(1.4);
	      temp->GetYaxis()->SetTitleSize(0.05);

	      // lines
	      temp->SetLineColor(SelectionColors[sdx]);
	      temp->SetLineStyle(LineStyles[fdx]);
	      temp->SetLineWidth(LineWidths[fdx]);
	      
	      // fill areas
	      temp->SetFillColor(FillColors[fdx]);
	      temp->SetFillStyle(FillStyles[fdx]);
	      
	      // markers
	      if(DrawStyles[hdx] == "Marker")
		{
		  temp->SetMarkerColor(SelectionColors[sdx]);
		  temp->SetMarkerStyle(MarkerStyles[fdx]);
		  temp->SetMarkerSize(MarkerSizes[fdx]);
		}
	      if(sdx == 0)
		{
		  if(FillStyles[fdx] == 1101 || DrawStyles[hdx] == "Hist") temp->Draw("HIST");
		  else temp->Draw("P");
		}
	      else
		{
		  if(FillStyles[fdx] == 1101 || DrawStyles[hdx] == "Hist") temp->Draw("same HIST");
		  else temp->Draw("same P ");
		}

	      leg->AddEntry(temp, SelectionLabels[sdx], "l f P");

	    }

	  // draw and save everything
	  if(DrawLegend[hdx] == true) leg->Draw("same");
	  label->Draw("same");	  

	  if(setLogY == true) canvas->SaveAs(Histograms[hdx]+"_7TeV_Shape.pdf");
	  else canvas->SaveAs(Histograms[hdx]+"_7TeV_Shape.pdf");

	}
    }
}
