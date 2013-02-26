// systematic error from PAS Tab.5 SM MC 1b-tag
// N_D = 195.6 ± 7.2 ± 53.0 53/195.6=0.27
//
// MC SF 0.97 for lepton ID

#include "StackWithRatio.h"
#include "valuesLM68.h"
#include "tdrStyle.h"

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
void HT_LM68(){

	setTDRStyle();
	gStyle->SetPadTopMargin(0.1);
                       
	double dataLumi = 4980;//4965.876/pb. -20/pb in ele
	double SF=0.97; // scale factor - missing part lepton id

	ElMuAdder ad("..//"); // path to root files

	// electron and muon data
	//ad.mName   = "analyzeSUSY1m_HTSelection/HT"; // muon histogram
	//ad.eName   = "analyzeSUSY1e_HTSelection/HT"; // electron histogram
	//ad.mName   = "analyzeRA4Muons/relIso"; // muon histogram
	ad.mName   = "analyzeSUSY1m_leptonSelection/nJets"; // muon histogram
	ad.eName   = "analyzeSUSY1e_leptonSelection/nJets"; // electron histogram
	//ad.mName   = "analyzeSUSY1m_jetSelection/nBjets_2"; // muon histogram
	//ad.eName   = "analyzeSUSY1e_jetSelection/nBjets_2"; // electron histogram
	TH1D* data      =  ad.get("ElHad.root","MuHad.root");

	// SM MC
	//ad.mName   = "analyzeSUSY1b1m_1/HT"; // muon histogram
	//ad.eName   = "analyzeSUSY1e_HTSelection/HT"; // electron histogram
	//ad.mName   = "analyzeRA4Muons/relIso"; // muon histogram
	ad.mName   = "analyzeSUSY1m_leptonSelection/nJets"; // muon histogram
	ad.eName   = "analyzeSUSY1e_leptonSelection/nJets"; // electron histogram
	//ad.mName   = "analyzeSUSY1m_jetSelection/nBjets_2"; // muon histogram
	//ad.eName   = "analyzeSUSY1e_jetSelection/nBjets_2"; // electron histogram
	TH1D* QCD       =  ad.get("QCD.root");
	TH1D* ZJets     =  ad.get("ZJets.root");
	TH1D* WJets     =  ad.get("WJetsHT.root");
	TH1D* SingleTop =  ad.get("SingleTop.root");
	TH1D* TTJets    =  ad.get("TTJetsFall11.root");
	// LM signal points
	TH1D* LM3       =  ad.get("LM3.root");
	TH1D* LM8       =  ad.get("LM8.root");

	//LM3->Smooth(5);


	StackWithRatio sr(dataLumi,"H_{T} [GeV]","Events / 50 GeV","Data/Simulation"); // L and x-axis label
	sr.SetXRange(0,2000);
	sr.SetStackYRange(0.1,1e5);
	sr.SetRatioYRange(-0.1,2.1);

	sr.band   = false; // draw an error band
	sr.relsys = 0.27; // relative systematic uncertainty

	sr.rebOff =  0;  // rebinning offset = number of empty bin at the low edge
        sr.rebN   =  1;  // # bins to merge

	sr.SF     = SF;  // scale factor data MC which is not yet included in rootfiles

	sr.AddData(data);

	// MC histogram, color,    nevnts, x-sect
	
	sr.Add(QCD,       kRed+2,   1, 0.001);
	sr.Add(ZJets,     kBlue-7,   1, 0.001);
	sr.Add(SingleTop, kGreen-3,  1, 0.001);
	sr.Add(WJets,     kYellow-4,   1, 0.001);
	sr.Add(TTJets,    kRed-4,    1, 0.001);

//	LM8->Smooth(2);
	LM8->GetXaxis()->SetRangeUser(375, 2000);
	                                                                        
	// add a few signal points
	// extra lines in stack: histo, color, nevnts, x-sect, style (line width)
//	sr.AddExtra(LM6,  kCyan+1, 427625, 0.3104*1.30,1); // old color 6
//	sr.AddExtra(LM8,  kBlue  , 421190,   0.73*1.41,2); // old color 8
	sr.AddExtra(LM3,  kBlack,  440000,   3.438*1.4,   1, 2); // old color 8
	sr.AddExtra(LM8,  kBlack,  421190,   0.73*1.41,   2, 3); // old color 8
	//sr.AddExtra(LM6,  kBlack,  427625,   0.3104*1.30, 1, 3); // old color 6
	TCanvas* c1 = new TCanvas("c1","",600,700);
	sr.DrawClone();

	sr.pad1->cd(); // stack

	TLegend *leg = new TLegend(0.65, 0.5, 0.9499, 0.9);
	leg->SetTextSize(0.05);
	leg->SetFillColor(0);
	leg->AddEntry(data,      "Data",             "lep");
	leg->AddEntry(TTJets,    "t#bar{t} + Jets",  "f");
	leg->AddEntry(WJets,     "W + Jets",         "f");
	leg->AddEntry(SingleTop, "Single Top",       "f");
	leg->AddEntry(ZJets,     "Z/#gamma* + Jets", "f");
	leg->AddEntry(QCD,       "QCD",              "f");
	leg->AddEntry(LM3,       "LM3",              "lp");
	leg->AddEntry(LM8,       "LM8",              "lp");
	leg->SetBorderSize(1);
	leg->Draw();

	TLatex *t1 = new TLatex(0,1.8e5,"CMS, 4.98 fb^{-1}, #sqrt{s} = 7 TeV");
	t1->SetTextSize(0.05);
	t1->Draw();

	//c1->SaveAs("HT_LM68.gif");
	c1->SaveAs("test.pdf");

}
