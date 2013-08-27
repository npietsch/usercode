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
#include "TPaveText.h";
#include <TDRStyle.h>

vector<TFile*> Files;
vector<TString> Samples;
vector<TString> Names;

vector<TString> Selections;

vector<TString> Histograms;
vector<TString> Labels;
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
void addHistogram(TString name, TString label, int color, int lineStyle, int lineWidth, int markerStyle, int markerSize)
{
  Histograms.push_back(name);
  Labels.push_back(label);
  Colors.push_back(color);
  LineStyles.push_back(lineStyle);
  LineWidths.push_back(lineWidth);
  MarkerStyles.push_back(markerStyle);
  MarkerSizes.push_back(markerSize);
}

// main function
int BtagEfficiency()
{
  bool Normalize=true;

  //--------------------------------------------------------------
  // Declare Samples
  //--------------------------------------------------------------

  TFile* TTJetsFall11   = new TFile("TTJetsFall11_new.root",   "READ");

  //-------------------------------------------------------------------------------------------------------------------
  // addSample(TFile* file, TString sample, TString name)
  //-------------------------------------------------------------------------------------------------------------------

  addSample(TTJetsFall11, "TTJets", "t#bar{t}+Jets");

  //-------------------------------------------------------------------------------------------------
  // addHistogram(TString selection)
  //-------------------------------------------------------------------------------------------------

  Selections.push_back("analyzeBTagsMu");
  
  //--------------------------------------------------------------------------------------------------------------------
  // addHistogram(TString name, TString label, int color, int lineStyle, int lineWidth, int markerStyle, int markerSize)
  //--------------------------------------------------------------------------------------------------------------------

  addHistogram("b_trackCountingHighEffBJetTags", "b-jets",     2, 1, 2, 20, 1);
  addHistogram("c_trackCountingHighEffBJetTags", "c-jets",     4, 1, 2, 22, 1.1);
  addHistogram("l_trackCountingHighEffBJetTags", "other jets", 1, 1, 2, 23, 1.1);

  //------------
  // set style 
  //------------ 

  setTDRStyle();

  //--------
  // Plot
  //--------

  // loop over samples
   for(int fdx=0; fdx<(int)Files.size(); ++fdx)
     {

       std::cout << "\n"<< Names[fdx] << std::endl;
       std::cout << "---------------" << std::endl;

       // loop over selections
       for(int sdx=0; sdx<(int)Selections.size(); ++sdx)
	 {
	   TCanvas *c1=new TCanvas(Samples[fdx]+"_"+Selections[sdx],Samples[fdx]+"_"+Selections[sdx], 1);
	   
	   gPad->SetLogy();

	   // legend
	   //TLegend *leg = new TLegend(.59,.67,.90,.88);
	   //TLegend *leg = new TLegend(.59,.19,.90,.40);
	   TLegend *leg = new TLegend(.19,.59,.45,.88);
	   leg->SetTextFont(42);
	   leg->SetTextSize(0.05);
	   leg->SetFillColor(0);
	   leg->SetLineColor(1);
	   leg->SetShadowColor(0);
	   leg->SetLineColor(1);
	   leg->AddEntry((TObject*)0, Names[fdx], "");

	   // label
	   TPaveText *label = new TPaveText(0.14,0.94,0.99,1.,"NDC");
	   label->SetFillColor(0);
	   label->SetTextFont(42);
	   label->SetTextSize(0.043);
	   label->SetBorderSize(0);
	   label->SetTextAlign(12);

	   if(Normalize == true)
	     {
	       TText *text=label->AddText("Simulation, #sqrt{s} = 7 TeV");
	     }
	       else
	     {
	       TText *text=label->AddText("Simulation, #sqrt{s} = 7 TeV");
	     }

	   for(int hdx=0; hdx<(int)Histograms.size(); ++hdx)
	     {
	       if(hdx == 0)
		 {
		   std::cout << "Draw histogram 1" << std::endl;
 
		   // Draw first histogram
		   TH1F* Temp=(TH1F*)Files[fdx]->Get(Selections[sdx]+"/"+Histograms[0]);
		   
		   // Title
		   Temp->SetTitle("");
		   
		   // Scales
		   if(Normalize == true)
		     {
		       Temp->Scale(1/(Temp->Integral()));
		       Temp->SetMaximum(1);
		       Temp->SetMinimum(0.00001);
		       Temp->GetYaxis()->SetTitle("a.u.");
		     }
		   else
		     {
		       Temp->Scale(0.013);
		       Temp->SetMaximum(10000);
		       Temp->SetMinimum(0.1);
		       Temp->GetYaxis()->SetTitle("Matched Jets");
		     }

		   // Axes
		   Temp->GetXaxis()->SetTitle("B-discriminator");
		   Temp->GetXaxis()->SetTitleSize(0.05);
		   Temp->GetXaxis()->SetTitleFont(42);
		   Temp->GetXaxis()->SetTitleOffset(1.2);
		   
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

		   // Marker style, color, style, and size
		   Temp->SetMarkerStyle(MarkerStyles[hdx]);
		   Temp->SetMarkerColor(Colors[hdx]);
		   Temp->SetMarkerSize(MarkerSizes[hdx]);
		   
		   Temp->Draw();

		   leg->AddEntry(Temp, Labels[hdx] ,"l P");

		 }
	       else
		 {
		   std::cout << "Draw histogram " << hdx+1 << std::endl;

		   // Draw furhter histogram
		   TH1F* Temp=(TH1F*)Files[fdx]->Get(Selections[sdx]+"/"+Histograms[hdx]);
		   Temp->Draw("same");

		   // Scale
		   if(Normalize == true)
		     {
		       Temp->Scale(1/(Temp->Integral()));
		     }
		   else
		     {
		       Temp->Scale(0.013);
		     }

		   // Line color, style, and width
		   Temp->SetLineColor(Colors[hdx]);
		   Temp->SetLineStyle(LineStyles[hdx]);
		   Temp->SetLineWidth(LineWidths[hdx]);

		   // Marker style, color, style, and size
		   Temp->SetMarkerStyle(MarkerStyles[hdx]);
		   Temp->SetMarkerColor(Colors[hdx]);
		   Temp->SetMarkerSize(MarkerSizes[hdx]);

		   leg->AddEntry(Temp, Labels[hdx] ,"l P");
		 }
	     }
	   
	   // Draw legend and labels
 	   leg->Draw();
 	   label->Draw();
	   
	   // TLine
	   TLine * line = new TLine(3.3, 0.00001, 3.3, 1);
	   line->SetLineWidth(2);
	   line->SetLineStyle(2);
	   line->SetLineColor(1);
	   line->Draw();
	   
	   // Save canvas
	   if(Normalize == true) c1->SaveAs(Samples[fdx]+"_"+Selections[sdx]+"_normalized.pdf");
	   else c1->SaveAs(Samples[fdx]+"_"+Selections[sdx]+".pdf"); 
	 }
     }
}
