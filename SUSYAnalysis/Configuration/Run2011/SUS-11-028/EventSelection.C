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

// MC samples
vector<TFile*> MCFiles;
vector<TString> MCNames;
vector<unsigned int> MCLineColors;
vector<unsigned int> MCFillColors;
vector<unsigned int> MCFillStyles;
vector<double> Weights;
 
// Muon data samples
vector<TFile*> MuFiles;
vector<TString> MuNames;
vector<unsigned int> MuLineColors;
vector<unsigned int> MuFillColors;
vector<unsigned int> MuFillStyles;

// Electron data samples
vector<TFile*> ElFiles;
vector<TString> ElNames;
vector<unsigned int> ElLineColors;
vector<unsigned int> ElFillColors;
vector<unsigned int> ElFillStyles;

// MC histograms
vector<TString> MCHistograms;
vector<double> MCXminN;
vector<double> MCXmaxN;
vector<double> MCXminR;
vector<double> MCXmaxR;

// Data histograms
vector<TString> DataHistograms;
vector<double> DataXminN;
vector<double> DataXmaxN;
vector<double> DataXminR;
vector<double> DataXmaxR;

// Selections
vector<TString> MCMuSelections;
vector<TString> MCElSelections;
vector<TString> DataMuSelections;
vector<TString> DataElSelections;

// Scales vector
vector<double> Scales;

// add MC sample
void addMCSample(TFile* sample, TString name,  int lc, int fc, int fs, double weight);

void addMCSample(TFile* sample, TString name,  int lc, int fc, int fs, double weight)
{
  MCFiles.push_back(sample);
  MCNames.push_back(name);
  MCLineColors.push_back(lc);
  MCFillColors.push_back(fc);
  MCFillStyles.push_back(fs);
  Weights.push_back(weight);
}

// add Muon data samples
void addMuSample(TFile* sample, TString name, int lc, int fc, int fs);

void addMuSample(TFile* sample, TString name, int lc, int fc, int fs)
{
  MuFiles.push_back(sample);
  MuNames.push_back(name);
  MuLineColors.push_back(lc);
  MuFillColors.push_back(fc);
  MuFillStyles.push_back(fs);
}

// add Electron data sample
void addElSample(TFile* sample, TString name, int lc, int fc, int fs);

void addElSample(TFile* sample, TString name, int lc, int fc, int fs)
{
  ElFiles.push_back(sample);
  ElNames.push_back(name);
  ElLineColors.push_back(lc);
  ElFillColors.push_back(fc);
  ElFillStyles.push_back(fs);
}

// add MC histogram
void addMCHistogram(TString name, int xminN, int xmaxN, int xminR, int xmaxR);

void addMCHistogram(TString name, int xminN, int xmaxN, int xminR, int xmaxR)
{
  MCHistograms.push_back(name);
  MCXminN.push_back(xminN);
  MCXmaxN.push_back(xmaxN);
  MCXminR.push_back(xminR);
  MCXmaxR.push_back(xmaxR);
}

// add data histogram
void addDataHistogram(TString name, int xminN, int xmaxN, int xminR, int xmaxR);

void addDataHistogram(TString name, int xminN, int xmaxN, int xminR, int xmaxR)
{
  DataHistograms.push_back(name);
  DataXminN.push_back(xminN);
  DataXmaxN.push_back(xmaxN);
  DataXminR.push_back(xminR);
  DataXmaxR.push_back(xmaxR);
}

// main function
int EventSelection()
{

  // Normalize background to data? -1: No histogram normalized, 0: only specified normalized, +1: all normalized
  int Normalize=0;

  //--------------------------------------------------------------
  // Samples and luminosity
  //--------------------------------------------------------------

  TFile* TTJets    = new TFile("TTJetsFall11.root", "READ");
//   TFile* SingleTop = new TFile("SingleTop.root",    "READ");
//   TFile* WJetsHT   = new TFile("WJetsHT.root",      "READ");
//   TFile* ZJets     = new TFile("ZJets.root",        "READ");
//   TFile* QCD       = new TFile("QCD.root",          "READ");

//   TFile* LM3       = new TFile("LM3.root",          "READ");
//   TFile* LM6       = new TFile("LM6.root",          "READ");
//   TFile* LM8       = new TFile("LM8.root",          "READ");
//   TFile* LM13      = new TFile("LM13.root",         "READ");

  TFile* LM8_StopPair      = new TFile("LM8_StopPair.root",     "READ");
  TFile* LM8_SbottomPair   = new TFile("LM8_SbottomPair.root",  "READ");

  TFile* LM8_GluinoPair    = new TFile("LM8_GluinoPair.root",   "READ");
  TFile* LM8_GluinoSquark  = new TFile("LM8_GluinoSquark.root", "READ");

//   TFile* MuHad     = new TFile("MuHad.root",        "READ");
//   TFile* ElHad     = new TFile("ElHad.root",        "READ");

  // Luminosity for MuHad in pb^-1
  Double_t MuLumi=4980;

  // Luminosity for ElHad in pb^-1
  Double_t ElLumi=4980;

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

  //-------------------------------------------------------------------------------------------------------------------
  // addMCSample(TFile* sample, TString name, double weight, int lc, int fc, int fs)
  //-------------------------------------------------------------------------------------------------------------------

//   addMCSample(QCD,       "QCD",           kBlue,    kBlue,    1101, sQCD );
//   addMCSample(ZJets,     "Z+Jets",        kGreen+2, kGreen+2, 1101, sZJets);
//   addMCSample(WJetsHT,   "W+Jets",        kYellow,  kYellow,  1101, sWJets);
//   addMCSample(SingleTop, "Single Top",    kRed,     kRed,     1101, sSingleTop);

  addMCSample(LM8_StopPair,      "LM8 #tilde{t}#tilde{t}*",   kGreen+2, kGreen+2, 1101,   sLM8);
  addMCSample(LM8_SbottomPair,   "LM8 #tilde{b}#tilde{b}*",   kYellow,  kYellow,  1101,   sLM8);
  addMCSample(LM8_GluinoPair,    "LM8 #tilde{g}#tilde{g}",    kRed,     kRed,     1101,   sLM8);
  addMCSample(LM8_GluinoSquark,  "LM8 #tilde{g}#tilde{q}",    kRed+2,   kRed+2,   1101,   sLM8);

  //addMCSample(TTJets,    "t#bar{t}+Jets", kBlue,   0,   0, sTTJets);

  //-------------------------------------------------------------------------------------------------------------------
  // addMuSample(TFile* sample, TString name, double weight, int lc, int fc, int fs);
  //-------------------------------------------------------------------------------------------------------------------

  //addMuSample(MuHad, "MuHad", 1, 0, 0);
  addMuSample(TTJets, "semilep t#bar{t}", kBlue, 0, 0);

  //-------------------------------------------------------------------------------------------------------------------
  // addElSample(TFile* sample, TString name, double weight, int lc, int fc, int fs);
  //-------------------------------------------------------------------------------------------------------------------

  //addElSample(ElHad, "ElHad", 1, 0, 0);

  //-------------------------------------------------------------------------------------------------
  // push back selection steps to vector<TString> Selections and DataSelection;
  //-------------------------------------------------------------------------------------------------

  std::cout << "Test1" << std::endl;

//   MCMuSelections.push_back("analyzeSUSY1l_jetSelection_TTJets");
//   MCMuSelections.push_back("analyzeSUSY1l_HTSelection_TTJets");
//   MCMuSelections.push_back("analyzeSUSY1l_METSelection_TTJets");

//   DataMuSelections.push_back("analyzeSUSY1l_jetSelection_SemiLep");
//   DataMuSelections.push_back("analyzeSUSY1l_HTSelection_SemiLep");
//   DataMuSelections.push_back("analyzeSUSY1l_METSelection_SemiLep");

  MCMuSelections.push_back("analyzeCorrelation1l_HT400ToInf");

  DataMuSelections.push_back("analyzeCorrelation1l_HT400ToInf");

//   MCMuSelections.push_back("analyzeCorrelation1l_HT300ToInf_MET100ToInf");
//   MCMuSelections.push_back("analyzeCorrelation1l_HT300ToInf_MET150ToInf");

//   DataMuSelections.push_back("analyzeCorrelation1l_HT300ToInf_MET100ToInf");
//   DataMuSelections.push_back("analyzeCorrelation1l_HT300ToInf_MET150ToInf");

//   DataMuSelections.push_back("analyzeSUSY1m_leptonSelection");
//   DataMuSelections.push_back("analyzeSUSY1m_jetSelection");

  //-------------------------------------------------------------------------------------------------
  // push back histograms to vector<int> Histograms and DataHistograms;
  //-------------------------------------------------------------------------------------------------

  std::cout << "Test2" << std::endl;

  // MC
  //addMCHistogram("nLeptons",  1, 1, 1, 1);
  addMCHistogram("nJets",     1, 1, 1, 1);
  addMCHistogram("mT",        1, 1, 1, 1);
  addMCHistogram("MET",       1, 1, 1, 1);
  addMCHistogram("HT",        1, 1, 1, 1);

  //addMCHistogram("YMET",      1, 1, 1, 1);
  //addMCHistogram("mlb",       1, 1, 1, 1);

  addDataHistogram("nJets",     1, 1, 1, 1);
  addDataHistogram("mT",        1, 1, 1, 1);
  addDataHistogram("MET",       1, 1, 1, 1);
  addDataHistogram("HT",        1, 1, 1, 1);
  //addDataHistogram("YMET",      1, 1, 1, 1);
  //addDataHistogram("mlb",       1, 1, 1, 1);


//   addMCHistogram("nBjets_2",    1, 1, 1, 1);
//   addMCHistogram("HT",     1, 1, 1, 1);
//   addMCHistogram("MET",    1, 1, 1, 1);

//   // data
//   //addDataHistogram("nLeptons", 1, 1, 1, 1);
//   addDataHistogram("nJets",    1, 1, 1, 1);
//   addDataHistogram("nBjets_2",   1, 1, 1, 1);
//   addDataHistogram("HT",     1, 1, 1, 1);
//   addDataHistogram("MET",    1, 1, 1, 1);

  //--------
  // Plot
  //--------

  plotSet plots("Name");
  
  // Loop over muon selections
  for(int sdx=0; sdx<(int)MCMuSelections.size(); ++sdx)
    {
      std::cout << MCMuSelections[sdx] << std::endl;
      
      // Loop over histogram
      for(int h=0; h<(int)MCHistograms.size(); ++h)
	{ 
	  std::cout << MCHistograms[h] << std::endl;
	  
	  // Loop over MC samples
	  for(int i=0; i<(int)MCFiles.size(); ++i)
	    {
	      plots.addPlot((TH1F*)MCFiles[i]->Get(MCMuSelections[sdx]+"/"+MCHistograms[h]),MCNames[i],MCHistograms[h]+"_"+MCMuSelections[sdx],MuLumi*Weights[i],MCLineColors[i],MCFillStyles[i],MCFillColors[i]);
	    }      
	  
	  // loop over muon data samples
	  for(int i=0; i<(int)MuFiles.size(); ++i)
	    {
	      plots.addPlot((TH1F*)MuFiles[i]->Get(DataMuSelections[sdx]+"/"+DataHistograms[h]),MuNames[i],MCHistograms[h]+"_"+MCMuSelections[sdx],MuLumi*sTTJets,MuLineColors[i],MuFillStyles[i],MuFillColors[i]);
	    }
	}
    }
  plots.SetAxesTitles("mT_analyzeCorrelation1l_HT300ToInf_MET100ToInf", "m_{T} [GeV]", "events");
  plots.SetAxesTitles("nJets_analyzeCorrelation1l_HT300ToInf_MET100ToInf", "Number of jets", "events");
  plots.SetAxesTitles("mT_analyzeCorrelation1l_HT300ToInf_MET150ToInf", "m_{T} [GeV]", "events");
  plots.SetAxesTitles("nJets_analyzeCorrelation1l_HT300ToInf_MET150ToInf", "Number of jets", "events");

  plots.printAll("ylog");
}
