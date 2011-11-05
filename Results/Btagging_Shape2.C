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
  TFile* WJets =new TFile("BtagEff_WJets.root", "READ");
  TFile* SingleTop =new TFile("BtagEff_SingleTop.root", "READ");
  TFile* DYJets =new TFile("BtagEff_DY.root", "READ");
  TFile* QCD =new TFile("BtagEff_QCD.root", "READ");

  // addSample(TFile* sample, TString name)
  addSample(TTJets, "TTJets");
  addSample(WJets, "WJets");
  addSample(SingleTop, "SingleTop");
  addSample(DYJets, "DYJets");
  addSample(QCD, "QCD");

  // addAlgorithm(TString name)
  //addAlgorithm("TCHEM");
  addAlgorithm("SSVHEM");

  // addSelectionStep(TString name)
  addSelectionStep("1", 1, "Preselection");
  addSelectionStep("2", 2, "Electron selection");
  addSelectionStep("3", 4, "Jet selection");
  addSelectionStep("4", 8, "MET < 300 GeV");

  // Flavors
  Flavors.push_back("B");
  Flavors.push_back("C");
  Flavors.push_back("L");

  gStyle->SetCanvasColor(10);
  gStyle->SetOptStat(0);
  gStyle->SetPalette(1);
  gStyle->SetTitleFillColor(0);
		  
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
	      TCanvas *canvas =new TCanvas(Names[f]+"_"+Algos[a]+"_"+Flavors[flv]+"_Pt",Names[f]+"_"+Algos[a]+"_"+Flavors[flv]+"_Pt",1);
	      TLegend *leg = new TLegend(.5,.15,.88,.42);
	      leg->SetTextFont(42);
	      leg->SetFillColor(0);
	      leg->SetLineColor(0);
	      
	      TLegend *leg2 = new TLegend(.5,.15,.88,.42);
	      leg2->SetTextFont(42);
	      leg2->SetFillColor(0);
	      leg2->SetLineColor(0);

	      // loop over selection steps
	      for(int s=0; s < Steps.size(); ++s)
		{
		  std::cout << "Selection step " << Steps[s] <<  std::endl;

		  std::cout << "bTagEffRA4bEl"+Algos[a]+Steps[s]+"/Num"+Flavors[flv]+"JetsPt" << std::endl;

		  TH1F* Pt_=(TH1F*)Files[f]->Get("bTagEffRA4bEl"+Algos[a]+Steps[s]+"/Num"+Flavors[flv]+"JetsPt");
		  TH1F* TaggedPt_=(TH1F*)Files[f]->Get("bTagEffRA4bEl"+Algos[a]+Steps[s]+"/Num"+Flavors[flv]+"JetsTaggedPt");
		  
		  TH1F* Eta_=(TH1F*)Files[f]->Get("bTagEffRA4bEl"+Algos[a]+Steps[s]+"/Num"+Flavors[flv]+"JetsEta");
		  TH1F* TaggedEta_=(TH1F*)Files[f]->Get("bTagEffRA4bEl"+Algos[a]+Steps[s]+"/Num"+Flavors[flv]+"JetsTaggedEta"); 

		  TaggedPt_->Divide(Pt_);

		  //--------------------------------------
		  // Draw y errors
		  //--------------------------------------

		  // define shift
		  double shift_=2*s;
		  double shift2_=4*s;
		  double shift3_=6*s;

		  // define array xbinsPt
		  Int_t nBins=TaggedPt_->GetNbinsX();
		  double xbinsPt[11];
		  
		  // fill array xbinsPt
		  double xbin0=TaggedPt_->GetBinLowEdge(1);
		  xbinsPt[0]=xbin0;
		  std::cout << xbin0 << std::endl;
		  // 
		  double xbin=0;
		  for(int ibin=1; ibin<TaggedPt_->GetNbinsX(); ++ibin)
		    {
		      xbin=xbin+TaggedPt_->GetXaxis()->GetBinWidth(ibin);
		      //if(TaggedPt_->GetXaxis()->GetBinWidth(ibin)>10) shift_=shift2_;
		      if(TaggedPt_->GetXaxis()->GetBinWidth(ibin)>20) shift_=shift3_;
		      //xbinsPt[ibin]=xbin+shift_*(TaggedPt_->GetXaxis()->GetBinWidth(ibin));
		      xbinsPt[ibin]=xbin+shift_;
		      std::cout << xbin[ibin] << std::endl;
		    }
		  //double xEndShift=shift_*(TaggedPt_->GetXaxis()->GetBinWidth(TaggedPt_->GetNbinsX()));
		  xbinsPt[TaggedPt_->GetNbinsX()]=TaggedPt_->GetBinLowEdge(TaggedPt_->GetNbinsX()+1)+shift_;
		  
		  // define new histogram TaggePt_
		  char Tmp [70];
		  sprintf(Tmp,"%i_%i_%i_%i_Pt", f, a, flv, s);
		  TH1F* Tmp_=new TH1F(Tmp, "Tmp", nBins, xbinsPt);

		  // fill histogram TaggedPt_
		  for(int ibin=0; ibin<Tmp_->GetNbinsX()+1; ++ibin)
		    {
		      std::cout << ibin << std::endl;
		      Tmp_->SetBinContent(ibin,TaggedPt_->GetBinContent(ibin));
		      Tmp_->SetBinError(ibin,TaggedPt_->GetBinError(ibin));
		    }

		  // draw histogram Tmp_
		  Tmp_->SetTitle(Flavors[flv]+"Jets tag efficiency "+Algos[a]);
		  Tmp_->GetXaxis()->SetTitle("p_{T} [GeV]");
		  Tmp_->GetXaxis()->CenterTitle();
		  Tmp_->GetYaxis()->SetTitle("b-tag efficiency");
		  Tmp_->GetYaxis()->CenterTitle();
		  Tmp_->SetLineColor(LineColors[s]);
		  if(s==0) Tmp_->Draw("E x0");
		  else Tmp_->Draw("same E x0");

		  //--------------------------------------
		  // Draw x errors
		  //--------------------------------------

		  // draw histogram TaggePt_    
		  TaggedPt_->SetLineColor(LineColors[s]);
		  for(int ibin=0; ibin<TaggedPt_->GetNbinsX()+1; ++ibin)
		    {
		      TaggedPt_->SetBinError(ibin,0.0000000001);
		    }

		  TaggedPt_->Draw("same");
		  
		  leg->AddEntry(TaggedPt_,SelectionNames[s],"l");
		  
		}
	      leg->Draw("box");
	      canvas->SaveAs(Names[f]+"_"+Algos[a]+"_"+Flavors[flv]+"jetsEff_ElPt.pdf");


	      //----------------------------------------------------------------------------------------------
	      //----------------------------------------------------------------------------------------------
	      //----------------------------------------------------------------------------------------------


	      // Define canvas2., legend etc.
	      TCanvas *canvas2 =new TCanvas(Names[f]+"_"+Algos[a]+"_"+Flavors[flv]+"_Eta",Names[f]+"_"+Algos[a]+"_"+Flavors[flv]+"_Eta",1);
	      TLegend *leg = new TLegend(.6,.1,.99,.4);
	      leg->SetTextFont(42);
	      leg->SetFillColor(0);
	      leg->SetLineColor(0);
	      
	      // loop over selection steps
	      for(int s=0; s < Steps.size(); ++s)
		{
		  std::cout << "Selection step " << Steps[s] <<  std::endl;

		  std::cout << "bTagEffRA4bEl"+Algos[a]+Steps[s]+"/Num"+Flavors[flv]+"JetsEta" << std::endl;

		  TH1F* Eta_=(TH1F*)Files[f]->Get("bTagEffRA4bEl"+Algos[a]+Steps[s]+"/Num"+Flavors[flv]+"JetsEta");
		  TH1F* TaggedEta_=(TH1F*)Files[f]->Get("bTagEffRA4bEl"+Algos[a]+Steps[s]+"/Num"+Flavors[flv]+"JetsTaggedEta");
		  
		  TH1F* Eta_=(TH1F*)Files[f]->Get("bTagEffRA4bEl"+Algos[a]+Steps[s]+"/Num"+Flavors[flv]+"JetsEta");
		  TH1F* TaggedEta_=(TH1F*)Files[f]->Get("bTagEffRA4bEl"+Algos[a]+Steps[s]+"/Num"+Flavors[flv]+"JetsTaggedEta"); 

		  TaggedEta_->Divide(Eta_);

		  //--------------------------------------
		  // Draw y errors
		  //--------------------------------------

		  // define shift
		  shift_=0.025*s;

		  // define array xbinsEta
		  Int_t nBins=TaggedEta_->GetNbinsX();
		  double xbinsEta[8];
		  
		  // fill array xbinsEta
		  double xbin0=TaggedEta_->GetBinLowEdge(1);
		  xbinsEta[0]=xbin0;
		  std::cout << xbin0 << std::endl;
		  // 
		  xbin=0;
		  for(int ibin=1; ibin<TaggedEta_->GetNbinsX(); ++ibin)
		    {
		      xbin=xbin+TaggedEta_->GetXaxis()->GetBinWidth(ibin);
		      xbinsEta[ibin]=xbin+shift_;
		      std::cout << xbin[ibin] << std::endl;
		    }
		  xbinsEta[TaggedEta_->GetNbinsX()]=TaggedEta_->GetBinLowEdge(TaggedEta_->GetNbinsX()+1)+shift_;
		  
		  // define new histogram TaggeEta_
		  char TmpEta [70];
		  sprintf(TmpEta,"%i_%i_%i_%i_Eta", f, a, flv, s);
		  TH1F* TmpEta_=new TH1F(TmpEta, "TmpEta", nBins, xbinsEta);

		  // fill histogram TaggedEta_
		  for(int ibin=0; ibin<TmpEta_->GetNbinsX()+1; ++ibin)
		    {
		      std::cout << ibin << std::endl;
		      TmpEta_->SetBinContent(ibin,TaggedEta_->GetBinContent(ibin));
		      TmpEta_->SetBinError(ibin,TaggedEta_->GetBinError(ibin));
		    }

		  // draw histogram TmpEta_
		  TmpEta_->SetTitle(Flavors[flv]+"Jets tag efficiency "+Algos[a]);
		  TmpEta_->GetXaxis()->SetTitle("Eta");
		  TmpEta_->GetXaxis()->CenterTitle();
		  TmpEta_->GetYaxis()->SetTitle("b-tag efficiency");
		  TmpEta_->GetYaxis()->CenterTitle();
		  TmpEta_->SetLineColor(LineColors[s]);
		  if(s==0) TmpEta_->Draw("E x0");
		  else TmpEta_->Draw("same E x0");

		  //--------------------------------------
		  // Draw x errors
		  //--------------------------------------

		  // draw histogram TaggeEta_    
		  TaggedEta_->SetLineColor(LineColors[s]);
		  for(int ibin=0; ibin<TaggedEta_->GetNbinsX()+1; ++ibin)
		    {
		      TaggedEta_->SetBinError(ibin,0.0000000001);
		    }

		  TaggedEta_->Draw("same");
		  
		  leg2->AddEntry(TaggedEta_,SelectionNames[s],"l");
		  
		}
	      //leg2->Draw("box");
	      canvas2->SaveAs(Names[f]+"_"+Algos[a]+"_"+Flavors[flv]+"jetsEff_ElEta.pdf");


	    }
	}
      std::cout << "" << std::endl;
    }

  return 0;
  
}
