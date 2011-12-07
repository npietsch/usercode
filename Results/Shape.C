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
vector<double> MCMuWeights;
vector<double> MCElWeights;
vector<unsigned int> MCLineColors;
vector<unsigned int> MCFillColors;
vector<unsigned int> MCFillStyles;

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
void addMCSample(TFile* sample, TString name, double MuWeight, double ElWeight,  int lc, int fc, int fs);

void addMCSample(TFile* sample, TString name, double MuWeight, double ElWeight,  int lc, int fc, int fs)
{
  MCFiles.push_back(sample);
  MCNames.push_back(name);
  MCMuWeights.push_back(MuWeight);
  MCElWeights.push_back(ElWeight);
  MCLineColors.push_back(lc);
  MCFillColors.push_back(fc);
  MCFillStyles.push_back(fs);
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
int Btagging()
{

  // Normalize background to data? -1: No histogram normalized, 0: only specified normalized, +1: all normalized
  int Normalize=0;
  
  // Initialize scale factors
  double MuSF=1;
  double ElSF=1;

  //--------------------------------------------------------------
  // Samples and luminosity
  //--------------------------------------------------------------

  TFile* Test=new TFile("Test.root","READ");

//   TFile* TTJets=new TFile("TTJets.root","READ");
//   TFile* SingleTop=new TFile("SingleTop.root","READ");
//   TFile* WJets=new TFile("WJets.root","READ");
//   TFile* DY=new TFile("DY.root","READ");
//   TFile* QCD=new TFile("QCD.root","READ");
//   TFile* LM3=new TFile("LM3.root","READ");

//   TFile* SM=new TFile("SM.root","READ");

//   TFile* MuHad=new TFile("MuHad.root","READ");
//   TFile* ElHad=new TFile("ElHad.root","READ");

  // Luminosity for MuHad in fb^-1
  Double_t MuLumi=4.123723;

  // Luminosity for ElHad in fb^-1
  Double_t ElLumi=4.190583;

  //-------------------------------------------------------------------------------------------------------------------
  // addMCSample (TFile* sample, TString name, double weight, int lc, int fc, int fs)
  //-------------------------------------------------------------------------------------------------------------------

  addMCSample(QCD,       "QCD",           MuLumi, ElLumi, kBlue-7,  kBlue-7,  0);

//   addMCSample(QCD,       "QCD",           MuLumi, ElLumi, kBlue-7,  kBlue-7,  1101);
//   addMCSample(DY,        "DY+Jets",       MuLumi, ElLumi, kGreen+2, kGreen+2, 1101);
//   addMCSample(WJets,     "W+Jets",        MuLumi, ElLumi, kYellow,  kYellow,  1101);
//   addMCSample(SingleTop, "Single Top",    MuLumi, ElLumi, kRed+2,   kRed+2,   1101);
//   addMCSample(TTJets,    "T#bar{T}+Jets", MuLumi, ElLumi, kRed,     kRed,     1101);
  
  //-------------------------------------------------------------------------------------------------------------------
  // addMuSample(TFile* sample, TString name, double weight, int lc, int fc, int fs);
  //-------------------------------------------------------------------------------------------------------------------

//   addMuSample(MuHad, "MuHad", 1, 0, 0);

  //-------------------------------------------------------------------------------------------------------------------
  // addElSample(TFile* sample, TString name, double weight, int lc, int fc, int fs);
  //-------------------------------------------------------------------------------------------------------------------

//   addElSample(ElHad, "ElHad", 1, 0, 0);

  //-------------------------------------------------------------------------------------------------
  // push back selection step to vector<TString> Selections and DataSelection;
  //-------------------------------------------------------------------------------------------------

  MCMuSelections.push_back("analyzeBtagsRA4bMuTCHEM3noSF");
  MCMuSelections.push_back("analyzeBtagsRA4bMuSSVHEM3noSF");

  DataMuSelections.push_back("analyzeBtagsRA4bMuTCHEM3");
  DataMuSelections.push_back("analyzeBtagsRA4bMuSSVHEM3");
 
  MCElSelections.push_back("analyzeBtagsRA4bElTCHEM3noSF");
  MCElSelections.push_back("analyzeBtagsRA4bElSSVHEM3noSF");
  
  DataElSelections.push_back("analyzeBtagsRA4bElTCHEM3");
  DataElSelections.push_back("analyzeBtagsRA4bElSSVHEM3");

  //-------------------------------------------------------------------------------------------------
  // push back histogram to vector<int> Histograms and DataHistograms;
  //-------------------------------------------------------------------------------------------------

  
  addMCHistogram("BtagsPt_btagWeight", 1, 1, 1, 1);
  addMCHistogram("NrHighPtBtags",  1, 1, 1, 1);
  
  addDataHistogram("BtagsPt", 1, 1, 1, 1);
  addDataHistogram("NrHighPtBtags",  1, 1, 1, 1);

  //===========================================================================
  //================================ BAUSTELLE ================================
  //===========================================================================

  // muon channel
  TH1F* MCMuHist1=(TH1F*)SM->Get(MCMuSelections[0]+"/BtagsPt_btagWeight");
  TH1F* MCMuHist2=(TH1F*)SM->Get(MCMuSelections[0]+"/BtagPtBins_btagWeight");

  std::cout << "MCMuHist1->Integral(5,24): " << MCMuHist1->Integral(5,24)<< std::endl;
  std::cout << "MCMuHist2->Integral(1,1): " << MCMuHist2->Integral(1,1)<< std::endl;

  double MCMuInt=MuLumi*MCMuHist1->Integral(5,24);
  double MCMuIntErr=MuLumi*MCMuHist2->GetBinError(1);
 
  TH1F* DataMuHist=(TH1F*)MuHad->Get(DataMuSelections[0]+"/BtagsPt");
  double DataMuInt=DataMuHist->Integral(5,24);
  double DataMuIntErr=sqrt(DataMuInt);
  
  MuSF=DataMuInt/MCMuInt;
  
  double MuSFErr=sqrt(pow(DataMuIntErr/MCMuInt,2) + pow(DataMuInt*MCMuIntErr/(MCMuInt*MCMuInt),2));
  
  std::cout << MuSF << " +- " << MuSFErr << std::endl;

  //-------------------------------------------------------

  double MCMuRatio=MuSF*MuLumi*(MCMuHist1->Integral(25,49));
  double MCMuRatioErr=sqrt(pow(MuSF*MuLumi*(MCMuHist2->GetBinError(2)),2)+ pow(MuSFErr*MuLumi*(MCMuHist1->Integral(25,49)),2));

  std::cout << MCMuRatioErr << std::endl;

  double DataMuRatio=DataMuHist->Integral(25,49);
  double DataMuRatioErr=sqrt(DataMuRatio);

  std::cout << DataMuRatioErr << std::endl;

  double MuRatio=DataMuRatio/MCMuRatio;

  double MuRatioErr=sqrt(pow(DataMuRatioErr/MCMuRatio,2) + pow(DataMuRatio*MCMuRatioErr/(MCMuRatio*MCMuRatio),2));

  std::cout << DataMuRatioErr/MCMuRatio << std::endl;
  std::cout << DataMuRatio*MCMuRatioErr/(MCMuRatio*MCMuRatio)  << std::endl;
  std::cout << " " << std::endl;
  
  std::cout << MuRatio << " +- " << MuRatioErr << std::endl  << std::endl;


  //============================================================================================================

  // electron channel
  TH1F* MCElHist1=(TH1F*)SM->Get(MCElSelections[0]+"/BtagsPt_btagWeight");
  TH1F* MCElHist2=(TH1F*)SM->Get(MCElSelections[0]+"/BtagPtBins_btagWeight");

  std::cout << "MCElHist1->Integral(5,24): " << MCElHist1->Integral(5,24)<< std::endl;
  std::cout << "MCElHist2->Integral(1,1): " << MCElHist2->Integral(1,1)<< std::endl;

  double MCElInt=ElLumi*MCElHist1->Integral(5,24);
  double MCElIntErr=ElLumi*MCElHist2->GetBinError(1);
 
  TH1F* DataElHist=(TH1F*)ElHad->Get(DataElSelections[0]+"/BtagsPt");
  double DataElInt=DataElHist->Integral(5,24);
  double DataElIntErr=sqrt(DataElInt);
  
  ElSF=DataElInt/MCElInt;
  
  double ElSFErr=sqrt(pow(DataElIntErr/MCElInt,2) + pow(DataElInt*MCElIntErr/(MCElInt*MCElInt),2));
  
  std::cout << ElSF << " +- " << ElSFErr << std::endl;

  //-------------------------------------------------------

  double MCElRatio=ElSF*ElLumi*(MCElHist1->Integral(25,49));
  double MCElRatioErr=sqrt(pow(ElSF*ElLumi*(MCElHist2->GetBinError(2)),2)+ pow(ElSFErr*ElLumi*(MCElHist1->Integral(25,49)),2));

  std::cout << MCElRatioErr << std::endl;

  double DataElRatio=DataElHist->Integral(25,49);
  double DataElRatioErr=sqrt(DataElRatio);

  std::cout << DataElRatioErr << std::endl;

  double ElRatio=DataElRatio/MCElRatio;

  double ElRatioErr=sqrt(pow(DataElRatioErr/MCElRatio,2) + pow(DataElRatio*MCElRatioErr/(MCElRatio*MCElRatio),2));

  std::cout << DataElRatioErr/MCElRatio << std::endl;
  std::cout << DataElRatio*MCElRatioErr/(MCElRatio*MCElRatio)  << std::endl;
  std::cout << " " << std::endl;
  
  std::cout << ElRatio << " +- " << ElRatioErr << std::endl  << std::endl;



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
	      plots.addPlot((TH1F*)MCFiles[i]->Get(MCMuSelections[sdx]+"/"+MCHistograms[h]),MCNames[i],MCHistograms[h]+"_"+MCMuSelections[sdx],MuSF*MCMuWeights[i],MCLineColors[i],MCFillStyles[i],MCFillColors[i]);
	    }      
	  
	  // loop over muon data samples
	  for(int i=0; i<(int)MuFiles.size(); ++i)
	    {
	      plots.addPlot((TH1F*)MuFiles[i]->Get(DataMuSelections[sdx]+"/"+DataHistograms[h]),MuNames[i],MCHistograms[h]+"_"+MCMuSelections[sdx],1,MuLineColors[i],MuFillStyles[i],MuFillColors[i]);
	    }
	  
	}
    }
  
  // Loop over electron selections
  for(int sdx=0; sdx<(int)MCElSelections.size(); ++sdx)
    {
      std::cout << MCElSelections[sdx] << std::endl;
	  
      // Loop over histogram
      for(int h=0; h<(int)MCHistograms.size(); ++h)
	{ 
	  std::cout << MCHistograms[h] << std::endl;
	  
	  // Loop over MC samples
	  for(int i=0; i<(int)MCFiles.size(); ++i)
	    {
	      plots.addPlot((TH1F*)MCFiles[i]->Get(MCElSelections[sdx]+"/"+MCHistograms[h]),MCNames[i],MCHistograms[h]+"_"+MCElSelections[sdx],ElSF*MCElWeights[i],MCLineColors[i],MCFillStyles[i],MCFillColors[i]);
	    }      
	  
	  // loop over muon data samples
	  for(int i=0; i<(int)ElFiles.size(); ++i)
	    {
	      plots.addPlot((TH1F*)ElFiles[i]->Get(DataElSelections[sdx]+"/"+DataHistograms[h]),ElNames[i],MCHistograms[h]+"_"+MCElSelections[sdx],1,ElLineColors[i],ElFillStyles[i],ElFillColors[i]);
	    }
	  
	}
    }

  plots.printAll("ylog");
}
