// systematic error from PAS Tab.5 SM MC 1b-tag
// N_D = 195.6 ± 7.2 ± 53.0 53/195.6=0.27
//
// MC SF 0.97 for lepton ID

#include "StackWithRatio.h"
#include "tdrStyle.h"

vector<TString> MuHistograms;
vector<TString> ElHistograms;
vector<TString> Prefix;
vector<TString> Names;
vector<TString> XTitles;
vector<TString> YTitles;
vector<double> Xmin;
vector<double> Xmax;
vector<double> Ymin;
vector<double> Ymax;
vector<double> Smin;
vector<double> Smax;
vector<int> Legend;

void addMCHistogram(TString prefix, TString name, TString XTitle, TString YTitle, double xmin, double xmax, double ymin, double ymax, double smin, double smax, int legend)
{
  Prefix.push_back(prefix);
  Names.push_back(name);
  MuHistograms.push_back(prefix+"1m_"+name);
  ElHistograms.push_back(prefix+"1e_"+name);
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

class ElMuAdder {
public:

	TString path; // directory name for files
	TString mName;// root dir/histo for muons
	TString eName;// root dir/histo for electrons

	ElMuAdder(const char* pth="./") : path(pth) {};

	// 2 file arguments -> add e+m from different files e.g. data
	// this is considered to be data not added to sum histo
	TH1D* get(const TString& eFile, const TString& mFile){
		TFile mfile(path+mFile);
		TFile efile(path+eFile);
		TH1D* mH = (TH1D*)mfile.Get(mName);
		TH1D* eH = (TH1D*)efile.Get(eName);
		gROOT->cd();
		TH1D*  H = mH->Clone();
		H->Add(eH);
		return H;
	}

	// 1 file argument -> add e+m from same files e.g. mc
	// this is considered to be MC -> added to sum histo
	TH1D* get(const TString& File){ //
		TFile file(path+File);
		TH1D* mH = (TH1D*)file.Get(mName);
		TH1D* eH = (TH1D*)file.Get(eName);
		gROOT->cd();
		TH1D*  H = mH->Clone();// Sumw2() is copied as well
		H->Add(eH);
		return H;
	}
  
};

//-------------------- main --------------------
void EventSelectionAll(){

	setTDRStyle();
	gStyle->SetPadTopMargin(0.1);
                       
	double dataLumi = 4980;//4965.876/pb. -20/pb in ele
	double SF=0.97; // scale factor - missing part lepton id

	ElMuAdder ad("./"); // path to root files

	//add MC histogram
// 	addMCHistogram("analyzeSUSY2b", "1/nPV",       "Number of primaty vertices", "Events", 0,  50, 0.1, 1e4, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeSUSY2b", "1/nPV_noWgt", "Number of primaty vertices", "Events", 0,  50, 0.1, 1e4, -0.1, 2.1, 1);

// 	addMCHistogram("analyzeSUSY", "jetSelection/TCHE", "B-discriminator", "Events", -20,  20, 0.1, 1e5, -0.1, 2.1, 0);

// 	addMCHistogram("analyzeSUSY", "jetSelection/Jet0_Et", "p_{T}^{jet1}","Events", 0,  900, 0.1, 1e4, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeSUSY", "jetSelection/Jet1_Et", "p_{T}^{jet2}","Events", 0,  900, 0.1, 1e4, -0.1, 2.1, 0);
// 	addMCHistogram("analyzeSUSY", "jetSelection/Jet2_Et", "p_{T}^{jet3}","Events", 0,  450, 0.1, 1e4, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeSUSY", "jetSelection/Jet3_Et", "p_{T}^{jet4}","Events", 0,  450, 0.1, 1e4, -0.1, 2.1, 0);

// 	addMCHistogram("analyzeSUSY",   "jetSelection/mT", "m_{T} [GeV]","Events / 10 GeV", 0,  400, 0.1, 1e4, -0.1, 2.1, 1);	
// 	addMCHistogram("analyzeSUSY1b", "1/mT", "m_{T} [GeV]","Events", 0,  400, 0.1, 5e3, -0.1, 2.1, 1);	
// 	addMCHistogram("analyzeSUSY3b", "1/mT", "m_{T} [GeV]","Events", 0,  400, 0.1, 5e3, -0.1, 2.1, 0);

//  	addMCHistogram("analyzeSUSY",   "jetSelection/YMET", "Y_{MET}","Events", 0,  200, 0.1, 1e4, -0.1, 2.1, 1);
//  	addMCHistogram("analyzeSUSY1b", "1/YMET",            "Y_{MET}","Events", 0,  200, 0.1, 1e4, -0.1, 2.1, 1);
//  	addMCHistogram("analyzeSUSY3b", "1/YMET",            "Y_{MET}","Events", 0,  200, 0.1, 1e3, -0.1, 2.1, 0);

//  	addMCHistogram("analyzeSUSY",   "jetSelection/nBjets_2", "Number of b-jets","Events", -0.5,  5.5, 0.1, 1e5, -0.1, 2.1, 1);

// 	addMCHistogram("analyzeSUSY",   "leptonSelection/nJets", "Number of jets","Events", -0.5,  13.5, 0.1, 1e5, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeSUSY",   "jetSelection/nJets",    "Number of jets","Events",  3.5,  13.5, 0.1, 1e5, -0.1, 2.1, 1);
	addMCHistogram("analyzeSUSY1b", "1/nJets",               "Number of jets","Events",  3.5,  13.5, 0.1, 1e4, -0.1, 2.1, 1);
	addMCHistogram("analyzeSUSY3b", "1/nJets",               "Number of jets","Events",  3.5,  13.5, 0.1, 1e4, -0.1, 2.1, 1);

// 	addMCHistogram("analyzeSUSY",   "jetSelection/HT",    "H_{T} [GeV]","Events / 50 GeV", 0,  2000, 0.1, 1e5, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeSUSY1b", "1/HT", "H_{T} [GeV]","Events",  0, 2000, 0.1, 1e4, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeSUSY3b", "1/HT", "H_{T} [GeV]","Events",  0, 2000, 0.1, 1e3, -0.1, 2.1, 0);

//   	addMCHistogram("analyzeSUSY",   "jetSelection/MET",    "#slash{E}_{T} [GeV]","Events / 25 GeV", 0,  800, 0.1, 1e4, -0.1, 2.1, 1);
//   	addMCHistogram("analyzeSUSY",   "jetSelection/MHT",    "#slash{H}_{T} [GeV]","Events / 25 GeV", 0,  800, 0.1, 1e4, -0.1, 2.1, 1);
// 	addMCHistogram("analyzeSUSY1b", "1/MET", "#slash{E}_{T} [GeV]","Events",  0, 800, 0.1, 1e4, -0.1, 2.1, 1);
//  	addMCHistogram("analyzeSUSY3b", "1/MET", "#slash{E}_{T} [GeV]","Events",  0, 800, 0.1, 1e3, -0.1, 2.1, 0);

	for(int hdx=0; hdx<(int)MuHistograms.size(); ++hdx)
	  {
	    // electron and muon data
	    ad.mName   = MuHistograms[hdx]; // muon histogram
	    ad.eName   = ElHistograms[hdx]; // electron histogram
	    TH1D* data =  ad.get("ElHad.root","MuHad.root");
	
	    // SM MC
	    ad.mName   =  MuHistograms[hdx]; // muon histogram
	    ad.eName   =  ElHistograms[hdx]; // electron histogram
	    TH1D* QCD       =  ad.get("QCD.root");
	    TH1D* ZJets     =  ad.get("ZJets.root");
	    TH1D* WJets     =  ad.get("WJetsHT.root");
	    TH1D* SingleTop =  ad.get("SingleTop.root");
	    TH1D* TTJets    =  ad.get("TTJetsFall11.root");
	    // LM signal points
	    TH1D* LM8       =  ad.get("LM8.root");
	    TH1D* LM6       =  ad.get("LM6.root");
	    
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
	    
	    sr.AddData(data);

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

	    TCanvas* c1 = new TCanvas(MuHistograms[hdx],MuHistograms[hdx],600,700);
	    sr.DrawClone();
	    
	    sr.pad1->cd(); // stack
	    
	    TLegend *leg = new TLegend(0.68, 0.45, 0.9499, 0.9);
	    leg->SetTextSize(0.05);
	    leg->SetFillColor(0);
 	    leg->AddEntry(data,      "Data",             "lep");
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

// 	    TLatex *t1 = new TLatex(0,1.8*Ymax[hdx],"L = 4.98 fb^{-1}, #sqrt{s} = 7 TeV");
// 	    t1->SetTextSize(0.05);
// 	    t1->Draw();

	    TString NAME = Prefix[hdx]+"1l_"+Names[hdx]+".pdf";
	    NAME.ReplaceAll("/", "_");
	    c1->SaveAs(NAME);
	  }
	
}
