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
void EventSelection(){

	setTDRStyle();
	gStyle->SetPadTopMargin(0.1);
	gStyle->SetLineStyleString(11,"14 12");
           
	double dataLumi = 4980;//4965.876/pb. -20/pb in ele
	double SF=0.97; // scale factor - missing part lepton id

	// define files
	TFile* TTJets_file    = new TFile("TTJetsFall11.root", "READ");
	TFile* SingleTop_file = new TFile("SingleTop.root",    "READ");
	TFile* WJets_file     = new TFile("WJetsHT.root",      "READ");
	TFile* ZJets_file     = new TFile("ZJets.root",        "READ");
	TFile* QCD_file       = new TFile("QCD.root",          "READ");
	
	TFile* LM3_file       = new TFile("LM3.root",          "READ");
	TFile* LM6_file       = new TFile("LM6.root",          "READ");
	TFile* LM8_file       = new TFile("LM8.root",          "READ");
	
	TFile* MuHad_file     = new TFile("MuHad.root",        "READ");
	TFile* ElHad_file     = new TFile("ElHad.root",        "READ");

	//addMCHistogram(TString name, int xmin, int xmax)	
	addMCHistogram("analyzeSUSY1m_leptonSelection/Muon0_Pt",  "p_{T}^{muon}","Events",  0,  300, 0.1, 1e5, -0.1, 2.1, 1);
	addMCHistogram("analyzeSUSY1m_leptonSelection/Muon0_Eta", "#eta^{muon}", "Events", -3,    3, 0.1, 1e4, -0.1, 2.1, 0);
// 	addMCHistogram("analyzeSUSY1m_leptonSelection/nJets", "Number of Jets",  "Events",        -0.5,  13.5, 0.1, 1e5, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeSUSY1m_leptonSelection/nPV", "Number of primary vertices", "Events",  -0.5,  50.5, 0.1, 1e5, -0.1, 2.1, 1);

// 	addMCHistogram("analyzeSUSY1e_leptonSelection/Electron0_Pt",  "p_{T}^{electron}","Events",  0,  300, 0.1, 1e5, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeSUSY1e_leptonSelection/Electron0_Eta", "#eta^{electron}", "Events", -3,    3, 0.1, 1e4, -0.1, 2.1, 0);

//	addMCHistogram("analyzeSUSY1m_jetSelection/HT",    "HT [GeV]","Events / 50 GeV", 0,  2000, 0.1, 1e5, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeSUSY1b1m_1/HT", "H_{T} [GeV]","Events / 50 GeV",  0, 2000, 0.1, 1e3, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeSUSY2b1m_1/HT", "H_{T} [GeV]","Events / 50 GeV",  0, 2000, 0.1, 1e3, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeSUSY3b1m_1/HT", "H_{T} [GeV]","Events / 50 GeV",  0, 2000, 0.1, 1e3, -0.1, 2.1, 1);


// 	addMCHistogram("analyzeRA4Muons/relIso", "rel. Isolation","Events",  0, 2, 1, 1e5, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeRA4Muons/relIso_Nminus1", "rel. Isolation","Events",  0, 2, 0.1, 1e5, -0.1, 2.1, 1);

// 	addMCHistogram("analyzeRA4Muons/pt",     "p_{T}",     "Events / 10 GeV",   0, 300, 1, 1e5, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeRA4Muons/eta",    "#eta",      "Events",           -3,   3, 1, 1e5, -0.1, 2.1, 1);

//  	addMCHistogram("analyzeRA4Muons/globalMuonPromptTight", "globalMuonPromptTight","Events",  0, 2, 1, 1e6, -0.1, 2.1, 1);
//  	addMCHistogram("analyzeRA4Muons/allTrackerMuons","allTrackerMuons","Events",  0, 2, 1,   1e6, -0.1, 2.1, 1);
//  	addMCHistogram("analyzeRA4Muons/dB",             "dB",             "Events",  0, 0.2, 1, 1e6, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeRA4Muons/dz",             "dz",             "Events",  0,   1, 1, 1e6, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeRA4Muons/nMatches",       "nMatches",       "Events",  0,  20, 1, 1e6, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeRA4Muons/normChi2",       "normChi2",       "Events",  0,  10, 1, 1e6, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeRA4Muons/nValidMuonHits", "nValidMuonHits", "Events",  0,  20, 1, 1e6, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeRA4Muons/nTrackerHits",   "nTrackerHits",   "Events",  0,  20, 1, 1e6, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeRA4Muons/nPixelLayersWithMeasurement", "nPixelLayersWithMeasurement", "Events", 0, 10, 1, 1e6, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeRA4Muons/ptError",         "ptError",       "Events",  0, 0.1,   1, 1e6, -0.1, 2.1, 1);
//	addMCHistogram("analyzeRA4Muons/pfConsistency",   "pfConsistency", "Events",  0,   1, 0.1, 1e7, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeSUSY3b1m_1/nJets", "Number of Jets","Events", 0,  12, 0.1, 1e3, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeSUSY1m_leptonSelection/nJets", "Number of Jets","Events", 0,  12, 0.1, 1e5, -0.1, 2.1, 1);

	for(int hdx=0; hdx<(int)Histograms.size(); ++hdx)
	  {
	    // get histograms
	    TH1D* TTJets    = (TH1D*)TTJets_file    ->Get(Histograms[hdx]);
	    TH1D* SingleTop = (TH1D*)SingleTop_file ->Get(Histograms[hdx]);
	    TH1D* WJets     = (TH1D*)WJets_file     ->Get(Histograms[hdx]);
	    TH1D* ZJets     = (TH1D*)ZJets_file     ->Get(Histograms[hdx]);
	    TH1D* QCD       = (TH1D*)QCD_file       ->Get(Histograms[hdx]);
	    
	    TH1D* LM3       = (TH1D*)LM3_file       ->Get(Histograms[hdx]);
	    TH1D* LM6       = (TH1D*)LM6_file       ->Get(Histograms[hdx]);
	    TH1D* LM8       = (TH1D*)LM8_file       ->Get(Histograms[hdx]);
	    
	    TH1D* MuHad     = (TH1D*)MuHad_file     ->Get(Histograms[hdx]);
	    TH1D* ElHad     = (TH1D*)ElHad_file     ->Get(Histograms[hdx]);
	    
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
	    
	    sr.AddData(MuHad);

	    // MC histogram, color,    nevnts, x-sect

	    sr.Add(QCD,       kRed+2,    1, 0.001);
	    sr.Add(ZJets,     kBlue-7,   1, 0.001);
	    sr.Add(SingleTop, kGreen-3,  1, 0.001);
	    sr.Add(WJets,     kYellow-4, 1, 0.001);
	    sr.Add(TTJets,    kRed-4,    1, 0.001);

	    // add a few signal points
	    // extra lines in stack: histo, color, nevnts, x-sect, style (line width)
	    sr.AddExtra(LM8,  kBlue,   421190,   0.73*1.41,   1,  2); 
	    sr.AddExtra(LM6,  kBlack,  427625,   0.404,       2,  3);

	    TCanvas* c1 = new TCanvas(Histograms[hdx],Histograms[hdx],600,700);
	    sr.DrawClone();
	    
	    sr.pad1->cd(); // stack
	    
	    TLegend *leg = new TLegend(0.68, 0.48, 0.9499, 0.9);
	    leg->SetTextSize(0.05);
	    leg->SetFillColor(0);
	    leg->AddEntry(MuHad,     "Data",             "lep");
	    leg->AddEntry(TTJets,    "t#bar{t} + Jets",  "f");
	    leg->AddEntry(WJets,     "W + Jets",         "f");
	    leg->AddEntry(SingleTop, "Single Top",       "f");
	    leg->AddEntry(ZJets,     "Z/#gamma* + Jets", "f");
	    leg->AddEntry(QCD,       "QCD",              "f");
	    leg->AddEntry(LM8,       "LM8",              "lp");
	    leg->AddEntry(LM6,       "LM6",              "lp");
	    leg->SetBorderSize(1);
	    if(Legend[hdx] == 1) leg->Draw();
	    	    
	    TPaveText *label = new TPaveText(0.06,0.94,0.99,1.,"NDC");
	    label->SetFillColor(0);
	    label->SetTextFont(62);
	    label->SetTextSize(0.05);
	    label->SetBorderSize(0);
	    label->SetTextAlign(12);
	    TText *text=label->AddText("4.98 fb^{-1}, #sqrt{s} = 7 TeV");
	    label->Draw();

// 	    TLatex *t1 = new TLatex(0,1.8e5,"L = 4.98 fb^{-1}, #sqrt{s} = 7 TeV");
// 	    t1->SetTextSize(0.05);
// 	    t1->Draw();

	    TString NAME = Histograms[hdx]+".pdf";
	    NAME.ReplaceAll("/", "_");
	    c1->SaveAs(NAME);
	  }
}
