#include <vector>
#include <iostream>
#include <bitset>
#include <fstream>
#include "TFile.h"
#include "TH1.h"
#include "TH2.h"
#include "TProfile2D.h"
#include "TF1.h"
#include "TCanvas.h"
#include "TStyle.h"
#include "TLegend.h"
#include "TPaveText.h"
#include <TDRStyle.h>
//#include <TDRStyle_Projection.h>

vector<TFile*> Files;
vector<TString> Samples;
vector<TString> Names;

vector<TString> Histograms;
vector<TString> XLabels;
vector<TString> YLabels;
vector<unsigned int> LowerBinsX;
vector<unsigned int> UpperBinsX;
vector<unsigned int> LowerBinsY;
vector<unsigned int> UpperBinsY;

vector<TString> Modules;
vector<TString> Selections;
vector<TString> Channels;
vector<TString> SelectionLabels;
vector<TString> ChannelLabels;


// addSample
void addSample(TFile* file, TString sample, TString name)
{
  Files.push_back(file);
  Samples.push_back(sample);
  Names.push_back(name);
}

// add histogram
void addHistogram(TString name, TString xLabel, TString yLabel, int lowerBinX, int upperBinX, int lowerBinY, int upperBinY )
{
  Histograms.push_back(name);
  XLabels.push_back(xLabel);
  YLabels.push_back(yLabel);
  LowerBinsX.push_back(lowerBinX);
  UpperBinsX.push_back(upperBinX);
  LowerBinsY.push_back(lowerBinY);
  UpperBinsY.push_back(upperBinY);
}

// add selection step
void addSelectionStep(TString module, TString step, TString selectionLabel)
{
  Modules.push_back(module);
  Selections.push_back(step);
  SelectionLabels.push_back(selectionLabel);
}

// add selection step
void addChannel(TString channel, TString channelLabel)
{
  Channels.push_back(channel);
  ChannelLabels.push_back(channelLabel);
}

// main function
int KappaScan()
{
  bool SeparateChannels = true;


  // files
   TFile* SemiLepElMu = new TFile("SemiLepElMuTTJets.root", "READ");
   
  //--------------------------------------------------------------------------------------------------
  // add addSample(TFile* file, TString sample, TString name)
  //--------------------------------------------------------------------------------------------------

  addSample(SemiLepElMu,"SemiLepElMuTTJets", "Semilep. t#bar{t}+Jets e/#mu");
  
  //--------------------------------------------------------------------------------------------------
  // addHistogram(TString name, TString xLabel, int firstValue, int lastValue, int drawLegend) 
  //--------------------------------------------------------------------------------------------------
  
  addHistogram("HT_YMET", "H_{T} [GeV]", "Y_{MET} [GeV^{#frac{1}{2}}]", 10, 41, 7, 51);
  
  //--------------------------------------------------------------------------------------------------
  // addSelectionStep(TString module, TString step, TString selectionLabel)
  //--------------------------------------------------------------------------------------------------
  
  //addSelectionStep("analyzeSUSY1", "_leptonSelection", "lepton selection");
  addSelectionStep("analyzeSUSY1", "_jetSelection",    "jet selection");
  
  //--------------------------------------------------------------------------------------------------
  // addChannel(TString channel, TString channelLabel)
  //--------------------------------------------------------------------------------------------------
  
  addChannel("m", "muon channel");
  //addChannel("e", "electron channel");
  
  //--------------------------------------------------------------------------------------------------
  // Set style 
  //--------------------------------------------------------------------------------------------------

  setTDRStyle();
  
  //--------------------------------------------------------------------------------------------------
  // Plot
  //--------------------------------------------------------------------------------------------------

  for(int fdx=0; fdx<(int)Files.size(); ++fdx)
    {
      for(int hdx=0; hdx<(int)Histograms.size(); ++hdx)
	{ 
	  std::cout << "\n" << Histograms[hdx] << std::endl;
	  std::cout << "-----------------------" << std::endl;
	  
	  for(int sdx=0; sdx<(int)Selections.size(); ++sdx)
	    {
	      if(SeparateChannels == true)
		{
		  for(int cdx=0; cdx<(int)Channels.size(); ++cdx)
		    {
		      std::cout << Modules[sdx]+Channels[cdx]+Selections[sdx] << "_" << Histograms[hdx] << std::endl;
		      
		      TCanvas *canvas = new TCanvas(Modules[sdx]+Channels[cdx]+Selections[sdx]+"_"+Histograms[hdx]+"_"+Samples[fdx],Modules[sdx]+Channels[cdx]+Selections[sdx]+"_"+Histograms[hdx]+"_"+Samples[fdx], 1);
		      
		      TPaveText *label = new TPaveText(0.14,0.94,0.99,1.,"NDC");
		      label->SetFillColor(0);
		      label->SetTextFont(42);
		      label->SetTextSize(0.043);
		      label->SetBorderSize(0);
		      label->SetTextAlign(12);
		      TText *text=label->AddText("Simulation, #sqrt{s} = 7 TeV, "+ChannelLabels[cdx]);
		      
		      TH2F* Hist = (TH2F*)Files[fdx]->Get(Modules[sdx]+Channels[cdx]+Selections[sdx]+"/"+Histograms[hdx]);
		      
		      std::cout << LowerBinsX[hdx] << std::endl;
		      std::cout << UpperBinsX[hdx] << std::endl;

		      TH2F* Scan=new TH2F("Scan", "Scan", 40, 0, 2000, 50, 0, 25);

		      for(int binX=13; binX<=25; ++binX)
			{

			  for(int binY=10; binY<=25; ++binY)
			    {
			      //std::cout << "x bin: " << binX << ", y bin: " << binY << std::endl;

			      double nA = Hist->Integral(LowerBinsX[hdx], binX,            LowerBinsY[hdx], binY);
			      double nB = Hist->Integral(binX,            UpperBinsX[hdx], LowerBinsY[hdx], binY);
			      double nC = Hist->Integral(LowerBinsX[hdx], binX,            binY,       UpperBinsY[hdx]);
			      double nD = Hist->Integral(binX,            UpperBinsX[hdx], binY,       UpperBinsY[hdx]);

			      double Kappa=(nD*nA)/(nB*nC);
			      
			      //std::cout << Kappa << std::endl;

			      Scan->SetBinContent(binX, binY, Kappa);
			    }
			}
		      
		      Scan->Draw();
		      canvas->SaveAs(Modules[sdx]+Channels[cdx]+Selections[sdx]+"_"+Histograms[hdx]+"_ProjectionX_"+Samples[fdx]+".pdf");                      
		    }
		}
	    }      
	}
    }
}
