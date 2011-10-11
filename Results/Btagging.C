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
vector<string> Names;
vector<double> Weights;
vector<double> Scales;
vector<double> Xmin;
vector<double> Xmax;
vector<unsigned int> LineColors;
vector<unsigned int> FillColors;
vector<unsigned int> FillStyles;

vector<TString> Selections;
vector<TString> Histograms;

int Btagging()
{
  // Normalize background to data?
  int Normalize=0;

  // Number of signal samples
  int s=1;

  //--------------------------------------------------------------
  // push back files to vector vector<TFile*> Files
  //--------------------------------------------------------------

  std::cout << "Read files" << std::endl;

  Files.push_back (new TFile("QCD.root", "READ"));
  Files.push_back (new TFile("DY.root","READ"));
  Files.push_back (new TFile("WJets.root","READ"));
  Files.push_back (new TFile("SingleTop.root","READ"));
  //Files.push_back (new TFile("FullHadTTBar.root","READ"));
  //Files.push_back (new TFile("TauTTBar.root","READ"));
  //Files.push_back (new TFile("FullLepTTBar.root","READ"));
  //Files.push_back (new TFile("SemiLepTTBar.root","READ"));
  Files.push_back (new TFile("TTJets.root","READ"));

  //Files.push_back (new TFile("LM3.root","READ"));
  //Files.push_back (new TFile("LM8.root","READ"));
  //Files.push_back (new TFile("LM9.root","READ"));
  //Files.push_back (new TFile("LM13.root","READ"));

  Files.push_back (new TFile("MuHad.root","READ"));
  //Files.push_back (new TFile("ElHad.root","READ"));

  int f=Files.size();

  //--------------------------------------------------------------
  // push back names to vector<string> Names
  //--------------------------------------------------------------

  Names.push_back("QCD");
  Names.push_back("Z+Jets");
  Names.push_back("W+Jets");
  Names.push_back("Single top");
  //Names.push_back("Fullhad t#bar{t}");
  //Names.push_back("Tau t#bar{t}");
  //Names.push_back("Di-lep t#bar{t}");
  //Names.push_back("Semilep t#bar{t}");
  Names.push_back("T#bar{T}+Jets");

  //Names.push_back("LM3");
  //Names.push_back("LM8");
  //Names.push_back("LM9");
  //Names.push_back("LM13");

  Names.push_back("MuHad");
  //Names.push_back("ElHad");

  //--------------------------------------------------------------
  // Specify integrated luminosity (in pb^-1) and event weights
  //--------------------------------------------------------------
  
  Int_t Luminosity=2104;
  //Int_t Luminosity=1965;

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

  Int_t NGLM13=77000;
  Double_t XSLM13=6.899;
  
  Double_t WeightQCD=0.001*(Luminosity*(XSQCD))/NGQCD;
  Double_t WeightTTJets=(Luminosity*(XSTTJets))/NGTTJets;
  Double_t WeightDY=(Luminosity*(XSDY))/NGDY;
  Double_t WeightWJets=(Luminosity*(XSWJets))/NGWJets;
  Double_t WeightSingleTop=0.001*Luminosity*XSSingleTop/NGSingleTop;
  Double_t WeightLM3=(Luminosity*(XSLM3))/NGLM3;
  Double_t WeightLM8=(Luminosity*(XSLM8))/NGLM8;
  Double_t WeightLM9=(Luminosity*(XSLM9))/NGLM9;
  Double_t WeightLM13=(Luminosity*(XSLM13))/NGLM13;

  //--------------------------------------------------------------
  // push back event weights to vector<double> Weights;
  //--------------------------------------------------------------

  Weights.push_back(WeightQCD);
  Weights.push_back(WeightDY);
  Weights.push_back(WeightWJets);
  Weights.push_back(WeightSingleTop);
  //Weights.push_back(WeightTTJets);
  //Weights.push_back(WeightTTJets);
  //Weights.push_back(WeightTTJets);
  //Weights.push_back(WeightTTJets);
  Weights.push_back(WeightTTJets);

  //Weights.push_back(WeightLM3);
  //Weights.push_back(WeightLM8);
  //Weights.push_back(WeightLM9);
  //Weights.push_back(WeightLM13);

  Weights.push_back(1);
 //Weights.push_back(1);

  //--------------------------------------------------------------
  // push back line colors to vector<int> LineColors;
  //--------------------------------------------------------------
  LineColors.push_back(kBlue-7);
  LineColors.push_back(kGreen+2);
  LineColors.push_back(kYellow);
  LineColors.push_back(kRed+2);
  LineColors.push_back(kRed);
  LineColors.push_back(1);

  //--------------------------------------------------------------
  // push back fill colors to vector<int> FillColors;
  //--------------------------------------------------------------

  FillColors.push_back(kBlue-7);
  FillColors.push_back(kGreen+2);
  FillColors.push_back(kYellow);
  FillColors.push_back(kRed+2);
  FillColors.push_back(kRed);
  FillColors.push_back(0);

  //--------------------------------------------------------------
  // push back fill style to vector<int> FillStyles;
  //--------------------------------------------------------------

  FillStyles.push_back(1101);
  FillStyles.push_back(1101);
  FillStyles.push_back(1101);
  FillStyles.push_back(1101);
  FillStyles.push_back(1101);
  FillStyles.push_back(0);

  //--------------------------------------------------------------
  // push back selection step to vector<int> Selections;
  //--------------------------------------------------------------

  Selections.push_back("1m_2");

  //--------------------------------------------------------------
  // push back histogram to vector<int> Selections;
  //--------------------------------------------------------------

  Histograms.push_back("JetsPt");

//   Histograms.push_back("LowPtJetsBdisc");
//   Histograms.push_back("HighPtJetsBdisc");
//   Histograms.push_back("NrBtags");
//   Histograms.push_back("LowPtBtagsEta");
//   Histograms.push_back("HighPtBtagsEta");
//   //Histograms.push_back("dPhiBtagMET");
  Histograms.push_back("BtagsPt");
//   Histograms.push_back("BtagsPt_1b");
//   Histograms.push_back("BtagsPt_2b");

  //--------------------------------------------------------------
  // push back regions for normalization
  //--------------------------------------------------------------

  Xmin.push_back(1);
  Xmin.push_back(1);
  Xmin.push_back(1);
  Xmin.push_back(1);
  Xmin.push_back(1);
  Xmin.push_back(4);
  Xmin.push_back(1);
  Xmin.push_back(1);
  
  Xmax.push_back(1);
  Xmax.push_back(1);
  Xmax.push_back(1);
  Xmax.push_back(1);
  Xmax.push_back(1);
  Xmax.push_back(24);
  Xmax.push_back(1);
  Xmax.push_back(1);
  
  //--------------------------------------------------------------
  // Calculate Integrals und push back scale factors
  //--------------------------------------------------------------

  for(int h=0; h<(int)Histograms.size(); ++h)
    {
      double xmin=Xmin[h];
      double xmax=Xmax[h];
      
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
	  // if MC background should be normalized to data in whol region
	  if(xmin==1 && xmax==1)
	    {
	      xmin=0;
	      TH1F* Hist=(TH1F*)Files[0]->Get("analyzeBtags"+Selections[0]+"/"+Histograms[h]);
	      xmax=Hist->GetNbinsX();
	    }
	  
	  double BackgroundSum=0;
	  double Signal=0;
	  double SF=1;
	  
	  for(int mcx=0; mcx<(f-s); ++mcx)
	    {
	      TH1F* hist=(TH1F*)Files[mcx]->Get("analyzeBtags"+Selections[0]+"/"+Histograms[h]);
	      double Int=(Weights[mcx])*(hist->Integral(xmin,xmax));
	      BackgroundSum=BackgroundSum+Int;
	    }    
	  
	  TH1F* hist=(TH1F*)Files[f-s]->Get("analyzeBtags"+Selections[0]+"/"+Histograms[h]);
	  
	  Signal=hist->Integral(xmin,xmax);
	  SF=Signal/BackgroundSum;
	  
	  Scales.push_back(SF);
	  std::cout << "Scale factor:" << SF << std::endl;
	}
    }

  //--------
  // Plot
  //--------

  plotSet plots("Name");

  for(int h=0; h<Histograms.size(); ++h)
    { 
      for(int i=0; i<f-s; ++i)
	{
	  plots.addPlot((TH1F*)Files[i]->Get("analyzeBtags"+Selections[0]+"/"+Histograms[h]),Names[i],Histograms[h]+"_"+Selections[0],Weights[i]*Scales[h],LineColors[i],FillStyles[i],FillColors[i]);
	}       
    }
  
  for(int h=0; h<Histograms.size(); ++h)
    {
      for(int step=0; step<Selections.size(); ++step)
	{
	  for(int i=f-s; i<f; ++i)
	    {
	      plots.addPlot((TH1F*)Files[i]->Get("analyzeBtags"+Selections[0]+"/"+Histograms[h]),Names[i],Histograms[h]+"_"+Selections[0],Weights[i],LineColors[i],FillStyles[i],FillColors[i]);
	    }       
	}
    }
  
  plots.printAll("ylog");
}
