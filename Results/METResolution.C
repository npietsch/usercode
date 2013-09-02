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
vector<double> FirstValues;
vector<double> LastValues;
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

vector<double> HTAverage;

// addSample
void addSample(TFile* file, TString sample, TString name)
{
  Files.push_back(file);
  Samples.push_back(sample);
  Names.push_back(name);
}

// add histogram
void addHistogram(TString name, TString xLabel, double firstValue, double lastValue, int drawLegend)
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
int METResolution()
{
  bool Log = true;
  bool SeparateChannels = false;
  bool CombineChannels = true;

  double LogMin=0.0001;
  double LogMax=0.4;

  double Min=0;
  double Max=0.18;

  TFile* SemiLepElMu = new TFile("SemiLepElMuTTJets_Correlation.root", "READ");
  
  //--------------------------------------------------------------------------------------------------
  // add addSample(TFile* file, TString sample, TString name)
  //--------------------------------------------------------------------------------------------------

  addSample(SemiLepElMu,"SemiLepElMuTTJets", "Semilep. t#bar{t}+Jets e/#mu");
  
  //--------------------------------------------------------------------------------------------------
  // addHistogram(TString name, TString xLabel, int firstValue, int lastValue, int drawLegend) 
  //--------------------------------------------------------------------------------------------------
  
  addHistogram("HT_HadMET", "#Delta#slash{E}_{T} [GeV]", -200., 200., 1);

  //--------------------------------------------------------------------------------------------------
  // addSelectionStep(TString module, TString step, TString selectionLabel)
  //--------------------------------------------------------------------------------------------------
  
  addSelectionStep("analyzeCorrelation1", "_nJets4ToInf", "nJets > 4");
  
  //--------------------------------------------------------------------------------------------------
  // addChannel(TString channel, TString channelLabel)
  //--------------------------------------------------------------------------------------------------
  
  addChannel("m", "muon channel");
  addChannel("e", "electron channel");
  
  //--------------------------------------------------------------------------------------------------
  // addBin(int firstBin, int lastBin, TString binLabel, int binColor, int marker) 
  //--------------------------------------------------------------------------------------------------

  addBin(19, 25,  "360 < H_{T} < 500",   kRed-4,  22);
  addBin(26, 32,  "500 < H_{T} < 640",   kBlue-7, 23);
  addBin(33, 39,  "640 < H_{T} < 780",   1,       20);
  addBin(39, 45,  "780 < H_{T} < 920",   kRed+2,  21);

//   addBin(21, 30,  "400 < H_{T} < 600",   kRed-4,  22);
//   addBin(31, 40,  "600 < H_{T} < 800",   kBlue-7, 23);
//   addBin(41, 50,  "800 < H_{T} < 1000",   1,       20);
  
//   addBin(7,  12,  "3 < #frac{p_{T}^{lep}}{#sqrt{H_{T}}} < 6",   2, 22);
//   addBin(13, 18,  "6 < #frac{p_{T}^{lep}}{#sqrt{H_{T}}} < 9",   4, 23);
//   addBin(18, 23,  "9 < #frac{p_{T}^{lep}}{#sqrt{H_{T}}} < 12",  1, 20);

  //addBin(7,  12,  "3 < p_{T}^{lep}/ #sqrt{H_{T}} < 6",   2, 22);
  //addBin(13, 18,  "6 < p_{T}^{lep}/ #sqrt{H_{T}} < 9",   4, 23);
  //addBin(18, 23,  "9 < p_{T}^{lep}/ #sqrt{H_{T}} < 12",  1, 20);

  
  //--------------------------------------------------------------------------------------------------
  // Set style 
  //--------------------------------------------------------------------------------------------------
  
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
		      
		      //TLegend *leg = new TLegend(.53,.62,.95,.93);
		      TLegend *leg = new TLegend(.58,.67,1,.98);
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
			  std::cout << FirstValues[hdx] << std::endl;

			  Projection->GetXaxis()->SetRangeUser(FirstValues[hdx],LastValues[hdx]);
			  Projection->Scale(1/Projection->Integral(0,-1));
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
			  else Projection->DrawCopy("same");;
			}
		      
		      // draw legend
		      if(DrawLegend[hdx] == 1) leg->Draw();
		  
		      // draw labels
		      label->Draw();
		      		  
		      // draw TLine
		      if(Log == true)
			{
			  TLine * line = new TLine(0, LogMin, 0, LogMax);
			  line->SetLineWidth(2);
			  line->SetLineStyle(2);
			  line->SetLineColor(1);
			  //line->Draw();
			}
		      else
			{
			  TLine * line = new TLine(0, Min, 0, Max);
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
		  
		  TCanvas *canvas = new TCanvas(Modules[sdx]+"l"+Selections[sdx]+"_"+Histograms[hdx]+"_"+Samples[fdx],Modules[sdx]+"1l"+Selections[sdx]+"_"+Histograms[hdx]+"_"+Samples[fdx], 1);
		  
		  //TLegend *leg = new TLegend(.53,.62,.95,.93);
		  TLegend *leg = new TLegend(.66,.72,1,1);
		  leg->SetTextFont(42);
		  leg->SetTextSize(0.042);
		  //leg->SetTextSize(0.043);
		  leg->SetFillColor(0);
		  leg->SetLineColor(1);
		  leg->SetShadowColor(0);
		  
		  TPaveText *label = new TPaveText(0.14,0.94,0.57,1.,"NDC");
		  label->SetFillColor(0);
		  label->SetTextFont(42);
		  label->SetTextSize(0.043);
		  label->SetBorderSize(0);
		  label->SetTextAlign(12);
		  TText *text=label->AddText("Simulation, #sqrt{s} = 7 TeV");
		  
		  TH2F* Hist  = (TH2F*)Files[fdx]->Get(Modules[sdx]+Channels[0]+Selections[sdx]+"/"+Histograms[hdx]);

		  for(int ddx=1; ddx<(int)Channels.size(); ++ddx)
		    {
		      TH2F* Hist2 = (TH2F*)Files[fdx]->Get(Modules[sdx]+Channels[ddx]+Selections[sdx]+"/"+Histograms[hdx]);
		      Hist->Add(Hist2);
		    }

		  TH1F* ProjectionHT = (TH1F*)Hist2->ProjectionX(Histograms[hdx], 0, -1,"");
		  for(int bin=0; bin<(int)FirstBins.size(); ++bin)
		    {
		      ProjectionHT->GetXaxis()->SetRangeUser(FirstBins[bin]*20-20,LastBins[bin]*20-20);
		      std::cout << ProjectionHT->GetMean() << std::endl;

		      HTAverage.push_back(ProjectionHT->GetMean());

		      ProjectionHT->Clear();
		    }

		  for(int bin=0; bin<(int)FirstBins.size(); ++bin)
		    {
		      std::cout << "bins " << FirstBins[bin] << " - " << LastBins[bin] << std::endl;

		      // create projection
		      TH1F* Projection = (TH1F*)Hist->ProjectionY(Histograms[hdx], FirstBins[bin], LastBins[bin],"");
		      
		      // edit ranges and scale
		      Projection->GetXaxis()->SetRangeUser(FirstValues[hdx],LastValues[hdx]);
		      
		      Projection->Scale(1/Projection->Integral(0,-1));
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

		      std::cout << Projection->GetMean() << std::endl;
		      std::cout << Projection->GetRMS() << std::endl;
		      std::cout << Projection->GetRMS()/sqrt(HTAverage[bin]) << std::endl;
		    }
		  
		  // draw legend
		  if(DrawLegend[hdx] == 1) leg->Draw();
		  
		  // draw labels
		  label->Draw();
		  
		  // draw TLine
		  if(Log == true)
		    {
		      TLine * line = new TLine(0, LogMin, 0, LogMax);
		      line->SetLineWidth(2);
		      line->SetLineStyle(2);
		      line->SetLineColor(1);
		      line->Draw();
		    }
		  else
		    {
		      TLine * line = new TLine(0, Min, 0, Max);
		      line->SetLineWidth(2);
		      line->SetLineStyle(2);
		      line->SetLineColor(1);
		      line->Draw();
		    }

		  // save canvas
		  if(Log == true)
		    {
		      canvas->SetLogy();
		      canvas->SaveAs(Modules[sdx]+"l"+Selections[sdx]+"_"+Histograms[hdx]+"_ProjectionY_"+Samples[fdx]+"_log.pdf");
		    }
		  else
		    {
		      canvas->SaveAs(Modules[sdx]+"l"+Selections[sdx]+"_"+Histograms[hdx]+"_ProjectionY_"+Samples[fdx]+".pdf");
		    }
		}
	    }  
	}
    }
}
