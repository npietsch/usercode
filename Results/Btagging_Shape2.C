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

vector<TFile*> Files;
vector<TString> Names;
vector<TString> Algos;
vector<TString> Flavors;
vector<TString> Steps;
vector<TString> SelectionNames;


vector<unsigned int> LineColors;

vector<TH1F*> Histograms;

void addSample(TFile* sample, TString name);

void addSample(TFile* sample, TString name)
{
  Files.push_back(sample);
  Names.push_back(name);
}

void addAlgorithm(TString name);

void addAlgorithm(TString name)
{
  Algos.push_back(name);
}


void addSelectionStep(TString name);

void addSelectionStep(TString name, int lc, TString sn)
{
  Steps.push_back(name);
  LineColors.push_back(lc);
  SelectionNames.push_back(sn);
}

int Btagging_Shape2()
{
  // Define sample
  TFile* TTJets=new TFile("BtagEff_TTJets.root","READ");
  
  // addSample(TFile* sample, TString name)
  addSample(TTJets, "TTJets");
  
  // addAlgorithm(TString name)
  addAlgorithm("TCHEM");
  addAlgorithm("SSVHEM");

  // addSelectionStep(TString name)
  addSelectionStep("1", 1, "after muon cut");
  addSelectionStep("2", 4, "after jet cut");
  //addSelectionStep("3", 2, "after met cut");

  // Flavors
  Flavors.push_back("B");
  Flavors.push_back("C");
  Flavors.push_back("L");

  gStyle->SetCanvasColor(10);
  //gStyle->SetOptStat(0);
  gStyle->SetPalette(1);

  // loop over files
  for(int f=0; f<(int)Files.size(); ++f)
    {
      std::cout << Names[f] << std::endl;
      std::cout << "------------" << std::endl;
      
      // loop over algorithms
      for(int a=0; a<Algos.size(); ++a)
	{
	  std::cout << Algos[a] << std::endl;

	  // loop over flavor	  
	  for(int flv=0; flv<(int)Flavors.size(); ++flv)
	    {
	      // Define canvas., legend etc.
	      //sprintf(canvas,Algos[a]);x
	      TCanvas *canvas =new TCanvas(Names[f]+"_"+Algos[a]+"_"+Flavors[flv],Names[f]+"_"+Algos[a]+"_"+Flavors[flv],1);
	      TLegend *leg = new TLegend(.58,.2,.99,.6);
	      leg->SetTextFont(42);
	      leg->SetFillColor(0);
	      leg->SetLineColor(0);
	      
	      // loop over selection steps
	      for(int s=0; s < Steps.size(); ++s)
		{
		  
		  std::cout << "Selection step " << Steps[s] <<  std::endl;
		  TH1F* Pt_=(TH1F*)Files[f]->Get("bTagEff"+Algos[a]+Steps[s]+"/Num"+Flavors[flv]+"JetsPt");
		  TH1F* TaggedPt_=(TH1F*)Files[f]->Get("bTagEff"+Algos[a]+Steps[s]+"/Num"+Flavors[flv]+"JetsTaggedPt");
		  
		  TH1F* Eta_=(TH1F*)Files[f]->Get("bTagEff"+Algos[a]+Steps[s]+"/Num"+Flavors[flv]+"JetsEta");
		  TH1F* TaggedEta_=(TH1F*)Files[f]->Get("bTagEff"+Algos[a]+Steps[s]+"/Num"+Flavors[flv]+"JetsTaggedEta");
		  
		  TaggedPt_->Divide(Pt_);
		  TaggedPt_->SetLineColor(LineColors[s]);
		  TaggedPt_->SetTitle(Algos[a]);
		  TaggedPt_->GetXaxis()->SetTitle("p_{T} [GeV]");
		  TaggedPt_->GetXaxis()->CenterTitle();
		  TaggedPt_->GetYaxis()->SetTitle("b-tag efficiency");
		  TaggedPt_->GetYaxis()->CenterTitle();
		  TaggedPt_->SetDefaultSumw2(true);

		  if(s==0) TaggedPt_->Draw("");
		  else TaggedPt_->Draw("same");
		  
		  leg->AddEntry(TaggedPt_,SelectionNames[s],"l");
		  
		}
	      leg->Draw("box");
	      canvas->SaveAs(Names[f]+"_"+Algos[a]+"_"+Flavors[flv]+"jetsEff.pdf");
	    }
	}
      std::cout << "" << std::endl;
    }

  return 0;
  
}
