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
vector<TString> HistogramLabels;

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
void addHistogram(TString name, TString xLabel, TString yLabel, double lowerValueX, double higherValueX, double lowerValueY, double higherValueY, TString histogramLabel)
{
  Histograms.push_back(name);
  XLabels.push_back(xLabel);
  YLabels.push_back(yLabel);
  LowerValuesX.push_back(lowerValueX);
  HigherValuesX.push_back(higherValueX);
  LowerValuesY.push_back(lowerValueY);
  HigherValuesY.push_back(higherValueY);
  HistogramLabels.push_back(histogramLabel);
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
int Colz600600()
{
  bool Log = true;
  bool SeparateChannels = false;
  bool CombineChannels = true;

  double LogMin=0.001;
  double LogMax=0.6;

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
  
  addHistogram("HT_nJets",  "H_{T} [GeV]", "nJets", 0, 1000, 0.5, 15.5, "375 < H_{T} < 1000");

  
  //--------------------------------------------------------------------------------------------------
  // addSelectionStep(TString module, TString step, TString selectionLabel)
  //--------------------------------------------------------------------------------------------------
  
  addSelectionStep("analyzeCorrelation1", "_noCuts",          "no cuts");
  addSelectionStep("analyzeCorrelation1", "_preselection",    "preselection");
  addSelectionStep("analyzeCorrelation1", "_leptonSelection", "lepton selection");
  addSelectionStep("analyzeCorrelation1", "_jetSelection",    "jet selection");

  //--------------------------------------------------------------------------------------------------
  // addChannel(TString channel, TString channelLabel)
  //--------------------------------------------------------------------------------------------------
  
  addChannel("m", "muon channel");
  addChannel("e", "electron channel");
  
  //--------------------------------------------------------------------------------------------------
  // Set style 
  //--------------------------------------------------------------------------------------------------

  setTDRStyle();
  tdrStyle->SetPadLeftMargin(0.12);
  tdrStyle->SetPadRightMargin(0.19);
  tdrStyle->SetPadTopMargin(0.1);
  tdrStyle->SetPadBottomMargin(0.14);
  tdrStyle->SetPalette(1);
  tdrStyle->SetCanvasDefH(600);
  tdrStyle->SetCanvasDefW(600);


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

		      TProfile2D* Profile = (TProfile2D*)Hist->ProfileX();

// 		      // Set Ranges
// 		      if(Log == true)
// 			{
// 			  Hist->SetMinimum(LogMin);
// 			  Hist->SetMaximum(LogMax);
// 			}
// 		      else
// 			{
// 			  Hist->SetMinimum(Min);
// 			  Hist->SetMaximum(Max);
// 			} 
		      Hist->GetXaxis()->SetRangeUser(LowerValuesX[hdx],HigherValuesX[hdx]);
		      Hist->GetYaxis()->SetRangeUser(LowerValuesY[hdx],HigherValuesY[hdx]);
		      
		      // edit titles
		      Hist->SetTitle("");
		      
		      Hist->GetXaxis()->SetTitle(XLabels[hdx]);
		      Hist->GetXaxis()->SetTitleOffset(1.1);
		      Hist->GetXaxis()->SetTitleSize(0.05);
		      Hist->GetXaxis()->SetTitleFont(42);
		      Hist->GetXaxis()->SetLabelFont(42);
		      
		      Hist->GetYaxis()->SetTitle(YLabels[hdx]);
		      Hist->GetYaxis()->SetTitleOffset(0.9);
		      Hist->GetYaxis()->SetTitleSize(0.05);
		      Hist->GetYaxis()->SetTitleFont(42);
		      Hist->GetYaxis()->SetLabelFont(42);
		      
		      Hist->GetZaxis()->SetTitle("Events");
		      Hist->GetZaxis()->SetTitleOffset(0.6);
		      Hist->GetZaxis()->SetTitleSize(0.05);
		      Hist->GetZaxis()->SetTitleFont(42);
		      Hist->GetZaxis()->SetLabelFont(42);

		      Hist->Draw("colz");
		      
		      Profile->SetLineColor(1);
		      Profile->SetLineWidth(2);
		      Profile->Draw("same");
		      
 		      // draw labels
 		      label->Draw();
		  		      
		      // save canvas
		      if(Log == true)
			{
			  canvas->SetLogz();
			  canvas->SaveAs(Modules[sdx]+Channels[cdx]+Selections[sdx]+"_"+Histograms[hdx]+"_"+Samples[fdx]+"_log.pdf");
			}
		      else
			{
			  canvas->SaveAs(Modules[sdx]+Channels[cdx]+Selections[sdx]+"_"+Histograms[hdx]+"_"+Samples[fdx]+".pdf");
			}
		    }	
		}

	      if(CombineChannels == true)
		{
		  std::cout << Modules[sdx]+"l"+Selections[sdx] << "_" << Histograms[hdx] << std::endl;
		      
		      TCanvas *canvas = new TCanvas(Modules[sdx]+"l"+Selections[sdx]+"_"+Histograms[hdx]+"_"+Samples[fdx],Modules[sdx]+"l"+Selections[sdx]+"_"+Histograms[hdx]+"_"+Samples[fdx], 1);
		      
		      TPaveText *label = new TPaveText(0.07,0.92,0.96,1.,"NDC");
		      label->SetFillColor(0);
		      label->SetTextFont(42);
		      label->SetTextSize(0.06);
		      label->SetBorderSize(0);
		      label->SetTextAlign(12);
		      TText *text=label->AddText("Simulation, #sqrt{s} = 7 TeV");
		      
 		      TH2F* Hist = (TH2F*)Files[fdx]->Get(Modules[sdx]+Channels[0]+Selections[sdx]+"/"+Histograms[hdx]);

		      for(int cfx=0; cdx<(int)Channels.size(); ++cdx)
			{
			  
			  TH2F* Hist2 = (TH2F*)Files[fdx]->Get(Modules[sdx]+Channels[cfx]+Selections[sdx]+"/"+Histograms[hdx]);
			  Hist->Add(Hist2);
			}
		      TProfile2D* Profile = (TProfile2D*)Hist->ProfileX();
			  
			  
// 		      // Set Ranges
// 		      if(Log == true)
// 			{
// 			  Hist->SetMinimum(LogMin);
// 			  Hist->SetMaximum(LogMax);
// 			}
// 		      else
// 			{
// 			  Hist->SetMinimum(Min);
// 			  Hist->SetMaximum(Max);
// 			} 
		      Hist->GetXaxis()->SetRangeUser(LowerValuesX[hdx],HigherValuesX[hdx]);
		      Hist->GetYaxis()->SetRangeUser(LowerValuesY[hdx],HigherValuesY[hdx]);
		      
		      // edit titles
		      Hist->SetTitle("");
		      
		      Hist->GetXaxis()->SetTitle(XLabels[hdx]);
		      Hist->GetXaxis()->SetTitleOffset(1.1);
		      Hist->GetXaxis()->SetTitleSize(0.06);
		      Hist->GetXaxis()->SetTitleFont(42);
		      Hist->GetXaxis()->SetLabelFont(42);
		      Hist->GetXaxis()->SetLabelSize(0.05);
		      
		      Hist->GetYaxis()->SetTitle(YLabels[hdx]);
		      Hist->GetYaxis()->SetTitleOffset(1.);
		      Hist->GetYaxis()->SetTitleSize(0.06);
		      Hist->GetYaxis()->SetTitleFont(42);
		      Hist->GetYaxis()->SetLabelFont(42);
		      Hist->GetYaxis()->SetLabelSize(0.05);

		      Hist->GetZaxis()->SetTitle("Events");
		      Hist->GetZaxis()->SetTitleOffset(1.1);
		      Hist->GetZaxis()->SetTitleSize(0.06);
		      Hist->GetZaxis()->SetTitleFont(42);
		      Hist->GetZaxis()->SetLabelFont(42);
		      Hist->GetZaxis()->SetLabelSize(0.05);

		      Hist->Draw("colz");
		      
		      Profile->SetLineColor(1);
		      Profile->SetLineWidth(3);
		      Profile->Draw("same");
		      
 		      // draw labels
 		      label->Draw();
		  		      
		      // save canvas
		      if(Log == true)
			{
			  canvas->SetLogz();
			  canvas->SaveAs(Modules[sdx]+"l"+Selections[sdx]+"_"+Histograms[hdx]+"_"+Samples[fdx]+"_log.pdf");
			}
		      else
			{
			  canvas->SaveAs(Modules[sdx]+"l"+Selections[sdx]+"_"+Histograms[hdx]+"_"+Samples[fdx]+".pdf");
			}
		}	
	    }
	}
    }
}

