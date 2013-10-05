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

vector<TString> SelectionSteps;
vector<TString> SelectionLabels;

void addMCSample(TFile* MCSample, TString MCName, TString MCLabel, double MCWeight, int MCLc, int MCFc, int MCFs)
{
  MCFiles.push_back(MCSample);
  MCNames.push_back(MCName);
  MCLabels.push_back(MCLabel);
  MCWeights.push_back(MCWeight);
  MCLineColors.push_back(MCLc);
  MCFillColors.push_back(MCFc);
  MCFillStyles.push_back(MCFs);
}

void addSelection(TString selectionStep, TString selectionLabel)
{
  SelectionSteps.push_back(selectionStep);
  SelectionLabels.push_back(selectionLabel);
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
  TFile* ElHad         = new TFile("ElHad_new.root",         "READ");

  //--------------------------------------------------------------------------------------------------------------
  // addMCSample(TFile* MCSample, TString MCName, TString MCLabel, double MCWeight, int MCLc, int MCFc, int MCFs)
  //--------------------------------------------------------------------------------------------------------------

  addMCSample(TTJetsFall11, "TTJets",    "$\\textmd{t}\\bar{\\textmd{t}}$+Jets",   1, kRed,      0, 0);
  addMCSample(SingleTop,    "SingleTop", "Single Top",      1, kGreen-3,  0, 0);
  //addMCSample(ZJets,        "ZJets",     "Z/#gamma*+Jets",  1, kBlue-7,   0, 0);
  addMCSample(WJetsHT,      "WJets",     "W+Jets",          1, kYellow-4, 0, 0);
  addMCSample(QCD,          "QCD",       "QCD",             1, kRed+2,    0, 0);
  
  //addMCSample(LM6,          "LM6",       "LM6",             1, kBlack,    0, 0);
  //addMCSample(LM8,          "LM8",       "LM8",             1, kBlue,     0, 0);
  //addMCSample(LM9,          "LM9",       "LM9",             1, kRed,      0, 0);
  
  //--------------------------------------------------------------------------------------------------------------
  // addSelection(TString selection, TString selectionLabel)
  //--------------------------------------------------------------------------------------------------------------

  addSelection("analyzeSUSY1m_noCuts", "no Cuts");
  
  //------------
  // set style 
  //------------ 

  setTDRStyle();
  gStyle->SetPadLeftMargin(0.16);
  gStyle->SetPadRightMargin(0.05);
  gStyle->SetPadTopMargin(0.08);
  gStyle->SetPadBottomMargin(0.14);

  //------------------
  // Create tables
  //------------------

  std::cout << "\n" << std::endl;

  std::cout << "\\begin{table*}[htb]" << std::endl;
  std::cout << "\\caption{CAPTION}" << std::endl;
  std::cout << "\\begin{center}" << std::endl;
  std::cout << "\\begin{tabular}{|l|";
  
   // loop over MC samples
  for(int fdx=0; fdx<(int)MCFiles.size(); ++fdx)
    {
      std::cout << "c|";
    }
  std::cout << "}" << std::endl;
  std::cout << "\\hline\n" << std::endl;

  // head line
  std::cout << "Selection";
   // loop over MC samples
  for(int fdx=0; fdx<(int)MCFiles.size(); ++fdx)
    {
      std::cout << " & " << MCLabels[fdx];
    }
  std::cout << " \\\\" << std::endl;

  std::cout << "\\hline" << std::endl;
  std::cout << "\\hline" << std::endl;
  
//   //loop over selections
//   for(int sdx=0; sdx<(int)SelectionSteps.size(); ++sdx)
//     {
//       std::cout << "\n"<< SelectionLabels[sdx] << std::endl;
//       std::cout << "---------------" << std::endl;
      
//       // loop over MC samples
//       for(int fdx=0; fdx<(int)MCFiles.size(); ++fdx)
// 	{

// 	  std::cout << "\n"<< MCNames[fdx] << std::endl;
       
// 	}
//     }

  std::cout << "\n" << std::endl;

  std::cout << "\\end{tabular}" << std::endl;
  std::cout << "\\end{center}" << std::endl;
  std::cout << "\\end{table*}" << std::endl;
  
}
