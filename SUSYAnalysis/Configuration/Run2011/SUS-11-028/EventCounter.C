#include <vector>
#include "TFile.h"
#include "TF1.h"
#include "TH1.h"

// Samples
vector<TFile*> Files;
vector<TString> Names;
vector<double> Weights;

// Selections
vector<TString> Selections;
vector<TString> Labels;

// add selection
void addSelection(TString selection, TString label)
{
  Selections.push_back(selection);
  Labels.push_back(label);
}

// add sample
void addSample(TFile* sample, TString name, double weight)
{
  Files.push_back(sample);
  Names.push_back(name);
  Weights.push_back(weight);
}

// main function
int EventCounter()
{
  //--------------------------------------------------------------
  // Samples and luminosity
  //--------------------------------------------------------------

  //TFile* SemiLep     = new TFile("SemiLep.root", "READ");
  TFile* SemiLepElMu = new TFile("SemiLepElMu.root", "READ");
  TFile* SemiLepTau  = new TFile("SemiLepTau.root",  "READ");
  TFile* DiLep       = new TFile("DiLep.root",       "READ");
  TFile* SingleTop   = new TFile("SingleTop.root",   "READ");
  TFile* WJetsHT     = new TFile("WJetsHT.root",     "READ");
  //TFile* ZJets       = new TFile("ZJets.root",       "READ");
  //TFile* QCD         = new TFile("QCD.root",         "READ");
  
  TFile* LM6         = new TFile("LM6.root",          "READ");
  TFile* LM8         = new TFile("LM8.root",          "READ");
  TFile* LM6StopPair = new TFile("LM6StopPair.root",  "READ");
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


  //--------------------------------------------------------------
  // addSample(TFile* sample, TString label, double weight)
  //--------------------------------------------------------------

  addSample(SemiLepElMu, "t#bar{t} Semilep e/#mu",  sTTJets);
  //addSample(SemiLep,     "t#bar{t} Semilep",        sTTJets);
  addSample(SemiLepTau,  "t#bar{t} Semilep #tau",   ((5/2)*sTTJets));
  addSample(DiLep,       "t#bar{t} Dilep",          ((5/3)*sTTJets));
  addSample(SingleTop,   "Single Top",              sSingleTop);
  addSample(WJetsHT,     "W+Jets",                  sWJets);

  //addSample(LM8,         "LM8",                     sLM8);
  addSample(LM6,         "LM6",                     sLM6);
  //addSample(LM8StopPair, "LM8 #tilde{t}#tilde{t}*", sLM8);
  //addSample(LM6StopPair, "LM6 #tilde{t}#tilde{t}*", sLM6);

  //--------------------------------------------------------------
  // push back selection steps to vector<TString> Selections
  //--------------------------------------------------------------

  addSelection("analyzeCorrelation1l",                                   "1 lep, $\\geq3$ jets");
  addSelection("analyzeCorrelation1l_HT600ToInf",                        "$H_{T}>600\\,\\textmd{GeV}$");
  addSelection("analyzeCorrelation1l_HT600ToInf_MET150ToInf",            "$\\not\\!\\!E_{T}>150\\,\\textmd{GeV}$");
  //addSelection("analyzeCorrelation1l_HT600ToInf_MET150ToInf_nJets3ToInf","$m_{T}>120\\,\\textmd{GeV}$");
  
  //--------------------------------------------------------------
  // Display event yields
  //--------------------------------------------------------------

  int minNJets = 7;

  for(int sdx=0; sdx<(int)Selections.size(); ++sdx)
    { 
      std::cout << Labels[sdx] << " & ";
      
      for(int fdx=0; fdx<(int)Files.size(); ++fdx)
	{
	  TH1F* temp=(TH1F*)Files[fdx]->Get(Selections[sdx]+"/nJets");
	  
	  if(fdx == Files.size()-1)
	    {
	      std::cout << temp->Integral(minNJets,temp->GetNbinsX()+1)*20000*Weights[fdx] << " \\\\\n";
	    }
	  else
	    {
	      std::cout << temp->Integral(minNJets,temp->GetNbinsX()+1)*20000*Weights[fdx] << " & ";
	    }
	}
    }
}
