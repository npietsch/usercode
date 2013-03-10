// systematic error from PAS Tab.5 SM MC 1b-tag
// N_D = 195.6 ± 7.2 ± 53.0 53/195.6=0.27
//
// MC SF 0.97 for lepton ID

#include "StackWithRatio.h"
#include "tdrStyle.h"

vector<TString> Histograms;
vector<TString> XTitles;
vector<TString> YTitles;
vector<double> Xmin;
vector<double> Xmax;
vector<double> Ymin;
vector<double> Ymax;
vector<double> Smin;
vector<double> Smax;
vector<int> Legend;

void addMCHistogram(TString name, TString XTitle, TString YTitle, double xmin, double xmax, double ymin, double ymax, double smin, double smax, int legend)
{
  Histograms.push_back(name);
  XTitles.push_back(XTitle);
  YTitles.push_back(YTitle);
  Xmin.push_back(xmin);
  Xmax.push_back(xmax);
  Ymin.push_back(ymin);
  Ymax.push_back(ymax);
  Smin.push_back(smin);
  Smax.push_back(smax);
  Legend.push_back(legend);
}

//-------------------- main --------------------
void Prelection14TeV(){

	setTDRStyle();
	gStyle->SetPadTopMargin(0.1);
	gStyle->SetLineStyleString(11,"14 12");
           
	double dataLumi = 4980;//4965.876/pb. -20/pb in ele
	double SF=0.97; // scale factor - missing part lepton id

	// define files
	TFile* TTJets_file    = new TFile("TTJets.root", "READ");
	//TFile* SingleTop_file = new TFile("SingleTop.root",    "READ");
	TFile* WJets_file     = new TFile("WJets.root",      "READ");
	TFile* ZJets_file     = new TFile("ZJets.root",        "READ");
	TFile* QCD_file       = new TFile("QCD.root",          "READ");
	
	TFile* A1_file       = new TFile("A1.root",          "READ");
	TFile* B1_file       = new TFile("B1.root",          "READ");
	TFile* C1_file       = new TFile("C1.root",          "READ");

	//addMCHistogram(TString name, int xmin, int xmax)	
	addMCHistogram("preselection14TeV/HT",  "H_{T} [GeV]","Events / 50 GeV", 0,  4000, 0.1, 1e7, -0.1, 2.1, 1);
	for(int hdx=0; hdx<(int)Histograms.size(); ++hdx)
	  {
	    // get histograms
	    TH1D* TTJets    = (TH1D*)TTJets_file    ->Get(Histograms[hdx]);
	    //TH1D* SingleTop = (TH1D*)SingleTop_file ->Get(Histograms[hdx]);
	    TH1D* WJets     = (TH1D*)WJets_file     ->Get(Histograms[hdx]);
	    TH1D* ZJets     = (TH1D*)ZJets_file     ->Get(Histograms[hdx]);
	    TH1D* QCD       = (TH1D*)QCD_file       ->Get(Histograms[hdx]);
	    
	    TH1D* A1        = (TH1D*)A1_file        ->Get(Histograms[hdx]);
	    TH1D* B1        = (TH1D*)B1_file        ->Get(Histograms[hdx]);
	    TH1D* C1        = (TH1D*)C1_file        ->Get(Histograms[hdx]);
	    
	    // stack with ratio
	    StackWithRatio sr(dataLumi, XTitles[hdx], YTitles[hdx], "Data/Simulation");
	    sr.SetXRange(Xmin[hdx],Xmax[hdx]);
	    sr.SetStackYRange(Ymin[hdx],Ymax[hdx]);
	    sr.SetRatioYRange(Smin[hdx],Smax[hdx]);
	    
	    sr.band   = false; // draw an error band
	    sr.relsys = 0.27; // relative systematic uncertainty
	    
	    sr.rebOff =  0;  // rebinning offset = number of empty bin at the low edge
	    sr.rebN   =  1;  // # bins to merge
	    
	    sr.SF     = SF;  // scale factor data MC which is not yet included in rootfiles
	    
	    // MC histogram, color,    nevnts, x-sect

	    sr.Add(QCD,       kRed+2,    1, 0.001);
	    sr.Add(ZJets,     kBlue-7,   1, 0.001);
	    //sr.Add(SingleTop, kGreen-3,  1, 0.001);
	    sr.Add(WJets,     kYellow-4, 1, 0.001);
	    sr.Add(TTJets,    kRed-4,    1, 0.001);

	    // add a few signal points
	    // extra lines in stack: histo, color, nevnts, x-sect, style (line width)
	    sr.AddExtra(A1,  kBlue,   1,   0.001,   1,  2); 
	    sr.AddExtra(B1,  kBlack,  1,   0.001,   1,  2);
	    sr.AddExtra(C1,  kBlack,  1,   0.001,   2,  3);

	    TCanvas* c1 = new TCanvas(Histograms[hdx],Histograms[hdx],600,700);
	    sr.DrawClone();
	    
	    sr.pad1->cd(); // stack
	    
	    TLegend *leg = new TLegend(0.68, 0.48, 0.9499, 0.9);
	    leg->SetTextSize(0.05);
	    leg->SetFillColor(0);
	    leg->AddEntry(TTJets,    "t#bar{t} + Jets",  "f");
	    leg->AddEntry(WJets,     "W + Jets",         "f");
	    //leg->AddEntry(SingleTop, "Single Top",       "f");
	    leg->AddEntry(ZJets,     "Z/#gamma* + Jets", "f");
	    leg->AddEntry(QCD,       "QCD",              "f");
	    leg->AddEntry(A1,        "scenario A",       "lp");
	    leg->AddEntry(B1,        "scenario B",       "lp");
	    leg->AddEntry(C1,        "scenario C",       "lp");
	    leg->SetBorderSize(1);
	    if(Legend[hdx] == 1) leg->Draw();
	    	    
	    TPaveText *label = new TPaveText(0.06,0.94,0.99,1.,"NDC");
	    label->SetFillColor(0);
	    label->SetTextFont(62);
	    label->SetTextSize(0.05);
	    label->SetBorderSize(0);
	    label->SetTextAlign(12);
	    TText *text=label->AddText("300 fb^{-1}, #sqrt{s} = 14 TeV");
	    label->Draw();

// 	    TLatex *t1 = new TLatex(0,1.8e5,"L = 4.98 fb^{-1}, #sqrt{s} = 7 TeV");
// 	    t1->SetTextSize(0.05);
// 	    t1->Draw();

	    TString NAME = Histograms[hdx]+".pdf";
	    NAME.ReplaceAll("/", "_");
	    c1->SaveAs(NAME);
	  }
}
