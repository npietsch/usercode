#include "StackMC.h"
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
  //	this is considered to be MC -> added to sum histo
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
void LM_2(){

	setTDRStyle();
	gStyle->SetPadTopMargin(0.1);
	gStyle->SetPadLeftMargin(0.14);
	gStyle->SetPadBottomMargin(0.13);
	gStyle->SetPadRightMargin(0.05);

	gStyle->SetLineStyleString(11,"14 12");
   
	double dataLumi = 4980;//4965.876/pb. -20/pb in ele
	double SF=1; // scale factor - missing part lepton id
	//double nEvt=421190;
	//double Xsec=1.0293;
	double nEvt=427625;
	double Xsec=0.404;
	//double nEvt=437030;
	//double Xsec=10.82472;

	ElMuAdder ad("./"); // path to root files


	addMCHistogram("analyzeSUSYGenEvent",   "leptonSelection/nrJets", "Number of jets","Events", -0.5,  13.5, 0, 95, -0.1, 2.1, 1);

	//addMCHistogram("analyzeSUSY3b1m_1/nJets", "Number of jets", "Events", 0, 14, 0.1, 20, -0.1, 2.1, 1);
	for(int hdx=0; hdx<(int)MuHistograms.size(); ++hdx)
	  {
	    std::cout << MuHistograms[hdx] << std::endl;
	    std::cout << ElHistograms[hdx] << std::endl;

	    ad.mName   =  MuHistograms[hdx]; // muon histogram	    
	    ad.eName   =  ElHistograms[hdx]; // electron histogram
	    
 	    // get histograms
	    TH1D* All          = ad.get("LM6_new.root");
	    TH1D* GluinoPair   = ad.get("LM6_GluinoPair_new.root");
	    TH1D* GluinoSquark = ad.get("LM6_GluinoSquark_new.root");
	    TH1D* SquarkPair   = ad.get("LM6_SquarkPair_new.root");
	    TH1D* StopSbottom  = ad.get("LM6_StopSbottom_new.root");
	    TH1D* Other        = ad.get("LM6_Other_new.root");

	    TH1D* Dummy        = ad.get("Dummy.root");

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

	    TCanvas* c1 = new TCanvas(Prefix[hdx]+"1l_"+Names[hdx],Prefix[hdx]+"1l_"+Names[hdx],600,600);
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
	    	    
	    TPaveText *label = new TPaveText(0.09,0.91,0.99,1.,"NDC");
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

	    TString NAME = Prefix[hdx]+"1l_"+Names[hdx]+".pdf";
	    NAME.ReplaceAll("/", "_");
	    c1->SaveAs(NAME);
	  }
}
