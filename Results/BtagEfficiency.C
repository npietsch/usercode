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
#include <TDRStyle.h>

vector<TFile*> Files;
vector<TString> Samples;
vector<TString> Names;

vector<TString> Selections;

vector<TString> Histograms;
vector<unsigned int> Colors;
vector<unsigned int> LineStyles;
vector<unsigned int> LineWidths;
vector<unsigned int> MarkerStyles;
vector<unsigned int> MarkerSizes;

// add  sample
void addSample(TFile* file, TString sample, TString name)
{
  Files.push_back(file);
  Samples.push_back(sample);
  Names.push_back(name);
}

// add selection step 
void addHistogram(TString selection)
{
  Selections.push_back(selection);
}

// add histogram
void addHistogram(TString name, int color, int lineStyle, int lineWidth, int markerStyle, int markerSize)
{
  Histograms.push_back(name);
  Colors.push_back(color);
  LineStyles.push_back(lineStyle);
  LineWidths.push_back(lineWidth);
  MarkerStyles.push_back(markerStyle);
  MarkerSizes.push_back(markerSize);
}

// main function
int BtagEfficiency()
{
  //--------------------------------------------------------------
  // Declare Samples
  //--------------------------------------------------------------

  TFile* TTJetsFall11   = new TFile("TTJetsFall11_new.root",   "READ");

  //-------------------------------------------------------------------------------------------------------------------
  // addSample(TFile* sample, TString name)
  //-------------------------------------------------------------------------------------------------------------------

  addSample(TTJetsFall11, "TTJets", "t#bar{t}+Jets");

  //-------------------------------------------------------------------------------------------------
  // 
  //-------------------------------------------------------------------------------------------------

  Selections.push_back("analyzeBTagsMu");
  
  //-------------------------------------------------------------------------------------------------
  // 
  //-------------------------------------------------------------------------------------------------

  addHistogram("b_trackCountingHighEffBJetTags", 2, 1, 1, 1, 1);
  addHistogram("q_trackCountingHighEffBJetTags", 4, 1, 1, 1, 1);
  addHistogram("g_trackCountingHighEffBJetTags", 1, 1, 1, 1, 1);

  //------------
  // set style 
  //------------ 

  setTDRStyle();

  //--------
  // Plot
  //--------

  // loop over samples
   for(int ndx=0; ndx<(int)Files.size(); ++ndx)
     {

       std::cout << "\n"<< Names[ndx] << std::endl;
       std::cout << "---------------" << std::endl;

       // loop over selections
       for(int sdx=0; sdx<(int)Selections.size(); ++sdx)
	 {
	   TCanvas *c1=new TCanvas(Selections[sdx]+"_"+Histograms[0]+"_"+Names[ndx],Selections[sdx]+"_"+Histograms[0]+"_"+Names[ndx], 1);
	   
	   gPad->SetLogy();

	   // legend
	   TLegend *leg = new TLegend(.29,.68,.91,.89);
	   leg->SetTextFont(42);
	   leg->SetTextSize(0.043);
	   leg->SetFillColor(0);
	   leg->SetShadowColor(0);
	   leg->SetLineColor(1);
      
	   // label
	   TPaveText *label = new TPaveText(0.14,0.94,0.99,1.,"NDC");
	   label->SetFillColor(0);
	   label->SetTextFont(42);
	   label->SetTextSize(0.043);
	   label->SetBorderSize(0);
	   label->SetTextAlign(12);
	   TText *text=label->AddText("Simulation, #sqrt{s} = 7 TeV");

	   for(int hdx=0; hdx<(int)Histograms.size(); ++hdx)
	     {
	       if(hdx == 0)
		 {
		   std::cout << "Draw histogram 1" << std::endl;
 
		   // Draw first histogram
		   TH1F* Temp=(TH1F*)Files[ndx]->Get(Selections[sdx]+"/"+Histograms[0]);
		   
		   // Title
		   Temp->SetTitle("");
		   
		   // Axes
		   Temp->GetXaxis()->SetTitle("B-discriminator");
		   Temp->GetXaxis()->SetTitleSize(0.05);
		   Temp->GetXaxis()->SetTitleFont(42);
		   Temp->GetXaxis()->SetTitleOffset(1.2);
		   
		   Temp->GetYaxis()->SetTitle("a.u.");
		   Temp->GetYaxis()->SetTitleOffset(1.5);
		   Temp->GetYaxis()->SetTitleSize(0.05);
		   Temp->GetYaxis()->SetTitleFont(42);
		   
		   // Labels
		   Temp->SetLabelColor(1, "XYZ");
		   Temp->SetLabelFont(42, "XYZ");
		   Temp->SetLabelOffset(0.007, "XYZ");
		   Temp->SetLabelSize(0.04, "XYZ");

		   // Line color, style, and width
		   Temp->SetLineColor(Colors[hdx]);
		   Temp->SetLineStyle(LineStyles[hdx]);
		   Temp->SetLineWidth(LineWidths[hdx]);
		   
		   Temp->Draw();
		 }
	       else
		 {
		   std::cout << "Draw histogram " << hdx+1 << std::endl;
		   
		   // Draw furhter histogram
		   TH1F* Temp=(TH1F*)Files[ndx]->Get(Selections[sdx]+"/"+Histograms[hdx]);
		   Temp->Draw("same");

		   // Line color, style, and width
		   Temp->SetLineColor(Colors[hdx]);
		   Temp->SetLineStyle(LineStyles[hdx]);
		   Temp->SetLineWidth(LineWidths[hdx]);
		 }
	     }
	   
	   // 	   // Draw legend and labels
 	   leg->Draw();
 	   label->Draw("same");
	   
	   // Save canvas
	   
	 }
     }
}
