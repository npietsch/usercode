#include "StackMC.h"
#include "tdrStyle_14TeV.h"

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
void Preselection14TeV(){

	setTDRStyle();
	gStyle->SetPadTopMargin(0.1);
	gStyle->SetLineStyleString(11,"14 12");
           
	double dataLumi = 1000;//4965.876/pb. -20/pb in ele
	double SF=1; // scale factor - missing part lepton id

	// define files
	TFile* TTJets_file    = new TFile("TTJets.root", "READ");
	//TFile* SingleTop_file = new TFile("SingleTop.root",    "READ");
	TFile* WJets_file     = new TFile("WJets.root",         "READ");
	TFile* ZJets_file     = new TFile("ZJets.root",         "READ");
	TFile* QCD_file       = new TFile("QCD.root",           "READ");
	
	TFile* A1_file       = new TFile("A1.root",             "READ");
	TFile* B1_file       = new TFile("B1.root",             "READ");
	TFile* C1_file       = new TFile("C1.root",             "READ");

	TFile* Dummy_file    = new TFile("Dummy.root",          "READ");

// 	//addMCHistogram(TString name, int xmin, int xmax)
// 	addMCHistogram("analyzeBino_45Jets_1/HT",         "H_{T} [GeV]",         "Events / 50 GeV", 500,  5000, 1, 1e6, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeBino_45Jets_1/MET",        "#slash{E}_{T} [GeV]", "Events / 50 GeV", 100,  2000, 1, 1e6, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeBino_45Jets_1/MHT",        "#slash{H}_{T} [GeV]", "Events / 50 GeV",   0,  2000, 1, 1e6, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeBino_45Jets_1/nJets",      "Number of jets",      "Events",         -0.5,    15, 1, 1e6, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeBino_45Jets_2/nJets",      "Number of jets",      "Events",         -0.5,    15, 1, 1e6, -0.1, 2.1, 1);	
// 	addMCHistogram("analyzeBino_45Jets_2/nVetoLeptons", "Number of veto leptons",  "Events",   -0.5,     5, 1, 1e6, -0.1, 2.1, 1);	
// 	addMCHistogram("analyzeBino_45Jets_3/nVetoLeptons", "Number of veto leptons",  "Events",   -0.5,     5, 1, 1e6, -0.1, 2.1, 1);
// // 	addMCHistogram("analyzeBino_45Jets_1/nMuons",     "Number of muons",     "Events",         -0.5,     5, 1, 1e6, -0.1, 2.1, 1);
// // 	addMCHistogram("analyzeBino_45Jets_1/nElectrons", "Number of electrons", "Events",         -0.5,     5, 1, 1e6, -0.1, 2.1, 1);
// //  	addMCHistogram("analyzeBino_45Jets_1/nLeptons",   "Number of leptons",   "Events",         -0.5,     5, 1, 1e6, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeBino_45Jets_3/DeltaPhi_MET_Jet0",  "#Delta#Phi (jet^{1}, #slash{H}_{T})",   "Events",  -3,  3, 1, 1e5, -0.1, 2.1, 0);
// 	addMCHistogram("analyzeBino_45Jets_4/DeltaPhi_MET_Jet0",  "#Delta#Phi (jet^{1}, #slash{H}_{T})",   "Events",  -3,  3, 1, 1e5, -0.1, 2.1, 0);
// 	addMCHistogram("analyzeBino_45Jets_4/DeltaPhi_MET_Jet1",  "#Delta#Phi (jet^{2}, #slash{H}_{T})",   "Events",  -3,  3, 1, 1e5, -0.1, 2.1, 0);
// 	addMCHistogram("analyzeBino_45Jets_5/DeltaPhi_MET_Jet1",  "#Delta#Phi (jet^{2}, #slash{H}_{T})",   "Events",  -3,  3, 1, 1e4, -0.1, 2.1, 0);
// 	addMCHistogram("analyzeBino_45Jets_5/DeltaPhi_MET_Jet2",  "#Delta#Phi (jet^{3}, #slash{H}_{T})",   "Events",  -3,  3, 1, 1e4, -0.1, 2.1, 0);
// 	addMCHistogram("analyzeBino_45Jets_6/DeltaPhi_MET_Jet2",  "#Delta#Phi (jet^{3}, #slash{H}_{T})",   "Events",  -3,  3, 1, 1e4, -0.1, 2.1, 0);
// 	addMCHistogram("analyzeBino_45Jets_6/YMET",  "Y_{MET} [GeV^{1/2}]", "Events", 0,    50, 1, 1e4, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeBino_45Jets_7/YMET",  "Y_{MET} [GeV^{1/2}]", "Events", 0,    50, 1, 1e4, -0.1, 2.1, 1);
// 	//addMCHistogram("analyzeBino_45Jets_8/YMET",  "Y_{MET} [GeV^{1/2}]", "Events", 0,    50, 1, 1e4, -0.1, 2.1, 1);

// 	addMCHistogram("analyzeBino_45Jets_6/HT",  "H_{T} [GeV]",         "Events / 50 GeV", 500,  5000, 1, 1e5, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeBino_45Jets_6/MET", "#slash{E}_{T} [GeV]", "Events / 50 GeV", 100,  2000, 1, 1e5, -0.1, 2.1, 1);
	addMCHistogram("analyzeBino_56Jets_8/minj3", "minj3", "Events / 50 GeV", 0, 2000, 0.5, 1000, -0.1, 2.1, 1);

// 	addMCHistogram("analyzeWino_1/nLeptons", "Number of leptons",   "Events",          -0.5,   15, 1, 1e5, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeWino_2/nJets",    "Number of jets",      "Events",           3.5,   15, 1, 1e5, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeWino_3/HT",       "H_{T} [GeV]",         "Events / 50 GeV",  500, 5000, 1, 1e3, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeWino_3/MET",      "#slash{E}_{T}[GeV]",  "Events / 50 GeV",  100, 5000, 1, 1e3, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeWino_3/YMET",     "Y_{MET} [GeV^{1/2}]", "Events",             0,   50, 1, 1e3, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeWino_3/mT",       "m_{T} [GeV]",         "Events / 10 GeV",    0,  600, 1, 1e3, -0.1, 2.1, 1);

// 	addMCHistogram("analyzeWino_4/HT",       "H_{T} [GeV]",         "Events / 50 GeV",  500, 5000, 1, 1e3, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeWino_4/MET",      "#slash{E}_{T}[GeV]",  "Events / 50 GeV",  100, 5000, 1, 1e3, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeWino_4/YMET",     "Y_{MET} [GeV^{1/2}]", "Events",             0,   50, 1, 1e3, -0.1, 2.1, 1);

// 	addMCHistogram("analyzeSignal_1/HT",  "H_{T} [GeV]",         "Events / 50 GeV", 0,  4000, 1, 1e7, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeSignal_1/MET", "#slash{E}_{T} [GeV]", "Events / 50 GeV", 0,  4000, 1, 1e7, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeWino_1/HT",  "H_{T} [GeV]",         "Events / 50 GeV", 0,  4000, 1, 1e7, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeWino_1/MET", "#slash{E}_{T} [GeV]", "Events / 50 GeV", 0,  4000, 1, 1e7, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeWino_2/HT",  "H_{T} [GeV]", "Events / 50 GeV", 0,  4000, 1, 1e6, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeWino_2/MET",  "#slash{E}_{T} [GeV]","Events / 50 GeV", 0,  4000, 1, 1e6, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeWino_2/nJets", "Number of jets","Events", -0.5,  15, 1, 1e6, -0.1, 2.1, 1);

// 	addMCHistogram("analyzeWino_4/min234", "min234", "Events / 50 GeV", 0, 1000, 0, 450, -0.1, 2.1, 1);

	for(int hdx=0; hdx<(int)Histograms.size(); ++hdx)
	  {
	    std::cout << Histograms[hdx] << std::endl;

	    // get histograms
	    TH1D* QCD       = (TH1D*)QCD_file       ->Get(Histograms[hdx]);
	    TH1D* TTJets    = (TH1D*)TTJets_file    ->Get(Histograms[hdx]);
	    //TH1D* SingleTop = (TH1D*)SingleTop_file ->Get(Histograms[hdx]);
	    TH1D* WJets     = (TH1D*)WJets_file     ->Get(Histograms[hdx]);
	    TH1D* ZJets     = (TH1D*)ZJets_file     ->Get(Histograms[hdx]);
	    
	    TH1D* A1        = (TH1D*)A1_file        ->Get(Histograms[hdx]);
	    TH1D* B1        = (TH1D*)B1_file        ->Get(Histograms[hdx]);
	    TH1D* C1        = (TH1D*)C1_file        ->Get(Histograms[hdx]);

	    TH1D* Dummy     = (TH1D*)Dummy_file     ->Get(Histograms[hdx]);
	    
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
	    	 
	    sr.AddData(Dummy);

	    // MC histogram, color,    nevnts, x-sect
	    sr.Add(ZJets,     kBlue-7,   1, 0.001);
	    //sr.Add(SingleTop, kGreen-3,  1, 0.001);
	    sr.Add(WJets,     kYellow-4, 1, 0.001);
	    sr.Add(TTJets,    kRed-4,    1, 0.001);
	    sr.Add(QCD,       kRed+2,    1, 0.001);

	    // add a few signal points
	    // extra lines in stack: histo, color, nevnts, x-sect, style (line width)
	    sr.AddExtra(A1,  kBlue,  1,   0.001,   1,  3); 
	    sr.AddExtra(B1,  kBlack, 1,   0.001,   2,  3);
	    sr.AddExtra(C1,  kRed+3, 1,   0.001,   1,  3);

	    TCanvas* c1 = new TCanvas(Histograms[hdx],Histograms[hdx],600,700);
	    sr.DrawClone();
	    
	    sr.pad1->cd(); // stack
	    
	    TLegend *leg = new TLegend(0.68, 0.48, 0.9499, 0.9);
	    leg->SetTextSize(0.05);
	    leg->SetFillColor(0);
	    leg->AddEntry(TTJets,    "t#bar{t} + Jets",   "f");
	    leg->AddEntry(WJets,     "W + Jets",          "f");
	    //leg->AddEntry(SingleTop, "Single Top",       "f");
	    leg->AddEntry(ZJets,     "Z/#gamma* + Jets",  "f");
	    leg->AddEntry(QCD,       "QCD",               "f");
	    leg->AddEntry(A1,        "scenario A",        "lp");
	    leg->AddEntry(B1,        "scenario B",        "lp");
	    leg->AddEntry(C1,        "scenario C",        "lp");
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
