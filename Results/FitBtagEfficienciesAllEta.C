#include <vector>
#include <iostream>
#include <bitset>
#include <vector>
#include <fstream>
#include "TFile.h"
#include "TH1.h"
#include "TH2.h"
#include "TF1.h"
#include "TCanvas.h"
#include "TStyle.h"
#include "TLegend.h"
#include "TPaveText.h"
#include "TDRStyle_FitBtagEfficienciesAllEta.h"

vector<TFile*> Files;
vector<TString> Names;
vector<unsigned int> SampleColors;
vector<unsigned int> MarkerStyles;
vector<double> MarkerSizes;
vector<unsigned int> FitStyles;

vector<TString> Algos;

vector<TString> Flavors;

vector<TString> Steps;
vector<unsigned int> LineColors;
vector<TString> SelectionNames;

vector<TH1F*> Histograms;

// function addSample
void addSample(TFile* sample, TString name, int lc, int ms, double msize, int fs);

void addSample(TFile* sample, TString name, int lc, int ms, double msize, int fs)
{
  Files.push_back(sample);
  Names.push_back(name);
  SampleColors.push_back(lc);
  MarkerStyles.push_back(ms);
  MarkerSizes.push_back(msize);
  FitStyles.push_back(fs);
}

// funtion addAlgorithm
void addAlgorithm(TString name);

void addAlgorithm(TString name)
{
  Algos.push_back(name);
}

// funtion addSelectionStep
void addSelectionStep(TString name, int lc, TString sn);

void addSelectionStep(TString name, int lc, TString sn)
{
  Steps.push_back(name);
  LineColors.push_back(lc);
  SelectionNames.push_back(sn);
}

// fit ranges
Double_t x0=40;
Double_t x1=90;
Double_t x2=185;
Double_t x3=670;

// fit function
Double_t fitf(Double_t *x, Double_t *par)
{
  double fitValue=0;
  
  if(x0 < x[0] && x[0] <= x1)
    {
      fitValue=par[0]+par[1]*(x[0]-x0);
    }
  else if(x1 < x[0] && x[0] <= x2) 
    {
      fitValue=par[0]+par[1]*(x1-x0);//+par[2]*(x[0]-x1);
    }
  else if(x2 <= x[0] && x[0] <= x3) 
    {
      fitValue=par[0]+par[1]*(x1-x0)+par[2]*(x[0]-x2);
    }
  
  return fitValue;
 }

int BtagEfficienciesAllEta()
{
  //-----------------------------------------------------
  // Define samples
  //-----------------------------------------------------

  TFile* TTJets    = new TFile("TTJetsFall11_2.root", "READ");
  TFile* WJetsHT   = new TFile("WJetsHT.root",        "READ");
  TFile* SingleTop = new TFile("SingleTop.root",      "READ");

  TFile* LM3       = new TFile("LM3.root",            "READ");
  TFile* LM8       = new TFile("LM8.root",            "READ");
  TFile* LM13      = new TFile("LM13.root",           "READ");

  //-----------------------------------------------------
  // addSample(TFile* sample, TString name)
  //-----------------------------------------------------

  addSample(TTJets,    "T#bar{T}+Jets", kRed,     20, 1.1, 7);
//   addSample(SingleTop, "single top",    kBlue,    20, 1.1, 7);
//   addSample(WJetsHT,   "W+Jets",        kGreen+2, 23, 1.2, 7);

//   addSample(LM3,  "LM3",  kRed+2,   20, 0.9, 7);
//   addSample(LM8,  "LM8",  kBlue,    23, 1.1, 7);
//   addSample(LM13, "LM13", kGreen+2, 24, 1.2, 7);

  //-----------------------------------------------------
  // addAlgorithm(TString name)
  //-----------------------------------------------------

  addAlgorithm("TCHEM");

  //-----------------------------------------------------
  // Flavors
  //-----------------------------------------------------

  Flavors.push_back("B");
  //Flavors.push_back("C");
  //Flavors.push_back("L");

  //-----------------------------------------------------
  // addSelectionStep(TString name, int lc, TString sn);
  //-----------------------------------------------------

  addSelectionStep("", 8, "RA4b");

  //-----------------------------------------------------
  // set Style
  //-----------------------------------------------------

  setTDRStyle();
 
  // loop over algorithms
  for(int a=0; a<Algos.size(); ++a)
    {
      std::cout << Algos[a] << std::endl;
      
      // loop over flavor	  
      for(int flv=0; flv<(int)Flavors.size(); ++flv)
	{
	  // loop over selection steps
	  for(int s=0; s < Steps.size(); ++s)
	    {
	      std::cout << "Selection step " << Steps[s] <<  std::endl;
	       
	      // Define canvas, legend and labels
	      TCanvas *canvas =new TCanvas(SelectionNames[s]+"_"+Algos[a]+"_"+Flavors[flv]+"_Pt",SelectionNames[s]+"_"+Algos[a]+"_"+Flavors[flv]+"_Pt",1);

	      TLegend *leg = new TLegend(.68,.18,.91,.245);
	      //TLegend *leg = new TLegend(.64,.18,.91,.35);
	      leg->SetTextFont(42);
	      leg->SetFillColor(0);
	      leg->SetLineColor(1);
	      
	      TPaveText *label = new TPaveText(0.14,0.91,0.6,0.99,"NDC");
	      label->SetFillColor(0);
	      label->SetTextFont(42);
	      label->SetBorderSize(0);
	      TText *text=label->AddText("CMS Simulation, #sqrt{s}=7 TeV");
	      text->SetTextAlign(22);
	      
	      TPaveText *label2 = new TPaveText(0.33,0.23,0.53,0.33,"NDC");
	      label2->SetFillColor(0);
	      label2->SetTextFont(62);
	      label2->SetBorderSize(0);
	      TText *text2=label2->AddText("0 < |#eta| < 2.4");
	      text2->SetTextAlign(22);

	      TPaveText *label3 = new TPaveText(.60,.68,.91,.85,"NDC");
	      label3->SetFillColor(0);
	      label3->SetTextFont(42);
	      label3->SetBorderSize(1);
	      TText *text3=label3->AddText("p0    0.63195 #pm 0.00266");
	      TText *text4=label3->AddText("p1    0.00216 #pm 0.00007");
	      TText *text5=label3->AddText("p2   -0.00054 #pm 0.00003");
	      text3->SetTextAlign(22);

	      // declare Maximum and ybin
	      double Maximum=0;

	      // loop over files
	      for(int f=0; f<(int)Files.size(); ++f)
		{
		  TH1F* Pt_=(TH1F*)Files[f]->Get("bTagEffRA4bMu"+Algos[a]+Steps[s]+"/Num"+Flavors[flv]+"JetsPt");
		  TH1F* Pt2_=(TH1F*)Files[f]->Get("bTagEffRA4bEl"+Algos[a]+Steps[s]+"/Num"+Flavors[flv]+"JetsPt");
		  Pt_->Add(Pt2_);

		  TH1F* TaggedPt_=(TH1F*)Files[f]->Get("bTagEffRA4bMu"+Algos[a]+Steps[s]+"/Num"+Flavors[flv]+"JetsTaggedPt");
		  TH1F* TaggedPt2_=(TH1F*)Files[f]->Get("bTagEffRA4bEl"+Algos[a]+Steps[s]+"/Num"+Flavors[flv]+"JetsTaggedPt");
		  TaggedPt_->Add(TaggedPt2_);

		  TaggedPt_->Divide(Pt_);
		  
		  // define shifts of markers in x direction
		  double shift_=3*(f);
		  double shift2_=5*(f);
		  double shift3_=7*(f);
		  
		  // define int nBins and arrays xbinsPt and xbinsPtX
		  Int_t nBins=TaggedPt_->GetNbinsX();
		  double xbinsPt[18];
		  double xbinsPtX[18];

		  // fill arrays xbinsPt and xbinsPtX
		  double xbin0=TaggedPt_->GetBinLowEdge(1);
		  xbinsPt[0]=xbin0;
		  xbinsPtX[0]=xbin0;

		  double ibinX=0;
		  for(int xbin=1; xbin<TaggedPt_->GetNbinsX(); ++xbin)
		    {
		      ibinX=ibinX+TaggedPt_->GetXaxis()->GetBinWidth(xbin);
		      if(TaggedPt_->GetXaxis()->GetBinWidth(xbin)>20) shift_=shift3_;

		      xbinsPtX[xbin]=ibinX;
		      xbinsPt[xbin]=ibinX+shift_;
		    }
		  xbinsPt[TaggedPt_->GetNbinsX()]=TaggedPt_->GetBinLowEdge(TaggedPt_->GetNbinsX()+1)+shift_;
		  xbinsPtX[TaggedPt_->GetNbinsX()]=TaggedPt_->GetBinLowEdge(TaggedPt_->GetNbinsX()+1);

		  // define new histograms Tmp_ and Tmp2_
		  char Tmp [70];
		  char Tmp2 [70];
		  sprintf(Tmp,"%i_%i_%i_%i_Pt", f, a, flv, s);
		  sprintf(Tmp2,"%i_%i_%i_%i_Pt2", f, a, flv, s);
		  TH1F* Tmp_=new TH1F(Tmp, Tmp, nBins, xbinsPt);
		  TH1F* Tmp2_=new TH1F(Tmp2, Tmp2, nBins, xbinsPtX);

		  // fill histogramw Tmp_ and Tmp2_
		  for(int xbin=0; xbin<Tmp_->GetNbinsX()+1; ++xbin)
		    {
		      Tmp_->SetBinContent(xbin,TaggedPt_->GetBinContent(xbin));
		      Tmp_->SetBinError(xbin,TaggedPt_->GetBinError(xbin));
		      
		      Tmp2_->SetBinContent(xbin,TaggedPt_->GetBinContent(xbin));
		      Tmp2_->SetBinError(xbin,0.0000001);

		      if(TaggedPt_->GetBinContent(xbin)+TaggedPt_->GetBinError(xbin) > Maximum)
			{
			  Maximum=TaggedPt_->GetBinContent(xbin)+TaggedPt_->GetBinError(xbin);
			}
		    }

		  //--------------------------------------
		  // Define and draw histograms
		  //--------------------------------------

		  // Draw marker
		  Tmp_->SetTitle("");

		  if(Flavors[flv]=="B")
		    {
		      Tmp_->SetMaximum(1);
		      Tmp_->SetMinimum(0);
		      Tmp_->GetXaxis()->SetTitle("b-jet p_{T} [GeV]");
		      Tmp_->GetYaxis()->SetTitle("b-tag efficiency");
		    }
		  if(Flavors[flv]=="C")
		    {
		      Tmp_->SetMaximum(1.05*0.599472);
		      Tmp_->SetMinimum(0);
		      Tmp_->GetXaxis()->SetTitle("c-jet p_{T} [GeV]");
		      Tmp_->GetYaxis()->SetTitle("mistag efficiency");
		    }
		  if(Flavors[flv]=="L")
		    {
		      Tmp_->SetMaximum(1.05*0.117256);
		      Tmp_->SetMinimum(0);
		      Tmp_->GetXaxis()->SetTitle("light quark/gluon jet p_{T} [GeV]");
		      Tmp_->GetYaxis()->SetTitle("mistag efficiency");
		    }

		  Tmp_->GetXaxis()->SetTitleOffset(1.2); 
		  Tmp_->GetYaxis()->SetTitleOffset(1.);
		  Tmp_->SetLineColor(SampleColors[f]);
		  Tmp_->SetLineWidth(1);
		  Tmp_->SetMarkerStyle(MarkerStyles[f]);
		  Tmp_->SetMarkerColor(SampleColors[f]);
		  Tmp_->SetMarkerSize(MarkerSizes[f]);		      
		  if(f==0) Tmp_->Draw("E x0");
		  else Tmp_->Draw("same E x0");
		  
		  // Draw x-errors
		  Tmp2_->SetLineColor(SampleColors[f]);
		  Tmp2_->SetLineWidth(1);
		  Tmp2_->Draw("same");

		  // fit function
		  Double_t parameters[6];

 		  if(Flavors[flv] == "B")
 		    {
		      TF1 *g1 = new TF1("g1","[0]+[1]*x",x0,x1);
		      g1->SetLineColor(SampleColors[f]);
		      g1->SetLineWidth(1);
		      Tmp_->Fit(g1,"R");
		      Tmp_->GetFunction("g1")->ResetBit(1<<9);
		      
		      TF1 *g2 = new TF1("g2","[0]+[1]*x",x1,x2);
		      g2->SetLineColor(SampleColors[f]);
		      g2->SetLineWidth(1);
		      Tmp_->Fit(g2,"R+");
		      Tmp_->GetFunction("g2")->ResetBit(1<<9);

		      TF1 *g3 = new TF1("g3","[0]+[1]*x",x2,x3);
		      g3->SetLineColor(SampleColors[f]);
		      g3->SetLineWidth(1);
		      Tmp_->Fit(g3,"R+");
		      Tmp_->GetFunction("g3")->ResetBit(1<<9);

		      g1->GetParameters(&parameters[0]);
		      g2->GetParameters(&parameters[2]);
		      g3->GetParameters(&parameters[4]);

		      TF1 *func = new TF1("fitf", fitf, x0, x3, 3);

		      // Sets initial values
		      func->SetParameters(parameters[0],parameters[1],parameters[5]);
		      //func->SetParameters(6.32386e-01, 2.13442e-03, 2.56885e-05, -5.44586e-04);
		      func->SetLineColor(1);
		      func->SetLineWidth(3);
		      //func->SetNpx(1000);
		      //func->Draw("same");

		      // Fit histogram in range defined by function
		      Tmp_->Fit(func,"R");
		      //Tmp_->GetFunction("func")->ResetBit(1<<9);

		      func->SetParameters(0,0.1);

		    }
		  leg->AddEntry(Tmp_,Names[f],"l P");

	      std::cout << "==============================" << std::endl;
	      std::cout << "Maximum: " << Maximum << std::endl;
	      std::cout << "==============================" << std::endl;

	      leg->SetShadowColor(0);
	      //leg->Draw();
	      label->Draw();
	      //label2->Draw();
	      label3->Draw();

	      canvas->SaveAs(Algos[a]+"_"+Flavors[flv]+"jetsEfficiency.png");
	      
		}
	    }
	}
    }
  std::cout << "" << std::endl;
  
  return 0;
}
