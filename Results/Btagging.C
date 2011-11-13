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

vector<TFile*> DataFiles;
vector<TString> DataNames;
vector<double> DataWeights;
vector<unsigned int> DataLineColors;
vector<unsigned int> DataFillColors;
vector<unsigned int> DataFillStyles;

vector<TString> Histograms;
vector<double> XminN;
vector<double> XmaxN;
vector<double> XminR;
vector<double> XmaxR;

vector<TString> DataHistograms;
vector<double> DataXminN;
vector<double> DataXmaxN;
vector<double> DataXminR;
vector<double> DataXmaxR;

vector<TString> Selections;
vector<TString> DataSelections;

vector<double> Scales;

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

void addDataSample(TFile* sample, TString name, double weight, int lc, int fc, int fs);

void addDataSample(TFile* sample, TString name, double weight, int lc, int fc, int fs)
{
  DataFiles.push_back(sample);
  DataNames.push_back(name);
  DataWeights.push_back(weight);
  DataLineColors.push_back(lc);
  DataFillColors.push_back(fc);
  DataFillStyles.push_back(fs);
}

void addHistogram(TString name, int xminN, int xmaxN, int xminR, int xmaxR);

void addHistogram(TString name, int xminN, int xmaxN, int xminR, int xmaxR)
{
  Histograms.push_back(name);
  XminN.push_back(xminN);
  XmaxN.push_back(xmaxN);
  XminR.push_back(xminR);
  XmaxR.push_back(xmaxR);
}

void addDataHistogram(TString name, int xminN, int xmaxN, int xminR, int xmaxR);

void addDataHistogram(TString name, int xminN, int xmaxN, int xminR, int xmaxR)
{
  DataHistograms.push_back(name);
  DataXminN.push_back(xminN);
  DataXmaxN.push_back(xmaxN);
  DataXminR.push_back(xminR);
  DataXmaxR.push_back(xmaxR);
}

int Btagging()
{

  // Normalize background to data? -1: No histogram normalized, 0: only specified normalized, +1: all normalized
  int Normalize=0;
  
  //--------------------------------------------------------------
  // Samples and event weights
  //--------------------------------------------------------------

  TFile* TTJets=new TFile("TTJets.root","READ");
  TFile* SingleTop=new TFile("SingleTop.root","READ");
  TFile* WJets=new TFile("WJets.root","READ");
  TFile* DY=new TFile("DY.root","READ");
  TFile* QCD=new TFile("QCD.root","READ");
  TFile* LM3=new TFile("LM3.root","READ");

  TFile* SM=new TFile("SM.root","READ");

  TFile* MuHad=new TFile("MuHad.root","READ");
  TFile* ElHad=new TFile("ElHad.root","READ");

  //TFile* SM=new TFile("SM.root","READ");

  // Luminosity for MuHad in fb^-1
  //Double_t Lumi=4.123723;
  //Double_t Lumi=2.165723;
  //Double_t Lumi=1.958;
  //Double_t Lumi=0.661;

  // Luminosity for ElHad in fb^-1
  Double_t Lumi=4.190583;

  Int_t NGQCD=1;
  Double_t XSQCD=1;
  
  Int_t NGTTJets=3701947;
  Double_t XSTTJets=157.5;
  
  Int_t NGDY=36277961;
  Double_t XSDY=3048;
  
  Int_t NGWJets=81352581;
  Double_t XSWJets=31314; 
  
  Int_t NGSingleTop=1; 
  Double_t XSSingleTop=1;
  
  Int_t NGLM3=36475;
  Double_t XSLM3=3.438;
  
  Int_t NGLM8=10595;
  Double_t XSLM8=0.73;
  
  Int_t NGLM9=79665;
  Double_t XSLM9=7.134;
  
  Double_t WeightQCD=(Lumi*(XSQCD))/NGQCD;
  Double_t WeightTTJets=(Lumi*(XSTTJets))/NGTTJets;
  Double_t WeightDY=(Lumi*(XSDY))/NGDY;
  Double_t WeightWJets=(Lumi*(XSWJets))/NGWJets;
  Double_t WeightSingleTop=(Lumi*XSSingleTop)/NGSingleTop;
  Double_t WeightLM3=(Lumi*(XSLM3))/NGLM3;
  Double_t WeightLM8=(Lumi*(XSLM8))/NGLM8;
  Double_t WeightLM9=(Lumi*(XSLM9))/NGLM9;
  
  //-------------------------------------------------------------------------------------------------------------------
  // addSample (TFile* sample, TString name, double weight, int lc, int fc, int fs)
  //-------------------------------------------------------------------------------------------------------------------

  addSample(QCD,       "QCD",           Lumi, kBlue-7,  kBlue-7,  1101);
  addSample(DY,        "DY+Jets",       Lumi, kGreen+2, kGreen+2, 1101);
  addSample(WJets,     "W+Jets",        Lumi, kYellow,  kYellow,  1101);
  addSample(SingleTop, "Single Top",    Lumi, kRed+2,   kRed+2,   1101);
  addSample(TTJets,    "T#bar{T}+Jets", Lumi, kRed,     kRed,     1101);
  //addSample(LM3,       "LM3",           Lumi, kBlue,    0,        0);

  addSample(ElHad,     "ElHad",    1,    1,        0,        0);

  //-------------------------------------------------------------------------------------------------
  // push back selection step to vector<TString> Selections and DataSelection;
  //-------------------------------------------------------------------------------------------------

//   Selections.push_back("analyzeBtagsRA4bMuTCHEM3");
//   Selections.push_back("analyzeBtagsMuTCHEM3");
//   Selections.push_back("analyzeBtagsMuTCHEM3highPt");
//   Selections.push_back("analyzeBtagsMuTCHEM3highPtdilep");
  
//   DataSelections.push_back("analyzeBtagsRA4bMuTCHEM3");
//   DataSelections.push_back("analyzeBtagsMuTCHEM3");
//   DataSelections.push_back("analyzeBtagsMuTCHEM3highPt");
//   DataSelections.push_back("analyzeBtagsMuTCHEM3highPtdilep");

  Selections.push_back("analyzeBtagsRA4bElTCHEM3");
  Selections.push_back("analyzeBtagsElTCHEM3");
  Selections.push_back("analyzeBtagsElTCHEM3highPt");
  Selections.push_back("analyzeBtagsElTCHEM3highPtdilep");

  DataSelections.push_back("analyzeBtagsRA4bElTCHEM3");
  DataSelections.push_back("analyzeBtagsElTCHEM3");
  DataSelections.push_back("analyzeBtagsElTCHEM3highPt");
  DataSelections.push_back("analyzeBtagsElTCHEM3highPtdilep");

  //-------------------------------------------------------------------------------------------------
  // push back histogram to vector<int> Histograms and DataHistograms;
  //-------------------------------------------------------------------------------------------------

  //addHistogram("btagWeights", 1, 1, 1, 1);
  //addHistogram("nBtags", 1, 1, 1, 1);
  //addHistogram("BtagsPt_btagWeight", 1, 1, 1, 1);
  //addHistogram("BtagsPt_btagWeight", 1, 1, 1, 1);
  //addHistogram("MET", 1, 1, 1, 1);
  //addHistogram("BtagsEta", 1, 1, 1, 1);
  //addHistogram("BtagsEta_btagWeight", 1, 1, 1, 1);
  addHistogram("NrHighPtBtags", 1, 1, 1, 1);
  addHistogram("NrLowPtBtags", 1, 1, 1, 1);
  //addHistogram("NrHighPtJets", 1, 1, 1, 1);
  //addHistogram("NrLowPtJets", 1, 1, 1, 1);
  //addHistogram("NrJets", 1, 1, 1, 1);
  addHistogram("NrBtags", 1, 1, 1, 1);
  //addHistogram("BtagsPt_btagWeight", 1, 1, 1, 1);
 
  //addDataHistogram("nBtags", 1, 1, 1, 1);
  //addDataHistogram("nBtags", 1, 1, 1, 1);
  //addDataHistogram("BtagsPt", 1, 1, 1, 1);
  //addDataHistogram("BtagsPt", 1, 1, 1, 1);
  //addDataHistogram("MET", 1, 1, 1, 1);
  //addDataHistogram("BtagsEta", 1, 1, 1, 1);
  //addDataHistogram("BtagsEta", 1, 1, 1, 1);
   addDataHistogram("NrHighPtBtags", 1, 1, 1, 1);
   addDataHistogram("NrLowPtBtags", 1, 1, 1, 1);
   //addDataHistogram("NrHighPtJets", 1, 1, 1, 1);
   //addDataHistogram("NrLowPtJets", 1, 1, 1, 1);
   //addDataHistogram("NrJets", 1, 1, 1, 1);
   addDataHistogram("NrBtags", 1, 1, 1, 1);
  //addDataHistogram("BtagsPt", 1, 1, 1, 1);

  //===========================================================================
  //================================ BAUSTELLE ================================
  //===========================================================================

  double SF=1;

//   TH1F* HistMC=(TH1F*)SM->Get(Selections[0]+"/"+Histograms[0]);
//   double AllMC=Lumi*HistMC->Integral(5,24);
  
//   double AllMCErr=Lumi*sqrt(1000);

//   TH1F* HistData=(TH1F*)MuHad->Get(DataSelections[0]+"/"+DataHistograms[0]);
//   double Data=HistData->Integral(5,24);
//   double DataErr=sqrt(Data);

//   double SF=Data/AllMC;

//   double SFErr=sqrt(pow(DataErr/AllMC,2) + pow(Data*AllMCErr/(AllMC*AllMC),2));

//   std::cout << SF << " +- " << SFErr << std::endl;

//   //-------------------------------------------------------

  
//   double AllMCRatio=SF*Lumi*(HistMC->Integral(25,49));
  
//   double AllMCRatioErr=sqrt(pow(SF*Lumi*sqrt(30),2)+ pow(SFErr*Lumi*(HistMC->Integral(25,49)),2));

//   std::cout << AllMCRatioErr << std::endl;
//   std::cout << SF*Lumi*sqrt(30) << std::endl;
//   std::cout << SFErr*Lumi*(HistMC->Integral(25,49)) << std::endl;

//   double DataRatio=HistData->Integral(25,49);
//   double DataRatioErr=sqrt(DataRatio);

//   double Ratio=DataRatio/AllMCRatio;



//   double RatioErr=sqrt(pow(DataRatioErr/AllMCRatio,2) + pow(DataRatio*AllMCRatioErr/(AllMCRatio*AllMCRatio),2));

//   std::cout << DataRatioErr/AllMCRatio << std::endl;
//   std::cout << DataRatio*AllMCRatioErr/(AllMCRatio*AllMCRatio)  << std::endl;
//   //std::cout <<  << std::endl;

//   std::cout << Ratio << " +- " << RatioErr << std::endl;


  //--------
  // Plot
  //--------

  plotSet plots("Name");

  for(int sdx=0; sdx<Selections.size(); ++sdx)
    {
      for(int h=0; h<Histograms.size(); ++h)
	{ 
	  std::cout << Histograms[h] << std::endl;
	  
	  // loop over f-s MC background files
	  for(int i=0; i<(int)Files.size()-1; ++i)
	    {
	      plots.addPlot((TH1F*)Files[i]->Get(Selections[sdx]+"/"+Histograms[h]),Names[i],Histograms[h]+"_"+Selections[sdx],SF*Weights[i],LineColors[i],FillStyles[i],FillColors[i]);
	    }      
	  
	  // loop over data files
	  for(int i=Files.size()-1; i<(int)Files.size(); ++i)
	    {
	      plots.addPlot((TH1F*)Files[i]->Get(DataSelections[sdx]+"/"+DataHistograms[h]),Names[i],Histograms[h]+"_"+Selections[sdx],Weights[i],LineColors[i],FillStyles[i],FillColors[i]);
	    }  
	}
    }
  plots.printAll("ylog");
}
