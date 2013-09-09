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
vector<double> LowerValuesX;
vector<double> HigherValuesX;
vector<double> LowerValuesY;
vector<double> HigherValuesY;
vector<unsigned int> DrawLegend;

vector<TString> Modules;
vector<TString> Selections;
vector<TString> Channels;
vector<TString> SelectionLabels;
vector<TString> ChannelLabels;

vector<unsigned int> FirstBins;
vector<unsigned int> LastBins;
vector<TString> BinLabels;
vector<unsigned int> BinColors;
vector<unsigned int> MarkerStyles;

// addSample
void addSample(TFile* file, TString sample, TString name)
{
  Files.push_back(file);
  Samples.push_back(sample);
  Names.push_back(name);
}

// add histogram
void addHistogram(TString name, TString xLabel, TString yLabel, double lowerValueX, double higherValueX, double lowerValueY, double higherValueY, int drawLegend)
{
  Histograms.push_back(name);
  XLabels.push_back(xLabel);
  YLabels.push_back(yLabel);
  LowerValuesX.push_back(lowerValueX);
  HigherValuesX.push_back(higherValueX);
  LowerValuesY.push_back(lowerValueY);
  HigherValuesY.push_back(higherValueY);
  DrawLegend.push_back(drawLegend);
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
int Colz()
{
  bool Log = false;
  bool SeparateChannels = false;
  bool CombineChannels = true;

  double LogMin=0.001;
  double LogMax=0.8;

  double Min=0;
  double Max=0.5;

  int NormBin=9;

  TFile* WJetsHT = new TFile("WJetsHT.root",      "READ");
  //TFile* TTJets  = new TFile("TTJetsFall11.root", "READ");
  TFile* SemiLepElMu = new TFile("SemiLepElMuTTJets_Correlation.root", "READ");
  TFile* SemiLepTau  = new TFile("SemiLepTauTTJets.root",  "READ");
  TFile* DiLep       = new TFile("DiLepTTJets.root", "READ");
  TFile* FullHad     = new TFile("FullHadTTJets.root", "READ");
  TFile* SingleTop   = new TFile("SingleTop.root", "READ");

  //--------------------------------------------------------------------------------------------------
  // add addSample(TFile* file, TString sample, TString name)
  //--------------------------------------------------------------------------------------------------

  //addSample(WJetsHT, "WJetsHT", "W+Jets");
  addSample(SemiLepElMu,"SemiLepElMuTTJets", "Semilep. t#bar{t}+Jets e/#mu");
  //addSample(SemiLepTau, "SemiLepTauTTJets",  "Semilep. t#bar{t}+Jets #tau");
  //addSample(DiLep,      "DiLepTTJets",       "Dilep. t#bar{t}+Jets");
  //addSample(FullHad,    "FullHadTTJets",     "Fullhad. t#bar{t}+Jets");
  //addSample(SingleTop,    "SingleTop",        "Single Top");

  //--------------------------------------------------------------------------------------------------
  // addHistogram(TString name, TString xLabel, int firstValue, int lastValue, int drawLegend) 
  //--------------------------------------------------------------------------------------------------
  
  addHistogram("NuPt_fakeMET",  "P_{T}^{#nu}", "#slash{E}_{T}^{fake} [GeV]", 0, 500, 0, 500, 1);
  
  //--------------------------------------------------------------------------------------------------
  // addSelectionStep(TString module, TString step, TString selectionLabel)
  //--------------------------------------------------------------------------------------------------
  
  addSelectionStep("analyzeSUSY1", "_leptonSelection", "lepton selection");
  addSelectionStep("analyzeSUSY1", "_jetSelection",    "jet selection");

  //--------------------------------------------------------------------------------------------------
  // addChannel(TString channel, TString channelLabel)
  //--------------------------------------------------------------------------------------------------
  
  addChannel("m", "muon channel");
  addChannel("e", "electron channel");
  
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
	  
// 	  for(int sdx=0; sdx<(int)Selections.size(); ++sdx)
// 	    {
// 	      if(SeparateChannels == true)
// 		{
// 		  for(int cdx=0; cdx<(int)Channels.size(); ++cdx)
// 		    {
// 		      std::cout << Modules[sdx]+Channels[cdx]+Selections[sdx] << "_" << Histograms[hdx] << std::endl;
		      
// 		      TCanvas *canvas = new TCanvas(Modules[sdx]+Channels[cdx]+Selections[sdx]+"_"+Histograms[hdx]+"_"+Samples[fdx],Modules[sdx]+Channels[cdx]+Selections[sdx]+"_"+Histograms[hdx]+"_"+Samples[fdx], 1);
		      
// 		      TLegend *leg = new TLegend(.55,.62,.95,.93);
// 		      leg->SetTextFont(42);
// 		      leg->SetTextSize(0.05);
// 		      //leg->SetTextSize(0.04);
// 		      leg->SetFillColor(0);
// 		      leg->SetLineColor(1);
// 		      leg->SetShadowColor(0);
		      
// 		      TPaveText *label = new TPaveText(0.14,0.94,0.99,1.,"NDC");
// 		      label->SetFillColor(0);
// 		      label->SetTextFont(42);
// 		      label->SetTextSize(0.043);
// 		      label->SetBorderSize(0);
// 		      label->SetTextAlign(12);
// 		      TText *text=label->AddText("Simulation, #sqrt{s} = 7 TeV, "+ChannelLabels[cdx]);
		      
// 		      TH2F* Hist = (TH2F*)Files[fdx]->Get(Modules[sdx]+Channels[cdx]+Selections[sdx]+"/"+Histograms[hdx]);
		      
// 		      for(int bin=0; bin<(int)FirstBins.size(); ++bin)
// 			{
// 			  std::cout << "bins " << FirstBins[bin] << " - " << LastBins[bin] << std::endl;
			  
// 			  // create projection
// 			  TH1F* Projection = (TH1F*)Hist->ProjectionX(Histograms[hdx], FirstBins[bin], LastBins[bin],"");
			  
// 			  // edit ranges and scale
// 			  Projection->GetXaxis()->SetRangeUser(FirstValues[hdx],LastValues[hdx]);
// 			  Projection->Scale(1/Projection->Integral(NormBin,-1));
// 			  			  if(Log == true)
// 			    {
// 			      Projection->SetMinimum(LogMin);
// 			      Projection->SetMaximum(LogMax);
// 			    }
// 			  else
// 			    {
// 			      Projection->SetMinimum(Min);
// 			      Projection->SetMaximum(Max);
// 			    } 

// 			  // edit titles
// 			  Projection->SetTitle("");
			  
// 			  Projection->GetXaxis()->SetTitle(XLabels[hdx]);
// 			  Projection->GetXaxis()->SetTitleOffset(1.2);
// 			  Projection->GetXaxis()->SetTitleSize(0.05);
// 			  Projection->GetXaxis()->SetTitleFont(42);
// 			  Projection->GetXaxis()->SetLabelFont(42);
			  
// 			  Projection->GetYaxis()->SetTitle("a.u.");
// 			  Projection->GetYaxis()->SetTitleOffset(1.4);
// 			  Projection->GetYaxis()->SetTitleSize(0.05);
// 			  Projection->GetYaxis()->SetTitleFont(42);
// 			  Projection->GetYaxis()->SetLabelFont(42);
			  
// 			  // edit lines and marker
// 			  Projection->SetLineColor(BinColors[bin]);
// 			  Projection->SetLineWidth(2);
// 			  Projection->SetMarkerStyle(MarkerStyles[bin]);
// 			  Projection->SetMarkerColor(BinColors[bin]);
			  
// 			  // add entry to leg
// 			  leg->AddEntry(Projection->Clone(),BinLabels[bin],"l P");
			  
// 			  if(bin == 0) Projection->DrawCopy();
// 			  else Projection->DrawCopy("same");
// 			}
		      
// 		      // draw legend
// 		      if(DrawLegend[hdx] == 1) leg->Draw();
		  
// 		      // draw labels
// 		      label->Draw();
		      	
// 		      // draw TLine
// 		      if(Log == true)
// 			{
// 			  TLine * line = new TLine(3, LogMin, 3, LogMax);
// 			  line->SetLineWidth(2);
// 			  line->SetLineStyle(2);
// 			  line->SetLineColor(1);
// 			  line->Draw();
// 			}
// 		      else
// 			{
// 			  TLine * line = new TLine(3, Min, 3, Max);
// 			  line->SetLineWidth(2);
// 			  line->SetLineStyle(2);
// 			  line->SetLineColor(1);
// 			  line->Draw();
// 			}
		      
// 		      // save canvas
// 		      if(Log == true)
// 			{
// 			  canvas->SetLogy();
// 			  canvas->SaveAs(Modules[sdx]+Channels[cdx]+Selections[sdx]+"_"+Histograms[hdx]+"_ProjectionX_"+Samples[fdx]+"_log.pdf");
// 			}
// 		      else
// 			{
// 			  canvas->SaveAs(Modules[sdx]+Channels[cdx]+Selections[sdx]+"_"+Histograms[hdx]+"_ProjectionX_"+Samples[fdx]+".pdf");
// 			}
// 		    }
// 		}
	}
    }
}
