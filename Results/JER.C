#include <vector>
#include <iostream>
#include <bitset>
#include <vector>
#include <fstream>
#include "TFile.h"
#include "TH1.h"
#include "TH2.h"
#include "TCanvas.h"
#include "TStyle.h"
#include "TLegend.h"

// declarations
vector<TString> MCModules;

vector<TFile*>  MCFiles;
vector<TString> MCNames;
vector<double>  MCXsecs;
vector<double>  MCEvents;

vector<TString> MCHistograms;
vector<TString> MCTitles;

// functions
void addMCModule(TString module);
void addMCModule(TString module)
{
  MCModules.push_back(module);
}

void addMCSample(TFile* sample, TString name, double xsec, double events);
void addMCSample(TFile* sample, TString name, double xsec, double events)
{
  MCFiles.push_back(sample);
  MCNames.push_back(name);
  MCXsecs.push_back(xsec);
  MCEvents.push_back(events);
}

void addMCHist(TString histogram, TString title);
void addMCHist(TString histogram, TString title)
{
  MCHistograms.push_back(histogram);
  MCTitles.push_back(title);
}

// main function
int JER()
{
  //-----------------------------------------------------------------------------------------
  // Define samples and luminosity
  //-----------------------------------------------------------------------------------------

  TFile* TTJets    = new TFile("Temp.root","READ");
  //TFile* SingleTop = new TFile("SingleTop.root","READ");
  //TFile* WJets     = new TFile("WJets.root","READ");
  //TFile* ZJets     = new TFile("ZJets.root","READ");
  //TFile* QCD       = new TFile("QCD.root","READ");

  // Luminosity for MuHad in fb^-1
  Double_t MuLumi=4621;

  // Luminosity for ElHad in fb^-1
  Double_t ElLumi=4613;

  //-----------------------------------------------------------------------------------------
  // addMCSample (TFile* sample, TString name, double weight, double events, double xsec)
  //-----------------------------------------------------------------------------------------

  //addMCSample(QCD,       "QCD",             0.001,   1        );
  //addMCSample(ZJets,     "ZJets",           3048,    36058014 );
  //addMCSample(WJets,     "W+Jets",          31314,   81060362 );
  //addMCSample(SingleTop, "Single Top",      0.001,   1        ); 
  addMCSample(TTJets,    "T#bar{T}+Jets",   157.5,   3631452  );
  
  //-----------------------------------------------------------------------------------------
  // addMCModule(TString name)
  //-----------------------------------------------------------------------------------------

  addMCModule("analyzeSUSY1b1m_4");

  //-----------------------------------------------------------------------------------------
  // addMCHist(TString histogram)
  //-----------------------------------------------------------------------------------------

  //addMCHist("HT_SigMET", "HT vs. Ymet");
  addMCHist("HT_SigMET_PT20_MET60", "HT vs. Ymet");

  //-----------------------------------------------------------------------------------------
  // Temp
  //-----------------------------------------------------------------------------------------

  vector<TString> JER;

  JER.push_back("_JER30Down");
  JER.push_back("_JER20Down");
  JER.push_back("_JER10Down");
  JER.push_back("");
  JER.push_back("_JER10Up");
  JER.push_back("_JER20Up");
  JER.push_back("_JER30Up");

  //-----------------------------------------------------------------------------------------
  // Plot histograms
  //-----------------------------------------------------------------------------------------

  gStyle->SetCanvasColor(10);
  gStyle->SetOptStat(0);
  gStyle->SetPalette(1);
  gStyle->SetTitleFillColor(0);
  
  for(int mdx=0; mdx<(int)MCModules.size(); ++mdx)
    {
      for(int hdx=0; hdx<(int)MCHistograms.size(); ++hdx)
	{
	  TCanvas *canvas=new TCanvas(MCModules[mdx]+MCHistograms[hdx], MCModules[mdx]+MCHistograms[hdx], 1);
	  
	  for(int jdx=0; jdx<(int)JER.size(); ++jdx)
	    {
	      TH2F* MCHist=(TH2F*)MCFiles[0]->Get(MCModules[mdx]+JER[jdx]+"/"+MCHistograms[hdx]);
	      
	      MCHist->Scale(MCXsecs[0]*MuLumi/MCEvents[0]);
	      
	      for(int fdx=1; fdx<(int)MCFiles.size(); ++fdx)
		{
		  TH2F* Temp=(TH2F*)MCFiles[fdx]->Get(MCModules[mdx]+JER[jdx]+"/"+MCHistograms[hdx]);
		  Temp->Scale(MCXsecs[fdx]*MuLumi/MCEvents[fdx]);
		  MCHist->Add(Temp);
		}
	      
	      double IntA=MCHist->Integral(16, 26,                    14, 22                   );
	      double IntB=MCHist->Integral(27, MCHist->GetNbinsX()+1, 14, 22                   );
	      double IntC=MCHist->Integral(16, 26,                    15, MCHist->GetNbinsY()+1);
	      double IntD=MCHist->Integral(27, MCHist->GetNbinsX()+1, 15, MCHist->GetNbinsY()+1);
	      
	      double kappa=(IntA*IntD)/(IntB*IntC);

	      std::cout << kappa << std::endl;
	      
	      

	    }
	  
// 	  canvas->SaveAs(MCModules[mdx]+"_"+MCHistograms[hdx]+".pdf");
 	 
 	}
    }
}
