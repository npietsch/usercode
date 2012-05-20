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

vector<TString> Selections;
vector<TString> Histograms;

// add  sample
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

// add  histogram
void addHistogram(TString name);

void addHistogram(TString name)
{
  Histograms.push_back(name);
}

// main function
int Plot()
{

  //--------------------------------------------------------------
  // Samples
  //--------------------------------------------------------------

  TFile* SemiLepTTJets = new TFile("naf_SemiLepTTJets_cfg/Ruediger.root","READ");
  //TFile* FullHadTTJets = new TFile("naf_FullHadTTJets_cfg/Ruediger.root","READ");
  //TFile* WJets         = new TFile("naf_WJets_cfg/Ruediger.root","READ");
  //TFile* ZJets         = new TFile("naf_ZJets_cfg/Ruediger.root","READ");
  //TFile* QCD           = new TFile("naf_QCD_cfg/Ruediger.root","READ");

  //TFile* A1            = new TFile("naf_A1_cfg/Ruediger.root","READ");
  
  //-------------------------------------------------------------------------------------------------------------------
  // addSample(TFile* sample, TString name, double weight, int lc, int fc, int fs)
  //-------------------------------------------------------------------------------------------------------------------

  //addSample(FullHadTTJets, "Fullhad t#bar{t}", 1, kRed+2,   kRed+2,   1101);
  addSample(SemiLepTTJets, "Semilep t#bar{t}", 1, kRed,     kRed,     1101);
  //addSample(ZJets,         "Zvv + Jets",       1, kGreen+2, kGreen+2, 1101);
  //addSample(WJets,         "Wlv + Jets",       1, kYellow,  kYellow,  1101);
  //addSample(QCD,           "QCD",              1, kBlue-7,  kBlue-7,  1101);

  //addSample(A1,            "A1",               1, 1,        0,        0   );

  //-------------------------------------------------------------------------------------------------
  // push back selection step to vector<TString> Selections and DataSelection;
  //-------------------------------------------------------------------------------------------------

  std::cout << "Test1" << std::endl;

  Selections.push_back("analyzeBino1");

  //-------------------------------------------------------------------------------------------------
  // push back histogram to vector<int> Histograms and DataHistograms;
  //-------------------------------------------------------------------------------------------------

  std::cout << "Test2" << std::endl;

  addHistogram("MET");
  
  //--------
  // Plot
  //--------

  plotSet plots("Name");

  // Loop selections
  for(int sdx=0; sdx<(int)Selections.size(); ++sdx)
    {
      std::cout << Selections[sdx] << std::endl;
	  
      // Loop over histogram
      for(int h=0; h<(int)Histograms.size(); ++h)
	{ 
	  std::cout << Histograms[h] << std::endl;
	  
	  // Loop over samples
	  for(int i=0; i<(int)Files.size(); ++i)
	    {
	      plots.addPlot((TH1F*)Files[i]->Get(Selections[sdx]+"/"+Histograms[h]),Names[i],Histograms[h]+"_"+Selections[sdx],Weights[i],LineColors[i],FillStyles[i],FillColors[i]);
	    }      
	}
    }
  
  plots.printAll("ylog");
}
