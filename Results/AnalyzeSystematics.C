#include <vector>
#include <iostream>
#include <bitset>
#include <vector>
#include <fstream>
#include "TFile.h"
#include "TH1.h"
#include "TCanvas.h"
#include "TStyle.h"
#include "TLegend.h"

// MC samples
vector<TFile*> MCFiles;
vector<TString> MCNames;
vector<double> MCXsec;
vector<double> MCEvents;

// MC histograms
vector<TString> Uncertainties;
vector<TString> MCHistograms;
vector<TString> Titles;

// Selections
vector<TString> Channels;
vector<TString> Names;
vector<TString> MCSelections;

// add MC sample
void addMCSample(TFile* sample, TString name, double xsec, double events);

void addMCSample(TFile* sample, TString name, double xsec, double events)
{
  MCFiles.push_back(sample);
  MCNames.push_back(name);
  MCXsec.push_back(xsec);
  MCEvents.push_back(events);
}

void addMCHistogram(TString uncertainty, TString histogram, TString unit);

void addMCHistogram(TString uncertainty, TString histogram, TString title)
{
  Uncertainties.push_back(uncertainty);
  MCHistograms.push_back(histogram);
  Titles.push_back(title);

}

void addSelection(TString channel, TString name);

void addSelection(TString channel, TString name)
{
  Channels.push_back(channel);
  Names.push_back(name);
}


// main function
int AnalyzeSystematics()
{
  //-----------------------------------------------------------------------------------------
  // Define samples and luminosity
  //-----------------------------------------------------------------------------------------

  TFile* TTJets    = new TFile("TTJets.root","READ");
  TFile* SingleTop = new TFile("SingleTop.root","READ");
  TFile* WJets     = new TFile("WJets.root","READ");
  TFile* ZJets     = new TFile("ZJets.root","READ");
  TFile* QCD       = new TFile("QCD.root","READ");
  
  // Luminosity for MuHad in fb^-1
  Double_t MuLumi=4621;

  // Luminosity for ElHad in fb^-1
  Double_t ElLumi=4613;

  //-----------------------------------------------------------------------------------------
  // addMCSample (TFile* sample, TString name, double weight, double events, double xsec)
  //-----------------------------------------------------------------------------------------

  addMCSample(QCD,       "QCD",           0.001, 1        );
  addMCSample(ZJets,     "ZJets",         3048,  36058014 );
  addMCSample(WJets,     "W+Jets",        31314, 81060362 );
  addMCSample(SingleTop, "Single Top",    0.001, 1        ); 
  addMCSample(TTJets,    "T#bar{T}+Jets", 157.5, 3631452  );
  
  //-----------------------------------------------------------------------------------------
  // void addSelection(TString channel, TString name)
  //-----------------------------------------------------------------------------------------

  addSelection("Mu", "Muon");
  //addSelection("El", "Electron");

  //-----------------------------------------------------------------------------------------
  // push back selections to vector<TSring> MCSelections;
  //-----------------------------------------------------------------------------------------

  //MCSelections.push_back("0");
  MCSelections.push_back("1");
  MCSelections.push_back("2");
  MCSelections.push_back("3");

  //-----------------------------------------------------------------------------------------
  // addMCHistogram(TString uncertainty, TString histogram)
  //-----------------------------------------------------------------------------------------

  //addMCHistogram("JEC", "HT", "[GeV]");  
  //addMCHistogram("JER", "HT", "[GeV]");
  addMCHistogram("BtagSF", "btagWeights_PUWgt", "b-tag weights");
  addMCHistogram("BtagSF", "TCHE", "TCHE dicriminator");

  //-----------------------------------------------------------------------------------------
  // Plot histograms
  //-----------------------------------------------------------------------------------------

  gStyle->SetCanvasColor(10);
  gStyle->SetOptStat(0);
  gStyle->SetPalette(1);
  gStyle->SetTitleFillColor(0);

  // loop over lepton channel
  for(int chx=0; chx<(int)Channels.size(); ++chx)
    {
      std::cout << "\nChannels[chx] channel" << std::endl;
      std::cout << "===========================================" << std::endl << std::endl;
      	  
      // loop over selection paths
      for(int sel=0; sel<(int)MCSelections.size(); ++sel)
	{
	  std::cout << "\nSelection path: " << MCSelections[sel]+"b" << std::endl;
	  std::cout << "-------------------------------------------" << std::endl;
	  
	  // loop over uncertainties
	  for(int unc=0; unc<(int)Uncertainties.size(); ++unc)
	    {
	      std::cout << "analyzeSystematics"+Channels[chx]+MCSelections[sel]+"b"+"JER/"+MCHistograms[unc] << std::endl;
	      
	      // Draw canvas
	      TCanvas *canvas=new TCanvas("analyzeSystematics"+Channels[chx]+MCSelections[sel]+"b"+Uncertainties[unc],"analyzeSystematics"+Channels[chx]+MCSelections[sel]+"b"+Uncertainties[unc],1);
	      
	      // Up
	      TH1F* HistUp=(TH1F*)MCFiles[0]->Get("analyzeSystematics"+Channels[chx]+MCSelections[sel]+"b"+Uncertainties[unc]+"Up/"+MCHistograms[unc]);
	      HistUp->Scale(MCXsec[0]*MuLumi/MCEvents[0]);
	      for(int file=1; file<(int)MCFiles.size(); ++file)
		{
		  TH1F* TempUp=(TH1F*)MCFiles[file]->Get("analyzeSystematics"+Channels[chx]+MCSelections[sel]+"b"+Uncertainties[unc]+"Up/"+MCHistograms[unc]);
		  TempUp->Scale(MCXsec[file]*MuLumi/MCEvents[file]);
		  HistUp->Add(TempUp);
		}
	      double Max=HistUp->GetMaximum();

	      // JER
	      TH1F* Hist=(TH1F*)MCFiles[0]->Get("analyzeSystematics"+Channels[chx]+MCSelections[sel]+"b"+"JER/"+MCHistograms[unc]);
	      Hist->Scale(MCXsec[0]*MuLumi/MCEvents[0]);
	      for(int file=1; file<(int)MCFiles.size(); ++file)
		{
		  TH1F* Temp=(TH1F*)MCFiles[file]->Get("analyzeSystematics"+Channels[chx]+MCSelections[sel]+"b"+"JER/"+MCHistograms[unc]);
		  Temp->Scale(MCXsec[file]*MuLumi/MCEvents[file]);
		  Hist->Add(Temp);
		}
	      if(Hist->GetMaximum()>Max) Max=Hist->GetMaximum(); 

	      // Down
	      TH1F* HistDown=(TH1F*)MCFiles[0]->Get("analyzeSystematics"+Channels[chx]+MCSelections[sel]+"b"+Uncertainties[unc]+"Down/"+MCHistograms[unc]);
	      HistDown->Scale(MCXsec[0]*MuLumi/MCEvents[0]);
	      for(int file=1; file<(int)MCFiles.size(); ++file)
		{
		  TH1F* TempDown=(TH1F*)MCFiles[file]->Get("analyzeSystematics"+Channels[chx]+MCSelections[sel]+"b"+Uncertainties[unc]+"Down/"+MCHistograms[unc]);
		  TempDown->Scale(MCXsec[file]*MuLumi/MCEvents[file]);
		  HistDown->Add(TempDown);
		}
	      if(HistDown->GetMaximum()>Max) Max=HistDown->GetMaximum(); 

	      // Histogram style
	      HistUp->SetMaximum(1.1*Max);
	      if(MCSelections[sel]=="1")
		{
		  HistUp->SetTitle(Names[chx]+" selection with "+MCSelections[sel]+" b-tag");
		}
	      else HistUp->SetTitle(Names[chx]+" selection with "+MCSelections[sel]+" b-tags");
	      HistUp->GetXaxis()->SetTitle(Titles[unc]);
	      HistUp->GetXaxis()->CenterTitle();
	      HistUp->GetYaxis()->SetTitle("events");
	      HistUp->GetYaxis()->CenterTitle();
	      
	      HistUp->SetLineColor(2);
	      HistUp->SetMarkerColor(2);
	      HistUp->SetMarkerStyle(22);
	      HistUp->SetMarkerSize(0.9);
	      HistUp->Draw();

	      Hist->SetLineColor(1);
	      Hist->SetMarkerColor(1);
	      Hist->SetMarkerStyle(21);
	      Hist->SetMarkerSize(0.8);
	      Hist->Draw("same");

	      HistDown->SetLineColor(4);
	      HistDown->SetMarkerColor(4);
	      HistDown->SetMarkerStyle(23);
	      HistDown->SetMarkerSize(0.9);
	      HistDown->Draw("same");
	      
	      // Legend
	      TLegend *leg = new TLegend(.65,.65,.98,.98);
	      leg->SetTextFont(42);
	      leg->SetFillColor(0);
	      leg->SetLineColor(0);
	      
	      leg->AddEntry(HistUp,   Uncertainties[unc]+" up",       "l P");
	      leg->AddEntry(Hist,     Uncertainties[unc]+" no shift", "l P");
	      leg->AddEntry(HistDown, Uncertainties[unc]+" down",     "l P");
	      
	      leg->Draw("same");
	      
	      canvas->SaveAs("analyzeSystematics"+Channels[chx]+MCSelections[sel]+"b"+"_"+Uncertainties[unc]+"_"+MCHistograms[unc]+".pdf");
	    } 
	}
    }
}
