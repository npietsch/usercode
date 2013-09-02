#include "StackMC.h"
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
void LM(){

	setTDRStyle();
	gStyle->SetPadTopMargin(0.1);
	gStyle->SetPadLeftMargin(0.14);
	gStyle->SetPadBottomMargin(0.13);
	gStyle->SetPadRightMargin(0.05);

	gStyle->SetLineStyleString(11,"14 12");
   
	double dataLumi = 4980;//4965.876/pb. -20/pb in ele
	double SF=1; // scale factor - missing part lepton id
	//double nEvt=421190;
	//double Xsec=1.029;
	double nEvt=427625;
	double Xsec=0.404;
	// define files
	TFile* All_file          = new TFile("LM6.root",          "READ");
	TFile* GluinoPair_file   = new TFile("LM6_GluinoPair.root",          "READ");
	TFile* GluinoSquark_file = new TFile("LM6_GluinoSquark.root",          "READ");
	TFile* SquarkPair_file   = new TFile("LM6_SquarkPair.root",          "READ");
	TFile* StopSbottom_file  = new TFile("LM6_StopSbottom.root",          "READ");
	TFile* Other_file        = new TFile("LM6_Other.root",          "READ");

	TFile* Dummy_file        = new TFile("Dummy.root",          "READ");

 	//addMCHistogram(TString name, int xmin, int xmax)
// 	addMCHistogram("analyzeBino_45Jets_1/HT",         "H_{T} [GeV]",         "Events / 50 GeV", 500,  5000, 1, 1e6, -0.1, 2.1, 1);
 	addMCHistogram("analyzeSUSYGenEvent1m_noCuts/nrBQuarks", "Number of b-quarks", "Events", 0, 6, 0.1, 1900, -0.1, 2.1, 1);
	//addMCHistogram("analyzeSUSY3b1m_1/nJets", "Number of jets", "Events", 0, 14, 0.1, 20, -0.1, 2.1, 1);
	for(int hdx=0; hdx<(int)Histograms.size(); ++hdx)
	  {
	    std::cout << Histograms[hdx] << std::endl;

	    // get histograms#3, 0.48, 0.9499, 0.9);
	    TH1D* All          = (TH1D*)All_file          ->Get(Histograms[hdx]);
	    TH1D* GluinoPair   = (TH1D*)GluinoPair_file   ->Get(Histograms[hdx]);
	    TH1D* GluinoSquark = (TH1D*)GluinoSquark_file ->Get(Histograms[hdx]);
	    TH1D* SquarkPair   = (TH1D*)SquarkPair_file   ->Get(Histograms[hdx]);
	    TH1D* StopSbottom  = (TH1D*)StopSbottom_file  ->Get(Histograms[hdx]);
	    TH1D* Other        = (TH1D*)Other_file        ->Get(Histograms[hdx]);

	    TH1D* Dummy     = (TH1D*)Dummy_file     ->Get(Histograms[hdx]);
	    
	    // stack with ratio
	    StackWithRatio sr(dataLumi, XTitles[hdx], YTitles[hdx], "Data/Simulation");
	    sr.SetXRange(Xmin[hdx],Xmax[hdx]);
	    sr.SetStackYRange(Ymin[hdx],Ymax[hdx]);
	    sr.SetRatioYRange(Smin[hdx],Smax[hdx]);
	    
	    sr.band   = false; // draw an error band
	    sr.relsys = 0.27; // relative systematic uncertainty#tilde{t}#tilde{t
	    
	    sr.rebOff =  0;  // rebinning offset = number of empty bin at the low edge
	    sr.rebN   =  1;  // # bins to merge
	    
	    sr.SF     = SF;  // scale\end{frame} factor data MC which is not yet included in rootfiles
	    	 
	    sr.AddData(Dummy);

	    // MC histogram, color,    nevnts, x-sect
	    sr.Add(Other,        kRed+2,    nEvt, Xsec);
	    sr.Add(SquarkPair,   kBlue-7,   nEvt, Xsec);
	    sr.Add(GluinoSquark, kGreen-3,  nEvt, Xsec);
	    sr.Add(GluinoPair,   kYellow-4, nEvt, Xsec);
	    sr.Add(StopSbottom,  kRed-4,    nEvt, Xsec);

	    TCanvas* c1 = new TCanvas(Histograms[hdx],Histograms[hdx],600,600);
	    //c1->SetLogy();

	    sr.DrawClone();
	    
	    TLegend *leg = new TLegend(0.7, 0.48, 0.9499, 0.9);
	    leg->SetTextSize(0.05);
	    leg->SetFillColor(0);
	    leg->AddEntry(StopSbottom, "#tilde{t}#kern[0.0]{#tilde{t}}*#kern[0.2]{+}#kern[0.3]{#tilde{b}}#tilde{b}*","f");
	    leg->AddEntry(GluinoPair,  "#tilde{g}#tilde{g}", "f");
	    leg->AddEntry(GluinoSquark,"#tilde{q}#tilde{g}", "f");
	    leg->AddEntry(SquarkPair,  "#tilde{q}#kern[0.0]{#tilde{q}}*#kern[0.2]{+}#kern[0.3]{#tilde{q}}#tilde{q}", "f");
	    leg->AddEntry(Other,       "other",              "f");
	    leg->SetBorderSize(1);
	    if(Legend[hdx] == 1) leg->Draw();
	    	    
	    TPaveText *label = new TPaveText(0.15,0.91,0.99,1.,"NDC");
	    label->SetFillColor(0);
	    label->SetTextFont(62);
	    label->SetTextSize(0.05);
	    label->SetBorderSize(0);
	    label->SetTextAlign(12);
	    TText *text=label->AddText("Simulation, 4.98 fb^{-1}, #sqrt{s} = 7 TeV");
	    label->Draw();

// 	    TLatex *t1 = new TLatex(0,1.8e5,"L = 4.98 fb^{-1}, #sqrt{s} = 7 TeV");
// 	    t1->SetTextSize(0.05);
// 	    t1->Draw();

	    TString NAME = Histograms[hdx]+".pdf";
	    NAME.ReplaceAll("/", "_");
	    c1->SaveAs(NAME);
	  }
}
