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
#include <stdio.h>
#include <math.h> 


vector<TFile*> MCFiles;
vector<TString> MCLabels;
vector<TString> MCNames;
vector<double> MCWeights;
vector<unsigned int> MCLineColors;
vector<unsigned int> MCFillColors;
vector<unsigned int> MCFillStyles;

vector<TString> MuSelectionSteps;
vector<TString> MuSelectionLabels;

vector<TString> ElSelectionSteps;
vector<TString> ElSelectionLabels;

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

void addMuSelection(TString MuSelectionStep, TString MuSelectionLabel)
{
  MuSelectionSteps.push_back(MuSelectionStep);
  MuSelectionLabels.push_back(MuSelectionLabel);
}

void addElSelection(TString ElSelectionStep, TString ElSelectionLabel)
{
  ElSelectionSteps.push_back(ElSelectionStep);
  ElSelectionLabels.push_back(ElSelectionLabel);
}

// main function
int Cutflow()
{
  double Lumi=0.97*4.980;

  //--------------------------------------------------------------
  // Samples
  //--------------------------------------------------------------

  //TFile* TTJetsFall11 = new TFile("TTJetsFall11_new.root", "READ");
  //TFile* SemiLepElMu  = new TFile("SemiLepElMu_new.root",      "READ");
  //TFile* SemiLepTau   = new TFile("SemiLepTau_new.root",       "READ");
  //TFile* DiLep        = new TFile("DiLep_new.root",            "READ");
  //TFile* FullHad      = new TFile("FullHad_new.root",          "READ");

   TFile* SingleTop     = new TFile("SingleTop_new.root",    "READ");

   TFile* SingleTop_b   = new TFile("SingleTop_b_new.root",  "READ");
   TFile* SingleTop_q   = new TFile("SingleTop_q_new.root",  "READ");
   TFile* SingleTop_W   = new TFile("SingleTop_W_new.root",  "READ");

   //TFile* ZJets         = new TFile("ZJets_new.root",        "READ");
   //TFile* WJetsHT       = new TFile("WJetsHT_new.root",      "READ");
   //TFile* QCD           = new TFile("QCD_new.root",          "READ");

   //TFile* MuHad         = new TFile("MuHad_new.root",        "READ");
   //TFile* ElHad         = new TFile("ElHad_new.root",        "READ");

   //TFile* AllSM         = new TFile("AllSM_new.root",        "READ");
  
   //TFile* LM6           = new TFile("LM6_new.root",          "READ");
   //TFile* LM8           = new TFile("LM8_new.root",          "READ");
//   TFile* LM9           = new TFile("LM9_new.root",          "READ");

  //--------------------------------------------------------------------------------------------------------------
  // addMCSample(TFile* MCSample, TString MCName, TString MCLabel, double MCWeight, int MCLc, int MCFc, int MCFs)
  //--------------------------------------------------------------------------------------------------------------

  //addMCSample(TTJetsFall11,"TTJets",  "All $\\textmd{t}\\bar{\\textmd{t}}$+Jets",   Lumi, kRed,      0, 0);
  //addMCSample(SemiLepElMu, "TTJets",  "Semilep. $e/\\mu$",  0.97*0.013178471, kRed,      0, 0);
  //addMCSample(SemiLepTau,  "TTJets",  "Semilep. $\\tau$",   0.97*0.013178471, kRed,      0, 0);
  //addMCSample(DiLep,       "TTJets",  "Dileptonic",         0.97*0.013178471, kRed,      0, 0);
  //addMCSample(FullHad,     "TTJets",  "Fullhadronic",       0.97*0.013178471, kRed,      0, 0);

  addMCSample(SingleTop,    "SingleTop", "Single Top",      Lumi, kGreen-3,  0, 0);

  addMCSample(SingleTop_b,  "SingleTop_b", "t+b",      Lumi, kGreen-3,  0, 0);
  addMCSample(SingleTop_q,  "SingleTop_q", "t+q",      Lumi, kGreen-3,  0, 0);
  addMCSample(SingleTop_W,  "SingleTop_w", "t+W",      Lumi, kGreen-3,  0, 0);

  //addMCSample(WJetsHT,      "WJets",     "W+Jets",          Lumi, kYellow-4, 0, 0);
  //addMCSample(ZJets,        "ZJets",     "$\\textmd{Z}/\\gamma^{*}$+Jets",  Lumi, kBlue-7,   0, 0);
  //addMCSample(QCD,          "QCD",       "QCD",             Lumi, kRed+2,    0, 0);
  
  //addMCSample(ElHad,        "ElHad",     "Data",            1,    kBlack,    0, 0);
  //addMCSample(AllSM,        "AllSM",     "all SM",          Lumi, kBlue,     0, 0);
  
  //addMCSample(LM6,          "LM6",       "LM6",             Lumi, kBlack,    0, 0);
  //addMCSample(LM8,          "LM8",       "LM8",             Lumi, kBlue,     0, 0);
  //addMCSample(LM9,          "LM9",       "LM9",             Lumi, kRed,      0, 0);
  

  //--------------------------------------------------------------------------------------------------------------
  // addMuSelection(TString selection, TString selectionLabel)
  //--------------------------------------------------------------------------------------------------------------

  //addMuSelection("analyzeSUSY1m_noCuts", "event cleaning");
  //addMuSelection("analyzeSUSY1m_preselectionLepton", "lepton selection");
  //addMuSelection("analyzeSUSY1m_preselectionHT", "$H_{T} > 375\\,\\textmd{GeV}$");
  //addMuSelection("analyzeSUSY1m_preselectionMET", "$\\not\\!\\!E_{T} > 60\\,\\textmd{GeV}$");
  addMuSelection("analyzeSUSY1m_leptonSelection", "preselection");
  addMuSelection("analyzeSUSY1m_jetSelection",    "jet selection");
  addMuSelection("analyzeSUSY0b1m_2",   "0 b-tags");
  addMuSelection("analyzeSUSY1b1m_2",   "1 b-tag");
  addMuSelection("analyzeSUSY2b1m_2",   "2 b-tags");
  addMuSelection("analyzeSUSY1b1m_1",   "$\\geqq 1$ b-tags");
  addMuSelection("analyzeSUSY2b1m_1",   "$\\geqq 2$ b-tags");
  addMuSelection("analyzeSUSY3b1m_1",   "$\\geqq 3$ b-tags");
    
  //--------------------------------------------------------------------------------------------------------------
  // addElSelection(TString selection, TString selectionLabel)
  //--------------------------------------------------------------------------------------------------------------
  
  //addElSelection("analyzeSUSY1e_noCuts", "event cleaning");
  //addElSelection("analyzeSUSY1e_preselectionLepton", "lepton selection");
  //addElSelection("analyzeSUSY1e_preselectionHT", "$H_{T} > 375\\,\\textmd{GeV}$");
  //addElSelection("analyzeSUSY1e_preselectionMET", "$\\not\\!\\!E_{T} > 60\\,\\textmd{GeV}$");
  addElSelection("analyzeSUSY1e_leptonSelection", "preselection");
  addElSelection("analyzeSUSY1e_jetSelection",    "jet selection");
  addElSelection("analyzeSUSY0b1e_2",   "0 b-tags");
  addElSelection("analyzeSUSY1b1e_2",   "1 b-tag");
  addElSelection("analyzeSUSY2b1e_2",   "2 b-tags");
  addElSelection("analyzeSUSY1b1e_1",   "$\\geqq 1$ b-tags");
  addElSelection("analyzeSUSY2b1e_1",   "$\\geqq 2$ b-tags");
  addElSelection("analyzeSUSY3b1e_1",   "$\\geqq 3$ b-tags");

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


  //---------------------
  // Muon channel
  //---------------------

  std::cout << "\nMuon channel" << std::endl;
  std::cout << "----------------\n" << std::endl;


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
  std::cout << "\\hline" << std::endl;

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
  
  //loop over selections
  for(int sdx=0; sdx<(int)MuSelectionSteps.size(); ++sdx)
    {
      std::cout << MuSelectionLabels[sdx];
      
      // loop over MC samples
      for(int fdx=0; fdx<(int)MCFiles.size(); ++fdx)
	{
	  TH1F* Temp=(TH1F*)MCFiles[fdx]->Get(MuSelectionSteps[sdx]+"/"+"NumEvents");
	  double Events=MCWeights[fdx]*Temp->Integral(0,-1);
	  std::cout << " & " << Events;
	}
      std::cout << " \\\\" << std::endl;
    }
  
  std::cout << "\\hline" << std::endl;

  std::cout << "\\end{tabular}" << std::endl;
  std::cout << "\\end{center}" << std::endl;
  std::cout << "\\end{table*}" << std::endl;

  //---------------------
  // Electron channel
  //---------------------

  std::cout << "\nElectron channel" << std::endl;
  std::cout << "----------------\n" << std::endl;

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
  std::cout << "\\hline" << std::endl;

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
  
  //loop over selections
  for(int sdx=0; sdx<(int)ElSelectionSteps.size(); ++sdx)
    {
      std::cout << ElSelectionLabels[sdx];
      
      // loop over MC samples
      for(int fdx=0; fdx<(int)MCFiles.size(); ++fdx)
	{
	  TH1F* Temp=(TH1F*)MCFiles[fdx]->Get(ElSelectionSteps[sdx]+"/"+"NumEvents");
	  double Events=MCWeights[fdx]*Temp->Integral(0,-1);
	  std::cout << " & " << Events;
	}
      std::cout << " \\\\" << std::endl;
    }
  
  std::cout << "\\hline" << std::endl;

  std::cout << "\\end{tabular}" << std::endl;
  std::cout << "\\end{center}" << std::endl;
  std::cout << "\\end{table*}" << std::endl;

  //---------------------
  // Combined channel
  //---------------------

  std::cout << "\nCombined channel" << std::endl;
  std::cout << "----------------\n" << std::endl;

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
  std::cout << "\\hline" << std::endl;

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
  
  //loop over selections
  for(int sdx=0; sdx<(int)MuSelectionSteps.size(); ++sdx)
    {
      std::cout << MuSelectionLabels[sdx];
      
      // loop over MC samples
      for(int fdx=0; fdx<(int)MCFiles.size(); ++fdx)
	{
	  //std::cout << MCNames[sdx] << std::endl;

	  if(MCNames[fdx] == "MuHad")
	    {
	      //std::cout << "Data" << std::endl;
	      
	      TH1F* TempMu=(TH1F*)MuHad->Get(MuSelectionSteps[sdx]+"/"+"NumEvents");
	      TH1F* TempEl=(TH1F*)ElHad->Get(ElSelectionSteps[sdx]+"/"+"NumEvents");
	      
	      double Events=MCWeights[fdx]*(TempMu->Integral(0,-1)+TempEl->Integral(0,-1));
	      std::cout << " & " << Events; 
	    }
	  else
	    {
	      TH1F* TempMu=(TH1F*)MCFiles[fdx]->Get(MuSelectionSteps[sdx]+"/"+"NumEvents");
	      TH1F* TempEl=(TH1F*)MCFiles[fdx]->Get(ElSelectionSteps[sdx]+"/"+"NumEvents");
	      
	      double Events=MCWeights[fdx]*(TempMu->Integral(0,-1)+TempEl->Integral(0,-1));
	      std::cout << " & " << Events;
	    }
	}
      std::cout << " \\\\" << std::endl;
    }
  
  std::cout << "\\hline" << std::endl;

  std::cout << "\\end{tabular}" << std::endl;
  std::cout << "\\end{center}" << std::endl;
  std::cout << "\\end{table*}" << std::endl;
}
