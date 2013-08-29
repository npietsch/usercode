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
void addHistogram(TString name, TString xLabel, int firstValue, int lastValue, int drawLegend)
{
  Histograms.push_back(name);
  XLabels.push_back(xLabel);
  FirstValues.push_back(firstValue);
  LastValues.push_back(lastValue);
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

// add bin
void addBin(int firstBin, int lastBin, TString binLabel, int binColor, int marker)
{
  FirstBins.push_back(firstBin);
  LastBins.push_back(lastBin);
  BinLabels.push_back(binLabel);
  BinColors.push_back(binColor);
  MarkerStyles.push_back(marker);
}

// main function
int ProjectionY()
{
  bool Log = false;
  bool SeparateChannels = true;
  bool CombineChannels = false;

  double LogMin=0.001;
  double LogMax=0.8;

  double Min=0;
  double Max=0.5;

  TFile* WJetsHT = new TFile("WJetsHT.root",      "READ");
  //TFile* TTJets  = new TFile("TTJetsFall11.root", "READ");
  TFile* SemiLepElMu = new TFile("SemiLepElMuTTJets.root", "READ");
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
  
  addHistogram("HT_YMET",     "Y_{MET} [GeV^{#frac{1}{2}}]", 0, 25, 1);
  //addHistogram("HT_LepPtSig", "H_{T} [GeV]", 360, 1000, 1);
  
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
  // addBin(int firstBin, int lastBin, TString binLabel, int binColor, int marker) 
  //--------------------------------------------------------------------------------------------------

  addBin(10, 12, "360 < H_{T} < 480",   kRed-4,  22);
  addBin(13, 15,  "480 < H_{T} < 600",  kBlue-7, 23);
  addBin(16, 18,  "600 < H_{T} < 720",  1,       20);
  addBin(19, 21,  "720 < H_{T} < 840",  kRed+2,  21);

//   addBin(7,  12,  "3 < #frac{p_{T}^{lep}}{#sqrt{H_{T}}} < 6",   2, 22);
//   addBin(13, 18,  "6 < #frac{p_{T}^{lep}}{#sqrt{H_{T}}} < 9",   4, 23);
//   addBin(18, 23,  "9 < #frac{p_{T}^{lep}}{#sqrt{H_{T}}} < 12",  1, 20);

  //addBin(7,  12,  "3 < p_{T}^{lep}/ #sqrt{H_{T}} < 6",   2, 22);
  //addBin(13, 18,  "6 < p_{T}^{lep}/ #sqrt{H_{T}} < 9",   4, 23);
  //addBin(18, 23,  "9 < p_{T}^{lep}/ #sqrt{H_{T}} < 12",  1, 20);

  
  // Set style 
  

  setTDRStyle();
  
  
  // Plot
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
		      
		      TLegend *leg = new TLegend(.53,.62,.95,.93);
		      leg->SetTextFont(42);
		      leg->SetTextSize(0.05);
		      //leg->SetTextSize(0.043);
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
		      
		      TH2F* Hist = (TH2F*)Files[fdx]->Get(Modules[sdx]+Channels[cdx]+Selections[sdx]+"/"+Histograms[hdx]);
		      
		      for(int bin=0; bin<(int)FirstBins.size(); ++bin)
			{
			  std::cout << "bins " << FirstBins[bin] << " - " << LastBins[bin] << std::endl;
			  
			  // create projection
			  TH1F* Projection = (TH1F*)Hist->ProjectionY(Histograms[hdx], FirstBins[bin], LastBins[bin],"");
			  
			  // edit ranges and scale
			  Projection->GetXaxis()->SetRangeUser(FirstValues[hdx],LastValues[hdx]);
			  Projection->Scale(1/Projection->Integral(7,-1));
			  if(Log = true)
			    {
			      Projection->SetMinimum(LogMin);
			      Projection->SetMaximum(LogMax);
			    }
			  else
			    {
			      Projection->SetMinimum(Min);
			      Projection->SetMaximum(Max);
			    } 
			  // edit titles and labels
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
			  Projection->SetLineColor(BinColors[bin]);
			  Projection->SetLineWidth(2);
			  Projection->SetMarkerStyle(MarkerStyles[bin]);
			  Projection->SetMarkerColor(BinColors[bin]);
			  
			  // add entry to leg
			  leg->AddEntry(Projection->Clone(),BinLabels[bin],"l P");
			  
			  if(bin == 0) Projection->DrawCopy();
			  else Projection->DrawCopy("same");
			}
		      
		      // draw legend
		      if(DrawLegend[hdx] == 1) leg->Draw();
		  
		      // draw labels
		      label->Draw();
		      		  
		      // draw TLine
		      if(Log = true)
			{
			  TLine * line = new TLine(3, LogMin, 3, LogMax);
			  line->SetLineWidth(2);
			  line->SetLineStyle(2);
			  line->SetLineColor(1);
			  //line->Draw();
			}
		      else
			{
			  TLine * line = new TLine(3, Min, 3, Max);
			  line->SetLineWidth(2);
			  line->SetLineStyle(2);
			  line->SetLineColor(1);
			  //line->Draw();
			}
		      
		      // save canvas
		      if(Log == true)
			{
			  canvas->SetLogy();
			  canvas->SaveAs(Modules[sdx]+Channels[cdx]+Selections[sdx]+"_"+Histograms[hdx]+"_ProjectionY_"+Samples[fdx]+"_log.pdf");
			}
		      else
			{
			  canvas->SaveAs(Modules[sdx]+Channels[cdx]+Selections[sdx]+"_"+Histograms[hdx]+"_ProjectionY_"+Samples[fdx]+".pdf");
			}
		    }
		}
		  
	      if(CombineChannels == true)
		{
		  std::cout << Modules[sdx]+"1l"+Selections[sdx] << "_" << Histograms[hdx] << std::endl;
		  
		  TCanvas *canvas = new TCanvas(Modules[sdx]+"1l"+Selections[sdx]+"_"+Histograms[hdx]+"_"+Samples[fdx],Modules[sdx]+"1l"+Selections[sdx]+"_"+Histograms[hdx]+"_"+Samples[fdx], 1);
		  
		  TLegend *leg = new TLegend(.53,.62,.95,.93);
		  leg->SetTextFont(42);
		  leg->SetTextSize(0.05);
		  //leg->SetTextSize(0.043);
		  leg->SetFillColor(0);
		  leg->SetLineColor(1);
		  leg->SetShadowColor(0);
		  
		  TPaveText *label = new TPaveText(0.14,0.94,0.99,1.,"NDC");
		  label->SetFillColor(0);
		  label->SetTextFont(42);
		  label->SetTextSize(0.043);
		  label->SetBorderSize(0);
		  label->SetTextAlign(12);
		  TText *text=label->AddText("Simulation, #sqrt{s} = 7 TeV");
		  
		  TH2F* Hist = (TH2F*)Files[fdx]->Get(Modules[sdx]+Channels[0]+Selections[sdx]+"/"+Histograms[hdx]);
		  
		  for(int ddx=1; ddx<(int)Channels.size(); ++ddx)
		    {
		      TH2F* Hist2 = (TH2F*)Files[fdx]->Get(Modules[sdx]+Channels[ddx]+Selections[sdx]+"/"+Histograms[hdx]);
		      Hist->Add(Hist2);
		    }

		  for(int bin=0; bin<(int)FirstBins.size(); ++bin)
		    {
		      std::cout << "bins " << FirstBins[bin] << " - " << LastBins[bin] << std::endl;
		      
		      // create projection
		      TH1F* Projection = (TH1F*)Hist->ProjectionY(Histograms[hdx], FirstBins[bin], LastBins[bin],"");
		      
		      // edit ranges and scale
		      Projection->GetXaxis()->SetRangeUser(FirstValues[hdx],LastValues[hdx]);
		      Projection->Scale(1/Projection->Integral(9,24));
		      if(Log = true)
			{
			  Projection->SetMinimum(LogMin);
			  Projection->SetMaximum(LogMax);
			}
		      else
			{
			  Projection->SetMinimum(Min);
			  Projection->SetMaximum(Max);
			}
		      
		      // edit titles and labels
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
		      Projection->SetLineColor(BinColors[bin]);
		      Projection->SetLineWidth(2);
		      Projection->SetMarkerStyle(MarkerStyles[bin]);
		      Projection->SetMarkerColor(BinColors[bin]);
		      
		      // add entry to leg
		      leg->AddEntry(Projection->Clone(),BinLabels[bin],"l P");
		      
		      if(bin == 0) Projection->DrawCopy();
		      else Projection->DrawCopy("same");
		    }
		  
		  // draw legend
		  if(DrawLegend[hdx] == 1) leg->Draw();
		  
		  // draw labels
		  label->Draw();
		  
		  // draw TLine
		  if(Log = true)
		    {
		      TLine * line = new TLine(3, LogMin, 3, LogMax);
		      line->SetLineWidth(2);
		      line->SetLineStyle(2);
		      line->SetLineColor(1);
		      //line->Draw();
		    }
		  else
		    {
		      TLine * line = new TLine(3, Min, 3, Max);
		      line->SetLineWidth(2);
		      line->SetLineStyle(2);
		      line->SetLineColor(1);
		      //line->Draw();
		    }

		  // save canvas
		  if(Log == true)
		    {
		      canvas->SetLogy();
		      canvas->SaveAs(Modules[sdx]+"1l"+Selections[sdx]+"_"+Histograms[hdx]+"_ProjectionY_"+Samples[fdx]+"_log.pdf");
		    }
		  else
		    {
		      canvas->SaveAs(Modules[sdx]+"1l"+Selections[sdx]+"_"+Histograms[hdx]+"_ProjectionY_"+Samples[fdx]+".pdf");
		    }
		}
	    }  
	}
    }
}
