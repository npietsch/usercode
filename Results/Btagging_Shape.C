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
//#include <Plot.h>


vector<TFile*> Files;
vector<TString> Names;
vector<TString> Algos;
vector<int> Steps;

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

void addSelectionStep(TString name)
{
  Algos.push_back(name);
}

int Btagging_Shape()
{
  // Define sample
  TFile* TTJets=new TFile("BtagEff_TTJets.root","READ");
  
  // addSample(TFile* sample, TString name)
  addSample(TTJets, "TTJets");
  
  // addAlgorithm(TString name)
  addAlgorithm("TCHEM");

  // addSelectionStep(TString name)
  addSelectionStep("1");
  addSelectionStep("2");
  addSelectionStep("3");

  plotSet plots("Name");

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

	  // loop over selection steps
	  for(int s=0; s < Steps.size(); ++s)
	    {
	      std::cout << "Selection step " << Steps[s] << std::endl;
	      TH1F* BjetsPt_=(TH1F*)Files[f]->Get("bTagEff"+Algos[a]+Steps[s]+"/NumBJetsPt");
	      TH1F* BjetsTaggedPt_=(TH1F*)Files[f]->Get("bTagEff"+Algos[a]+Steps[s]+"/NumBJetsTaggedPt");
	      
	      TH1F* BjetsEta_=(TH1F*)Files[f]->Get("bTagEff"+Algos[a]+Steps[s]+"/NumBJetsEta");
	      TH1F* BjetsTaggedEta_=(TH1F*)Files[f]->Get("bTagEff"+Algos[a]+Steps[s]+"/NumBJetsTaggedEta");

	      //TH1F* BjetsEffPt_ = Divide(BjetsTaggedPt_, BjetsPt_ , 1, 1);
	      
	    }
	}
      std::cout << "" << std::endl;
    }


  
//   TH1F* hist1=(TH1F*)Files[0]->Get("analyzeSUSY1m_noCuts/nPU");
//   //TH1F* hist2=(TH1F*)Files[0]->Get("analyzeSUSY1m_noCuts/nPVweighted");
//   TH1F* hist2=(TH1F*)Files[1]->Get("pileup");

//   double hist1Int=hist1->Integral(1,hist1->GetNbinsX());
//   double hist2Int=hist2->Integral(1,hist2->GetNbinsX());
 
//   hist1->Scale(1/hist1Int);
//   hist2->Scale(1/hist2Int);

//   hist1->SetLineColor(2);
//   hist2->SetLineColor(4);;

//   TCanvas *c1 =new TCanvas( "nJets" , "nJets" ,1);
//   hist1->Draw("");
//   hist2->Draw("same");
//   gPad->SetLogy();

//   TLegend *leg = new TLegend(.58,.55,.99,.99);
//   leg->SetTextFont(42);
//   leg->SetFillColor(0);
//   leg->SetLineColor(0);

//   leg->AddEntry(hist1,"Ttbar weighted" ,"l");
//   leg->AddEntry(hist2,"May10 ReReco" ,"l");

//   leg->SetFillColor(10);
//   leg->Draw("box");

//   c1->SaveAs("PU.pdf");

    plots.printAll("ylog");
}
