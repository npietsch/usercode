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
vector<TString> DataSelections;
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
  
  Int_t Luminosity=2131; // Muon
  //Int_t Luminosity=2166; // Electron

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

  //--------------------------------------------
  //--------------------------------------------
  // ATTENTION: IS QCD SCALED BY A FACTOR 2?
  //--------------------------------------------
  //--------------------------------------------

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

  Selections.push_back("analyzeBtags1m_2");
  
  DataSelections.push_back("analyzeBtags1l_2");

  //--------------------------------------------------------------
  // push back histogram to vector<int> Selections;
  //--------------------------------------------------------------

  Histograms.push_back("LowPtJetsBdisc");
  Histograms.push_back("HighPtJetsBdisc");
//   Histograms.push_back("NrBtags");
//   Histograms.push_back("LowPtBtagsEta");
//   Histograms.push_back("HighPtBtagsEta");
//   Histograms.push_back("dPhiBtagMET");
//   Histograms.push_back("BtagsPt");
//   Histograms.push_back("JetsPt");
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
  Xmin.push_back(1);
  Xmin.push_back(4);
  Xmin.push_back(4);
  Xmin.push_back(1);
  Xmin.push_back(1);
  
  Xmax.push_back(1);
  Xmax.push_back(1);
  Xmax.push_back(1);
  Xmax.push_back(1);
  Xmax.push_back(1);
  Xmax.push_back(1);
  Xmax.push_back(24);
  Xmax.push_back(24);
  Xmax.push_back(1);
  Xmax.push_back(1);
  
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
      
      for(int i=0; i<f-s; ++i)
	{
	  plots.addPlot((TH1F*)Files[i]->Get(Selections[0]+"/"+Histograms[h]),Names[i],Histograms[h]+"_"+Selections[0],Weights[i],LineColors[i],FillStyles[i],FillColors[i]);

	  //plots.addPlot((TH1F*)Files[i]->Get(Selections[0]+"/"+Histograms[h]),Names[i],Histograms[h]+"_"+Selections[0],Weights[i]*Scales[h],LineColors[i],FillStyles[i],FillColors[i]);
	}       
    }
  
  for(int h=0; h<Histograms.size(); ++h)
    {
      for(int step=0; step<Selections.size(); ++step)
	{
	  for(int i=f-s; i<f; ++i)
	    {
	      plots.addPlot((TH1F*)Files[i]->Get(DataSelections[0]+"/"+Histograms[h]),Names[i],Histograms[h]+"_"+Selections[0],Weights[i],LineColors[i],FillStyles[i],FillColors[i]);
	    }       
	}
    }
  
  plots.printAll("ylog");
  //plots.printAll();
}
