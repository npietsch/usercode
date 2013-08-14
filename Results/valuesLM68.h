#ifndef _values_
#define _values_
// ---- globals

// lower bin edges
double HT0 = 375;
double Y0  = 3.25;

// lumi el and mu
double lumiE=4980;
double lumiM=4980;
double sL = 0.022; // rel sys. uncert. lumi

// efficiencies
double lepIDtrigEff = 0.97; // lepton ID and trigger SF
double sLID = 0.03;         // rel sys. uncert. " 

double SFE=lepIDtrigEff;
double SFM=lepIDtrigEff;

// rel sys model uncertainty: 
// pdf and normalized differential x-sec: (TOP-11-013) 10%+3.5%+0.5%+0.5% = ePdx = 0.106
// + 10/165 on total cross arXiv:0909.0037v1
// MCFM
double sMod = 0.16;

// sys. uncert. 0B comparison
double s0B = 0.1;

// size of data histo
int      n_x=80;
int      n_y=80;
double min_x=0;
double min_y=0;
double max_x=2000;
double max_y=20;

// x-section variation by 50%
//               0b,1b,2b,3b+,1b+,0b+
double xVar[]  = {0.03425,0.01042,0.01958,0.01370,0.00428,0}; // to be recreated !! 0b+ is dummy

// ----- MC x-section and event numbers

// QCD and SingleTop are normalized to 1000/pb for Niklas, Altan old files 2000
// TTJets WJets corrected for lost events, MC bugs...
// TTJets/ZJet/ZJets becomes larger , SingleTop/QCD smaller
int nMCLo=7;
char* MCNamesLo[] =  { "TTJetsSummer11", 
                            "SingleTop",
                                  "QCD",  
                                "ZJets",         
                                "WJets",         
                                  "LM6", 
                                  "LM8"};
long  MCEvntsLo[] =  {    3701947-70495, 
                                   1000, 
                                   1000, 
                        36277961-219947, 
                        81352581-292219, 
                                 427625,
                                 421190 };
//                                  10700 };
// high stat ttbar,wjets(probably only 50% processed !!! normalized such that WJets = WJetsHT)
// A from tw_fromNiklas_14_6_Lo_HT650_Y5.5/em0+.txt / A from tw_fromNiklas_14_6_Hi_HT650_Y5.5/em0+.txt
// Xsec wrong for HT300
int nMCHi=7;
char* MCNamesHi[] =  {   "TTJetsFall11",   
                            "SingleTop", 
                                  "QCD",  
                                "ZJets",
                           "WJetsHT300",
                                  "LM6",
                                  "LM8" };
// wrong event number(3415000) in processing 5327746 is correct in WJetsHT300
long   MCEvntsHi[] =  {        59517528,  // this is used in ABCD
                                   1000,        
                                   1000,   
                        36277961-219947, 
                               42280725,
                                 427625,
                                 421190 };
//                                  10700 }; //LM8_low
// low stat ttbar,wjets
double      XSs[] =  {             157.5, // this used in ABCD
                                     1.,
                                     1.,
                                  3048.,           
                                 31314.,           
                                     0.3104*1.3,  
                                     0.73*1.41 };

double weightsLo[] = {157.5/(3701947-70495),
                                    1./1000,
                                    1./1000,
                    3048./(36277961-219947),
                   31314./(81352581-292219),
                                0.3104/427625,
                                 0.73/10700 };
double weightsHi[] = {157.5/59517528,   // this is used in ABCDsys
                             1./1000,
                             1./1000,
             3048./(36277961-219947),
                     31314./1581767162 ,// adapted to lo
                         0.3104*1.30/427625,
                          0.73*1.41/10700 };
#endif
