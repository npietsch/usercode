#include <TH1.h>
#include <TH2.h>
#include <TGraph.h>
#include <TCanvas.h>
#include <TMath.h>
#include <string>
#include <fstream>

double min(double a, double b){ if(a > b){ return b; }else{ return a; } }
double max(double a, double b){ if(a > b){ return a; }else{ return b; } }

void many_fits_mean(){
  gROOT->SetBatch(kTRUE);

  using namespace std;


  Int_t iFont=42;
  gROOT->SetStyle("Plain");
  gStyle->SetOptStat("neMR");
  gStyle->SetTextFont(iFont);
  gStyle->SetFrameLineWidth(1);
  gStyle->SetHistLineWidth(2);
  gStyle->SetTitleXOffset (1.15);
  gStyle->SetTitleYOffset (0.01);
  gStyle->SetLabelSize(0.04,"XY");
  gStyle->SetLabelSize(0.035,"Z");
  gStyle->SetLabelOffset(0.01,"XY");
  gStyle->SetLabelOffset(0.004,"Z");
  gStyle->SetTitleSize(0.04,"XYZ");
  gStyle->SetTitleOffset(1.1,"XYZ");
  gStyle->SetTitleBorderSize(0);
  gStyle->SetTitleX(0.1);
  gStyle->SetTitleY(0.98);
  gStyle->SetStatX(0.87);
  gStyle->SetStatY(0.85);
  gStyle->SetStatFontSize(0.03);


  char* outfile;
  char* infile;
  char* psout_sta;
  char* psout;
  char* psout_end;

  //====================================================================
  // Here, you set the input root file in which there is the histogram 
  // you want to fit.
  //====================================================================
  
  //infile="plots_C_45j.root";
  infile="Ruediger.root";
  outfile="pros_H.root";   
  TFile file1(infile);
  TFile* file2 = new TFile(outfile,"RECREATE");  

  //====================================================================
  // Here, you set the name of the histogram you want to fit.
  //====================================================================
  //  TH1F *his = (TH1F*)file1.Get("his74_1"); // m234
  //  TH1F *his = (TH1F*)file1.Get("his91_1"); // m3j
      TH1F *his = (TH1F*)file1.Get("analyzeBino545/min123"); // m123

  gROOT->ForceStyle();
  c1 = new TCanvas("c1", "Title", 600, 400);
  //  c1->SetLogz(); 

  //====================================================================
  // Here, you set the range of the histrogram. (defining the fitting range from peak to point x)
  //====================================================================

  //double hmin = 0; double hmax = 1800; // overall fitting range
  double hmin = 0; double hmax = 1400; // overall fitting range
  int hbin = his->GetNbinsX();
  int width = his->GetBinWidth(1);
  int peak_bin = his->GetMaximumBin();
  int peak_val = his->GetMaximum();
  int last_bin = 0;
  // The higher boundary of the fitting range is given if the
  // y-value of the histogram becomes less than (peak value)/500.
  for(int i=peak_bin; i<hbin; i++){
    double yval = his->GetBinContent(i);
    // -- Kazuki's initial version:
    //    if( yval < peak_val/500. && last_bin == 0){
    //      last_bin = i-1;
    //    }    
    // -- my version:
    if( yval == 0. && last_bin == 0){
      last_bin = i-1;
    }    
  }
  if (last_bin == 0) {
    last_bin = hbin;
    double fmax_max = width * (last_bin);
  }
  else {
    double fmax_max = width * (last_bin+3);
  }
  double fmin_min = width * peak_bin;
  // Tuning variable fbin_min!
  double fbin_min = (0.5)*fabs(fmin_min-fmax_max)/(width);
  if( last_bin - peak_bin < 5 ){
    cout << "ERROR: too small fitting range -> abort" << endl;
    cout << "fbin_min " << fbin_min << endl;
    cout << "fitting range " << fmin_min <<"  "<< fmax_max << endl; 
    cout << "fitting bin range " << peak_bin <<"  "<< last_bin << endl; 
    break;
  }


  // histo for endpoint distributions extracted from nfits
  TH1F *fit_dist = new TH1F("","endpoint distribution",60,fmin_min,fmax_max);  

  //=========================

  // defining values for statistial analysis
  double ep_sum=0;
  double ep_val[2000]={0};
  double ep_err=0;

  // nfits fits are carried out
  int nfits = 1000;
  for(int i=0; i<nfits; i++){

    
    // randomly defined subrange

    double f1 = gRandom->Uniform(fmin_min, fmax_max);
    double f2 = gRandom->Uniform(fmin_min, fmax_max);

    // minimum fitting subrange (original: 5)
    if( fabs(f1-f2) < width * 5){
      i = i - 1;
      continue;
    }

    double fmin = min(f1,f2);
    double fmax = max(f1,f2);

    TF1 *func = new TF1("fitfunc",brokenLine,fmin,fmax,4);
    func->SetParameter(0,50);
    func->SetParameter(1,-0.01);
    func->SetParameter(2,-0.1);
    func->SetParameter(3,(fmax + fmin)/2.);
    func->SetLineColor(2);

    // Do the fit
    his->Fit( "fitfunc", "","", fmin, fmax );
    

    // Extract parameters, where p[3] is kink position in brokenLine function
    Double_t p[4];
    func->GetParameters(p);
    double end_p = p[3];
    cout << "Fit Result" << endl;
    cout << "Absolute Fitting Range = (" << fmin_min <<", "<< fmax_max <<")" 
	 << endl;
    cout << "Fitting Range = (" << fmin <<", "<< fmax <<")" << endl;
    cout << "Endpoint = " << end_p << endl;

    // sanity check
    if( end_p < fmin || end_p > fmax ){
      i = i-1;
      continue;
    }

    
    // fill statistical endpoint histo
    fit_dist->Fill( end_p );    

    // save values for statistical analysis afterwards
    ep_sum += end_p;
    ep_val[i] = end_p;

  }// end nfits loop

  cout << "fbin_min " << fbin_min << endl;
  cout << "fitting range " << fmin_min <<"  "<< fmax_max << endl; 
  cout << "fitting bin range " << peak_bin <<"  "<< last_bin << endl; 
  c1->Print("test.ps(");
  c1->Print("test_1.eps");
  gStyle->SetOptFit();
  fit_dist->GetXaxis()->SetTitle("mean");
  fit_dist->Draw();

  c1->Print("test.ps");
  c1->Print("test_2.eps");


  //--- analysis

  //--- define adapted mean_value

  ep_sum = ep_sum/nfits;
  double ep_tmp_val=0, ep_tmp_err=0;
  double ep_min_h = fit_dist->GetMaximum()/5;
  double ep_mean=0;
  double ep_mean_ed=0;
  double ep_err_ed=0;

  for (int i=0;i<nfits;i++) {
    ep_tmp_val += ep_val[i];
  }
  ep_mean = ep_tmp_val/nfits;
  

  for (int i=0;i<nfits;i++) {
      ep_tmp_err += pow((ep_val[i]-ep_mean),2);
  }  
  ep_err = sqrt (ep_tmp_err/(nfits-1));
  
  //--- now redefine ep_mean with values only inside one standard deviation and iterate
  
  //-- iter < 3:
//  original mean value = 983.577 +/- 120.374
//  adapted mean value = 1008.67 +/- 6.21959
//  endpoint values surviving within one sigma: 449

//--- iter < 5
//  original mean value = 983.577 +/- 120.374
//  adapted mean value = 1009.7 +/- 2.81419
//  endpoint values surviving within one sigma: 191


  ep_mean_ed = ep_mean;
  ep_err_ed = ep_err;
  int iter=0;
  while (iter<20) {
    int n_cnt=0;
    ep_tmp_val = 0;
    for (int i=0;i<nfits;i++) {
      if (fabs(ep_val[i]-ep_mean_ed)<2*ep_err_ed) {
	ep_tmp_val += ep_val[i];
	n_cnt++;
      }
    }
    ep_mean_ed = ep_tmp_val/n_cnt;
    
    ep_tmp_err=0;
    for (int i=0;i<nfits;i++) {
      if (fabs(ep_val[i]-ep_mean_ed)<2*ep_err_ed) {
	ep_tmp_err += pow((ep_val[i]-ep_mean_ed),2);
      }
    }
    ep_err_ed = sqrt( ep_tmp_err/(n_cnt-1) );
    iter++;
    cout << "adapted mean value = "<< ep_mean_ed << " +/- " << ep_err_ed << endl;
  }
    
  cout << "original mean value = "<< ep_mean << " +/- " << ep_err << endl;
  cout << "adapted mean value = "<< ep_mean_ed << " +/- " << ep_err_ed << endl;
  cout << "endpoint values surviving within one sigma: " << n_cnt << endl;
  //--- new plot according to maximum peak value
  
  double mean_range = fabs(fmax_max-fmin_min)/4;
  int mean_peak_bin = fit_dist->GetMaximumBin();
  int mean_width = fit_dist->GetBinWidth(1);
  double mean_peak = fmin_min + mean_peak_bin*mean_width;
  int mean_binsize = mean_range/mean_width;

  //keep binsize ?
  TH1F *mean_dist = new TH1F("","mean endpoint distribution",30,ep_mean-ep_err,ep_mean+ep_err);  
  
  for (int i=0;i<nfits;i++) {
    mean_dist->Fill(ep_val[i]);
  }
  
  mean_dist->Draw();

  c1->Print("test.ps)");

  file2->Write();
  
  //gPad->WaitPrimitive();
  gROOT->ProcessLine(".q");  
}

Double_t brokenLine (Double_t *x, Double_t *par) {
 Double_t func;
 if (x[0] >= par[3]) {
   func = par[0] + par[1]*(x[0] - par[3]);
 }
 else {
   func = par[0] + par[2]*(x[0] - par[3]);
 }
 return func;
}

Double_t brokenExp (Double_t *x, Double_t *par) {
  Double_t func;
  if (x[0] <= par[3]) {
    func = par[0] + par[1]*(x[0] - par[3]);
  }
  else {
    func = exp(-x[0]/par[4] + par[5]);
  }
  return func;
}
