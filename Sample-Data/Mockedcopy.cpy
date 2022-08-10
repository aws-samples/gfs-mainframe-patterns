      *****************************************************************         
      *                                                                         
      *     ACCOUNT BALANCE        - STANDARD TRANSMISSION FILE                 
      *                                                                         
      *        LRECL    = 1500                                                  
      *        FILENAME = FBSIT.FBDC400.ACCTBAL.FILE01-12                       
      *                                                                         
      *===============================================================*         
      *                          @REVISIONS@                          *         
      *---------------------------------------------------------------*         
      * MM/DD/YY   PROGRAMMER NAME                                              
      * --------   ---------------                                              
      * XX/XX/12   THOMAS VARGHESE   CM120280957                                
      *            INITIAL INSTALLATION                                         
JL0001* 12/04/15   JOHANNA LEWIS     CM151490384                                
JL0001*            ADD 2 FIELDS                                                 
      *****************************************************************         
                                                                                
       01  TX22N-BALANCE-RCD.                                                   
           05  TX22N-ACCOUNT-NUMBER             PIC X(09).                      
           05  TX22N-LAST-UPDATE-DATE           PIC 9(06).                      
           05  TX22N-NETWORTH-SGN               PIC X.                          
           05  TX22N-NETWORTH                   PIC 9(15)V99.                   
           05  TX22N-CASH-COLLECTED-SGN         PIC X.                          
           05  TX22N-CASH-COLLECTED             PIC 9(15)V99.                   
           05  TX22N-OTB-COLLECTED-SGN          PIC X.                          
           05  TX22N-OTB-COLLECTED              PIC 9(15)V99.                   
           05  TX22N-NET-TD-BALANCE-SGN         PIC X.                          
           05  TX22N-NET-TD-BALANCE             PIC 9(15)V99.                   
           05  TX22N-NETWORTH-MKTVAL-SGN        PIC X.                          
           05  TX22N-NETWORTH-MKTVAL            PIC 9(15)V99.                   
           05  TX22N-CASH-MMF-MKTVAL-SGN        PIC X.                          
           05  TX22N-CASH-MMF-MKTVAL            PIC 9(15)V99.                   
           05  TX22N-OPTION-MKTVAL-SGN          PIC X.                          
           05  TX22N-OPTION-MKTVAL              PIC 9(15)V99.                   
           05  TX22N-OPTION-IN-THE-MONEY-SGN    PIC X.                          
           05  TX22N-OPTION-IN-THE-MONEY-AMT    PIC 9(15)V99.                   
           05  TX22N-MEMO-ADJUSTMENTS-SGN       PIC X.                          
           05  TX22N-MEMO-ADJUSTMENTS           PIC 9(15)V99.                   
           05  TX22N-BUY-POWR-MGN-SGN           PIC X.                          
           05  TX22N-BUY-POWR-MGN-A             PIC 9(15)V99.                   
           05  TX22N-BUY-POWER-CORP-SGN         PIC X.                          
           05  TX22N-BUY-POWER-CORP             PIC 9(15)V99.                   
           05  TX22N-BUY-POWER-MUNI-SGN         PIC X.                          
           05  TX22N-BUY-POWER-MUNI             PIC 9(15)V99.                   
           05  TX22N-BUY-POWER-GOVT-SGN         PIC X.                          
           05  TX22N-BUY-POWER-GOVT             PIC 9(15)V99.                   
           05  TX22N-HOUSECALL-SURP-SGN         PIC X.                          
           05  TX22N-HOUSECALL-SURP             PIC 9(15)V99.                   
           05  TX22N-NYSECALL-SURP-SGN          PIC X.                          
           05  TX22N-NYSECALL-SURP              PIC 9(15)V99.                   
           05  TX22N-FEDCALL-SMA-SGN            PIC X.                          
           05  TX22N-FEDCALL-SMA                PIC 9(15)V99.                   
           05  TX22N-MIN-EQUITY-CALL-SGN        PIC X.                          
           05  TX22N-MIN-EQUITY-CALL            PIC 9(15)V99.                   
           05  TX22N-CORE-MM-AMT-SGN            PIC X.                          
           05  TX22N-CORE-MM-AMT                PIC 9(15)V99.                   
           05  TX22N-MGN-EQUITY-SGN             PIC X.                          
           05  TX22N-MGN-EQUITY                 PIC 9(15)V99.                   
           05  TX22N-LIQUIDATING-EQUITY-SGN     PIC X.                          
           05  TX22N-MGN-LIQUIDATING-EQUITY     PIC 9(15)V99.                   
           05  TX22N-MGN-EQUITY-PERCENT         PIC 9(3)V99.                    
           05  TX22N-FEDCALL-REDUCTION-SGN      PIC X.                          
           05  TX22N-FEDCALL-REDUCTION          PIC 9(15)V99.                   
           05  TX22N-HOUSECALL-REDUCTION-SGN    PIC X.                          
           05  TX22N-HOUSECALL-REDUCTION        PIC 9(15)V99.                   
           05  TX22N-NYSECALL-REDUCTION-SGN     PIC X.                          
           05  TX22N-NYSECALL-REDUCTION         PIC 9(15)V99.                   
           05  TX22N-OTB-UNCOLLECTED-SGN        PIC X.                          
           05  TX22N-OTB-UNCOLLECTED            PIC 9(15)V99.                   
           05  TX22N-MIN-ECALL-REDUCTION-SGN    PIC X.                          
           05  TX22N-MIN-ECALL-REDUCTION        PIC 9(15)V99.                   
           05  TX22N-TFR-LEGEND-CODE            PIC X.                          
           05  TX22N-MGN-PAPERS-SW              PIC X.                          
           05  TX22N-POSITION-SW                PIC X.                          
           05  TX22N-UNPRICED-POSITION-SW       PIC X.                          
           05  TX22N-EMPLOYEE-ACCT-SW           PIC X.                          
           05  TX22N-TYPE-OF-ACCT-SW            PIC X.                          
           05  TX22N-SHORT-POSITION-SW          PIC X.                          
           05  TX22N-LONG-POSITION-SW           PIC X.                          
           05  TX22N-MEMO-ENTRIES-SW            PIC X.                          
           05  TX22N-DAY-TRADES-SW              PIC X.                          
           05  TX22N-POSSIBLE-LIQ-SW            PIC X.                          
           05  TX22N-MIN-ECALL-TRANS-SW         PIC X.                          
           05  TX22N-RECORD-COUNT               PIC 9(3).                       
           05  TX22N-SUPER-BRH                  PIC X(03).                      
           05  TX22N-BUY-POWR-CSH-SGN           PIC X.                          
           05  TX22N-BUY-POWR-CSH-A             PIC 9(15)V99.                   
           05  TX22N-BUY-POWR-CMGN-SGN          PIC X.                          
           05  TX22N-BUY-POWR-CMGN-A            PIC 9(15)V99.                   
           05  TX22N-BUY-POWR-NMGN-SGN          PIC X.                          
           05  TX22N-BUY-POWR-NMGN-A            PIC 9(15)V99.                   
           05  TX22N-CUST-FACE-NETWORTH-SGN     PIC X.                          
           05  TX22N-CUST-FACE-NETWORTH-A       PIC 9(15)V99.                   
           05  TX22N-ACCOUNT-TYPE-INFO-1.                                       
               10  TX22N-ACCT-TYPE-1            PIC X(01).                      
               10  TX22N-MKTVAL-SGN-1           PIC X.                          
               10  TX22N-MKTVAL-1               PIC 9(15)V99.                   
               10  TX22N-TD-BALANCE-SGN-1       PIC X.                          
               10  TX22N-TD-BALANCE-1           PIC 9(15)V99.                   
               10  TX22N-SD-BALANCE-SGN-1       PIC X.                          
               10  TX22N-SD-BALANCE-1           PIC 9(15)V99.                   
           05  TX22N-ACCOUNT-TYPE-INFO-2.                                       
               10  TX22N-ACCT-TYPE-2            PIC X(01).                      
               10  TX22N-MKTVAL-SGN-2           PIC X.                          
               10  TX22N-MKTVAL-2               PIC 9(15)V99.                   
               10  TX22N-TD-BALANCE-SGN-2       PIC X.                          
               10  TX22N-TD-BALANCE-2           PIC 9(15)V99.                   
               10  TX22N-SD-BALANCE-SGN-2       PIC X.                          
               10  TX22N-SD-BALANCE-2           PIC 9(15)V99.                   
           05  TX22N-ACCOUNT-TYPE-INFO-3.                                       
               10  TX22N-ACCT-TYPE-3            PIC X(01).                      
               10  TX22N-MKTVAL-SGN-3           PIC X.                          
               10  TX22N-MKTVAL-3               PIC 9(15)V99.                   
               10  TX22N-TD-BALANCE-SGN-3       PIC X.                          
               10  TX22N-TD-BALANCE-3           PIC 9(15)V99.                   
               10  TX22N-SD-BALANCE-SGN-3       PIC X.                          
               10  TX22N-SD-BALANCE-3           PIC 9(15)V99.                   
           05  TX22N-ACCOUNT-TYPE-INFO-4.                                       
               10  TX22N-ACCT-TYPE-4            PIC X(01).                      
               10  TX22N-MKTVAL-SGN-4           PIC X.                          
               10  TX22N-MKTVAL-4               PIC 9(15)V99.                   
               10  TX22N-TD-BALANCE-SGN-4       PIC X.                          
               10  TX22N-TD-BALANCE-4           PIC 9(15)V99.                   
               10  TX22N-SD-BALANCE-SGN-4       PIC X.                          
               10  TX22N-SD-BALANCE-4           PIC 9(15)V99.                   
           05  TX22N-ACCOUNT-TYPE-INFO-5.                                       
               10  TX22N-ACCT-TYPE-5            PIC X(01).                      
               10  TX22N-MKTVAL-SGN-5           PIC X.                          
               10  TX22N-MKTVAL-5               PIC 9(15)V99.                   
               10  TX22N-TD-BALANCE-SGN-5       PIC X.                          
               10  TX22N-TD-BALANCE-5           PIC 9(15)V99.                   
               10  TX22N-SD-BALANCE-SGN-5       PIC X.                          
               10  TX22N-SD-BALANCE-5           PIC 9(15)V99.                   
           05  TX22N-ACCOUNT-TYPE-INFO-6.                                       
               10  TX22N-ACCT-TYPE-6            PIC X(01).                      
               10  TX22N-MKTVAL-SGN-6           PIC X.                          
               10  TX22N-MKTVAL-6               PIC 9(15)V99.                   
               10  TX22N-TD-BALANCE-SGN-6       PIC X.                          
               10  TX22N-TD-BALANCE-6           PIC 9(15)V99.                   
               10  TX22N-SD-BALANCE-SGN-6       PIC X.                          
               10  TX22N-SD-BALANCE-6           PIC 9(15)V99.                   
           05  TX22N-ACCOUNT-TYPE-INFO-7.                                       
               10  TX22N-ACCT-TYPE-7            PIC X(01).                      
               10  TX22N-MKTVAL-SGN-7           PIC X.                          
               10  TX22N-MKTVAL-7               PIC 9(15)V99.                   
               10  TX22N-TD-BALANCE-SGN-7       PIC X.                          
               10  TX22N-TD-BALANCE-7           PIC 9(15)V99.                   
               10  TX22N-SD-BALANCE-SGN-7       PIC X.                          
               10  TX22N-SD-BALANCE-7           PIC 9(15)V99.                   
           05  TX22N-ACCOUNT-TYPE-INFO-8.                                       
               10  TX22N-ACCT-TYPE-8            PIC X(01).                      
               10  TX22N-MKTVAL-SGN-8           PIC X.                          
               10  TX22N-MKTVAL-8               PIC 9(15)V99.                   
               10  TX22N-TD-BALANCE-SGN-8       PIC X.                          
               10  TX22N-TD-BALANCE-8           PIC 9(15)V99.                   
               10  TX22N-SD-BALANCE-SGN-8       PIC X.                          
               10  TX22N-SD-BALANCE-8           PIC 9(15)V99.                   
           05  TX22N-ACCOUNT-TYPE-INFO-9.                                       
               10  TX22N-ACCT-TYPE-9            PIC X(01).                      
               10  TX22N-MKTVAL-SGN-9           PIC X.                          
               10  TX22N-MKTVAL-9               PIC 9(15)V99.                   
               10  TX22N-TD-BALANCE-SGN-9       PIC X.                          
               10  TX22N-TD-BALANCE-9           PIC 9(15)V99.                   
               10  TX22N-SD-BALANCE-SGN-9       PIC X.                          
               10  TX22N-SD-BALANCE-9           PIC 9(15)V99.                   
           05  TX22N-ACCOUNT-TYPE-INFO-10.                                      
               10  TX22N-ACCT-TYPE-10           PIC X(01).                      
               10  TX22N-MKTVAL-SGN-10          PIC X.                          
               10  TX22N-MKTVAL-10              PIC 9(15)V99.                   
               10  TX22N-TD-BALANCE-SGN-10      PIC X.                          
               10  TX22N-TD-BALANCE-10          PIC 9(15)V99.                   
               10  TX22N-SD-BALANCE-SGN-10      PIC X.                          
               10  TX22N-SD-BALANCE-10          PIC 9(15)V99.                   
*****************                                                               
***************** NEW FIELDS                                                    
           05  TX22N-ACCOUNT-OTHER-INFO.                                        
               10  TX22N-PORT-MGN-IND           PIC X(01).                      
               10  TX22N-BORR-FULLY-PD-IND      PIC X(01).                      
               10  TX22N-BALS-REL-TYPE          PIC X(01).                      
               10  TX22N-INTL-IND               PIC X(01).                      
               10  TX22N-TRUST-ACCT-IND         PIC X(01).                      
               10  TX22N-NPL-ACCT-IND           PIC X(01).                      
               10  TX22N-NET-STL-IND            PIC X(01).                      
               10  TX22N-WHEN-ISSD-IND          PIC X(01).                      
               10  TX22N-TYP5-IND               PIC X(01).                      
               10  TX22N-AVAIL-BORR-SGN         PIC X.                          
               10  TX22N-AVAIL-BORR             PIC 9(15)V9(02).                
               10  TX22N-CSH-AVAIL-WTHD-SGN     PIC X.                          
               10  TX22N-CSH-AVAIL-WTHD         PIC 9(15)V9(02).                
               10  TX22N-STL-CSH-SGN            PIC X.                          
               10  TX22N-STL-CSH                PIC 9(15)V9(02).                
               10  TX22N-UNSTL-CSH-CR-SGN       PIC X.                          
               10  TX22N-UNSTL-CSH-CR           PIC 9(15)V9(02).                
               10  TX22N-UNSTL-CSH-DB-SGN       PIC X.                          
               10  TX22N-UNSTL-CSH-DB           PIC 9(15)V9(02).                
               10  TX22N-AVAIL-PAY-SGN          PIC X.                          
               10  TX22N-AVAIL-PAY              PIC 9(15)V9(02).                
JL0001         10  TX22N-PRIMARY-FUND-AMT-SGN   PIC X.                          
JL0001         10  TX22N-PRIMARY-FUND-AMT       PIC 9(15)V9(02).                
JL0001         10  TX22N-NON-CORE-MMKT-AMT-SGN  PIC X.                          
JL0001         10  TX22N-NON-CORE-MMKT-AMT      PIC 9(15)V9(02).                
JL0001         10  FILLER                       PIC X(237).                     
