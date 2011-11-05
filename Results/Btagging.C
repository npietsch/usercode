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
  TFile* MuHad=new TFile("MuHad.root","READ");

  TFile* SM=new TFile("SM.root","READ");

  // Luminosity for MuHad
  Int_t Luminosity=2960;
  //Int_t Luminosity=3652.723;

  // Luminosity for ElHad
  //Int_t Luminosity=2166;
  //Int_t Luminosity=3610.583;

  Int_t NGQCD=1;
  Double_t XSQCD=0.001;
  
  Int_t NGTTJets=3701947;
  Double_t XSTTJets=157.5;
  
  Int_t NGDY=36277961;
  Double_t XSDY=3048;
  
  Int_t NGWJets=81352581;
  Double_t XSWJets=31314; 
  
  Int_t NGSingleTop=1; 
  Double_t XSSingleTop=0.001;
  
  Int_t NGLM3=36475;
  Double_t XSLM3=3.438;
  
  Int_t NGLM8=10595;
  Double_t XSLM8=0.73;
  
  Int_t NGLM9=79665;
  Double_t XSLM9=7.134;
  
  Double_t WeightQCD=(Luminosity*(XSQCD))/NGQCD;
  Double_t WeightTTJets=(Luminosity*(XSTTJets))/NGTTJets;
  Double_t WeightDY=(Luminosity*(XSDY))/NGDY;
  Double_t WeightWJets=(Luminosity*(XSWJets))/NGWJets;
  Double_t WeightSingleTop=(Luminosity*XSSingleTop)/NGSingleTop;
  Double_t WeightLM3=(Luminosity*(XSLM3))/NGLM3;
  Double_t WeightLM8=(Luminosity*(XSLM8))/NGLM8;
  Double_t WeightLM9=(Luminosity*(XSLM9))/NGLM9;
  
  //-------------------------------------------------------------------------------------------------------------------
  // addSample (TFile* sample, TString name, double weight, int lc, int fc, int fs)
  //-------------------------------------------------------------------------------------------------------------------

  addSample(QCD,       "QCD",           1, kBlue-7,  kBlue-7,  1101);
  addSample(DY,        "DY+Jets",       1, kGreen+2, kGreen+2, 1101);
  addSample(WJets,     "W+Jets",        1, kYellow,  kYellow,  1101);
  addSample(SingleTop, "Single Top",    1, kRed+2,   kRed+2,   1101);
  addSample(TTJets,    "T#bar{T}+Jets", 1, kRed,     kRed,     1101);

  addDataSample(MuHad,      "MuHad",    1, 1,        0,        0);

  //-------------------------------------------------------------------------------------------------
  // push back selection step to vector<TString> Selections and DataSelection;
  //-------------------------------------------------------------------------------------------------

  Selections.push_back("analyzeBtagsSSVHEM3");

  DataSelections.push_back("analyzeBtagsSSVHEM3");

  //-------------------------------------------------------------------------------------------------
  // push back histogram to vector<int> Histograms and DataHistograms;
  //-------------------------------------------------------------------------------------------------

  addHistogram("btagWeights_noWgt", 1, 1, 1, 1);
  addHistogram("btagWeights", 1, 1, 1, 1);
  
  addDataHistogram("nBtags_noWgt", 1, 1, 1, 1);
  addDataHistogram("nBtags", 1, 1, 1, 1);

  //===========================================================================
  //================================ BAUSTELLE ================================
  //===========================================================================


  //--------------------------------------------------------------
  // Calculate scale factors and ratios
  //--------------------------------------------------------------

  for(int h=0; h<(int)Histograms.size(); ++h)
    {
      double AllData=0;
      double AllMC=0;
      double AllDataErr=0;
      double AllMCErr=0;
      
      double CombinedRatio=1;
      double CombinedRatioErr=0;
      
      for(int sel=0; sel<(int)Selections.size(); ++sel)
	{
	  std::cout << "----------------------------------" << std::endl;
	  std::cout << Histograms[h] << std::endl;
	  std::cout << "----------------------------------" << std::endl;

	  double xmin=XminN[h];
	  double xmax=XmaxN[h];
	  
	  // if no histogram should be normalized
	  if(Normalize==-1)
	    {
	      xmin=0;
	      xmax=0;
	    }
	  // if all histograms should be normalized
	  if(Normalize==1)
	    {
	      if(xmin==0 && xmax==0)
		{
	      xmin=1;
	      xmax=1;
		}
	    }
	  
	  // if MC background should not be normalized to data
	  if(xmin==0 && xmax==0)
	    {
	      Scales.push_back(1);
	      std::cout << "Scale factor: 1"  << std::endl;
	    }
	  else
	    {
	      // if MC background should be normalized to data in whole region
	      if(xmin==1 && xmax==1)
		{
		  xmin=0;
		  TH1F* Hist=(TH1F*)SM->Get(Selections[sel]+"/"+Histograms[h]);
		  xmax=Hist->GetNbinsX()+1;
		}

	      double MC=Luminosity*(hist->Integral(xmin,xmax));
	      double MCErr=sqrt(hist->GetEntries());


	    }

	}

    }

  //===========================================================================
  //================================ BAUSTELLE ================================
  //===========================================================================



//   //--------------------------------------------------------------
//   // Calculate scale factors and ratios
//   //--------------------------------------------------------------

//   double xmin2=25;
//   double xmax2=5;

//   for(int h=0; h<(int)Histograms.size(); ++h)
//     {
//       double DataSum=0;
//       double AllMC=0;
//       double DataSumErr=0;
//       double AllMCErr=0;
      
//       double CombinedRatio=1;
//       double CombinedRatioErr=0;
      
//       for(int sel=0; sel<(int)Selections.size(); ++sel)
// 	{ 
// 	  std::cout << "----------------------------------" << std::endl;
// 	  std::cout << Histograms[h] << std::endl;
// 	  std::cout << "----------------------------------" << std::endl;
	  
// 	  double xmin=Xmin[h];
// 	  double xmax=Xmax[h];
	  
// 	  // if no histogram should be normalized
// 	  if(Normalize==-1)
// 	    {
// 	      xmin=0;
// 	      xmax=0;
// 	    }
// 	  // if all histograms should be normalized
// 	  if(Normalize==1)
// 	    {
// 	      if(xmin==0 && xmax==0)
// 		{
// 	      xmin=1;
// 	      xmax=1;
// 		}
// 	    }
	  
// 	  // if MC background should not be normalized to data
// 	  if(xmin==0 && xmax==0)
// 	    {
// 	      Scales.push_back(1);
// 	      std::cout << "Scale factor: 1"  << std::endl;
// 	    }
// 	  else
// 	    {
// 	      // if MC background should be normalized to data in whol region
// 	      if(xmin==1 && xmax==1)
// 		{
// 		  xmin=0;
// 		  TH1F* Hist=(TH1F*)Files[0]->Get(Selections[sel]+"/"+Histograms[h]);
// 		  xmax=Hist->GetNbinsX()+1;
// 		}
	      
// 	      double MCSum=0;
// 	      double MCSumErr=0;
// 	      double Data=0;
// 	      double DataErr=0;
// 	      double SF=1;
// 	      double SFErr=0;
	      
// 	      double MCSum2=0;
// 	      double MCSum2Err=0;
// 	      double Data2=0;
// 	      double Data2Err=0;
// 	      double Ratio=1;
// 	      double RatioErr=0;
	      
// 	      for(int mcx=0; mcx<(f-s); ++mcx)
// 		{
// 		  TH1F* hist=(TH1F*)Files[mcx]->Get(Selections[sel]+"/"+Histograms[h]);
// 		  double Int=(Weights[mcx])*(hist->Integral(xmin,xmax));
// 		  double Err=(Weights[mcx])*(sqrt(hist->Integral(xmin,xmax)));
// 		  MCSum=MCSum+Int;
// 		  MCSumErr=MCSumErr+Err;
		  
// 		  double Int2=(Weights[mcx])*(hist->Integral(xmin2,xmax2));
// 		  double Err2=(Weights[mcx])*(sqrt(hist->Integral(xmin2,xmax2)));
// 		  MCSum2=MCSum2+Int2;
// 		  MCSum2Err=MCSum2Err+Err2;
// 		}   
 
// 	      int ddx=0;

// 	      if(sel==0) ddx=f-s;
// 	      if(sel==1) ddx=f-s+1;

// 	      TH1F* hist=(TH1F*)Files[ddx]->Get(DataSelections[0]+"/"+Histograms[h]);	  
// 	      Data=hist->Integral(xmin,xmax);
// 	      Data2=hist->Integral(xmin2,xmax2);
	      
// 	      DataErr=sqrt(Data);
// 	      Data2Err=sqrt(Data2);
	      
// 	      SF=Data/MCSum;
// 	      Scales.push_back(SF);
// 	      SFErr=sqrt(pow((DataErr/MCSum),2)+pow((Data*MCSumErr/(MCSum*MCSum)),2));	  
// 	      std::cout << "Scale factor for " << Names[ddx] << ": " << SF << " +- " << SFErr<< std::endl;
	      
// 	      Ratio=Data2/(SF*MCSum2);
	      
// 	      RatioErr=sqrt(pow((Data2Err/(SF*MCSum2)),2)+pow((Data2*SFErr/(SF*SF*MCSum2)),2)+pow((Data2*MCSum2Err/(SF*MCSum2*MCSum2)),2));
	      
// 	      std::cout << "Ratio for " << Names[ddx] << ": " << Ratio << " +- " << RatioErr << std::endl;
	      
// 	      //Backgrounds.push_back(SF*MCSum2);
// 	      //BackgroundsErr.push_back(sqrt(pow((SFErr*MCSum2),2)+pow((SF*MCSum2Err),2)));
	      
// 	      DataSum=DataSum+Data2;
// 	      AllMC=AllMC+SF*MCSum2;
// 	      AllMCErr=AllMCErr+sqrt(pow((SFErr*MCSum2),2)+pow((SF*MCSum2Err),2));

// 	      std::cout << "Data2: " << Data2 << std::endl;
// 	      std::cout << "DataSum: " << DataSum << std::endl;

// 	      std::cout << "MCSum2: " << MCSum2 << std::endl;
// 	      std::cout << "AllMC: " << AllMC << std::endl;

// 	      std::cout << "MCErr: " << sqrt(pow((SFErr*MCSum2),2)+pow((SF*MCSum2Err),2)) << std::endl;
// 	      std::cout << "AllMCErr: " << AllMCErr << std::endl;

// 	    }		     
// 	}

//       CombinedRatio=DataSum/AllMC;
//       DataSumErr=sqrt(DataSum);
//       CombinedRatioErr=sqrt(pow((DataSumErr/AllMC),2)+pow((DataSum*AllMCErr/(AllMC*AllMC)),2));
      
//       std::cout << "DataSum: " << DataSum << std::endl;
//       std::cout << "DataSumErr: " << DataSumErr << std::endl;

//       std::cout << "AllMC: " << AllMC << std::endl;
//       std::cout << "AllMCErr: " << AllMCErr << std::endl;

//       std::cout << pow((DataSumErr*AllMC),2) << std::endl;

//       std::cout << pow((DataSum*AllMCErr),2) << std::endl;

//       std::cout << "Combined ratio:" << CombinedRatio << " +- " << CombinedRatioErr << std::endl;  
//     }

  //--------
  // Plot
  //--------

  plotSet plots("Name");

  for(int h=0; h<Histograms.size(); ++h)
    { 
      std::cout << Histograms[h] << std::endl;
      
      // loop over f-s MC background files
      for(int i=0; i<Files.size(); ++i)
	{
	  plots.addPlot((TH1F*)Files[i]->Get(Selections[0]+"/"+Histograms[h]),Names[i],Histograms[h]+"_"+Selections[0],Weights[i],LineColors[i],FillStyles[i],FillColors[i]);
	}      
      
      // loop over s MC and data signal files
      for(int i=0; i<DataFiles.size(); ++i)
	{
	  plots.addPlot((TH1F*)Files[i]->Get(DataSelections[0]+"/"+DataHistograms[h]),Names[i],Histograms[h]+"_"+Selections[0],Weights[i],LineColors[i],FillStyles[i],FillColors[i]);
	}       
    }
  
  plots.printAll("ylog");
}
