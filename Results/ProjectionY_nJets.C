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
vector<unsigned int> FirstValues;
vector<unsigned int> LastValues;
vector<unsigned int> DrawLegend;

vector<TString> Modules;
vector<TString> Selections;
vector<TString> SelectionLabels;
vector<unsigned int> BinColors;
vector<unsigned int> MarkerStyles;

vector<TString> Channels;
vector<TString> ChannelLabels;

vector<unsigned int> FirstBins;
vector<unsigned int> LastBins;
vector<TString> BinLabels;
vector<TString> BinNames;

// addSample
void addSample(TFile* file, TString sample, TString name)
{
  Files.push_back(file);
  Samples.push_back(sample);
  Names.push_back(name);
}

// add histogram
void addHistogram(TString name, TString xLabel, int firstValue, int lastValue, int drawLegend)
{
  Histograms.push_back(name);
  XLabels.push_back(xLabel);
  FirstValues.push_back(firstValue);
  LastValues.push_back(lastValue);
  DrawLegend.push_back(drawLegend);
}

// add selection step
void addSelectionStep(TString module, TString step, TString selectionLabel, int binColor, int marker)
{
  Modules.push_back(module);
  Selections.push_back(step);
  SelectionLabels.push_back(selectionLabel);
  BinColors.push_back(binColor);
  MarkerStyles.push_back(marker);
}

// add selection step
void addChannel(TString channel, TString channelLabel)
{
  Channels.push_back(channel);
  ChannelLabels.push_back(channelLabel);
}

// add bin
void addBin(int firstBin, int lastBin, TString binLabel, TString binName)
{
  FirstBins.push_back(firstBin);
  LastBins.push_back(lastBin);
  BinLabels.push_back(binLabel);
  BinNames.push_back(binName);
}

// main function
int ProjectionY_nJets()
{
  bool Log = false;
  bool SeparateChannels = false;
  bool CombineChannels = true;

  double LogMin=0.001;
  double LogMax=0.3;

  double Min=0;
  double Max=0.25;

  int NormBin=0;

  //TFile* WJetsHT = new TFile("WJetsHT.root",      "READ");
  //TFile* TTJets  = new TFile("TTJetsFall11.root", "READ");
  TFile* SemiLepElMu = new TFile("SemiLepElMuTTJets_Correlation.root", "READ");
  //TFile* SemiLepTau  = new TFile("SemiLepTauTTJets.root",  "READ");
  //TFile* DiLep       = new TFile("DiLepTTJets.root", "READ");
  //TFile* FullHad     = new TFile("FullHadTTJets.root", "READ");
  //TFile* SingleTop   = new TFile("SingleTop.root", "READ");

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
  
  //addHistogram("HT_MET",     "#slash{E}_{T} [GeV]",        0, 500, 1);
  //addHistogram("HT_fakeMET", "#slash{E}_{T}^{fake} [GeV]", 0, 200, 1);
  addHistogram("HT_NuPt",    "p_{T}^{#nu} [GeV]", 0, 500, 1);

  //--------------------------------------------------------------------------------------------------
  // addSelectionStep(TString module, TString step, TString selectionLabel, int binColor, int marker)
  //--------------------------------------------------------------------------------------------------
  
  //addSelectionStep("analyzeCorrelation1", "_nJets1To1",    "nJets = 1", 1,         25);
  addSelectionStep("analyzeCorrelation1", "_nJets2To2",    "nJets = 2", kRed-4,    20);
  addSelectionStep("analyzeCorrelation1", "_nJets3To3",    "nJets = 3", kGreen-3,  21);
  addSelectionStep("analyzeCorrelation1", "_nJets4To4",    "nJets = 4", kBlue-7,   22);
  addSelectionStep("analyzeCorrelation1", "_nJets5To5",    "nJets = 5", kRed+2,    23);
  addSelectionStep("analyzeCorrelation1", "_nJets6To6",    "nJets = 6", 1,         20);
  //addSelectionStep("analyzeCorrelation1", "_nJets7To7",    "nJets = 7", kRed-4,         21);
  //addSelectionStep("analyzeCorrelation1", "_jetSelection",    "jet selection");

//   addSelectionStep("analyzeCorrelation1", "_nJets2To2",    "nJets = 2", kRed-4,    20);
//   addSelectionStep("analyzeCorrelation1", "_nJets3To3",    "nJets = 3", kYellow-4, 21);
//   addSelectionStep("analyzeCorrelation1", "_nJets4To4",    "nJets = 4", kGreen-3,  22);
//   addSelectionStep("analyzeCorrelation1", "_nJets5To5",    "nJets = 5", kBlue-7,   23);
//   addSelectionStep("analyzeCorrelation1", "_nJets6To6",    "nJets = 6", kRed+2,    20);
//   addSelectionStep("analyzeCorrelation1", "_nJets7To7",    "nJets = 7", 1,         21);
//   //addSelectionStep("analyzeCorrelation1", "_jetSelection",    "jet selection");
 
 
  //--------------------------------------------------------------------------------------------------
  // addChannel(TString channel, TString channelLabel)
  //--------------------------------------------------------------------------------------------------
  
  addChannel("m", "muon channel");
  addChannel("e", "electron channel");
  
  //--------------------------------------------------------------------------------------------------
  // addBin(int firstBin, int lastBin, TString binLabel) 
  //--------------------------------------------------------------------------------------------------

  addBin(7,  10, "375 < H_{T} < 450", "375HT450");
  addBin(11, 14, "450 < H_{T} < 550", "450HT550");
  addBin(15, 18, "550 < H_{T} < 650", "550HT650");
  addBin(19, 22, "650 < H_{T} < 750", "650HT750");
  addBin(23, 26, "750 < H_{T} < 850", "750HT850");
  addBin(27, 31, "850 < H_{T} < 1000","850HT1000");


//   addBin(7,  11, "375 < H_{T} < 500");
//   addBin(12, 16, "500 < H_{T} < 650");
//   addBin(17, 21, "650 < H_{T} < 800");
//   addBin(22, 26, "800 < H_{T} < 950");

  //--------------------------------------------------------------------------------------------------
  // Set style 
  //--------------------------------------------------------------------------------------------------

  setTDRStyle();
  
  //--------------------------------------------------------------------------------------------------
  // Plotx
  //--------------------------------------------------------------------------------------------------

  for(int fdx=0; fdx<(int)Files.size(); ++fdx)
    {
      for(int hdx=0; hdx<(int)Histograms.size(); ++hdx)
	{ 
	  std::cout << "\n" << Histograms[hdx] << std::endl;
	  std::cout << "-----------------------" << std::endl;

	  if(SeparateChannels == true)
	    {
	      for(int cdx=0; cdx<(int)Channels.size(); ++cdx)
		{		      
		  for(int bin=0; bin<(int)FirstBins.size(); ++bin)
		    {

		      std::cout << "\nbins " << FirstBins[bin] << " - " << LastBins[bin] << std::endl;
		      
		      //TCanvas *canvas = new TCanvas(Histograms[hdx]+"_1"+Channels[cdx]+"_"+FirstBins[bin]+"_"+LastBins[bin]+"_"+Samples[fdx],Histograms[hdx]+"_1"+Channels[cdx]+"_"+FirstBins[bin]+"_"+LastBins[bin]+"_"+Samples[fdx], 1);

		      TCanvas *canvas = new TCanvas(Histograms[hdx]+"_1"+Channels[cdx]+"_"+BinNames[bin]+"_"+Samples[fdx],Histograms[hdx]+"_1"+Channels[cdx]+"_"+BinNames[bin]+"_"+Samples[fdx], 1);

		      TLegend *leg = new TLegend(.65,.62,.95,.93);
		      leg->SetTextFont(42);
		      //leg->SetTextSize(0.05);
		      leg->SetTextSize(0.045);
		      leg->SetFillColor(0);
		      leg->SetLineColor(1);
		      leg->SetShadowColor(0);
		      
		      TPaveText *label = new TPaveText(0.14,0.94,0.99,1.,"NDC");
		      label->SetFillColor(0);
		      label->SetTextFont(42);
		      label->SetTextSize(0.043);
		      label->SetBorderSize(0);
		      label->SetTextAlign(12);
		      TText *text=label->AddText("Simulation, #sqrt{s} = 7 TeV, "+ChannelLabels[cdx]);
		      
		      for(int sdx=0; sdx<(int)Selections.size(); ++sdx)
			{
			  std::cout << Modules[sdx]+Channels[cdx]+Selections[sdx] << "_" << Histograms[hdx] << std::endl;
			  
			  TH2F* Hist = (TH2F*)Files[fdx]->Get(Modules[sdx]+Channels[cdx]+Selections[sdx]+"/"+Histograms[hdx]);
			  
 			  // create projection
 			  TH1F* Projection = (TH1F*)Hist->ProjectionY(Histograms[hdx], FirstBins[bin], LastBins[bin],"");
			  
			  // edit ranges and scale
			  Projection->GetXaxis()->SetRangeUser(FirstValues[hdx],LastValues[hdx]);
			  Projection->Scale(1/Projection->Integral(NormBin,-1));
			  if(Log == true)
			    {
			      Projection->SetMinimum(LogMin);
			      Projection->SetMaximum(LogMax);
			    }
			  else
			    {
			      Projection->SetMinimum(Min);
			      Projection->SetMaximum(Max);
			    } 
			  
			  // edit titles
			  Projection->SetTitle("");
			  
			  Projection->GetXaxis()->SetTitle(XLabels[hdx]);
			  Projection->GetXaxis()->SetTitleOffset(1.2);
			  Projection->GetXaxis()->SetTitleSize(0.05);
			  Projection->GetXaxis()->SetTitleFont(42);
			  Projection->GetXaxis()->SetLabelFont(42);
			  
			  Projection->GetYaxis()->SetTitle("a.u.");
			  Projection->GetYaxis()->SetTitleOffset(1.4);
			  Projection->GetYaxis()->SetTitleSize(0.05);
			  Projection->GetYaxis()->SetTitleFont(42);
			  Projection->GetYaxis()->SetLabelFont(42);
			  
			  // edit lines and marker
			  Projection->SetLineColor(BinColors[sdx]);
			  Projection->SetLineWidth(2);
			  Projection->SetMarkerStyle(MarkerStyles[sdx]);
			  Projection->SetMarkerColor(BinColors[sdx]);
			  
			  // add entry to leg
			  leg->AddEntry(Projection->Clone(),SelectionLabels[sdx],"l P");
			  
			  if(sdx == 0) Projection->DrawCopy();
			  else Projection->DrawCopy("same");
			}
		      
		      // draw legend
		      if(DrawLegend[hdx] == 1) leg->Draw();
		      
		      // draw labels
		      label->Draw();
		      
		      // save canvas
		      if(Log == true)
			{
			  canvas->SetLogy();
			  canvas->SaveAs(Histograms[hdx]+"_1"+Channels[cdx]+"_"+BinNames[bin]+"_"+Samples[fdx]+"_log.pdf");
			}
		      else
			{	
			  canvas->SaveAs(Histograms[hdx]+"_1"+Channels[cdx]+"_"+BinNames[bin]+"_"+Samples[fdx]+".pdf");
			}
		    }
		}
	    }

	  if(CombineChannels == true)
	    {		      
	      for(int bin=0; bin<(int)FirstBins.size(); ++bin)
		{
		  
		  std::cout << "\nbins " << FirstBins[bin] << " - " << LastBins[bin] << std::endl;
		  
		  TCanvas *canvas = new TCanvas(Histograms[hdx]+"_1l_"+BinNames[bin]+"_"+Samples[fdx],Histograms[hdx]+"_1l_"+BinNames[bin]+"_"+Samples[fdx], 1);
		  
		  TLegend *leg = new TLegend(.70,.62,.95,.93);
		  leg->SetTextFont(42);
		  //leg->SetTextSize(0.05);
		  leg->SetTextSize(0.045);
		  leg->SetFillColor(0);
		  leg->SetLineColor(1);
		  leg->SetShadowColor(0);
		  
		  TPaveText *label = new TPaveText(0.14,0.94,0.99,1.,"NDC");
		  label->SetFillColor(0);
		  label->SetTextFont(42);
		  label->SetTextSize(0.043);
		  label->SetBorderSize(0);
		  label->SetTextAlign(12);
		  TText *text=label->AddText("Simulation, #sqrt{s} = 7 TeV, "+BinLabels[bin]);
		  
		  

		  for(int sdx=0; sdx<(int)Selections.size(); ++sdx)
		    {
		      std::cout << Modules[sdx]+"_1l_"+Selections[sdx] << "_" << Histograms[hdx] << std::endl;
		      
		      TH2F* Hist = (TH2F*)Files[fdx]->Get(Modules[sdx]+Channels[0]+Selections[sdx]+"/"+Histograms[hdx]);

		      for(int cdx=0; cdx<(int)Channels.size(); ++cdx )
			{
			  TH2F* Hist2 = (TH2F*)Files[fdx]->Get(Modules[sdx]+Channels[cdx]+Selections[sdx]+"/"+Histograms[hdx]);
			  
			  Hist->Add(Hist2);
			}
		      
		      // create projection
		      TH1F* Projection = (TH1F*)Hist->ProjectionY(Histograms[hdx], FirstBins[bin], LastBins[bin],"");
		      
		      // edit ranges and scale
		      Projection->GetXaxis()->SetRangeUser(FirstValues[hdx],LastValues[hdx]);
		      Projection->Scale(1/Projection->Integral(NormBin,-1));
		      if(Log == true)
			{
			  Projection->SetMinimum(LogMin);
			  Projection->SetMaximum(LogMax);
			}
		      else
			{
			  Projection->SetMinimum(Min);
			  Projection->SetMaximum(Max);
			} 
		      
		      // edit titles
		      Projection->SetTitle("");
		      
		      Projection->GetXaxis()->SetTitle(XLabels[hdx]);
		      Projection->GetXaxis()->SetTitleOffset(1.2);
		      Projection->GetXaxis()->SetTitleSize(0.05);
		      Projection->GetXaxis()->SetTitleFont(42);
		      Projection->GetXaxis()->SetLabelFont(42);
		      
		      Projection->GetYaxis()->SetTitle("a.u.");
		      Projection->GetYaxis()->SetTitleOffset(1.4);
		      Projection->GetYaxis()->SetTitleSize(0.05);
		      Projection->GetYaxis()->SetTitleFont(42);
		      Projection->GetYaxis()->SetLabelFont(42);
		      
		      // edit lines and marker
		      Projection->SetLineColor(BinColors[sdx]);
		      Projection->SetLineWidth(2);
		      Projection->SetMarkerStyle(MarkerStyles[sdx]);
		      Projection->SetMarkerColor(BinColors[sdx]);
		      
		      // add entry to leg
		      leg->AddEntry(Projection->Clone(),SelectionLabels[sdx],"l P");
		      
		      if(sdx == 0) Projection->DrawCopy();
		      else Projection->DrawCopy("same");
		    }
		  
		  // draw legend
		  if(DrawLegend[hdx] == 1) leg->Draw();
		  
		  // draw labels
		  label->Draw();
		  
		  // save canvas
		  if(Log == true)
		    {
		      canvas->SetLogy();
		      canvas->SaveAs(Histograms[hdx]+"_1l_"+BinNames[bin]+"_"+Samples[fdx]+"_log.pdf");
		    }
		  else
		    {	
		      canvas->SaveAs(Histograms[hdx]+"_1l_"+BinNames[bin]+"_"+Samples[fdx]+".pdf");
		    }
		}
	    }
	}
    }
}
